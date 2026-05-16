**VDR-15 Plan: Prompt Optimization of VDR-LLM-Prolog**

Registry: @HOWL-VDR-15-2026

---

**Thesis**

The VDR-LLM-Prolog system reduces LLM token consumption by 85-95% per prompt by offloading parsing, computation, state management, retrieval, and formatting to exact primitives, KB lookups, and grammar templates. Even if per-token processing is slower due to Q335 exact arithmetic, total prompt cost is dramatically lower because the LLM generates 10-20x fewer tokens. The tokens it does generate are spent on judgment and prose — the two things token prediction actually does well. Results are more accurate because nothing computed by primitives can be wrong, and everything carries provenance.

---

**Section 1: The Token Cost Problem**

What a conventional LLM spends tokens on per prompt. Break down a typical prompt into categories: context re-reading, input parsing, state reconstruction, computation, deduction, formatting, hedging. Show that 80-90% of tokens are infrastructure, not judgment. Every infrastructure token has a nonzero error probability and no provenance. The cost scales with conversation length because state lives in the context window.

**Section 2: The Prompt Flow**

Full mechanical walkthrough of how a prompt moves through VDR-LLM-Prolog. Input arrives as bytes. Typo and classification KBs clean and tag tokens — zero LLM tokens. Scope resolution maps corrected tokens to KB paths via integer lookup — zero LLM tokens. Data fetching pulls referenced data into typed primitives — zero LLM tokens. Grammar parsing extracts additional structure from input — zero LLM tokens. Goal determination is where the LLM first engages, reading pre-structured, typed, scoped input. Plan goes into the stack. Orchestrated inference executes the plan through primitive calls. Output uses grammar for structure, LLM for prose only.

**Section 3: Token Accounting**

Formal accounting model. Define token categories: judgment tokens (reading content requiring human-level assessment, writing prose), command tokens (primitive invocations, roughly 8 tokens each), infrastructure tokens (everything else — parsing, computation, state, formatting, hedging). In conventional LLMs, infrastructure dominates. In VDR-LLM-Prolog, infrastructure is zero LLM tokens. Derive the ratio. Show that command tokens are low-entropy reference selection from a known vocabulary of roughly 300 names, not high-entropy generation.

**Section 4: The Crossover Calculation**

Q335 arithmetic is slower per operation than float. Quantify how much slower — one integer multiply on 100-digit numbers plus one divmod versus one float multiply. Then show the budget: if the system saves 2790 tokens on a 3000-token prompt, those 2790 tokens of forward-pass cost buy an enormous number of integer operations. Derive the crossover multiplier — how many times slower Q335 would need to be per operation before the system is net slower. Show it's roughly 10,000x for a single turn and grows with conversation length because token cost scales with context re-reading while primitive cost does not.

**Section 5: Conversation Length Scaling**

This is the structural advantage. Conventional LLMs: cost per turn scales linearly with conversation length times context size because every turn re-reads everything. VDR-LLM-Prolog: cost per turn stays roughly flat because state is in KBs at integer addresses. The LLM reads structured state summaries, not raw conversation history. Over 20 turns, conventional cost approaches 40,000-60,000 tokens. VDR-LLM-Prolog stays under 5,000 total LLM tokens. Graph the divergence.

**Section 6: The Capability Boundary**

Cases where conventional LLMs cannot perform the task at all. 1MB JSON exceeds context window. 10MB docx is impossible. 2000 support articles won't fit. 500 portfolio positions overflow. 200 source files can't be held simultaneously. VDR-LLM-Prolog handles all of these because data enters through primitives, never through the token stream. The data stays in KBs at integer addresses. The LLM sees structured summaries and specific slices pulled by command tokens. This isn't optimization — it's a category change from impossible to routine.

**Section 7: Use Case Demonstrations**

Seven use cases gamed out with specific builtin calls, token counts, and comparison to conventional LLM behavior. Each demonstrates the pattern: data enters through primitives, structure extracted by parsers, storage in typed KBs, computation by exact primitives, state persists across turns, output structure by grammar, LLM spends tokens only on judgment and prose.

1. SRE incident investigation — prometheus integration, time series analysis, root cause derivation
2. Legal contract review — document parsing, term extraction, obligation mapping, exposure calculation
3. Medical research synthesis — multi-paper ingestion, statistical aggregation, contradiction detection
4. Codebase migration — dependency analysis, pattern detection, automated transformation with test validation
5. Financial portfolio analysis — bulk position processing, exact arithmetic across 500 multiplications, correlation matrix
6. Customer support KB — bulk ingestion, indexed query, graph traversal of related articles
7. Academic grading — rubric application, statistical analysis, consistent feedback generation

Each case includes: operational environment used, grants required, specific builtins called with IDs, data flow through KBs, LLM token count breakdown by category, comparison conventional token count, accuracy comparison.

**Section 8: Accuracy by Construction**

Every token the LLM doesn't generate is a token that can't be wrong. Enumerate the error classes eliminated: arithmetic errors (digit prediction replaced by exact primitives), state errors (context window degradation replaced by KB persistence), formatting errors (structural token prediction replaced by grammar), retrieval errors (attention-based search replaced by integer-indexed lookup), confidence errors (hedging language replaced by exact fraction propagation). The remaining error surface is LLM judgment — intent recognition, step selection, prose generation. These are the tasks where token prediction has the lowest error rate because they're what it's actually trained to do.

**Section 9: The Attention Reduction**

Conventional attention serves multiple purposes simultaneously: relevance determination, fact retrieval, state tracking, relationship mapping, importance weighting. VDR-LLM-Prolog handles each structurally: relevance by lexical scoping, retrieval by integer address, state by KB persistence, relationships by typed connections, importance by exact confidence fractions. The LLM's attention operates on pre-structured, pre-scoped, pre-typed input. This enables simpler attention mechanisms — rational surrogates or linear attention instead of full transcendental softmax. The attention capacity freed from infrastructure is fully available for judgment.

**Section 10: Grammar as Token Eliminator**

Grammar provides structural tokens for free with guaranteed correctness. Quantify the savings: roughly 55% of tokens in JSON output are structural. In tables, roughly 60%. In code, roughly 40%. Grammar provides all of these at zero LLM token cost. On output, grammar constrains vocabulary to valid values per slot — 4 enum values instead of 50,000+ vocabulary. On input, grammar parses structure and delivers typed fields. The LLM receives and produces content, never structure. Bidirectional grammar means the same savings apply to both input parsing and output generation.

**Section 11: The Disposable Clone Advantage**

Conversation drift is a token cost problem — the longer the conversation, the more the LLM's reliability degrades, requiring more hedging tokens, more recapping tokens, more correction tokens. Disposable clones eliminate drift by killing degraded sessions and spawning fresh ones from frozen snapshots. Work committed to persistent KBs survives. The system gets more capable over conversation length instead of less reliable. Token efficiency stays constant or improves because the LLM always operates from a clean state with structured accumulated results.

**Section 12: Cumulative Token Economics**

Model the total system economics across a realistic workload — say 100 prompts over a working day in the SRE use case. Conventional: roughly 300,000 tokens, degrading accuracy, no persistent state between conversations, each conversation starts from zero. VDR-LLM-Prolog: roughly 30,000 LLM tokens, constant accuracy, persistent KB state accumulating across all conversations, each conversation starts with full prior context at integer addresses. The 10x token reduction compounds with the accuracy improvement and the state accumulation. Cost per useful conclusion drops by more than 10x because fewer conclusions need correction or rework.

**Appendix A: Token Cost Comparison Tables**

Per use case: conventional token count, VDR-LLM-Prolog token count, breakdown by category, ratio, error class comparison.

**Appendix B: Crossover Analysis**

Table showing Q335 slowdown factor versus net system performance at various conversation lengths. Shows that the crossover point moves further from break-even the longer the conversation runs.

**Appendix C: Builtin Call Patterns**

Common primitive chains for each use case. Shows the command token patterns that replace hundreds of generated tokens.

**Appendix D: Grammar Savings Quantification**

Per output format: token count with generation versus token count with grammar, structural token percentage, error probability eliminated.

**Appendix E: Attention Mechanism Comparison Under Reduced Load**

Compare full softmax, rational surrogate, and linear attention when the input is pre-structured typed data versus raw token sequences. Show that simpler mechanisms suffice when infrastructure load is removed.

---

**Validation approach:** The token counts come from the gamed-out use cases. The crossover calculation is exact VDR arithmetic. The accuracy claims follow from the primitive correctness already proven in VDR-1 through VDR-14. No new primitives, builtins, or struct fields are introduced. This paper is a pattern-of-use analysis over the existing specification, same as VDR-9.
