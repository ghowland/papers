# What Is The Universe Made Of, Really?
## A Plain-Language Guide to the PCTRM Substrate Specification

**Document:** pctrm_substrate_plain_language.md
**Audience:** Science-aware readers — you know what an atom is, you've heard of quantum mechanics, you don't need equations to follow an argument
**Purpose:** Explain what PCTRM says is actually going on at the most fundamental level of reality
**Date:** April 20, 2026

---

## The Question This Paper Answers

Physics has two descriptions of reality that both work spectacularly well but have never been put together.

**Quantum mechanics** describes the very small — atoms, particles, light. It makes predictions accurate to parts per trillion. It also has weird features nobody understands: particles that are connected across vast distances instantly, particles that are "waves" until you look at them, measurements that seem to change what's real.

**General relativity** describes the very large — gravity, the shape of spacetime, the expansion of the universe. It also makes predictions accurate to parts per trillion. It describes space and time as a smooth, continuous fabric that bends under matter.

Both theories assume spacetime is a **continuous manifold** — a smooth, infinitely divisible fabric. You can always zoom in further. There's always a halfway point between any two points. This assumption is the foundation of everything both theories say.

**PCTRM** — the Planck Cell-Tick Remainder Momentum model — proposes that this assumption is wrong. Spacetime is not continuous. It's discrete, like the pixels on a screen or the cells in a spreadsheet. At the smallest possible scale (the Planck scale, roughly 10⁻³⁵ meters), there are individual "cells" of space and individual "ticks" of time, and everything that happens is the result of simple arithmetic on those cells and ticks.

This paper explains what that means and what it buys you.

---

## The Setup: Cells, Ticks, and Neighbors

Imagine the universe as an enormous three-dimensional grid. Each little box in the grid is a "cell" — the smallest possible chunk of space. Time advances in "ticks" — the smallest possible duration. Between ticks, nothing happens. At each tick, the whole universe updates.

So far, this sounds like a lot of previous "discrete universe" ideas — digital physics, cellular automata, Wolfram's hypergraph programs. These all hit the same wall: a cubic grid has **preferred directions**. If you try to move along a diagonal, you have to take a zig-zag staircase through the cells, which is slower than moving along an axis. Light would travel faster horizontally than diagonally. But light doesn't do that in reality — it goes the same speed in every direction.

PCTRM solves this with a clever move:

**Position is discrete. Direction is continuous.**

In PCTRM's grid, each cell has a neighbor at a distance of exactly one Planck-length in **any direction** you point. Not just north, south, east, west, up, down — but any continuous direction on the sphere of possibilities. Which cell counts as your "next" cell depends on which way you're heading. This is called **direction-conditional adjacency**.

![Fig. 1: Cubic lattice vs direction-conditional adjacency](../figures/pctrm_01_direction_conditional_adjacency.png)

On the left: a standard grid. Neighbors are locked to axes. Diagonal motion requires a staircase. This produces preferred directions and breaks Lorentz invariance — the universe would have anisotropy baked in.

On the right: direction-conditional adjacency. Every neighbor is at exactly unit distance. Direction is continuous. There are no preferred axes. Light can travel in any direction at the same speed. Isotropy is built into the topology rather than imposed on it.

This one move is the most consequential technical choice in the whole framework. Everything else follows from it.

---

## How Light Moves, and Why It's Always the Same Speed

In PCTRM, a photon advances exactly one cell per tick. That's what the speed of light *is* — one cell per tick. Not 299,792,458 meters per second with some additional significance; that number is just the conversion into human units.

Because the speed is defined this way, something subtle happens with Einstein's question about why every observer measures the same speed of light regardless of how fast they're moving.

Imagine a photon is emitted at cell A and absorbed at cell B. There are exactly N cells between them. The photon takes exactly N ticks to get there. Any observer, no matter how they're moving, who counts the cells traversed and the ticks elapsed, gets N divided by N, which equals 1. One cell per tick. Same for everyone.

![Fig. 2: Photon propagation N/N = 1 arithmetic](../figures/pctrm_02_photon_nn_arithmetic.png)

This is a big deal because in standard physics, the constancy of the speed of light is a **postulate** — something we assume and then derive consequences from. In PCTRM, it's an **arithmetic identity**. N divided by N is 1. You can't argue with that. It's not a physical law that could have been otherwise; it's just counting.

This is what physicists mean when they talk about something being "derived from first principles." Standard physics postulates c is constant. PCTRM shows why it has to be.

(There's a caveat: this argument works cleanly for photons, which travel at c. For observers themselves moving at different speeds — time dilation — the argument is harder and isn't fully worked out yet. The paper acknowledges this as remaining work.)

---

## The Universe Is Made of Patterns Within Patterns

PCTRM organizes reality into a hierarchy. Everything is a "soliton" — a stable, self-sustaining pattern of cells, ticks, and interactions. The word "soliton" is borrowed from wave physics, where it means a wave that holds its shape as it travels. In PCTRM, a soliton is any pattern that persists.

Electrons are solitons. So are protons. So are atoms, molecules, planets, stars, galaxies — and the entire observable universe. The universe is the biggest soliton, and all the smaller solitons live inside it.

![Fig. 3: Six-level soliton hierarchy across 62 orders of magnitude](../figures/pctrm_03_hierarchy_levels_scale.png)

The vertical axis here spans 62 orders of magnitude — from Planck cells (10⁻³⁵ meters) to the observable universe (10²⁷ meters). The same vocabulary (soliton, cell, tick, channel, remainder) applies at every level. A proton and a galaxy obey the same substrate rules, just at wildly different scales.

There's one more twist: the hierarchy closes on itself. The inner boundary of the universal soliton — what we observe as the cosmic microwave background, the oldest light in the universe — **is** the substrate from which new particles emerge at the smallest scale. Look outward far enough and you're looking at the same thing you'd see if you could look inward far enough. The hierarchy is a loop, not a ladder.

This is a strange claim and it's not proven. But it has a consequence: the universe being "flat" (the three density parameters summing to exactly 1) isn't a coincidence requiring fine-tuning. You're always inside the universal soliton, so the total is always 1 by construction.

---

## Every Pattern Has Two Shapes: Sphere and Donut

One of PCTRM's central claims is that **every soliton, at every scale, has two geometric components**:

- A **spherical** component (the framework calls this the "modulus")
- A **toroidal** component (the framework calls this the "remainder") — "toroidal" means donut-shaped

This isn't metaphorical. The paper claims these two components are structurally real at every scale, and which one you see depends on what you're probing with.

![Fig. 4: Dual-geometry structure at four different scales](../figures/pctrm_04_dual_geometry_scales.png)

Look at a proton: it has a roughly spherical confinement boundary (the outer "shell" of what counts as the proton) and inside it, a donut-shaped structure made of gluon flux tubes, which carry about 99% of the proton's mass.

Look at an atom: it has roughly spherical electron shells and a donut-shaped magnetic-moment structure.

Look at Earth: roughly spherical atmospheric layers, and the donut-shaped Van Allen radiation belts.

Look at a galaxy: a roughly spherical dark-matter halo, and a donut-shaped disk.

The paper's claim is that this isn't coincidence — it's a universal structural decomposition. Every soliton has both a spherical sector and a toroidal sector because both are forced by the substrate's geometry.

Different probes see different sectors. A long-wavelength probe sees the spherical sector. A short-wavelength, high-energy probe sees the toroidal sector. In quantum electrodynamics at the four-loop level of precision, this crossover happens around 22 MeV of energy — muons probe the toroidal content that electrons don't reach, because muons are about 207 times heavier.

This is actually testable. The framework pre-registers specific predictions about what tau-lepton measurements should show when precision improves enough. If the predictions fail, this piece of the framework fails.

---

## Why Bell Correlations Aren't Spooky

Here's where PCTRM does something interesting. In 1935, Einstein, Podolsky, and Rosen pointed out that quantum mechanics seems to allow "spooky action at a distance" — two particles separated by any amount of space seem to coordinate their behavior instantaneously when either is measured. Einstein thought this was so bizarre it must mean quantum mechanics was incomplete.

In 1964, John Bell proved that this spooky coordination is real — no theory with only local, hidden variables can reproduce quantum predictions. Experiments since then (Aspect in 1982, Hensen in 2015, and many others) have confirmed the coordination is real. It happens faster than light could travel between the particles.

This has been a puzzle for ninety years. How do two things separated by a meter, a kilometer, a light-year, instantly coordinate?

PCTRM's answer: **they aren't separated**.

![Fig. 5: Euclidean view vs graph view of entangled particles](../figures/pctrm_05_channel_sharing_vs_euclidean.png)

On the left: the standard picture. Two particles, far apart, and some mysterious influence has to cross the intermediate space. Bell proved nothing local can do it. So the effect is "spooky."

On the right: PCTRM's picture. The two particles share channel substrate — they are **one pattern with two Euclidean handles**, not two separate objects. At the graph level, they're neighbors. Graph-distance 1. The "distance" between them that makes the coordination look spooky is a projection artifact of how the graph folds into 3D observational space.

In other words: the manifold — the smooth continuous space we observe — is emergent. It's what you get when you average over many graph updates. The graph itself doesn't know about "distance" in the Euclidean sense. Two cells that look far apart in our projected view can be graph-neighbors if a channel connects them directly.

Bell's theorem forbids local hidden variables **given a manifold as the background**. PCTRM dissolves the theorem not by adding hidden variables, but by denying the manifold is fundamental. The apparent non-locality is a projection artifact.

You lose nothing in this picture — no-signaling still holds (you can't send bits faster than light because the merged pattern isn't a communication channel in the sender/receiver sense), all the experimental confirmations still work. What you gain is an explanation for *why* correlation persists across arbitrary distance: because "distance" isn't what the correlation is traversing.

---

## The Born Rule Isn't Weird Anymore

In quantum mechanics, when you measure a particle, you get an outcome with some probability. The rule for calculating that probability is called the Born rule: the probability is the squared magnitude of something called the "amplitude."

Why squared? Why not linear, or cubed, or something else? Standard quantum mechanics doesn't say. The Born rule is postulated — you accept it and move on. Attempts to derive it within standard QM either fail or require additional assumptions.

PCTRM claims to derive it.

![Fig. 6: Born rule from unit-graph round-trip closure](../figures/pctrm_06_born_rule_unity.png)

Here's the argument in plain terms:

**1. The substrate only has unit distances.** Every adjacency is exactly one Planck-length. There is no half-cell, no 2.3 cells. Direction states — the "which way is this pattern pointing" information — automatically live on unit spheres because unit is the only distance that exists.

**2. Probabilities have to sum to 1.** Across a complete set of possible outcomes, the probabilities of all the outcomes have to add up to exactly 1. Not 0.98, not 1.02 — exactly 1. This is what it means to have a complete set of outcomes: one of them is what actually happens.

**3. Only squared magnitude gives automatic unity.** When you take a state (a unit vector) and a complete set of basis vectors (also unit vectors) and compute the probabilities, only the squared-magnitude rule |⟨α|ψ⟩|² automatically sums to 1 without additional renormalization. Linear amplitudes don't (they can be negative or complex). Fourth powers don't (the sum depends on which state you're in). Other powers don't either.

**4. In a discrete integer-fraction universe, you can't renormalize.** The standard physics trick of "fix it up afterwards by dividing by the sum" relies on continuous real numbers. Integer fractions with explicit moduli can't do this — there are no infinities to absorb, and no continuous renormalization to perform.

So the exponent 2 is *forced* by the structure. The Born rule stops being a postulate and becomes a theorem about what works on a unit-adjacency graph with integer arithmetic.

This is a genuine simplification. Ninety years of wondering "why squared?" resolves to "because unity is automatic when the exponent is 2, and nothing else works."

---

## Why There Are No Infinities

Standard quantum field theory — the mathematical framework behind the Standard Model of particle physics — has a well-known problem: lots of its calculations produce infinities.

When you calculate how particles interact, you have to add up contributions from all possible intermediate states. In continuous spacetime, those intermediate states have momentum that can take any value up to infinity. The sum diverges.

Physicists handle this with a procedure called **renormalization**: impose a cutoff, absorb the infinite parts into redefinitions of the constants of the theory, and keep only the finite physical predictions. It works brilliantly — QED is the most precisely tested theory in science — but it's ugly. Dirac called renormalization "a disgusting procedure." Feynman called it "a shell game." Everyone uses it because nothing else works, but it feels like cheating.

PCTRM doesn't have this problem because **integer arithmetic can't diverge**.

![Fig. 7: Continuum QFT divergences vs discrete substrate finite sums](../figures/pctrm_07_renormalization_unnecessary.png)

On the left: the standard QFT integral, running over continuous momentum up to infinity. Diverges. Requires a cutoff Λ imposed by hand. The divergent part gets absorbed into counterterms.

On the right: the PCTRM substrate sum, running over a finite graph. The maximum momentum is the Planck momentum (one cell per tick). There's no infinity because the graph is finite. Individual contributions from individual cells add up to a finite total.

This has several consequences that clean up long-standing problems:

- **The hierarchy problem dissolves.** In standard QFT, why is the Higgs boson so much lighter than the Planck scale when quantum corrections should pull it toward Planck? In PCTRM, there's no runaway correction because there's no infinite integral to run.

- **The cosmological constant problem dissolves.** Standard QFT predicts a vacuum energy 10¹²⁰ times larger than observed. In PCTRM, the vacuum energy is just the substrate's maintenance cost, which is a specific finite fraction (the framework claims this is (251−22π)/264 of total density, which matches the measured value to 85 parts per million).

- **The Landau pole dissolves.** Standard QED's coupling diverges at finite energy, indicating QED must be replaced above some scale. In PCTRM, couplings are channel counts, which are bounded above by total channel availability.

Renormalization is the price of assuming continuous spacetime. Discrete arithmetic doesn't pay that price.

---

## Measurement Isn't a Separate Thing

Quantum mechanics has a famously uncomfortable structural feature: it has **two** dynamics.

Between measurements, states evolve smoothly according to the Schrödinger equation — unitary evolution, deterministic, reversible. At the moment of measurement, states "collapse" into a specific outcome — non-unitary, probabilistic, irreversible. The collapse rule is not derivable from the evolution rule. They're two different kinds of dynamics glued together.

This raises an unanswerable question: **when does measurement happen?**

Standard QM doesn't say. The formalism has a "Heisenberg cut" between the quantum system being measured and the classical apparatus doing the measuring, but it doesn't tell you where to draw the cut. Wigner pushed it toward consciousness. Von Neumann showed the cut could be pushed arbitrarily far. Copenhagen declared the cut primitive. Many-worlds denied collapse by multiplying universes. Bohmian mechanics added hidden particle positions. Each interpretation picks a different answer and none can prove it's right.

PCTRM's approach: **there's only one dynamics**. Measurement is not a separate event.

![Fig. 8: Observation-as-entanglement — three-panel merger sequence](../figures/pctrm_08_observation_as_entanglement.png)

Here's what happens in PCTRM when you "measure" something:

**Panel 1.** The target is in a superposition — multiple candidate paths, channels agreeing across alternatives. Standard quantum superposition.

**Panel 2.** An observer enters the scene. The observer is just another soliton — no special status. It has channels that can merge with the target's channels. The merger begins to compete with the existing channel-agreement among alternatives.

**Panel 3.** The observer's merger wins. The prior multi-path agreement is displaced. A single outcome is recorded — not because something "collapsed," but because one channel-merger now dominates. The observer and target are now sharing channel substrate.

There's no second dynamics. There's only channel-merger competition. What we've been calling "measurement" is the pattern in which environmental mergers (observers, detectors, thermometers, photographic plates) outcompete isolated quantum coherence.

**This is the most important conceptual result in the framework.** The observer isn't a privileged category. Any soliton can participate in a merger. "Observers" are just solitons whose internal structure is complex enough that their mergers propagate into many further mergers, producing what we call "records." A thermometer, a human, an electron detector — all are doing the same thing physically.

This dissolves the measurement problem. The Copenhagen-vs-many-worlds-vs-Bohmian debates were about how to reconcile two dynamics. PCTRM has one dynamics. The debates become moot.

It also dissolves wave-particle duality. The particle "is" neither a wave nor a particle — it's a channel structure that produces wave-pattern outcomes when its agreement resolves over multiple paths (no observer) and particle-pattern outcomes when an observer participates in the agreement pool (single path selected). Same substrate dynamics, different configuration.

---

## What This Framework Is Claiming

To summarize the substrate specification in plain terms:

**1. Spacetime is discrete.** There are Planck cells and Planck ticks. Between ticks nothing happens; at each tick the whole universe updates.

**2. Adjacency is direction-conditional.** Each cell has neighbors at unit distance in any direction. Position is discrete; direction is continuous.

**3. Everything is a soliton.** Electrons, atoms, planets, galaxies, the universe — stable patterns in cell-tick arithmetic, organized as a hierarchy that closes on itself.

**4. Every soliton has two sectors.** Spherical (modulus) and toroidal (remainder). Different probes see different sectors.

**5. Interactions are channels.** Gravity, electromagnetism, the strong force, the weak force, and entanglement are all types of channels connecting solitons.

**6. Mass is the cost of existence.** Massive particles spend remainder maintaining their pattern against the vacuum. Photons are massless because they pay no tax.

**7. The speed of light is one cell per tick.** Its frame-independence follows from N/N = 1.

**8. Channels can connect distant cells directly.** Entangled particles share substrate — they are graph-neighbors regardless of Euclidean separation. Bell non-locality dissolves.

**9. The Born rule is forced by unity.** Only the exponent 2 gives automatic probability summation on a unit-adjacency graph.

**10. Renormalization is unnecessary.** Integer arithmetic doesn't produce infinities.

**11. Measurement is channel-merger, not collapse.** One dynamics, not two. The measurement problem dissolves.

**12. The Standard Model is a consequence.** Particle masses, coupling constants, gauge groups, CKM elements — all should emerge from substrate arithmetic. This is mostly still execution-pending.

**13. General relativity is a consequence.** 1/r² gravity from channels spreading on spherical surfaces; GR corrections from toroidal content at probe-scale resolution. Also execution-pending.

---

## What Hasn't Been Proved Yet

This framework makes strong claims and the paper is honest about what has been tested and what hasn't.

**What has been tested:**
- The basic vocabulary is internally consistent (Round 0, passed)
- Four independent cosmological predictions match measurement at their published precision
- The speed-of-light invariance for photons is an arithmetic identity
- Some QED four-loop calculations produce specific elliptic-function structures to parts-per-billion precision

**What's still pending:**
- Deriving particle masses from first principles
- Deriving 1/r² gravity from channel geometry
- Reproducing general relativity's corrections (Mercury precession, light bending, gravitational waves)
- Deriving Bell correlations quantitatively from channel-merger arithmetic
- Deriving the fine structure constant (137.036) from channel counting
- Observer time dilation (as opposed to photon invariance)

The framework's organizers have committed to a sequence of ten specific tests with pre-registered precision thresholds. If the tests pass, the substrate picture is validated. If they fail, the specific mechanisms are falsified. No fudging, no patching, no moving the goalposts.

This is what makes PCTRM unusual: it's **a speculative theory that has committed to conditions for its own falsification**. Most alternative-to-mainstream physics frameworks don't do this. PCTRM does.

---

## Why This Might Matter

If PCTRM is right, it changes the picture of physics in specific ways:

1. **The foundations of quantum mechanics get an explanation.** Why unit-sphere state spaces, why the Born rule, why measurement, why entanglement — these stop being postulates and become consequences of discrete graph structure.

2. **The infinities of quantum field theory go away.** Renormalization stops being necessary. The hierarchy problem and cosmological constant problem dissolve.

3. **Gravity and quantum mechanics operate on the same substrate.** Two theories that have resisted unification for a century are both expressed as channel arithmetic on the same graph.

4. **The "interpretation of quantum mechanics" question dissolves.** The question only existed because standard QM has two dynamics. PCTRM has one.

5. **Specific cross-domain predictions become possible.** The framework claims the same integer alphabet that produces cosmological parameters also produces particle-physics parameters — one substrate, not two frameworks for different scales.

If PCTRM is wrong, most of these benefits evaporate, but the program has been specific enough about what would falsify it that the failure itself would be informative. You'd know exactly which pieces of the substrate picture fail at which levels.

---

## What To Take Away

PCTRM is an attempt to replace the continuous manifold assumption at the base of modern physics with a discrete substrate — Planck cells updated at Planck ticks via integer arithmetic on channels connecting solitons. The direction-conditional adjacency is the technical move that makes it possible to be both discrete and isotropic. Everything else follows from that plus channel-mediated adjacency extension.

Whether it's right is an empirical question that will be settled by specific computational tests running over the next few years. Whether it's *interesting* is not — it's one of the very few frameworks that tries to derive the foundational features of quantum mechanics (Born rule, entanglement, measurement) from structural principles rather than postulate them, and that tries to do so in a way compatible with Standard Model phenomenology at measurement precision.

Most of what's new in PCTRM lives in the ontology, not in new predictions about new particles or new forces. The framework says: the Standard Model predictions are all correct, and here is the substrate that produces them.

If you want to check on the framework's progress: the tests that will validate or falsify it are listed explicitly, with specific precision thresholds, in the Round 1 program specification. Those results will come out in subsequent papers with real data. This paper explained what the framework *says is going on*. The next papers will show whether the saying holds up.

---

*End of pctrm_substrate_plain_language.md. This document accompanies figures produced by the PCTRM substrate diagram script. Intended for readers who want to understand what the framework claims at the level of structural commitments rather than mathematical formalism.*
