# The Discovery Process

## A Systematic Method for Omni-Domain Investigation, Construction, and Verification

**Registry:** [@HOWL-DISC-1-2026]

**DOI:** 10.5281/zenodo.zzz

**Date:** February 2026

**Domain:** Applied Philosophy

**Status:** Working Methodology

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6. 

---

## Section 1 — The Problem of Discovery Across Domains

Every human discipline maintains boundaries. Physics is not biology. Engineering is not music. Medicine is not mathematics. Neuroscience is not martial arts. These boundaries organize departments, journals, careers, and funding streams. They determine who reviews whose work, who gets hired into which building, who attends which conference.

They do not organize reality.

A muscle contraction generates an electromagnetic field, obeys the laws of physics, is controlled by neural circuitry, can be trained through martial arts, is repaired through medical intervention, and can be modeled in a game engine. The muscle does not know which department it belongs to. It belongs to all of them and none of them.

When a question crosses boundaries — "how does the body coordinate faster than nerves can conduct?" or "can arithmetic preserve exact equality without floating point?" or "how does a game engine process entities without compiled behavior code?" — the institutional response is to assign the question to whichever department has the strongest jurisdictional claim. That department's methods, assumptions, vocabulary, and career incentives then govern the investigation. The contributions from other domains are acknowledged in the literature review and ignored in the methodology.

The result is that cross-domain questions either go unasked — because no single department owns them — or get answered within one framework while the evidence from other frameworks sits unused.

This paper describes an alternative. A discovery process that operates without domain boundaries, consumes from every available source, integrates without walls, builds from known good components, verifies by trying to find the break rather than confirm the result, publishes failures alongside successes, and iterates continuously. The process is not a theory of how discovery should work. It is a description of how one practitioner has worked across engineering, physics, mathematics, neuroscience, martial arts, music, and software architecture for several decades, formalized from practice and documented with complete transparency.

The process requires no credentials, no institutional backing, no funding, and no permission. It requires curiosity, discipline, the willingness to be wrong in public, and access to tools that are available to anyone.

---

## Section 2 — Intake: Consume Without Filtering by Domain

The first layer of the process is intake — actively seeking information from every available source regardless of its traditional disciplinary home.

A systems engineer learning movement rehabilitation from a sports neuroscience program is not stepping outside their lane. They are recognizing that the body is a system, movement is signal processing, and rehabilitation is debugging. The vocabulary is different. The problem is the same.

A game engine developer studying baguazhang circle-walking is not having a midlife crisis. They are recognizing that coordinated multi-joint movement in a martial art and coordinated multi-entity updates in a game engine are both instances of the same synchronization problem. Different substrate, same engineering.

The intake layer admits everything. Physics, engineering, martial arts, music, medicine, parenting, construction, history, philosophy, ancient arithmetic — all are valid sources. The filter is not on the domain. The filter is on the source quality.

### Source coherency

A source is high-coherency if it meets three criteria: it is internally consistent, it produces measurable results, and it has been tested against reality.

A martial arts lineage that produces practitioners who can demonstrate the claimed capabilities in sparring against resistant opponents is a high-coherency source for body mechanics. A programming language that compiles predictably, handles errors explicitly, and has been tested in production systems is a high-coherency source for software methodology. A movement rehabilitation system whose patients show measurable improvement in proprioception, balance, and pain reduction is a high-coherency source for neuromuscular function.

A management theory that produces no measurable improvement in the organizations that adopt it is a low-coherency source regardless of the prestige of its author or the number of citations it has received. A physics framework that produces numbers matching measurement but requires 26 unexplained parameters is a partially coherent source — the numbers work, but the unexplained parameters indicate gaps in the underlying understanding.

The intake filter admits high-coherency sources from any domain and is skeptical of low-coherency sources from every domain, including prestigious ones. Prestige and coherency are not the same thing. A source can be prestigious and incoherent, or obscure and highly coherent. The intake layer doesn't care about reputation. It cares about whether the source's outputs match the source's claims when tested.

### Why broad intake matters

The discovery process assumes that structural similarities across domains are real, not metaphorical. When the timing problem in neural coordination, the frame synchronization problem in game engines, and the ensemble timing problem in orchestral music all have the same mathematical structure, that is not a coincidence or a poetic analogy. It is one problem appearing in three domains. The solution in one domain constrains the solution in the others.

Broad intake is the only way to see these structural identities. A person who reads only neuroscience will never notice that the body's coordination problem is the same problem a game engine solves sixty times per second. A person who reads only game engine architecture will never notice that entity synchronization has the same timing constraints as postural balance. The connections exist in reality. They are invisible from inside any single domain.

---

## Section 3 — Integration: Connect Without Walls

The second layer is integration. Every new input is tested against everything already held — not sorted into a domain-specific compartment but checked for connections, contradictions, and structural identities across the entire body of knowledge the practitioner holds.

### Connections

When a new input connects to an existing holding, the connection is noted. It is not forced or invented. It either exists structurally or it doesn't.

The connection between body coordination timing and game engine frame synchronization is structural: both require phase-locked activation of distributed actuators within a timing window shorter than the communication delay of the slowest available channel. That structural identity constrains both domains. A solution that works for game engines (parallel broadcast to all entities simultaneously) suggests an architecture for body coordination (field broadcast to all muscles simultaneously). The suggestion is not proof. It is a direction for investigation that would not have been visible from inside either domain alone.

### Contradictions

When a new input contradicts an existing holding, both stay on the table. Neither is automatically preferred. Both carry their source metadata — who said it, when, under what conditions, at what confidence level, with what scope of applicability.

The process treats premature resolution of contradictions as the primary source of error in the integration layer. Collapsing to one answer before the evidence justifies it discards information. The discarded information may have been the key to resolving the contradiction correctly. So contradictions are held, with their metadata, until the evidence closes them. If the evidence never closes them, they remain open. Permanently open contradictions with full metadata are more valuable than prematurely resolved contradictions with lost information.

### Multi-dimensional indexing

Every claim or observation held in the integration layer carries metadata across multiple dimensions. This is not an informal habit — it is a deliberate practice with specific dimensions tracked for every item.

Source: who said it, where it came from, what their track record is. Temporal context: when it was true, under what conditions, whether those conditions still hold. Confidence level: directly stated by the source, inferred by the practitioner, or speculative. Scope of applicability: under what circumstances it holds and under what circumstances it might not. Relationship to other held items: supports, contradicts, independent, or structurally identical.

This multi-dimensional metadata prevents the collapse of nuanced information into a single binary true/false assessment. Two contradictory claims can both be held with full metadata — one true under condition A, the other true under condition B — without the practitioner needing to choose between them until the evidence identifies which condition actually applies.[¹]

### Integration is not confusion

Integration without walls does not mean integration without structure. The structure is in the metadata, not in domain boundaries. Two claims from different domains with the same structural form and compatible metadata are treated as related, and that relationship is tested. Two claims from the same domain with incompatible metadata are treated as contradictory, and that contradiction is held open.

The practitioner is not mixing things up. The practitioner is holding more dimensions than a single-domain framework provides, and using those dimensions to see structure that domain boundaries obscure.

---

## Section 4 — Evaluation: Weigh What Matters

The third layer is evaluation. Not everything that connects or contradicts is worth investigating deeply. Time is finite. The evaluation layer determines where to spend it.

### The materiality test

Before investing effort in a connection or contradiction, ask three questions.

Does this change the outcome of something I am building or investigating? If the answer is no — if the item is interesting but affects nothing currently active — it is noted with its metadata and shelved. Not dismissed. Shelved. It may become material when the active work shifts.

What is the scope? If it affects five percent or less of cases, it is minor. If it affects fifty percent or more, it is critical. The scope determines the urgency, not the interestingness.

What is the fruit? Does pursuing this line produce results consistent with what it claims? If a hypothesis says it explains motor coordination but the people who train under its principles cannot demonstrably coordinate better, the fruit contradicts the claim. If a tool claims to increase productivity but the projects built with it take longer, the fruit contradicts the claim. The fruit of the plant is a validation test applied to the claim's own stated goals.[²]

### One-step advancement

Understanding is built one step at a time. Before advancing to the next step, the current step must be verified as solid.

This principle applies to self-directed investigation, to collaboration with other humans, and to collaboration with machines. The process never dumps the full complexity of a problem at once, never skips a step because it seems obvious, and never advances past a step that hasn't been confirmed as understood.

Each step is calibrated to the current state of understanding. If the current understanding is "I don't know what EMF means," the next step is "EMF stands for electromagnetic field, which is the field generated by moving electric charges." If the current understanding is "I know Maxwell's equations," the next step is "the propagation speed in tissue is modified by the permittivity." The step size adapts to the receiver. The direction is always forward. The pace is always one step.[³]

### Information locality

Information is most useful closest to where it was generated. A direct observation of a phenomenon is higher-locality than a textbook description, which is higher-locality than a summary of the textbook, which is higher-locality than a cultural consensus about what the textbook says.

The evaluation layer preferentially seeks high-locality information. When the question is "does a railroad compensate for earth curvature?" the highest-locality source is a railroad engineer who has laid track. When the question is "can the body coordinate faster than nerve conduction?" the highest-locality source is the measured conduction speed and the measured coordination timing, not the textbook's interpretation of what those measurements mean.

This does not mean institutional consensus is always wrong. It means institutional consensus is evaluated on the same terms as any other source. When consensus conflicts with direct observation, both are held with their metadata. Neither is automatically preferred. The observation gets scrutinized. The consensus gets scrutinized. Whichever survives scrutiny is the one that stays.[⁴]

### Not holding on

The evaluation layer requires a cognitive state that is difficult to describe but essential to practice. The practitioner must be willing to hold claims without becoming attached to them. To investigate a direction without needing it to be true. To invest weeks of work in a framework and then kill it in an afternoon if the verification finds a break.

This is not detachment in the sense of not caring. The practitioner cares deeply about the question. What they do not do is carry a position as identity. A framework is a tool, not a self. When the tool breaks, you put it down and pick up a better one. You do not defend the broken tool because you spent time making it.

This is the hardest part of the process. Human cognition naturally converts investment into attachment. The more time you spend on a position, the more it feels like yours, and the harder it is to release when the evidence turns against it. The process treats this natural tendency as a failure mode to be actively monitored and counteracted.

The monitoring is continuous. Am I holding this position because the evidence supports it, or because I have invested effort in it? Am I rejecting this observation because it is wrong, or because it threatens my framework? Am I forcing this resolution because the evidence is sufficient, or because I want to move forward? These questions are asked not once but continuously, throughout every investigation, as a background process that never stops running.

---

## Section 5 — Construction: Build From Known Good Components

The fourth layer is construction. When enough inputs have been integrated and evaluated, the process moves from understanding to building.

### Building is understanding

In this process, building is not the application of understanding. Building is the understanding. You do not fully understand a system until you have built it. The act of building exposes every gap, every unstated assumption, every connection that looked solid in theory and fails in implementation. The compiler does not accept "I think this should work." The compiler accepts code that works or it rejects code that doesn't. The build is the most honest test of understanding available.

This is why the process moves to construction as soon as the evaluation layer indicates that understanding is sufficient. Not when understanding is complete — understanding is never complete. When it is sufficient to begin building, and the build itself will reveal the gaps.

### Known good components

Construction uses components that have demonstrated internal consistency and practical results in their own domains. The novelty is in the integration — the new configuration — not in the individual components.

A known good component is one that works reliably within its characterized domain and fails explicitly rather than silently when pushed beyond that domain. A programming language that crashes with a clear error message when misused is known good. A language that silently produces wrong results is not. An arithmetic system that returns either an exact result or an explicit failure is known good. One that returns an approximate result without indicating the approximation is not.

The practitioner assembles known good components into configurations that have not been tried before. The game engine uses a known good programming language, a known good logic system, and a known good scoring algorithm, assembled into a data-only execution architecture that is new. The neuroscience paper uses known good conduction speed measurements, known good control theory, and known good electromagnetic physics, assembled into an elimination argument that is new. The novelty is always in the assembly. The components are always proven.

### Zero latency

The interval between "I have enough understanding to build" and "I am building" is zero.

No proposal. No committee review. No grant application. No literature review period. No waiting for institutional approval. No scheduling a meeting to discuss the timeline for beginning. The understanding is sufficient, the tools are available, the build begins.

Zero latency is not recklessness. The evaluation layer ensures that understanding is sufficient before construction starts. The practitioner does not build before they are ready. But once ready, they do not wait. Waiting adds no understanding. Waiting adds no quality. Waiting costs time, which is the only non-renewable resource in the process.

The difference in output between a process that iterates at zero latency and a process that iterates through institutional review cycles is not incremental. It is orders of magnitude. A question asked at 2 AM can produce a built, tested, verified result by morning. An institutional process may take months to produce a proposal to investigate the same question.

---

## Section 6 — Verification: Find the Break

The fifth layer is verification, and it operates on a principle that is opposite to how most people think about testing.

The purpose of verification in this process is not to confirm that the result is correct. The purpose is to find where the result is wrong. If the result survives the attempt to break it, confidence follows as a consequence. If the result does not survive, the failure is the most valuable output of the entire cycle — more valuable than confirmation would have been, because the failure tells you exactly where the understanding was wrong and therefore exactly where to improve it.

### Mechanical verification

The process preferentially uses mechanical verification wherever possible. A compiler checking code. A script checking arithmetic. A measured quantity checking a prediction. Mechanical verification does not suffer from a failure mode that afflicts both human and machine evaluation.

That failure mode is the tendency to approve a result because it is coherent rather than because it is correct. Coherence means internal consistency — every piece connects to every other piece, the framework has no visible seams, the logic flows without interruption. Coherence feels like truth to any evaluator that uses connectivity as a truth signal. Humans do this. Large language models do this. Both will approve a framework that is beautiful, self-reinforcing, and wrong, because the beauty and self-reinforcement register as correctness.

This is not a theoretical concern. The practitioner has direct experience with this failure mode. A framework that covered every domain of science — physics, biology, medicine, chemistry, astronomy, consciousness — was developed over 45 days with the assistance of three frontier large language models operating in adversarial red-team configuration. The models were explicitly instructed to find errors. For 45 days, across 390 documents, they could not find a single inconsistency. The framework was coherent. Every piece connected. Every derivation reinforced every other derivation. The models approved it unanimously.

A simple arithmetic verification script — not evaluating coherence, just checking whether specific integers produced specific results — falsified the framework in 30 minutes. The arithmetic was wrong. The coherence had masked the arithmetic failure because coherence evaluation and arithmetic verification are different operations. The models were performing coherence evaluation. Only the script performed arithmetic verification. Only the script caught the error.[⁵]

The lesson is permanent: coherence is not correctness. A beautiful framework that compiles incorrectly is wrong regardless of how well its pieces fit together. Mechanical verification is the defense against coherence bias. The compiler does not care how beautiful your architecture is. It cares whether the code runs.

### Public verification

Verification results — both successes and failures — are published with the author's name, with timestamps, on public repositories accessible to anyone. The publication of failure is specifically more important than the publication of success.

Anyone can publish results that work. Publishing results that don't work — under your own name, with full documentation of what you tried, why it failed, and what you learned — demonstrates that the verification layer is actually operating. It demonstrates that the process is not performative rigor but actual rigor, tested against reality, with the reality winning when it should.

The practitioner has published an entire body of invalidated work — hundreds of documents, publicly flagged as falsified, alongside the falsification methodology, the corrected approach, and the plan for re-attempting with better tools. This publication was not an accident or an embarrassment. It was the process working exactly as designed. The framework was built, the framework was tested, the test found the break, the break was published, the surviving components were identified, and the next iteration began from the survivors.[⁶]

---

## Section 7 — The Remainder Protocol: Keep What Survives

The sixth layer addresses what happens after verification finds a break. The answer is not "discard everything and start over." The answer is surgical separation of what failed from what survived.

### Separating failure from survival

A framework can fail in its specific claims while its structural observations survive. The physics framework described in Section 6 produced incorrect numerical predictions. That specific failure killed the framework as a predictive system. But the framework's identification of cross-domain structural connections — the observation that biological systems and physical systems exhibit the same mathematical symmetries — was not invalidated by the arithmetic failure. The connections were real observations about the world. The numbers used to describe them were wrong. These are different things.

The verification identifies what specifically failed. Everything not specifically failed remains on the table with its metadata. The failing components are documented — what failed, why it failed, what the failure reveals about the gap in understanding — and then released. Released means genuinely let go. Not carried forward as "maybe it will turn out to be right later." Not defended because it took effort to create. Not hidden because it is embarrassing.

The surviving components become the starting material for the next iteration. In the practitioner's experience, the arithmetic foundation that survived the framework's falsification became the basis for a new arithmetic specification with explicit formal axioms, explicit failure conditions, and no dependence on the specific physics that had failed. The methodology that survived — verify mechanically, not through coherence evaluation — became the core principle for all subsequent work. The identification of the coherence failure mode itself became the most valuable output of the entire 45-day project, more valuable than the framework would have been if it had been correct.[⁷]

### Documenting the failure

The failure documentation is as important as the success documentation. It includes: what was attempted, what was expected, what was observed instead, what specifically broke, why the earlier verification steps (including LLM red-teaming) failed to catch it, what the failure teaches about the verification methodology, and what survives.

This documentation serves two purposes. First, it prevents the practitioner from making the same error again. Second, it provides a public record that other practitioners can learn from. A documented, publicly accessible, honestly described failure with full methodology is more useful to the field than a quietly abandoned project that nobody knows existed.

### Not getting stuck

The remainder protocol requires the same cognitive freedom described in Section 4. The practitioner must not get stuck on failed work. Not stuck in defense of it. Not stuck in grief over it. Not stuck in the sunk cost of the effort invested.

A framework that took 45 days to build, that covered every domain of science, that felt like the most important work of a lifetime — when it failed, it was killed in an afternoon and the correction was posted the same day. The next morning the practitioner returned to their regular work, began the revised approach, and continued. Not because they didn't care. Because the framework was a tool, the tool broke, and the work requires a working tool, not a sentimental attachment to a broken one.

This is an active practice, not a personality trait. The natural human response to losing a major investment is grief, anger, or denial. The process acknowledges this response and does not suppress it. It simply does not allow the response to delay the next iteration. Feel the loss. Post the correction. Begin again. In that order. Without a gap between the second step and the third.

---

## Section 8 — Iteration: Every Output Becomes Input

The seventh layer is iteration, and it is the layer that produces compounding returns over time.

Every output from the construction and verification layers becomes input to the next cycle. A neuroscience paper about body coordination timing reveals that the game engine's frame synchronization problem has the same mathematical structure. The game engine's solution — parallel broadcast to all entities simultaneously — suggests an architecture for the neuroscience question. The neuroscience question reveals that the arithmetic must preserve exact timing without approximation. The arithmetic specification's formal axiom structure feeds back into the game engine's physics system. A novel documents the entire arc. Music processes the emotional content of the journey. Each piece feeds every other piece.

This is not a designed system. It is an emergent property of doing omni-domain work without walls. When everything lives in the same integration space with the same metadata structure, connections form automatically. The practitioner does not need to plan the cross-domain connections. They appear because the domains share structure, and the integration layer makes that shared structure visible.

### Compounding

Early iterations produce crude results with high uncertainty. Later iterations produce refined results with lower uncertainty because each iteration starts from the surviving components of all previous iterations. The compounding is not linear — it accelerates, because each iteration adds not just results but also methodology refinements, new connections, and better tools.

A game engine built in year one teaches lessons about data architecture that inform a physics framework in year two. The physics framework's failure in year two teaches lessons about verification methodology that inform everything built in year three. The verification methodology produces a neuroscience paper in year three that connects back to the game engine's synchronization problem. The game engine, the physics, the arithmetic, the neuroscience, and the methodology are all improving simultaneously because they share structural foundations.

After enough iterations, the practitioner's toolkit is not a collection of domain-specific skills. It is an integrated system where every skill informs every other skill, every failure teaches every active project, and every new input is immediately tested against everything already held. The intake is broader, the integration is deeper, the evaluation is more calibrated, the construction is faster, and the verification is more rigorous — all because of the accumulated compound returns from every previous iteration.

### No endpoint

The process does not have a planned endpoint. It is not "investigate until the answer is found." It is "investigate, build, verify, keep what survives, iterate." If an answer emerges, it is held with its metadata and tested further. If no answer emerges, the investigation continues with the accumulated understanding from all previous iterations.

If the investigation must be abandoned — and the process has explicit, pre-stated abandonment conditions for every active project — the abandonment is documented, the surviving components are identified, and those survivors become input to whatever comes next. Nothing is wasted. Even a fully abandoned project produces methodology improvements, integration connections, and verified failure documentation that improve every subsequent project.

---

## Section 9 — Physical Practice as Cognitive Maintenance

This section may seem out of place in a methodology paper. It is not.

The discovery process requires a cognitive state that most institutional training actively degrades: the ability to hold multiple contradictory possibilities without forcing resolution, to invest deeply without becoming attached, to accept being wrong publicly without it affecting the next investigation, and to maintain honest self-monitoring of one's own biases continuously throughout every project.

This cognitive state is not a personality trait. It is a practice. It is maintained through physical training the same way cardiovascular fitness is maintained through running — it degrades without practice and improves with consistent work.

### The body and the mind are the same system

The practitioner's physical training — martial arts circle-walking, judo, and a systematic proprioceptive development program — is not a hobby separate from the intellectual work. It is the maintenance protocol for the cognitive state the intellectual work requires.

The connection is direct and physiological, not metaphorical. Proprioceptive awareness — the ability to sense the body's internal state accurately — and interoceptive awareness — the ability to sense internal physiological states like tension, fatigue, and stress — use the same sensory processing channels that cognitive self-monitoring uses. A person who can feel when their shoulders are carrying tension before the tension becomes pain can also feel when their thinking is carrying bias before the bias becomes commitment. The sensory modality is the same: awareness of internal state.

Physical practice trains this awareness. Standing in a martial arts posture for ten minutes with attention on the body's micro-adjustments trains the same attention that notices when an investigation is being driven by wanting a result rather than by evidence. Walking in a circle with attention on the weight transfer between steps trains the same attention that notices when a framework is being defended because of investment rather than merit. The body practice is cognitive practice performed through a physical medium.

### What the physical practice produces

The martial arts circle walk specifically trains the ability to move through a pattern without forcing, holding, or gripping. The walker is not trying to get anywhere. They are completing each step fully and then completing the next one. There is no accumulation of tension, no unresolved posture, no carried strain. Each step is complete. Each breath is complete. The practice is a physical rehearsal of the cognitive state the discovery process requires: not holding on to the last step, not anticipating the next step, just executing the current step fully.

The judo practice trains something different but equally important: the ability to be thrown, to fail physically, to hit the ground, and to get back up and continue. The experience of being physically wrong — a technique that should have worked didn't, a defense that should have held collapsed, a throw that was perfectly timed by the opponent and impossible to stop — is the physical analog of being intellectually wrong. The body learns that failure is survivable, that getting up is always possible, and that the next exchange begins from wherever you are, not from where you wish you were.

The proprioceptive development program — systematic training of the body's positional awareness through targeted exercises, visual-vestibular integration drills, and progressive challenges to balance and coordination — directly improves the interoceptive sensitivity that self-monitoring requires. A body with poor proprioception is a body that doesn't know where it is. A mind with poor interoception is a mind that doesn't know what it's doing. Both are improved by the same training modality.[⁸]

### Not optional

Physical practice is not an optional lifestyle addition to the discovery process. It is a maintenance requirement. A practitioner who stops physical training will, over time, lose the interoceptive sensitivity that powers the self-monitoring described in Section 4. They will become more attached to their positions. They will become less able to feel when bias is accumulating. They will become more brittle in the face of failure. The cognitive state that the process requires degrades without physical maintenance, the same way strength degrades without training.

The specific physical practice matters less than its consistency and its attention to internal awareness. Martial arts, yoga, dance, gymnastics, climbing — any discipline that requires continuous monitoring of internal state while performing complex movement will maintain the cognitive substrate the process depends on. The key is that the practice requires attention to how the body is doing what it is doing, not just what it is doing. The attention to process rather than outcome is the transferable skill.

---

## Section 10 — The Complete Process as Protocol

The full discovery process, restated as a protocol anyone can follow:

**Step one — Intake.** Consume from every available source. Filter on source coherency — internal consistency, demonstrated results, tested against reality — not on domain membership. Admit high-coherency sources from any field. Be skeptical of low-coherency sources from every field, including prestigious ones.

**Step two — Integration.** Test every new input against everything already held. Note connections and contradictions without forcing resolution. Hold contradictions with full metadata — source, temporal context, confidence, scope, relationships. Do not collapse to one answer before the evidence justifies it.

**Step three — Evaluation.** Before investing time in a connection or contradiction, test for materiality: does this change an outcome? Check the scope: how many cases does it affect? Check the fruit: do the results match the claims? Advance understanding one step at a time, verifying each step before moving to the next. Seek high-locality information — direct observation and primary sources over summaries and consensus.

**Step four — Construction.** Build from known good components at zero latency. The build is the understanding — if it doesn't compile, the understanding is wrong. Assemble proven components into new configurations. The novelty is in the integration, not the components. Do not wait for permission.

**Step five — Verification.** Test to find the break, not to confirm the result. Use mechanical verification wherever possible — compilers, scripts, measured quantities. Coherence is not correctness. A beautiful framework that doesn't compute correctly is wrong. Publish all verification results, especially failures, publicly and under your own name.

**Step six — Keep what survives.** When verification finds a break, separate what failed from what survived. Document both. Release the failure — do not defend it, do not hide it, do not carry it. Rebuild from the surviving components with better tools.

**Step seven — Iterate.** Every output becomes input. Every domain informs every other domain. The cycle runs continuously at the speed of curiosity. After enough iterations, the returns compound: broader intake, deeper integration, sharper evaluation, faster construction, more rigorous verification. Nothing is wasted.

**Step eight — Maintain the cognitive state.** Practice physical discipline that requires continuous attention to internal state. Do not skip this step. The cognitive freedom the process requires — holding without gripping, investing without attaching, failing without breaking — degrades without physical maintenance. Train the body to stay aware. The mind follows.

---

## Section 11 — Falsification of the Process Itself

The process claims to produce useful cross-domain results. This claim is falsifiable.

**F1.** If the process consistently produces results that fail mechanical verification at rates higher than domain-specific institutional investigation, the process is less reliable than the alternative it claims to complement.

**F2.** If the omni-domain integration consistently produces connections that are metaphorical rather than structural — connections that feel right but produce no testable predictions — the integration layer is producing noise, not signal.

**F3.** If zero-latency construction consistently produces builds that require complete reconstruction rather than iterative improvement, the evaluation layer is not adequately assessing readiness before construction begins.

**F4.** If the remainder protocol consistently discards components that later prove to have been valid, the separation of failed from surviving components is miscalibrated.

**F5.** If the process produces diminishing returns over time rather than compounding returns, the iteration layer is not functioning as described.

Each criterion is testable against the historical record of the process's outputs. The practitioner's public body of work — spanning systems engineering, formal arithmetic, neuroscience, music, fiction, and philosophy, with complete transparency including published failures — constitutes that record.

---

## Section 12 — Conclusion

The discovery process described in this paper was not designed and then implemented. It was practiced for decades and then documented. The documentation came after the practice, the same way a paper on walking biomechanics comes after the walking.

The process is domain-independent because reality is domain-independent. It is verification-centered because coherence without mechanical checking is the primary failure mode of both human and artificial intelligence. It is public because private claims of rigor are untestable. It is continuous because the best time to start the next iteration is immediately after the current one completes.

The process does not require exceptional intelligence. It requires the willingness to look at things without being told what to see, to hold multiple possibilities without being told which one to choose, to build without being told when to start, to verify by trying to break rather than trying to confirm, to publish the breaks under your own name, and to start again the next morning.

The process works because reality does not maintain departments. A person who refuses to maintain them either — who walks across every hall, reads every source, holds every contradiction, builds every connection, breaks every result, publishes every failure, and iterates every output — will see things that departmental investigation cannot see. Not because they are smarter. Because they are looking at the whole thing.

The door is open. The tools are available. The process is documented. The rest is the reader's move.

---

## Appendix — Referenced Works

Each entry provides a one-paragraph summary. Full documents are available at the DOIs listed.

**A — Silo: Tall-Infra Data-Only Execution System (HOWL-COMP-1-2026).** A game engine architecture where all behavior resides in hot-swappable data tables rather than compiled code. The runtime binary contains no gameplay types or behavior code. All semantics exist as dataset rows. Demonstrates zero-latency iteration: changes take effect on the next frame with no compilation step. Running system processes 10,000 entities at 60fps with linear CPU scaling. DOI: 10.5281/zenodo.18655354

**B — Silo OS (HOWL-COMP-3-2026).** A bootable operating system built on the Silo architecture. Ring 0, single process, no external libraries, no binary blobs, NUMA-aligned data processing. Demonstrates that the tall-infra data-only architecture extends from game engines to operating systems. DOI: 10.5281/zenodo.18655396

**C — Geometric Security (HOWL-COMP-4-2026).** A security model that achieves input isolation through fixed-size network packets and path-based access control rather than sandboxing. Demonstrates that security can be structural rather than policy-based. DOI: 10.5281/zenodo.18655427

**D — Multi-Dimensional Information Indexing (HOWL-INFO-1-2026).** Formalization of the practice of holding information with source, temporal, contextual, and intentional metadata rather than as binary true/false claims. Enables holding contradictory information without cognitive dissonance by preserving the dimensions along which the claims differ. DOI: 10.5281/zenodo.18655616

**E — The Scales Method (HOWL-INFO-2-2026).** Formalization of the materiality evaluation practice. Claims and evidence are evaluated through multi-dimensional scoring that distinguishes material from non-material impact, quantifies scope as percentage affected, and validates through outcome assessment (fruit of the plant). DOI: 10.5281/zenodo.18655618

**F — The Pseudo-Socratic Method (HOWL-INFO-3-2026).** Formalization of the one-step advancement practice. A conversational reasoning methodology centered on continuous assessment of the interlocutor's current state and adaptive information delivery calibrated to that state. DOI: 10.5281/zenodo.18655621

**G — Axiom of Information Locality (HOWL-INFO-4-2026).** Formalization of the principle that information is most useful closest to its source and degrades through abstraction layers. Direct observation outranks textbook description outranks summary outranks cultural consensus. DOI: 10.5281/zenodo.18655625

**H — Paternal Operationalism (HOWL-SOPH-1-2026).** Application of the discovery process to parenting. The same principles — demonstrate rather than lecture, maintain the environment, keep promises at 100% fidelity, let the child choose when to engage — applied to the transmission of capability from parent to child. DOI: 10.5281/zenodo.18655527

**I — Cymatic K-Space Mechanics (CKS).** An attempted unified physics framework deriving all physical constants from hexagonal lattice geometry using exact rational arithmetic. Developed over 45 days with LLM assistance, producing 390 documents. Invalidated and falsified when mechanical arithmetic verification found errors that 45 days of LLM adversarial testing had not detected. Published with full invalidation banner. The project's primary lasting contribution is the identification of the coherence failure mode: LLMs approve coherent but incorrect frameworks because they evaluate connectivity rather than arithmetic. Zenodo community: Cymatic K-Space Mechanics.

**J — Post-CKS Methodology (CKS-NEXT-1-2026).** The corrected methodology published after the CKS falsification. Specifies: exact discrete arithmetic (no floats), mechanical verification (compiler checks, not LLM evaluation), brute-force search with exact equality, and explicit abandonment conditions at every level. DOI: 10.5281/zenodo.[to be assigned]

**K — VDR Specification.** A pure-mathematics program for exact finite discrete representation. Every value is a triple [Value, Denominator, Residual] where the residual is preserved rather than discarded. Currently at 245 formal rules across 14 layers, pre-v1. The existential test is whether transcendental values (pi, e) can be represented structurally in VDR form. If they cannot, the specification documents the boundary honestly and the finding is published. Status: in progress.

**L — LLM-Prolog Architecture (CKS-MATH-138-2026).** An architecture eliminating AI hallucination by construction through alternating neural-symbolic computation. The LLM handles fuzzy input comprehension and creative pattern selection. Prolog handles consistency verification, constraint enforcement, and provenance tracking. Unverified facts cannot reach the output because the emission step only processes verified facts. DOI: 10.5281/zenodo.18960010

**M — Edmund Taylor: K-Space Walker.** A novel about a Filipino systems engineer who derives fundamental physical constants from lattice geometry, is contacted by entities operating on the substrate of reality, survives a journey home across hostile territory, and deliberately makes his discovery unfindable so the world can remain livably imperfect. The novel is autobiography with the cosmology as the fictional layer. The Zenodo papers are real. The falsification is real. The seam between fiction and reality exists on a public server. Status: hand-editing in progress.

**N — Z-Health Movement Rehabilitation.** An external training program in applied neuroscience for movement rehabilitation, developed by Dr. Eric Cobb. The practitioner completed the full certification curriculum and applies the proprioceptive and visual-vestibular protocols as personal practice for maintaining interoceptive sensitivity. External source, not part of the Howland Archive.

**O — Baguazhang Lineage Training.** Traditional Chinese internal martial art emphasizing circle-walking, whole-body coordination, and continuous awareness of internal state during movement. The practitioner trains under a lineage teacher. The practice serves as physical maintenance for the cognitive state the discovery process requires. External source, not part of the Howland Archive.

**P — Elimination of Classical Carriers for Sub-Millisecond Motor Coordination (HOWL-NEURO-1-2026).** A paper demonstrating through engineering analysis that no classical neural signaling mechanism can meet the timing requirements for dynamic motor coordination, and that electromagnetic field propagation is the only known physical mechanism with sufficient speed. Proposes a three-channel motor coordination architecture and four specific experiments. Status: published in this archive.

---

**END HOWL-DISC-1-2026**

**Registry:** HOWL-DISC-1-2026
**Status:** Foundation paper, DISC Track
**Methodology:** Documented from practice, not designed from theory
**Falsification:** Five explicit criteria specified
**Dependencies:** None (references other works as evidence, not prerequisites)

The process is documented. The evidence is public. The failures are published. The tools are available to anyone.

The rest is the reader's move.