# Statistic

Type: Concept/definition.

## Existing material read

- `articles/statistic.qmd` before the edit: definition, moments and normal-sample statements, one worked classification question, and 32 linked questions. Leading body: 441 words; no figures.
- `sources/stat2004/chapters/inf-01-statistical-inference.qmd`, its random-sample, statistic, moments, and normal-sample arguments, including the use of an orthogonal rotation.
- `questions/ex-inf-which-are-statistics.qmd` and `questions/ex-inf-expected-sample-variance.qmd`, including hidden answers.

## Sources opened and facts used

1. R. A. Fisher, [“On the Mathematical Foundations of Theoretical Statistics”](https://jhanley.biostat.mcgill.ca/bios601/Likelihood/Fisher1922.pdf), *Philosophical Transactions A* 222 (1922), pp. 309–368, especially pp. 309–316. Read his distinction between estimation and distribution problems and his discussion of reducing samples to statistics, efficiency, and sufficiency. Used for definition, limits, connections, and history. Citation key `fisher1922`.
2. NIST/SEMATECH, [e-Handbook of Statistical Methods, Glossary](https://www.itl.nist.gov/div898/handbook/glossary.htm), first published 2002. Read entries “data reduction,” “sampling distribution,” “standard error,” and “statistic.” Used for the motivation and sampling interpretation. Citation key `nist_glossary2002`, added in this commit.
3. Kyle Siegrist, [“Special Properties of Normal Samples”](https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/06:_Random_Samples/6.08:_Special_Properties_of_Normal_Samples), in *Probability, Mathematical Statistics, and Stochastic Processes*, Statistics LibreTexts, page dated 2022. Read the original [Random Services chapter](https://www.randomservices.org/random/sample/Normal.html) as well, especially its proofs of sample-mean normality, mean/variance independence, and the chi-squared residual law. Used for the proof and statistical-use section. Citation key `siegrist2022_normals`, added in this commit.

## Verification and decisions

- The existing definition, both properties, example, citations, and question links are preserved. No content or figure was removed.
- One collapsed proof covers all three moments identities without normality and all three parts of the normal sample theorem by orthogonal rotation. The $t$ statement in statistical use follows from the same two independent components.
- Every new numeric sample summary and challenge was recomputed exactly in `checks/statistic.py`.
- The lead now uses “a statistic” and states its inferential purpose in words; the unknown-parameter distinction remains in the Definition.

## Correction pass

- Replaced unopened Casella–Berger, Wasserman, Lehmann–Casella, and Fisher 1925 citations in the extracted statistic and normal-sample statements with the Fisher 1922, NIST glossary, and Siegrist passages actually read. Every new citation has a source location.
- Added citations to the lead context, motivation, worked example, and hidden answer. Rephrased page-assembly language and kept History to the Fisher 1922 development. The arithmetic check now asserts the values and classification shown on the page.
