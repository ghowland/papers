**Programming: Bug Investigation**

The LLM receives a failing test. It pushes the failure into an LRU channel for recent failures and increments a counter tracking total failures this session.

```
CMD: lru_push(root.project.bugs.recent_failures, "test_047", 
    "graph_traversal: assertion error at line 89")
CMD: counter_inc(root.project.bugs.failure_count)
```

Before investigating, it checks whether this function has failed recently — maybe there's a pattern:

```
CMD: lru_peek(root.project.bugs.recent_failures, 10)
→ [{test_047: graph_traversal}, {test_044: graph_cycle}, {test_041: graph_bfs}]
```

Three graph-related failures in recent history. The LLM doesn't investigate test_047 in isolation — it formalizes all three as Prolog facts and writes dependency rules:

```
CMD: KB_ASSERT(root.project.bugs.investigation_01,
    fact(failure(test_047, function(graph_traversal), line(89))))
CMD: KB_ASSERT(root.project.bugs.investigation_01,
    fact(failure(test_044, function(graph_cycle), line(52))))
CMD: KB_ASSERT(root.project.bugs.investigation_01,
    fact(failure(test_041, function(graph_bfs), line(31))))
CMD: KB_ASSERT(root.project.bugs.investigation_01,
    fact(calls(graph_traversal, graph_bfs)))
CMD: KB_ASSERT(root.project.bugs.investigation_01,
    fact(calls(graph_cycle, graph_bfs)))
CMD: KB_ASSERT(root.project.bugs.investigation_01,
    rule(common_dependency(F1, F2, Dep) :- 
        calls(F1, Dep), calls(F2, Dep), F1 \= F2))
CMD: KB_QUERY(root.project.bugs.investigation_01, 
    common_dependency(graph_traversal, graph_cycle, Dep))
→ Dep = graph_bfs
```

Both failing functions depend on graph_bfs. The LLM acquires a lock before starting the fix — signaling that this module is being worked on:

```
CMD: lock_acquire(root.project.graph_module.editing, holder: "bug_fix_001")
```

It pushes a remediation plan onto a stack so it can unwind if something goes wrong:

```
CMD: stack_push(root.project.bugs.undo_stack, 
    snapshot_ref("root.project.graph_module.v3"))
CMD: stack_push(root.project.bugs.fix_steps,
    "1. read graph_bfs source")
CMD: stack_push(root.project.bugs.fix_steps,
    "2. write instrumented version")  
CMD: stack_push(root.project.bugs.fix_steps,
    "3. run all three failing tests")
CMD: stack_push(root.project.bugs.fix_steps,
    "4. if pass: commit. if fail: pop undo_stack and revert")
```

It writes a Python script that instruments graph_bfs with exact VDR fraction tracing at each step, runs it against the three failing tests, and stores the trace output:

```
CMD: ENV_UPLOAD(env_dev, trace_bfs.py, root.project.scripts.trace)
CMD: ENV_EXEC(env_dev, "python3", root.project.scripts.trace)
→ stored at root.project.bugs.trace_results
```

The LLM uses string primitives to parse the trace:

```
CMD: PURE_FN string_split(trace_output, "\n") → trace_lines
CMD: PURE_FN list_filter(trace_lines, predicate(contains("ERROR"))) → error_lines
CMD: PURE_FN list_length(error_lines) → 3
CMD: PURE_FN string_split(error_lines[0], ":") → ["line 31", "visited set not reset between calls"]
```

Root cause found: the visited set persists across calls instead of resetting. The LLM writes the fix, runs the tests:

```
CMD: ENV_EXEC(env_dev, "python3 -m pytest test_graph.py")
→ 3 passed, 0 failed
```

It updates the tracking state:

```
CMD: counter_add(root.project.bugs.failure_count, -3)
CMD: lru_push(root.project.bugs.recent_fixes, "graph_bfs_visited_reset",
    "visited set was shared across calls")
CMD: lock_release(root.project.graph_module.editing)
CMD: stack_pop(root.project.bugs.fix_steps)  // clear the plan
CMD: bitset_set(root.project.bugs.resolved, 41)
CMD: bitset_set(root.project.bugs.resolved, 44)
CMD: bitset_set(root.project.bugs.resolved, 47)
```

And writes a permanent Prolog rule so the pattern is detectable in future code:

```
CMD: KB_ASSERT(root.project.code_rules,
    rule(smell(shared_mutable_state, Function) :-
        uses(Function, Collection),
        mutates(Function, Collection),
        called_multiple_times(Function),
        not(resets(Function, Collection))))
```

---

**Programming: Architecture Design**

User asks "should I use a message queue or database polling for our job processing?" The LLM creates a working data dict for the requirements:

```
CMD: KB_ASSERT(root.project.design.job_system,
    binding("max_jobs_per_minute", number(500)))
CMD: KB_ASSERT(root.project.design.job_system,
    binding("ordering_required", atom(true)))
CMD: KB_ASSERT(root.project.design.job_system,
    binding("failure_retry", atom(true)))
CMD: KB_ASSERT(root.project.design.job_system,
    binding("max_latency_ms", number(200)))
CMD: KB_ASSERT(root.project.design.job_system,
    binding("existing_infra", list([postgres, redis])))
```

It formalizes the architectural trade-offs as Prolog:

```
CMD: KB_ASSERT(root.knowledge.architecture.patterns,
    rule(fits(message_queue, Requirements) :-
        member(ordering_required(true), Requirements),
        member(max_latency_ms(L), Requirements), L < 500,
        member(failure_retry(true), Requirements)))

CMD: KB_ASSERT(root.knowledge.architecture.patterns,
    rule(fits(db_polling, Requirements) :-
        member(max_jobs_per_minute(N), Requirements), N < 100,
        member(existing_infra(Infra), Requirements), member(postgres, Infra)))

CMD: KB_ASSERT(root.knowledge.architecture.patterns,
    rule(fits(redis_queue, Requirements) :-
        member(existing_infra(Infra), Requirements), member(redis, Infra),
        member(ordering_required(true), Requirements),
        member(max_latency_ms(L), Requirements), L < 100))
```

It queries for all fitting patterns:

```
CMD: KB_QUERY(root.project.design.job_system, 
    findall(P, fits(P, gathered_requirements), Patterns))
→ Patterns = [message_queue, redis_queue]
```

Database polling is eliminated — 500 jobs/minute exceeds its threshold. Two options remain. The LLM writes Python to model throughput under load using exact fractions:

```
CMD: ENV_UPLOAD(env_dev, throughput_model.py, root.project.design.throughput)
// Script: model queue depth over time at 500/min arrival rate
// with exact VDR fractions for service time distributions
CMD: ENV_EXEC(env_dev, "python3", root.project.design.throughput)
→ {redis_queue: {p99_latency: fraction(85, 1), queue_depth_steady: fraction(12, 1)},
   rabbitmq: {p99_latency: fraction(120, 1), queue_depth_steady: fraction(23, 1)}}
```

Both work, but redis_queue uses existing infrastructure. The LLM stores the decision with its full rationale:

```
CMD: KB_ASSERT(root.project.design.decisions,
    fact(decision(job_processing, redis_queue, 
        reasons([existing_infra, lower_latency, lower_queue_depth]),
        eliminated([db_polling(throughput_insufficient)]),
        alternatives([rabbitmq(viable_but_new_dependency)]))))
```

---

**Speech Writing: Argument Construction**

User says "write a speech arguing for universal basic income." The LLM creates a working KB for the argument and a queue for the argument structure:

```
CMD: queue_create(root.writing.ubi_speech.argument_order, capacity: 20)
CMD: counter_create(root.writing.ubi_speech.unsupported_claims)
CMD: lru_create(root.writing.ubi_speech.sources, capacity: 30)
```

It searches for evidence and stores each finding as a Prolog fact with source provenance, pushing each source into the LRU for quick reference:

```
// After web search
CMD: KB_ASSERT(root.writing.ubi_speech.evidence,
    fact(claim(poverty_reduction, "UBI pilots in Kenya showed 42% poverty reduction",
        source("GiveDirectly 2023"), strength(peer_reviewed))))
CMD: lru_push(root.writing.ubi_speech.sources, "poverty_reduction", 
    "GiveDirectly 2023 Kenya pilot")

CMD: KB_ASSERT(root.writing.ubi_speech.evidence,
    fact(claim(entrepreneurship, "Recipients 23% more likely to start business",
        source("MIT study 2024"), strength(peer_reviewed))))
CMD: lru_push(root.writing.ubi_speech.sources, "entrepreneurship",
    "MIT 2024 study")

CMD: KB_ASSERT(root.writing.ubi_speech.evidence,
    fact(claim(cost_feasible, "Total cost approximately 3.2T per year",
        source("blogger estimate"), strength(unverified))))
CMD: lru_push(root.writing.ubi_speech.sources, "cost_feasible",
    "blogger estimate — WEAK")
CMD: counter_inc(root.writing.ubi_speech.unsupported_claims)
```

The counter caught that the cost claim is unverified. The LLM writes Prolog rules to check argument validity:

```
CMD: KB_ASSERT(root.writing.ubi_speech.logic,
    rule(well_supported(Claim) :- 
        claim(Claim, _, source(_), strength(S)),
        member(S, [peer_reviewed, government_report, meta_analysis])))

CMD: KB_ASSERT(root.writing.ubi_speech.logic,
    rule(needs_strengthening(Claim) :-
        claim(Claim, _, _, strength(S)),
        member(S, [unverified, press_release, anecdotal])))

CMD: KB_ASSERT(root.writing.ubi_speech.logic,
    rule(counter_argument_exists(Claim, Counter) :-
        claim(Claim, _, _, _),
        known_objection(Claim, Counter)))

CMD: KB_ASSERT(root.writing.ubi_speech.logic,
    fact(known_objection(cost_feasible, "inflation risk from monetary expansion")))
CMD: KB_ASSERT(root.writing.ubi_speech.logic,
    fact(known_objection(poverty_reduction, "dependency and reduced work incentive")))
```

It queries for the argument's structural health:

```
CMD: KB_QUERY(root.writing.ubi_speech.logic,
    findall(C, needs_strengthening(C), Weak))
→ Weak = [cost_feasible]

CMD: KB_QUERY(root.writing.ubi_speech.logic,
    findall(C-Obj, counter_argument_exists(C, Obj), Objections))
→ Objections = [cost_feasible-"inflation risk", poverty_reduction-"dependency"]

CMD: counter_get(root.writing.ubi_speech.unsupported_claims) → 1
```

One weak claim, two known objections to address. The LLM searches specifically for better cost data, finds a CBO estimate, updates the fact:

```
CMD: KB_RETRACT(root.writing.ubi_speech.evidence,
    claim(cost_feasible, _, source("blogger estimate"), _))
CMD: KB_ASSERT(root.writing.ubi_speech.evidence,
    fact(claim(cost_feasible, "Estimated 2.8T annually offset by eliminated programs",
        source("CBO 2025 analysis"), strength(government_report))))
CMD: counter_dec(root.writing.ubi_speech.unsupported_claims)
CMD: lru_push(root.writing.ubi_speech.sources, "cost_feasible",
    "CBO 2025 — upgraded from blog")
```

Now it builds the argument order in the queue, structured for persuasive flow:

```
CMD: queue_push(root.writing.ubi_speech.argument_order, 
    "hook: personal story of economic insecurity")
CMD: queue_push(root.writing.ubi_speech.argument_order,
    "claim: poverty_reduction — strongest evidence first")
CMD: queue_push(root.writing.ubi_speech.argument_order,
    "preempt objection: dependency — address with MIT entrepreneurship data")
CMD: queue_push(root.writing.ubi_speech.argument_order,
    "claim: entrepreneurship — pivot from defense to offense")
CMD: queue_push(root.writing.ubi_speech.argument_order,
    "claim: cost_feasible — CBO numbers, offset by eliminated programs")
CMD: queue_push(root.writing.ubi_speech.argument_order,
    "preempt objection: inflation — address with targeted implementation")
CMD: queue_push(root.writing.ubi_speech.argument_order,
    "close: vision of economic security as foundation for flourishing")
```

The LLM pops each section from the queue and generates text for it, checking each section against the evidence KB to ensure every claim has a source. The generated speech has a complete argument graph in the KB — every claim, its evidence, its source strength, known objections and their rebuttals, all queryable.

---

**Email Response: Thread Analysis**

User pastes a 15-message email thread. The LLM parses each message with string primitives and builds a structured representation:

```
CMD: PURE_FN string_split(thread_text, "---MESSAGE BOUNDARY---") → messages
CMD: PURE_FN list_length(messages) → 15
CMD: counter_create(root.email.thread_001.message_count)
CMD: counter_set(root.email.thread_001.message_count, 15)
CMD: lru_create(root.email.thread_001.key_statements, capacity: 50)
CMD: bitset_create(root.email.thread_001.messages_processed, width: 15)
```

For each message, it extracts structure and asserts Prolog facts:

```
// Process message 0
CMD: PURE_FN string_split(messages[0], "\n") → lines
CMD: PURE_FN list_filter(lines, predicate(starts_with("From:"))) → ["From: Sarah"]
CMD: PURE_FN list_filter(lines, predicate(starts_with("Date:"))) → ["Date: May 12"]

CMD: KB_ASSERT(root.email.thread_001.structure,
    fact(message(0, sender("Sarah"), date("May 12"), 
        contains_proposal("migrate to new API by Q3"))))
CMD: KB_ASSERT(root.email.thread_001.structure,
    fact(message(0, asks_question("what is the testing timeline?"))))
CMD: lru_push(root.email.thread_001.key_statements, "msg_0_proposal",
    "Sarah: migrate to new API by Q3")
CMD: bitset_set(root.email.thread_001.messages_processed, 0)

// ... process all 15 ...
CMD: bitset_count(root.email.thread_001.messages_processed) → 15
CMD: bitset_all_set(root.email.thread_001.messages_processed) → true
```

Now the LLM writes Prolog rules to analyze the thread dynamics:

```
CMD: KB_ASSERT(root.email.thread_001.analysis,
    rule(proposal(Text, Author, MsgNum) :-
        message(MsgNum, sender(Author), _, contains_proposal(Text))))

CMD: KB_ASSERT(root.email.thread_001.analysis,
    rule(agreement(Proposal, Author, MsgNum) :-
        proposal(Proposal, _, ProposalMsg),
        message(MsgNum, sender(Author), _, affirms(Proposal)),
        MsgNum > ProposalMsg))

CMD: KB_ASSERT(root.email.thread_001.analysis,
    rule(objection(Proposal, Author, Reason, MsgNum) :-
        proposal(Proposal, _, ProposalMsg),
        message(MsgNum, sender(Author), _, objects(Proposal, Reason)),
        MsgNum > ProposalMsg))

CMD: KB_ASSERT(root.email.thread_001.analysis,
    rule(unanswered_question(Question, Asker, MsgNum) :-
        message(MsgNum, sender(Asker), _, asks_question(Question)),
        not((message(LaterMsg, _, _, answers(Question)), LaterMsg > MsgNum))))

CMD: KB_ASSERT(root.email.thread_001.analysis,
    rule(resolved(Proposal) :-
        proposal(Proposal, _, _),
        findall(A, agreement(Proposal, A, _), Agreements),
        length(Agreements, N), N >= 2,
        not(objection(Proposal, _, _, _))))

CMD: KB_ASSERT(root.email.thread_001.analysis,
    rule(contested(Proposal, Objections) :-
        proposal(Proposal, _, _),
        findall(A-R, objection(Proposal, A, R, _), Objections),
        Objections \= []))
```

Query the analysis:

```
CMD: KB_QUERY(root.email.thread_001.analysis,
    findall(P, resolved(P), Resolved))
→ Resolved = ["use staging environment for testing"]

CMD: KB_QUERY(root.email.thread_001.analysis,
    findall(P-Os, contested(P, Os), Contested))
→ Contested = ["migrate to new API by Q3" - 
    [("Mike", "Q3 too aggressive"), ("Lisa", "need backward compat plan")]]

CMD: KB_QUERY(root.email.thread_001.analysis,
    findall(Q-A-M, unanswered_question(Q, A, M), Unanswered))
→ Unanswered = [("what is the testing timeline?", "Sarah", 0),
                 ("who owns the backward compat layer?", "Lisa", 9)]
```

The LLM formats the summary with exact references. Every conclusion traces to specific messages. The user sees: one resolved decision, one contested proposal with two specific objections, and two unanswered questions still hanging.

---

**List Generation: Research Compilation**

User asks "list approaches to reducing memory usage in large language models." The LLM creates a research workspace:

```
CMD: lru_create(root.research.llm_memory.sources, capacity: 40)
CMD: counter_create(root.research.llm_memory.approaches_found)
CMD: bitset_create(root.research.llm_memory.source_quality_checked, width: 40)
CMD: queue_create(root.research.llm_memory.to_investigate, capacity: 30)
```

It searches, stores findings, and pushes each approach into the investigation queue for deeper analysis:

```
// After multiple web searches
CMD: KB_ASSERT(root.research.llm_memory.findings,
    fact(approach("quantization", 
        description("reduce weight precision from fp16 to int8/int4"),
        memory_reduction(fraction(75, 100)),
        quality_impact(fraction(2, 100)),
        source("Dettmers et al 2023"),
        source_type(peer_reviewed))))
CMD: counter_inc(root.research.llm_memory.approaches_found)
CMD: lru_push(root.research.llm_memory.sources, "quantization", "Dettmers 2023")
CMD: queue_push(root.research.llm_memory.to_investigate, "quantization")

CMD: KB_ASSERT(root.research.llm_memory.findings,
    fact(approach("pruning",
        description("remove near-zero weights"),
        memory_reduction(fraction(60, 100)),
        quality_impact(fraction(5, 100)),
        source("Frantar & Alistarh 2023"),
        source_type(peer_reviewed))))
CMD: counter_inc(root.research.llm_memory.approaches_found)
CMD: queue_push(root.research.llm_memory.to_investigate, "pruning")

// ... more approaches ...
CMD: counter_get(root.research.llm_memory.approaches_found) → 8
```

The LLM writes Prolog ranking rules using exact fractions for the scoring:

```
CMD: KB_ASSERT(root.research.llm_memory.ranking,
    rule(score(Approach, Score) :-
        approach(Approach, _, memory_reduction(MR), quality_impact(QI), _, source_type(ST)),
        source_weight(ST, SW),
        Score is MR * SW - QI * fraction(2, 1)))

CMD: KB_ASSERT(root.research.llm_memory.ranking,
    rule(source_weight(peer_reviewed, fraction(10, 10))))
CMD: KB_ASSERT(root.research.llm_memory.ranking,
    rule(source_weight(industry_report, fraction(8, 10))))
CMD: KB_ASSERT(root.research.llm_memory.ranking,
    rule(source_weight(blog_post, fraction(4, 10))))

CMD: KB_QUERY(root.research.llm_memory.ranking,
    findall(A-S, score(A, S), Scores))
→ unsorted scores
CMD: PURE_FN list_sort_by_key(Scores, key(second), descending) → ranked_list
```

Now it processes the investigation queue, checking each approach for relationships with others:

```
CMD: KB_ASSERT(root.research.llm_memory.relationships,
    rule(complementary(A, B) :-
        approach(A, _, _, _, _, _), approach(B, _, _, _, _, _), A \= B,
        not(conflicts(A, B))))
CMD: KB_ASSERT(root.research.llm_memory.relationships,
    rule(conflicts(quantization, pruning_structured) :-
        true))  // structured pruning changes shapes, complicating quantization

CMD: KB_QUERY(root.research.llm_memory.relationships,
    findall(A-B, complementary(A, B), Combos))
```

The LLM uses Python to compute the combined memory reduction of complementary approaches:

```
CMD: ENV_UPLOAD(env_dev, combined_reduction.py, root.research.scripts.combine)
// Script: for each complementary pair, compute combined reduction
// assuming multiplicative independence: combined = 1 - (1-a)(1-b)
// using exact VDR fractions
CMD: ENV_EXEC(env_dev, "python3", root.research.scripts.combine)
→ {quantization+distillation: fraction(87, 100), 
   pruning+distillation: fraction(82, 100), ...}
```

The final list has exact scores, ranked by a declared formula, with source provenance, relationship analysis between approaches, and computed combination effects. Every number is an exact fraction. The user can query "why is quantization ranked first?" and get the scoring breakdown from the KB.

---

**List Generation: Decision Matrix**

User asks "help me compare three programming languages for our backend rewrite." The LLM creates the decision structure:

```
CMD: lru_create(root.decisions.backend_lang.research_cache, capacity: 30)
CMD: counter_create(root.decisions.backend_lang.criteria_count)
CMD: ring_create(root.decisions.backend_lang.discussion_points, capacity: 20)
```

It collects criteria and weights from the user, storing them as working data:

```
CMD: KB_ASSERT(root.decisions.backend_lang.criteria,
    binding("performance", fraction(3, 10)))
CMD: KB_ASSERT(root.decisions.backend_lang.criteria,
    binding("hiring_pool", fraction(2, 10)))
CMD: KB_ASSERT(root.decisions.backend_lang.criteria,
    binding("ecosystem", fraction(2, 10)))
CMD: KB_ASSERT(root.decisions.backend_lang.criteria,
    binding("learning_curve", fraction(1, 10)))
CMD: KB_ASSERT(root.decisions.backend_lang.criteria,
    binding("memory_safety", fraction(2, 10)))
CMD: counter_set(root.decisions.backend_lang.criteria_count, 5)
```

It writes a Prolog constraint to verify the weights sum to exactly 1:

```
CMD: KB_ASSERT(root.decisions.backend_lang.validation,
    rule(weights_valid :-
        findall(W, (binding(_, W), is_fraction(W)), Weights),
        vdr_sum(Weights, Sum),
        Sum =:= fraction(1, 1)))
CMD: KB_QUERY(root.decisions.backend_lang.validation, weights_valid)
→ true
```

It scores each language on each criterion, storing as a dict-like structure:

```
CMD: KB_ASSERT(root.decisions.backend_lang.scores,
    fact(score(go, performance, fraction(8, 10))))
CMD: KB_ASSERT(root.decisions.backend_lang.scores,
    fact(score(go, hiring_pool, fraction(7, 10))))
CMD: KB_ASSERT(root.decisions.backend_lang.scores,
    fact(score(go, ecosystem, fraction(7, 10))))
CMD: KB_ASSERT(root.decisions.backend_lang.scores,
    fact(score(go, learning_curve, fraction(8, 10))))
CMD: KB_ASSERT(root.decisions.backend_lang.scores,
    fact(score(go, memory_safety, fraction(6, 10))))

// ... same for rust and kotlin ...
```

Prolog computes weighted totals with exact fractions:

```
CMD: KB_ASSERT(root.decisions.backend_lang.computation,
    rule(weighted_total(Lang, Total) :-
        findall(W*S, 
            (binding(Criterion, W), score(Lang, Criterion, S)), 
            Products),
        sum_products(Products, Total)))

CMD: KB_QUERY(root.decisions.backend_lang.computation,
    findall(L-T, weighted_total(L, T), Totals))
→ [go-fraction(71,100), rust-fraction(74,100), kotlin-fraction(68,100)]
CMD: PURE_FN list_sort_by_key(Totals, key(second), descending)
→ [rust-74/100, go-71/100, kotlin-68/100]
```

Close race between Rust and Go. The LLM logs the discussion point:

```
CMD: ring_write(root.decisions.backend_lang.discussion_points,
    "Rust leads by 3% — within sensitivity range. 
     Changing performance weight from 30% to 25% might flip the ranking.")
```

It writes Python to do sensitivity analysis — which weight changes would flip the outcome:

```
CMD: ENV_UPLOAD(env_dev, sensitivity.py, root.decisions.scripts.sensitivity)
// Script: for each criterion, find the weight change threshold
// that would change the winner, using exact fractions
CMD: ENV_EXEC(env_dev, "python3", root.decisions.scripts.sensitivity)
→ {performance: "if reduced to 22/100, Go wins",
   memory_safety: "if reduced to 12/100, Go wins",
   hiring_pool: "if increased to 28/100, Go wins"}
```

The decision matrix has exact scores, verified weight constraints, sensitivity analysis, and logged discussion points. The user can change any weight and the ranking recomputes from exact fractions.

---

**Creative: Worldbuilding Consistency**

User is writing a fantasy novel. The LLM maintains the world state:

```
CMD: lru_create(root.stories.novel.recent_events, capacity: 50)
CMD: counter_create(root.stories.novel.chapter_count)
CMD: counter_create(root.stories.novel.consistency_violations)
CMD: bitset_create(root.stories.novel.characters_introduced, width: 100)
CMD: stack_create(root.stories.novel.plot_threads, capacity: 20)
CMD: lock_create(root.stories.novel.timeline_locked)
```

As the user writes chapters, the LLM extracts world facts and asserts them:

```
CMD: KB_ASSERT(root.stories.novel.world_rules,
    fact(magic_affinity(fire, faction(southern_guild))))
CMD: KB_ASSERT(root.stories.novel.world_rules,
    fact(banned_in(southern_guild, region(northern_province))))
CMD: KB_ASSERT(root.stories.novel.world_rules,
    fact(character(maya, faction(southern_guild), magic(fire))))
CMD: KB_ASSERT(root.stories.novel.world_rules,
    fact(character(kael, faction(northern_court), magic(ice))))
CMD: bitset_set(root.stories.novel.characters_introduced, 0)  // maya
CMD: bitset_set(root.stories.novel.characters_introduced, 1)  // kael

CMD: KB_ASSERT(root.stories.novel.world_rules,
    rule(violation(Character, Action, Region, Reason) :-
        character(Character, faction(F), _),
        event(Character, Action, Region),
        banned_in(F, Region),
        Reason = faction_banned))

CMD: KB_ASSERT(root.stories.novel.world_rules,
    rule(violation(Character, uses_magic(Type), Region, Reason) :-
        character(Character, _, magic(Type)),
        magic_affinity(Type, faction(F)),
        character(Character, faction(CF), _),
        CF \= F,
        Reason = wrong_faction_for_magic))
```

User writes a new scene: "Maya travels to the Northern Province and uses fire magic to light a signal."

```
CMD: KB_ASSERT(root.stories.novel.chapter_7,
    fact(event(maya, travels_to, northern_province)))
CMD: KB_ASSERT(root.stories.novel.chapter_7,
    fact(event(maya, uses_magic(fire), northern_province)))
CMD: lru_push(root.stories.novel.recent_events, "ch7_scene1",
    "Maya uses fire magic in Northern Province")
CMD: counter_inc(root.stories.novel.chapter_count)

// Check for violations
CMD: KB_QUERY(root.stories.novel.world_rules,
    findall(V, violation(maya, _, _, V), Violations))
→ Violations = [faction_banned]
CMD: counter_inc(root.stories.novel.consistency_violations)
```

The LLM reports: "Consistency issue — Maya is Southern Guild, which is banned in the Northern Province. Options: (1) she's traveling in disguise, (2) the ban was recently lifted, (3) she's defecting." It pushes each option as a plot thread:

```
CMD: stack_push(root.stories.novel.plot_threads, 
    "unresolved: Maya's presence in Northern Province needs justification")
```

The user says "she's traveling in disguise." The LLM updates:

```
CMD: KB_ASSERT(root.stories.novel.chapter_7,
    fact(condition(maya, disguised_as(northern_merchant), northern_province)))
CMD: KB_ASSERT(root.stories.novel.world_rules,
    rule(exemption(Character, Region, disguise) :-
        condition(Character, disguised_as(_), Region)))

// Recheck — violation should be resolved with exemption
CMD: KB_ASSERT(root.stories.novel.world_rules,
    rule(effective_violation(Character, Action, Region, Reason) :-
        violation(Character, Action, Region, Reason),
        not(exemption(Character, Region, _))))

CMD: KB_QUERY(root.stories.novel.world_rules,
    findall(V, effective_violation(maya, _, _, V), ActiveViolations))
→ ActiveViolations = []
CMD: counter_dec(root.stories.novel.consistency_violations)
CMD: stack_pop(root.stories.novel.plot_threads)  // resolved
```

But the disguise creates a new tension — the LLM writes a rule for it:

```
CMD: KB_ASSERT(root.stories.novel.world_rules,
    rule(tension(Character, discovery_risk, Region) :-
        condition(Character, disguised_as(_), Region),
        character(Character, faction(F), _),
        banned_in(F, Region)))

CMD: stack_push(root.stories.novel.plot_threads,
    "active tension: Maya could be discovered in Northern Province")
```

Twenty chapters later, the user can query:

```
CMD: stack_to_list(root.stories.novel.plot_threads)
→ all unresolved plot threads
CMD: counter_get(root.stories.novel.consistency_violations) → 0
CMD: bitset_count(root.stories.novel.characters_introduced) → 23
CMD: lru_peek(root.stories.novel.recent_events, 10) → last 10 events
```

---

**Teaching: Socratic Dialogue**

Student asks "why is binary search O(log n)?" The LLM doesn't just explain — it builds an interactive proof the student can query:

```
CMD: counter_create(root.teaching.binary_search.student_steps)
CMD: lru_create(root.teaching.binary_search.student_answers, capacity: 20)
CMD: bitset_create(root.teaching.binary_search.concepts_understood, width: 5)
// bit 0: halving, bit 1: recursion, bit 2: base case, 
// bit 3: counting halvings, bit 4: log definition
CMD: stack_create(root.teaching.binary_search.hint_stack, capacity: 10)
```

The LLM prepares the Prolog model and pushes hints onto a stack for progressive disclosure:

```
CMD: stack_push(root.teaching.binary_search.hint_stack,
    "What happens to the search space after each comparison?")
CMD: stack_push(root.teaching.binary_search.hint_stack,
    "If you start with 1000 elements and halve each time, how many steps to reach 1?")
CMD: stack_push(root.teaching.binary_search.hint_stack,
    "2^10 = 1024 ≈ 1000. What does the exponent 10 represent?")
CMD: stack_push(root.teaching.binary_search.hint_stack,
    "log₂(n) is the number of times you can halve n before reaching 1")

CMD: KB_ASSERT(root.teaching.binary_search.model,
    fact(array_size(16)))
CMD: KB_ASSERT(root.teaching.binary_search.model,
    rule(search_space(0, N) :- array_size(N)))
CMD: KB_ASSERT(root.teaching.binary_search.model,
    rule(search_space(Step, Size) :-
        PrevStep is Step - 1,
        search_space(PrevStep, PrevSize),
        Size is PrevSize // 2,
        Size > 0))
CMD: KB_ASSERT(root.teaching.binary_search.model,
    rule(steps_needed(N, Steps) :-
        findall(S, search_space(S, _), AllSteps),
        length(AllSteps, Steps)))
```

The LLM asks the first question by popping the hint stack:

```
TEXT: "Let's figure this out together. Say you have 16 sorted elements."
CMD: stack_peek(root.teaching.binary_search.hint_stack)
→ "What happens to the search space after each comparison?"
TEXT: "What happens to the number of elements you need to look at 
      after you check the middle element?"
CMD: counter_inc(root.teaching.binary_search.student_steps)
```

Student says "it gets cut in half."

```
CMD: lru_push(root.teaching.binary_search.student_answers, "step_1",
    "correct: search space halves")
CMD: bitset_set(root.teaching.binary_search.concepts_understood, 0)  // halving understood
CMD: stack_pop(root.teaching.binary_search.hint_stack)  // consume used hint
```

The LLM uses Python to trace the actual search with the student:

```
CMD: ENV_UPLOAD(env_dev, trace_search.py, root.teaching.scripts.trace)
// Script: binary search on [1..16], target=11, 
// print search space at each step as exact count
CMD: ENV_EXEC(env_dev, "python3", root.teaching.scripts.trace)
→ "Step 0: 16 elements → Step 1: 8 → Step 2: 4 → Step 3: 2 → Step 4: 1. Found at step 4."
```

```
TEXT: "Look at the trace: 16 → 8 → 4 → 2 → 1. That's 4 steps."
CMD: stack_peek(root.teaching.binary_search.hint_stack)
→ "If you start with 1000 elements and halve each time, how many steps to reach 1?"
TEXT: "Now — if you started with 1000 elements instead of 16, 
      how many halvings would it take?"
CMD: counter_inc(root.teaching.binary_search.student_steps)
```

Student says "about 10."

```
CMD: lru_push(root.teaching.binary_search.student_answers, "step_2", "correct: ~10")
CMD: bitset_set(root.teaching.binary_search.concepts_understood, 3)  // counting halvings
CMD: stack_pop(root.teaching.binary_search.hint_stack)

// Verify with Prolog
CMD: KB_ASSERT(root.teaching.binary_search.model,
    fact(array_size_alt(1000)))
CMD: KB_QUERY(root.teaching.binary_search.model,
    steps_needed(1000, S))
→ S = 10
```

Student got it right. The LLM checks the concept bitset:

```
CMD: bitset_to_list(root.teaching.binary_search.concepts_understood) → [0, 3]
// Understood: halving (0), counting halvings (3)
// Missing: recursion (1), base case (2), log definition (4)
```

Three concepts still to cover. The LLM continues with targeted questions for each gap, using the hint stack for progressive disclosure and the bitset to track exactly which concepts the student has demonstrated understanding of. When all 5 bits are set, the lesson is complete.

---

**Research: Literature Review**

User asks about a specific research area. The LLM creates the research infrastructure:

```
CMD: lru_create(root.research.survey.papers, capacity: 50)
CMD: counter_create(root.research.survey.papers_found)
CMD: counter_create(root.research.survey.papers_analyzed)
CMD: bitset_create(root.research.survey.themes_covered, width: 10)
CMD: queue_create(root.research.survey.to_analyze, capacity: 30)
CMD: ring_create(root.research.survey.methodology_notes, capacity: 20)
CMD: lock_create(root.research.survey.analysis_in_progress)
```

After searching, it stores each paper and queues it for analysis:

```
CMD: KB_ASSERT(root.research.survey.papers_kb,
    fact(paper("p001", title("Exact Arithmetic in Neural Networks"),
        authors(["Smith", "Jones"]), year(2024), 
        venue("NeurIPS"), citations(45))))
CMD: counter_inc(root.research.survey.papers_found)
CMD: queue_push(root.research.survey.to_analyze, "p001")
CMD: lru_push(root.research.survey.papers, "p001", "Smith & Jones 2024 — exact arithmetic NN")
```

It locks the analysis phase and processes the queue:

```
CMD: lock_acquire(root.research.survey.analysis_in_progress, holder: "deep_analysis")

CMD: queue_pop(root.research.survey.to_analyze) → "p001"
```

For each paper, it writes Prolog facts encoding its claims and relationships:

```
CMD: KB_ASSERT(root.research.survey.analysis,
    fact(paper_claims("p001", 
        [claim(exact_fractions_eliminate_drift, supported),
         claim(performance_cost_10x, measured),
         claim(scales_to_1M_params, demonstrated)])))

CMD: KB_ASSERT(root.research.survey.analysis,
    fact(paper_relationship("p001", extends, "p007")))
CMD: KB_ASSERT(root.research.survey.analysis,
    fact(paper_relationship("p001", contradicts, "p012")))
CMD: KB_ASSERT(root.research.survey.analysis,
    fact(paper_methodology("p001", experimental, controlled)))

CMD: counter_inc(root.research.survey.papers_analyzed)
CMD: ring_write(root.research.survey.methodology_notes,
    "p001: experimental, controlled, but only tested on small models <1M params")
```

After analyzing all papers, it uses graph primitives on the citation and relationship network:

```
CMD: PURE_FN graph_from_edges(all_paper_relationships) → citation_graph
CMD: PURE_FN graph_connected_components(citation_graph) → clusters
CMD: PURE_FN graph_pagerank(citation_graph, fraction(85, 100)) → influence_scores
CMD: PURE_FN list_sort_by_key(influence_scores, key(second), descending) → ranked_papers
```

It writes Prolog to identify research gaps — claims made by only one paper with no replication:

```
CMD: KB_ASSERT(root.research.survey.gap_analysis,
    rule(unreplicated_claim(Claim, Paper) :-
        paper_claims(Paper, Claims),
        member(claim(Claim, _), Claims),
        findall(P2, (paper_claims(P2, C2), member(claim(Claim, _), C2), P2 \= Paper), Others),
        Others = []))

CMD: KB_QUERY(root.research.survey.gap_analysis,
    findall(C-P, unreplicated_claim(C, P), Gaps))
→ gaps with provenance
```

It identifies contradictions:

```
CMD: KB_ASSERT(root.research.survey.contradictions,
    rule(active_contradiction(Claim, Paper1, Paper2) :-
        paper_claims(Paper1, C1), member(claim(Claim, supported), C1),
        paper_claims(Paper2, C2), member(claim(Claim, refuted), C2)))

CMD: KB_QUERY(root.research.survey.contradictions,
    findall(C-P1-P2, active_contradiction(C, P1, P2), Contradictions))
```

The literature review has a citation graph with PageRank influence scores, thematic clusters, unreplicated claims, active contradictions between papers, and methodology notes in a rolling buffer. Every finding is queryable and traceable to specific papers.

```
CMD: lock_release(root.research.survey.analysis_in_progress)
CMD: bitset_to_list(root.research.survey.themes_covered)
→ which themes still need papers
```

---

**Planning: Project Decomposition**

User says "plan the implementation of a new microservice." The LLM builds the plan as a formal structure:

```
CMD: queue_create(root.project.microservice.task_queue, capacity: 50)
CMD: stack_create(root.project.microservice.blocked_stack, capacity: 20)
CMD: counter_create(root.project.microservice.total_tasks)
CMD: counter_create(root.project.microservice.completed_tasks)
CMD: bitset_create(root.project.microservice.milestones, width: 8)
CMD: lock_create(root.project.microservice.deployment_gate)
CMD: ring_create(root.project.microservice.daily_progress, capacity: 30)
```

It formalizes tasks and dependencies in Prolog:

```
CMD: KB_ASSERT(root.project.microservice.plan,
    fact(task(t01, "define API schema", effort(2), milestone(0))))
CMD: KB_ASSERT(root.project.microservice.plan,
    fact(task(t02, "implement handlers", effort(5), milestone(1))))
CMD: KB_ASSERT(root.project.microservice.plan,
    fact(task(t03, "write unit tests", effort(3), milestone(1))))
CMD: KB_ASSERT(root.project.microservice.plan,
    fact(task(t04, "integration tests", effort(3), milestone(2))))
CMD: KB_ASSERT(root.project.microservice.plan,
    fact(task(t05, "load testing", effort(2), milestone(3))))
CMD: KB_ASSERT(root.project.microservice.plan,
    fact(task(t06, "deploy to staging", effort(1), milestone(4))))
CMD: KB_ASSERT(root.project.microservice.plan,
    fact(task(t07, "security review", effort(2), milestone(5))))
CMD: KB_ASSERT(root.project.microservice.plan,
    fact(task(t08, "deploy to production", effort(1), milestone(6))))

CMD: KB_ASSERT(root.project.microservice.plan,
    fact(depends(t02, t01)))
CMD: KB_ASSERT(root.project.microservice.plan,
    fact(depends(t03, t02)))
CMD: KB_ASSERT(root.project.microservice.plan,
    fact(depends(t04, t03)))
CMD: KB_ASSERT(root.project.microservice.plan,
    fact(depends(t05, t04)))
CMD: KB_ASSERT(root.project.microservice.plan,
    fact(depends(t06, t05)))
CMD: KB_ASSERT(root.project.microservice.plan,
    fact(depends(t07, t06)))
CMD: KB_ASSERT(root.project.microservice.plan,
    fact(depends(t08, t07)))

CMD: counter_set(root.project.microservice.total_tasks, 8)
```

It uses graph primitives for planning analysis:

```
CMD: PURE_FN graph_from_edges(dependencies) → dep_graph
CMD: PURE_FN graph_topological_sort(dep_graph) → execution_order
CMD: PURE_FN graph_shortest_path(dep_graph, t01, t08) → critical_path

// Prolog computes total critical path effort
CMD: KB_ASSERT(root.project.microservice.plan,
    rule(critical_path_effort(Total) :-
        critical_path(Path),
        findall(E, (member(T, Path), task(T, _, effort(E), _)), Efforts),
        vdr_sum(Efforts, Total)))
CMD: KB_QUERY(root.project.microservice.plan, critical_path_effort(Total))
→ Total = 19 days

// Find parallelizable tasks
CMD: KB_ASSERT(root.project.microservice.plan,
    rule(parallelizable(T1, T2) :-
        task(T1, _, _, _), task(T2, _, _, _), T1 \= T2,
        not(depends(T1, T2)), not(depends(T2, T1)),
        not((depends(T1, Common), depends(T2, Common)))))
```

It loads the execution order into the task queue:

```
CMD: queue_push(root.project.microservice.task_queue, t01)
CMD: queue_push(root.project.microservice.task_queue, t02)
// ... in topological order ...
```

As tasks complete:

```
CMD: queue_pop(root.project.microservice.task_queue) → t01
// ... work happens ...
CMD: counter_inc(root.project.microservice.completed_tasks)
CMD: bitset_set(root.project.microservice.milestones, 0)  // API schema milestone
CMD: ring_write(root.project.microservice.daily_progress,
    "Day 2: API schema complete, handlers started")
```

Before production deployment, the lock gate ensures all prerequisites are met:

```
CMD: KB_ASSERT(root.project.microservice.plan,
    rule(deploy_ready :-
        bitset_all_set(milestones, [0,1,2,3,4,5]),
        counter_get(completed_tasks, C),
        counter_get(total_tasks, T),
        C =:= T - 1))  // all but deploy itself

CMD: KB_QUERY(root.project.microservice.plan, deploy_ready)
→ true
CMD: lock_release(root.project.microservice.deployment_gate)
// Now deployment task can proceed
```

---

**Data Quality: Investigation**

User says "our model accuracy dropped after the last data update." The LLM structures the investigation:

```
CMD: counter_create(root.ops.data_investigation.hypotheses_tested)
CMD: counter_create(root.ops.data_investigation.sources_checked)
CMD: lru_create(root.ops.data_investigation.findings, capacity: 30)
CMD: bitset_create(root.ops.data_investigation.sources_cleared, width: 20)
CMD: queue_create(root.ops.data_investigation.check_queue, capacity: 20)
CMD: stack_create(root.ops.data_investigation.investigation_path, capacity: 15)
CMD: lock_acquire(root.ops.data_investigation.active, holder: "accuracy_drop")
```

It queries the lifecycle KB for changed data sources:

```
CMD: KB_QUERY(root.project.model.sources, 
    findall(S, (source(S, added_in(update_v7))), NewSources))
→ NewSources = [source_news_2026_04, source_code_github_v2, source_forums_v1]

// Queue each for investigation
CMD: queue_push(root.ops.data_investigation.check_queue, "source_news_2026_04")
CMD: queue_push(root.ops.data_investigation.check_queue, "source_code_github_v2")
CMD: queue_push(root.ops.data_investigation.check_queue, "source_forums_v1")
```

It pushes the investigation strategy onto the stack:

```
CMD: stack_push(root.ops.data_investigation.investigation_path,
    "phase: checking each new source for quality issues")
```

For each source, it writes Python to measure its impact:

```
CMD: queue_pop(root.ops.data_investigation.check_queue) → "source_news_2026_04"
CMD: counter_inc(root.ops.data_investigation.sources_checked)

CMD: ENV_UPLOAD(env_analysis, check_source.py, root.ops.scripts.check)
// Script: compute accuracy on validation subset from this source only
CMD: ENV_EXEC(env_analysis, "python3", root.ops.scripts.check)
→ {accuracy_on_source: fraction(62, 100), baseline_accuracy: fraction(91, 100)}
```

Major discrepancy. The LLM records the finding:

```
CMD: lru_push(root.ops.data_investigation.findings, "news_2026_04",
    "accuracy 62% vs 91% baseline — major quality issue")
CMD: KB_ASSERT(root.ops.data_investigation.evidence,
    fact(source_anomaly("source_news_2026_04", 
        accuracy_on_source(fraction(62, 100)),
        expected(fraction(91, 100)),
        delta(fraction(-29, 100)))))
```

It digs deeper with Prolog to find why:

```
CMD: KB_ASSERT(root.ops.data_investigation.analysis,
    rule(likely_cause(Source, language_contamination) :-
        source_anomaly(Source, _, _, _),
        source_quality(Source, language_confidence(LC)),
        LC < fraction(90, 100)))
CMD: KB_ASSERT(root.ops.data_investigation.analysis,
    rule(likely_cause(Source, duplication) :-
        source_anomaly(Source, _, _, _),
        source_quality(Source, dedup_ratio(DR)),
        DR > fraction(5, 100)))
CMD: KB_ASSERT(root.ops.data_investigation.analysis,
    rule(likely_cause(Source, domain_mismatch) :-
        source_anomaly(Source, accuracy_on_source(A), expected(E), _),
        A < E * fraction(7, 10)))

CMD: KB_QUERY(root.ops.data_investigation.analysis,
    findall(C, likely_cause("source_news_2026_04", C), Causes))
→ Causes = [domain_mismatch]
CMD: counter_inc(root.ops.data_investigation.hypotheses_tested)
```

Python confirms with a sample inspection:

```
CMD: ENV_UPLOAD(env_analysis, sample_inspect.py, root.ops.scripts.sample)
// Script: random sample of 100 docs from this source, 
// compute language scores and topic distribution
CMD: ENV_EXEC(env_analysis, "python3", root.ops.scripts.sample)
→ {non_english_percentage: fraction(34, 100), 
   topic_distribution: {sports: fraction(45, 100), 
                        finance: fraction(30, 100), 
                        tech: fraction(25, 100)}}
```

34% non-English content in a supposedly English corpus. Found it.

```
CMD: lru_push(root.ops.data_investigation.findings, "root_cause",
    "source_news_2026_04: 34% non-English, language filter failed")
CMD: bitset_set(root.ops.data_investigation.sources_cleared, 1)  // github cleared
CMD: bitset_set(root.ops.data_investigation.sources_cleared, 2)  // forums cleared
// source 0 (news) NOT cleared — it's the problem

CMD: stack_push(root.ops.data_investigation.investigation_path,
    "root cause found: language contamination in news source")
CMD: stack_push(root.ops.data_investigation.investigation_path,
    "remediation: exclude source, retrain, add language check constraint")

// Write permanent rule to prevent recurrence
CMD: KB_ASSERT(root.project.model.constraints,
    constraint("source_language_purity", operational, active,
        condition(forall(source(S), language_confidence(S) > fraction(95, 100))),
        on_violation("block_training")))

CMD: lock_release(root.ops.data_investigation.active)
```

The full investigation path is on the stack, all findings are in the LRU, the bitset shows which sources were cleared and which weren't, the counter shows how many hypotheses were tested, and a permanent constraint prevents the same issue from recurring.

---

The pattern across all domains is the same: the LLM uses the data primitives as organizational scaffolding — queues for plans and pending work, stacks for undo and investigation paths, LRUs for recent context, counters for progress and budgets, bitsets for completion tracking, locks for coordination, ring buffers for rolling history. Prolog handles deduction and constraint verification. Python handles computation and data gathering. String and list primitives handle parsing and filtering. The LLM orchestrates all of it through compact command token references. None of these tools reason. The LLM doesn't compute. Together they cover the full loop: observe, hypothesize, gather, deduce, act, verify, record.
