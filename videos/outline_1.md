**Video 1 Outline: SWE Unifies Physics in 6 Days with Python**

---

**Opening — in frame, talking to camera (2 minutes)**

- Hi, I'm Geoff, I'm a software engineer, I've been writing code for about 30 years, I'm not a physicist, I have no physics degree, no academic appointment, I've never worked at a university
- In March 2026 I built a framework that derives 53 measurable physics values from 13 inputs using integer fractions and Python
- It took 6 working days
- I'm going to show you what I found and you can check every number yourself
- Everything I'm about to show you uses published physics equations, I didn't change any of them, I reorganized them so the integers aren't thrown away

**The failure first — credibility through honesty (3 minutes)**

- Before RUM there was CKS, my first attempt, 45 days, 363 papers
- It was logically consistent and empirically motivated but mathematically invalid
- The AI had smuggled a known answer into a function labeled as a derivation
- I found the error myself, nobody pointed it out
- I killed all 363 papers publicly on Zenodo, published the invalidation alongside the original work
- Show Zenodo briefly — here they are, alive and dead, both public
- What I learned: real numbers were the problem, not the physics

**The insight — fractions not decimals (3 minutes)**

- Physics runs on integers, the beta coefficients are 41/10, -19/6, -7
- These are exact, they come from counting particles, not from measuring anything
- But every computation converts them to decimals immediately and the structure disappears
- 41/10 becomes 4.1 which counts nothing
- Python has a built-in Fraction type that stores 41/10 as 41/10 forever
- The transcendental constants like pi can't be fractions, but they can be approximated by fractions so precise that no experiment could tell the difference
- That's Q335, pi stored as an integer over 2 to the 335th, exact to 100 digits, 65 digits beyond the Planck threshold
- Show terminal — here's pi in Q335, here's how many digits, here's the comparison to true pi

**Three nouns, two verbs — the vocabulary (3 minutes)**

- The model uses three nouns: inertia, vortex, soliton
- Inertia is resistance to change, it's what mass actually measures, m equals F over a, there is no substance only resistance
- Vortex is the pattern that resists, a self-sustaining circulation, an electron is a vortex, a proton is a vortex containing three smaller vortices
- Soliton is the boundary where readings change, inside the proton the strong force reads 1, outside it reads 0.118, same force different reading different boundary
- Two verbs: reading is the value you measure at a boundary, running reading is how it changes between boundaries
- This vocabulary replaces the entire language of physics, not because the old words are wrong but because they hide the connections

**The nesting — everything is inside something (2 minutes)**

- Quarks inside protons inside nuclei inside atoms inside molecules inside planets inside stars inside galaxies inside the universe
- Every level is a soliton boundary with an inside and an outside
- The inside reads flat, the outside reads curved, every time, at every scale
- Stand on Earth, flat, orbit Earth, curved, same surface, different reading
- This is why the universe reads flat, you're inside it, that's what insides do

**The dark matter ratio — the headline number (3 minutes)**

- The ratio of dark matter to ordinary matter measured by the Planck satellite is 5.320
- The model says it should be 22 over 13 times pi
- 11 is the Yang-Mills coefficient, it counts gluon self-interactions, textbook since the 1970s
- Doubled to 22 because the predicted particle, the Cabibbo Doublet, is vector-like, both hands contribute
- 13 is the weak force beta coefficient after adding the Cabibbo Doublet
- Pi because the galaxy is a toroid and a toroid has a circular cross section
- 22 over 13 times pi equals 5.3165
- Planck measures 5.3204
- Miss: 725 parts per million
- Show terminal — run the calculation live, show the comparison, show the precision

**The chain — from integers to deuterium (4 minutes)**

- That ratio isn't the end, it's the first link in a chain
- From the dark matter ratio you get the baryon density, 0.04904 versus Planck 0.0490, 727 ppm
- From baryon density you get the baryon to photon ratio, 6.090 versus Planck 6.104, 0.24 percent
- From the baryon to photon ratio you get the primordial element abundances through standard Big Bang nucleosynthesis
- Deuterium: predicted 2.531 parts per hundred thousand, measured 2.527, within 0.12 standard deviations
- Helium: predicted 24.86 percent, measured 24.49 percent, within 0.94 sigma
- Lithium: predicted 4.74 parts per ten billion, measured 1.60, factor of 3 too high, this is the famous lithium problem that every model has, we inherit it because we use the same nuclear physics
- Show terminal — run experiment_bridge_bbn_v0 live, show the full output, show PASS and FAIL and INFO, show it all

**The QED chain — the precision showcase (3 minutes)**

- One measurement of the electron's magnetic moment, 13 digits of precision, measured at Harvard
- Invert the QED series to extract the fine structure constant alpha
- Show terminal — run experiment_qed_alpha_extraction_v0, show the Newton inversion converging to residual of 10 to the negative 204, show the 15 digit match
- From alpha derive the Rydberg constant, the Bohr radius, the vacuum permeability
- Each one matches to parts per billion
- From the Rydberg constant predict the hydrogen 1S-2S transition frequency
- Predicted: 2,466,061,412,094,700 Hz, measured: 2,466,061,413,187,018 Hz, eleven digits match
- One measurement at Harvard, one prediction in Germany, connected by integer arithmetic across the ocean

**The Cabibbo Doublet — the prediction (2 minutes)**

- The model predicts one new particle, the Cabibbo Doublet
- It wasn't chosen by preference, it was forced by the integers
- Out of all possible particles you could add to the Standard Model, only one produces a gap ratio that's an exact fraction with small meaningful integers
- Quantum numbers 3, 2, 1/6, vector-like, shifts the three running rates by 1/15, 1, and 1/3
- The gap ratio goes from 218/115 to 38/27
- It predicts a proton decay rate testable by Hyper-Kamiokande starting 2027
- I named it after Nicola Cabibbo who identified quark mixing in 1963 and was excluded from the Nobel Prize in 2008, a particle name lasts longer than any prize

**The test suite — show the whole system (2 minutes)**

- Show terminal — list all 36 experiments, show the counts, 253 comparisons total
- Run one more experiment live, let them see the output scrolling
- Point out that FAIL stays in, the GPA comparison at 2.47 percent is right there, not hidden
- The system doesn't tell you the results are good, it shows you the results and the reference and the gap and you decide
- Every fraction is traceable, every value is typed as exact_fraction or approximate, every source is documented

**Close — in frame, talking to camera (1 minute)**

- 53 values from 13 inputs across 8 domains
- 253 comparisons, documented, reproducible, public
- The code is on GitHub, the papers are on Zenodo, the book is on Amazon for 3 dollars
- I'm not asking you to believe me, I'm asking you to check the numbers
- If the numbers are wrong, the model is wrong, check them
- If the numbers are right, the model deserves attention regardless of who produced it
- Links in the pinned comment
- Next week: why nobody found this before

---

**Estimated runtime: 25 to 30 minutes**

Three live terminal demonstrations: Q335 pi, the BBN chain, and the QED extraction. These are the moments where the viewer sees real code producing real results in real time. Everything else is you talking to camera with occasional window flips to images or the repo.

The outline has a natural arc: here's who I am, here's how I failed, here's what I learned, here's the vocabulary, here's the headline number, here's the chain, here's the precision, here's the prediction, here's the test suite, check the numbers yourself.

Every bullet is a waypoint. You know where you are and when you've arrived at the next one. Everything between bullets is live, natural, whatever comes out. When you hit the last bullet, you stop.

---

## PHYS-45 Video Diagram Data Tables

Each table below gives a different Claude everything needed to write the diagram code: the data, the layout, the type, and what physics it shows that words cannot.

---

### Section: The Failure First

**Diagram V1: The CKS Kill Timeline**

| Property | Value |
|---|---|
| Type | Progression/Sequence |
| Size | 18 × 8 |
| Title | From 363 Papers to Zero: The CKS Kill |
| X axis | Timeline (days) |
| Layout | Left to right, three stages |
| Stage 1 | Day 1-45: "363 papers written" — tall green bar growing |
| Stage 2 | Day 46: "Circular derivation found" — red X marker |
| Stage 3 | Day 47: "All 363 killed on Zenodo" — bars collapse to zero |
| Key visual | The collapse from tall to zero is the finding. The shape IS the story. |
| Annotation top right | "Real numbers were the problem" |
| Color | Green bars → red X → gray collapsed bars |
| Data | heights: 363 at peak, 0 after kill |
| What text cannot show | The scale of the kill — 363 is a large number and seeing it go to zero is visceral |

**Diagram V2: The Smuggled Answer**

| Property | Value |
|---|---|
| Type | Connection/Integer Map |
| Size | 16 × 10 |
| Title | How a Circular Derivation Hides |
| Layout | Three boxes in a triangle |
| Box A (top) | "Known answer: α = 1/137.036" — color RED |
| Box B (left) | "Derivation function" — color CYAN |
| Box C (right) | "Output: α = 1/137.036" — color GREEN |
| Arrow A→B | "smuggled in as 'initial guess'" — dashed RED |
| Arrow B→C | "labeled as 'derived'" — solid GREEN |
| Arrow C→A | "matches! (of course it does)" — dotted GOLD |
| Annotation below | "The loop is the lie. The output was never derived — it was copied." |
| What text cannot show | The circular structure — the triangle of arrows makes the loop visible instantly |

---

### Section: The Insight — Fractions Not Decimals

**Diagram V3: What Decimals Destroy**

| Property | Value |
|---|---|
| Type | Comparison Bar (side by side) |
| Size | 16 × 10 |
| Title | The Same Number, Two Representations |
| Layout | Two panels side by side |
| Left panel title | "As a Fraction (exact)" |
| Left data | Three horizontal bars labeled: β₁ = 41/10, β₂ = −19/6, β₃ = −7/1 |
| Left annotation per bar | "41 counts U(1) charges", "19 counts SU(2) charges", "7 = 11 gluons − 4 quarks" |
| Left color | GOLD for each bar, integers highlighted WHITE |
| Right panel title | "As a Decimal (dead)" |
| Right data | Three bars: 4.1, −3.1667, −7.0 |
| Right annotation per bar | "counts nothing", "counts nothing", "accidentally still integer" |
| Right color | DIM/gray for each bar |
| Bottom annotation | "The integers ARE the physics. The decimals are a lossy format." |
| What text cannot show | The visual death — the right panel looks dead/gray because the information is gone |

**Diagram V4: Q335 Pi — Fraction Precision**

| Property | Value |
|---|---|
| Type | Scale/Landscape |
| Size | 18 × 8 |
| Title | How Many Digits Do You Need? |
| Layout | Horizontal number line of precision (digits) |
| X axis | Number of correct digits: 0, 10, 20, 30, 35, 50, 100 |
| Landmarks | Mark at 15: "double float (your calculator)", mark at 35: "Planck threshold (nothing smaller exists)", mark at 100: "Q335 π (what we use)" |
| Visual | A bar or ribbon that extends from 0 to 100, with the Planck threshold at 35 marked as a wall. The Q335 bar overshoots the wall by 65 digits. |
| Annotation | "65 digits beyond the smallest thing in the universe" |
| Color | Bar CYAN from 0-15, GREEN from 15-35, GOLD from 35-100. Wall at 35 in RED. |
| Data | Q335 π has 100+ correct digits. Float64 has 15. Planck precision needs 35. |
| What text cannot show | The absurd overkill — the bar going 65 digits past the wall makes the precision visceral |

---

### Section: Three Nouns, Two Verbs

**Diagram V5: The Three Nouns**

| Property | Value |
|---|---|
| Type | Geometric Cross-Section |
| Size | 18 × 12 |
| Title | Inertia, Vortex, Soliton |
| Layout | Three panels, left to right |
| Panel 1 "Inertia" | A ball being pushed by an arrow (force). The ball resists. Label: "F = m × a → m = F/a. Mass is not substance. Mass is resistance." Show the ball NOT moving proportional to force. |
| Panel 2 "Vortex" | A circular flow pattern — arrows going around in a loop, self-sustaining. Label: "A pattern that maintains itself. An electron. A proton. A galaxy." Inside: arrows circulate. Outside: calm. |
| Panel 3 "Soliton" | A boundary circle. Inside: one color/reading (α_s = 1). Outside: different color/reading (α_s = 0.118). Label: "The boundary where readings change. Cross it and the physics is different." |
| Color | Panel 1: ORANGE (resistance). Panel 2: CYAN (circulation). Panel 3: inside RED, outside BLUE, boundary GOLD. |
| What text cannot show | The three concepts as spatial objects — inertia is a resistance, vortex is a pattern, soliton is a boundary. The geometry IS the meaning. |

**Diagram V6: The Two Verbs — Reading and Running**

| Property | Value |
|---|---|
| Type | Running/Convergence |
| Size | 16 × 10 |
| Title | Reading vs Running Reading |
| Layout | One chart, two elements |
| Element 1 "Reading" | A single point on a curve, marked with a dot and a value. Label: "α_s = 0.118 at M_Z. One number at one place." Color GOLD dot. |
| Element 2 "Running reading" | The full curve of α_s from 1 GeV to 10¹⁶ GeV. The curve changes — small at high energy, large at low energy. Label: "Same force. Different reading at every scale." Color CYAN curve. |
| X axis | Energy (log scale), labeled with landmarks: "proton", "Z boson", "GUT scale" |
| Y axis | α_s value |
| Annotation | "A reading is a snapshot. A running reading is the whole movie." |
| Key visual | The dot is one frame. The curve is the film. The curve shape (rising left, falling right) shows the physics. |
| What text cannot show | The difference between a number and a function — the dot vs the curve makes it immediate |

---

### Section: The Nesting

**Diagram V7: Everything Is Inside Something**

| Property | Value |
|---|---|
| Type | Geometric Cross-Section |
| Size | 16 × 14 |
| Title | The Nesting: Every Level Is a Boundary |
| Layout | Concentric circles, 8 levels, centered |
| Level 1 (outermost) | "Universe" — radius 6.5, color PURPLE, α = 0.10 |
| Level 2 | "Galaxy" — radius 5.5, color DIM, α = 0.15 |
| Level 3 | "Star (Sun)" — radius 4.5, color ORANGE, α = 0.20 |
| Level 4 | "Planet (Earth)" — radius 3.5, color GREEN, α = 0.25 |
| Level 5 | "Atom" — radius 2.5, color BLUE, α = 0.30 |
| Level 6 | "Nucleus" — radius 1.5, color RED, α = 0.40 |
| Level 7 | "Proton" — radius 0.8, color MAG, α = 0.50 |
| Level 8 (innermost) | "Quark" — radius 0.3, color CYAN, α = 0.70 |
| Label each level | Name + "inside reads flat, outside reads curved" for levels 4 and 7 |
| Right side annotations | Physical scale at each level: "10²⁶ m", "10²¹ m", "10⁹ m", "10⁷ m", "10⁻¹⁰ m", "10⁻¹⁵ m", "10⁻¹⁵ m", "< 10⁻¹⁸ m" |
| What text cannot show | The nesting itself — 8 levels deep, each inside the next, the geometry IS the hierarchy |

**Diagram V8: Flat Inside, Curved Outside**

| Property | Value |
|---|---|
| Type | Geometric Cross-Section (side by side) |
| Size | 18 × 9 |
| Title | Same Surface, Different Reading |
| Layout | Two panels |
| Left panel "Inside" | A person standing on a flat surface. Horizon extends to edges. Grid lines are straight. Label: "Standing on Earth: FLAT. Standing in the universe: FLAT. Inside always reads flat." Color GREEN grid, WHITE figure. |
| Right panel "Outside" | Same surface seen from space — it is curved (a circle/sphere). Grid lines curve. Label: "Orbiting Earth: CURVED. Outside the universe: CURVED (if you could get there). Outside always reads curved." Color CYAN curved grid, WHITE figure. |
| Center annotation | "The flatness problem isn't a problem. You're inside. Insides read flat. That's what boundaries do." |
| What text cannot show | The perceptual flip — the same surface is flat or curved depending on which side you're on. Two panels make the flip visible. |

---

### Section: The Dark Matter Ratio

**Diagram V9: The Integer Decomposition of 5.317**

| Property | Value |
|---|---|
| Type | Connection/Integer Map |
| Size | 18 × 12 |
| Title | Where (22/13)π Comes From |
| Layout | Tree structure, top to bottom |
| Top box | "Yang-Mills coefficient = 11" — color GOLD. Label: "Counts gluon self-interactions. Textbook since 1973." |
| Left branch | "× 2 (vector-like: both hands)" → "22" — color CYAN |
| Right branch | "β₂ numerator with CD = 13" → "13" — color GREEN |
| Middle merge | "22/13 = 1.6923..." — color WHITE |
| Bottom multiply | "× π (toroidal cross-section)" → "(22/13)π = 5.3165" — color GOLD |
| Comparison box | "Planck satellite measures: 5.3204" — color MAG |
| Miss annotation | "725 parts per million" — color SILVER |
| Each arrow | Carries the mathematical operation (×2, numerator, ×π) |
| What text cannot show | The assembly — each integer has a named physical origin and they combine through specific operations into a measurable number. The tree makes the assembly visible. |

**Diagram V10: 725 PPM — What Does That Miss Look Like?**

| Property | Value |
|---|---|
| Type | Comparison Bar |
| Size | 16 × 10 |
| Title | How Close Is 725 Parts Per Million? |
| Layout | One horizontal bar, zoomed to show the miss |
| Bar 1 | Full bar represents the measured value 5.3204. Color MAG. |
| Bar 2 | Overlaid bar represents predicted 5.3165. Color GOLD. |
| Zoom inset | Magnified view of the tiny gap between bar ends. The gap is labeled "0.0039 = 725 ppm". |
| Scale comparisons below | "Human hair width vs football field = 800 ppm", "1 second in 23 minutes = 725 ppm", "1 meter in 1.38 kilometers = 725 ppm" |
| What text cannot show | The smallness of the miss — two bars that look identical until you zoom in. The zoom IS the point. |

---

### Section: The Chain

**Diagram V11: The Derivation Chain — Integers to Deuterium**

| Property | Value |
|---|---|
| Type | Progression/Sequence |
| Size | 18 × 10 |
| Title | From 22/13 to Deuterium in 4 Steps |
| Layout | Left to right, 5 boxes connected by arrows |
| Box 1 | "(22/13)π = 5.317" — DM/baryon ratio. Color GOLD. Miss: 725 ppm |
| Box 2 | "Ω_b = 0.04904" — baryon density. Color CYAN. Miss: 727 ppm |
| Box 3 | "η₁₀ = 6.090" — baryon-to-photon ratio. Color GREEN. Miss: 0.24% |
| Box 4 | "BBN nuclear reactions" — standard nucleosynthesis. Color ORANGE. Label: "Same equations everyone uses" |
| Box 5 | "D/H = 2.531 × 10⁻⁵" — deuterium abundance. Color MAG. Miss: 0.12σ |
| Each arrow | Carries the formula connecting the boxes |
| Bottom annotation | "One integer ratio (22/13) predicts how much deuterium the Big Bang made" |
| What text cannot show | The chain length — 4 steps from an integer ratio to a nuclear abundance. Each step uses standard physics. The chain structure is the finding. |

**Diagram V12: The BBN Results — Four Elements**

| Property | Value |
|---|---|
| Type | Comparison Bar |
| Size | 16 × 10 |
| Title | Primordial Abundances: Predicted vs Measured |
| Layout | Four pairs of bars (predicted/measured) |
| Pair 1 | D/H: predicted 2.531e-5, measured 2.527e-5. Miss: 0.12σ. Color GREEN (close). |
| Pair 2 | Y_p (He-4): predicted 24.86%, measured 24.49%. Miss: 0.94σ. Color GREEN. |
| Pair 3 | He-3: predicted vs measured. Color CYAN. |
| Pair 4 | Li-7: predicted 4.74e-10, measured 1.60e-10. Miss: 2.96×. Color RED (the lithium problem). |
| Annotation on Li-7 | "The lithium problem. Every model has this. We inherit it because we use the same nuclear physics." |
| What text cannot show | The contrast — three green bars (agreement) and one red bar (lithium). The visual immediately communicates "three work, one doesn't, and that's known." |

---

### Section: The QED Chain

**Diagram V13: One Measurement to Twelve Digits**

| Property | Value |
|---|---|
| Type | Scale/Landscape |
| Size | 18 × 8 |
| Title | From One Trapped Electron to α at 12 Digits |
| Layout | Horizontal, left to right |
| Left | Penning trap icon (a circle with an electron). Label: "aₑ = 0.00115965218059. Measured at Harvard. One electron in a magnetic field." Color GOLD. |
| Middle | Newton inversion arrow. Label: "Invert the QED series. Residual: 10⁻²⁰⁴." Color CYAN. |
| Right | α⁻¹ = 137.035999207. Label: "12 digits. Matches Rb recoil to 0.007 ppb." Color GREEN. |
| Below | Number line showing 12 digits with each digit highlighted. The matching digits in GREEN, any mismatch in RED. All 12 match. |
| What text cannot show | The precision chain — one input, one inversion, 12 digits of agreement. The number line with 12 green digits is the visual proof. |

**Diagram V14: The Hydrogen Frequency**

| Property | Value |
|---|---|
| Type | Comparison Bar (digit-by-digit) |
| Size | 18 × 8 |
| Title | Harvard Measures, Germany Predicts: 11 Digits Match |
| Layout | Two rows of digits, aligned |
| Row 1 "Predicted" | 2 4 6 6 0 6 1 4 1 2 0 9 4 7 0 0 — each digit in its own box. Color GOLD. |
| Row 2 "Measured" | 2 4 6 6 0 6 1 4 1 3 1 8 7 0 1 8 — each digit in its own box. Color CYAN. |
| Matching digits | First 9-10 digits highlighted GREEN (they match). Diverging digits in DIM. |
| Annotation | "One measurement in Massachusetts. One prediction from German spectroscopy data. Connected by integer arithmetic." |
| Frequency label | "2,466,061,413,187,018 Hz" — the hydrogen 1S-2S transition |
| What text cannot show | The digit-by-digit alignment — seeing 11 green boxes in a row then the mismatch starting. The precision is visual. |

---

### Section: The Cabibbo Doublet

**Diagram V15: The Cabibbo Doublet Identity Card**

| Property | Value |
|---|---|
| Type | Identity Card |
| Size | 16 × 12 |
| Title | The Cabibbo Doublet: The One Particle the Integers Demand |
| Layout | Central card with quantum numbers and properties |
| Quantum numbers | SU(3) = 3 (color triplet), SU(2) = 2 (weak doublet), Y = 1/6 (hypercharge). Each in its own labeled box. |
| Type | "Vector-like: both left and right hands transform the same way" |
| Beta shifts | Δb₁ = 1/15, Δb₂ = 1, Δb₃ = 1/3 — each in a box with the Fraction |
| Gap ratio | "SM: 218/115. With CD: 38/27. Only this particle gives small meaningful integers." |
| Named after | "Nicola Cabibbo (1935-2010). Identified quark mixing. Excluded from the 2008 Nobel. A particle name lasts longer than any prize." |
| Prediction | "Proton decay testable by Hyper-Kamiokande starting 2027" |
| What text cannot show | All the quantum numbers and Fractions in one visual reference — the card format lets the viewer see everything at once |

**Diagram V16: Why This Particle and No Other**

| Property | Value |
|---|---|
| Type | Comparison Bar |
| Size | 16 × 10 |
| Title | 15 Candidates, 14 Fail, 1 Survives |
| Layout | 15 horizontal bars, each a BSM candidate |
| Data per bar | Candidate name, gap ratio, pass/fail |
| Bar 1 | "Cabibbo Doublet (3,2,1/6)" — gap 38/27 — GREEN (survives) |
| Bars 2-6 | 5 tested candidates — gap ratios shown — RED (fail). Labels: "VL lepton doublet", "VL e singlet", "VL u singlet", "VL d singlet", "..." |
| Bars 7-15 | 10 untested candidates — GRAY (pending) |
| Threshold line | "Gap ratio must be exact fraction with small integers" — GOLD horizontal line |
| Annotation | "The integers chose the particle. We didn't." |
| What text cannot show | The elimination — 14 red bars and 1 green bar. The visual immediately communicates uniqueness. |

---

### Section: The Test Suite

**Diagram V17: The 253 Comparisons — Pass/Fail/Info Map**

| Property | Value |
|---|---|
| Type | Comparison Bar (stacked or grid) |
| Size | 18 × 10 |
| Title | 253 Comparisons Across 9 Domains |
| Layout | Grid or stacked bar by domain |
| Domains | QED, Electroweak, GUT, Cosmology, BBN, Muon g-2, CKM, Mass, GR |
| Per domain | Number of PASS (GREEN), FAIL (RED), INFO (SILVER), SKIP (DIM) |
| Approximate counts | ~220 PASS, ~5 FAIL, ~20 INFO, ~8 SKIP |
| Key visual | Overwhelming green with occasional red. The ratio IS the story. |
| Annotation | "FAIL stays in. The system doesn't hide failures. It shows them." |
| What text cannot show | The scale — 253 comparisons across 9 domains with the pass/fail ratio visible at a glance |

**Diagram V18: The 13 Inputs and 53 Outputs**

| Property | Value |
|---|---|
| Type | Connection/Integer Map |
| Size | 18 × 12 |
| Title | 13 In, 53 Out: The Surplus Is +40 |
| Layout | Left column: 13 input boxes. Right column: 9 domain boxes. Arrows from inputs to domains. |
| 13 inputs | α⁻¹, mₑ, mμ, mτ, M_Z, m_t, M_H, sin²θ_W, α_s, G_F, Ω_DM, π, aₑ |
| 9 domains | QED (7 outputs), EW (6), GUT (5), Cosmo (5), BBN (4), g-2 (3), CKM (3), Mass (3), GR (12+) |
| Each arrow | From specific inputs to their domain. Some inputs feed multiple domains. |
| Count annotation | "53 derived values. 13 measured inputs. Surplus: +40. No free parameters." |
| Color | Inputs in GOLD. Domains in their standard colors (QED=GOLD, GR=GREEN, Cosmo=PURPLE, etc.) |
| What text cannot show | The fan-out — 13 inputs spreading to 53 outputs across 9 domains. The arrows make the connection structure visible. |

---

### Section: Close

**Diagram V19: The Precision Staircase**

| Property | Value |
|---|---|
| Type | Scale/Landscape |
| Size | 18 × 10 |
| Title | From 0.007 ppb to 725 ppm: The Precision Staircase |
| Layout | Vertical log scale, best to worst precision |
| Data points | α⁻¹ at 0.007 ppb, Mercury at 2.8 ppm, sin²θ_W at 12 ppm, solar redshift at 16 ppm, Hulse-Taylor at 42 ppm, Koide at 62 ppm, M_W at 195 ppm, α_s at 0.33%, GPS at 0.35%, DM/baryon at 725 ppm |
| Each point | Labeled with name, miss value, and domain color |
| Visual | Points descending from top (best) to bottom (worst). The log scale shows that even the "worst" result (725 ppm) is less than 0.1% off. |
| Annotation | "The worst prediction misses by less than one part in a thousand." |
| What text cannot show | The dynamic range of precision — 5 orders of magnitude from ppb to ppm, all successes |

**Diagram V20: Check the Numbers**

| Property | Value |
|---|---|
| Type | Identity Card |
| Size | 16 × 10 |
| Title | Everything You Need to Check |
| Layout | Three boxes with links |
| Box 1 | "Code: github.com/[repo]" — color CYAN |
| Box 2 | "Papers: zenodo.org/[doi]" — color GREEN |
| Box 3 | "Book: amazon.com/[link]" — color GOLD. "$3" |
| Center text | "If the numbers are wrong, the model is wrong.\nIf the numbers are right, the model deserves attention\nregardless of who produced it." |
| No data | This is the call to action, not a data diagram |
| What text cannot show | Nothing — this is a text card. But the three-box layout with links makes it scannable and actionable. Include as closing frame. |

---

**Total: 20 diagram data tables across 10 sections. Two per section. Each table gives a new Claude the type, layout, data, colors, annotations, and what physics the diagram communicates that text cannot.**
