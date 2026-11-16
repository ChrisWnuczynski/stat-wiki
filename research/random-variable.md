# Random variable

Type: Concept/definition.

## Existing material read

- articles/random-variable.qmd before the edit: a real-valued function definition, CDF, discrete and continuous laws, the mass/density/CDF figure, an expectation-of-a-function property and discrete proof, a two-toss example in Interpretation, four inline citations, and nine linked questions. Leading body: 872 words; one figure.
- sources/stat2003/chapters/prob-02-random-variables.qmd for the original definitions and figure; sources/stat3004/chapters/sp-10-random-variables.qmd for the measurable-map formulation and law; relevant linked question pages, including ex-prob-three-point-expectation.qmd and c-42.qmd.

## Sources opened and facts used

1. Andrey Kolmogorov, [*Foundations of the Theory of Probability*, English translation of the 1933 original](https://www.stat.yale.edu/~pollard/Courses/600.spring2018/Handouts/Foundations1933.pdf), Chapter III §2. Read the definition as a function whose strict-threshold preimages are events, its distribution-function convention, and its use of the induced probability law. Existing key kolmogorov1933_slln.
2. Patrick Billingsley, [*Probability and Measure*, 3rd edition](https://www.colorado.edu/amath/sites/default/files/attached-files/billingsley.pdf), §§13–14 and 20. Read the measurable-map definition, preimages of Borel sets, composition theorem, distribution or law, CDF, and density discussion. Existing key billingsley1995.
3. Rick Durrett, [*Probability: Theory and Examples*, 5th ed.](https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf), Chapter 1 §§1.1–1.3, 1.6 and Chapter 2 §2.1. Read the probability-space and discrete-law definitions, expected-value formulas, and independence rules used in the coin and dice examples. Existing key `durrett2019`.
4. Charles M. Grinstead and J. Laurie Snell, [*Introduction to Probability*](https://math.dartmouth.edu/~prob/prob/prob.pdf), Chapter 6 §6.1. The discrete-variable and mass-function material was opened during the Expectation correction. Existing key `grinstead_snell1997`.
5. NIST/SEMATECH, [e-Handbook of Statistical Methods, Glossary](https://www.itl.nist.gov/div898/handbook/glossary.htm), entries “statistic” and “sampling distribution.” Existing key `nist_glossary2002`, opened during the Statistic correction.

## Verification and decisions

- The hand-specified lead uses “a random variable.” The article includes a measurable-map Definition, transformation and expectation Properties, Statistical use, a two-dice Worked example, misconceptions, limits, connections, and two cited History paragraphs. The Interpretation keeps its two-coin worked example.
- A single collapsed Proof box establishes measurable transformations, the expectation transfer formula in discrete and continuous cases, CDF properties and the converse construction. The existing discrete grouping proof remains.
- The original source chapter asserted that a density equals the CDF derivative at every differentiability point. This is false for an arbitrary representative of a density. The source sentence was corrected to equality almost everywhere; its density definition and example remain.
- The source correction also affects the generated Continuous distribution page. Its body is 486 words versus its 475-word preservation baseline after adding an explanation of why equality is only almost everywhere. The first rebuild flagged a five-word loss there; the explanatory sentence resolved it, and all 63 tests pass.
- `checks/random-variable.py` enumerates the two-toss and two-dice examples with exact rational probabilities and asserts the printed values.
- The CDF, discrete and continuous definitions, figure, two-toss example, and nine question links remain. Citations to unopened Casella–Berger, Feller, Laplace, and Grimmett–Stirzaker were replaced in the researched prose and inherited definitions with located Kolmogorov, Billingsley, Durrett, and NIST references. The added link-only question list and history disclaimer were removed. The shared discrete definition gained a located Grinstead–Snell citation to keep its dependent article above the inline-citation floor.
