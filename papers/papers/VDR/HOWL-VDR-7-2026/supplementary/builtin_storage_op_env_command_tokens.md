# VDR-Prolog: Unified Weight Storage, Operational Environments, and Command Tokens
## Completing the Architecture

---

## 1. Everything in KBs: Model Weights and Data Weights

### 1.1 The Fat Struct Principle

A KB entry does not need every field populated. The KB is a fat struct — it has slots for everything any entry might need, and any given entry uses only the slots relevant to it. An atom fact about Bob's age uses the value slot and nothing else. A model weight uses the value slot, the gradient history slot, the initialization provenance slot, and the denominator complexity slot. A raw data point uses the value slot, the source slot, the timestamp slot, and the confidence slot.

```
KBEntry = struct {
    // Identity
    id: Text,
    predicate: Text,
    args: []Term,
    
    // Value (always present)
    value: Term,
    
    // Provenance (populated when tracked)
    derived_from: ?Derivation,
    source: ?Text,
    created_at: ?timestamp,
    modified_at: ?timestamp,
    created_by: ?Text,
    
    // Weight provenance (populated for model parameters)
    initialization: ?InitRecord,
    gradient_history: ?[]GradientRecord,
    update_history: ?[]UpdateRecord,
    checkpoint_values: ?[]CheckpointRecord,
    denominator_complexity: ?DenomRecord,
    
    // Data provenance (populated for data entries)
    data_source: ?DataSourceRecord,
    preprocessing_chain: ?[]TransformRecord,
    confidence: ?fraction,
    quality_flags: ?[]Text,
    
    // Versioning
    version: ?i32,
    version_history: ?[]VersionRecord,
    
    // Weighting
    data_weight: ?fraction,       // how much this data point matters in training
    provenance_weight: ?fraction, // confidence in the derivation chain
    
    // Constraints
    local_constraints: ?[]Constraint,
    
    // KB membership
    kb: Text,
    tags: []Text,
};
```

Most entries leave most fields null. A simple binding like `bob_age = 32` populates id, predicate, value, kb, and maybe created_at. A model weight populates the weight provenance fields. A training data point populates the data provenance fields. The struct is the same. The populated fields vary.

### 1.2 Data Weights in KBs

Every data point used for training has a weight — how much it contributes to the loss and gradient. In standard ML, these weights are floats buried in a DataLoader. In VDR-Prolog, they are exact fractions stored as KB facts alongside the data itself.

```
Fact: training_data("sample_042", 
    input(token_seq([42, 17, 93])),
    target(token(5)),
    data_weight(fraction(1, 100)),
    source("corpus_a"),
    quality(verified),
    version(1)).
```

The data weight is queryable, modifiable, and constrained:

```
Rule: total_data_weight(Total) :-
    findall(W, training_data(_, _, _, data_weight(W), _, _, _), Ws),
    vdr_sum(Ws, Total).

Constraint: data_weights_sum_to_one(
    condition(total_data_weight(fraction(1, 1))),
    on_violation("warn")).
```

If you upweight one sample, the system can verify that the total still sums to 1 (or whatever the normalization target is). If you flag a sample as low quality and reduce its weight, the provenance records why, when, and by whom.

### 1.3 Provenance Weights

Not all derivations are equally trustworthy. A value derived from exact VDR arithmetic has provenance weight 1 — the derivation is exact and verifiable. A value derived from a truncated Taylor series has provenance weight proportional to the precision — 100 digits means high confidence, 5 digits means low. A value imported from an external source has provenance weight based on the source's reliability.

```
Fact: provenance_weight(
    attention_weight(doc(42), pos(3), pos(7)),
    fraction(1, 1),
    reason("exact VDR softmax, sum verified to 1")).

Fact: provenance_weight(
    exp_value(x, depth(12)),
    fraction(999999999999, 1000000000000),
    reason("Taylor truncation at depth 12, ~36 correct digits")).

Fact: provenance_weight(
    external_constant("laporta_I4_master_1"),
    fraction(1, 1),
    reason("known to 4800 digits, imported as exact rational")).

Fact: provenance_weight(
    user_stated("bob_age", 32),
    fraction(1, 2),
    reason("user-stated, not independently verified")).
```

Provenance weights propagate through derivation chains:

```
Rule: effective_provenance_weight(Value, Weight) :-
    provenance_weight(Value, W, _),
    Weight = W.

Rule: effective_provenance_weight(Value, Weight) :-
    derived_from(Value, _, Sources),
    findall(W, (member(S, Sources), effective_provenance_weight(S, W)), Ws),
    vdr_min_list(Ws, Weight).
    // The chain is as strong as its weakest link
```

A value derived from one exact source and one user-stated source has provenance weight 1/2 — the minimum of the chain. The system knows which parts of its knowledge are exact and which are estimated.

---

## 2. Operational Environments

### 2.1 The Concept

An operational environment is a compute context where operational primitives execute. It is not the LLM's process. It is a separate, sandboxed, inspectable execution context.

```
OperationalEnv = struct {
    id: Text,
    type: enum { docker, vm, local, ssh_remote },
    
    // Docker-specific
    image: ?Text,              // "ubuntu:24.04", "alpine:3.19", "python:3.8-slim"
    container_id: ?Text,       // runtime container ID
    
    // VM-specific
    vm_id: ?Text,
    vm_image: ?Text,
    
    // SSH-specific
    host: ?Text,
    port: ?i32,
    credential: ?Text,         // reference to credential in KB
    
    // Local-specific
    working_dir: ?Text,
    
    // Common
    status: enum { stopped, starting, running, error },
    startup_script: ?Text,     // commands to run on creation
    installed_packages: []Text,
    env_vars: dict,
    resource_limits: ResourceLimits,
    created_at: timestamp,
    last_active: timestamp,
    
    // KB reference
    kb: Text,                  // this env's KB for tracking state
    grants: []Text,            // which grants authorize operations here
};

ResourceLimits = struct {
    max_cpu_seconds: ?i32,
    max_memory_mb: ?i32,
    max_disk_mb: ?i32,
    max_network_bytes: ?i32,
    max_processes: ?i32,
};
```

### 2.2 Environment Types

**Docker container.** The default. A fresh Ubuntu 24.04 or Alpine container with a declared set of packages. The LLM can install additional packages via the operational primitive system (with the appropriate grant). The container is ephemeral — it can be destroyed and recreated from the spec. All persistent state lives in the KB, not in the container.

```
Fact: env("env_vdr_test", 
    type(docker),
    image("python:3.8-slim"),
    startup_script("pip install fractions"),
    status(running),
    kb("kb_env_vdr_test"),
    grants(["alice_project_exec", "alice_project_fs"])).
```

**VM.** For heavier workloads or when Docker is not available. Same interface — the system connects to it, runs commands, captures output.

**Local execution.** For trusted environments where sandboxing is unnecessary. The operational primitives run directly on the host system. Requires explicit local_execution grant with strong constraints.

**SSH remote.** Connect to a remote machine via SSH with public key authentication. The credential is a reference to a key stored in the credential KB.

```
Fact: credential("alice_gpu_server",
    type(ssh_pubkey),
    host("gpu01.lab.example.com"),
    port(22),
    username("alice"),
    key_ref("ssh_key_alice_gpu01"),
    issued_at(timestamp(2026, 5, 1)),
    expires_at(timestamp(2026, 6, 1))).
```

### 2.3 Unified Interface

Every environment type presents the same interface to the operational primitive system:

```
EnvInterface = trait {
    exec(command: Text, args: []Text) → ExecResult,
    upload(local_path: Text, remote_path: Text) → TransferResult,
    download(remote_path: Text, local_path: Text) → TransferResult,
    shell(command: Text) → ShellResult,
    file_read(path: Text) → Content,
    file_write(path: Text, content: Content) → WriteResult,
    list_dir(path: Text) → []DirEntry,
    process_start(command: Text) → TaskId,
    process_poll(task_id: TaskId) → TaskStatus,
    process_output(task_id: TaskId) → (stdout: Text, stderr: Text),
};
```

Whether the backend is Docker, a VM, SSH, or local — the LLM uses the same primitives. The environment selection is a configuration fact in the KB. Switching environments is changing which env KB is active.

### 2.4 Environment as KB

Each operational environment has its own KB tracking:

```
KB: kb_env_vdr_test
  facts:
    env_type: docker
    env_image: python:3.8-slim
    env_status: running
    installed: [fractions, pytest]
    
  execution_log:
    exec_001: exec_python("test_basic.py") → 12 passed, 0 failed (3.2s)
    exec_002: exec_python("test_layer_1.py") → 15 passed, 0 failed (8.1s)
    exec_003: fs_write("gym/gym_16_graph_theory.py", content) → ok
    
  uploaded_files:
    "gym/gym_16_graph_theory.py" → version 1, uploaded at turn 52
    "gym/gym_17_game_theory.py" → version 1, uploaded at turn 52
    
  task_history:
    task_001: pytest gym/ → completed, 157 passed, 5 failed
```

---

## 3. Command Tokens

### 3.1 The Concept

Currently, LLMs produce output as a stream of text tokens. Every character, every word, every code block is a token prediction. This is wasteful when the output is a structured command rather than natural language.

Command tokens are a parallel output channel where the LLM issues structured commands instead of generating text. The command is not a text string that gets parsed. It is a structured token that directly invokes a primitive or operational function.

### 3.2 Command Token Types

```
CommandToken = enum {
    // Pure primitive invocation
    PURE_FN(name: Text, args: []Term) → Term,
    
    // Operational primitive invocation
    OP_FN(name: Text, args: []Term, env: Text, grant: Text) → TaskId,
    
    // KB operations
    KB_ASSERT(kb: Text, fact: Fact),
    KB_RETRACT(kb: Text, fact: Fact),
    KB_QUERY(kb: Text, predicate: Text, args: []Term) → []Result,
    
    // Environment operations
    ENV_EXEC(env: Text, command: Text, args: []Text) → TaskId,
    ENV_UPLOAD(env: Text, content: Content, remote_path: Text) → TransferResult,
    ENV_DOWNLOAD(env: Text, remote_path: Text) → Content,
    
    // Context operations
    CTX_ACTIVATE(kb: Text),
    CTX_DEACTIVATE(kb: Text),
    CTX_SNAPSHOT(name: Text),
    
    // Versioning
    VERSION_CREATE(project: Text, name: Text, data: Term),
    VERSION_TAG(project: Text, version: i32, tag: Text),
    
    // Flow control
    WAIT(task_id: TaskId),
    POLL(task_id: TaskId),
    STORE_RESULT(task_id: TaskId, kb: Text, key: Text),
    
    // Direct output (bypass LLM token generation)
    DIRECT_OUTPUT(source: Text),      // serve KB data or file directly
    ATTACHMENT(source: Text, name: Text), // attach file to response
};
```

### 3.3 How the LLM Uses Command Tokens

The LLM's output stream interleaves text tokens and command tokens:

```
Output stream:

[TEXT] "I'll write the gym script, upload it to the test environment, "
[TEXT] "and run the tests."
[NEWLINE]
[CMD] ENV_UPLOAD(env="env_vdr_test", 
                 content=<generated script>, 
                 remote_path="/workspace/gym/gym_16_graph_theory.py")
[CMD] ENV_EXEC(env="env_vdr_test", 
               command="python3", 
               args=["/workspace/gym/gym_16_graph_theory.py"])
[CMD] STORE_RESULT(task_id=<from exec>, 
                   kb="kb_vdr_gyms", 
                   key="gym_16_result_v1")
[TEXT] "The script is uploaded and running. I'll report results "
[TEXT] "when it completes."
```

The text tokens are rendered as conversation text. The command tokens are executed by the primitive system. The user sees the text and the command outcomes. The commands themselves can be shown (for transparency) or hidden (for cleanliness), controlled by a user preference.

### 3.4 Command Token Permissions

Command tokens are subject to the same positive grant system as operational primitives:

```
Rule: can_issue_command(Cmd) :-
    command_type(Cmd, Type),
    command_env(Cmd, Env),
    active_grants(Grants),
    member(G, Grants),
    grant_covers_command(G, Type, Env).
```

The LLM cannot issue a command token for which there is no valid grant. If the LLM tries to upload a file to an environment it does not have write access to, the command token is rejected before execution. The rejection is logged and surfaced to the user.

### 3.5 Scratchpad vs Output

The LLM has two output channels:

**User-facing output.** Text tokens and direct output commands. This is what the user sees.

**Scratchpad.** Internal reasoning, intermediate computations, command sequences. This is visible to the owner but hidden from end users by default.

Command tokens in the scratchpad are still executed but their results are not surfaced unless the user asks:

```
Scratchpad:
  [CMD] PURE_FN("list_sort", [[47, 3, 91, 15], ascending]) → [3, 15, 47, 91]
  [CMD] PURE_FN("vdr_mean", [[3/7, 1/2, 5/11]]) → 191/462
  [CMD] KB_QUERY("kb_characters_b", "bob_age", [Age]) → Age = 59

User-facing:
  [TEXT] "The average of those fractions is 191/462, "
  [TEXT] "and Bob is 59 in the London story."
```

The scratchpad computation is exact (primitives), the data retrieval is exact (KB query), and the user-facing text frames the results. The user can request to see the scratchpad: "/show scratchpad" surfaces the command tokens and their results.

---

## 4. Versioning in Projects

### 4.1 Version as KB Fact

Every artifact in a project can be versioned. A version is a snapshot of the artifact at a point in time, stored as a KB fact.

```
Fact: version("project_vdr", "gym_16_script", 
    version_num(1),
    content_ref("kb_vdr_gyms/gym_16_v1"),
    created_at(timestamp(2026, 5, 16, 14, 30, 0)),
    created_by("system"),
    tag("initial"),
    parent_version(none),
    test_result("19/20 passed"),
    notes("maxflow BFS has a bug")).

Fact: version("project_vdr", "gym_16_script",
    version_num(2),
    content_ref("kb_vdr_gyms/gym_16_v2"),
    created_at(timestamp(2026, 5, 16, 15, 0, 0)),
    created_by("system"),
    tag("maxflow_fixed"),
    parent_version(1),
    test_result("20/20 passed"),
    notes("fixed BFS loop termination")).
```

### 4.2 Version Operations

```
// Create new version
[CMD] VERSION_CREATE(
    project="project_vdr", 
    artifact="gym_16_script",
    content=<script content>,
    notes="fixed BFS loop termination")

// Tag a version
[CMD] VERSION_TAG(
    project="project_vdr",
    artifact="gym_16_script",
    version=2,
    tag="release")

// Retrieve specific version
[CMD] KB_QUERY("kb_vdr_gyms", 
    version("project_vdr", "gym_16_script", version_num(2), content_ref(Ref), _, _, _, _, _, _))
[CMD] DIRECT_OUTPUT(Ref)

// Diff between versions
[CMD] PURE_FN("diff", [version_content(1), version_content(2)]) → structured diff

// Rollback
[CMD] VERSION_CREATE(
    project="project_vdr",
    artifact="gym_16_script",
    content=version_content(1),
    notes="rollback to v1",
    parent_version=2)
```

### 4.3 Version History as KB

```
KB: kb_vdr_gyms_versions
  version("gym_16_script", 1, "initial", "19/20", timestamp(...))
  version("gym_16_script", 2, "maxflow_fixed", "20/20", timestamp(...))
  version("gym_17_script", 1, "initial", "24/24", timestamp(...))
  version("gym_18_script", 1, "initial", "27/27", timestamp(...))
  
  latest("gym_16_script", 2)
  latest("gym_17_script", 1)
  latest("gym_18_script", 1)
  
  tagged("gym_16_script", 2, "release")
```

Queryable:

```
?- version("gym_16_script", V, _, "20/20", _).
% Which versions of gym_16 had all tests passing?

?- latest(Artifact, V), version(Artifact, V, _, Result, _), 
   not(Result = "all_passed").
% Which artifacts have latest versions with failures?

?- tagged(Artifact, V, "release").
% Which artifacts have tagged releases?
```

---

## 5. The Complete Operational Flow

A concrete example of the LLM using everything together:

```
User: "Write gym_24 for representation theory, run it, 
       and store the results"

LLM reasoning (scratchpad):
  [CMD] KB_QUERY("kb_project_vdr", constraint("python_38_compat")) → active
  [CMD] KB_QUERY("kb_project_vdr", constraint("30_sec_runtime")) → active
  [CMD] KB_QUERY("kb_vdr_gyms", latest_gym_number) → 23
  
LLM output:
  [TEXT] "Writing gym_24_representation_theory.py with Python 3.8 
          compatibility and under 30-second runtime constraint."

LLM generates script (text tokens for the code)...

  [CMD] ENV_UPLOAD(
      env="env_vdr_test",
      content=<generated gym script>,
      remote_path="/workspace/gym/gym_24_representation_theory.py")
  
  [TEXT] "Script uploaded. Running now."
  
  [CMD] ENV_EXEC(
      env="env_vdr_test",
      command="python3",
      args=["/workspace/gym/gym_24_representation_theory.py"])
  → task_id = "task_047"
  
  [CMD] STORE_RESULT(
      task_id="task_047",
      kb="kb_vdr_gyms",
      key="gym_24_result_v1")
  
  [TEXT] "Test running in background as task_047."

[... conversation continues ...]

[Task completes]

LLM (next turn):
  [CMD] POLL("task_047") → completed
  [CMD] KB_QUERY("kb_vdr_gyms", "gym_24_result_v1") → result
  
  [TEXT] "Gym 24 finished: "
  [DIRECT_OUTPUT] kb://kb_vdr_gyms/gym_24_result_v1
  
  [TEXT] "14 passed, 0 failed. Storing as version 1."
  
  [CMD] VERSION_CREATE(
      project="project_vdr",
      artifact="gym_24_script",
      content=<script content>,
      notes="initial, 14/14 passed")
  
  [CMD] KB_ASSERT("kb_vdr_gyms",
      gym_result("gym_24", "representation_theory", 14, 14, 0))
  
  [CMD] KB_ASSERT("kb_project_vdr",
      set_binding("total_tests", number(719)))  // 705 + 14
  
  [TEXT] "Updated project stats: 719 total tests, 0 VDR errors."
  [ATTACHMENT] fs://env_vdr_test/workspace/gym/gym_24_representation_theory.py
```

Every step is a command token or text. The command tokens execute exact operations. The results are stored in KBs with versioning. The project working data is updated. The file is available as a direct download. The user sees the framing text and the results. Everything is logged, provenance-tracked, and queryable.

---

## 6. I/O Handling for Long Operations

### 6.1 Chunked Output

Long-running operations produce output over time. The system handles this in chunks:

```
Task: compile_large_project → running for 45 seconds

Chunk 1 (at 10s): "Compiling module 1/12..."
Chunk 2 (at 20s): "Compiling module 5/12..."
Chunk 3 (at 35s): "Compiling module 10/12... 2 warnings"
Chunk 4 (at 45s): "Complete. 12/12 modules, 2 warnings, 0 errors"

Each chunk stored:
  task_output("task_048", chunk(1), timestamp(10s), "Compiling module 1/12...")
  task_output("task_048", chunk(2), timestamp(20s), "Compiling module 5/12...")
  ...
```

### 6.2 Streaming vs Polling

Two modes for consuming task output:

**Polling.** The LLM checks on each turn whether tasks have new output. This is the default for background tasks. The user is not interrupted.

**Streaming.** For tasks the user is actively watching, output chunks are surfaced as they arrive, interleaved with the conversation.

```
User: "/watch task_048"

System: switches task_048 to streaming mode

[Chunk arrives] "Compiling module 5/12..."
[User types something]
LLM responds to user
[Chunk arrives] "Compiling module 10/12... 2 warnings"
LLM: "The compilation is still running — 10 of 12 modules done, 
      2 warnings so far. Shall I show the warnings?"
```

### 6.3 Turn-Like Processing

Task output chunks are processed like conversation turns. Each chunk can trigger:
- Reminder checks (did the output contain an error pattern?)
- Constraint checks (did the output exceed a resource limit?)
- KB updates (store intermediate results)
- Watch triggers (notify if condition met)

```
Watch: watch("compile_error",
    condition(task_output(_, _, _, Content), contains(Content, "error")),
    message("Compilation error detected"),
    watch_type(on_change)).
```

If any chunk contains "error," the watch fires immediately, regardless of whether the user is actively watching the task.

---

## 7. Summary: The Complete System

```
┌─────────────────────────────────────────────────┐
│                   USER                           │
│  Selects KBs, issues commands, receives output   │
│  Direct downloads, attachments, surfaced data    │
└────────────────────┬────────────────────────────┘
                     │
┌────────────────────┴────────────────────────────┐
│              LLM + COMMAND TOKENS                │
│  Text tokens (conversation)                      │
│  Command tokens (primitives, ops, KB, versioning)│
│  Scratchpad (internal reasoning with primitives) │
└────────────────────┬────────────────────────────┘
                     │
┌────────────────────┴────────────────────────────┐
│              VDR-PROLOG KB LAYER                 │
│  Everything is a KB                              │
│  Facts, rules, constraints, working data         │
│  Tags, groups, views, versions                   │
│  Reminders, watches, prompted constraints        │
│  Pure primitive results stored as facts           │
│  Operational results stored as facts              │
│  Provenance weights, data weights                │
└────────────────────┬────────────────────────────┘
                     │
┌────────────────────┴────────────────────────────┐
│           PRIMITIVE LAYER                        │
│  Pure: string, list, math, set, dict, stats,     │
│        linear algebra, graph, regex, format       │
│  Operational: filesystem, compile, execute,       │
│               lint, network, process              │
│  All gated by positive credential grants          │
└────────────────────┬────────────────────────────┘
                     │
┌────────────────────┴────────────────────────────┐
│         OPERATIONAL ENVIRONMENTS                 │
│  Docker containers (default sandbox)             │
│  VMs (heavy workloads)                           │
│  Local execution (trusted)                       │
│  SSH remotes (distributed)                       │
│  Unified interface: exec, upload, download       │
│  Async task management with KB-stored results    │
└─────────────────────────────────────────────────┘
```

Every box is made of KBs. Every arrow passes exact data. Every operation is logged. Every result is versioned. Every constraint is checked. Every grant is verified. Everything is queryable. Everything is surfaceable. Everything is downloadable.

The LLM generates text for humans and command tokens for machines. The primitives compute exactly. The environments execute safely. The KBs store everything. The constraints enforce everything. The user sees everything they are authorized to see, and can download anything by address without the LLM regenerating it.

That is the complete system.
