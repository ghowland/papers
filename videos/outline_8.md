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
