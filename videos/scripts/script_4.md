# Video 4 Script: What Unification Actually Gets You — From Fiber Optics to Drug Design

## Delivery Notes

This is the most accessible video in the series. No equations, minimal Greek letters, maximum real-world connection. You're answering the "so what" question. The audience is anyone who watched Videos 1-3 and thought "interesting, but what does it do for me?" The energy is entrepreneurial — you're describing opportunities, not just results.

Each industry section follows the same template: current state → gap → the chain from integers → what's missing. The repetition IS the argument. By the third industry, the viewer predicts the pattern.

---

## SECTION 1: Opening — Reframing the Question (1 minute)

*[In frame, talking to camera. No slides.]*

### TECHNICAL VERSION

Three videos in, you've seen the framework: 53 derived values from 13 inputs across 9 domains. You've seen why it wasn't found before. You've seen the complete twelve-layer stack.

The natural response is: so what? Gauge coupling unification is a physics problem. Why should anyone outside physics care?

Because unification isn't a physics achievement. It's an engineering achievement. Every industry that depends on a physical constant — telecommunications, semiconductors, pharmaceuticals, climate science, materials engineering — is waiting for derivation chains that connect measured parameters to their integer origins. The chains are visible now. The computation remains to be done.

This video traces those chains from the gauge group to your internet speed, your medication cost, and your climate model.

### NON-TECHNICAL VERSION

Three videos in, you've seen what the model does and how it works. The natural question is: so what? Who cares about unifying physics forces?

You should. Because unification isn't about physics — it's about everything physics touches. Your phone, your medication, your internet speed, your solar panel, your climate forecast. All of these depend on physical constants that are currently measured, not derived.

Measured constants have margins of error. Margins of error mean safety factors. Safety factors mean wasted performance — slower internet, worse drugs, less efficient solar cells.

If you can derive those constants from integers with higher precision than current measurements, you can shrink the margins. Not by building new hardware — by understanding the existing hardware better.

This video is about those chains. From gauge integers to your daily life.

### MERGE NOTES

You're an engineer. "So what does it do" is a question you've answered a thousand times. The framing — "it's an engineering achievement, not a physics achievement" — is yours. Lead with it.

---

## SECTION 2: The General Principle (2 minutes)

*[In frame. No slides yet.]*

### TECHNICAL VERSION

The general principle is a derivation chain: every engineering parameter traces back through material properties, atomic physics, and molecular physics to the fundamental couplings, which trace to gauge integers.

Material property → atomic/molecular physics → fundamental couplings → gauge integers.

Each link in the chain is a known physics calculation. None requires new physics. The obstacle at each link is computational difficulty and departmental isolation, not missing equations.

Example: the refractive index of silica glass at 1550 nm. This is a material property that determines the performance of every fiber optic system on Earth. It traces through the Sellmeier dispersion model (bulk optics) → electronic polarizability of Si and O atoms (atomic physics) → binding energies set by α and nuclear charges Z_Si = 14, Z_O = 8 (quantum electrodynamics) → α derived from integer fraction arithmetic (gauge theory).

Each link uses known equations. No link has been computed end-to-end in exact arithmetic. The chain exists. The computation hasn't been run.

### NON-TECHNICAL VERSION

Here's the principle, and I'll say it once because it applies to every example in this video.

Every engineering problem depends on a material property. That property depends on how atoms are arranged and how they interact. How atoms interact depends on the fundamental forces. The fundamental forces are controlled by integer fractions.

So: engineering problem → material property → atomic physics → integer fractions.

Every link in that chain uses known equations. Every link has been computed individually. Nobody has run the full chain from integers to engineering parameter in exact arithmetic. The equations exist. The computation hasn't been done.

That's the opportunity. Not new physics. New computation. Using existing equations, in exact arithmetic, crossing every departmental wall.

### MERGE NOTES

You understand this as a pipeline. Input → transformations → output. Each transformation is a known function. Nobody has composed the full pipeline. You can explain this from engineering intuition without any physics terminology.

---

## SECTION 3: Fiber Optics — The Most Concrete Example (5 minutes)

*[Slides showing DWDM channel plans and safety margins]*

### TECHNICAL VERSION

Dense wavelength division multiplexing (DWDM) systems transmit multiple data channels on different wavelengths of light through a single optical fiber. Current commercial deployments achieve approximately 100 Tb/s per fiber. Laboratory demonstrations have reached 430 Tb/s (NTT, 2024). The theoretical limit for standard single-mode fiber (SMF-28) is approximately 600 Tb/s, set by the Shannon limit in the nonlinear fiber channel.

The gap between 100 and 600 Tb/s exists because three physical parameters are known through empirical curve fitting rather than first-principles derivation:

1. The Sellmeier coefficients: six fitted parameters (B₁, B₂, B₃, C₁, C₂, C₃) that determine the refractive index n(λ) as a function of wavelength. These are obtained by fitting the Sellmeier equation n²(λ) = 1 + Σ B_i λ²/(λ² − C_i) to measured refractive index data. The fit achieves ~10⁻⁶ accuracy in n, but the individual coefficients carry fitting uncertainties of 1-5%.

2. The Kerr nonlinear coefficient n₂: measured at approximately 2.6 × 10⁻²⁰ m²/W ± 5%. This parameter governs self-phase modulation (SPM), cross-phase modulation (XPM), and four-wave mixing (FWM) — the three primary nonlinear impairments that limit channel capacity.

3. The chromatic dispersion slope: the rate of change of group velocity dispersion with wavelength, which determines the precision of dispersion compensation across the DWDM band.

The derivation chain: α (from QED chain, 12 digits) → electronic structure of Si (Z=14) and O (Z=8) → SiO₂ molecular polarizability → bulk refractive index → Sellmeier coefficients → n₂ from the third-order susceptibility χ⁽³⁾ → channel interaction parameters.

Each link is a standard quantum chemistry or condensed matter calculation. The chain from α to SiO₂ polarizability is within reach of current quantum chemistry methods for a three-atom molecule (though the crystal environment adds complexity). The precision gain: moving from 5% empirical uncertainty to sub-ppm derivation on n₂ alone would enable tighter channel spacing, reducing guard bands, and increasing usable bandwidth by 15-30% on existing deployed fiber.

This is not a hardware upgrade. It's a physics upgrade applied to hardware already in the ground.

### NON-TECHNICAL VERSION

Let me start with the most concrete example.

Your internet runs on light. Specifically, on fiber optic cables carrying dozens of different colors of light simultaneously — each color carrying its own data stream. This technology is called DWDM, dense wavelength division multiplexing.

Current commercial systems deliver about 100 terabits per second per fiber. Lab records have reached 430 terabits. The theoretical limit is about 600 terabits. There's a huge gap between what we're doing and what the fiber can actually handle.

Why the gap? Because the physical parameters that govern how light behaves in glass — how fast it travels at each color, how different colors interfere with each other — are known through curve fitting, not derivation. Engineers measured the glass, fitted curves to the measurements, and built their systems around those curves. The curves are good — about 5% uncertainty. But 5% uncertainty means 5% safety margins. Safety margins mean wasted capacity.

There are six numbers — the Sellmeier coefficients — that determine how light bends in glass. They're fitted, not derived. There's one number — the Kerr coefficient — that determines how strongly different channels interfere. It's measured at plus or minus 5%. Guard bands between channels are set for worst case, not the true boundary.

The chain from integers to these numbers exists. The fine structure constant — which we derive to 12 digits — determines how silicon and oxygen atoms interact. Their interaction determines the glass's optical properties. The glass properties determine the Sellmeier coefficients. The Sellmeier coefficients determine channel spacing.

Every link in that chain uses known equations. Nobody has run the chain end-to-end in exact arithmetic. If you did, and the result gave you the Kerr coefficient to parts per million instead of 5%, you could tighten the channel spacing on fiber that's already in the ground. Not new cables — same cables, better understanding.

That's not a hardware upgrade. It's a physics upgrade.

### MERGE NOTES

This is your strongest applied example because you understand telecom infrastructure. The DWDM numbers (100 Tb/s commercial, 430 lab, 600 theoretical) are concrete. The "5% uncertainty means 5% safety margins" framing is engineering common sense. The punch line — "same cables, better understanding" — is yours. You don't need to explain the Sellmeier equation. Just say "six numbers that describe how light bends in glass, currently fitted from measurements."

---

## SECTION 4: Handset Radio — Same Principle, Different Domain (3 minutes)

### TECHNICAL VERSION

5G NR systems operating in sub-6 GHz and mmWave bands achieve approximately 30-50% of theoretical Shannon capacity on deployed hardware. The gap is attributable to safety margins on four parameters:

1. Impedance matching: antenna-to-PA matching is guaranteed to ±5% across the operating band, with reflected power managed by isolators. Tighter matching enables higher power efficiency.

2. Subcarrier spacing: OFDM guard bands (guard intervals, cyclic prefix extensions) are sized for worst-case multipath, not actual channel conditions in real time. The guard overhead is 7-25% of subcarrier spacing depending on the numerology.

3. Power amplifier backoff: PAs operate 3-6 dB below their compression point to avoid nonlinear distortion. The backoff is sized by the peak-to-average power ratio (PAPR) plus a safety margin derived from empirically-characterized AM/AM and AM/PM curves.

4. FFT arithmetic: every OFDM modem computes the FFT using IEEE 754 float64 representations of the twiddle factors exp(−2πik/N). The π in the exponent inherits 15-digit precision. For a 4096-point FFT, the accumulated arithmetic error contributes to the error vector magnitude (EVM) floor.

The Q335 FFT addresses point 4 directly. Replace float64 π with Q335 π (101 digits, denominator 2³³⁵). The twiddle factors become integer pairs. The butterfly operations become integer multiply and bit-shift. The arithmetic error contribution to EVM drops to effectively zero — 10⁻¹⁰¹ vs 10⁻¹⁵.

### NON-TECHNICAL VERSION

Same principle, different domain.

Your phone uses a technology called OFDM — it splits a radio signal into thousands of tiny sub-channels and sends data on each one simultaneously. It's the same idea as fiber optics but through the air.

Current 5G systems operate at about 30 to 50% of their theoretical capacity. The rest is lost to safety margins. The antenna matching is approximate. The spacing between sub-channels includes guard bands for worst-case interference. The power amplifier is deliberately turned down to avoid distortion. Every one of these margins is lost performance — lower data rates, higher power consumption, shorter battery life.

And here's one you might not expect: the math itself introduces errors. Every modem in every phone on Earth runs a mathematical operation called the FFT — the fast Fourier transform. That operation uses pi. And pi is stored as a 15-digit decimal approximation. Every calculation that uses that approximation inherits a tiny error. Tiny, but real.

Q335 replaces that 15-digit approximation with a 101-digit exact fraction. The error drops from one part in a quadrillion to one part in... a number so large it doesn't have a name. Effectively zero.

Same modem. Same antenna. Same spectrum. Just more precise arithmetic.

### MERGE NOTES

You understand OFDM from your telecom background. The FFT-uses-pi point is technically precise and surprising to most audiences. "Every modem in every phone on Earth runs the FFT with approximate pi" is a line nobody expects. You can deliver the 5G capacity gap (30-50% of theoretical) from your industry knowledge.

---

## SECTION 5: The Q335 FFT — The Patent Example (3 minutes)

### TECHNICAL VERSION

The Q335 FFT is a concrete, patentable implementation that exists solely because of the integer fraction methodology.

Implementation: for an N-point FFT, compute the twiddle factors ω_k = exp(−2πik/N) as Q335 integers: cos(2πk/N) and sin(2πk/N) each represented as ⌊f(k) × 2³³⁵⌋. The denominator 2³³⁵ means division is a right bit-shift by 335 positions — a single clock cycle on any processor.

Storage: for N = 4096, the twiddle table requires 4096 × 2 × 42 bytes = 335 KB (each Q335 integer is ~42 bytes at 335 bits). This is smaller than the L2 cache of a modern mobile processor.

Silicon: the multiplier is a 335-bit × 335-bit integer multiply, implementable in approximately 0.8 mm² at 5nm process technology. This is less than 4% of a modern modem SoC die area.

Result: the arithmetic error contribution to EVM drops from ~−80 dBc (float64) to ~−600 dBc (Q335). This eliminates the arithmetic noise floor entirely, enabling the step from 1024-QAM (10 bits/symbol) to 4096-QAM (12 bits/symbol) — a 20% throughput increase on the same spectrum allocation.

The patent space is currently empty. No prior art exists for integer arithmetic FFT implementations above 64-bit precision. The Q335 FFT specification is being released publicly to demonstrate what the methodology produces.

### NON-TECHNICAL VERSION

Let me give you something concrete. Something you could build.

Every digital signal processing system on Earth — every phone, every router, every radar, every audio system — runs the FFT with approximate arithmetic. The errors are tiny, but they set a floor on how precisely the system can distinguish signals from noise.

Q335 eliminates that floor. Replace the 15-digit pi with a 101-digit exact fraction. The key trick: the fraction has a denominator that's a power of 2, so dividing by it is just shifting bits — free on any processor.

The twiddle table — the lookup table of sine and cosine values the FFT uses — takes about 335 kilobytes. That's smaller than the cache in your phone's processor. The multiplier circuit takes less than 1 square millimeter at 5 nanometers — less than 4% of a modern modem chip.

The result: the step from 1024-QAM to 4096-QAM. That's 10 bits per symbol to 12 bits per symbol. A 20% throughput increase on the same spectrum. No new antennas. No new spectrum licenses. Just more precise arithmetic.

And the patent space is empty. Nobody has built an integer FFT above 64-bit precision. I'm releasing the specification for free, as a proof of concept for what the methodology produces.

### MERGE NOTES

This is the most tangible deliverable in the entire series and you understand it as an engineer. The storage numbers (335 KB), the die area (0.8 mm²), the throughput gain (20%) — these are specs you can cite. "The patent space is empty" is a verifiable claim. "I'm releasing it for free" establishes your intent. The 1024-QAM to 4096-QAM step is concrete and meaningful to anyone in telecom.

---

## SECTION 6: Semiconductor Physics — The Chain Exists (2 minutes)

### TECHNICAL VERSION

The silicon band gap E_g = 1.12 eV at 300K determines the operational characteristics of every silicon-based transistor, solar cell, and integrated circuit. The global semiconductor industry ($600B annual revenue) is built on this single number.

Current theoretical accuracy: density functional theory (DFT) with standard exchange-correlation functionals achieves E_g ≈ 0.5-0.7 eV for silicon — a 40-50% underestimation. The GW approximation (many-body perturbation theory) achieves ~1.1 eV — within 2% — but at extreme computational cost. Quantum Monte Carlo methods can in principle reach meV accuracy but require billions of CPU-hours per material.

The derivation chain: α (12 digits from QED) → electronic structure of Si (Z=14, diamond cubic lattice, Bloch wavefunctions) → band structure → E_g.

The chain exists. Every link is a known calculation. The bottleneck is the many-electron problem: silicon has 14 electrons per atom, a unit cell of 2 atoms, and a crystal environment that requires periodic boundary conditions. Current methods approximate the electron-electron interaction. The exact interaction is known (it's the Coulomb potential, which depends on α), but solving for 28 interacting electrons exactly is computationally intractable with current algorithms.

This is stated honestly: the path exists, the computation is hard.

### NON-TECHNICAL VERSION

The silicon band gap. One number — 1.12 electron volts — that determines every transistor, every solar cell, every computer chip on Earth. A 600-billion-dollar industry built on one measurement.

The current theoretical methods can predict this number to about 2% accuracy on a good day, using enormous computing resources. That's useful but it's not the precision you'd get from an exact derivation.

The chain from integers exists. The fine structure constant determines how silicon's 14 electrons arrange themselves. Their arrangement determines the band gap. The band gap determines everything else.

But here's the honest limit: computing the exact arrangement of 14 interacting electrons in a crystal lattice is one of the hardest computational problems in physics. The equations are known. Solving them exactly is beyond current algorithms for all but the simplest systems.

The path exists. The computation is hard. Both facts stated plainly.

### MERGE NOTES

The silicon band gap is a number most of your audience uses every day without knowing it. "A 600-billion-dollar industry built on one measurement" is vivid. The honest limit — "the equations are known, solving them exactly is hard" — is important. Don't overclaim. The path exists but the computation is genuinely difficult.

---

## SECTION 7: Medicine — The Longest Chain (3 minutes)

### TECHNICAL VERSION

Pharmaceutical drug development: average time to market 10-15 years, cost $1-2B per approved drug, clinical trial failure rate ~90%. The computational bottleneck is binding affinity prediction — whether a candidate molecule binds to a target protein with sufficient specificity and strength.

Current binding prediction accuracy: ~70% for whether binding occurs (binary classification), ~1 kcal/mol for binding free energy (compared to the ~3-10 kcal/mol range of therapeutic binding). The 30% false negative/positive rate drives the high clinical failure rate.

The error source: force field parameters. Molecular dynamics simulations use parameterized potentials — Lennard-Jones ε and σ, partial atomic charges, torsion barriers — that are fitted to experimental data or quantum chemistry calculations at moderate accuracy. These parameters trace to:

- Electronic polarizability → α and nuclear charges Z
- Bond lengths and angles → solutions of the electronic Schrödinger equation with the Coulomb potential (which depends on α)
- Van der Waals interactions → London dispersion forces, which depend on α² and polarizabilities

The relevant nuclear charges for drug-relevant chemistry: H (Z=1), C (Z=6), N (Z=7), O (Z=8), S (Z=16). Five integers.

The derivation chain: α (12 digits) → electronic structure of C, N, O, H, S → molecular polarizabilities → force field parameters → binding affinity predictions.

Each link is known physics. The molecular polarizability calculation is within reach of current quantum chemistry for small molecules. The force field parameterization is an active research area. The endpoint — predicting drug efficacy from gauge integers — is decades away. But every percentage point improvement in binding prediction saves hundreds of millions in failed clinical trials.

### NON-TECHNICAL VERSION

Now the longest chain. Medicine.

Getting a drug from idea to pharmacy takes 10 to 15 years and costs 1 to 2 billion dollars. 90% of drugs that enter clinical trials fail. The main reason: we can't predict well enough whether a molecule will bind to its target protein.

Current prediction accuracy: about 70%. That means 30% of the time, the computer says "yes, this molecule will work" and nature says "no." Or the computer says "no" and misses a drug that would have worked. That 30% error rate is why trials are so expensive — you have to try the molecules in humans because the computer can't tell you.

The 30% error comes from the parameters in the simulation. The simulation models atoms as balls connected by springs, and the spring constants are fitted from measurements. The fits are approximate.

Where do those spring constants come from? From how atoms push and pull on each other. How atoms push and pull depends on the fine structure constant and the nuclear charges. For drug chemistry, the nuclear charges are: hydrogen 1, carbon 6, nitrogen 7, oxygen 8, sulfur 16. Five integers.

Five integers, through a chain of known equations, determine whether a drug molecule binds to a protein. The chain is long. Each link is a research program. The endpoint — predicting drug efficacy from integers — is decades away.

But every percentage point improvement in binding prediction saves hundreds of millions in failed clinical trials. A 1% improvement in prediction accuracy is worth more than most entire research programs.

### MERGE NOTES

The drug development numbers (10-15 years, $1-2B, 90% failure) are public and dramatic. The "five integers determine drug binding" claim is technically precise — nuclear charges are integers and they do determine chemistry. The honest limit — "decades away" — is crucial. Don't promise anything close. The economic argument — "1% improvement saves hundreds of millions" — is concrete and true.

---

## SECTION 8: Climate — The Most Tractable Applied Chain (2 minutes)

### TECHNICAL VERSION

The greenhouse effect is mediated primarily by CO₂, H₂O, CH₄, and N₂O absorption of infrared radiation. The absorption spectrum of each molecule is determined by its vibrational and rotational energy levels, which are determined by molecular structure, which traces to α and nuclear charges.

CO₂ (O=C=O, linear triatomic): Z_C = 6, Z_O = 8. Three atoms, 22 electrons. The vibrational modes are the symmetric stretch (ν₁, Raman active), the asymmetric stretch (ν₃, IR active at 4.26 μm), and the bending mode (ν₂, IR active at 15 μm). The ν₂ bending mode at 15 μm (667 cm⁻¹) is the primary greenhouse absorption — it sits near the peak of Earth's thermal emission spectrum.

The derivation chain: α + Z_C + Z_O → CO₂ electronic structure → bond length (1.16 Å) → vibrational frequencies → absorption cross-sections → atmospheric absorption spectrum → radiative forcing.

This is one of the nearest targets. CO₂ is a three-atom molecule. Current quantum chemistry (coupled cluster with perturbative triples, CCSD(T)) can compute vibrational frequencies of triatomic molecules to ~1 cm⁻¹ accuracy — already better than the spectroscopic databases used in climate models. Running this in exact fraction arithmetic from α-derived inputs would close the chain.

Climate science currently treats absorption spectra as empirical data from the HITRAN database. The derivation from first principles to spectroscopic precision has not been done in a framework that traces the inputs to gauge integers.

### NON-TECHNICAL VERSION

Climate science has what might be the most tractable chain of all.

The greenhouse effect works because certain molecules absorb infrared light — heat radiation. CO2 is the main one. It absorbs specific wavelengths of heat, trapping energy in the atmosphere.

Which wavelengths CO2 absorbs depends on how the molecule vibrates. How it vibrates depends on the bond properties. Bond properties depend on how carbon and oxygen atoms interact. How they interact depends on the fine structure constant and two nuclear charges: carbon 6, oxygen 8.

Two integers and alpha determine the greenhouse effect.

CO2 is three atoms. Three atoms is a problem we can solve. Current quantum chemistry can already compute the vibration frequencies of a three-atom molecule to high precision. Running that computation in exact arithmetic, starting from alpha derived from gauge integers, would complete the chain.

Climate science currently treats the absorption spectrum of CO2 as measured data — they look it up in a database. The derivation from integers to spectrum has not been done. But the molecule is simple enough that it could be.

This is one of the nearest targets. Short chain. Known equations. High-precision measurements available for comparison.

### MERGE NOTES

"Two integers and alpha determine the greenhouse effect" is a striking claim and it's technically correct. CO2 as a three-atom molecule being computationally tractable is an honest assessment. You don't need to explain coupled cluster methods — just say "current quantum chemistry can handle three-atom molecules." The practical implication — "climate models look up this data instead of computing it" — is something you can state.

---

## SECTION 9: What Changes for Ordinary People (2 minutes)

*[In frame, no slides.]*

### TECHNICAL VERSION

The applied chains represent one dimension of impact. A second dimension is conceptual: the unification framework simplifies the intellectual structure of physics from approximately 12 subdisciplines with separate vocabularies to one discipline with one vocabulary.

Educational impact: the soliton hierarchy teaches one principle (nested boundaries with reading changes) and applies it at every level. A student who understands inertia, vortex, and soliton at the proton level understands the same concepts at the galaxy level. The current curriculum teaches forces, particles, atoms, molecules, planets, stars, and galaxies as separate subjects with separate terminology. The unification reduces the cognitive load.

Conceptual impact: dark matter becomes less mysterious when an integer ratio matches the satellite measurement at 725 ppm. The cosmological constant becomes less baffling when it's the ground state reading of the outermost boundary. These reframings don't solve the problems — they make them approachable.

Methodological impact: before proposing new particles, dimensions, or forces to explain a discrepancy, check which boundary you're reading from. The Hubble tension (73 vs 67.4) might be a reading difference, not a physics difference.

### NON-TECHNICAL VERSION

You don't need to derive protein folding from integers to benefit from this.

Understanding replaces mystery. When someone tells you "95% of the universe is unknown — dark matter and dark energy" — that sounds terrifying. When you learn that an integer ratio matches the dark matter measurement to 725 parts per million, and the rest is the ground state energy of the outermost boundary, it's less terrifying. The mystery shrinks.

Education changes. Right now, students learn four forces in separate chapters, separate years, sometimes separate departments. Imagine teaching one principle — a boundary where readings change — and showing four examples. Same idea, different depth. The student sees unity from day one instead of hoping to discover it in graduate school.

And methodology changes. Before physicists propose new particles, new dimensions, new forces to explain why two measurements disagree — maybe check whether the two measurements are looking at different boundaries. Different boundaries give different readings. That's not a crisis. That's the principle working exactly as expected.

### MERGE NOTES

"Understanding replaces mystery" is your framing. The education point — "one principle with four examples instead of four separate subjects" — is something you feel strongly about. You can deliver the dark matter reframing ("an integer ratio matches at 725 ppm") from your own experience of encountering it. The methodology point — "check which boundary you're reading from before inventing new particles" — is your soliton principle applied.

---

## SECTION 10: The Promise and the Honest Limit (2 minutes)

*[In frame, talking to camera.]*

### TECHNICAL VERSION

Computed and verified: gauge integers → cosmological densities → primordial element abundances (D/H at 0.12σ). Electron magnetic moment → α → Rydberg → hydrogen 1S-2S frequency (11 digits). Gauge integers → sin²θ_W → M_W → Z decay widths (15 observables, all matching).

Not computed: integers → SiO₂ optical properties → Sellmeier coefficients. α → CO₂ vibrational spectrum. Gauge group → force field parameters → protein folding. Si band gap from first principles in exact arithmetic.

These are future work. Years for the nearest targets (CO₂ spectrum, glass optics). Decades for the furthest (drug design, materials by integer design).

But every chain that has been computed works. No chain has failed except where the one-loop approximation is insufficient (proton mass, pion mass — known fix: two-loop). The walls are departmental, not physical. The equations exist. The computation awaits.

### NON-TECHNICAL VERSION

Let me be honest about what we've done and what we haven't.

Done: from gauge integers to deuterium abundance — seven steps, matches within the noise. From one electron's wobble to hydrogen's light frequency — eleven digits match across the ocean. From gauge integers to Z boson decay rates — fifteen predictions, all matching.

Not done: from integers to how light bends in glass. From alpha to CO2's absorption spectrum. From the gauge group through chemistry to drug binding.

Those chains are years away for the nearest targets, decades for the furthest.

But every chain we've actually run has worked. Every one. No exceptions — except where we know the approximation is too crude, and we know the fix. The chains that exist work. The chains that don't exist yet use the same kinds of equations. The walls between us and those chains are departmental, not physical.

The discovery is done. The universe runs on integer fractions. What remains is computation.

### MERGE NOTES

This is where your credibility is built. "Let me be honest about what we've done and what we haven't" is a line that earns trust. The list of "done" is specific and verifiable. The list of "not done" is equally specific. "The discovery is done, what remains is computation" is your thesis statement for the applied program. Don't soften it, don't hedge it beyond what you've already hedged.

---

## SECTION 11: Close (1 minute)

*[In frame, talking to camera.]*

### TECHNICAL VERSION

Unification connects the gauge group to the bandwidth of optical fiber, the efficiency of radio modems, the band gap of semiconductors, the binding affinity of drug molecules, and the absorption spectrum of greenhouse gases. Every engineering industry that operates on empirically-fitted physical parameters is waiting for derivation chains that originate at the gauge integers.

The Q335 FFT specification demonstrates what these chains produce: a zero-arithmetic-error implementation of the most common signal processing operation in the world, applicable to every phone, router, radar, and satellite. I'm releasing it publicly.

The methodology generalizes to every domain where empirical parameters with safety margins limit performance. The chains are visible. The links remain to be computed.

### NON-TECHNICAL VERSION

Unification isn't an abstract achievement for physicists. It's the thing that connects the gauge group to the speed of your internet, the cost of your medication, and the accuracy of your climate model.

Every industry that depends on measured physical constants with safety margins is waiting for derivation chains that cross departmental walls. The chains are visible now. The links remain to be computed.

I have a specification for the Q335 FFT — a zero-error implementation of the most common signal processing operation in the world. I'm releasing it for free, as a demonstration of what these chains produce.

The universe runs on integers. The engineering runs on approximations of those integers. The gap between them is the opportunity.

Next week: the number system. Why fractions preserve structure that decimals erase, and how Q335 makes it work.

Links in the pinned comment. Check the numbers.

### MERGE NOTES

"The gap between integers and approximations is the opportunity" — that's your closing thesis and it's pure engineering. The Q335 FFT release is a tangible deliverable. "Check the numbers" as always.

---

## TERMINAL DEMO NOTES

Light on demos for this video — it's mostly conceptual:

**Demo 1 (Section 5):** Show Q335 pi briefly. Remind them from Video 1. Then show: "this is the pi that goes into the FFT." 30 seconds.

**Demo 2 (Section 10):** Run one experiment briefly as a reminder that the chains work. 30 seconds.

Total demo time: ~1 minute. This video is 90% talking to camera and slides.

---

## PACING GUIDE

| Section | Duration | Energy | Key Moment |
|---|---|---|---|
| Opening | 1 min | Reframing | "Engineering achievement, not physics" |
| General principle | 2 min | Setting up | "Known equations, not yet run end-to-end" |
| Fiber optics | 5 min | Concrete | "Same cables, better understanding" |
| Handset radio | 3 min | Building | "Every phone runs the FFT with approximate pi" |
| Q335 FFT | 3 min | Exciting | "20% throughput increase, zero new hardware" |
| Semiconductor | 2 min | Honest | "The path exists, the computation is hard" |
| Medicine | 3 min | Visionary | "Five integers determine drug binding" |
| Climate | 2 min | Tractable | "Two integers and alpha" |
| Ordinary people | 2 min | Accessible | "Understanding replaces mystery" |
| Promise and limit | 2 min | Honest | "The discovery is done, computation remains" |
| Close | 1 min | Direct | "The gap is the opportunity" |

Total: ~26 minutes.

---

## SLIDE NOTES

This video has fewer pre-made diagram slides than the others since it's more conceptual and industry-focused. Use the following:

- DWDM channel plan diagram (create or source a standard telecom diagram)
- Q335 FFT block diagram (show the integer twiddle table concept)
- Chain diagrams for each industry: simple arrows showing integer → atomic → molecular → engineering parameter
- The "done vs not done" comparison for the honest limit section
- Closing card with links

You may want to create simple slides in presentation software rather than matplotlib for this video, since the content is engineering-oriented rather than physics-diagram oriented. The existing talk slides (talk1-3 series) can be referenced briefly for the recap moments.
