## First-Class Knowledge Base Surfacing

### The Principle

Nothing in the system is hidden from itself or from an authorized user. Every KB, every fact, every binding, every constraint, every derivation, every topic state is queryable, surfaceable, and directly addressable. The system does not need to reconstruct or paraphrase its own state — it can point directly at the structured data and say "here it is."

This is a fundamental departure from how LLMs currently work. A current LLM has internal activations that are opaque tensors. If a user asks "what do you know about Bob," the model generates tokens that approximate its internal state. The tokens might be wrong. They might be incomplete. They might hallucinate facts that are not actually represented anywhere. The model's internal state and its verbal report about that state are two completely different things, and there is no mechanism to ensure they agree.

In VDR-Prolog, the model's knowledge is structured facts in knowledge bases. When the user asks "what do you know about Bob," the system does not generate tokens about Bob. It runs a query against the active KBs and returns the actual facts. The output is not a paraphrase of knowledge. It is the knowledge itself, directly surfaced.

### Direct Data Output

The critical mechanism is that the system can return structured data without tokenizing it through the language model. The LLM generates natural language for conversation, explanation, and reasoning. But when the user asks for data, the system can bypass the LLM entirely and serve the structured facts directly.

```
User: "What do I know about Bob in this story?"

System action:
  1. Identify active topic → story_b
  2. Query: findall(Key-Value, binding(kb_characters_b, Key, Value), Results)
  3. Results are structured facts, not generated tokens

Output (mixed):
  LLM text: "Here's what we have for Bob in the London story:"
  Direct data (from KB, not tokenized):
    bob_age: 59
    bob_town: London
    bob_occupation: retired professor
    bob_introduced_at: chapter 1, paragraph 3
    
  LLM text: "Margaret is also in this story — want to see her details?"
```

The data block is not generated text. It is a direct read from `kb_characters_b`, formatted for display. The LLM did not produce the number 59. The KB produced it. The LLM produced the framing sentence. The distinction matters because the data cannot be wrong — it is exactly what is stored. The framing sentence could be wrong (the LLM might mischaracterize the data), but the data itself is authoritative.

### Addressable References

Every fact in every KB has an address. The address is the KB path plus the fact identifier. These addresses are first-class objects that the LLM can use in its outputs.

```
User: "What learning rate are we using?"

System action:
  1. Query: resolve("lr", Value) in active scope
  2. Found: binding(kb_vdr_training, "lr", fraction(1, 10))
  3. Address: kb_vdr_training/lr

Output:
  LLM text: "The learning rate is "
  Direct reference: [kb_vdr_training/lr → 1/10]
  LLM text: ", set during training configuration."
```

The reference `[kb_vdr_training/lr → 1/10]` is a live link to the actual data. If the value changes (the user updates the learning rate), the reference resolves to the new value. The LLM's surrounding text might become stale, but the reference never lies.

This is analogous to a spreadsheet cell reference versus a hardcoded number. The reference always reflects the current state. The surrounding text is static commentary.

### The Permission Model

Not all users see all KBs. The owner of the LLM system sees everything. A constrained user sees only what the constraint set permits.

```
Rule: user_can_see(User, KB) :-
    user_role(User, owner).
    % Owner sees everything

Rule: user_can_see(User, KB) :-
    user_role(User, operator),
    not(kb_classified(KB, internal_only)).
    % Operators see everything except internal-only KBs

Rule: user_can_see(User, KB) :-
    user_role(User, end_user),
    kb_visibility(KB, public).
    % End users see only public KBs

Rule: user_can_see(User, KB) :-
    user_role(User, end_user),
    kb_granted(KB, User).
    % End users see KBs explicitly granted to them
```

The constrained user asks "what do you know about me?" The system queries only the KBs the user is permitted to see. Model weights, training provenance, internal constraint states — these are in KBs marked `internal_only` and are invisible to end users. But the end user's conversation history, their stored preferences, their working data — these are in KBs the user can see and query freely.

The unconstrained owner asks the same question and sees everything: model parameters, training history, constraint violations, internal reasoning traces, all KB states across all topics. Nothing is hidden because nothing needs to be hidden from the person who controls the system.

### The LLM's Self-Access

The LLM itself has access to all KBs during its reasoning process. This is not optional. The LLM's ability to produce correct outputs depends on it being able to read its own structured state.

```
Rule: llm_can_access(KB) :- kb_exists(KB).
% The LLM can access every KB during reasoning.
% Output filtering happens at the surfacing layer, not the reasoning layer.
```

The reasoning layer and the output layer are separate. The LLM reasons over all available KBs. The output layer filters what the user sees based on permissions. This means the LLM can use internal facts (model architecture, training state, constraint status) to inform its reasoning without exposing those facts to the user.

But if the user is the owner, the output filter is identity — everything the LLM sees, the owner sees. The owner can ask "show me the internal constraint state" and get the actual constraint facts, not a summary.

### Surfacing Modes

The system supports multiple surfacing modes depending on what the user needs:

**Narrative mode.** The LLM generates natural language with embedded references to KB facts. This is the default conversational mode. The LLM explains, and the data supports.

```
"The model's attention at position 3 was dominated by position 1, 
with weight [kb_inference_batch42/attn_weight_3_1 → 43545600/59565131], 
which is about 73%. This makes sense because position 1 contains the 
subject that position 3's verb needs to agree with."
```

**Table mode.** The system dumps a structured view of a KB or query result. No LLM framing. Just data.

```
User: "/show kb_characters_b"

bob_age:        59
bob_town:       London
bob_occupation: retired professor
margaret_age:   45
margaret_role:  spy
```

**Tree mode.** The system shows the KB hierarchy with scoping.

```
User: "/tree"

[active] kb_global
  [active] kb_project_vdr
    [active] kb_vdr_core
      [active] kb_vdr_llm         ← current topic
        [active] kb_vdr_training
    [inactive] kb_vdr_gyms
  [inactive] kb_math_series
[inactive] kb_story_a
[inactive] kb_story_b
```

**Provenance mode.** The system shows the derivation chain for a specific value.

```
User: "/provenance kb_vdr_training/layer1_weight_0_0"

Value: 31/140
  ← sgd_update(step=1, lr=1/10, gradient=-3/7)
    ← value_at(step=0): 1/4
      ← xavier_init(seed=42, fan_in=2, fan_out=2)
    ← gradient_at(step=0): -3/7
      ← backward(loss=17/2, ...)
        ← mse(pred=[8, 13], target=[10, 10])
          ← forward(input=[1, 1], weights=...)
```

Every line is a fact in the KB. Every value is an exact fraction. The chain is complete back to initialization.

**Constraint mode.** The system shows active constraints and their status.

```
User: "/constraints"

[active] vdr_exact           — operational — verified at turn 45
[active] python_38_compat    — operational — verified at turn 45
[active] 30_sec_runtime      — operational — verified at turn 43
[active] sum_to_one          — axiom       — verified at turn 44
[active] non_negative_attn   — axiom       — verified at turn 44
[active] denom_bound_2^64    — project     — VIOLATED at turn 40
  → parameter layer2.weight[1][3] has denominator 2^71
[parked] story_consistency   — project     — parked with topic story_b
```

**Diff mode.** The system shows what changed between two points.

```
User: "/diff step(0) step(1)"

Changed:
  layer1_weight_0_0: 1/4 → 31/140
  layer1_weight_0_1: 1/3 → 47/210
  layer1_weight_1_0: -1/4 → -29/140
  layer1_weight_1_1: 1/6 → 23/210
  layer1_bias_0: 0 → 3/70
  layer1_bias_1: 0 → -1/70
  loss: 17/2 → (not yet computed)
  
Unchanged: 4,291 bindings
```

### Slash Commands as KB Queries

The surfacing modes above use slash commands, but these are just syntactic sugar for KB queries. The LLM recognizes the intent and translates to the appropriate query:

```
"/show kb_characters_b"
  → findall(K-V, binding(kb_characters_b, K, V), Results)

"/tree"
  → build_kb_tree(root, Tree)

"/provenance X"
  → derivation_chain(X, Chain)

"/constraints"
  → findall(C, constraint(C, _, Status, _, _, _), All)

"/diff A B"
  → diff(A, B, Added, Removed, Changed)
```

But the user does not need to use slash commands. They can ask in natural language:

"Show me everything about Bob" → the LLM recognizes this as a KB query, runs it, surfaces the results directly.

"What changed since last checkpoint" → the LLM recognizes this as a diff query, identifies the relevant checkpoints, runs the diff, surfaces the structured output.

"Why is this weight 31/140" → the LLM recognizes this as a provenance query, traces the derivation, surfaces the chain.

The LLM's role shifts from "produce tokens that approximate the answer" to "identify the right query, run it against the KB, and frame the results for the user." The data comes from the KB. The framing comes from the LLM. They are clearly separated.

### Structured Output Alongside Generated Text

The output format interleaves LLM-generated text with direct KB output. The two are visually and semantically distinct:

```
LLM: "Looking at the training run, the loss decreased from step 0 to step 1:"

KB [kb_vdr_training/loss_history]:
  step 0: 17/2 (= 8.5)
  step 1: 1687374558939772106219752230270721/98493723850592747520000000000000000 (≈ 0.0171)

LLM: "That's a significant drop. The weight updates were:"

KB [kb_vdr_training/weight_diff step(0)→step(1)]:
  layer1_weight_0_0: 1/4 → 31/140 (δ = -3/70)
  layer1_weight_0_1: 1/3 → 47/210 (δ = -1/42)
  ...

LLM: "The gradients suggest the model is learning the input-output mapping. 
Want me to run another training step?"
```

The KB blocks are authoritative data. They cannot hallucinate. They are not paraphrases. They are the actual stored facts, formatted for display. The LLM text between them is interpretation — it could be wrong, but the data it is interpreting is guaranteed correct.

### Self-Reference in Reasoning

The LLM can reference KB facts during its own reasoning process, not just in output:

```
Internal reasoning (visible to owner, hidden from end user):

  Query: What is the current active constraint set?
  KB result: [vdr_exact, python_38_compat, 30_sec_runtime, sum_to_one, ...]
  
  Query: Does the proposed code violate python_38_compat?
  KB result: constraint condition is (no_walrus_operator, no_match_statement, ...)
  Check: proposed code contains no walrus operator, no match statement
  Result: no violation
  
  Query: What is the estimated runtime?
  KB result: similar operations in kb_vdr_gyms took < 5 seconds
  Check: 5 < 30
  Result: within 30_sec_runtime constraint
  
  Proceed with output.
```

The LLM does not need to remember the constraints from the system prompt. It queries them from the KB. It does not need to guess whether the code is Python 3.8 compatible. It checks the constraint condition against the actual code. The reasoning is grounded in structured facts, not in pattern-matched context tokens.

### The Fundamental Shift

In a conventional LLM, the model's knowledge and its output are the same thing — both are token sequences. The model "knows" something only in the sense that it can generate tokens about it. There is no separate store of verified facts. There is no authority that is not the model's own generation.

In VDR-Prolog with first-class KB surfacing, knowledge and output are distinct. Knowledge lives in KBs as structured, exact, queryable facts. Output is a mix of LLM-generated framing and directly surfaced KB data. The LLM can be wrong in its framing. The KB data cannot be wrong — it is what it is.

This means the user can trust the data even when they cannot fully trust the model. The KB is an exact record. The model is an interpreter of that record. The interpreter might misinterpret, but the record is always available for the user to check.

That is what first-class surfacing means. Not "the LLM can talk about its data." Rather: "the data is directly available as structured output, and the LLM's role is to frame it, not to reproduce it."
