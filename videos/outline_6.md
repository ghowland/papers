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
