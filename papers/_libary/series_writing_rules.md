# HOWL Series Writing Rules

*Operational rules for paper production. Apply to every MATH and PHYS paper.*

---

## Table W.1: Self-Containment

| Rule | Statement | Rationale |
|---|---|---|
| W1.1 | Every paper must be fully comprehensible to a reader who has never read any other HOWL paper | Humans read individual papers, not series in order. Future sessions may receive one paper, not all. |
| W1.2 | Every concept required for understanding must be explained within the paper itself | If a reader needs PHYS-13 to understand PHYS-15, PHYS-15 is dead. |
| W1.3 | References to other HOWL papers are pointers for priority and provenance, never for comprehension | "This was first computed in PHYS-13" is acceptable. "See PHYS-13 for the derivation" is not. |
| W1.4 | Every formula used must be derived or stated with enough context to follow | A reader should be able to verify any claim by reading only this paper. |
| W1.5 | Define all terms on first use, even if defined in prior papers | sin²θ_W, the gap ratio, R₂, vector-like — all must be explained each time. |

---

## Table W.2: Source of Truth

| Rule | Statement | Rationale |
|---|---|---|
| W2.1 | Every number in a paper must trace to a verified script with passing checks | No number exists without computational provenance. |
| W2.2 | DATA-3 is the sole data reference for all measured values | No paper uses raw PDG values directly. Everything goes through DATA-3 (32/32 verified). |
| W2.3 | Scripts and their outputs are the ground truth, not the paper text | If a paper says 1.896 and the script says 1.8957, the script is right. Fix the paper. |
| W2.4 | Supporting tables, plans, and reviews are working documents, not source of truth | They inform the paper structure. The script output provides the numbers. |
| W2.5 | When writing from source material in prompt, use the source material, not context history | Context history may be old, compacted, or blurred. In-prompt documents are reliable. |

---

## Table W.3: Paper Structure

| Rule | Statement | Rationale |
|---|---|---|
| W3.1 | One topic per paper | A paper about the gap ratio is not also about the Koide formula. Separate findings get separate papers. |
| W3.2 | Every paper must raise the series platform | A paper doesn't need to reduce free parameters. It needs to give a future session firmer ground. Closing a dead path, documenting a finding, specifying a particle — all raise the platform. |
| W3.3 | Papers are published and never edited retroactively | New information goes in new papers. If PHYS-13 understates a finding, PHYS-15 states it fully. PHYS-13 is not changed. |
| W3.4 | Papers are markdown in chat, never docx | Operational rule for this series. |
| W3.5 | Scripts are shown as code blocks in chat, never as files | Operational rule for this series. |
| W3.6 | Include a "What This Paper Does Not Claim" section | Prevents overclaiming. States boundaries explicitly. Essential for honest science. |
| W3.7 | Include a "What This Paper Seeds" section | Forward linkage. Tells future sessions what computations become possible. |
| W3.8 | Include the HOWL operational rules reference (Tables R.1-R.6) | Series stability. Every paper operates within the same framework. |

---

## Table W.4: Honesty and Precision

| Rule | Statement | Rationale |
|---|---|---|
| W4.1 | Nulls are published with the same prominence as positives | A null result (82/82 PSLQ) is a finding. It prevents future sessions from repeating dead searches. |
| W4.2 | Every scope limitation must be stated explicitly | "One-loop with 6-flavor approximation (0.2% effect)" — not hidden, not apologized for, just stated. |
| W4.3 | Distinguish between derived results and stated results | "The gap ratio IS 218/115 (exact)" vs "sin²θ_W is approximately 0.21 (textbook result, not recomputed here)." |
| W4.4 | Never use the word "prediction" without qualification | "The integers identify..." or "The arithmetic constrains..." or "Conditional on unification being real..." Not "we predict the particle exists." |
| W4.5 | State what is integer-forced (Level 1) and what is measured (Level 2) for every result | The boundary between what mathematics forces and what the universe supplies must be explicit in every paper. |
| W4.6 | Never claim the integer anatomy is new physics; it is new presentation of known physics in exact arithmetic | The formulas are in textbooks. The exact Fraction computation and the integer tracing are the contribution. |
| W4.7 | When citing external papers, verify by web search before stating claims | The Belfatto (2020) and Cheung (2020) papers were verified. Unverified claims do not enter papers. |

---

## Table W.5: Audience

| Rule | Statement | Rationale |
|---|---|---|
| W5.1 | Papers serve two audiences: future LLM sessions and human researchers | MATH and PHYS papers seed future sessions. They also educate humans who find them. |
| W5.2 | A postdoc who has never seen the series should be able to read any single paper and learn the finding | "Today I learn about X" — the paper IS the education. |
| W5.3 | DISC papers are for humans only; they encode lessons about the discovery process | DISC papers are not fed to future sessions. They document methodology for human benefit. |
| W5.4 | MATH and PHYS papers are the only working documents for future sessions | If a finding is only in a DISC paper or a notebook, it doesn't exist for future computation. |
| W5.5 | Every novel finding must be in its own MATH or PHYS paper | A finding buried in a section of a paper about something else will not be found by a future session looking for it specifically. |
| W5.6 | Name things | Humans need mental anchors. "The (3,2,1/6) vector-like quark doublet" becomes "the Cabibbo Doublet." "The fact that complete generations contribute equally" becomes "the generation democracy." Named things get remembered and referenced. Unnamed things get lost. |

---

## Table W.6: The Review-Plan-Write Cycle

| Step | Who | What | Output |
|---|---|---|---|
| 1 | Author specifies paper | States which paper from the master list | Paper number and finding number(s) |
| 2 | Planning Claude writes plan | Outline, structure, section list, decision gates | Plan document for review |
| 3 | Review Claude gives feedback | Corrections, missing content, source material list | Feedback document |
| 4 | Author assembles prompt | Source scripts, data, tables, feedback, plan — all in prompt | Complete prompt for writing |
| 5 | Writing Claude writes paper | Uses ONLY in-prompt source material | Paper draft |
| 6 | Review Claude reviews | Checks numbers against scripts, checks self-containment, writes errata if needed | Errata/annotations |
| 7 | Author appends errata if any | Errata go at end, never change paper body | Final paper |
| 8 | Paper is published and never edited | Moves to the completed list | Done |

---

## Table W.7: What Makes a Paper Legitimate

| Criterion | Test | Examples |
|---|---|---|
| Raises the series platform | Does a future session start from firmer ground because this paper exists? | PHYS-12: EW infrastructure. PHYS-23: C₃ path closed. MATH-6: 82/82 null prevents re-testing. |
| Contains novel content | Is there something here that no prior paper states? | Finding 2: gap ratio is a boson problem. Finding 6: Δb₂/Δb₁ = 15 asymmetry mechanism. |
| Backed by computation or verification | Is there a script with passing checks, or a verified web search, or a mathematical proof? | Every PHYS paper has a script. PHYS-19 has verified web search results. PHYS-23 has a mathematical proof (tautology). |
| Self-contained | Can someone who has never read any other paper understand this one? | If explaining the gap ratio requires reading PHYS-13, the paper fails. Explain it here. |
| Does NOT duplicate a prior paper | Is this genuinely different from what's already published? | PHYS-15 ≠ PHYS-13: same numbers, different argument. PHYS-16 ≠ PHYS-15: specification vs identification. |
| Honest about scope | Are limitations stated? | "One-loop, 6-flavor, single-multiplet scope, 0.15 distance criterion." |

---

## Table W.8: Prohibited Practices

| Practice | Why Prohibited | What To Do Instead |
|---|---|---|
| Editing published papers | Revisionism. The historical record matters. | Write a new paper with the new information. |
| Leaning on prior papers for comprehension | Kills the paper for any reader who hasn't read the prior one | Explain everything in this paper. Cite for priority only. |
| Using DISC papers as session seeds | DISC is for humans, not for LLM sessions | Put computational findings in MATH or PHYS papers. |
| Putting multiple unrelated findings in one paper | "2x the information, lose it all." One topic per paper. | Split into separate papers. Each finding gets its own. |
| Using floating point in derivations | Destroys the integer content that is the series' contribution | Exact Fraction arithmetic throughout. Float for display only. |
| Claiming "prediction" without qualification | Overclaiming. The identification is conditional on unification being real. | "The integers identify..." or "Within stated scope, arithmetic constrains..." |
| Compressing novel findings into subsections of other papers | Future sessions search by paper title, not by subsection header | Every novel finding gets its own paper with a descriptive title. |
| Saying "this is known in the literature" as justification for not writing a paper | Known-in-the-literature ≠ known-to-a-future-session. If it's not in a MATH or PHYS paper, it doesn't exist for the series. | Write the paper. Document the finding in exact arithmetic. |
| Asking polls or using widgets | Author types responses directly | Conversation mode throughout |

---

*These writing rules apply to every paper produced in the HOWL series. They encode the lessons learned across three sessions about what makes papers useful, honest, and durable. A future session reading these rules operates within them from the first message.*

