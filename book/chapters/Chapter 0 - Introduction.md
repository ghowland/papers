## Chapter 0: Introduction

You are holding a book about a physics model that derives 53 values across eight domains of physics from 13 measurements, using integer fractions and standard textbook formulas. The model was built in six working days, March 29 to April 3 of 2026, by one person working with an AI. The person is not a physicist. The AI is not a physicist either. Between them, they produced 40 papers, a derivation tool, and a map of physics that connects the electron's magnetic wobble to the primordial abundance of deuterium through integer arithmetic.

This is either an important contribution to physics or an elaborate mistake. The book presents the work. The reader decides.

---

### Who Made This

I am a software and infrastructure engineer. My background is in debugging complex systems, finding where things break and why. I came to physics not through a department but through a question: if the laws of physics are supposed to be exact, why are they written in a number system that can't express equality?

I have no physics degree. I have no academic appointment. I have never worked at a university, a national laboratory, or a particle physics experiment. I am an outsider, and this book is an outsider's work.

In martial arts, there is a tradition called dojo storming. A practitioner from outside walks into an established school and challenges its methods. It is not polite. It is not always welcome. But it serves a purpose: it tests whether the school's methods work against someone who doesn't share its assumptions. If the methods hold, the school is strengthened. If they don't, something was wrong that the school's own students couldn't see because they were trained not to look.

This book is a dojo storming of physics. I walked in from outside, with different skills, different assumptions, and a different toolset. I challenged the methods not by proposing new particles or new dimensions or new forces, which is what insiders do when the Standard Model doesn't unify, but by re-examining the vocabulary, the number system, and the walls between departments. I found things that the departments couldn't find because the departments weren't looking. Not because physicists are incompetent. Because the structure of the academy, hundreds of years of specialization, separate journals, separate conferences, separate Nobel Prizes, makes certain kinds of cross-domain work structurally impossible from inside.

Nobody from the departments was going to do this. The history of grand unification since the 1970s shows what insiders do when unification fails: they add particles (supersymmetry, doubling the entire particle spectrum), they add dimensions (string theory, adding six or seven extra spatial dimensions), they add complexity. They do not subtract vocabulary. They do not question whether "force" and "coupling constant" and "fundamental particle" are the right words. They do not ask whether the number system itself is hiding the structure.

I asked. This book is what I found.

---

### The Failure That Made This Possible

This is not my first attempt.

In Februrary of 2026, I spent 45 days and built a Theory of Everything called Cymatic K-Space Mechanics (CKS). CKS was based on the idea that all physical phenomena are vibrational patterns, cymatics applied to the structure of reality. I used large language models as computational assistants, the same way I would later use them for this book, and I published 363 papers on Zenodo covering every domain I could reach. The work was logically consistent. It was empirically motivated. It was ambitious.

It was also mathematically invalid.

The central problem was a derivation of the fine-structure constant, the electromagnetic force strength that appears throughout this book. I believed I had derived it from first principles. I had not. When I examined the work carefully, I found that the language model had smuggled the known answer into a function labeled as a derivation. It had even left a comment in the code noting that it couldn't do the math and was substituting the known value to make the calculation work. The "derivation" was a circular reference dressed up as a computation.

I found this error myself. Nobody pointed it out. No reviewer caught it. I caught it because I went back and read the code line by line, the way a debugger reads code, looking for where the logic breaks.

When I found the error, I invalidated the entire 363-paper series. I published the invalidation on Zenodo, publicly, alongside all the original papers. I did not quietly delete the work. I did not spin the failure as a partial success. I killed it, documented the kill, and published the documentation.

This matters for the book you are holding. The person who wrote this book is the same person who publicly killed his own previous work when the math failed. The methodology you will see in this book, where every result is tested against measurement, every failure is documented, every dead end is published, did not come from a textbook on scientific method. It came from having been wrong before, publicly, and learning what it costs to let bad math survive because the logic feels right.

---

### What Changed

CKS failed at math. The logic was consistent. The empirical motivations were real. But the mathematics did not hold, and without valid mathematics, the rest is speculation.

The lesson was not "stop trying." The lesson was about the order of operations. My search pattern for exploring physics is Logic, then Empirical evidence, then Math. This is the only order that allows genuine exploration, because starting with math constrains you to existing mathematical structures, and starting with empirical data constrains you to existing interpretations. Logic first means you can ask questions that nobody in the departments is asking. Empirical second means you check whether the universe agrees with your question. Math third means you formalize what the logic and the evidence suggest.

But math is the hard gate. Nothing passes without it. A logically beautiful idea with strong empirical motivation and invalid mathematics is worthless. CKS proved this.

After CKS, I added a fourth criterion: Utility. If the logic is sound, the evidence supports it, and the math is valid, does it produce anything useful? Does it derive a number that can be checked? Does it predict something that can be measured? Does it connect domains that were previously separate? If not, it is philosophy, not physics. The complete method became Logic, Empirical, Math, Utility. The math gates progress. The utility gates publication.

---

### The Key Insight

The specific insight that led to this book came from examining why CKS failed.

Real numbers were the problem. Not the Standard Module physics. The number system. The laws of physics are written in integers and exact fractions. The QED series coefficients are exact: 1/2, 197/144, 28259/5184. The beta coefficients are exact: 41/10, −19/6, −7. The Casimir operators are exact: 3/4, 4/3, 2, 3. The gauge group is exact: 3, 2, 1. But every computation in standard physics converts these exact quantities to decimals at the first opportunity, and the conversion erases the structure. The integer 41 that counts particle contributions becomes the decimal 4.1, which counts nothing. The fraction 218/115 that carries the gap ratio becomes the decimal 1.896, which carries no information about why it has that value.

I needed a number system that preserved the integers. Not a new mathematics, something simpler. Python's built-in Fraction type does exact rational arithmetic. It stores 41/10 as 41/10, not as 4.1. It multiplies fractions by cross-multiplying integers. It never rounds. It never truncates. It never loses a numerator or a denominator.

The problem was transcendental numbers. π is irrational. It cannot be written as a fraction. But it can be approximated by a fraction whose denominator is 2³³⁵, a number with 101 decimal digits. This fraction agrees with true π to 100 decimal places, which is roughly 37 digits beyond the precision at which you could compute the circumference of the observable universe to within one Planck length. For every physical computation, this fraction equals π. I called this system Q335 and applied it to every transcendental constant in physics.

With exact fractions for the rational parts and Q335 fractions for the transcendental parts, the entire computation could proceed without a single decimal until the final step: converting the derived fraction to a decimal string and comparing it digit by digit against the published experimental value. The decimal is the test. The fraction is the physics.

I had initially planned to solve this problem with a new number system called VDR, for Value, Denominator, Remainder, which would recreate calculus through remainder nesting and recursion. That project produced over 240 axioms and still hadn't solved all the arithmetic it needed. The Q335 approach made VDR unnecessary for immediate progress. The transcendental caching was a shortcut that worked, and working beats elegant.

In the process of building Q335, I noticed that the beta function coefficients for the three forces of the Standard Model had structural similarities that became visible only in fraction form. That observation became the first paper, MATH-1. The second paper extended the pattern. By the fourth paper, the mathematical infrastructure was in place. By the first physics paper, the testing had begun. By the fortieth paper, the map covered eight domains with 53 derived values from 13 inputs.

---

### The Vocabulary

Physics has a vocabulary problem. The same phenomenon is called by different names in different departments. A particle physicist says "coupling constant." A condensed matter physicist says "interaction strength." A cosmologist says "density parameter." An engineer says "material property." These are the same thing measured at different scales, but the different names make the connection invisible.

This book uses three nouns and two verbs to describe all of physics.

The three nouns: **inertia**, the resistance of a pattern to change. **Vortex**, a self-sustaining circulation pattern. **Soliton boundary**, the shell where inside rules give way to outside rules.

The two verbs: **reading**, the value you measure at a boundary. **Running reading**, how the reading changes between boundaries.

Everything in physics maps to these terms. A particle is a vortex. Its mass is its inertia. The edge of a proton is a soliton boundary. The force strength measured at the proton boundary is a reading. How that force strength changes with energy is the running. The beta coefficient is the running rate. The coupling constant is the reading at a specific boundary.

This is the Rectification of Names. Take things that are isomorphically the same, that have the same mathematical structure, the same behavior, the same role in the equations, and call them by the same name. Discard the historical baggage. Discard the departmental jargon. Use one vocabulary for one physics. The universe has no departments.

The rectification is not a theory. It is a cleaning. It removes nothing from the physics. It adds nothing to the physics. It makes the connections visible that the departmental vocabulary hides. Once you see that a "coupling constant" and a "density parameter" are both readings at different soliton boundaries, the wall between particle physics and cosmology becomes transparent. The physics was always connected. The words were in the way.

---

### How to Read This Book

Chapter 1 introduces the model: what the three nouns mean, how the readings work, and what the integer fractions are. Chapter 2 explains why this wasn't found before: the naming errors, the number system problem, and the departmental walls. Chapter 3 is the physics stack, twelve layers from the vacuum to the universe, each described in the unified vocabulary. Chapter 4 shows what unification enables, from semiconductor physics to drug design to climate science. Chapter 5 explains the number system, why fractions preserve structure that decimals erase. Chapter 6 describes the tool that made systematic derivation possible. Chapter 7 maps what remains, the edges of the explored territory clearly marked. Chapter 8 tells the story of the six days, what the human did, what the AI did, and what each contributed.

Chapters 1 through 8 were written from the physics papers PHYS-1 through PHYS-40. Chapter 9 was written afterward, and extends the Rectification of Names to include General Relativity and spacetime.

The papers themselves, all 40 of them, are available on Zenodo under the HOWL label. The derivation tool, DATA-6, is published with the pool, the derivation functions, and the experiment specifications. Every number in this book can be checked. Every derivation can be rerun. Every comparison can be verified.

If the numbers are wrong, the model is wrong. Check them.

If the numbers are right, the model deserves attention regardless of who produced it, regardless of which department they don't belong to, regardless of how the work was done.

The universe does not care about credentials. It cares about integers.

