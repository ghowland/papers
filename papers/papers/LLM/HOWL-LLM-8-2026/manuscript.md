# The Low-Token / Next-Token Problem

## Why the Weakest Choice Governs the Strongest Weight

**Registry:** [@HOWL-LLM-8-2026]

**Series Path:** [@HOWL-LLM-3-2026] → [@HOWL-LLM-7-2026] → [@HOWL-LLM-8-2026]

**DOI:** 10.5281/zenodo.zzz

**Date:** July 2026

**Domain:** LLM Mechanics / Generation Theory

**Status:** Working Methodology

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections and one biographical note were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.8. 

---

## 1. Why this paper exists

Two earlier papers in this series described consequences without isolating their cause. [@HOWL-LLM-3-2026] established that LLM generation is ballistic — launched, not steered — and that the illusion of steering comes from adjusting the launch. [@HOWL-LLM-7-2026] established that repeated machine modification erodes the structural coherence of mature software, the decoherency tumbler. Both papers are correct, and both stand on a mechanism at the sampler floor that has been used throughout the series but never lifted out and examined on its own.

This paper lifts it out. The mechanism is small enough to state in a paragraph and permanent enough to survive any amount of scaling. It is responsible for a set of failures that appear unrelated to a user — the code that drifts out of your style, the variable the model will not stop renaming, the security fix that quietly reverts, the confident wrong answer in an unfamiliar domain — and are in fact one failure, seen from different angles.

The mechanism is easiest to reach through a single question, which the paper will answer completely: **what will the next token be, after the least-worst last token?**

The reader is assumed to use LLMs and to understand, at a working level, that generation proceeds one token at a time. No further machinery is assumed. Each concept is built before it is used, and the paper's claim is not a discovery but an explanation — a mechanism walked from the floor upward, with its consequences enumerated so they can be recognized in the wild.

## 2. The machine's one move

An LLM performs exactly one operation. Given a sequence of tokens — the context — it produces a probability distribution over the possible next token, and one token is selected from that distribution. That token is appended to the context, and the operation repeats. There is no second mechanism. Everything the model appears to do at a higher level — reasoning, planning, refusing, recalling — is this one move, run in sequence.

Because there is only one move, the quality of a generation is entirely the quality of its individual selections, and the quality of a single selection is governed by one underlying quantity: **support**. Support is how much of the training data informs the distribution at this specific point in this specific context. It is the sample size behind the estimate.

Support is not uniform, and its non-uniformity is the entire subject of this paper. Across different contexts, support varies by many orders of magnitude. In some contexts the model is estimating a next-token distribution from effectively the whole corpus; in others, from a handful of examples; in others, from nothing that resembles the current situation at all. The model's behavior is radically different in these regimes, and it gives the user no signal about which regime it is in. The output looks the same either way. That last fact — uniform-looking output across wildly non-uniform support — is where most practical trouble begins, and the paper returns to it repeatedly.

Begin with the regime where everything works.

## 3. The landslide

The deepest statistics in the entire corpus are the shallowest ones: pair statistics — which token tends to follow which. Every adjacent pair of tokens ever written contributes a sample to these counts, so the evidence behind them is denser than the evidence behind anything else the model knows. This is why, of everything in the context window, the **immediately prior token carries the strongest local conditioning weight**. Attention reads the whole window and integrates far-flung context, but the local pull exerted by the last token is backed by the most samples the model has for anything, and it dominates the shape of the next distribution more than any single other feature.

The clean demonstration is the fragment **"straw-"**. Ask what token comes next and there is, functionally, no distribution to speak of: "berry" takes almost all the probability mass, and "berries," "man," "-colored," and a scattering of others divide the remainder. Millions of samples inform this one selection. It cannot go wrong. The prior token has all but determined the next.

Call this regime the **landslide**: dense support, a sharp peak, the next token nearly forced and nearly always correct. The overwhelming majority of tokens in the overwhelming majority of generations are landslides. This is not a weakness — it is why generation works at all. A machine that produced fluent, grammatical, mostly-correct text could do so only if most of its selections were nearly forced, and they are. The landslide is the model's home ground, and on its home ground it is superb.

The paper is not about the landslide. It is about what happens when the model leaves it.

## 4. Determinism is not the cure

Before descending into the sparse regime, one exit must be closed, because it is the exit most readers reach for first.

The natural intuition is that the trouble is *randomness*. The model samples from a distribution; sampling introduces chance; therefore reduce the chance. Set temperature to zero and take the most probable token every time. Or go further than temperature — the author's own work removes the last sources of nondeterminism from the arithmetic itself. Deployed LLM inference is not actually deterministic even at temperature zero: floating-point addition is non-associative on parallel hardware, so reduction order changes the low bits; batching makes one request's computation depend on which other requests share its batch; mixture-of-experts routing can flip on epsilon differences; serving stacks differ across machines. The VDR series ([@HOWL-VDR-1-2026] and following) replaces floating-point arithmetic with exact integer-rational arithmetic and achieves bit-identical output on every run, in transformers and in diffusion models alike. Determinism, at every level, is achievable. The author has achieved it.

It cures nothing that this paper is about.

Determinism makes a selection *reproducible*. It does not make the underlying distribution *better estimated*. A deterministic model that walks into a badly-mapped region of the corpus takes the same wrong turn on every run — a frozen error instead of a variable one. The exact-arithmetic experiments demonstrate this directly: the streams become perfectly reproducible, and they contain exactly the same class of failure they contained before, now repeatable to the bit. This is worth stating as a finding, because it retires a common hope: **determinism was never the disease.** The disease is not that the model chooses randomly among candidates. The disease is that, in some regions, all the candidates are bad, the model cannot tell, and it must choose anyway. That is the next section.

## 5. The least-worst token

Some contexts are rare. Your codebase uses a pattern almost no one else uses. A constraint combination arises that the corpus barely contains. A technical corner is reached that few people have ever written about publicly. A convention is invoked that exists, in its exact form, in one repository on Earth — yours. In these regions, the next-token distribution is not a landslide. It is a smear: a small set of candidate tokens, each backed by thin evidence, the estimates poor because the corpus scarcely visited this territory. The peak is low and the shoulders are flat. The model does not know what comes next, in the only sense a model can be said to know anything — the distribution it computed is not concentrated.

And the model must emit something. The architecture has no abstain, no "I am not sure," no request for clarification issued from inside the forward pass. It computes a distribution and a token comes out. So it selects the best of a bad shortlist — the **least-worst token**: the most probable candidate in a set where even the most probable candidate is not well-supported. Frequently this token is not what the context actually called for. It is not your variable name; it is the corpus's name for that kind of object. It is not the struct field your system defines; it is the field a similar-looking system would have. It is the nearest thing the thin evidence could suggest, which in a sparse region is a thing borrowed from a denser region nearby.

A single least-worst token, in isolation, is survivable. A user might not even notice it. The problem is not the token. The problem is everything that comes after it, and to see why requires one more mechanical fact — the one the whole paper turns on.

## 6. The laundering step

Here is the mechanical heart of the low-token/next-token problem, and it is a single sentence with heavy consequences: **the least-worst token, once emitted, enters the context with full authority.**

Consider what the context window actually is. It is a sequence of tokens. It is *not* a sequence of tokens each annotated with the confidence that produced it. When the model selected the least-worst token, that selection came out of a low, flat, five-candidate smear — a distribution that, if it could speak, would have said "I have very little to go on here." But the distribution does not travel forward. Only the token does. And once the token is in the context, it is indistinguishable, in every respect that affects the next selection, from a landslide token that came out of a million-sample peak. The context contains "the token that was chosen," not "the token that was chosen, and here is how unsure the model was when it chose it."

There is no channel — none, at any model scale, at any temperature, in any current architecture — by which the uncertainty that produced a token propagates to the tokens that follow it. The forward pass has no memory of its own doubt. The posterior uncertainty is *laundered into prefix fact* at the instant of emission. The model has its doubt, emits, and one token later has forgotten it entirely, because there was never anywhere for that doubt to be stored.

Now combine this with Section 3. The strongest local conditioning weight on the next selection is the immediately prior token. So the next selection conditions *hardest* on precisely the token that was least trustworthy — and it conditions on it as though it were certain, because the machine cannot represent that it was anything else.

This is the pivot of the entire mechanism. A model that could carry its uncertainty forward could recover: it could treat a low-confidence token as tentative, hedge the next step, hold the door open for a correction. It cannot. The uncertainty is gone, the token is fact, and the fact is the heaviest single influence on what comes next.

## 7. Sparse conditions on sparse

Follow the sequence forward from the laundered token.

The context was already in a sparse region — that is what produced the least-worst token in the first place. The token that was emitted is slightly wrong for that region: a median borrowing, an approximate fit. Now ask about the support for the *pair*: the wrong-ish token, followed by whatever should come after it, in this already-rare context. That pair is rarer than the region was. A rare context that now contains a mildly off token is a *more* specific, *less* sampled situation than the rare context alone. The candidate set for the next token narrows. The estimates degrade. The next selection is a least-worst drawn from a shortlist worse than the one before it.

This is the low-token/next-token problem, stated exactly. **Tokens that follow low-choice tokens are worse selections, because they sequentially inherit a prefix built from low-choice selections — and the strongest weight of all is the prior token.** The error does not merely persist into the next step. It compounds, because each step conditions most heavily on the previous step's weakest output, and each step's own uncertainty is laundered before the following step runs. There is no point at which the accumulated doubt becomes visible to the machine and triggers a correction, because the doubt was never accumulated anywhere. Each step begins fresh, treating a compromised prefix as ground truth.

The intuitive form of this, which every experienced user has felt without a mechanism for it: *if the last turn was good enough, why is this turn different?* Because nothing held the last turn in place. There is no invariant, no confidence carried forward — only the next selection, conditioned on a prefix that silently degraded. The generation is not being steered off course by an external force. It is walking off course under its own conditioning, one laundered token at a time.

## 8. Drainage

The compounding has a shape, and the shape is the reason the failure is so difficult to catch in the act.

Picture the corpus as terrain. The dense-support regions — common idioms, tutorial patterns, the median of everything ever written publicly — are valleys: broad, low, heavily sampled, easy to fall into and hard to climb out of. The sparse regions — your specific system, your unusual requirement, your one-of-one convention — are ridgelines: narrow, high, lightly sampled, easy to fall off. A least-worst token is a step off the ridge. And every subsequent conditional, pulled by the mass of the corpus, flows *downhill* toward the valleys.

Crucially, the stream does not fragment as it falls. The model's fluency machinery fights fragmentation at every single step: whatever the prefix now contains, however compromised, the model finds a continuation that renders it locally coherent. It is very good at this — local coherence is a landslide-grade skill, backed by enormous support. So the generation does not break. It **bends**. It exits the intended region along a smooth, plausible curve and re-enters the nearest dense basin, where support is thick again and every selection is a landslide once more. The generation *recovers its confidence without recovering its correctness*. It reads well. It reads better, often, than the correct output would have, because the valley is where the most fluent, most idiomatic, most tutorial-shaped text lives.

This is the signature that every practitioner has seen and few have named. A function that begins in your idiom — your naming, your structure, your conventions — reaches the part of your pattern the corpus does not know, takes one soft wrong turn there, and then proceeds with total fluency in a dialect that is no longer yours. The guard you would never write. The allocation in the wrong style. The renamed variable. The helpful refactor of the thing that must not be refactored. The error is not the wrong turn. The error is that everything after the wrong turn conditioned on it with full weight, and the stream's own coherence-seeking actively steered toward the valley where that wrong token is normal and your intent is foreign.

Name the phenomenon: **drainage.** Not a random walk — a random walk has no preferred direction, and this has a strong one. The descent is directed, always the same direction: away from the specific intent that lives on the ridge, toward the corpus mass that fills the valley. And under deterministic sampling, it is the *same* descent every run — the exact-arithmetic experiments show a generation draining down the identical path each time, because the terrain is fixed and the walk is now deterministic. Reproducible descent toward the mean.

## 9. The atomic case: the renaming problem

The smallest complete instance of the mechanism has been observed for years, resists every attempt at instruction, and contains every element of the machinery in miniature.

Name a variable `viewScreen` in a context where the corpus's overwhelming convention for that kind of object is `viewRect`. Ask the model to work with your code, and watch it rename the variable — not once, correctable, but persistently, reverting your name every time it must produce the identifier, regardless of how forcefully you forbid it.

The mechanism is exactly the one this paper has built. The identifier is not *stored* anywhere as a fact the model holds. Every time `viewScreen` must appear in the output, it is *reconstructed* — the model reaches the position where the name goes and runs the same next-token election it runs everywhere. At that position, two forces vote. In-context evidence: your code, right there in the window, saying `viewScreen`, a distribution informed by a single sample. Prior mass: a million repositories where an object of that shape is named `viewRect`, a landslide. Copy-from-context is a real and strong behavior — the model does mostly repeat identifiers it sees — but it is a *weighting*, not a rule. It is one force among two, and where your name is semantically "wrong" by corpus standards, the two forces are close enough that the election is genuinely contested. It only has to lose once. And it is held dozens of times per file, once at every appearance of the name.

The moment it loses once, the laundering step (Section 6) takes over and the loss cascades. The median token `viewRect` enters the context with full authority. Now the context contains *both* names, and the median one has in-context support too. Every subsequent election is conditioned on a contaminated electorate, and the model is not "changing your name back" — it is re-deriving the name at every use site, and the derivation now has evidence on both sides, pulling harder toward the corpus with each appearance it wins. Drainage, at the granularity of a single identifier.

This is why enforcement language fails, and it fails *structurally*, not for lack of emphasis. "NEVER rename these variables — many modules depend on them, renaming breaks the build" is, mechanically, more tokens in the context. Those tokens shift the weighting at each election. They do not remove the election. Removing the election would require a rejection step — a mechanism that checks the proposed token against a constraint and refuses violations — and the forward pass has none (Section 6). Putting the rule in the prompt is an attempt to install an invariant through the context window, and the context window is an *evidence channel for an estimator*, not an invariant store. You can add evidence. You cannot add a constraint. Berating the model is adjusting a prior with a rock.

The available outcomes are exactly two, and there will never be a third within this architecture. Either rename your variable to `viewRect` — dissolve the conflict by moving your code onto the corpus's manifold, so that prior and context vote together and the election becomes unanimous — which works, at the cost of a small payment of *yours-ness* each time, sanding off the specificity that made your code navigable and yours. Or take the artifact out of the sampler's jurisdiction entirely: generate once, own it, and never submit it to another election. **Rename it, or own it.** The whole of this paper is contained in that variable.

## 10. Where sparse support lives

The mechanism would be a curiosity if sparse regions were rare, or unimportant, or shrinking. They are none of these. They are where all the value is, and they are inexhaustible.

The intuitive hope is that scaling solves this: a larger model trained on a larger corpus has denser support everywhere, so the sparse regions fill in and the least-worst token becomes rare. Scaling does densify the manifold — it genuinely improves coverage of the common. But it cannot reach the regions that matter most, for a structural reason: **the valuable regions are valuable precisely because they are rare.** Your codebase exists once. Your architectural conventions exist once. A genuine fix for a real security vulnerability is off-median *by construction* — the vulnerability existed *because* the natural, corpus-dense way to write that check was subtly wrong, so the fix is necessarily a departure from the dense pattern (see [@HOWL-COMP-14-2026] on regression to the vulnerable mean). A genuinely new system, an unprecedented constraint, a first-of-its-kind design: each one mints new off-manifold territory that no prior corpus could contain. **Specificity generates the sparse tail faster than any training run absorbs it.** The tail is not a shrinking remainder that scaling will eventually eliminate. It is continuously replenished by exactly the acts — building the new, fixing the specific, holding a convention — that constitute original technical work. The machine is strongest where you need it least, and weakest at the precise coordinates of everything that makes your work yours.

The full escalation, from safe to impossible:

**Dense support** — millions of samples. Landslides; stable, correct streams. Common idioms, tutorial patterns, mainstream framework code, genre artifacts. The model's home ground.

**Thin support** — hundreds of samples. Least-worst picks that enter the context with full authority. Uncommon APIs, niche conventions, the first sign of trouble.

**Sparse-on-sparse** — pair-level support after a least-worst token. Compounding; the drainage begins. This is the interior of a generation working through your specific code.

**Off-manifold** — one-of-one. No meaningful estimate exists; the model snaps to the nearest dense region and drains toward it. Your codebase, your fix, your convention — and, outside software, your face against a matcher trained on a distribution you have left ([@HOWL-COMP-14-2026] treats the identity-drift case).

**Zero support** — self-invented. A dialect whose only sample is its own just-emitted definition. Ask the model to invent a macro language and then write programs in it: the language has, at the moment of use, a corpus of exactly one document — the definition it produced four hundred tokens ago. Its only mechanism for using the language correctly is in-context imitation, which is soft, decays with distance, and bends steadily toward the raw-corpus mass where the macro does not exist. Bootstrap incoherence: the language, its implementation, and its entire usage corpus must all be generated in one mutually-conditioning stream, with no external verifier anywhere in it.

One inversion completes the terrain map, because it shows that even dense support does not contain what would actually rescue the sparse case. Dense regions have their own blindness. Where support is overwhelming, sequences fuse into single statistical units and their *internal structure* becomes invisible. The well-known failure to count the letters in "strawberry" is not a sparse-support failure — it is the opposite. "berry" after "straw-" is so forced, so landslide, that the word passes through the model as one fused object, and its component letters were never load-bearing in any conditional the model ran. Thin support cannot find your structure; dense support cannot see structure at all, only flow. And neither regime contains *holding* — the carrying of a fact across positions, checked and enforced. This is the finding of the companion papers restated at the token floor: the architecture has no rejection step, and — this paper's specific contribution — **no confidence channel.** The machine can neither refuse a proposed token nor remember that it was unsure of one. Both absences are permanent for the architecture, and between them they are the entire low-token/next-token problem.

## 11. Containments

The mechanism cannot be fixed. It is architectural, and this paper's final claim is that no amount of scaling touches it. But it can be *routed around*, and four containments are documented across this registry, in ascending order of strength. Each one accepts that the machine forgets its doubt, and works around the forgetting rather than curing it.

**Manufacture density.** If the sparse region is where failure lives, make the region locally dense for the duration of one generation. Pack the context with owned material: the struct definitions, the named existing patterns the new code should follow, the specification written from ownership. This performs, by hand, a kind of kernel-density estimation around your own conventions — for one generation, your off-manifold territory has enough in-context evidence to shift the elections in your favor, and they run with the best odds they will ever have. This is why one carefully-assembled prompt outperforms a hundred corrective exchanges: the corrections arrive after the drainage, while the manufactured density arrives before it. (Specification: [@HOWL-ENG-3-2026] Appendix F.1; [@HOWL-COMP-14-2026] context assembly.)

**One pass.** Manufactured density is a wasting asset, and this is the containment users most often violate. Every token the model *generates* and appends to the context is median material that dilutes your owned evidence; every subsequent turn re-runs every election with a progressively more contaminated electorate. Multi-turn refinement of owned code is, mechanically, a daily referendum on every identifier and every convention in the file, held against an electorate of everything ever written, with each turn's median output added to the voter rolls. The renaming problem is unwinnable across turns for exactly this reason. Generate once, at maximum attention, against maximum manufactured density — and then stop submitting the artifact to the sampler.

**External certainty.** Since the machine has no memory of its own confidence, supply one from outside. Every load-bearing property must live in machinery that actually holds things: deterministic verifiers, pinned tests, type systems, checked runtime invariants, deterministic code generators. The generator proposes; the machinery rejects violations; the rejection step the architecture lacks is bolted on externally. This is the whole strategy of the composition method in [@HOWL-COMP-14-2026] and the conversion criterion in [@HOWL-ENG-3-2026] Appendix B: never ask the model to hold an invariant, because it cannot; put every invariant in a machine that can.

**Ownership on arrival.** The strongest and most permanent containment is the artifact's exit from the sampler's jurisdiction. Integrate the output, adjust it, debug it, commit it in your own words — build position in it ([@HOWL-ENG-3-2026] Steps 3 and 6) — and it enters stillness, where no election is ever held over it again. Drainage operates only on what the sampler can still touch; code that has become yours is no longer in play. This is why the durable protocol is generate-once-then-own: the generation is the model's, the ownership is yours, and the boundary between them is patrolled by the act of integration.

The honest boundary must be stated plainly, because it is the paper's final claim. All four containments are *routing*, not repair. The mechanism is in the architecture. Scale the model a hundred-million-fold and every estimate improves, the sparse regions recede somewhat, the least-worst tokens grow rarer — and nothing structural changes. The forward pass will still lack a rejection step. The context will still be a sequence of tokens rather than of confidences. The prior token will still carry the strongest weight. And a least-worst token will still be laundered into fact one step after it was doubted, in whatever sparse regions remain — and Section 10 established that sparse regions are replenished by original work faster than scaling drains them. The problem is permanent for this architecture. A different architecture — one with an actual rejection step and an actual confidence channel — would be a different machine, and building it is a different program (see [@HOWL-LLM-1-2026] and the VDR-LLM-Prolog series, where the rejection step is provided by construction through a symbolic knowledge base). That program is the only thing that changes the answer to this paper's question.

## 12. Closing

The question was: what will the next token be, after the least-worst last token?

The complete mechanical answer: **the least-worst continuation of a prefix that now contains an error wearing the costume of a fact — chosen from a smaller candidate set, with thinner support than the token before it, pulled downhill by the mass of the corpus, and delivered with exactly the same fluency as everything else in the stream.** The error is invisible in the output because the output is uniformly confident; the descent is directed because the corpus has a center of mass; and the whole process is deterministic under exact arithmetic, which proves that the trouble was never randomness but always the machine's inability to know, or to remember, that it did not know.

Everything else built across this registry's LLM and engineering series is machinery against that one sentence. The tumbler's deterministic verifiers, the pinned invariants, the one-pass discipline, the ownership protocol, the human held at the end of every accountability chain, the symbolic rejection step of the VDR-LLM-Prolog architecture — all of it is a single intervention applied at different altitudes and different scales. It is, in every case, the same thing: **an external memory of certainty, built around a machine that forgets its own doubt one token after having it.**

---

## Appendix A — The Support Escalation Ladder

| Regime | Support depth | Selection behavior | Stream effect | Example |
|---|---|---|---|---|
| Landslide | Millions of samples | Near-forced, near-always right | Stable, correct | "straw-" → "berry"; tutorial idioms; mainstream framework code |
| Thin | Hundreds of samples | Least-worst pick; enters with full authority | First soft wrong turn | Uncommon API; niche convention |
| Sparse-on-sparse | Pair-level, post-least-worst | Worse least-worst from a narrower set | Compounding; drainage begins | Interior of a generation working through your specific code |
| Off-manifold | One-of-one | Snap to nearest dense region | Full drainage; dialect shift | Your codebase; a real security fix; the renaming problem; identity drift |
| Zero-support | Only its own definition | In-context imitation, decaying with distance | Bootstrap incoherence | A self-invented macro language, written in itself |
| Dense-fused (inverse) | Overwhelming | Sequence passes as one fused unit | Internal structure invisible | Counting the letters in "strawberry" |

## Appendix B — The Drainage Trace

*A single generation over owned code, step by step.*

| Step | Context state | Support regime | Selection | Effect on stream |
|---|---|---|---|---|
| 1 | Owner's idiom; context packed with owned structs and named patterns | Manufactured density | Landslides | Correct; in your dialect |
| 2 | Reaches the one-of-one pattern — the unusual guard, the owned name | Off-manifold | Least-worst: the nearest median equivalent | Soft wrong turn; enters context with full authority |
| 3 | Prefix now contains the median token | Sparse-on-sparse | Conditions hardest on the least-trustworthy token | Error compounds; no doubt carried forward |
| 4 | Stream bends toward the dense basin | Rising toward dense | Landslides — in the *wrong* dialect | Fluency fully recovered; correctness not |
| 5 | Remainder of generation | Dense | Confident, idiomatic median continuation | The building looks perfect; it is no longer yours |

## Appendix C — Containment Cross-Reference

| Containment | This paper | Full specification elsewhere in the registry |
|---|---|---|
| Manufacture density | §11.1 | [@HOWL-ENG-3-2026] App. F.1 (phase 3); [@HOWL-COMP-14-2026] context assembly |
| One pass | §11.2 | [@HOWL-ENG-3-2026] App. F.3 (multi-turn erosion); [@HOWL-LLM-2-2026] |
| External certainty | §11.3 | [@HOWL-COMP-14-2026] verifier stack; [@HOWL-ENG-3-2026] App. B (conversion criterion) |
| Ownership on arrival | §11.4 | [@HOWL-ENG-3-2026] Steps 3, 6 (position, the log); [@HOWL-COMP-14-2026] two-class theorem |
| Architectural replacement (out of scope here) | §11 boundary | [@HOWL-LLM-1-2026]; VDR-LLM-Prolog series (rejection step by construction) |

## Appendix D — Relation to Prior LLM-Series Papers

| Paper | Establishes | This paper adds |
|---|---|---|
| [@HOWL-LLM-3-2026] Riding the Rocket | Generation is ballistic, not steerable | The token-level mechanism *of* ballistic drift: laundering + prior-token dominance |
| [@HOWL-LLM-4-2026] Incompatibility by Construction | What cannot be fixed with more LLM | The specific unfixable: no confidence channel, permanent for the architecture |
| [@HOWL-LLM-7-2026] Agentic Decoherency Tumbler | Repeated modification erodes coherence | The per-token cause of per-edit erosion: every regeneration re-runs the elections |
| [@HOWL-LLM-1-2026] Integer LLM + Prolog | A neural-symbolic architecture | Names precisely what the symbolic side supplies: the missing rejection step |
