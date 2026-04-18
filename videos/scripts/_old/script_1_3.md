
# 1 - 5 minute
## Figures: 15, 16


- This model predicts 1 new particle.  Not by choice, it was a mathematically forced selection, as the only set of integer fractions that met all the requirements to complete the standard model GUT unification.

- I repeat, I did not choose this particle to create a new particle, I did an experiment where I tried to derive all the integers that could make close GUT unification, while being small, and having compositions that match particle physics requirements with valid gauge group representations.  This is a lot of constraints, not a numerology search, but a constraint driven search that produced a vector-like two-handed (left and right chirality) doublet, that I have named the "Cabibbo Doublet".

- This was named after the Cabibbo Angle, for quark mixing which he discovered in 1963.  After I named after his mixing angle and the "doublet" for "the gauge groups SU(2) representation, under the weak force group", I learned more about Nicola Cabibbo's history and that he was not included in a nobel prize that extended his original research.  Now I think it's a fitting name, if the predicted particle is confirmed by experiment, his work gets its legacy.

- The Cabibbo Doublet prediction is testable, and the Hyper-Kamiokande experiment in Japan starts in 2027.  If protons decay at the predicted 3 × 10^34 to 10^35 years in the p → e⁺π⁰ channel.  

- A proton (p) decays by breaking into a positron (e⁺, an anti-electron) and a neutral pion (π⁰, a short-lived particle made of a quark and antiquark), with the arrow meaning "decays into" and the whole expression describing one specific break pattern — the "channel" — out of several possible patterns different unification models predict.


- If it isn't confirmed, then I will falsify the prediction, and invalidate any paths of the series that relied on it.  The same way I did with CKS.



The standard term is beta coefficient shifts:
	- 
	- more specifically, "one-loop beta coefficient shifts" if you want to be precise).
	- The quantities Δb₁, Δb₂, Δb₃ are the shifts to the three one-loop beta coefficients contributed by adding the Cabibbo Doublet to the Standard Model's particle content.



# 2 - 4 minute
## Figures: 17, 18



- This is the experiment system used in the book, which is Data-6, but I cloned it to Data-7 so I can keep working and demo it without messing up the book's reference point.  So we will be using Data-7 python scripts.

- Just like you want tests for production software to ensure its repeatable and to verify computationally without human error, I built the same kind of system for my integer physics experiments.

- Its a python system that loads programs, experiments, values, and their result values and result reports from and to JSON.  All the inputs are stored as integer fractions, with provenance as to where they came from, what type of data the source was, a decimal, approximate or exact fraction, but they are all computed as fractions with Python Fraction library until they finally converted using mpmath to 50 or 100 digits to compare against the measured decimal values by string comparison.

- As of the book, there were 36 experiments with 253 comparisons.  Each comparisons takes a predicted value and compares it to a measured value, and if it passes to the precision the comparison required (N digits), it gets a PASS, if it is marginal it gets an INFO, if it is outside margin it gets a FAIL.  Runs are incremental data, they are never deleted, so if the experiment gets changed, we keep all the run data and can inspect the history, which is useful to fix problems and trace how the solution evolved.

- The reason I am confident that this is a strong model is because all of this is so simple.  I load integer fractions from JSON, I do computation on this from the standard model equations, and then save them and then compare them to the saved measured values, and if they match, thats a PASS.  If they dont, thats a FAIL.  Both are good information, and so I have been able to work quickly, and produce enough to make over 50 papers and a book about Integer Physics worth sharing.

- The Data-7 tool allows anyone to jump in and make their own experiments by hand editing the JSON and writing your own python or getting AI assistance to do it.  Feeding my papers to the AIs will get their context set up so that they can use standard model solutions with integer fractions to write Python Fraction only code, and test it.



# 3 - 2 minute
## Figures: 19, 20


- By the end of the book, around April 10th, here's what the project had achieved:

- 53 values prediction through derivation, from 13 integer fraction inputs across 9 areas of physics.  253 comparisons, all documented and reprodicble and public on Gitub and published on Zenodo.  In the code on Github, you can read the derivations, they are from the standard model.  The Kindle book is out for $2.99, the minimum price I could set for the widest distribution channels.

- This model is replicatable, extendible, and it's simple.  It's not new physics, even the newly predicted particle is forced from existing physics rules, not something I have added.  

- Next week we start the second chapter, why nobody found this before.


