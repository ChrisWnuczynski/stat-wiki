# Cumulative distribution function

Type: Concept/definition.

## Existing material read

- articles/cumulative-distribution-function.qmd before the edit: CDF definition, inverse-transform property, two figures (mass/density/CDF comparison and inverse transform), a cubic-CDF worked problem, a maximum-CDF worked problem, seven cited works, and sixteen linked questions. Leading body: 431 words; two figures.
- sources/stat2003/chapters/prob-02-random-variables.qmd for the definition, endpoint formula, and mass/density comparison; sources/stat2003/chapters/prob-03-simulation.qmd for inverse-transform simulation; sources/stat3004/chapters/sp-10-random-variables.qmd for measurability, jumps, and endpoint conventions; sources/using-r/chapters/ur-02-probability-and-simulation.qmd for the empirical CDF.
- questions/ex-sp-right-continuous.qmd, questions/ex-prob-cubic-cdf.qmd, and questions/ex-prob-cdf-of-maximum.qmd, including their worked answers.

## Sources opened and facts used

1. Andrey Kolmogorov, [*Foundations of the Theory of Probability*, English translation of the 1933 original](https://www.stat.yale.edu/~pollard/Courses/600.spring2018/Handouts/Foundations1933.pdf), Chapter III §2. Read the definition of a distribution function as $P(X<x)$, the resulting left-continuity, the $[a,b)$ interval convention, and the statement that it determines the Borel law. Existing key kolmogorov1933_slln identifies the original work; the opened copy is a later English edition.
2. Patrick Billingsley, [*Probability and Measure*, 3rd edition](https://www.colorado.edu/amath/sites/default/files/attached-files/billingsley.pdf), §§12 and 14. Read the modern $P(X\le x)$ definition, jump size, four characterizing properties, measure construction, and both proofs of the generalized-inverse construction. Existing key billingsley1995.
3. The source chapters retain Feller, Grimmett–Stirzaker, Ross, and Durrett as standard references for their existing material. Their full book texts were not opened for this page; the key CDF and inverse results were checked against the opened Billingsley text and are proved in the new box.

## Verification and decisions

- The new sections add a precise Definition, Properties, Interpretation, Statistical use, a mixed-law Worked example, Common misconceptions, Assumptions and limits, Connections, Check yourself, and two cited History paragraphs. Lead context and a motivating example make the topic concrete before formulas.
- One collapsed Proof box covers monotonicity, right-continuity, limits, interval and atom formulas, the inverse-transform construction and converse CDF characterization, and the original maximum-CDF result. Density differentiation is stated almost everywhere, avoiding a false pointwise claim for arbitrary density representatives.
- The history explicitly distinguishes Kolmogorov's strict-inequality, left-continuous convention from this site's right-continuous convention. It does not claim who first introduced distribution functions or when the inequality convention changed.
- The existing generator already had an Interpretation slot but did not accept researched prose for it. A two-line build_wiki.py change now admits that subsection and puts its explanation before the retained inverse-transform figure. No unrelated template behavior was changed.
- checks/cumulative-distribution-function.py uses exact fractions for the new mixed-law example, the retained cubic-CDF problem, the retained maximum problem, and discrete inverse behavior.
- Both original figures, both original worked examples, their citations, and all sixteen question links remain. No figure, definition, example, or practice question was removed.
- A single-page Quarto render produced no HTML after roughly two minutes and was stopped; the generator, Python suite, arithmetic checks, and offline citation check completed.
