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
