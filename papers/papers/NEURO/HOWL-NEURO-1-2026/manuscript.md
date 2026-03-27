# Elimination of Classical Carriers for Sub-Millisecond Motor Coordination

## An Engineering Analysis of Timing Requirements Across Human and Animal Motor Tasks

**Registry:** [@HOWL-NEURO-1-2026]

**DOI:** 10.5281/zenodo.18655527

**Date:** March 27 2026

**Domain:** Applied Philosophy

**Status:** Working Methodology

**AI Usage Disclosure:** Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Opus 4.6. 

---

## Section 1 — The Baseball Fan

A foul ball comes off the bat and arcs into the stands. It reaches the spectators in roughly two seconds. Every person in the flight path does the same thing. They flinch. Their shoulders come up. Their hands fly toward their face. They duck. They grab at the air. They spill their drink on themselves and hit the person beside them. Forty thousand people in the stadium, and the six in the ball's path all look like they've never used their own arms before.

Except one. A man two seats over reaches up with one hand, tracks the ball into his palm, and catches it clean. He sits back down. His drink is intact. The crowd cheers. He looks like a different species from the people around him.

He played outfield in college. They didn't.

But here is the strange part. If you watch the replay in slow motion, the outfielder flinched too. His shoulders came up. His head ducked. For the first 80 milliseconds, his body did exactly what everyone else's body did — a fast, whole-body protective brace. Then his response diverged. His hands redirected from his face toward the ball. His arm extended along the interception trajectory. His grip opened, timed itself to the ball's arrival, and closed. In 200 milliseconds he went from flinching to catching.

Two questions arise from this observation.

First: why is the flinch so fast? Everyone's hands are up within 100 milliseconds. That is faster than conscious decision-making. Faster than visual object identification. Faster than any deliberate motor plan. Something activated the entire body simultaneously, before the brain had finished determining what the object was.

Second: why is the flinch so bad? The reaction is fast and synchronized — every muscle group activates at once — but the activation is purposeless. The arms go up but not toward the ball. The hands close but on empty air. The body is coordinated in timing but uncoordinated in purpose.

Fast but purposeless. Synchronized but undirected. That is the signature of a system that has a timing channel and a content channel, and the timing channel fired before the content channel had anything to say.

This paper will demonstrate what those two channels are, why both are necessary, and why the timing channel must operate through a physical mechanism that neuroscience has not yet characterized as a coordination pathway.

---

## Section 2 — The Engineering Problem

Set aside biology. Consider the problem as pure engineering.

A control system must coordinate actuators distributed across a flexible structure 1.8 meters long. The structure is mechanically unstable — it is an inverted pendulum balanced on a small base, with multiple mass centers stacked vertically, each one capable of independent displacement. The actuators are muscles. The sensors are proprioceptors. The communication medium is biological tissue — conductive, wet, warm, and electromagnetically noisy.

The actuators must fire in coordinated patterns to maintain the structure's balance. The coordination must be precise: if the ankle actuators fire 5 milliseconds before the hip actuators during a perturbation correction, the correction produces a torque that makes the instability worse rather than better. The actuators don't just need to fire — they need to fire together, within a timing window tight enough that their combined effect is constructive rather than destructive.

The question is: what timing window does the system actually require, and what communication speed does that timing window demand?

### The control theory constraint

For a feedback control loop to track a periodic disturbance of frequency f_c, the total open-loop delay τ must satisfy:

τ ≤ 1 / (2π × f_c × β)

where β is the stability margin, typically 10 for robust control systems that must operate under uncertainty (Ogata, Modern Control Engineering).

This means the entire round trip — sense the disturbance, transmit the information to the controller, compute the correction, transmit the command to the actuator, and execute the correction — must complete within τ.

The correction frequency f_c is determined by the mechanical dynamics of the structure. A tall, narrow, top-heavy inverted pendulum on a small base requires higher correction frequencies than a short, wide, bottom-heavy structure on a broad base. The correction frequency is not a choice — it is dictated by the physics of the structure.

For a standardized human of 1.8 meters standing height, the relevant frequencies will be derived activity by activity in Section 5.

### The minimum speed inequality

For any communication mechanism carrying coordination signals between two actuators separated by distance d, the one-way transit time is:

t_transit = d / v

where v is the propagation speed of the mechanism in biological tissue.

The round-trip time, including any transduction delays required to convert between physical domains, is:

t_round = 2 × t_transit + n × t_transduction

where n is the number of domain-crossing events (e.g., mechanical to electrical, electrical to chemical) and t_transduction is the delay per crossing.

For the round-trip time to satisfy the control theory constraint:

t_round ≤ 1 / (2π × f_c × β)

This is the inequality that every candidate communication mechanism must satisfy. It is pure arithmetic: distance, speed, transduction cost, and the physics of the structure determine whether a mechanism can work. No statistical analysis is required. No p-values. No sample size debates. The mechanism either satisfies the inequality or it does not.

---

## Section 3 — Carrier Enumeration

Every known physical mechanism that could carry a coordination signal through biological tissue is enumerated below with its measured propagation speed. For each mechanism, the one-way transit time is computed over two standardized distances: 10 cm (the approximate body length of a laboratory mouse in bipedal reach posture) and 100 cm (the approximate ankle-to-neck distance in a 1.8-meter human).

### 3.1 Myelinated axon conduction

The fastest neural signaling pathway. Action potentials propagate along myelinated axons via saltatory conduction, jumping between nodes of Ranvier.

Measured speed: 80-120 m/s. We use the upper bound of 120 m/s throughout this paper.

One-way transit, 10 cm: 0.83 ms
One-way transit, 100 cm: 8.3 ms

Minimum synaptic relay: any signal that must cross from one neuron to another requires at least one synaptic transmission. A minimal reflex arc requires three neurons (sensory, interneuron, motor) and therefore two synaptic relays. A more realistic coordination pathway from sensor to spinal cord to motor neuron involves a minimum of three synaptic relays.

Synaptic delay: 0.5 ms per synapse (Kandel, Principles of Neural Science).

Minimum round-trip at 100 cm with 3 synaptic relays: 2 × 8.3 + 3 × 0.5 = 18.1 ms
Minimum round-trip at 10 cm with 3 synaptic relays: 2 × 0.83 + 3 × 0.5 = 3.2 ms

Source: Kandel, Principles of Neural Science, 6th edition. Conduction velocities for Aα fibers.

### 3.2 Unmyelinated C fiber conduction

Slow pain and temperature fibers. Included for completeness.

Measured speed: 0.5-2 m/s.

One-way transit, 100 cm at 2 m/s: 500 ms
Round-trip at 100 cm: > 1,000 ms

Eliminated at every frequency relevant to motor coordination. Not considered further.

### 3.3 Gap junction electrical coupling

Direct electrical coupling between neurons through gap junction channels (connexins). Eliminates synaptic delay at each junction but propagation is still limited by membrane time constants.

Measured effective speed: ≤ 120 m/s. Gap junctions reduce per-hop delay but do not exceed the propagation speed of myelinated axons. They also require direct cytoplasmic continuity between cells, which limits their range to cells in physical contact.

One-way transit, 100 cm: 8.3 ms
Minimum round-trip at 100 cm with reduced synaptic cost (1 relay instead of 3): 2 × 8.3 + 1 × 0.5 = 17.1 ms
Minimum round-trip at 10 cm: 2 × 0.83 + 1 × 0.5 = 2.2 ms

These estimates are generous. Gap junction chains spanning 100 cm of continuous cytoplasmic coupling do not exist in the mammalian motor system. The actual effective round-trip would be longer because the chain must cross non-gap-junction boundaries at some points.

### 3.4 Bone conduction (acoustic wave)

Mechanical compression waves propagating through cortical bone.

Measured speed: ~1,500 m/s (standard acoustic physics of cortical bone).

One-way transit, 100 cm: 0.67 ms
One-way transit, 10 cm: 0.067 ms

However, bone conduction carries mechanical energy, not neural commands. To drive muscle contraction, the mechanical signal must be transduced back into the neural domain. This requires at minimum:

Event 1: neural command generates muscle contraction (already in neural domain)
Event 2: muscle contraction generates mechanical wave in bone
Event 3: mechanical wave propagates through bone (fast)
Event 4: mechanical wave arrives at distant site
Event 5: mechanoreceptor transduces mechanical signal to neural signal
Event 6: neural signal drives corrective muscle contraction

The minimum transduction cost is two domain crossings (neural→mechanical, mechanical→neural) at 0.5 ms each = 1.0 ms.

Effective round-trip at 100 cm: 2 × 0.67 + 2 × 0.5 = 2.3 ms
Effective round-trip at 10 cm: 2 × 0.067 + 2 × 0.5 = 1.1 ms

Note: these estimates are generous. They assume only two transduction events. A more realistic pathway involves additional neural processing between the mechanoreceptor and the motor command, adding further synaptic delays.

### 3.5 Hydraulic pressure wave

Pressure waves propagating through interstitial fluid and blood.

Measured speed: ~1,500 m/s (acoustic speed in water/soft tissue).

Same transduction bottleneck as bone conduction. The signal propagates fast but must be transduced back to the neural domain.

Effective round-trip at 100 cm: 2.3 ms (same as bone conduction)
Effective round-trip at 10 cm: 1.1 ms (same as bone conduction)

### 3.6 Fascial mechanotransduction

Tension waves propagating through the fascial network — the continuous web of connective tissue that links muscles, bones, and organs.

Measured speed: 10-30 m/s (Schleip, Fascia: The Tensional Network of the Human Body). We use the upper bound of 30 m/s.

One-way transit, 100 cm: 33.3 ms
One-way transit, 10 cm: 3.3 ms

Plus transduction delays (same mechanical-to-neural cost): 1.0 ms minimum.

Effective round-trip at 100 cm: 2 × 33.3 + 2 × 0.5 = 67.6 ms
Effective round-trip at 10 cm: 2 × 3.3 + 2 × 0.5 = 7.6 ms

### 3.7 Piezoelectric signaling in collagen

Collagen fibers exhibit piezoelectric properties — mechanical stress generates electrical potential. This could theoretically carry information.

Measured propagation speed: poorly characterized. Estimated at 30-100 m/s based on mechanical wave speeds in connective tissue. We use the upper bound of 100 m/s.

One-way transit, 100 cm: 10 ms
One-way transit, 10 cm: 1.0 ms

Plus transduction delays: 1.0 ms minimum.

Effective round-trip at 100 cm: 2 × 10 + 2 × 0.5 = 21 ms
Effective round-trip at 10 cm: 2 × 1.0 + 2 × 0.5 = 3.0 ms

Note: this mechanism is the least well-characterized in the enumeration. The estimated speed has no single authoritative source and is stated honestly as an estimate.

### 3.8 Chemical and ion diffusion

Neurotransmitter release, calcium waves, ion cloud propagation.

Diffusion coefficient: ~1 µm²/ms (standard physical chemistry).

Time to traverse 100 cm by diffusion: approximately 10¹⁰ ms (about 300 years).
Time to traverse 10 cm by diffusion: approximately 10⁸ ms (about 3 years).

Eliminated at every frequency. Not considered further.

### 3.9 Electromagnetic field propagation

Maxwell's transverse electromagnetic field propagating through biological tissue.

Phase velocity in soft tissue: c/n where n is the refractive index of the tissue. For soft tissue at low frequencies, permittivity values from the Gabriel 1996 dataset (FCC tissue permittivity database) give an effective propagation speed of approximately 0.7c ≈ 2.1 × 10⁸ m/s.

One-way transit, 100 cm: 4.8 × 10⁻⁶ ms (4.8 nanoseconds)
One-way transit, 10 cm: 4.8 × 10⁻⁷ ms (0.48 nanoseconds)

No transduction delay. The electromagnetic field is generated by neural and muscular electrical activity and can directly influence membrane potential in distant neurons and muscle cells without requiring synaptic transmission or domain crossing. The field is the signal.

Effective round-trip at 100 cm: ~0.00001 ms
Effective round-trip at 10 cm: ~0.000001 ms

Effectively instantaneous at all biological timescales.

Source: Maxwell's equations applied with tissue permittivity from Gabriel, S., Lau, R.W., & Gabriel, C. (1996). The dielectric properties of biological tissues. Physics in Medicine and Biology, 41(11), 2231-2249.

### 3.10 Summary table — measured speeds

| Carrier | Speed (m/s) | 100 cm one-way | 10 cm one-way | 100 cm round-trip | 10 cm round-trip |
|---|---|---|---|---|---|
| Myelinated axon | 120 | 8.3 ms | 0.83 ms | 18.1 ms | 3.2 ms |
| Gap junction chain | ≤120 | 8.3 ms | 0.83 ms | 17.1 ms | 2.2 ms |
| Bone conduction | 1,500 | 0.67 ms | 0.067 ms | 2.3 ms | 1.1 ms |
| Hydraulic wave | 1,500 | 0.67 ms | 0.067 ms | 2.3 ms | 1.1 ms |
| Fascial | 30 | 33.3 ms | 3.3 ms | 67.6 ms | 7.6 ms |
| Piezoelectric | 100 | 10 ms | 1.0 ms | 21 ms | 3.0 ms |
| EMF | 2.1 × 10⁸ | 0.0000048 ms | 0.00000048 ms | ~0 ms | ~0 ms |

All round-trip times include minimum transduction delays where the mechanism requires domain crossing.

---

## Section 4 — The Generous Table

The measured values in Section 3 represent current scientific knowledge. It is possible that undiscovered biological enhancements exist that would increase the effective speed of one or more classical carriers. To prevent the analysis from being dismissed on the grounds of incomplete knowledge, we now present generous and extremely generous estimates for each carrier.

These generous estimates have no empirical basis. They represent hypothetical biological tricks — undiscovered myelination enhancements, faster transduction, shortcut pathways — that we grant for the sake of argument. If the conclusion holds even under these generous assumptions, it holds regardless of what future research discovers about classical carrier speeds.

### 4.1 Generosity factors

For propagation speed: 2x generous, 4x extremely generous.
For transduction delay: reduced from 0.5 ms to 0.25 ms per event at generous, and to 0.1 ms at extremely generous.

No known biological mechanism justifies any of these enhancements. They are granted purely to stress-test the conclusion.

### 4.2 Generous round-trip table — human (100 cm)

| Carrier | Measured RT | 2x Generous RT | 4x Extreme RT |
|---|---|---|---|
| Myelinated axon | 18.1 ms | 9.8 ms | 5.6 ms |
| Gap junction chain | 17.1 ms | 9.1 ms | 5.0 ms |
| Bone conduction | 2.3 ms | 1.2 ms | 0.53 ms |
| Hydraulic wave | 2.3 ms | 1.2 ms | 0.53 ms |
| Fascial | 67.6 ms | 34.1 ms | 17.3 ms |
| Piezoelectric | 21 ms | 10.8 ms | 5.5 ms |
| EMF | ~0 ms | ~0 ms | ~0 ms |

### 4.3 Generous round-trip table — mouse (10 cm)

| Carrier | Measured RT | 2x Generous RT | 4x Extreme RT |
|---|---|---|---|
| Myelinated axon | 3.2 ms | 1.6 ms | 0.72 ms |
| Gap junction chain | 2.2 ms | 1.1 ms | 0.52 ms |
| Bone conduction | 1.1 ms | 0.57 ms | 0.27 ms |
| Hydraulic wave | 1.1 ms | 0.57 ms | 0.27 ms |
| Fascial | 7.6 ms | 3.9 ms | 2.0 ms |
| Piezoelectric | 3.0 ms | 1.5 ms | 0.72 ms |
| EMF | ~0 ms | ~0 ms | ~0 ms |

### 4.4 Maximum correction frequency supported by each carrier

Using the control theory formula: max f_c = 1 / (2π × τ × β) with β = 10.

**Human (100 cm distance):**

| Carrier | Measured max Hz | 2x Generous max Hz | 4x Extreme max Hz |
|---|---|---|---|
| Myelinated axon | 0.9 Hz | 1.6 Hz | 2.8 Hz |
| Gap junction chain | 0.9 Hz | 1.8 Hz | 3.2 Hz |
| Bone conduction | 6.9 Hz | 13.3 Hz | 30.1 Hz |
| Hydraulic wave | 6.9 Hz | 13.3 Hz | 30.1 Hz |
| Fascial | 0.2 Hz | 0.5 Hz | 0.9 Hz |
| Piezoelectric | 0.8 Hz | 1.5 Hz | 2.9 Hz |
| EMF | >1,000,000 Hz | >1,000,000 Hz | >1,000,000 Hz |

**Mouse (10 cm distance):**

| Carrier | Measured max Hz | 2x Generous max Hz | 4x Extreme max Hz |
|---|---|---|---|
| Myelinated axon | 5.0 Hz | 10.0 Hz | 22.1 Hz |
| Gap junction chain | 7.2 Hz | 14.5 Hz | 30.7 Hz |
| Bone conduction | 14.5 Hz | 28.0 Hz | 59.1 Hz |
| Hydraulic wave | 14.5 Hz | 28.0 Hz | 59.1 Hz |
| Fascial | 2.1 Hz | 4.1 Hz | 8.0 Hz |
| Piezoelectric | 5.3 Hz | 10.6 Hz | 22.1 Hz |
| EMF | >1,000,000 Hz | >1,000,000 Hz | >1,000,000 Hz |

### 4.5 Reading the table

For humans at measured carrier speeds, the absolute classical ceiling is bone conduction and hydraulic waves at 6.9 Hz. Nothing classical supports coordination above 7 Hz over a 100 cm distance. Even at 4x extreme generosity — granting every classical carrier a quadrupled speed and halved transduction delay that nobody has ever measured — the ceiling rises to only 30 Hz.

For mice, the shorter distance is more forgiving. At measured speeds the ceiling is 14.5 Hz. At 4x extreme generosity, bone conduction and hydraulic waves reach 59 Hz. This is the highest frequency any classical carrier can theoretically support under the most generous possible assumptions, over the shortest distance in the analysis.

The question that follows is: do human and mouse motor activities actually require correction frequencies above these ceilings?

---

## Section 5 — The Activity Demand Matrix

For each motor activity, we estimate the minimum correction frequency required for the coordination to succeed. These estimates are deliberately conservative — we use the low end of what the physics demands, not the high end. If the conservative estimate already exceeds the classical carrier ceiling, the actual requirement only makes the gap wider.

The estimates are derived from the mechanical time constants of each activity — the time available for a correction before the error grows beyond recovery. A system balancing on a wide base with low center of mass has a long time constant and needs slow corrections. A system balancing on a point with high center of mass has a short time constant and needs fast corrections. The physics determines the requirement.

### 5.1 Human activities (1.8 m tall, 100 cm coordination distance)

**Quiet stance on flat ground, both feet.** Wide base of support. Low center of mass relative to base width. Skeletal stacking through calcaneus provides passive stability — the skeleton can briefly hold the body upright without muscular correction. Postural sway frequency measured at 0.5-3 Hz with correction responses at 6-12 Hz. This is the least demanding balance task humans perform.
Estimated minimum correction frequency: 6-12 Hz.
At measured classical ceiling (6.9 Hz): MARGINAL. At 2x generous (13.3 Hz): PASS. At 4x extreme (30.1 Hz): PASS.

**Walking, single-limb stance phase.** During each stride, body weight transfers to a single foot for approximately 400 ms. Base of support narrows to one foot. Center of mass moves forward at 1.2 m/s and laterally with each weight transfer. No passive skeletal resting during the transition between double support and single support. Ankle, hip, and trunk must coordinate continuously to prevent lateral fall. EMG studies show postural muscle activation at 20-40 Hz during single-limb stance.
Estimated minimum correction frequency: 15-25 Hz.
At measured classical ceiling: FAIL. At 2x generous: MARGINAL at low end. At 4x extreme: PASS.

**Toddler's first step.** The child releases the table leg. Center of mass shifts forward and laterally simultaneously in a movement pattern the child has never performed. There is no learned motor program. Every correction is novel. The base of support transitions from two hands and two feet to two feet to one foot. No skeletal resting point during single-limb phase. No prior training to draw on. The musculoskeletal system is still developing and the corrections must be computed in real time with no stored program.
Estimated minimum correction frequency: 20-40 Hz.
At measured classical ceiling: FAIL. At 2x generous: FAIL at high end. At 4x extreme: PASS at low end, MARGINAL at high end.

**Running, stance phase.** Ground contact time per leg approximately 200-300 ms at moderate speed. Ground reaction forces 2-3 times body weight. The body must absorb impact, redirect center of mass, and generate propulsive force within the stance window. The ground reaction force vector changes continuously throughout stance.
Estimated minimum correction frequency: 30-50 Hz.
At measured classical ceiling: FAIL. At 2x generous: FAIL. At 4x extreme: PASS at low end only.

**Catching a ball (planned, expected).** Visual tracking, hand positioning, grip timing, arm extension along interception trajectory. Inter-joint timing for coordinated reaching measured at 5-10 ms precision between shoulder, elbow, and wrist.
Estimated minimum correction frequency: 30-60 Hz.
At measured classical ceiling: FAIL. At 2x generous: FAIL. At 4x extreme: PASS at low end only.

**Unexpected perturbation response (being pushed).** Perturbation unpredicted. Detection, characterization, response selection, and execution must all occur within the mechanical time constant. Measured initial corrective EMG responses begin 40-60 ms after perturbation — well within the first neural round-trip time, suggesting the initial response uses a pathway faster than spinal reflex arc.
Estimated minimum correction frequency: 30-60 Hz.
At measured classical ceiling: FAIL. At 2x generous: FAIL. At 4x extreme: PASS at low end only.

**Sprinting, ground contact phase.** Contact time 80-100 ms at elite speeds. Ground reaction forces 4-5 times body weight. The entire stance phase — impact absorption, center of mass redirection, propulsive force generation, spinal stabilization, arm coordination — occurs in a window shorter than one correction cycle at any classical carrier speed.
Estimated minimum correction frequency: 60-120 Hz.
At measured classical ceiling: FAIL. At 2x generous: FAIL. At 4x extreme: FAIL.

**Jumping, inter-joint timing.** Takeoff requires coordinated extension of ankle, knee, and hip in a precise temporal sequence. If ankle extends before the knee is ready, force is wasted. Measured inter-joint timing precision for maximal vertical jump: 5-10 ms between joints.
Estimated minimum correction frequency: 40-80 Hz.
At measured classical ceiling: FAIL. At 2x generous: FAIL. At 4x extreme: FAIL at high end.

**Landing, impact absorption.** Impact duration 50-100 ms depending on stiffness strategy. Ground reaction forces 3-10 times body weight depending on drop height. Eccentric muscle contractions must be precisely timed and graded across every joint simultaneously. Surface compliance, angle, and symmetry of contact are unknown until the foot touches — the system needs real-time feedback during the impact window.
Estimated minimum correction frequency: 50-200 Hz.
At measured classical ceiling: FAIL. At 2x generous: FAIL. At 4x extreme: FAIL.

**Typing at speed.** Sequential finger movements at 5-10 keystrokes per second. Each keystroke requires coordinated flexion, extension, and stabilization across 3-4 finger joints plus wrist stabilization. Inter-keystroke timing precision measured at 20-30 ms.
Estimated minimum correction frequency: 20-40 Hz.
At measured classical ceiling: FAIL. At 2x generous: FAIL at high end. At 4x extreme: PASS.

**Wrestling and grappling.** Both bodies in continuous unpredictable contact. Forces change direction and magnitude multiple times per second. An intelligent adversary actively attempts to destroy postural stability. Correction demand is continuous, multi-directional, and adversarial. The correction frequency must match or exceed the opponent's perturbation rate.
Estimated minimum correction frequency: 30-100 Hz.
At measured classical ceiling: FAIL. At 2x generous: FAIL. At 4x extreme: FAIL at high end.

**Tightrope walking.** Base of support is one-dimensional — the width of the wire. Any lateral deviation must be corrected immediately. The mechanical time constant is extremely short.
Estimated minimum correction frequency: 20-40 Hz.
At measured classical ceiling: FAIL. At 2x generous: FAIL at high end. At 4x extreme: PASS.

**Piano, fast passage.** Sequential and simultaneous finger coordination at high speed. Professional pianists execute passages requiring 10-15 notes per second with inter-note timing precision of 5-10 ms. Both hands operate independently with different coordination patterns.
Estimated minimum correction frequency: 40-80 Hz.
At measured classical ceiling: FAIL. At 2x generous: FAIL. At 4x extreme: FAIL at high end.

**Martial arts, fast combination.** Sequential strikes, each requiring whole-body coordination — legs, hips, trunk, shoulder, arm. Return to guard between strikes. 3-5 strikes per second in trained fighters. Each strike requires coordination across the full 100 cm kinetic chain.
Estimated minimum correction frequency: 50-120 Hz.
At measured classical ceiling: FAIL. At 2x generous: FAIL. At 4x extreme: FAIL.

**Ballet fouetté turn on toe.** Single toe as base. Body rotating at 1-2 revolutions per second. Working leg extending and retracting to modulate angular momentum. Arms opening and closing for rotation control. Head spotting — stays facing the audience while the body rotates, then whips around to re-acquire the focal point. Five simultaneous coordination tasks on a point base.
Estimated minimum correction frequency: 40-100 Hz.
At measured classical ceiling: FAIL. At 2x generous: FAIL. At 4x extreme: FAIL at high end.

**Ballet head spot whip.** During the fouetté, the head stays stationary then whips 360 degrees in 100-200 ms. The neck muscles must decelerate the head to zero at exactly the correct orientation while the torso continues rotating beneath it.
Estimated minimum correction frequency: 80-200 Hz.
At measured classical ceiling: FAIL. At 2x generous: FAIL. At 4x extreme: FAIL.

**Figure skating rotation.** Rotation at 5-6 revolutions per second during a triple axel. The Nyquist sampling theorem requires the correction frequency to be at least twice the rotation frequency to track angular position — minimum 10-12 Hz just to avoid aliasing. Actual control of rotation rate, angular position, landing preparation, and blade orientation requires correction frequencies well above Nyquist.
Estimated minimum correction frequency: 40-80 Hz.
At measured classical ceiling: FAIL. At 2x generous: FAIL. At 4x extreme: FAIL at high end.

**Triple axel landing.** Landing backward on one foot on a 4 mm blade on ice with negligible friction, after 3.5 rotations in 0.7 seconds of airtime. Impact 5-8 times body weight. The blade must land on the correct edge at the correct angle. All correction must occur within the 50-100 ms impact window.
Estimated minimum correction frequency: 80-200 Hz.
At measured classical ceiling: FAIL. At 2x generous: FAIL. At 4x extreme: FAIL.

### 5.2 The full activity matrix — human

| Activity | Min Hz (conservative) | Measured ceiling (6.9 Hz) | 2x generous (13.3 Hz) | 4x extreme (30.1 Hz) | EMF |
|---|---|---|---|---|---|
| Quiet stance | 6-12 | MARGINAL | PASS | PASS | PASS |
| Walking | 15-25 | FAIL | MARGINAL | PASS | PASS |
| Toddler first step | 20-40 | FAIL | FAIL | MARGINAL | PASS |
| Running | 30-50 | FAIL | FAIL | MARGINAL | PASS |
| Catching (planned) | 30-60 | FAIL | FAIL | MARGINAL | PASS |
| Unexpected push | 30-60 | FAIL | FAIL | MARGINAL | PASS |
| Typing at speed | 20-40 | FAIL | FAIL | PASS | PASS |
| Sprinting | 60-120 | FAIL | FAIL | FAIL | PASS |
| Jumping | 40-80 | FAIL | FAIL | FAIL | PASS |
| Landing | 50-200 | FAIL | FAIL | FAIL | PASS |
| Wrestling | 30-100 | FAIL | FAIL | FAIL | PASS |
| Tightrope | 20-40 | FAIL | FAIL | PASS | PASS |
| Piano fast passage | 40-80 | FAIL | FAIL | FAIL | PASS |
| Martial arts combo | 50-120 | FAIL | FAIL | FAIL | PASS |
| Ballet fouetté | 40-100 | FAIL | FAIL | FAIL | PASS |
| Head spot whip | 80-200 | FAIL | FAIL | FAIL | PASS |
| Figure skating spin | 40-80 | FAIL | FAIL | FAIL | PASS |
| Triple axel landing | 80-200 | FAIL | FAIL | FAIL | PASS |

### 5.3 Reading the matrix

At measured classical carrier speeds, only quiet stance on flat ground is marginally supportable. Every other human motor activity fails.

At 2x generous speeds — doubling every classical carrier beyond its measured capability — walking becomes marginal and everything else still fails.

At 4x extreme speeds — quadrupling every carrier and halving transduction delays, with no empirical basis for either enhancement — walking, toddler first steps, running, planned catching, unexpected perturbation response, typing, and tightrope walking become marginally supportable. Everything involving high-speed coordination — sprinting, landing, jumping, combat, ballet, figure skating, fast piano — still fails.

No amount of generosity applied to classical carriers can support the upper half of the human activity repertoire. The activities that fail at 4x extreme are not exotic feats — they include sprinting, jumping, landing from a drop, playing a musical instrument at speed, and catching a ball. These are activities that billions of humans perform routinely.

EMF passes every activity with six orders of magnitude of headroom. The propagation delay is nanoseconds. The correction frequency ceiling is above one million hertz. There is no human motor activity that approaches the limit of EMF propagation speed.

### 5.4 Mouse activities (10 cm body, 10 cm coordination distance)

Mice do not perform ballet or figure skating. But they perform motor tasks that are measurably demanding, many of which are standard neuroscience experimental protocols.

**Quadrupedal walking.** Wide base, four contact points, low center of mass. The least demanding mouse locomotion.
Estimated minimum correction frequency: 10-20 Hz.

**Quadrupedal running.** Higher speed, shorter contact times per limb.
Estimated minimum correction frequency: 20-40 Hz.

**Wheel running at speed.** Continuous adjustment to curved surface. Standard laboratory exercise equipment.
Estimated minimum correction frequency: 30-50 Hz.

**Bipedal reach for food.** The mouse stands on hindpaws on toe tips, reaching upward for food from a dispenser. Digitigrade posture — all weight on metatarsal heads, no calcaneal resting point. Full muscular suspension of the entire kinetic chain. Zero passive stability. Point base of support. High center of mass relative to base. This is the most demanding balance posture in the standard mouse behavioral repertoire.
Estimated minimum correction frequency: 40-80 Hz.

**Rotorod at speed.** Standard neuroscience balance test. Mouse walks on a rotating cylinder, rotation speed increases until the animal falls. Requires continuous adjustment to a moving, curved, accelerating surface.
Estimated minimum correction frequency: 40-80 Hz.

**Balancing on narrow beam.** Standard neuroscience balance test. Reduced base of support.
Estimated minimum correction frequency: 30-60 Hz.

**Landing from drop.** Impact absorption on all four limbs simultaneously.
Estimated minimum correction frequency: 50-100 Hz.

**Fighting another mouse.** Unpredictable perturbation from an adversary.
Estimated minimum correction frequency: 40-100 Hz.

### 5.5 The full activity matrix — mouse

| Activity | Min Hz (conservative) | Measured ceiling (14.5 Hz) | 2x generous (28 Hz) | 4x extreme (59.1 Hz) | EMF |
|---|---|---|---|---|---|
| Quadrupedal walk | 10-20 | MARGINAL | PASS | PASS | PASS |
| Quadrupedal run | 20-40 | FAIL | MARGINAL | PASS | PASS |
| Wheel running | 30-50 | FAIL | MARGINAL | PASS | PASS |
| Bipedal reach | 40-80 | FAIL | FAIL | MARGINAL | PASS |
| Rotorod at speed | 40-80 | FAIL | FAIL | MARGINAL | PASS |
| Narrow beam | 30-60 | FAIL | FAIL | MARGINAL | PASS |
| Landing from drop | 50-100 | FAIL | FAIL | FAIL | PASS |
| Mouse fighting | 40-100 | FAIL | FAIL | FAIL | PASS |

### 5.6 Interpreting the mouse matrix

Even at 4x extreme generosity, mouse bipedal reach, rotorod at speed, and narrow beam balance are only marginally supportable. Landing from a drop and fighting fail at every generosity level.

The bipedal reach posture is particularly significant because the mouse is performing a task its musculoskeletal system was not designed for. The entire kinetic chain — toes, ankles, knees, hips, spine, head, plus forelimbs reaching for food — must be actively stabilized by continuous muscular contraction with no skeletal resting point. The correction frequency demand is at least as extreme as a human on a tightrope and probably greater because the mouse's body plan is optimized for quadrupedal locomotion, not bipedal balance.

---

## Section 6 — The Multi-Node Coordination Problem

The analysis in Sections 3-5 uses a simplified model: one signal traversing one distance between two actuators. The actual coordination problem is substantially harder.

The human body is not a single pendulum. It is a stack of mass centers at different heights, each one exerting gravitational torque on the joints below it, each one requiring active stabilization in coordination with every other mass center in the stack. A correction at the ankle changes the loading on the knee. The knee correction changes the loading on the hip. The hip correction changes the loading on the spine. Every correction propagates mechanical consequences up and down the chain.

For corrections to be constructive rather than destructive, all nodes must share state information within a single correction cycle. If the ankle corrects without knowledge of what the hip is doing, and the hip corrects without knowledge of what the ankle is doing, the corrections can conflict — producing overcorrection, oscillation, or instability.

### 6.1 Human coordination nodes (1.8 m standing height)

| Node | Height from ground | Role |
|---|---|---|
| Foot (center of pressure) | 0 cm | Ground contact, base of support |
| Ankle joint axis | 9 cm | Primary balance actuator |
| Knee joint axis | 50 cm | Stance leg stability |
| Ischium (hip base) | 82 cm | Pelvic floor, seated reference |
| Ilium (iliac crest) | 105 cm | Hip stabilization, lateral balance |
| L1 (lumbar-thoracic junction) | 120 cm | Trunk base, core stability |
| T6 (mid-thorax) | 140 cm | Trunk center, respiratory coupling |
| C7 (cervicothoracic junction) | 155 cm | Shoulder girdle base |
| C1 (atlas, skull base) | 170 cm | Head stabilization, vestibular coupling |
| Head center of mass | 180 cm | Highest mass center, visual stabilization |

Bilateral arm nodes (variable height): shoulder at 150 cm, elbow at 110 cm, hand at 82 cm at rest but highly variable during reaching.

### 6.2 The state-sharing problem

For each correction cycle, every node must know what every other relevant node is doing. This is not a single signal traversing one distance. It is a multi-point broadcast where every node transmits its state and every node receives the state of all others, within the correction cycle period.

The number of node pairs requiring state exchange is n(n-1)/2. For 10 primary nodes, that is 45 pairs. Each pair has a different distance. The longest pair (foot to head) is 180 cm. The shortest adjacent pairs are 10-20 cm.

### 6.3 Serial relay model

If state information propagates by serial relay — each node passes state to its neighbor, which passes to the next — the total latency is the sum of all hops. For the myelinated axon pathway at 120 m/s, the serial cascade from foot to head traverses approximately 180 cm with 9 inter-node hops, each requiring at least one synaptic relay.

Total serial latency: 180/120,000 × 1000 + 9 × 0.5 = 1.5 + 4.5 = 6.0 ms one-way.

This is the one-way latency for state to propagate from foot to head. The round-trip is twice this: 12 ms. During that 12 ms, no node has complete state information about the full chain. Corrections computed during this window are based on incomplete data.

At any correction frequency above 13 Hz, the serial cascade latency exceeds the correction cycle period. The system cannot complete one state-sharing pass before the next correction is due.

### 6.4 Parallel broadcast from central controller

If state is collected centrally (e.g., at the spinal cord or brainstem) and corrections broadcast outward, the latency is dominated by the most distant node.

Distance from lumbar spinal cord to ankle: approximately 85 cm. Distance from lumbar spinal cord to C1: approximately 85 cm in the opposite direction. The round trip for the most distant pair through the central controller is approximately 170 cm at 120 m/s plus synaptic delays.

Total parallel round-trip: 170/120,000 × 1000 × 2 + 3 × 0.5 = 2.8 + 1.5 = 4.3 ms minimum.

At any correction frequency above 37 Hz, the parallel broadcast latency exceeds the cycle period.

### 6.5 EMF broadcast

Every node transmits its electromagnetic field signature simultaneously. Every other node receives the field from every other node simultaneously. The propagation time over 180 cm at 2.1 × 10⁸ m/s is 8.6 nanoseconds.

Total state-sharing latency: approximately 0.000009 ms.

All 45 node pairs share state within 9 nanoseconds. The entire correction cycle period is available for computation and execution. No communication cost.

### 6.6 The state-sharing budget

| Model | State-sharing latency (180 cm) | Budget consumed at 50 Hz (20 ms cycle) | Budget remaining for computation |
|---|---|---|---|
| Serial relay | 12 ms | 60% | 40% |
| Parallel broadcast | 4.3 ms | 21.5% | 78.5% |
| EMF | 0.000009 ms | 0.00005% | 99.99995% |

At 100 Hz correction frequency (10 ms cycle):

| Model | State-sharing latency | Budget consumed | Budget remaining |
|---|---|---|---|
| Serial relay | 12 ms | 120% (IMPOSSIBLE) | None |
| Parallel broadcast | 4.3 ms | 43% | 57% |
| EMF | 0.000009 ms | 0.00009% | 99.99991% |

The serial relay model physically cannot operate at 100 Hz — the state-sharing alone takes longer than the entire cycle. The parallel broadcast model can barely operate at 100 Hz but consumes nearly half the budget on communication, leaving limited time for computation.

EMF provides state-sharing for free at every frequency.

---

## Section 7 — The Three-Channel Architecture

If EMF provides the timing signal and synaptic transmission provides the motor commands, why does the body need both? Why not just one?

Because they carry different types of information, and neither can carry what the other carries.

### 7.1 Channel one — electromagnetic field (the fast channel)

Carries: timing, synchronization, phase relationships.
Speed: effectively instantaneous at biological distances.
Content: minimal. "Fire NOW." "Phase-lock with this group." "Synchronize at this frequency."
Cannot carry: molecular specificity, force levels, muscle fiber recruitment patterns, direction, magnitude of contraction.

The EMF channel is the conductor's baton. It tells every musician when to play. It does not tell them which note to play.

### 7.2 Channel two — synaptic transmission (the rich channel)

Carries: content, specificity, molecular identity.
Speed: 1-120 m/s depending on myelination.
Content: which specific neurotransmitter, which receptor, which ion channel, what force level, which specific muscle fibers to recruit, excitatory or inhibitory, what magnitude.
Cannot carry: sub-millisecond timing across distances greater than a few centimeters.

The synaptic channel is the sheet music. It tells every musician which note to play, at what volume, with what articulation. It cannot tell them when to play it with sub-millisecond precision across the full orchestra.

### 7.3 Channel three — neuromodulatory (the configuration channel)

Carries: mode, state, network topology configuration.
Speed: diffusion-mediated, seconds to minutes.
Content: which coordination networks are active, what overall state the system is in (calm, alert, combat, sleep), which phase-lock relationships to prioritize.
Cannot carry: timing or specific motor commands.

The neuromodulatory channel is the program selection. It determines which piece the orchestra is performing. It does not conduct the orchestra or specify the notes. It sets the context within which the other two channels operate.

Neuropeptides, hormones, and neuromodulators like dopamine, serotonin, noradrenaline, and cortisol operate on this channel. When a person steps onto the mat for judo, the configuration channel shifts the entire coordination network from "walking around" to "fighting." This reconfiguration takes seconds, which is why there is a warmup period and why experienced fighters "find their rhythm" over the first minute of engagement.

### 7.4 Why all three are necessary

Timing without content is flailing. The EMF channel fires "NOW" and every muscle activates simultaneously with no coordinated purpose. This is the baseball fan's flinch — fast, synchronized, useless.

Content without timing is dyscoordination. The synaptic pathways carry perfect motor commands but the commands arrive at different muscles at different times because the content channel cannot synchronize across the full body within the required timing window. This is the presentation of certain neurological conditions — the patient knows what to do but the execution is temporally fragmented.

Configuration without timing or content is mood without action. The neuromodulatory state says "we are in combat mode" but neither coordination nor execution occurs. This is the freeze response — the system is configured for action but neither the timing nor the content channels are operating.

All three channels together: the configuration channel sets the network to combat mode, the EMF channel synchronizes all relevant muscle groups into phase-lock at the combat coordination frequency, and the synaptic channel delivers the specific force commands to each muscle at each moment. The result is coordinated, purposeful, fast action — the trained fighter responding to a throw attempt with a counter in 200 milliseconds.

### 7.5 The fast and the rich

The division can be stated in five words: EMF is fast. Synapses are rich.

The body needs the fast channel for coordination timing. The body needs the rich channel for motor content. The body needs the configuration channel to set the context. No single channel can do all three jobs. The three-channel architecture is not redundancy — it is division of labor across three physical mechanisms with different speed and content characteristics.

---

## Section 8 — The Surprise Response as Natural Experiment

Return to the baseball fan.

The three-channel model predicts three distinct phases in any surprise motor response, each mediated by a different combination of channels.

### 8.1 Phase one — startle (0-80 ms)

The visual system detects a fast-approaching object on a collision trajectory. The brainstem triggers a startle reflex before the prefrontal cortex has identified the object. The EMF timing channel fires a generic protective activation signal. Every motor node receives it simultaneously. The response is fast, whole-body, stereotyped: shoulders up, head down, hands up, trunk flexion.

This phase is identical in every human regardless of training. The trained outfielder and the civilian produce the same startle. The EMF channel fires on threat geometry — fast approaching object — not on object identity.

The startle is not a failure of coordination. It is the timing channel operating alone, without content. The "NOW" signal fires. The content channel has not yet loaded any program. The result is fast, synchronized, purposeless protective activation.

### 8.2 Phase two — identification (80-200 ms)

The visual cortex completes object identification. The prefrontal cortex recognizes the context. The decision to redirect from protection to task-specific action occurs. This phase is cognitive, mediated by standard neural pathways, and takes roughly the same time in trained and untrained subjects — visual processing speed does not differ significantly between people who can catch and people who cannot.

### 8.3 Phase three — program loading (200-400 ms)

The trained outfielder: the cerebellum loads the catching program. The configuration channel switches the EMF mesh from startle topology to catching topology. The synaptic content channel activates the trained motor pathways. The hands redirect from the face toward the ball. The arm extends along the interception trajectory. The grip opens, times itself to the ball's arrival, and closes.

The untrained civilian: the cerebellum searches for a catching program and finds nothing. The configuration channel has no trained catching topology to switch to. The content channel has no pathway to activate. The civilian remains in startle mode or transitions to a crude, uncoordinated reaching gesture.

### 8.4 The critical observation

Even the trained outfielder startles first. The startle is not a skill issue. It is a channel issue. The timing channel fires before the content channel has loaded. The trained outfielder recovers from startle to catch in 200 milliseconds because the content channel has a program ready. The civilian does not recover because there is no program to load.

The surprise response is a natural experiment that separates the two channels without any experimental intervention. Everyone has experienced both states. The three-channel model explains the difference: fast but purposeless activation (timing channel alone) transitioning to fast and purposeful action (timing plus content channels together) if and only if the content channel has a trained program available.

---

## Section 9 — EMF Propagation Architectures

Stating that "EMF" is the timing channel is necessary but incomplete. The body is not a vacuum. It is a dense, warm, electromagnetically noisy medium where every neuron fires, every muscle generates fields, every cardiac cycle broadcasts, and every ion channel contributes to a cacophony of electromagnetic activity. A femto-Tesla coordination signal from C1 does not propagate through silence. It propagates through a screaming crowd.

The question is not whether EMF can propagate through tissue — it can, at well-characterized speeds. The question is how a coordination signal maintains integrity in the presence of overwhelming biological electromagnetic noise.

This paper enumerates the candidate architectures. It does not claim to determine which one the body uses. That is an experimental question for future work.

### 9.1 Architecture one — direct broadcast

A single neuron or group at one node generates an electromagnetic field. The field radiates through tissue. A distant node detects the field.

Problem: signal-to-noise ratio. The coordination signal at femto-Tesla levels competes with electromagnetic noise from cardiac activity (millivolt range), neural firing throughout the brain and spinal cord, and muscular activity throughout the body. The ratio of signal to noise is approximately 1:10⁹. Direct detection of a single source through bulk tissue noise is physically implausible without encoding.

Assessment: unlikely as primary mechanism. Possible as gross synchronization backup.

### 9.2 Architecture two — phase-lock handshake

Two nodes establish synchronized oscillation at a specific frequency. Once locked, communication occurs through phase deviation against the locked carrier — the same principle as FM radio. The receiver does not need to detect the absolute signal above the noise. It detects phase change relative to its own oscillation.

The carrier-to-noise ratio determines success, not the absolute signal strength. Phase-locked systems can communicate through noise that would completely overwhelm amplitude-based detection.

The biological question: can neurons establish and maintain phase-lock at femto-Tesla field strengths? Ephaptic coupling — where the field generated by one neuron's activity influences neighboring neurons without synaptic connection — has been demonstrated in cortical tissue at millivolt-per-meter field strengths over micrometer-to-millimeter distances. Whether phase-lock extends to longer ranges through accumulated coupling is an open question.

Assessment: biologically plausible. The strongest single-mechanism candidate.

### 9.3 Architecture three — relay chain and mesh network

Phase-lock propagates through nearest-neighbor coupling. Each link in the chain maintains lock over millimeters — well within the range where ephaptic coupling is demonstrated. The coordination signal propagates as a wave of synchronization through the chain.

This model extends naturally to a mesh network. Nodes do not form serial chains — they form simultaneous multi-frequency phase-lock relationships with multiple partners. The C1 vertebra, the right big toe, the left wrist, the right shoulder, and the left jaw might all participate in a single phase-lock network, while simultaneously participating in other networks at different frequencies.

The body's coordination topology is a mesh, not a ring. Communication is simultaneous, not serial. Each node maintains independent phase-lock relationships with multiple partners at multiple frequencies.

The mesh network model predicts graceful degradation from injury — the network loses nodes but does not fail catastrophically. This matches clinical observation: spinal lesions and peripheral nerve injuries degrade coordination proportionally rather than producing total collapse, and partial recovery occurs through network reorganization.

Assessment: biologically plausible. Explains graceful degradation, motor learning, and the intermediate inconsistency of skill acquisition.

### 9.4 Architecture four — waveguide

Certain anatomical structures could confine and guide the electromagnetic field, reducing attenuation and improving signal-to-noise by excluding noise sources outside the waveguide.

Candidate waveguides: myelinated nerve bundles (dielectric insulator surrounding a conductive core — structurally identical to a coaxial cable), fascial planes (sheets of connective tissue with different electromagnetic properties than surrounding muscle), blood vessels (conductive fluid in tubular geometry), and the spinal canal (cerebrospinal fluid in a bony tube).

A myelinated axon functioning as an electromagnetic waveguide would carry the field at a speed determined by the dielectric properties of myelin and the bundle geometry, independent of its role in saltatory spike conduction. The two functions — spike conduction along the axon and field propagation along the sheath — are physically compatible in the same structure.

Assessment: biologically plausible. Would explain why myelination improves coordination beyond what conduction speed alone accounts for — the myelin serves as both spike insulator and field waveguide.

### 9.5 Architecture five — frequency multiplexing

Different coordination tasks operate on different frequency bands. Postural coordination at one frequency, fine motor coordination at another, cardiac coordination at another. Each muscle group tunes to its coordination frequency through the frequency selectivity of its neural oscillations.

Neural frequency bands are well-documented: theta (4-8 Hz), alpha (8-13 Hz), beta (13-30 Hz), gamma (30-100 Hz), high gamma (100-200 Hz). These bands coexist in the same tissue simultaneously. Cross-frequency coupling — where the phase of one band modulates the amplitude of another — is a measured phenomenon.

Assessment: biologically plausible. Would explain how multiple independent coordination tasks can operate simultaneously without interference.

### 9.6 The probable reality

These architectures are not mutually exclusive. The most likely implementation is a combination: phase-locked nodes in a mesh topology, communicating through frequency-multiplexed channels, with major pathways guided by anatomical waveguides, using nearest-neighbor relay to extend range.

This paper does not claim to know which combination the body uses. It establishes that EMF is necessary for the timing channel, enumerates the architectures that could implement the timing channel, and proposes experiments that would discriminate between them.

---

## Section 10 — Expanded Hebb's Rule and Motor Learning

"Neurons that fire together wire together" is Hebb's rule, and it has always been described as a synaptic phenomenon — repeated co-activation strengthens the chemical synapse between neurons. But if EMF phase-locking is a real coordination mechanism, Hebb's rule has a second channel.

### 10.1 Classical Hebb

Repeated co-activation strengthens synaptic connections. Dendrites grow more receptors. Transmission becomes faster and more reliable. The material pathway builds through use.

### 10.2 Expanded Hebb

Neurons that fire together first phase-lock together through EMF coupling, then wire together through synaptic strengthening.

The field is the scout. It establishes the temporal coordination between nodes that need to work together. The synapse is the road crew. It builds the material pathway that carries the content.

The scout moves at the speed of light and says "this pathway matters, build here." The road crew builds over days and weeks of repeated use, and when it's built, it carries the payload the scout can't carry.

### 10.3 Motor learning dynamics under the two-channel model

**Early learning.** A novice attempts a triple axel. No EMF phase-lock network exists for this movement pattern. No synaptic pathways are established. Both channels are absent. The movement fails completely.

**Intermediate learning.** After moderate training, some phase-lock relationships have been established but they are unstable. The athlete can sometimes land the jump — when the phase-lock holds for the full 0.7 seconds of airtime, the timing is right and the trained content carries the movement. But the phase-lock network is fragile. Distraction, fatigue, or anxiety disrupts the phase-lock and the attempt fails. This is the stage every athlete recognizes: sometimes it works perfectly and you can't explain why, sometimes it fails completely and you can't explain why. The variability is not in the muscles. It is in the coordination network.

**Expert performance.** After extensive training, both channels are fully built. The phase-lock network is dense and stable. The synaptic pathways are robust and heavily myelinated. Both channels support the movement. Even if one channel has a momentary disruption, the other compensates. This is why experts are consistent — redundancy in the coordination architecture, not just strength in any single pathway.

**Relearning after layoff.** After years of retirement, the athlete attempts the skill again. Synaptic pathways have weakened through disuse. But the phase-lock relationships — if they are a property of the electromagnetic network topology — may re-establish faster than the synapses rebuild. This would explain why motor skills return faster than they were originally learned. The field network re-locks, providing a coordination scaffold around which the synaptic pathways reconsolidate. "It's like riding a bike" — the first channel comes back faster than the second.

### 10.4 The fatigue cliff

Athletes report a consistent phenomenon: performance is stable, stable, stable, then collapses suddenly. Not gradual degradation — a cliff.

The two-channel model predicts this. The EMF timing channel fatigues first — phase-lock becomes unstable, the mesh thins. During this degradation, the synaptic content channel compensates. Performance remains adequate because the material pathways are robust enough to partially cover the loss of precise timing. Then the synaptic channel also fatigues under the increased burden of compensating for the degraded timing channel. Both channels are now degraded simultaneously. Performance collapses suddenly because the compound failure of both channels is qualitatively different from the degradation of either channel alone.

The single-channel synaptic model predicts gradual degradation proportional to metabolic exhaustion. The cliff is not predicted. The cliff is observed universally in athletics. The two-channel model accounts for it.

### 10.5 The myelination bonus

Myelination increases axon conduction speed. But the timing analysis in this paper shows that even myelinated conduction is too slow for coordination across distances greater than a few centimeters at the frequencies human motor activities demand. If the synapse is the content channel and speed is not the binding constraint on content delivery, why does myelination improve coordination so dramatically?

Because the myelin sheath is also an electromagnetic waveguide. When the synaptic pathway myelinates, the electromagnetic properties of the pathway change. The dielectric sheath confines the field. The axon bundle becomes a better waveguide. The phase-lock between endpoints becomes more stable because the field has a physical channel that guides it rather than propagating through bulk tissue.

The material infrastructure (myelin) improves both channels simultaneously: the wired channel (faster spike conduction for content delivery) and the wireless channel (better field waveguide for timing stability). Two functions in one structure. One characterized. One not yet.

---

## Section 11 — Proposed Experimental Program

### Experiment 1 — Mouse startle desynchronization

**Rationale.** The acoustic startle reflex is involuntary, stereotyped, brainstem-mediated, and requires no cortical involvement or training. It is the purest expression of the timing channel operating alone. If EMF provides the timing for whole-body synchronization, interference at the coordination frequency should desynchronize the bilateral startle response.

**Method.** Standard acoustic startle protocol in laboratory mice. Bilateral surface EMG at 10 kHz sampling on symmetric muscle groups (bilateral gastrocnemius, bilateral trapezius). Baseline startle synchrony measured across 50 trials per animal. Then EMF interference introduced at the predicted coordination frequency during startle trials. Controls: sham interference (equipment active, no signal), off-frequency interference (signal at frequencies above and below predicted coordination band), broadband noise control.

**Prediction.** Frequency-specific EMF interference desynchronizes bilateral startle timing — muscles still fire (the brainstem command still arrives via synaptic pathway) but they fire out of sync (the EMF timing signal is jammed). Off-frequency interference and sham produce no desynchronization.

**Safety.** Continuous ECG monitoring throughout all trials. Femto-Tesla amplitude — orders of magnitude below known tissue damage thresholds. Protocol begins at lowest amplitude and titrates upward. Any cardiac irregularity terminates the session and is reported as a finding.

**Significance.** If bilateral startle synchrony is degraded specifically by interference at the predicted coordination frequency, the timing channel has been isolated in its purest form.

### Experiment 2 — Mouse bipedal reach degradation

**Rationale.** The bipedal reach posture is the most demanding balance task in the standard mouse behavioral repertoire. The mouse is on toe tips with zero passive stability and full muscular suspension of the kinetic chain. If any motor task requires EMF coordination, this one does.

**Method.** Train mice to reach bipedally for food reward. Establish baseline hold duration, postural sway, and success rate across hundreds of trials. Apply EMF interference at the predicted coordination frequency during bipedal reach only. Compare with quadrupedal locomotion under the same interference.

**Prediction.** Frequency-specific interference degrades bipedal reach (reduced hold time, increased sway, more failures) without affecting quadrupedal locomotion. The task-specific and frequency-specific double dissociation is the signature. If the effect is specific to both the demanding task and the predicted frequency, it cannot be explained by startle, pain, general neurological disruption, or nonspecific artifact.

**Dose-response.** Titrate interference amplitude from lowest to highest. Plot hold-time versus amplitude. The shape of the curve tests the network architecture: gradual degradation supports mesh network (progressive connection loss), sudden threshold failure supports single-channel model.

### Experiment 3 — Mouse rotorod fatigue cliff

**Rationale.** The two-channel model predicts that EMF interference should shift the fatigue cliff earlier by forcing the synaptic channel to carry the full coordination load sooner.

**Method.** Standard rotorod protocol at fixed speed, run to failure. Measure time-to-failure with and without sub-threshold EMF interference (amplitude below the level that causes immediate performance failure).

**Prediction.** Under interference, time-to-failure decreases and the performance degradation curve changes shape — from gradual decline to sharper cliff — because the timing channel is degraded, loading the content channel earlier, which fatigues faster under the increased burden.

### Experiment 4 — Human VR surprise catching

**Rationale.** The surprise response separates the timing and content channels naturally. VR provides perfect stimulus control. Training manipulation builds the content channel while the timing channel is always present.

**Method.** Subjects in VR goggles performing a primary visual task. Balls launch from periphery toward face at randomized intervals. Full upper body surface EMG at 10 kHz sampling plus high-speed motion capture at 1,000+ fps.

Two groups: trained (practiced VR ball catching between sessions) and untrained. Within each group: EMF interference versus no interference, randomized across trials, subject-blinded.

**Predictions.**

Phase one (startle, 0-80 ms): identical across all four conditions. If EMF interference desynchronizes the startle, this replicates Experiment 1 in humans.

Phase two (identification, 80-200 ms): shorter in trained than untrained. Unaffected by interference because this phase is cognitive, not coordinative.

Phase three (execution, 200-400 ms): trained without interference shows coordinated catching. Trained with interference shows correct spatial trajectory but degraded inter-muscle timing — the subject reaches toward the right place but the grip timing is off. Untrained without interference shows uncoordinated flailing. Untrained with interference shows worse flailing.

**Critical comparison.** Trained with interference versus trained without. If interference degrades temporal coordination (phase dispersion between muscle groups) while preserving spatial accuracy (hand trajectory toward interception point), that is a clean dissociation of the timing channel from the content channel. This result cannot be explained by a single-channel model.

**Note on the theoretically decisive experiment.** The theoretically most powerful test of the EMF coordination hypothesis would be active interference at sufficient amplitude to completely disrupt the body's internal electromagnetic coordination, producing total motor coordination failure. This experiment would constitute a directed energy weapon and cannot be ethically conducted on human or vertebrate animal subjects except at the sub-threshold levels specified in this protocol. The paper notes the existence of military directed-energy research programs that may have produced relevant classified results. This observation is made without endorsement of those methods.

**Note on the Faraday cage.** A commonly proposed experimental design is to test balance inside a Faraday cage that blocks electromagnetic fields. This design is invalid for the EMF coordination hypothesis because the coordination signal is endogenous — generated by the body's own tissue and propagating through the body's own tissue as the medium. A Faraday cage attenuates external fields entering or leaving the enclosure. It does not attenuate fields propagating within the body. The body is the medium, and the cage is outside the medium.

---

## Section 12 — Falsification Criteria

This paper is falsified if any of the following are demonstrated.

**F1.** Mouse bilateral startle synchrony is unaffected by frequency-specific EMF interference at any amplitude up to the safety limit. This would indicate that the startle is not EMF-coordinated.

**F2.** Mouse bipedal reach performance is unaffected by frequency-specific EMF interference while being degraded by broadband interference. This would indicate a nonspecific effect rather than frequency-specific timing channel disruption.

**F3.** Trained human VR catching shows degraded spatial accuracy rather than degraded temporal coordination under EMF interference. This would indicate the interference is disrupting the content channel, not the timing channel, contradicting the two-channel model.

**F4.** The fatigue cliff is absent in both interference and non-interference conditions on the rotorod, or present equally in both. This would falsify the two-channel fatigue prediction.

**F5.** A classical carrier is discovered that propagates above 1,000 m/s through soft tissue without transduction delay. This would require revision of the carrier elimination argument to include the new carrier.

**F6.** Measurement of actual correction frequencies during demanding motor tasks (bipedal reach in mice, sprinting or ballet in humans) reveals that the frequencies are below the classical carrier ceiling at measured speeds. This would eliminate the timing gap that motivates the entire argument.

Each criterion is concrete, testable, and would genuinely terminate the relevant part of the hypothesis if observed.

---

## Section 13 — What We Claim and What We Do Not Claim

### We claim

The timing requirements for dynamic motor coordination exceed what any classical carrier can provide, even under extremely generous assumptions about undiscovered biological enhancements. This is demonstrated by the engineering analysis: distance, speed, and timing arithmetic applied to measured carrier speeds and estimated activity demands.

The electromagnetic field is the only known physical mechanism with sufficient propagation speed to meet the timing requirements for all human and mammalian motor activities. This follows from the carrier elimination.

### We propose

A three-channel architecture: EMF for timing, synaptic transmission for content, neuromodulatory signaling for configuration. This is a hypothesis consistent with known motor phenomena but not yet experimentally confirmed.

An expanded Hebb's rule: neurons that fire together first phase-lock through EMF, then wire together through synaptic strengthening. This explains motor learning dynamics, the fatigue cliff, the myelination bonus, and rapid relearning after layoff.

Specific experiments on mice and humans that would confirm or falsify the EMF timing hypothesis and discriminate between possible architectures.

### We do not claim

That EMF is sufficient for motor coordination. It is necessary for timing. Content requires synaptic pathways. Configuration requires neuromodulation. All three channels are needed.

That we know which EMF architecture the body uses. We enumerate candidates (broadcast, phase-lock, relay chain, mesh network, waveguide, frequency multiplexing) and propose experiments to discriminate between them.

Anything requiring exotic physics. This paper uses classical electrodynamics, standard control theory, and measured biological parameters. No quantum effects, no microtubules, no consciousness theories.

### We do not dismiss

Slower corrective pathways. They exist, they carry content, they are essential. They simply cannot meet the sub-millisecond timing specification that dynamic motor coordination requires.

---

## Section 14 — Data Annex

All tables in this paper are reproducible with a pocket calculator. No statistical software is required. The arithmetic is: distance divided by speed equals transit time. Transit time plus transduction delays equals round-trip time. Round-trip time compared to the control theory delay ceiling determines pass or fail.

### A. Carrier speed reference table

All values from Section 3, with measured, 2x generous, and 4x extreme estimates.

### B. Maximum correction frequency table

All values from Section 4, for human (100 cm) and mouse (10 cm) distances.

### C. Human activity demand matrix

All values from Section 5.1, with pass/fail against each carrier at each generosity level.

### D. Mouse activity demand matrix

All values from Section 5.4, with pass/fail against each carrier at each generosity level.

### E. Multi-node distance matrix

All inter-node distances from Section 6.1.

### F. State-sharing budget analysis

Serial relay, parallel broadcast, and EMF state-sharing costs at 50 Hz and 100 Hz correction frequencies.

---

## References

1. Kandel, E.R., Schwartz, J.H., Jessell, T.M., Siegelbaum, S.A., & Hudspeth, A.J. Principles of Neural Science, 6th Edition. McGraw-Hill, 2021. (Conduction velocities, synaptic delays, neural architecture.)

2. Gabriel, S., Lau, R.W., & Gabriel, C. The dielectric properties of biological tissues: III. Parametric models for the dielectric spectrum of tissues. Physics in Medicine and Biology, 41(11), 2271-2293, 1996. (Tissue permittivity for EM propagation calculations.)

3. Ogata, K. Modern Control Engineering, 5th Edition. Prentice Hall, 2010. (Control theory delay requirements, stability margins.)

4. Schleip, R., Findley, T.W., Chaitow, L., & Huijing, P.A. Fascia: The Tensional Network of the Human Body. Churchill Livingstone, 2012. (Fascial mechanotransduction propagation speeds.)

---

**END HOWL-NEURO-1-2026**

**Registry:** HOWL-NEURO-1-2026
**Status:** Position paper with proposed experimental program
**Verification:** All arithmetic reproducible with pocket calculator
**Falsification:** Six explicit criteria specified
**Experimental program:** Four experiments proposed (three mouse, one human)
**Claims boundary:** Necessity of EMF for timing established by elimination; mechanism and architecture proposed but not yet confirmed

The carrier elimination table is arithmetic.
The activity matrix is physics.
The three-channel model is a hypothesis.
The experiments are a program.

The arithmetic is not debatable. The physics is measurable. The hypothesis is testable. The program is executable.

The rest is someone's move.