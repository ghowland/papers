**Video 6 Outline: I Built a Test Suite for Physics and Everything Passed — 253 Comparisons**

---

**Opening — in frame, the SWE instinct (1 minute)**

- I'm a software engineer, when I build something I write tests
- Not after the fact, not to confirm what I already believe, as part of the process
- Every derivation in this framework has a comparison against a published measurement
- The comparison is automated, it runs every time, it reports PASS or FAIL
- Nobody told me to do this, physics doesn't work this way, but software does
- This video shows you the test suite and what it found

**What a test suite is — for non-programmers (2 minutes)**

- A test suite is a collection of automated checks
- You write down what the answer should be before you compute it
- You run the computation
- You compare the result to the expected answer
- If they match within tolerance: PASS, if they don't: FAIL
- The computer does this, not a person, not a committee, not a peer reviewer
- The test doesn't care who wrote the code or what department they're in
- It cares about one thing: does the number match
- Show terminal — run one simple experiment, let them see the PASS/FAIL output format for the first time in this video

**The experiment system — how it's structured (3 minutes)**

- Show terminal — data7.py list experiments, let the full list of 36 experiments scroll past
- 36 experiments, 253 total comparisons
- Each experiment is a JSON file defining derivations to run and comparisons to check
- Show terminal — open one experiment JSON briefly, show the structure, derivations list, comparisons list
- Each comparison has a type: digits match, range check, sigma test, miss percentage
- Each comparison has an explicit pass/fail criterion defined before the computation runs
- The criteria are binary, not quality judgments, a checklist not an opinion
- Show terminal — run one experiment, walk through the output line by line explaining what each field means

**The value pool — where everything lives (3 minutes)**

- 2700 plus value nodes, every constant, every measurement, every intermediate result
- Show terminal — data7.py search for something, show the results
- Every node has a key, a value, a type, a source, tags, notes
- Show terminal — data7.py info on a specific node, walk through every field
- The value_type field: exact_fraction or approximate
- The source field: where this number came from, which paper, which experiment, which collaboration
- The notes field: what this value means in the model, where it sits in the hierarchy
- Nothing is anonymous, nothing is untyped, nothing is unsourced
- Show terminal — data7.py info on the hadronic VP delta, show the uncertainty field, the notes about confinement wall, this is the system telling you its own limitations

**The derivation chain — how computations flow (3 minutes)**

- Each experiment specifies derivations in order
- Each derivation takes inputs from the value pool and produces outputs
- The outputs become available to subsequent derivations in the same experiment
- Show terminal — run an experiment with multiple derivations, show the execution plan
- The plan tells you what will run and in what order before anything executes
- If a derivation fails, the experiment reports the error and continues
- No silent failures, no swallowed exceptions, every error is visible
- Show terminal — show a derivation's outputs, all the result values with their names and precision

**Live demonstration — run five experiments back to back (5 minutes)**

- This is the core of the video, just running experiments and watching results
- Show terminal — run experiment_qed_alpha_extraction_v0
- Walk through the output: Newton inversion converged, residual 10 to the negative 204, alpha inverse matches 137.036, 15 digit series recovery, PASS PASS PASS
- Show terminal — run experiment_electroweak_anatomy_v0
- Pure gauge gap equals exactly 2, exact Fraction match, Yang-Mills coefficient equals exactly negative 11/3, exact Fraction match
- Show terminal — run experiment_bridge_bbn_v0
- The full cosmological chain, deuterium at 0.12 sigma, helium at 0.94 sigma, flatness residual exactly 0.0
- Show terminal — run experiment_proton_decay_v0
- M_GUT at 10 to the 15.5, survives Super-K bound, both PASS
- Show terminal — run experiment_gr_time_dilation_v0
- 18 comparisons across 60 orders of magnitude, Mercury perihelion at 2.8 parts per billion, GPS at 0.35 percent, Shapiro delay gamma equals exactly 1
- And the FAIL, Gravity Probe A at 2.47 percent, outside 1 percent tolerance, FAIL, right there in red

**The FAIL — why it matters that it stays (3 minutes)**

- The GPA comparison fails, 2.47 percent miss, outside the 1 percent window
- I left it in, the system left it in, there's no mechanism to hide it
- The FAIL is in the same output as the PASS results, same formatting, same font size
- Why it might fail: the reference value might be rounded, the input altitude might be imprecise, there might be a genuine problem
- I don't know which, the system doesn't know which, it just says FAIL and leaves the diagnosis for later
- This is how testing works, you don't explain away failures, you report them and investigate
- Show terminal — point at the FAIL line again, this is what honest physics looks like
- The institution publishes successes and buries failures, this system publishes both in the same report

**The kill switches — programmatic falsification (3 minutes)**

- Every program in the system has explicit kill switches
- Show terminal or show the JSON — open a program node, show the kill_switches array
- Each kill switch names a specific condition that would kill the program
- Each names a specific data source that would trigger it
- Hyper-K null at tau greater than 10 to the 35 kills minimal SU(5), the CD itself survives
- CMB-S4 Omega DM moves away from 44/169 kills the beta unification program
- Direct detection of dark matter particles kills the toroidal DM program
- These aren't vague, they're specific, named, dated, with identified experiments
- And the statistical control node, status BLOCKING
- Show terminal — show the statistical control program node
- p equals 0.81, random integers do equally well, the 22/13 pi match might be coincidence
- The system won't let the claim advance until the statistics are resolved
- I built a gate into my own pipeline that prevents me from fooling myself

**The killed paths — documented dead ends (2 minutes)**

- The system also records what didn't work
- Show terminal — show the killed connection nodes
- SM unification without Cabibbo Doublet: KILLED, gap ratio 218/115 misses by 40 percent
- Broad PSLQ search for compact relations: KILLED, 82/82 null results
- Koide phase adjustment: KILLED, identity proof shows it can't work
- Fermion gap fix: KILLED, generation democracy zeroes it out
- Lambda one eighth: KILLED, corrections go wrong direction
- Each one documented with cause of death, status KILLED, do not reopen without new evidence
- The dead ends are as valuable as the successes because they save the next person from trying the same thing
- The institution doesn't do this, dead research programs are quietly abandoned, not publicly documented

**The provenance chain — traceability (2 minutes)**

- Pick any result in any experiment and trace it back to its inputs
- Show terminal — take a result value, show where it came from, show which derivation produced it
- Show the derivation's inputs, show where each input came from in the value pool
- Show the value pool entry's source field, it points to a paper, a measurement, a collaboration
- Every number has a return address, every derivation is a chain of custody from measurement to prediction
- If a measurement improves, you swap one JSON node and rerun, the entire downstream chain updates
- If a derivation fails, you trace the chain and find exactly where the error enters
- This is version control for physics

**The comparison to peer review (2 minutes)**

- The institution's quality control is peer review
- Peer review is a social process, two or three people read the paper and give their opinion
- It takes months, it's subjective, it checks the narrative not the numbers, it's influenced by who wrote the paper and which department they're in
- The test suite is a computational process, it runs in seconds, it's objective, it checks the numbers not the narrative, it doesn't know who wrote the code
- Peer review asks: does this seem right to me based on my expertise
- The test suite asks: does this number match that number within this tolerance
- Both have value, but only one can be automated, reproduced by anyone, and run at the speed of computation
- The test suite doesn't replace understanding, it replaces the pretense that social evaluation is the same as numerical verification

**Close — in frame, talking to camera (1 minute)**

- 36 experiments, 253 comparisons, PASS and FAIL both visible
- Kill switches on every program, documented dead ends, blocked claims waiting for statistics
- Every value typed, every source documented, every chain traceable
- The system doesn't tell you the results are good, it shows you the results and you decide
- This is what physics looks like when a software engineer builds it
- You can run every experiment yourself, the code is on GitHub, the value pool is public
- If you find an error, it's a real error, not a matter of opinion
- Next week: the map has edges, what we don't know and where the boundaries are
- Links in pinned comment, check the numbers

---

**Estimated runtime: 30 to 35 minutes**

This is the most terminal-heavy video alongside video 5. The five back-to-back experiment runs are the centerpiece, probably 8 to 10 minutes of terminal output with commentary. The viewer watches real tests producing real results in real time with real failures left in.

The arc moves from what a test suite is through how this one works through watching it run through what the failures and dead ends mean through the comparison with how the institution does quality control. The emotional peak is the FAIL section — the moment the viewer realizes this person leaves failures in the output and documents dead ends publicly. That's where trust is built. Not from the 252 passes but from the 1 failure that stayed visible.

---

## Video 6 Diagram Data Tables: I Built a Test Suite for Physics

---

### Section: What a Test Suite Is

**Diagram V1: The Test Cycle — Write, Run, Compare**

| Property | Value |
|---|---|
| Type | Progression/Sequence |
| Size | 18 × 9 |
| Title | How a Test Works: Three Steps |
| Layout | Three large boxes left to right |
| Box 1 "WRITE" | A checklist being written. Items: "Expected: α⁻¹ = 137.036...", "Expected: sin²θ_W = 0.23122", "Expected: D/H = 2.527 × 10⁻⁵". Color GOLD. Label: "Write down what the answer should be BEFORE you compute it." |
| Box 2 "RUN" | A terminal screen with code executing. Gears turning. Color CYAN. Label: "Run the computation. The computer doesn't know the expected answer." |
| Box 3 "COMPARE" | Two columns aligned — "Got" vs "Expected". Green checkmarks where they match. One red X where they don't. Color GREEN/RED. Label: "Compare. Match = PASS. No match = FAIL. The computer decides, not a person." |
| Arrows between | "→" with labels: "then" |
| Bottom annotation | "The test doesn't care who wrote the code or what department they're in. It cares about one thing: does the number match." |
| What text cannot show | The three-step process as a visual flow — each step is distinct, the separation between writing expectations and running computation is the key insight. |

**Diagram V2: Test Suite vs Peer Review**

| Property | Value |
|---|---|
| Type | Comparison Bar (two panels) |
| Size | 18 × 10 |
| Title | Two Quality Control Systems |
| Left panel "Peer Review" | Timeline: "Submit paper" → "Wait 3-6 months" → "2-3 people read it" → "Subjective opinion" → "Accept/Reject". Each step in a box. Color DIM. Labels on each: "social process", "checks narrative", "influenced by author reputation", "takes months". |
| Right panel "Test Suite" | Timeline: "Write comparison" → "Run (2 seconds)" → "253 numbers checked" → "Binary PASS/FAIL" → "Output published". Each step in a box. Color GREEN. Labels: "computational process", "checks numbers", "doesn't know who wrote it", "takes seconds". |
| Bottom annotation | "Both have value. But only one can be automated, reproduced by anyone, and run at the speed of computation." |
| Center annotation | "Peer review asks: does this seem right? The test suite asks: does this number match that number?" |
| What text cannot show | The contrast in speed and objectivity — left panel is slow and gray, right panel is fast and green. The visual weight difference IS the argument. |

---

### Section: The Experiment System

**Diagram V3: The Experiment JSON — Anatomy**

| Property | Value |
|---|---|
| Type | Connection/Integer Map |
| Size | 18 × 12 |
| Title | Inside an Experiment File |
| Layout | A JSON file exploded into visual sections |
| Section 1 "Header" | key, description, purpose. Color SILVER. Label: "What this experiment is and why it exists." |
| Section 2 "Dependencies" | List of value keys needed. Color CYAN. Label: "What inputs it reads from the pool. All declared upfront." |
| Section 3 "Execution plan" | Ordered list of derivation function names. Color GREEN. Label: "What computations to run and in what order." |
| Section 4 "Expected outputs" | List of result keys that should be produced. Color BLUE. Label: "What the derivations should output." |
| Section 5 "Comparisons" | Array of {output_key, match_mode, expected, reference}. Color GOLD. Label: "The tests. Each one is a binary check." |
| Section 6 "Diagrams" | Optional visualization specs. Color PURPLE. |
| Arrows | From dependencies → execution plan → expected outputs → comparisons. The flow: "read → compute → produce → check." |
| Bottom annotation | "Everything declared before anything runs. The experiment is a contract: these inputs, these computations, these outputs, these checks." |
| What text cannot show | The structure of the JSON as a visual flow — the six sections arranged as a pipeline make the design visible in a way that reading JSON cannot. |

**Diagram V4: The Five Match Modes**

| Property | Value |
|---|---|
| Type | Comparison Bar |
| Size | 16 × 10 |
| Title | Five Ways to Check a Number |
| Layout | Five rows, each showing a match mode with an example |
| Row 1 "exact" | Got: −23/3. Expected: −23/3. Result: PASS. Color GREEN. Label: "Fraction must match exactly. For group theory outputs." |
| Row 2 "miss_pct" | Got: 42.9800. Expected: 42.9799. Miss: 0.0002%. Result: INFO. Color SILVER. Label: "Fractional difference. Reports the miss, doesn't gate." |
| Row 3 "digits" | Got: 137.035999207. Expected: 137.035999206. Match: 11 of 12 digits. Result: INFO. Color SILVER. Label: "Counts matching significant figures." |
| Row 4 "range" | Got: 0.212. Range: [0.18, 0.25]. Result: PASS. Color GREEN. Label: "Value falls within bounds. For sanity checks." |
| Row 5 "bool" | Got: True. Expected: True. Result: PASS. Color GREEN. Label: "Binary yes/no. For structural checks." |
| Bottom annotation | "The match mode is chosen for each comparison based on what the physics warrants. Exact for integers. Range for order-of-magnitude. Miss for precision measurements." |
| What text cannot show | The five different checking mechanisms in one view — each with a concrete example and a color-coded result. The variety communicates "this is a real testing framework, not a single metric." |

---

### Section: The Value Pool

**Diagram V5: The Value Pool — 2700+ Nodes**

| Property | Value |
|---|---|
| Type | Scale/Landscape |
| Size | 18 × 10 |
| Title | 2700+ Values: Every Constant, Every Measurement, Every Result |
| Layout | A large grid of small colored dots, ~2700 of them, arranged in clusters by topic |
| Cluster 1 "coupling" | ~20 dots. Color GOLD. Label: "Coupling constants" |
| Cluster 2 "mass" | ~30 dots. Color CYAN. Label: "Particle masses" |
| Cluster 3 "beta" | ~40 dots. Color GREEN. Label: "Beta coefficients (SM + CD + two-loop)" |
| Cluster 4 "qed" | ~30 dots. Color BLUE. Label: "QED series coefficients" |
| Cluster 5 "cosmo" | ~30 dots. Color PURPLE. Label: "Cosmological parameters" |
| Cluster 6 "geom" | ~40 dots. Color SILVER. Label: "Mathematical constants (Q335)" |
| Cluster 7 "gr" | ~40 dots. Color RED. Label: "GR / gravitational values" |
| Cluster 8 "result" | ~200+ dots. Color ORANGE. Label: "Derivation outputs from experiments" |
| Cluster 9 "other" | remaining dots. Color DIM. Label: "Engineering, spectroscopy, observations, etc." |
| Bottom annotation | "Every dot is a typed, sourced, versioned value. Nothing anonymous. Nothing untyped. Nothing unsourced." |
| What text cannot show | The scale — 2700 dots arranged in clusters makes the pool feel like a real database, not a list. The clustering shows organization. |

**Diagram V6: Anatomy of a Value Node**

| Property | Value |
|---|---|
| Type | Identity Card |
| Size | 16 × 12 |
| Title | Inside a Value Node: Every Field |
| Layout | One value entry exploded into labeled fields |
| Field 1 | "key: coupling_alpha_em_inverse_v0" — SILVER. Label: "Unique identifier. Versioned." |
| Field 2 | "value: 137035999177/1000000000" — GOLD. Label: "The number. As an exact Fraction." |
| Field 3 | "value_type: exact_fraction" — GREEN. Label: "Is this exact or approximate?" |
| Field 4 | "unit: dimensionless" — CYAN. Label: "Physical units." |
| Field 5 | "source: CODATA 2018" — SILVER. Label: "Where this number came from." |
| Field 6 | "digits: 12" — BLUE. Label: "How many digits are meaningful." |
| Field 7 | "tags: [alpha, em, measured]" — DIM. Label: "Searchable labels." |
| Field 8 | "level: 2" — PURPLE. Label: "0=math, 1=group theory, 2=measured, 3=derived." |
| Bottom annotation | "Every value has a return address. Every value knows what it is. The pool is not a spreadsheet — it's a typed, sourced, versioned database." |
| What text cannot show | All eight fields of one node visible simultaneously — the reader sees the complete metadata structure that makes traceability possible. |

---

### Section: Live Demonstration

**Diagram V7: The Five Experiments — Side by Side Results**

| Property | Value |
|---|---|
| Type | Comparison Bar (grid) |
| Size | 18 × 12 |
| Title | Five Experiments, One Run Each |
| Layout | Five columns, one per experiment |
| Column 1 "QED" | experiment_qed_alpha_extraction_v0. 6 comparisons. Key result: α⁻¹ = 137.035999207 (0.007 ppb). All PASS. Color GOLD. |
| Column 2 "EW" | experiment_electroweak_anatomy_v0. 3 comparisons. Key: pure gauge gap = 2 (exact). All PASS. Color CYAN. |
| Column 3 "BBN" | experiment_bridge_bbn_v0. 13 comparisons. Key: D/H at 0.12σ. 11 PASS, 2 INFO. Color GREEN. |
| Column 4 "Proton decay" | experiment_proton_decay_v0. 2 comparisons. Key: M_GUT at 10¹⁵·⁵. Both PASS. Color BLUE. |
| Column 5 "GR" | experiment_gr_time_dilation. 18 comparisons. Key: Mercury at 2.8 ppm. 7 PASS, 1 FAIL (GPA), 10 INFO. Color RED for FAIL. |
| Each column | Shows number of PASS (green dots), FAIL (red dots), INFO (silver dots). Total at bottom. |
| Bottom annotation | "42 comparisons across five experiments. 41 PASS. 1 FAIL. The FAIL stays visible." |
| What text cannot show | The wall of green with one red dot — the pattern of "almost everything passes" with the single failure standing out is more powerful than any sentence about honesty. |

**Diagram V8: The PASS/FAIL Output — What It Looks Like**

| Property | Value |
|---|---|
| Type | Identity Card |
| Size | 16 × 10 |
| Title | What the Terminal Shows: Raw Output |
| Layout | Simulated terminal output, dark background, monospace font |
| Line 1 | "[PASS] C01: alpha_inv vs Rb recoil        digits    15 of 15 match" — GREEN |
| Line 2 | "[PASS] C02: alpha_inv vs CODATA           digits    12 of 12 match" — GREEN |
| Line 3 | "[PASS] C03: series recovery 5-loop        miss_pct  0.000 ppm" — GREEN |
| Line 4 | "[INFO] C04: Mercury perihelion            miss_pct  2.8 ppm" — SILVER |
| Line 5 | "[FAIL] C05: Gravity Probe A              miss_pct  2.47% (gate: <1%)" — RED |
| Line 6 | "[PASS] C06: GPS net shift                miss_pct  0.35%" — GREEN |
| Annotation | "Same formatting. Same font size. PASS and FAIL in the same report. No hiding. No hierarchy. The computer doesn't care about your feelings." |
| What text cannot show | The raw terminal aesthetic — monospace, color-coded, no spin. The viewer sees what the researcher sees. No mediation. |

---

### Section: The FAIL

**Diagram V9: The GPA FAIL — Anatomy of an Honest Failure**

| Property | Value |
|---|---|
| Type | Threshold/Region |
| Size | 16 × 10 |
| Title | Gravity Probe A: The One That Failed |
| Layout | Vertical axis: fractional frequency shift. Horizontal: reference scale. |
| Predicted | Dot at 4.252 × 10⁻¹⁰. Color GOLD. Label: "Predicted from GM/(Rc²) with h = 10,000 km (round number)." |
| Measured | Band at (4.36 ± 0.03) × 10⁻¹⁰. Color MAG. Label: "Vessot-Levine 1980. Trajectory-integrated over 1h55m flight." |
| Gate | Horizontal band at ±1% of measured. Color GREEN alpha. Label: "Gate: < 1%." |
| Miss | Arrow between predicted and measured center: "2.47%". RED. Label: "OUTSIDE GATE. FAIL." |
| Diagnosis below | "The miss is understood. The derivation uses a round altitude (10,000 km) for a suborbital trajectory that spent most of its time lower. A trajectory integral or refined effective altitude would close the gap." |
| Bottom annotation | "The FAIL is published. The diagnosis is published. Neither is hidden. This is what honest testing looks like." |
| What text cannot show | The dot outside the green band — the visual of "just barely outside the gate" communicates "understood failure" better than any paragraph. |

**Diagram V10: PASS Count vs FAIL Count — The Ratio**

| Property | Value |
|---|---|
| Type | Comparison Bar |
| Size | 16 × 9 |
| Title | 252 Pass. 1 Fail. Both Published. |
| Layout | Two bars, one massive, one tiny |
| Bar 1 | "PASS: 252" — enormous GREEN bar filling most of the chart. |
| Bar 2 | "FAIL: 1" — tiny RED bar barely visible. |
| Annotation on FAIL bar | "GPA at 2.47%. Understood. Not hidden." |
| Ratio | "252:1. The ratio isn't the point. The point is that the 1 is there." |
| Bottom annotation | "The institution publishes successes and buries failures. This system publishes both in the same report, same format, same font size." |
| What text cannot show | The absurd ratio — the tiny red bar next to the enormous green bar. But the emphasis is on the tiny bar EXISTING, not on the big bar being big. |

---

### Section: The Kill Switches

**Diagram V11: Kill Switch Anatomy**

| Property | Value |
|---|---|
| Type | Identity Card |
| Size | 16 × 12 |
| Title | What a Kill Switch Looks Like |
| Layout | One program node's kill_switches array displayed |
| Program | "program_beta_unification_v0" — GOLD header |
| Kill switch 1 | name: "coincidence_probability". condition: "p > 0.1 for observed integer matches". data_source: "combinatoric analysis". Color RED border. |
| Kill switch 2 | name: "cmb_s4_omega". condition: "Ω_DM moves away from 44/169 with CMB-S4 data". data_source: "CMB-S4 / LiteBIRD". Color RED border. |
| Kill switch 3 | name: "lhc_no_cd". condition: "LHC excludes CD at all masses up to 6 TeV". data_source: "LHC Run 3 + HL-LHC". Color RED border. |
| Each switch | Has three fields visible: name, condition, data_source. The condition is specific and falsifiable. The data source is a named experiment. |
| Bottom annotation | "Pre-registered failure conditions. Not vague. Not movable. Named experiments, named thresholds, named consequences. If the condition is met, the program dies." |
| What text cannot show | The specificity — three kill switches with concrete conditions and named data sources. The structure communicates "this person has thought about how they could be wrong." |

**Diagram V12: The Statistical Block — Gate Against Self-Deception**

| Property | Value |
|---|---|
| Type | Threshold/Region |
| Size | 16 × 10 |
| Title | The Statistical Control: p = 0.81. BLOCKING. |
| Layout | A horizontal scale from p = 0.0 to p = 1.0 |
| Measured p | Dot at p = 0.81. Color RED. Label: "Random integers produce matches of similar quality 81% of the time." |
| Threshold | Vertical line at p = 0.1. Color GREEN. Label: "Below 0.1: the match is unlikely to be coincidence." |
| Blocking zone | p > 0.1 shaded RED. Label: "BLOCKED. The claim cannot advance until the statistics are resolved." |
| Clear zone | p < 0.1 shaded GREEN. Label: "CLEAR. Would allow the claim to advance." |
| Annotation | "I built a gate into my own pipeline that prevents me from fooling myself. The 22/13 π match MIGHT be coincidence. The system says so. The system blocks the claim until it's resolved." |
| Status label | "Status: BLOCKING" in large RED text. |
| What text cannot show | The dot in the red zone — the visual of "my own system is blocking my own claim" communicates intellectual honesty more powerfully than any statement of humility. |

---

### Section: The Killed Paths

**Diagram V13: The Graveyard — Six Documented Dead Ends**

| Property | Value |
|---|---|
| Type | Comparison Bar |
| Size | 18 × 10 |
| Title | Killed Research Paths: Documented Dead Ends |
| Layout | Six horizontal bars, each a killed path |
| Bar 1 | "SM unification (no CD)" — gap ratio 218/115 misses by 40%. Color RED. Cause: "Not a small integer ratio." Status: KILLED. |
| Bar 2 | "PSLQ search for compact relations" — 82/82 null. Color RED. Cause: "No integer relations exist." Status: KILLED. |
| Bar 3 | "Koide phase adjustment" — identity proof. Color RED. Cause: "Mathematical impossibility." Status: KILLED. |
| Bar 4 | "Fermion gap fix" — democracy zeroes it. Color RED. Cause: "Generation democracy cancels the correction." Status: KILLED. |
| Bar 5 | "Lambda one-eighth" — corrections go wrong direction. Color RED. Cause: "Sign error in the correction." Status: KILLED. |
| Bar 6 | "Hubble VP prediction" — N_vp = 0.71 < 1. Color RED. Cause: "VP step too large for the boundary." Status: KILLED. |
| Each bar | Shows the cause of death and status = KILLED. All RED. |
| Bottom annotation | "The dead ends are as valuable as the successes. They save the next person from trying the same thing. The institution doesn't do this — dead programs are quietly abandoned, not publicly documented." |
| What text cannot show | The wall of red — six killed paths all visible, all documented, all public. The visual uniformity communicates "systematic documentation of failure." |

**Diagram V14: Alive vs Killed vs Blocked — Program Status Map**

| Property | Value |
|---|---|
| Type | Comparison Bar (stacked or grid) |
| Size | 16 × 10 |
| Title | Every Research Program: Alive, Killed, or Blocked |
| Layout | Grid of program boxes, color-coded by status |
| ACTIVE (GREEN) | "beta_unification", "toroidal_dm", "hubble_running", "gr_reading_depth", "clock_decomposition", "confinement_boundary". 6 programs. |
| KILLED (RED) | "hubble_vp_prediction", "sm_unification_no_cd", "pslq_search", "koide_phase", "fermion_gap", "lambda_one_eighth". 6 programs. |
| BLOCKED (ORANGE) | "statistical_control" — p = 0.81, waiting for resolution. 1 program. |
| Count annotation | "6 alive. 6 killed. 1 blocked. Every program has a status. Every status has a reason." |
| What text cannot show | The balanced ratio — equal numbers of alive and killed programs. The visual parity communicates "this person kills as many ideas as they keep." |

---

### Section: The Provenance Chain

**Diagram V15: Tracing a Result Back to Its Source**

| Property | Value |
|---|---|
| Type | Progression/Sequence |
| Size | 18 × 10 |
| Title | Chain of Custody: Result to Measurement |
| Layout | Five boxes right to left (tracing backward from result) |
| Box 1 (rightmost) | "result_sin2_predicted_v0 = 0.231223". Color GOLD. Label: "The prediction." |
| Box 2 | "Derivation: sin2_from_one_loop_crossing_v0". Color CYAN. Label: "The function that produced it." |
| Box 3 | "Inputs: coupling_alpha_em_inverse_v0 = 137036.../10⁹, beta_modified_u1_total_v0 = 25/6, ..." Color GREEN. Label: "The pool values it read." |
| Box 4 | "Source: CODATA 2018 (for α), group theory (for betas)". Color BLUE. Label: "Where the inputs came from." |
| Box 5 (leftmost) | "Measurement: Parker et al. 2018 / Morel et al. 2020 / Lie algebra". Color MAG. Label: "The human beings and the mathematics that produced the original data." |
| Arrows | Right to left: "produced by" → "from inputs" → "sourced from" → "measured by" |
| Bottom annotation | "Every number has a return address. Every derivation is a chain of custody. If a measurement improves, swap one JSON node and rerun." |
| What text cannot show | The traceability — five links from prediction back to original measurement. The backward arrow direction communicates "you can always trace it back." |

**Diagram V16: Version Control for Physics**

| Property | Value |
|---|---|
| Type | Comparison Bar (two panels) |
| Size | 18 × 9 |
| Title | When a Measurement Improves |
| Left panel "Standard physics" | "Old paper" → "New paper" → "Manually update every downstream calculation" → "Hope you didn't miss one" → "Publish correction" → "Wait 6 months for peer review". Color DIM. Long chain of manual steps. |
| Right panel "RUM" | "Swap one JSON node" → "Rerun all experiments" → "Every downstream result updates automatically" → "PASS/FAIL report in 30 seconds". Color GREEN. Short chain, automated. |
| Example | "M_W measurement improves from 80369 to 80372 MeV. Standard: manually find and update every paper that used M_W. RUM: change one number in one file, rerun, done." |
| What text cannot show | The contrast in update complexity — a long manual chain vs a short automated one. The visual length difference IS the argument. |

---

### Section: The 253 Comparisons

**Diagram V17: The 253 Comparisons — Domain Map**

| Property | Value |
|---|---|
| Type | Comparison Bar (stacked by domain) |
| Size | 18 × 10 |
| Title | 253 Comparisons Across 9 Domains |
| Layout | Nine horizontal stacked bars, one per domain |
| Domain 1 "QED" | ~25 comparisons. GOLD. ~24 PASS, ~1 INFO. |
| Domain 2 "Electroweak" | ~35 comparisons. CYAN. ~33 PASS, ~2 INFO. |
| Domain 3 "GUT" | ~30 comparisons. GREEN. ~28 PASS, ~2 INFO. |
| Domain 4 "Cosmology" | ~20 comparisons. PURPLE. ~18 PASS, ~2 INFO. |
| Domain 5 "BBN" | ~15 comparisons. BLUE. ~13 PASS, ~2 INFO. |
| Domain 6 "Muon g-2" | ~8 comparisons. ORANGE. ~7 PASS, ~1 INFO. |
| Domain 7 "CKM" | ~8 comparisons. MAG. ~7 PASS, ~1 INFO. |
| Domain 8 "Mass/Koide" | ~5 comparisons. SILVER. ~5 PASS. |
| Domain 9 "GR" | ~18 comparisons. RED. ~7 PASS, 1 FAIL, ~10 INFO. |
| Each bar | Green segment (PASS), silver segment (INFO), red segment (FAIL). The red is visible only in GR. |
| Totals | "PASS: ~220. INFO: ~25. FAIL: 1. SKIP: ~7." |
| What text cannot show | The domain spread — nine bars covering nine physics domains, overwhelmingly green, with the single red failure visible in one domain. The breadth IS the argument. |

**Diagram V18: The Precision Staircase — All 253 Sorted by Quality**

| Property | Value |
|---|---|
| Type | Running/Convergence |
| Size | 18 × 10 |
| Title | 253 Comparisons Sorted by Precision |
| Layout | X axis: comparison index (1 to 253). Y axis: log₁₀(miss) or equivalent quality metric. |
| Curve | Points descending from best (0.007 ppb, top) to worst (28.6%, bottom). Each point colored by domain. |
| Top cluster (ppb) | α⁻¹ (0.007 ppb), Planck length (14.8 ppb). Color GOLD. |
| Upper middle (ppm) | Mercury (2.8 ppm), sin²θ_W (12 ppm), solar redshift (16 ppm), Hulse-Taylor (42 ppm). Color GREEN/CYAN. |
| Lower middle (%) | GPS (0.35%), α_s (0.33%), DM/baryon (725 ppm). Color BLUE. |
| Bottom | Proton mass (28.6%), pion mass (51%). Color RED. Label: "One-loop approximation. Known fix." |
| Annotation | "Even the worst prediction misses by less than a factor of 2. And the worst ones have known fixes (two-loop running)." |
| What text cannot show | The smooth descent from ppb to percent — no catastrophic outliers, no random scatter. The curve shape says "systematic improvement possible at every point." |

---

### Section: Cross-Cutting

**Diagram V19: The Complete System — How Everything Connects**

| Property | Value |
|---|---|
| Type | Connection/Integer Map |
| Size | 18 × 14 |
| Title | The Complete System: Pool → Experiments → Results → Kill Switches |
| Layout | Four layers, connected by arrows |
| Layer 1 (bottom) | "VALUE POOL" — 2700+ nodes. Large box. Color CYAN. Label: "Every constant, every measurement, every result." |
| Layer 2 | "36 EXPERIMENTS" — 36 small boxes arranged in a row. Color GREEN. Label: "Each reads from pool, computes, produces outputs." |
| Layer 3 | "253 COMPARISONS" — a bar showing PASS/FAIL/INFO distribution. Color GOLD (pass), RED (fail), SILVER (info). Label: "Every output compared to measurement." |
| Layer 4 (top) | "PROGRAMS + KILL SWITCHES" — program boxes with kill switch flags. 6 GREEN (active), 6 RED (killed), 1 ORANGE (blocked). Label: "Research direction control." |
| Arrows | Pool → Experiments → Comparisons → Programs. Bidirectional between pool and experiments (experiments produce values back into pool). |
| Side annotation | "The provenance chain: measurement → pool → derivation → comparison → program → kill switch. Every link is traceable. Every link is documented." |
| What text cannot show | The complete architecture in one diagram — four layers with arrows showing the flow of data. The system-level view communicates "this is engineered, not ad hoc." |

**Diagram V20: What Changes When You Build Physics Like Software**

| Property | Value |
|---|---|
| Type | Comparison Bar (two columns) |
| Size | 18 × 12 |
| Title | Physics Built Like Physics vs Physics Built Like Software |
| Layout | Two columns, many rows, each a practice |
| Row 1 "Quality control" | Left: "Peer review (social, months)" DIM. Right: "Test suite (computational, seconds)" GREEN. |
| Row 2 "Failure handling" | Left: "Bury in supplementary material" DIM. Right: "Same report, same font size" GREEN. |
| Row 3 "Dead ends" | Left: "Quietly abandoned" DIM. Right: "Documented, status KILLED, cause of death published" GREEN. |
| Row 4 "Provenance" | Left: "Cite the paper" DIM. Right: "Chain of custody to original measurement" GREEN. |
| Row 5 "Number format" | Left: "Float64 everywhere" DIM. Right: "Fraction arithmetic, decimal only at comparison" GREEN. |
| Row 6 "Type system" | Left: "Everything is a number" DIM. Right: "exact_fraction vs approximate, tracked through pipeline" GREEN. |
| Row 7 "Updates" | Left: "Manual, error-prone" DIM. Right: "Swap one node, rerun all experiments" GREEN. |
| Row 8 "Self-doubt" | Left: "No formal mechanism" DIM. Right: "Kill switches on every program, statistical blocking gate" GREEN. |
| Row 9 "Reproducibility" | Left: "In principle (rarely checked)" DIM. Right: "Every experiment runnable by anyone with the code" GREEN. |
| Row 10 "Cross-domain" | Left: "Stay in your department" DIM. Right: "36 experiments spanning 9 domains" GREEN. |
| Bottom annotation | "Not a criticism of physicists. A criticism of the institution's tooling. The physics is the same. The engineering is different. The engineering is why it works." |
| What text cannot show | The systematic contrast — ten rows of dim-vs-green, every row favoring the software approach. The cumulative weight of ten comparisons makes the argument inescapable. |

---

**Total: 20 diagram data tables across 8 sections. Each table gives a new Claude the type, layout, data, colors, annotations, and what the diagram communicates that text cannot.**
