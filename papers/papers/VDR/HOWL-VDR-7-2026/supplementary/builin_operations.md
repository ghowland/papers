# VDR-Prolog Operational Primitives
## Constrained Side-Effecting Operations With Credential Gating and Async Execution

---

## 1. The Distinction: Pure vs Operational

The previous report defined pure primitives — functions that always produce the same output from the same input, have no side effects, and terminate in bounded time. String reversal, list sorting, exact arithmetic. These are the safe core.

Operational primitives are different. They interact with the outside world. They read and write files. They compile code. They execute scripts. They download content. They create directories. They take time. They can fail for reasons unrelated to their inputs — disk full, network down, permission denied, process killed.

These operations are essential for a working system. An LLM that can reason about code but cannot compile it, can discuss files but cannot read them, can plan a project but cannot create directories — that LLM is a consultant, not an engineer. It gives advice. It does not do work.

But operational primitives are dangerous in a way pure primitives are not. A pure function that reverses a string cannot delete your files. An operational primitive that executes a script can do anything the script does. The constraint system must handle this difference explicitly.

---

## 2. Positive Constraint Gating

Every operational primitive requires a positive constraint to execute. This inverts the default. Pure primitives are allowed unless a constraint prohibits them. Operational primitives are prohibited unless a constraint explicitly allows them.

```
Rule: can_execute(Op) :-
    operational_primitive(Op),
    positive_grant(Op, Grant),
    grant_valid(Grant),
    grant_covers(Grant, Op).

Rule: can_execute(Op) :-
    pure_primitive(Op).
    % Pure primitives are always allowed (subject to normal constraints)

Rule: execute(Op) :-
    can_execute(Op), !,
    run_operational(Op).

Rule: execute(Op) :-
    not(can_execute(Op)),
    log(blocked(Op, "no valid positive grant")),
    fail.
```

A positive grant is a structured credential:

```
Grant = struct {
    name: Text,
    operation_class: Text,      // "filesystem", "compile", "execute", "network"
    allowed_operations: []Text,  // specific ops within class
    location: Text,             // path, URL, or scope
    credential: Text,           // auth token or key reference
    issued_by: Text,            // who granted this
    issued_at: i32,             // timestamp
    expires_at: i32,            // expiration timestamp
    max_uses: ?i32,             // optional use limit
    uses_remaining: ?i32,       // decremented on use
    constraints: []Constraint,  // additional constraints on use
};
```

Example:

```
positive_grant("alice_project_fs", 
    operation_class("filesystem"),
    allowed_operations(["read", "write", "create_dir", "list_dir"]),
    location("/home/alice/projects/vdr/"),
    credential(token("fs_alice_2026_abc123")),
    issued_by("alice"),
    issued_at(timestamp(2026, 5, 16, 10, 0, 0)),
    expires_at(timestamp(2026, 5, 17, 10, 0, 0)),
    max_uses(1000),
    uses_remaining(1000),
    constraints([
        constraint("no_delete", condition(op \= "delete"), on_violation("block")),
        constraint("no_hidden_files", condition(not(starts_with(filename, "."))), on_violation("block")),
        constraint("max_file_size", condition(size =< 10_000_000), on_violation("block"))
    ])
).
```

This grant says: Alice has authorized filesystem operations (read, write, create_dir, list_dir but not delete) in her VDR project directory, using a specific token, for 24 hours, up to 1000 operations, with additional constraints against deleting anything, touching hidden files, or writing files larger than 10MB. Every field is a Prolog fact. Every constraint is verifiable. The grant is inspectable, auditable, and revocable.

---

## 3. Operational Primitive Categories

### Category 1: Filesystem Operations

| Primitive | Class | Side Effect | Requires Grant | Example |
|-----------|-------|-------------|----------------|---------|
| fs_read | filesystem | Read file contents | read + location | fs_read("/home/alice/vdr/vdr.py") → content |
| fs_write | filesystem | Create/overwrite file | write + location | fs_write("/home/alice/vdr/new.py", content) |
| fs_append | filesystem | Append to file | write + location | fs_append(path, content) |
| fs_exists | filesystem | Check file existence | read + location | fs_exists(path) → bool |
| fs_list_dir | filesystem | List directory contents | list_dir + location | fs_list_dir(path) → [entries] |
| fs_create_dir | filesystem | Create directory | create_dir + location | fs_create_dir(path) |
| fs_delete | filesystem | Delete file or directory | delete + location | fs_delete(path) |
| fs_move | filesystem | Move/rename | write + both locations | fs_move(src, dst) |
| fs_copy | filesystem | Copy file | read src + write dst | fs_copy(src, dst) |
| fs_file_size | filesystem | Get file size | read + location | fs_file_size(path) → bytes |
| fs_file_modified | filesystem | Get modification time | read + location | fs_file_modified(path) → timestamp |
| fs_glob | filesystem | Find files by pattern | read + location | fs_glob(path, "*.py") → [files] |
| fs_tree | filesystem | Recursive directory listing | read + location | fs_tree(path) → tree structure |
| fs_diff | filesystem | Diff two files | read + both locations | fs_diff(a, b) → diff |
| fs_checksum | filesystem | File hash | read + location | fs_checksum(path) → hash |

**Constraint integration:** Every fs operation checks the grant's location constraint (path must be under the granted directory), the operation must be in allowed_operations, the grant must not be expired, and uses_remaining must be positive. After execution, uses_remaining is decremented and the operation is logged as a KB fact with timestamp, path, and result status.

### Category 2: Code Compilation

| Primitive | Class | Side Effect | Requires Grant | Example |
|-----------|-------|-------------|----------------|---------|
| compile_zig | compile | Invoke Zig compiler | compile + location | compile_zig(src_dir, target) → result |
| compile_python_check | compile | Python syntax check | compile + location | compile_python_check(file) → ok/errors |
| compile_c | compile | Invoke C compiler | compile + location | compile_c(file, flags) → result |
| compile_rust | compile | Invoke Rust compiler | compile + location | compile_rust(src_dir, target) → result |

Each returns a structured result:

```
CompileResult = struct {
    success: bool,
    exit_code: number,
    stdout: atom,
    stderr: atom,
    duration_ms: number,
    output_path: ?atom,
    warnings: []atom,
    errors: []atom,
};
```

### Category 3: Script Execution

| Primitive | Class | Side Effect | Requires Grant | Example |
|-----------|-------|-------------|----------------|---------|
| exec_python | execute | Run Python script | execute + location | exec_python(file, args) → result |
| exec_shell | execute | Run shell command | execute + location | exec_shell(cmd) → result |
| exec_zig_test | execute | Run Zig tests | execute + location | exec_zig_test(src_dir) → result |
| exec_pytest | execute | Run pytest | execute + location | exec_pytest(test_dir) → result |
| exec_script | execute | Run arbitrary script | execute + location | exec_script(interpreter, file, args) → result |

Each returns:

```
ExecResult = struct {
    success: bool,
    exit_code: number,
    stdout: atom,
    stderr: atom,
    duration_ms: number,
    started_at: timestamp,
    finished_at: timestamp,
    pid: number,
};
```

### Category 4: Linting and Analysis

| Primitive | Class | Side Effect | Requires Grant | Example |
|-----------|-------|-------------|----------------|---------|
| lint_python | lint | Run Python linter | read + location | lint_python(file) → [issues] |
| lint_zig | lint | Run Zig linter | read + location | lint_zig(file) → [issues] |
| lint_json | lint | Validate JSON | read + location | lint_json(file) → ok/errors |
| lint_markdown | lint | Check markdown | read + location | lint_markdown(file) → [issues] |
| analyze_imports | lint | List Python imports | read + location | analyze_imports(file) → [modules] |
| analyze_complexity | lint | Cyclomatic complexity | read + location | analyze_complexity(file) → metrics |
| analyze_dependencies | lint | Module dependency graph | read + location | analyze_dependencies(dir) → graph |
| count_lines | lint | Line counts by type | read + location | count_lines(file) → {code: N, comment: M, blank: K} |

Linting is read-only. It requires only a read grant on the target location. But it still requires a positive grant because it accesses the filesystem.

### Category 5: Network Operations

| Primitive | Class | Side Effect | Requires Grant | Example |
|-----------|-------|-------------|----------------|---------|
| net_download | network | Download URL to file | network + write location | net_download(url, path) → result |
| net_fetch | network | HTTP GET, return content | network | net_fetch(url) → content |
| net_post | network | HTTP POST | network | net_post(url, body) → response |
| net_ping | network | Check host reachability | network | net_ping(host) → latency_ms |
| net_dns_resolve | network | DNS lookup | network | net_dns_resolve(hostname) → ip |

Network operations require both a network grant and (for downloads) a filesystem write grant on the destination.

### Category 6: Process Management

| Primitive | Class | Side Effect | Requires Grant | Example |
|-----------|-------|-------------|----------------|---------|
| proc_start | process | Start background process | execute + location | proc_start(cmd) → task_id |
| proc_poll | process | Check process status | process | proc_poll(task_id) → running/finished/failed |
| proc_wait | process | Block until complete | process | proc_wait(task_id) → result |
| proc_kill | process | Terminate process | process | proc_kill(task_id) → ok |
| proc_stdout | process | Read current stdout | process | proc_stdout(task_id) → content |
| proc_stderr | process | Read current stderr | process | proc_stderr(task_id) → content |
| proc_list | process | List active processes | process | proc_list() → [task_ids] |

---

## 4. Async Execution and Working Memory

Operational primitives may take seconds, minutes, or hours. The system must not block on them. The architecture is:

### 4.1 Task Submission

When an operational primitive is invoked, it creates a task:

```
Task = struct {
    id: Text,                    // unique task identifier
    operation: Text,             // "exec_pytest", "compile_zig", etc.
    args: []Term,                // operation arguments
    grant: Text,                 // which grant authorized this
    status: enum { pending, running, completed, failed, killed },
    submitted_at: timestamp,
    started_at: ?timestamp,
    completed_at: ?timestamp,
    result: ?ExecResult,
    topic: Text,                 // which topic this belongs to
    notify_on_complete: bool,    // whether to notify the LLM
};
```

The task is asserted as a KB fact:

```
task("task_001", "exec_pytest", ["/home/alice/vdr/"], 
     grant("alice_project_exec"), 
     status(pending), 
     submitted_at(timestamp(2026,5,16,14,30,0)),
     topic("vdr_testing")).
```

### 4.2 Background Execution

The task runs in a separate process. The conversation continues. The LLM does not wait. It says:

```
LLM: "I've started running the test suite. Task ID: task_001. 
      I'll let you know when it finishes. Meanwhile, what else 
      shall we work on?"
```

### 4.3 Working Memory Update on Completion

When the task completes, the result is written to working memory in the task's topic KB:

```
task("task_001", ..., status(completed), 
     completed_at(timestamp(2026,5,16,14,30,47)),
     result(exec_result(success, 0, "705 tests passed", "", 12400))).

task_result_summary("task_001", "pytest: 705 passed, 0 failed, 12.4s").
```

### 4.4 LLM Polling and Notification

On each turn, the LLM checks for completed tasks in its active scope:

```
Rule: pending_results(Results) :-
    active_topic(T),
    findall(TaskId-Summary, 
        (task(TaskId, _, _, _, status(completed), _, topic(T)),
         task_result_summary(TaskId, Summary),
         not(task_acknowledged(TaskId))),
        Results).
```

If there are completed tasks, the LLM mentions them at the end of its response:

```
LLM: [responds to whatever the user asked]

---
Background task completed:
  task_001 (pytest): 705 passed, 0 failed, 12.4s
  [View full output: /task_001/stdout]
```

The user can then ask for details, or ignore the notification and continue. The task result persists in the KB until explicitly pruned.

### 4.5 Explicit Polling

The user can also explicitly ask:

```
User: "Are my tests done yet?"
LLM: [queries task status]
Action: proc_poll("task_001") → completed
KB: task("task_001", ..., status(completed), result(...))
Output: "Yes, task_001 finished 30 seconds ago. 705 tests passed in 12.4s."
```

---

## 5. Direct Download Without LLM Processing

This is a critical feature. If the user knows the address of data in the KB or filesystem, they can download it directly without the LLM generating or processing it.

### 5.1 The Problem

Currently, if you want a file the LLM has access to, you ask for it, the LLM reads it, tokenizes it, and regenerates it in the output. This is slow, lossy (token limits truncate large files), and unnecessary. The data exists. The user wants it. The LLM is a middleman adding latency and potential errors.

### 5.2 Direct Access Predicate

```
direct_access(Resource, User, Content) :-
    resource_exists(Resource),
    user_can_see(User, Resource),
    resource_content(Resource, Content).
```

Resource types that support direct access:

| Resource Type | Address Format | Example |
|---------------|---------------|---------|
| KB fact | kb_name/predicate/args | kb_vdr_training/parameter_value/layer.1.weight |
| KB dump | kb_name/* | kb_characters_b/* |
| Working data | topic/binding/key | story_b/binding/bob_age |
| File | fs://path | fs:///home/alice/vdr/vdr.py |
| Task output | task://task_id/stdout | task://task_001/stdout |
| Task output | task://task_id/stderr | task://task_001/stderr |
| Checkpoint | checkpoint://step_N | checkpoint://step_100 |
| Diff | diff://snap_a/snap_b | diff://step_0/step_100 |
| Export | export://kb_name | export://kb_characters_b |

### 5.3 User-Initiated Direct Download

```
User: "/download fs:///home/alice/vdr/test_basic.py"

System:
  1. Check: user_can_see(alice, fs:///home/alice/vdr/test_basic.py) → true
  2. Check: positive_grant covers fs_read at this path → true
  3. Serve file directly as attachment
  4. No LLM processing. No tokenization. No regeneration.
  5. Log: direct_access(alice, fs:///home/alice/vdr/test_basic.py, timestamp)
```

```
User: "/download export://kb_characters_b"

System:
  1. Check: user_can_see(alice, kb_characters_b) → true
  2. Serialize KB to JSON (using pure primitive format_json)
  3. Serve as attachment
  4. No LLM processing.
  5. Log: direct_access(alice, export://kb_characters_b, timestamp)
```

```
User: "/download task://task_001/stdout"

System:
  1. Check: task_001 belongs to alice's topic → true
  2. Serve stdout content directly
  3. No LLM processing.
```

### 5.4 LLM-Initiated Direct Attachment

The LLM can also decide to attach data directly rather than generating it:

```
User: "Show me the VDR source code"

LLM reasoning:
  - User wants file content
  - File exists at known path
  - Direct attachment is better than token-regeneration
  
LLM output:
  "Here's the VDR core source:"
  [Attachment: fs:///home/alice/vdr/vdr.py — direct, not generated]
```

The attachment is the actual file, not the LLM's token-by-token reproduction of the file. The file is exact. The LLM's reproduction would be approximate (token limits, potential errors, no guarantee of completeness).

### 5.5 Direct Access to Computed Results

When a pure primitive produces a large result, it can be stored in the KB and offered as a direct download rather than embedded in the conversation:

```
User: "Sort all 500 entries in the dataset by age"

LLM:
  Action: list_sort_by_key(kb_query_all(kb_dataset, entries), "age", ascending)
  Result: 500-element sorted list (stored in KB as sorted_result_001)

Output:
  "Sorted all 500 entries by age."
  [Attachment: kb://sorted_result_001 — 500 entries, direct download]
  "The youngest is Alice (17) and the oldest is Harold (94)."
```

The LLM provides a summary. The full data is a direct download from the KB. The user gets both: the LLM's interpretation and the exact data. The data is not generated. It is computed by a primitive and stored.

---

## 6. The Credential and Grant System

### 6.1 Grant Hierarchy

Grants follow the KB hierarchy:

```
kb_global
  grant: "system_read" — read any file in system dirs (no write, no execute)
  
kb_org_acme
  grant: "org_network" — network access to approved domains
  
kb_dept_engineering
  grant: "eng_compile" — compile in project directories
  grant: "eng_execute" — execute tests in project directories
  
kb_team_backend
  grant: "backend_db_read" — read from staging database
  
kb_user_alice
  grant: "alice_project_fs" — full filesystem in /home/alice/projects/
  grant: "alice_deploy" — deploy to staging (time-limited, requires 2FA)
```

Alice inherits all ancestor grants. She can read system files (from global), access approved network domains (from org), compile and execute tests (from engineering), read the staging database (from backend), and has full filesystem access in her project directory (personal). She can also deploy to staging, but only with a time-limited 2FA-verified grant.

### 6.2 Grant Lifecycle

```
Grant States: inactive → active → expired
                ↓                    ↑
              revoked            time_limit
```

| Transition | Trigger | Logged? |
|-----------|---------|---------|
| inactive → active | Issued by admin or self (for personal grants) | Yes: issuer, timestamp, scope |
| active → expired | Current time exceeds expires_at | Yes: automatic |
| active → revoked | Admin or issuer revokes | Yes: revoker, reason |
| active → exhausted | uses_remaining reaches 0 | Yes: automatic |

### 6.3 Grant Verification on Every Operation

```
Rule: grant_valid(Grant) :-
    grant_status(Grant, active),
    grant_expires(Grant, Exp),
    current_timestamp(Now),
    Now < Exp,
    grant_uses_remaining(Grant, Uses),
    Uses > 0.

Rule: grant_covers(Grant, Op) :-
    grant_operation_class(Grant, Class),
    operation_class(Op, Class),
    grant_allowed_operations(Grant, Allowed),
    operation_type(Op, Type),
    member(Type, Allowed),
    grant_location(Grant, GrantLoc),
    operation_location(Op, OpLoc),
    path_within(OpLoc, GrantLoc).

Rule: grant_constraints_satisfied(Grant, Op) :-
    grant_constraints(Grant, Constraints),
    forall(member(C, Constraints), constraint_satisfied_for(C, Op)).
```

Every operational primitive goes through this verification chain before execution. The verification is a Prolog query — it uses the same logic engine, the same KB structure, the same constraint system. The security model is not a separate system bolted on. It is facts and rules in the knowledge base.

---

## 7. Execution Logging and Audit Trail

Every operational primitive execution is logged as a KB fact:

```
execution_log("exec_001",
    operation("exec_pytest"),
    args(["/home/alice/vdr/"]),
    grant("alice_project_exec"),
    user("alice"),
    started_at(timestamp(2026,5,16,14,30,0)),
    completed_at(timestamp(2026,5,16,14,30,47)),
    duration_ms(47000),
    exit_code(0),
    success(true),
    topic("vdr_testing")).
```

The audit trail is queryable:

```
?- execution_log(_, operation("fs_write"), _, _, user("alice"), _, _, _, _, _, _).
% All file writes by Alice

?- execution_log(_, _, _, grant(G), _, _, _, _, _, success(false), _).
% All failed operations, with which grant was used

?- execution_log(_, _, _, _, _, started_at(S), completed_at(E), _, _, _, _),
   duration(S, E, D), D > 60000.
% All operations that took more than 60 seconds
```

---

## 8. The Complete Primitive Taxonomy

| Category | Type | Grant Required | Async? | Side Effects |
|----------|------|---------------|--------|-------------|
| String operations | Pure | No | No | None |
| List/array operations | Pure | No | No | None |
| VDR arithmetic | Pure | No | No | None |
| Set operations | Pure | No | No | None |
| Dictionary operations | Pure | No | No | None |
| Linear algebra | Pure | No | No | None |
| Statistics/probability | Pure | No | No | None |
| Conversion/formatting | Pure | No | No | None |
| Date/time | Pure | No | No | None |
| Hashing/encoding | Pure | No | No | None |
| Graph operations | Pure | No | No | None |
| Regex/pattern matching | Pure | No | No | None |
| Logic/control flow | Pure | No | No | None |
| KB/constraint operations | Pure (KB-internal) | No | No | KB state change |
| Filesystem | Operational | filesystem grant | Optional | Disk read/write |
| Compilation | Operational | compile grant | Yes (recommended) | Disk write, CPU |
| Script execution | Operational | execute grant | Yes (recommended) | Arbitrary |
| Linting/analysis | Operational | read grant | Optional | None (read-only) |
| Network | Operational | network grant | Yes (recommended) | Network I/O |
| Process management | Operational | process grant | Inherently async | Process lifecycle |
| Direct download | Operational | read grant on resource | No | Data transfer |

---

## 9. Integration With the VDR-Prolog System

The primitives — both pure and operational — are the hands of the VDR-LLM-Prolog system. The LLM is the brain (intent recognition, planning, explanation). The Prolog KB is the memory (facts, rules, constraints, provenance). The primitives are the hands (computation, file operations, compilation, execution).

The flow for a complex task:

```
User: "Run the VDR test suite, and if it passes, 
       commit the changes to the gym scripts"

LLM reasoning:
  1. This requires execute grant (pytest) and filesystem grant (git commit)
  2. Check grants: alice_project_exec covers pytest, alice_project_fs covers git
  3. Plan: run tests first (async), then conditionally commit

LLM output:
  "Starting the test suite now. I'll commit if all tests pass."

Actions:
  Task 1: proc_start("python3 -m pytest test_*.py")
  → task_001 submitted, running in background

[... conversation continues on other topics ...]

[Task 1 completes: 705 passed, 0 failed]

LLM (next turn):
  "Test suite finished: 705 passed, 0 failed. 
   Proceeding with the commit."

Actions:
  Task 2: exec_shell("git add gym/gym_16*.py gym/gym_17*.py ...")
  Task 3: exec_shell("git commit -m 'Add gyms 16-23'")

LLM:
  "Changes committed. Here's the summary:"
  [KB: task_003 result → commit hash, files changed, diff stats]
```

Every step is logged. Every grant is verified. Every result is in the KB. The LLM orchestrated the workflow. The primitives did the work. The constraint system ensured authorization. The async system kept the conversation flowing.

---

## 10. What This Means

The LLM no longer needs to pretend to be a computer. It has one. The pure primitives give it exact computation for anything that has a known algorithm. The operational primitives give it the ability to interact with the real world — files, compilers, networks, processes. The credential system constrains what it can touch. The async system prevents it from blocking. The KB records everything for audit and provenance.

The LLM's unique contribution becomes what it was always meant to be: understanding intent, making plans, explaining results, and connecting pieces together in ways that rigid programs cannot. Everything else — sorting, compiling, file management, arithmetic, formatting — is delegated to primitives that do it correctly every time.

This is not tool use. This is tool integration. The tools are inside the system, governed by the same constraint logic, recorded in the same knowledge base, and subject to the same provenance tracking as everything else. When the LLM says "I compiled your code," you can query the KB for the exact compilation command, the exact exit code, the exact stderr output, the exact timestamp, and the exact grant that authorized it. No trust required. Full verifiability.
