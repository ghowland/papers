# Cross-Domain Learning: How Bits and Ops Transfer Between Domains
## The Mechanical Process of Learning New Domains Using What You Already Know

**Registry:** [@HOWL-INFO-15-2026]

**Series Path:** [@HOWL-COMP-1-2026] → ... → [@HOWL-COMP-12-2026] → [@HOWL-INFO-11-2026] → ... → [@HOWL-INFO-13-2026] → [@HOWL-MATH-15-2026] → ... → [@HOWL-MATH-20-2026] → [@HOWL-INFO-14-2026] → [@HOWL-INFO-15-2026]

**Date:** June 2026

**DOI:** 10.5281/zenodo.zzz

**Domain:** Information Theory / Information Processing Theory

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6.

---

## Two Kinds of Information

Information does two things. It moves, and it gets acted on.

When information moves — from a book to your eyes, from a server to your laptop, from one person's mouth to another person's ears — the unit is the bit. One binary distinction. Shannon formalized this in 1948: how to measure information in transit, how to encode it efficiently, how to transmit it reliably through a noisy channel. The bit is the same whether it travels over fiber optic cable or is carried by a pigeon. What varies is the speed and reliability of the channel, not the nature of the bit.

When information gets acted on — when you read the book and understand it, when the server processes a request, when the listener parses the sentence and decides what to do — the unit is the op. One irreducible transformation by one processor. The op is the same whether the processor is a CPU executing an instruction, a surgeon making an incision, or a person reading a sentence. What varies is how long each op takes and how many are needed, not the nature of the op.

Together, bits and ops cover everything information does. Shannon formalized movement. A companion framework [@HOWL-INFO-14-2026] formalizes action. This paper uses both to explain how people learn new domains and how what you already know accelerates what you learn next.

---

## Domains Have Bits and Ops

Every domain you might learn — medicine, software engineering, physics, a new language, a new codebase, woodworking, chess — consists of bits and ops. The bits are the domain's data: its vocabulary, its facts, its measurements, its notation, the tokens you need to recognize and decompress. The ops are the domain's transformations: its procedures, its judgments, its reasoning patterns, the things you do to the data to produce results.

When you don't know a domain, both its bits and its ops are invisible to you. You can't recognize the vocabulary, so you can't parse the data. You can't execute the procedures, so you can't produce results. Learning a domain is the process of making its bits recognizable and its ops executable. This process is identical in structure whether the domain is cardiac surgery or French cooking. The mechanism is universal. The content is local.

Within any domain, you constantly face a population of things that need attention and can only work on one at a time. The pile of symptoms to consider, the stack of bugs to investigate, the queue of orders to fill, the set of candidate moves on the board. Getting from "everything" to "the one thing I'm working on right now" follows a fixed sequence: you enumerate what's in front of you, filter out what's irrelevant, score what remains against your current priorities, and select the highest-scored candidate for action. This is the reduction pipeline — the mechanism by which multiplicity becomes unity, by which many becomes one, by which a processor that can only act on one thing at a time navigates a world that presents many things simultaneously. The pipeline operates within every domain. It also operates across domains, as we'll see.

---

## Dissolution: How Things Become Free

When you perform an operation enough times under consistent enough conditions, something happens to it. The op count drops. The thing that once required conscious attention — checking the mirror while driving, reading a word in your native language, navigating a familiar codebase — becomes structural. It happens without consuming your scarce pipeline. The processing cost goes to zero. This is not forgetting. Forgetting is loss. This is compression into structure that produces correct results without conscious effort. The term for it is dissolution.

Dissolution follows a curve. The first time you encounter something, the cost is maximum — many ops, full conscious engagement. With practice, the cost descends. The descent is steep early and flattens into a long tail. There is a floor called R* — the minimum number of correct ops any competent person needs for reliable execution. Below R* you're guessing, not executing. Between R* and zero is the territory dissolution absorbs: the gap between competent execution and fully structural operation. A new driver's mirror check starts at six ops (scan, identify, assess, interpret, decide, act). After months of practice it reaches one op (single glance acquiring image plus threat assessment — this is R*). After years it reaches zero (structural, no conscious engagement at all). The progression is: high cost, then competent, then free.

But dissolution has conditions. It holds within the region of circumstances you actually practiced in. Drive in calm weather on familiar roads and your lane-keeping is dissolved — zero ops, fully structural. Suddenly encounter ice on an unfamiliar road at night and the dissolved skills promote back to conscious processing. You're spending ops on things that were free a moment ago, and you're spending them all at once because multiple dissolved skills break simultaneously. The region where dissolution holds is the validity envelope. Its width along any dimension equals the variety of conditions you practiced under. Narrow practice produces narrow envelopes. When conditions step outside the envelope, the dissolved skill costs ops again.

The simultaneous promotion of multiple dissolved skills back to conscious processing is a cascade. Its severity equals the count of things that break, independent of the trigger's magnitude. A bee flying into a cockpit — negligible trigger, but if it breaks three dissolved flying skills simultaneously, the cascade count is three. A thunderclap — large trigger, but if it only breaks the assumption of calm weather, the cascade count is one. The bee is more dangerous than the thunder if it invalidates more dissolutions. Severity is a property of what breaks, not of what caused the break.

---

## Six Levels of Domain Knowledge

When you encounter any domain, you occupy one of six levels relative to it. These levels are not arbitrary labels — they correspond to measurable transitions in what you can do and what it costs you. Each level has a definition, a processing signature, and a testable boundary separating it from the next.

**None.** The domain's bits and ops are invisible to you. You cannot distinguish signal from noise. You cannot identify which parts are data and which are structure. You cannot segment the stream into discrete tokens. The domain is outside your operational boundary entirely. Your processing cost for every element is not high — it is undefined. You cannot even enumerate what you don't know because you lack the compression tokens to segment the domain into addressable pieces.

Before the Rosetta Stone was discovered, European scholars looking at Egyptian hieroglyphs could not answer the most basic question: are these language? Is this a writing system carrying encoded information, or is it decorative art, or religious symbolism without linguistic content? The domain's bits were not recognized as bits. The scholars were at none — not because they were unintelligent but because the domain had given them no entry point. You cannot begin the reduction pipeline on something you cannot enumerate, and you cannot enumerate something you cannot recognize as containing information at all.

**A little.** You have encountered the domain. Some tokens decompress — you recognize a few terms, you can identify some of the domain's bits as bits and some of its ops as ops. But most of the domain is still an undifferentiated mass. Your processing cost is maximum for everything you can see and undefined for everything you can't. You know enough to know the domain exists. You do not know enough to navigate it.

After the Rosetta Stone provided Greek text aligned with hieroglyphic text, scholars could begin decompressing individual tokens. They knew some symbols mapped to known words. But knowing thirty symbols does not mean you can read a temple wall. The vocabulary is partially dissolved. Common tokens decompress. Rare ones do not. The grammar is opaque — you can recognize individual words without understanding how they combine.

The boundary from none to a little is bit recognition: the moment someone recognizes that the domain contains bits and ops at all. For hieroglyphs, "these are language, not decoration." For a new programming language, "this is code, not random characters." For a new scientific field, "these measurements contain structure, not just noise." The test is simple: present material from the domain. Can the person distinguish signal from noise? Can they identify any discrete tokens? If no, they are at none. If yes, they have crossed to a little.

**Exposure.** You have seen enough to enumerate the domain's major structures. You can segment it into regions — this part is data, that part is transformation, these are the main entities, those are the main processes. The common vocabulary is partially dissolved — you can decompress frequent terms without conscious effort, though specialized terms still cost ops. You can read a paper in the domain and follow the argument even if you cannot reproduce it. The reduction pipeline works — you can enumerate, filter, score, and select within the domain — but slowly, with high cost per step.

For hieroglyphs, this is the stage where scholars could distinguish royal cartouches from religious formulae from administrative records — structural segmentation achieved even though many individual symbols remained opaque. For a new codebase, this is being able to identify the network layer versus the storage layer versus the UI layer without understanding the implementation of any of them.

The boundary from a little to exposure is structural segmentation: can the person segment new domain material into its major structural components without external help? If they can recognize individual tokens but cannot identify the domain's major regions and their relationships, they are still at a little.

**Coverage.** You have interacted with enough of the domain to have encountered most of its major patterns. The dissolution curve has passed its knee — the steep initial descent is done, and you are in the long tail of refinement. Most common operations cost few ops. The domain's internal structure is visible to you — you can see which tasks cluster together, which tasks are similar to each other, which tasks are isolated. You can handle novel problems because your structural recognition is sufficient to identify when something does not fit existing patterns. You make mistakes on edge cases but handle the mainstream correctly.

For hieroglyphs, this is the stage where scholars could read unknown texts — texts with no Greek parallel, where decipherment had to generalize beyond the training data. For a programmer on a new codebase, this is when you can fix bugs in code you have never seen before because the patterns are familiar enough to navigate independently.

The boundary from exposure to coverage is novel problem handling: give the person a problem they have never seen that uses the domain's standard patterns. Can they solve it without reference material? If yes, they have coverage. If they need to look things up constantly, they are still at exposure.

**Expert.** Most of the domain's routine operations are dissolved — zero ops, fully structural. Your processing cost profile is near zero for the standard task set. You can teach the domain, assess others in it, identify novel problems, and produce original work efficiently. The validity envelopes on your dissolved skills are wide — you handle variation, pressure, and novel conditions without cascade. Your cost is near zero for routine work and moderate for the domain's frontier problems.

The boundary from coverage to expert is the teaching boundary: can the person teach a novice to reach coverage in a fraction of the time it took them? Can they accurately assess another practitioner's level? Can they identify which specific tasks the other person needs to work on next? Teaching requires reversing dissolution — reconstructing explicit steps from structural knowledge so that a learner can follow the reduction chain consciously. If someone can do the work but cannot teach it or assess others, they have deep practice but not expert-level structural understanding.

**Master.** The domain's processing structure itself is dissolved — not just the operations but the meta-patterns of how the domain works, where its provable results and its empirical-only results are, what transfers to adjacent domains and what does not. The master can redesign the domain's infrastructure, identify its structural limitations, and see connections to other domains that specialists within the domain cannot see because their dissolution is content-deep but structure-narrow. The mastery is of the domain's architecture, not just its operations.

The boundary from expert to master is the architecture boundary: can the person identify structural limitations of the domain's current framework? Can they propose alternatives that the domain's experts have not considered? Can they connect the domain to other domains in ways that produce novel results? This boundary has an environmental dependency that the others do not: mastery requires the domain to be alive. It must have a frontier — unsolved problems, unexplored connections, territory where the existing framework does not yet reach. A dead language has a ceiling at expert. You can become the world's leading authority on Egyptian hieroglyphs — near-zero processing cost on everything that survives in the archaeological record. But the record is the boundary. You cannot master what has no frontier to push against.

---

## Expert and Master Both Work at One

Neither expert nor master is at zero cost on everything. Both encounter novel problems. Both engage their conscious pipeline. Both spend ops. The distinction is what they do when working consciously.

The expert at One executes. They encounter a novel problem, engage the reduction pipeline, work through it efficiently, solve it, and dissolve it into their inventory. Their time at One is productive — low cost per step, good pipeline, fast dissolution after the work is done. They add to the domain's mapped territory. They produce more of what the domain already has.

The master at One sees. They encounter the same novel problem and they do not just solve it — they see what the problem reveals about the domain's structure. They see where the problem does not fit the existing framework. They see connections to other domains that nobody in this domain would see because nobody else has those other domains dissolved. The expert solves problems. The master dissolves the problems that generate the problems — by finding structural shortcuts that nobody knew existed, by connecting domains that nobody knew were connected, by reframing questions so that what was only measurable becomes provable, or what required dozens of ops can be done in three.

Consider a geometric ratio that appears as the cross-sectional area factor in pipe flow, the plate area factor in capacitance calculations, the aperture factor in antenna theory, and similar roles in six other engineering domains. An expert in any one of those domains has dissolved their field's use of the ratio to zero cost — they apply it without thinking. None of them sees the cross-domain identity because their expertise is within one domain. A master — operating consciously across domains, examining what is in front of them with multiple dissolved codebooks available — sees that nine experts in nine departments are all performing the same geometric operation under nine different names. That observation does not solve a problem within any domain. It reveals structure that transforms how all nine domains relate to each other.

The expert uses freed pipeline capacity to solve more problems faster. The master uses freed pipeline capacity to see connections, question structures, and create things that transform the landscape. Same pipeline. Same conscious processing. Different target.

---

## The Rosetta Stone: How One Domain Helps You Learn Another

When you dissolve a domain, you do not just dissolve its content. You dissolve its processing structure — its reduction patterns, its characteristic failure modes, its cardinality relationships, the shape of its dissolution curves. That structure is a codebook. And when you encounter a new domain, that codebook is available.

The mechanism is the same one that governs communication between two people, but applied to communication within one person between two domains. When an expert explains something to a novice, the total cost has three parts: the expert's encoding cost (near zero — the material is dissolved), the channel cost (the words, the page, the screen), and the novice's decoding cost (high — each unfamiliar term costs ops to decompress). The expert's dissolved knowledge is the sender. The novice's undissolved state is the receiver. The gap between their dissolution states — the dissolution differential — predicts how hard the communication will be.

Cross-domain learning within one person follows the same structure. Domain A's dissolved processing structure is the sender. Your own attention — your conscious pipeline — is the channel. Domain B's undissolved material is the receiver. The dissolution differential between your A-codebook and B's structural requirements predicts the cost. Where A and B share processing structure, the differential is low and B's structure dissolves fast because A already built the relevant codebook entries. Where they do not share structure, the differential is high and B costs nearly full price.

The codebook alignment is imperfect. You imperfectly know domain A. You know even less of domain B. Your A-codebook offers candidate structural matches for what you encounter in B — hypotheses, not answers. Some are correct. The feedback loop you dissolved in TCP really is the same structure as the demand-response loop in supply chain management. The tokens are different — packets versus pallets, window size versus reorder point — but the processing structure is identical. Other candidates are wrong. The surface similarity masks a different underlying mechanism. A pattern that looks like a feedback loop turns out to be open-loop with delayed measurement. You do not know which candidates are correct and which are wrong until you compare to reality, which is why comparing to reality is a non-negotiable step in the operational method.

Cross-domain transfer is hypothesis generation, not pattern matching. Your dissolved A-structure generates candidate reductions for B's population of unfamiliar elements. Those candidates enter B's reduction pipeline at the enumeration stage — they expand the set of things you consider. Some candidates are good and accelerate dissolution. Some are wrong and get eliminated when you filter and score against B's actual behavior. The value is not certainty. The value is a richer enumeration — a lower probability that the correct structural match was never in your candidate set at all. Enumeration failure — where the right answer was never considered — is the most dangerous failure in any reduction pipeline because it is invisible from inside. You confidently select the best of what you enumerated, never knowing that the correct answer was not among them. Each dissolved domain reduces this probability by adding structural candidates that a single-domain perspective would never generate.

Multiple domains compound this effect. With one dissolved domain, you have one set of candidate structural parallels. With five, you have five. The correct structural parallel for domain F might not exist in domain A's codebook but might exist in domain C's. More dissolved domains means more candidate analogies means higher probability that the correct match is somewhere in your enumeration. This is the polyglot effect. A monolingual person learning their second language pays full cost for everything — phonology, grammar, vocabulary, pragmatics. A person who has learned fifteen languages has dissolved the meta-structure of language acquisition itself — what to listen for first, how grammar categories map across languages, where false cognates hide, how to bootstrap vocabulary through context. Their sixteenth language dissolves faster not because the language is easier but because the process of language acquisition is dissolved. The structural transfer compounds with each domain added.

But false parallels also scale. More domains means more wrong candidates alongside the right ones. The filtering and scoring stages have to do more work. The net benefit is positive only when the rate of correct structural matches grows faster than the rate of false ones — which happens when the domains share genuine processing structure, and does not happen when they do not. Dissolving TCP does not help you play violin. The processing structures do not overlap. Transfer is proportional to structural overlap, and structural overlap is an empirical property of the domain pair, not a universal guarantee.

The meta-task of structural recognition itself dissolves with practice. Early cross-domain work has high cost on the recognition task — you misidentify parallels, miss real ones, over-apply analogies from your strongest domain. With practice, the recognition improves. Each confirmed parallel strengthens correct structural matching. Each falsified parallel prunes a false pattern. The codebook does not just grow — it gets more accurate. The compare-to-reality step provides the feedback that drives this meta-dissolution. Without that step, the codebook grows but does not improve, and the false-parallel rate eventually overwhelms the benefit.

---

## Conditions for Dissolution

Dissolution is not automatic. It requires four conditions, and domains that deny any one of them resist dissolution regardless of the person's capabilities or cross-domain inventory.

Rapid feedback. You need to be able to test whether your reduction was correct on a timescale that allows the result to connect to the attempt that produced it. If you try something and learn whether it worked three months later, the feedback does not drive dissolution because the context has changed too much between attempt and result. The attempt and the feedback must be close enough in time that your pipeline can connect them.

Manageable iteration cost. Each attempt must not consume prohibitive resources. If every experiment costs a thousand dollars, you cannot run enough experiments for the dissolution curve to descend. If every test requires a week of setup, you cannot iterate fast enough for the steep early portion of the curve to complete in a reasonable time. The cost per iteration bounds the number of iterations, which bounds the dissolution rate.

Context consistency. The domain must hold still enough for repetition to accumulate. If the rules change every time you practice, the dissolution curve cannot descend because each repetition is effectively a first encounter under new conditions. Some variation is necessary for widening validity envelopes, but the core structure must be stable enough that repeated practice on it produces genuine dissolution rather than perpetual re-learning.

Sufficient repetitions available. You must be able to practice enough times for the curve to descend meaningfully. Some domains gate repetitions — you cannot perform surgery a thousand times in a month, you cannot launch rockets daily, you cannot run clinical trials on demand. The gating limits how fast the dissolution curve can descend regardless of everything else.

These conditions are checkable before entering a domain. They are properties of the domain-person relationship, not of the person alone. Physics met all four conditions for a software engineer with dissolved integer arithmetic: large language models provide vocabulary feedback (rapid), CODATA provides pre-computed experimental results to test against (cheap iteration), the mathematical structure is stable (context consistency), and Python executes tests in seconds allowing thousands of iterations per day (sufficient repetitions). The domain yielded not because of special talent but because the conditions were met.

Rocketry provides the counterexample. The theory transfers — orbital mechanics, propulsion physics, materials science all have structural overlap with other engineering domains. But the hands-on operational domain fails multiple conditions: each test is expensive (iteration cost), dangerous (constraining iteration rate), slow to provide complete feedback (days to weeks per test cycle), and capital-gated (limiting total repetitions). Cross-domain structural transfer would help with design and analysis — the theoretical portions where cheap iteration is possible. It would not dissolve the operational domain because the conditions prevent sufficient iteration there.

The framework does not claim all domains are equally accessible. It claims dissolution is universal in mechanism. The mechanism requires conditions. The conditions are empirically checkable and produce specific predictions about which domains will resist acquisition regardless of the person attempting them.

---

## The Operational Method

There is a repeatable process for entering a domain and moving through the levels. It is not a methodology imposed from outside — it is the reduction pipeline applied to understanding itself. Each step has a discipline that prevents the common failure modes.

**Name everything.** Before you can work on anything in a new domain, you need to know what is there. Not understand it. Not explain it. Name it. This is a thing. That is a different thing. These are the things. Enumeration — making the domain's population explicit and finite — is the precondition for everything else.

The discipline is: do not skip this. Do not jump to connections before the names are complete. Do not theorize about relationships between things you have not yet named. If you cannot name something in one sentence, it is two things and needs splitting. If the list feels incomplete, there is a name missing — find it before moving on.

**Simplify.** After the names exist, compress the list through three operations. First, merge: are any of these the same thing under different names? If two names always appear together with identical behavior, they are one thing wearing two labels. Merge them. This reduces your working set. Second, split: do any of these have edge cases that behave differently from the main case? If a name conceals two behaviors, separate them. This increases your working set but increases it honestly — the edge case was always there, and naming it separately means you can handle it separately instead of being surprised when it diverges. Third, extract: does any of these make a decision? If so, separate the decision from the execution. The thing itself does not decide — a decision router decides, and the thing executes. This isolates complexity in a visible place rather than hiding it inside operations that should be simple.

**Connect.** Once the names are simplified, identify relationships between them. What follows what? What depends on what? What interacts with what? The connections are observed, not invented. You look at the named things and ask what the relationships actually are, not what you think they should be. If two things look connected but you cannot state the connection in one sentence, either the connection is not real or you have not named the intermediate thing that mediates it. Do not force connections for elegance. Connect because the relationship survives inspection.

**Compare to reality.** You now have names and connections. They predict something specific. Reality either confirms or denies. This is the step that separates the method from speculation. Does this name actually correspond to a single thing? Does this connection actually hold? Does the prediction the names and connections generate actually match what happens? The test is always the same structure: the model predicts, reality adjudicates. If you cannot state what the prediction is, the names and connections are not specific enough to be tested, which means they are not specific enough to be useful.

**Formalize or build.** If the work is theoretical, the names become definitions, the connections become axioms, the predictions become theorems, and the tests become falsification criteria. The formalization adds precision and communicability — it makes the observations rigorous enough to derive consequences that can be independently verified. If the work is practical, the names become types, the connections become interfaces, the predictions become tests, and you build the thing the specification describes. In either case, the formalization or construction must follow the naming and comparing, not precede it. Do not formalize guesses. Formalize what survived empirical comparison. Do not build before you have named what you are building.

**Test by gaming out.** You have formalized or built. Now actively try to break it. What if this assumption is wrong? What if this connection does not hold under these conditions? What if there is a case you did not name? This is not confirmation — it is adversarial testing against your own work. The coverage audit. The stress test. The question "what would kill this?" asked seriously with the intent to find the answer. Every failure you find yourself is cheap. Every failure someone else finds is expensive. Kill your own work before someone else does.

**Fail and restart.** This is the hardest discipline and the one that separates the method from everything else. When a name is wrong, when a connection does not hold, when a prediction fails, when reality contradicts the model — do not patch. Do not hedge. Do not add qualifiers until the claim survives by saying nothing. The claim failed. Publish the failure — it is a finding, not a shame. Find what the failure revealed. Name what is actually there, informed by what the failure taught you. Restart the cycle with better names.

The failed version dies. A new version emerges from its remains. Each restart incorporates everything the previous attempt taught. The new names are more precise because you know where the old names broke. The new connections are more accurate because you know which old connections did not hold. The new comparison is more targeted because you know which tests killed the previous version. The spiral tightens with each iteration — not because you are converging on a predetermined answer but because each failure eliminates territory and the surviving territory is smaller and more precisely mapped.

The failure mode this discipline prevents is the dilution cascade. When pressure arrives — a counterexample, a failed test, an objection — the natural response is to hedge. Weaken the claim. Add qualifiers. "In some cases, under certain conditions, the pattern may partially hold." Each hedge preserves the claim's existence at the cost of its content. After enough hedges, the claim says nothing. It cannot be wrong because it does not commit to anything. The method says: commit. If the commitment fails, the failure is informative. If you hedge instead, you learn nothing and produce nothing.

---

## Two Disciplines That Make It Work

The operational method produces results only if two underlying disciplines are maintained throughout.

**Failable design.** Everything you produce — code, claims, models, specifications — should fail loudly when it encounters something outside its specification. Not fail silently. Not catch the error and continue. Not log the exception and move on. Fail. Stop. Show you what went wrong and where.

In code, this means you do not write try/catch around your own logic. Your logic should work. If it does not, you need to know immediately — not after the error has propagated through six more functions and corrupted state you cannot reconstruct. Out of memory is information — it tells you your model of resource consumption is wrong at this specific point. Out of bounds is information — it tells you your model of data structure is wrong at this specific point. Null where you expected a value is information — it tells you your model of data flow is wrong at this specific point. Catching these errors is refusing to hear the feedback. The feedback is the most valuable thing the system produces.

The only place error handling belongs is at the boundary with things outside your control. The network drops. The disk fills. The hardware returns a fault. These are events you can observe but cannot prevent — they are outside your operational boundary. The correct response is structural resilience: catch the external failure, handle it with a predetermined response (abort, retry, degrade gracefully), and raise it to the level that needs to know. But the boundary between your logic and external events must be crisp. Everything inside the boundary should fail loudly on violations. Everything outside the boundary gets structural handling.

A hedged claim is the intellectual equivalent of a silent error catch. It catches every counterexample and continues as though the thesis stands. The counterexample was information — it was telling you the model is wrong at this specific point. The hedge suppressed it. The method depends on reality's feedback reaching you. Anything that blocks feedback — error suppression in code, hedging in claims, patching in specifications, defensive constructions that absorb contradictions — breaks the spiral.

**Testing range.** Do not only practice with things you can handle. Practice with things that defeat you completely.

In judo, this means you do not only spar with people at your level or below. You spar with people you cannot do anything against — complete walls. Then you know your limits. The technique that works on everyone at your level never works on them. This is information. It tells you the validity envelope of that technique — the range of conditions where it succeeds and the boundary where it fails. If you only practice against people you can beat, you never discover the boundary. You believe the technique always works because you have never tested it against what breaks it.

In language learning, tourist phrases and conversation are not the same thing. You can memorize the phrase book and produce acceptable output in controlled situations — ordering food, asking directions, greeting people. But when someone responds with three sentences of natural speech, you cannot parse any of it. The phrase book dissolved a narrow set of outputs. It did not dissolve the comprehension required for uncontrolled input. The validity envelope is the width of what you practiced. Tourist phrases produce a tourist-width envelope.

The expert discovers their limits by testing against what breaks them, not by confirming what works. The same dissolution that makes routine operations free can hide the boundaries where routine stops working. The plateau looks flat and safe — excellent performance, no indication of trouble. The cliff is at the edge, invisible until you step over it. Testing the boundaries deliberately — sparring with walls, attempting problems that are too hard, entering conversations where you cannot keep up — is how you map the cliff before you fall off it. The failures at the boundaries are the most informative data you can collect.

---

## Testable Predictions

The framework produces specific predictions that would be falsified by specific observations.

**Transfer affinity is measurable.** Dissolving a task in domain X should reduce the first-encounter cost for structurally related tasks in domain Y by a predictable amount proportional to the structural overlap between the tasks. This is testable by measuring processing cost on domain Y tasks before and after dissolving structurally related domain X tasks, with appropriate controls. Falsified if no correlation exists between structural overlap and cross-domain cost reduction.

**Acquisition rate increases with domain count when structural overlap exists.** A person dissolving their fifth structurally related domain should reach coverage faster than they reached coverage in their second. This is testable by tracking time-to-coverage across successive domain acquisitions for the same person. Falsified if acquisition rate is constant regardless of domain count, or if it increases even when successive domains lack structural overlap with the existing inventory.

**The operational method produces dissolution in any domain meeting the four conditions.** A person applying the method — name, simplify, connect, compare, formalize or build, test, fail and restart — should achieve measurable dissolution in any domain where rapid feedback, manageable iteration cost, context consistency, and sufficient repetitions are available, regardless of their prior domain history. Falsified if the method fails systematically in a domain meeting all four conditions despite faithful application.

**Domains failing dissolution conditions resist acquisition regardless of inventory.** A person with extensive dissolved inventory across many domains should still struggle to dissolve a domain where one or more conditions are absent — expensive iteration, slow feedback, unstable context, or gated repetitions. Falsified if someone dissolves such a domain at the same rate as a domain meeting all four conditions.

**Master-level work correlates with cross-domain dissolved inventory.** Transformative contributions — work that reveals structure invisible to single-domain experts, that connects previously unconnected domains, that produces what the domain has never seen — should correlate with the breadth of the producer's dissolved structural inventory across adjacent domains, not solely with time spent in the target domain. Falsified if time-in-domain is the sole predictor and cross-domain inventory adds no explanatory power.

**The meta-dissolution curve bends downward.** Time to coverage plotted against domain count should show a decreasing trend when successive domains share structural overlap with the existing inventory. Each new domain should dissolve faster than the last, not linearly but with accelerating returns, because the meta-structure of domain acquisition itself dissolves. Falsified if the curve is flat, linear, or does not accelerate when structural overlap is present.

---

## Scope and Honest Boundaries

This paper does not claim all domains are equally accessible. Domains are accessible to the degree that they meet the four dissolution conditions for a given person. The conditions are properties of the domain-person relationship, and they vary.

This paper does not claim cross-domain transfer replaces within-domain practice. Transfer provides hypotheses — candidate structural matches that enrich the enumeration stage of the reduction pipeline. Practice provides dissolution. The hypotheses must be tested within the domain, and the results must be dissolved through repetition within the domain. Transfer accelerates but does not substitute.

This paper does not claim the operational method guarantees mastery. Mastery requires the domain to have a living frontier and requires the processor to operate consciously on the domain's architecture rather than just its content. The method brings you to coverage reliably and to expert with sufficient practice. Mastery depends on what you do with your conscious processing once the routine is dissolved — whether you look at the problem or at what the problem reveals about everything else. That is a choice, not a procedure.

This paper does not claim the polyglot effect is unlimited. False structural parallels scale with domain count alongside true ones. When structural overlap between the new domain and existing inventory is low, the false-parallel rate can overwhelm the benefit of richer enumeration. The transfer mechanism predicts its own boundaries: it works when genuine structural overlap exists, and it does not work when it does not.

This paper does not claim any individual case as proof of universality. Any single corpus — any single person's cross-domain output — demonstrates possibility, not generality. The mechanism is the claim. Individual cases are data points. The predictions are falsifiable. The mechanism stands or falls on whether the predictions hold across many actors, many domains, and many conditions — not on any single demonstration, however extensive.

---

# Appendix Tables — Cross-Domain Learning: How Bits and Ops Transfer Between Domains

---

## Table A: Six Acquisition Levels

| level | name | definition | processing_signature | boundary_test | environmental_dependency |
|:---|:---|:---|:---|:---|:---|
| 0 | None | Domain invisible; cannot distinguish signal from noise; cannot enumerate what is unknown because compression tokens for segmentation are absent | Hp undefined on all elements; domain is outside operational boundary | N/A (entry state) | None |
| 1 | A little | Bit recognition achieved; some tokens decompress; most of domain is undifferentiated population; enough to know domain exists, not enough to navigate | Hp maximum for visible elements; undefined for invisible elements | Bit recognition: can person distinguish signal from noise, identify discrete tokens, recognize domain contains information? | None |
| 2 | Exposure | Major structures segmentable; common vocabulary partially dissolved; can follow arguments but not reproduce them; reduction pipeline works but slowly | Hp high but decreasing; common terms dissolving; specialized terms still costly | Structural segmentation: can person segment new domain material into major components without external help? | None |
| 3 | Coverage | Dissolution curve past knee; most common operations low cost; domain task topology visible; handles novel input without reference; mistakes on edge cases | Hp near zero for common tasks; moderate for uncommon; high for edge cases | Novel problem handling: can person solve unseen problem using standard patterns without reference material? | None |
| 4 | Expert | Routine operations dissolved; can teach, assess others, identify novel problems, produce original work; wide validity envelopes; efficient conscious processing on frontier | Hp near zero across standard task set; moderate for frontier | Teaching boundary: can person teach novice to coverage faster than they achieved it, accurately assess others, identify specific dissolution targets? | None |
| 5 | Master | Domain processing structure itself dissolved; sees architectural limitations, cross-domain connections invisible to specialists; operates on domain architecture not just content | Hp near zero on meta-structure; conscious processing directed at architectural questions | Architecture boundary: can person identify structural limitations, propose unconsidered alternatives, connect domain to other domains producing novel results? | Domain must be alive with unsolved problems and unexplored connections; dead domains ceiling at expert |

---

## Table B: Level Transition Markers

| transition | from | to | marker_name | observable_capability | historical_example_hieroglyphs |
|:---|:---|:---|:---|:---|:---|
| T1 | None | A little | Bit recognition | Distinguishes signal from noise; identifies discrete tokens; recognizes domain contains information | Rosetta Stone discovered; scholars recognize marks as language not decoration |
| T2 | A little | Exposure | Structural segmentation | Segments domain material into major components without help; identifies which regions address which subdomains | Cartouches distinguished from religious formulae from administrative records |
| T3 | Exposure | Coverage | Novel problem handling | Solves unseen problems using standard patterns without reference material; generalizes beyond training data | Unknown texts readable without Greek parallel translation |
| T4 | Coverage | Expert | Teaching | Teaches novice to coverage faster; accurately assesses other practitioners; identifies specific dissolution targets for others | Teaching others to read; identifying translation errors; producing original interpretations |
| T5 | Expert | Master | Architectural redesign | Identifies structural limitations of current framework; proposes alternatives experts haven't considered; connects to other domains producing novel results | Ceiling at expert — language is dead, no frontier; the record is the boundary |

---

## Table C: Expert vs Master at One

| property | expert | master |
|:---|:---|:---|
| State during novel work | One (conscious, active processing) | One (conscious, active processing) |
| Target of conscious processing | The problem | What the problem reveals about everything else |
| Output | More of what domain already has; mapped territory extended | What domain has never seen; often what domain could not see because its dissolved framework excluded it |
| Relationship to domain problems | Solves problems | Dissolves the problems that generate the problems |
| Effect on R* | Reduces own Hp for specific tasks | Reduces R* for entire task classes by finding structural shortcuts or reframing questions |
| Cross-domain visibility | Low — expertise is within one domain | High — multiple dissolved domains provide structural comparisons |
| Use of freed pipeline | Solve more problems faster | See connections, question structures, create transformative results |
| Domain classification effect | None — works within existing framework | May shift tasks from empirical-only to provably bounded, or from bounded to provable |

---

## Table D: Cross-Domain Transfer Mechanism

| component | definition | role_in_transfer | failure_mode |
|:---|:---|:---|:---|
| Source codebook | Processing structure dissolved in prior domains; reduction patterns, failure modes, cardinality relationships | Generates candidate structural matches for new domain; enriches enumeration | Codebook too narrow: few candidates generated; high probability of enumeration failure |
| Candidate generation | Dissolved A-structure offers structural hypotheses for B's unfamiliar elements | Expands enumeration set beyond what single-domain perspective would produce | False parallels: surface similarity masks different underlying mechanism |
| Filtering against reality | Candidates tested against new domain's actual behavior via compare-to-reality step | Eliminates wrong candidates; confirms correct ones; improves codebook accuracy | Skipping comparison: false parallels persist; codebook grows without improving |
| Compounding | Each dissolved domain adds structural entries to codebook; probability of correct match in enumeration increases with domain count | Reduces enumeration failure probability across successive domains | False parallels also scale; net benefit depends on genuine structural overlap exceeding false-match rate |
| Meta-dissolution | The structural recognition task itself dissolves with practice; recognizing which parallels are load-bearing versus surface becomes structural | Improves quality of candidate generation; reduces false-parallel rate | Without compare-to-reality feedback, meta-dissolution cannot occur; recognition does not self-correct |
| Self-communication model | Domain A dissolved structure is sender (near-zero encode cost); own attention is channel; domain B undissolved material is receiver (pays decode ops) | Dissolution differential between A-codebook and B-structural-requirements predicts cost | Imperfect alignment: processor imperfectly knows A, knows even less of B; alignment improves with practice in both |

---

## Table E: Four Dissolution Conditions

| condition | definition | why_required | domain_meeting | domain_failing |
|:---|:---|:---|:---|:---|
| Rapid feedback | Can test whether reduction was correct on timescale connecting result to attempt | Attempt and feedback must be close enough for pipeline to link cause and effect; delayed feedback does not drive dissolution | Programming (compiler errors in seconds); physics via Python (test in seconds); cooking (taste immediately) | Clinical trials (months to years); policy effects (years to decades) |
| Manageable iteration cost | Each attempt does not consume prohibitive resources | Cost per iteration bounds number of iterations; bounds dissolution rate; steep early curve requires many iterations | Software (free to compile); mathematics (paper and pencil); language practice (free conversation) | Rocketry (millions per launch); chip fabrication (months per iteration); surgery (one patient per attempt) |
| Context consistency | Domain holds still enough for repetition to accumulate | Core structure must be stable for repeated practice to produce genuine dissolution rather than perpetual re-learning | Mathematics (axioms stable); established codebases (architecture stable between refactors); physics constants (CODATA stable) | Early-stage startups (product changes weekly); active war zones (conditions change hourly); rapidly evolving APIs |
| Sufficient repetitions available | Can practice enough times for curve to descend meaningfully | Dissolution curve requires many repetitions; gated access limits how fast curve can descend regardless of other conditions | Typing (unlimited practice); instrument practice (unlimited); code review (continuous) | Rare surgeries (few per year); space missions (few per decade); judicial trials (few per career for specific case types) |

---

## Table F: Operational Method Steps

| step | name | action | maps_to_in_framework | discipline | failure_if_skipped |
|:---|:---|:---|:---|:---|:---|
| 1 | Name everything | Make domain population explicit and finite; one name, one thing, one sentence | Enumeration (first pipeline stage) | Don't skip; don't jump to connections; don't theorize about unnamed things; if can't name in one sentence, split | Unnamed elements invisible to pipeline; enumeration failure — correct answer never in candidate set |
| 2 | Simplify | Merge same-thing-different-names; split edge-cases-hiding-under-one-name; extract decisions into visible routers | Filtering (second pipeline stage); compression | Merge reduces working set; split increases it honestly; extraction isolates complexity visibly | Redundant names create false connections; hidden edge cases surprise during execution; embedded decisions make simple things unpredictably complex |
| 3 | Connect | Identify relationships between names; observe, don't invent; one sentence per connection or missing intermediate name | Scoring (third pipeline stage) | Don't force connections for elegance; connect because relationship survives inspection | Invented connections fail on contact with reality; missing connections leave structure incomplete |
| 4 | Compare to reality | Names and connections predict something specific; reality confirms or denies; run the test, yes or no | Selection (fourth pipeline stage) plus falsification | Don't skip comparison; don't assume correctness from internal consistency; state prediction explicitly | Model diverges from reality silently; errors compound; false parallels persist |
| 5a | Formalize (if formal) | Names become definitions; connections become axioms; predictions become theorems; tests become falsification criteria | Dissolution infrastructure (converting active understanding to communicable structure) | Math follows observation, not leads it; don't formalize guesses; formalize what survived comparison | Imprecise claims resist testing; consequences cannot be derived; communication fails |
| 5b | Build (if practical) | Names become types; connections become interfaces; predictions become tests; build what specification says exactly | Dissolution infrastructure (converting active understanding to working structure) | Deviations mean spec or implementation wrong; find out which | Implementation drifts from specification; defects hidden in gap between intent and construction |
| 6 | Test by gaming out | Actively try to break it; what if this assumption wrong? what case didn't I name? adversarial self-testing | Validity envelope widening; cascade testing | Kill your own work before someone else does; self-falsification is cheap, external is expensive | Untested assumptions become cliffs; failures discovered in production not development |
| 7 | Fail and restart | Failed claim dies; publish failure; find what failure revealed; rename from what learned; restart cycle; don't patch | Release back to Infinity and re-reduce with better enumeration | Don't hedge; don't patch; don't dilute; A fails, B emerges incorporating everything A taught | Dilution cascade: successive hedges drain claim of content; patches accumulate on broken foundation; spiral cannot tighten |

---

## Table G: Two Disciplines

| discipline | definition | mechanism | violation_consequence | boundary_example |
|:---|:---|:---|:---|:---|
| Failable design | Everything produced fails loudly at specification violations; no silent error absorption in own logic | Out of memory, out of bounds, null where expected are information about model incorrectness at specific points; feedback must reach processor | Silent catch hides contradiction; error propagates through subsequent operations; state corrupts; diagnosis becomes impossible when failure eventually surfaces | Only catch at boundary with uncontrollable externals: network drops, disk full, hardware faults; these get structural handling (abort, retry, degrade); own logic never silently caught |
| Testing range | Practice against what defeats you, not just what confirms you; test boundaries deliberately | Validity envelope width equals training breadth; sparring with walls maps cliff locations before you fall off them; tourist phrases are not conversation | Narrow practice produces narrow envelopes; cliff at boundary invisible from plateau; first encounter with out-of-envelope conditions produces unrecoverable cascade | Judo: practice with complete walls, not just peers; language: attempt uncontrolled conversation, not just phrase reproduction; code: test pathological inputs, not just happy paths |

---

## Table H: Hedging as Silent Catch

| code_pattern | knowledge_pattern | mechanism | consequence | method_alternative |
|:---|:---|:---|:---|:---|
| try/catch with empty handler | "X may sometimes contribute to Y" | Catches every counterexample; continues as though thesis stands | Error information suppressed; model incorrectness preserved; downstream failures larger and harder to diagnose | Let it fail; the exception tells you where the model is wrong |
| catch and log without action | "Some evidence suggests X, though results are mixed" | Records counterexample but takes no corrective action | False sense of monitoring; log grows but understanding doesn't; same failure recurs | Treat the counterexample as a finding; revise names and connections |
| catch with fallback to default | "When X does not hold, we fall back to general principles" | Replaces specific failed prediction with vague unfalsifiable one | Specific claim dies quietly inside vague wrapper; no one learns what failed or why | Publish the specific failure; find what it reveals; restart naming from what was learned |
| defensive null checks everywhere | "To the extent that data is available, the pattern appears consistent" | Preemptively absorbs every possible failure before it manifests | System never fails, therefore never provides diagnostic information; all feedback blocked | Fail on null; the null tells you which name doesn't correspond to a real thing |

---

## Table I: Transfer Affinity Examples

| source_domain | target_domain | shared_processing_structure | transfer_type | predicted_benefit |
|:---|:---|:---|:---|:---|
| TCP congestion control | Supply chain inventory management | Feedback loop under unreliable conditions; demand signal with delay; overshoot/undershoot dynamics | Structural: same reduction pattern, different tokens | High — same control-theoretic structure; vocabulary translates directly |
| Software state machines | Clinical diagnostic protocols | Enumeration of states; transition conditions; unreachable state detection; completeness checking | Structural: same enumeration and exhaustiveness pattern | Moderate — structure transfers; domain content (medical knowledge) does not |
| Musical instrument practice | Athletic skill acquisition | Dissolution curve shape; plateau detection; varied practice for envelope widening; motor chain dissolution | Process: same dissolution mechanics on motor chains | Moderate — meta-structure of practice transfers; specific motor patterns do not |
| Software debugging | Medical differential diagnosis | Enumerate candidates; filter by evidence; score by probability and severity; select and test; revise on new evidence | Pipeline: same four-stage reduction on candidate populations | High — pipeline structure nearly identical; experienced debugger recognizes diagnostic pattern immediately |
| Chess positional evaluation | Investment portfolio assessment | Weighted multi-factor scoring; positional versus tactical distinction; long-term versus short-term tradeoff | Scoring: multi-factor evaluation under uncertainty | Low-moderate — surface similarity high but underlying mechanism differs; chess is closed system, markets are not; false-parallel risk |
| TCP congestion control | Violin performance | None | No structural overlap | Zero — dissolved TCP provides no candidates for violin enumeration |

---

## Table J: Dissolution Condition Assessment Examples

| domain | rapid_feedback | manageable_iteration | context_consistency | sufficient_repetitions | conditions_met | predicted_accessibility |
|:---|:---|:---|:---|:---|:---|:---|
| Programming (new language) | Yes (compiler in seconds) | Yes (free) | Yes (language spec stable) | Yes (unlimited) | 4/4 | High — all conditions met; cross-domain transfer from other languages compounds |
| Physics via computation | Yes (Python in seconds) | Yes (free) | Yes (CODATA stable) | Yes (unlimited) | 4/4 | High — conditions met; transfer from SWE and math compounds |
| Conversational French | Moderate (conversation partner needed) | Yes (free with partner) | Yes (language stable) | Moderate (depends on immersion access) | 3-4/4 | Moderate — feedback delay is primary constraint; immersion dramatically improves |
| Rocketry (operational) | No (months per test) | No (millions per launch) | Moderate (physics stable, engineering varies) | No (few per year) | 1/4 | Low — theory accessible via computation; operations resist dissolution |
| Surgery (specific procedure) | Moderate (outcome visible but delayed) | No (one patient per attempt) | Yes (anatomy stable) | No (few per year for rare procedures) | 1-2/4 | Low for rare procedures — simulation partially substitutes; common procedures dissolve through residency volume |
| Cooking | Yes (taste immediately) | Yes (cheap ingredients) | Yes (chemistry stable) | Yes (multiple meals daily) | 4/4 | High — all conditions met; among fastest-dissolving practical domains |
| Early-stage startup strategy | No (market feedback in months) | Moderate (each pivot has cost) | No (market changes continuously) | No (limited pivots before capital exhaustion) | 0-1/4 | Very low — theory of startups accessible; actual strategic dissolution resists because conditions absent |
| Mathematics (proof writing) | Moderate (self-verifiable but slow) | Yes (free) | Yes (axioms permanent) | Yes (unlimited) | 3-4/4 | High for technique; proof discovery (frontier) is Class E with slower feedback |

---

## Table K: Falsifiable Predictions

| prediction | claim | test_method | falsification_criterion |
|:---|:---|:---|:---|
| PR1 | Transfer affinity is measurable: dissolving task in domain X reduces first-encounter cost for structurally related tasks in domain Y | Measure processing cost on domain Y tasks before and after dissolving structurally related domain X tasks; control for unrelated tasks | No correlation between structural overlap and cross-domain cost reduction |
| PR2 | Acquisition rate increases with domain count when structural overlap exists | Track time-to-coverage across successive domain acquisitions for same person; record structural overlap between each new domain and existing inventory | Acquisition rate constant regardless of domain count; or increases without structural overlap |
| PR3 | Operational method produces dissolution in any domain meeting four conditions | Apply method (name, simplify, connect, compare, formalize/build, test, fail-restart) in domain meeting all four conditions; measure dissolution curve | Method fails systematically in domain meeting all four conditions despite faithful application |
| PR4 | Domains failing dissolution conditions resist acquisition regardless of inventory | Person with extensive dissolved multi-domain inventory attempts domain failing one or more conditions; measure dissolution rate | Person dissolves condition-failing domain at same rate as condition-meeting domain |
| PR5 | Master-level work correlates with cross-domain dissolved inventory | Assess transformative contributions against producer's breadth of dissolved structural inventory across adjacent domains and time-in-target-domain | Time-in-domain is sole predictor; cross-domain inventory adds no explanatory power |
| PR6 | Meta-dissolution curve bends downward | Plot time-to-coverage against domain count for persons acquiring successive structurally overlapping domains | Curve flat, linear, or does not accelerate when structural overlap present |

---

## Table L: The Polyglot Effect Across Domain Types

| domain_count | language_analogy | general_domain_analogy | meta_structure_state | typical_acquisition_character |
|:---|:---|:---|:---|:---|
| 1 (first) | First foreign language; full cost on everything; phonology, grammar, vocabulary, pragmatics all at maximum cost | First domain beyond native expertise; every pattern novel; process of learning itself costs full ops | Undissolved; learning how to learn | Slow; high error rate; frequent enumeration failure; process feels arbitrary |
| 2-3 | Some grammar categories recognized across languages; false cognates concept established; learning process partially dissolved | Structural parallels to first domain recognized; compare-to-reality discipline emerging; merge/split instincts developing | Partially dissolved; some meta-patterns recognized | Faster than first; still high false-parallel rate; process becoming recognizable |
| 4-7 | Grammar mapping dissolved; phonological categories dissolved; vocabulary bootstrapping via cognates and context dissolved; learning process efficient | Reduction pipeline recognition across domains dissolved; failure mode taxonomy emerging; naming discipline automatic | Substantially dissolved; meta-structure available as structural codebook | Noticeably faster; false-parallel rate decreasing; process feels familiar regardless of domain content |
| 8-15 | New language acquired in weeks; structural recognition fires immediately; content is new but structure is free | New domain's processing structure recognized quickly; content dissolves fast when structure already decoded; novel contributions possible early | Fully dissolved; domain acquisition is itself a dissolved skill | Fast; low false-parallel rate; process is transparent; focus shifts from learning process to domain content immediately |
| 15+ | New language acquired in days of immersion; existing codebook so rich that most structural patterns pre-decoded | New domain decoded primarily through existing structural inventory; genuinely novel structures rare and highly informative | Dissolved and refined; meta-codebook large and accurate | Very fast where structural overlap exists; clear recognition of where overlap is absent; honest about limits |

---

## Table M: Processing Entropy Signature by Level

| level | routine_tasks | novel_standard_tasks | frontier_tasks | meta_structure | overall_profile |
|:---|:---|:---|:---|:---|:---|
| None | Undefined | Undefined | Undefined | Undefined | No elements visible; profile does not exist for this domain |
| A little | Maximum (for visible elements) | Undefined (cannot distinguish novel from routine) | Undefined | Undefined | Sparse; few elements visible; all costly |
| Exposure | High, decreasing | High | Undefined (cannot identify frontier) | Undefined | Broad but uniformly high; dissolution beginning on common elements |
| Coverage | Near zero | Moderate | High | High | Bimodal: dissolved common tasks plus costly uncommon; task topology visible |
| Expert | Near zero | Low-moderate | Moderate | Moderate | Near origin for standard set; moderate on frontier; wide validity envelopes |
| Master | Near zero | Low | Moderate (directed at architectural questions) | Near zero | Near origin across domain; conscious processing targeted at structure not content |

---

## Table N: Historical Level Transitions — Egyptian Hieroglyphs

| year_approximate | event | from_level | to_level | marker | evidence |
|:---|:---|:---|:---|:---|:---|
| Pre-1799 | European scholars examine hieroglyphs | None | None | Cannot determine whether marks are language, decoration, or religious symbolism | Debate over whether hieroglyphs carry linguistic content at all |
| 1799 | Rosetta Stone discovered | None | A little | Bit recognition: aligned Greek text proves marks are language | Individual token mapping begins; first symbols decoded |
| 1822 | Champollion decipherment | A little | Exposure | Structural segmentation: phonetic vs logographic principles identified; cartouches parsed; grammatical categories emerging | Can distinguish text types; can read known parallel texts; cannot read arbitrary texts independently |
| Mid-1800s | Grammar and vocabulary systematized | Exposure | Coverage | Novel problem handling: unknown texts readable without parallel; generalization beyond Rosetta training data | Scholars read temple walls, administrative records, literary texts without Greek parallel |
| Late 1800s-present | Mature Egyptology | Coverage | Expert | Teaching boundary: textbooks written; students trained to coverage; translations assessed; original interpretations produced | University departments; peer review; standardized pedagogy; original scholarly contributions |
| N/A | Master level | Expert | Ceiling | Architecture boundary unreachable: no living speakers, no new texts being produced, no frontier to push against | Domain is dead; record is the boundary; structural limitations of current framework identifiable but not testable against new data |

---

## Table O: Dead Domain Constraint

| property | living_domain | dead_domain |
|:---|:---|:---|
| Frontier | Exists; unsolved problems; unexplored connections; novel data arriving | Absent; record is fixed; no new data; unsolved problems are permanently unsolvable due to missing evidence |
| Maximum achievable level | Master (no ceiling) | Expert (ceiling at architecture boundary) |
| Novel work possible | Yes; original contributions at frontier; transformative structural work | Limited; reinterpretation of existing record; combinatorial analysis of fixed corpus |
| Cross-domain connection testable | Yes; predictions can be tested against new domain behavior | Limited; connections can be proposed but not tested against new evidence from within the dead domain |
| Validity envelope expandable | Yes; new conditions encountered; envelopes widen through practice under novel circumstances | No; conditions are historical and fixed; envelopes cannot widen beyond what the record contains |
| Architectural redesign testable | Yes; alternative frameworks produce different predictions testable against new data | Limited; alternative frameworks may organize existing data differently but cannot be adjudicated by new evidence |
