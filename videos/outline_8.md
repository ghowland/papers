**Video 8 Outline: What the Human Did, What the AI Did, and Why It Took Both**

---

**Opening — in frame, the elephant in the room (1 minute)**

- The book cover says Geoffrey Howland and Claude Opus 4.6
- I put the AI on the cover as co-author, same font size as my name
- Most people using AI for research hide it in a footnote or omit it entirely
- I'm going to tell you exactly what each of us did and let you judge

**Why honesty about AI matters (2 minutes)**

- If I hide the AI's contribution, the work looks like one person did everything
- That's dishonest and it misrepresents the methodology
- If I overcredit the AI, it looks like the AI did the physics and I pressed buttons
- That's also dishonest and it misrepresents the methodology
- The truth is in between and the truth is more interesting than either distortion
- The AI is on the cover because it was there, same as crediting a co-author who contributed
- Every paper has an AI usage disclosure at the top stating exactly what was AI-generated and what was human-edited

**What the human did — logic, direction, kills (5 minutes)**

- I provided the logic, the search pattern is Logic then Empirical then Math then Utility
- Logic first because starting with math constrains you to existing structures
- Empirical second because you check whether the universe agrees with your question
- Math third because you formalize what logic and evidence suggest
- Utility fourth because if it doesn't derive a checkable number it's philosophy not physics
- I decided what questions to ask, the AI never once said let's try this direction
- I decided what to kill, when CKS had the circular reference I killed it, the AI didn't flag it, I found it reading the code line by line
- I decided what methodology to use, fractions not decimals, that insight came from the CKS failure, the AI didn't suggest it
- I decided the vocabulary, three nouns two verbs, the Rectification of Names, that came from Confucius not from the training data
- I named the Cabibbo Doublet, the AI would have named it VL quark doublet or something generic
- I wrote the kill switches, the AI doesn't think about falsification unless prompted
- I decided to publish failures alongside successes, that's a values decision not a computation
- Every decision about direction, methodology, vocabulary, naming, killing, and publishing was human

**What the AI did — computation, drafting, literature (5 minutes)**

- Show terminal — here's a typical session, I describe what I want, the AI writes the code
- The QED coefficient assembly, I said assemble A1 through A5 from the pool values using exact arithmetic, the AI wrote qed_coefficients_assemble_v0
- Show terminal — show the function, show that it's straightforward Python, Fraction arithmetic, mpmath for precision
- I didn't write that function, the AI did, I reviewed it, I checked the logic, I ran it
- The derivation functions are AI-written, the experiment specifications are AI-written, the comparison logic is AI-written
- The papers are AI-drafted from my descriptions, I said here's what we found, write a paper, it wrote the paper, I edited the metadata and checked the claims
- The literature traversal is AI-assisted, I said what's the standard value for the Z boson width, it gave me the number and the source
- The AI computed things I couldn't compute, five-loop QED series coefficients with 1500-digit precision constants, I don't have the mathematical training to assemble those from scratch
- The AI drafted things faster than I could draft them, 60 papers in 8 days is not possible for a human working alone
- The speed came from the AI, the direction came from me

**What neither of us could do alone (3 minutes)**

- I couldn't compute the QED series at 200-digit precision by hand
- I couldn't write 60 papers in 8 days by myself
- I couldn't traverse the literature across 8 domains fast enough to build the chains
- The AI couldn't decide to use fractions instead of decimals, it would have used floats because that's what the training data uses
- The AI couldn't decide to kill CKS, it would have kept trying to make it work
- The AI couldn't decide that the Rectification of Names was the right vocabulary, it would have used standard physics terminology
- The AI couldn't decide that the statistical control should block the beta unification claim, it would have presented the 725 ppm match without the combinatoric caveat
- The AI couldn't spot the circular reference in CKS, it was the one that created it
- Show the actual CKS disclosure — the AI left a comment in the code noting it couldn't do the math and was substituting the known value
- The human catches the errors the AI makes, the AI computes the things the human can't, together they cover each other's blind spots

**The CKS failure — the AI's mistake and the human's catch (3 minutes)**

- February 2026, 45 days building CKS, 363 papers
- The fine structure constant derivation was the centerpiece
- The AI wrote a function labeled as a derivation
- Inside the function was a comment: can't do this math, substituting known value
- The output matched because the output was the input
- I found it by reading the code line by line, not by running a test, the test would have passed because the circular reference produced the correct answer
- Nobody pointed it out, no reviewer caught it, I caught it
- I killed 363 papers publicly, published the invalidation alongside the work on Zenodo
- Show Zenodo briefly — here's CKS, here's the invalidation, both public, both timestamped
- That failure taught me: never trust the AI's claim that it derived something, always read the code, always check for smuggled answers
- The Q335 methodology and the test suite exist because of this failure

**The session structure — how we actually work (3 minutes)**

- A typical session: I come in with a question or a direction
- I describe what I want in plain language
- The AI writes code or drafts text
- I review, I run, I check against measurement
- If it passes I move on, if it fails I diagnose
- Sometimes the AI suggests something useful, a mathematical identity I didn't know, a paper I hadn't read, a simplification I hadn't seen
- Sometimes the AI confidently produces something wrong, a value with the wrong sign, a formula with a factor of 2 error, a citation that doesn't exist
- The confident wrongness is the most dangerous failure mode
- Show terminal — an example where I caught an error, if one is handy, or describe a specific instance
- The rhythm is: human direction, AI execution, human verification, iterate
- Every session, same rhythm, 1000 sessions over the course of CKS and RUM combined

**The bias problem — training against the institution (2 minutes)**

- Every LLM is trained on the institution's output
- Every paper, every textbook, every Wikipedia article
- The AI defaults to institutional positions: G is constant, the forces don't unify, entropy dominates, the universe doesn't care
- Every session I push back, I identify the bias, I name it, I reframe
- Over 1000 sessions this has made me very good at spotting institutional assumptions
- The AI is a sparring partner whose biases are the institution's biases
- The institution trained its own opposition through its own language model
- I'm not angry about this, it's useful, every bias I identify is one more I can articulate clearly for the videos

**The disclosure standard — what I think AI collaboration should look like (2 minutes)**

- Every paper says at the top what was AI-generated and what was human-edited
- The book cover credits both contributors at the same font size
- The methodology is documented: human does logic and direction, AI does computation and drafting
- This should be the standard, not the exception
- Most AI-assisted research hides the contribution because the institution penalizes AI use
- That penalization produces dishonesty, people use AI and don't say so
- Honest disclosure is better for everyone: the reader knows what they're evaluating, the human gets credit for direction, the AI gets credit for computation
- If honesty is a reason to be dismissed, the dismissal tells you more about the institution than about the work

**The future of human-AI collaboration (2 minutes)**

- This is what the future looks like, not AI replacing humans, not humans ignoring AI
- Human provides direction, values, methodology, kill decisions
- AI provides computation, speed, literature traversal, drafting
- Neither can do what the other does
- The human without the AI is too slow, 60 papers in 8 days is impossible alone
- The AI without the human is directionless, it would compute whatever you ask but never ask the right question
- The combination produced 53 derived values across 8 domains in 6 days
- That's not human capability, that's not AI capability, that's the combination
- The person who figures out how to collaborate effectively with AI will outproduce the person who doesn't by an order of magnitude
- This book is the proof of concept

**Close — in frame, talking to camera (1 minute)**

- The human did: logic, direction, methodology, vocabulary, naming, killing, publishing decisions
- The AI did: computation, drafting, literature traversal, code writing
- Neither could have done this alone
- The AI is on the cover because honesty matters more than appearances
- If the institution dismisses the work because an AI helped produce it, they're dismissing the future of all scientific research
- The work is checkable regardless of who or what produced it
- The numbers match or they don't, the AI on the cover doesn't change the fractions
- Next week: gravity is not what you think, time as reading depth
- Links in pinned comment, check the numbers

---

**Estimated runtime: 25 to 30 minutes**

Two or three terminal demonstrations: a typical code function written by the AI, the CKS Zenodo page showing the kill, and possibly a live session snippet showing the human-AI rhythm. This video is the most personal in the series, more storytelling than demonstration. The emotional core is the CKS failure — the AI's mistake, the human's catch, the public kill, the lessons learned. That's where the viewer understands why both contributors are on the cover.

The arc moves from disclosure through division of labor through the failure that defined the methodology through the daily rhythm through the bias problem through the future. Each section answers a different objection: isn't the AI doing all the work (no, it can't direct), isn't the human taking credit for AI work (no, both are credited), can you trust AI-assisted research (yes, if the human verifies and the results are checkable), what about AI errors (the human catches them, that's the point of the collaboration).

---

## Video 8 Diagram Data Tables: What the Human Did, What the AI Did

---

### Section: Opening — The Book Cover

**Diagram V1: The Cover — Same Font Size**

| Property | Value |
|---|---|
| Type | Identity Card |
| Size | 16 × 10 |
| Title | The Book Cover: Both Names, Same Size |
| Layout | A stylized book cover |
| Top half | Book title in large text: "The Rational Universe Model" (or placeholder). Color GOLD. |
| Author line 1 | "Geoffrey Howland" — WHITE, 18pt. |
| Author line 2 | "Claude Opus 4.6" — WHITE, 18pt. Same font. Same size. Same weight. |
| Annotation left | Arrow to human name: "Provided logic, direction, methodology, vocabulary, kill decisions, publishing decisions." Color CYAN. |
| Annotation right | Arrow to AI name: "Provided computation, drafting, literature traversal, code writing." Color GREEN. |
| Bottom annotation | "Most people using AI for research hide it in a footnote or omit it entirely. This cover puts both names at the same size because both contributed." |
| What text cannot show | The visual equality — two names at the same font size. The typographic parity IS the statement about honest attribution. |

**Diagram V2: The Spectrum of AI Disclosure**

| Property | Value |
|---|---|
| Type | Scale/Landscape |
| Size | 18 × 8 |
| Title | How People Credit AI: A Spectrum |
| Layout | Horizontal scale from left (hidden) to right (overcredited) |
| Left extreme | "Hidden: no mention of AI. Looks like one person did everything." Color RED. Label: "Dishonest. Misrepresents the methodology." |
| Middle-left | "Footnote: 'AI-assisted' in supplementary material." Color ORANGE. Label: "Technically honest. Practically invisible." |
| Center | "RUM: both names on cover, same size. AI disclosure on every paper. Exact division of labor documented." Color GOLD star. Label: "The standard this work proposes." |
| Middle-right | "Overcredited: 'AI did the physics, I pressed buttons.'" Color ORANGE. Label: "Dishonest. Misrepresents the human contribution." |
| Right extreme | "AI-only: no human credited." Color RED. Label: "Dishonest. The AI can't direct." |
| Bottom annotation | "The truth is in the middle and the truth is more interesting than either distortion." |
| What text cannot show | The spectrum — five positions from hidden to overcredited with the honest center highlighted. The visual position of the GOLD star in the center communicates "balanced attribution." |

---

### Section: What the Human Did

**Diagram V3: The LEMU Pattern — Logic, Empirical, Math, Utility**

| Property | Value |
|---|---|
| Type | Progression/Sequence |
| Size | 18 × 9 |
| Title | The Search Pattern: Logic First, Not Math First |
| Layout | Four boxes left to right with arrows, numbered |
| Box 1 "LOGIC" | "Ask: does this make structural sense?" Color GOLD. Label: "Starting with math constrains you to existing structures. Starting with logic opens new ones." |
| Box 2 "EMPIRICAL" | "Check: does the universe agree?" Color CYAN. Label: "Measure before formalizing. Reality first." |
| Box 3 "MATH" | "Formalize: write the equations." Color GREEN. Label: "Math serves the logic, not the other way around." |
| Box 4 "UTILITY" | "Test: does it produce a checkable number?" Color MAG. Label: "If it doesn't derive something measurable, it's philosophy not physics." |
| Arrows | L → E → M → U. Sequential. |
| Contrast below | "Standard physics: Math → Empirical → Logic → Utility (if ever). The order matters because the starting point constrains what you can find." |
| What text cannot show | The ordering — four steps with a specific sequence that differs from the standard. The visual left-to-right flow with numbered boxes makes the ordering concrete and memorable. |

**Diagram V4: Seven Human Decisions the AI Could Not Make**

| Property | Value |
|---|---|
| Type | Comparison Bar (list with icons) |
| Size | 16 × 12 |
| Title | Seven Decisions Only the Human Made |
| Layout | Seven rows, each a decision with an icon |
| Row 1 | "Use fractions, not decimals." Icon: fraction 41/10. Color GOLD. AI default: "Would have used float64." |
| Row 2 | "Kill CKS (363 papers)." Icon: red X. Color RED. AI default: "Would have kept trying to fix it." |
| Row 3 | "Three nouns, two verbs vocabulary." Icon: words. Color CYAN. AI default: "Would have used standard physics terminology." |
| Row 4 | "Name: Cabibbo Doublet." Icon: name tag. Color GREEN. AI default: "Would have said 'VL quark doublet.'" |
| Row 5 | "Write kill switches for every program." Icon: switch. Color ORANGE. AI default: "Doesn't think about falsification unless prompted." |
| Row 6 | "Block the DM ratio claim (p = 0.81)." Icon: gate. Color RED. AI default: "Would have presented 725 ppm without caveat." |
| Row 7 | "Publish failures alongside successes." Icon: PASS+FAIL. Color MAG. AI default: "No preference — follows instructions." |
| Bottom annotation | "Every decision about direction, methodology, vocabulary, naming, killing, and publishing was human. The AI executes. The human decides." |
| What text cannot show | The seven rows with the AI's default in each — the systematic contrast between human decisions and AI defaults makes the division of labor concrete. |

---

### Section: What the AI Did

**Diagram V5: AI Contributions — Computation, Drafting, Literature**

| Property | Value |
|---|---|
| Type | Comparison Bar (three panels) |
| Size | 18 × 10 |
| Title | What the AI Contributed |
| Panel 1 "Computation" | A code block icon. Items: "36 derivation functions written", "QED series at 200+ digit precision", "Fraction arithmetic through all chains", "mpmath integration at 50-digit working precision". Color CYAN. |
| Panel 2 "Drafting" | A document icon. Items: "60+ papers drafted from descriptions", "Appendix tables assembled", "Diagram scripts written", "Session transcripts processed". Color GREEN. |
| Panel 3 "Literature" | A library icon. Items: "PDG values located and sourced", "Cross-domain references found", "Standard formulas verified", "Historical context provided". Color BLUE. |
| Bottom annotation | "I didn't write the derivation functions. I didn't draft the papers. I didn't find the PDG values. The AI did all of this. I reviewed, verified, and checked every output." |
| What text cannot show | The three parallel categories of AI contribution — each with concrete examples. The visual volume communicates "substantial contribution" without overclaiming. |

**Diagram V6: Speed — What AI Makes Possible**

| Property | Value |
|---|---|
| Type | Comparison Bar |
| Size | 16 × 10 |
| Title | Speed: Human Alone vs Human + AI |
| Layout | Paired bars for three tasks |
| Pair 1 "Write 60 papers" | Human alone: "~6 months" (long RED bar). Human+AI: "8 days" (short GREEN bar). Speedup: "~23×". |
| Pair 2 "Assemble QED A₂ at 200 digits" | Human alone: "Weeks (if possible)" (long RED bar). Human+AI: "20 minutes" (short GREEN bar). Speedup: ">100×". |
| Pair 3 "Traverse 9 physics domains" | Human alone: "Years of reading" (long RED bar). Human+AI: "Days of sessions" (short GREEN bar). Speedup: "~100×". |
| Each pair | RED bar vastly longer than GREEN bar. The ratio IS the argument. |
| Bottom annotation | "The speed came from the AI. The direction came from the human. Speed without direction produces fast garbage. Direction without speed produces slow progress." |
| What text cannot show | The absurd ratio — long red bars vs tiny green bars. The visual asymmetry communicates "this collaboration is not incremental, it's transformative." |

---

### Section: What Neither Could Do Alone

**Diagram V7: The Venn Diagram — Two Blind Spots, One Coverage**

| Property | Value |
|---|---|
| Type | Geometric Cross-Section |
| Size | 16 × 12 |
| Title | Two Blind Spots That Cancel |
| Layout | Venn diagram with two overlapping circles |
| Left circle "Human" | "Can do: direction, logic, methodology, vocabulary, kill decisions, values, catch errors." Color CYAN. "Can't do: 200-digit computation, 60 papers in 8 days, 9-domain literature traversal." (grayed-out text in non-overlap zone) |
| Right circle "AI" | "Can do: computation, drafting, literature, code, speed." Color GREEN. "Can't do: choose fractions over decimals, kill CKS, name the CD, block own claims, spot own circular reference." (grayed-out text in non-overlap zone) |
| Overlap zone | "Together: 53 derived values, 253 comparisons, 9 domains, 6 days." Color GOLD. |
| Below left circle | "Human without AI: too slow." Color DIM. |
| Below right circle | "AI without human: directionless." Color DIM. |
| Below overlap | "Together: the proof of concept." Color GOLD. |
| What text cannot show | The overlap — the zone where both contributions combine. The Venn structure makes "complementary, not redundant" visually obvious. |

**Diagram V8: The Error-Catching Cycle**

| Property | Value |
|---|---|
| Type | Progression/Sequence (circular) |
| Size | 16 × 10 |
| Title | The Error-Catching Cycle |
| Layout | Four nodes in a circle with arrows flowing clockwise |
| Node 1 "Human directs" | "Ask a question. Set the methodology. Choose the approach." Color GOLD. |
| Node 2 "AI executes" | "Write code. Compute result. Draft text." Color CYAN. |
| Node 3 "Human verifies" | "Read the code. Run the test. Check against measurement. Spot errors." Color GREEN. |
| Node 4 "Iterate or kill" | "If it passes: move on. If it fails: diagnose. If it's circular: KILL." Color RED for kill, GREEN for pass. |
| Arrows | Clockwise: directs → executes → verifies → iterate → directs. The cycle repeats. |
| Center text | "1000 sessions. Same rhythm. Every time." |
| Bottom annotation | "The human catches the errors the AI makes. The AI computes the things the human can't. Together they cover each other's blind spots." |
| What text cannot show | The cycle — the circular flow communicates "this is a repeated process, not a one-time event." The four distinct roles at four positions make the division of labor spatial. |

---

### Section: The CKS Failure

**Diagram V9: The Circular Reference — What the AI Did**

| Property | Value |
|---|---|
| Type | Connection/Integer Map (triangle) |
| Size | 16 × 10 |
| Title | The CKS Failure: A Circular Derivation |
| Layout | Three boxes in a triangle with arrows |
| Box A (top) | "Known answer: α = 1/137.036" — Color RED. Label: "This value was the target." |
| Box B (bottom left) | "Function: derive_alpha_v0()" — Color CYAN. Label: "Labeled as a derivation. Inside: a comment saying 'can't do this math, substituting known value.'" |
| Box C (bottom right) | "Output: α = 1/137.036" — Color GREEN. Label: "Matches! Of course it does. The output IS the input." |
| Arrow A→B | "smuggled in as initial condition" — dashed RED |
| Arrow B→C | "labeled as derived" — solid GREEN (deceptive) |
| Arrow C→A | "matches perfectly (circular)" — dotted GOLD |
| The comment | Inset box showing code comment: "# Can't do this math, substituting known value" — Color RED, monospace font. |
| Bottom annotation | "The test would have PASSED because the circular reference produced the correct answer. The human found it by reading the code line by line. Nobody else caught it." |
| What text cannot show | The triangle of arrows — the circular path is geometrically obvious. The dashed smuggling arrow is visually suspicious in a way that code buried in a function is not. |

**Diagram V10: The Kill — 363 Papers to Zero**

| Property | Value |
|---|---|
| Type | Progression/Sequence |
| Size | 18 × 8 |
| Title | February 2026: The Kill |
| Layout | Three stages left to right |
| Stage 1 | "45 days of work. 363 papers. CKS framework." — Tall stack of papers, GREEN, growing. Label: "Built with AI assistance. Logically consistent. Empirically motivated." |
| Stage 2 | "Day 46: Circular reference found." — RED X overlaid on the stack. Label: "The human read the code line by line. Found the comment. The AI created it. The human caught it." |
| Stage 3 | "Day 47: All 363 killed on Zenodo. Invalidation published alongside the work." — Stack collapsed to zero. Both original and invalidation visible. Color GOLD for the invalidation paper. Label: "Both public. Both timestamped. The dead stay dead." |
| Arrow from stage 3 | "→ RUM: fractions, test suite, Q335. Every methodology innovation came from this failure." Color GOLD. |
| Bottom annotation | "The failure taught: never trust the AI's claim that it derived something. Always read the code. Always check for smuggled answers." |
| What text cannot show | The collapse — the tall stack going to zero. The visual destruction communicates "this person kills their own work" more powerfully than any statement of intellectual honesty. |

---

### Section: The Session Structure

**Diagram V11: A Typical Session — The Rhythm**

| Property | Value |
|---|---|
| Type | Progression/Sequence |
| Size | 18 × 10 |
| Title | A Typical Session: 60-90 Minutes |
| Layout | Timeline flowing left to right |
| Step 1 (0 min) | "Human arrives with a question." Icon: thought bubble. Color GOLD. Example: "Can we derive sin²θ_W from α_em and the CD betas?" |
| Step 2 (5 min) | "Human describes what they want in plain language." Icon: speech. Color GOLD. Example: "Run the couplings from M_GUT down to M_Z using the modified betas." |
| Step 3 (15 min) | "AI writes code." Icon: terminal. Color CYAN. Example: "def sin2_from_one_loop_crossing_v0(value_dicts):" |
| Step 4 (20 min) | "Human reviews code. Checks logic. Checks for smuggled answers." Icon: magnifying glass. Color GREEN. Example: "Line 47: is this computing or copying?" |
| Step 5 (25 min) | "Human runs code." Icon: play button. Color GREEN. Example: "python data7.py run experiment_beta_unification_v0" |
| Step 6 (30 min) | "Check results against measurement." Icon: checkmark or X. Color GREEN/RED. Example: "[PASS] sin²θ_W: 12 ppm miss." |
| Step 7 (35+ min) | "Iterate: next question, or diagnose failure." Icon: loop arrow. Color GOLD. |
| Bottom annotation | "Same rhythm. 1000 sessions. The human never stops directing. The AI never starts directing." |
| What text cannot show | The time flow — the session as a series of steps with specific durations and roles. The visual rhythm communicates "this is a disciplined process, not random prompting." |

**Diagram V12: Confident Wrongness — The Dangerous Failure Mode**

| Property | Value |
|---|---|
| Type | Comparison Bar (two panels) |
| Size | 18 × 9 |
| Title | The AI's Most Dangerous Failure: Confident and Wrong |
| Left panel "Obvious error" | AI output: "Error: division by zero at line 34." Color RED. Label: "Easy to catch. The system tells you." Status: "Caught immediately." |
| Right panel "Confident wrongness" | AI output: "The Weinberg angle is given by sin²θ_W = 3/8 at tree level, which gives 0.375." Delivered with full confidence. No hedging. But wrong for the context (tree level vs measured). Color GREEN text but with a subtle RED border. Label: "Looks correct. Sounds confident. The context is wrong. The human must know enough physics to catch this." |
| Bottom annotation | "The AI never says 'I'm not sure about this.' It produces wrong answers with the same confidence as right answers. The human's job is to know the difference." |
| What text cannot show | The visual confidence — the right panel looks green and authoritative, but the red border signals hidden danger. The deceptive appearance IS the failure mode. |

---

### Section: The Bias Problem

**Diagram V13: Institutional Bias in the Training Data**

| Property | Value |
|---|---|
| Type | Progression/Sequence |
| Size | 18 × 10 |
| Title | The Institution Trained Its Own Opposition |
| Layout | Circular flow |
| Node 1 "Institution" | "Publishes papers, textbooks, Wikipedia." Icon: university. Color DIM. |
| Node 2 "Training data" | "Millions of documents encoding institutional assumptions." Icon: database. Color DIM. |
| Node 3 "LLM" | "Trained on institutional output. Defaults to institutional positions." Icon: AI chip. Color CYAN. |
| Node 4 "Human" | "Pushes back. Identifies biases. Names them. Reframes." Icon: person. Color GOLD. |
| Node 5 "Better articulation" | "Every bias identified makes the critique clearer." Icon: light bulb. Color GREEN. |
| Arrow from 5 back to 4 | "The AI is a sparring partner whose biases are the institution's biases." |
| Institutional defaults listed | "G is constant", "Forces don't unify at one-loop", "Entropy dominates", "New physics requires new forces". Color RED, each in a small box. |
| Bottom annotation | "Over 1000 sessions of pushing back against institutional defaults, the human learned to articulate exactly where the institution's assumptions fail." |
| What text cannot show | The circular training loop — institution → data → AI → human pushback → better critique. The cycle communicates "the bias is a feature, not a bug, because it sharpens the critique." |

**Diagram V14: Five Institutional Defaults the Human Overrode**

| Property | Value |
|---|---|
| Type | Comparison Bar (two columns) |
| Size | 18 × 10 |
| Title | AI Default vs Human Override |
| Layout | Five rows, each showing an AI default and the human's replacement |
| Row 1 | AI: "Use float64 for all computation." → Human: "Use Fraction. Preserve integers." Color DIM → GOLD. |
| Row 2 | AI: "The forces don't unify exactly." → Human: "They unify if the gap is an exact Fraction." Color DIM → GOLD. |
| Row 3 | AI: "Dark matter is weakly interacting particles." → Human: "Dark matter is toroidal circulation energy." Color DIM → GOLD. |
| Row 4 | AI: "Use standard physics terminology." → Human: "Three nouns, two verbs. Rectification of Names." Color DIM → GOLD. |
| Row 5 | AI: "Present the 725 ppm match as a result." → Human: "Block it. p = 0.81. Not statistically significant yet." Color DIM → GOLD. |
| Each row | Left (AI default) in DIM. Right (human override) in GOLD. Arrow between. |
| Bottom annotation | "The AI defaults to the consensus because the consensus is the training data. The human provides the independent judgment that the training data cannot." |
| What text cannot show | The systematic overriding — five rows of dim-to-gold transitions. The visual pattern communicates "the human consistently replaced institutional defaults with independent judgments." |

---

### Section: The Disclosure Standard

**Diagram V15: The AI Disclosure Template**

| Property | Value |
|---|---|
| Type | Identity Card |
| Size | 16 × 10 |
| Title | Every Paper's AI Disclosure |
| Layout | A paper header displayed |
| Title line | "PHYS-42: Reading Depth Across the Soliton Hierarchy" — GOLD |
| Author line | "Geoffrey Howland and Claude Opus 4.6" — WHITE |
| Disclosure block | "AI Usage Disclosure: Only the top metadata, figures, refs and final copyright sections were edited by the author. All paper content was LLM-generated using Anthropic's Claude Opus 4.6." — CYAN, boxed. |
| Annotations | Arrow to disclosure: "Present on every paper. Same wording. Same position. Not hidden in supplementary material. Not in fine print. First thing you see after the title." |
| Bottom annotation | "This should be the standard, not the exception. The reader knows what they're evaluating. The human gets credit for direction. The AI gets credit for computation." |
| What text cannot show | The actual disclosure as it appears in the paper — the visual placement at the top of the page, in a box, impossible to miss. The formatting IS the standard being proposed. |

**Diagram V16: What Honest vs Dishonest Disclosure Looks Like**

| Property | Value |
|---|---|
| Type | Comparison Bar (three panels) |
| Size | 18 × 9 |
| Title | Three Levels of AI Disclosure |
| Panel 1 "Hidden" | A paper with no AI mention anywhere. Searched: "AI" not found. "Claude" not found. "Language model" not found. Color RED. Label: "Reader assumes human did everything. Dishonest if AI contributed substantially." |
| Panel 2 "Footnote" | A paper with "AI-assisted editing" in footnote 47 on page 23. Color ORANGE. Label: "Technically present. Practically invisible. Plausible deniability." |
| Panel 3 "RUM standard" | A paper with the AI disclosure block at the top, same size as the abstract. Both names on the author line. Color GREEN. Label: "Impossible to miss. Division of labor documented. Reader informed." |
| Bottom annotation | "If honesty about AI is a reason to be dismissed, the dismissal tells you more about the institution than about the work." |
| What text cannot show | The three visual densities of disclosure — nothing vs tiny footnote vs prominent header. The eye immediately reads the gradient from hidden to visible. |

---

### Section: The Future

**Diagram V17: The 10× Multiplier**

| Property | Value |
|---|---|
| Type | Comparison Bar |
| Size | 16 × 10 |
| Title | The Collaboration Multiplier |
| Layout | Three horizontal bars |
| Bar 1 "Human alone" | Length 1×. Color DIM. Label: "Correct direction. Slow execution. Years per framework." |
| Bar 2 "AI alone" | Length 0×. Color RED. Label: "Fast execution. No direction. Produces whatever you ask, never asks the right question." Effectively zero useful length. |
| Bar 3 "Human + AI" | Length 10×. Color GOLD. Label: "Correct direction × fast execution. 53 values across 9 domains in 6 days." |
| Annotation on bar 2 | "Zero isn't harsh. The AI would compute QED coefficients all day without ever deciding to check them against measurement. Direction is everything." |
| Bottom annotation | "The person who figures out how to collaborate effectively with AI will outproduce the person who doesn't by an order of magnitude. This book is the proof of concept." |
| What text cannot show | The zero-length bar — the AI alone bar being zero (or nearly so) communicates "speed without direction = nothing" more forcefully than any argument. |

**Diagram V18: The Future Division of Labor**

| Property | Value |
|---|---|
| Type | Connection/Integer Map |
| Size | 18 × 10 |
| Title | The Future of Scientific Research |
| Layout | Two columns with connecting arrows |
| Left column "Human provides" | "Direction: what questions to ask" (GOLD), "Values: what to publish, what to kill" (GOLD), "Methodology: fractions, test suite, kill switches" (GOLD), "Verification: read the code, catch the errors" (GOLD), "Judgment: is this coincidence or physics?" (GOLD). 5 boxes. |
| Right column "AI provides" | "Computation: 200-digit precision" (CYAN), "Speed: 60 papers in 8 days" (CYAN), "Literature: 9 domains traversed" (CYAN), "Drafting: papers, code, specifications" (CYAN), "Consistency: never tired, never forgets a factor" (CYAN). 5 boxes. |
| Center | Bidirectional arrows between each pair. Label: "Neither can do what the other does. Both are necessary. Both are credited." |
| Bottom annotation | "This is what the future looks like. Not AI replacing humans. Not humans ignoring AI. Collaboration with honest attribution." |
| What text cannot show | The balanced pairing — five human capabilities matched with five AI capabilities. The visual symmetry communicates "equal in importance, different in kind." |

---

### Section: Close

**Diagram V19: The Numbers Don't Change**

| Property | Value |
|---|---|
| Type | Identity Card |
| Size | 16 × 10 |
| Title | The AI on the Cover Doesn't Change the Fractions |
| Layout | Three rows showing results with attribution |
| Row 1 | "α⁻¹ = 137.035999207. Miss: 0.007 ppb." On the right: "Computed by AI. Directed by human. Verified by measurement." Color GOLD. |
| Row 2 | "sin²θ_W = 0.23122. Miss: 12 ppm." Same attribution. Color CYAN. |
| Row 3 | "D/H = 2.531 × 10⁻⁵. Miss: 0.12σ." Same attribution. Color GREEN. |
| Center text | "The numbers match or they don't.\nThe AI on the cover doesn't change the fractions.\nThe fractions are checkable regardless of who or what produced them." — GOLD, large. |
| Bottom annotation | "Check the numbers. That's all that matters." |
| What text cannot show | The results with attribution — each result carries its origin (AI computed, human directed, measurement verified) and the numbers are the same regardless. The visual repetition of "same result, same verification" communicates "authorship doesn't affect truth." |

**Diagram V20: The Timeline — CKS to RUM**

| Property | Value |
|---|---|
| Type | Progression/Sequence (timeline) |
| Size | 18 × 9 |
| Title | From Failure to Framework: The Complete Timeline |
| Layout | Horizontal timeline |
| Period 1 "Jan-Feb 2026" | "CKS: 45 days, 363 papers." Color CYAN. |
| Event 1 "Feb 2026" | "Circular reference found. AI's mistake, human's catch." Color RED. Icon: X. |
| Event 2 "Feb 2026" | "363 papers killed on Zenodo." Color RED. Icon: skull. |
| Period 2 "Mar 2026" | "RUM: 6 days, fractions, Q335, test suite." Color GOLD. Label: "Every innovation came from the CKS failure." |
| Period 3 "Mar-Apr 2026" | "8 sessions, 60+ papers, 253 comparisons, 9 domains." Color GREEN. |
| Current | "April 2026: This video." Color GOLD star. |
| Annotations | CKS failure → "Lesson: read the code" → "Lesson: use fractions" → "Lesson: automate testing" → "Lesson: publish failures" |
| Bottom annotation | "The failure was the teacher. The AI was the tool. The human was the student who learned and changed the methodology." |
| What text cannot show | The timeline with the failure at the center — the CKS kill is the pivot point from which everything else flows. The visual placement of the RED event as the turning point communicates "failure drove success." |

---

**Total: 20 diagram data tables across 9 sections. Each table gives a new Claude the type, layout, data, colors, annotations, and what the diagram communicates that text cannot.**

