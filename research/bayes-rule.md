# Bayes' rule

Type: Theorem.

## Material checked

- The generated article before this edit had 931 body words, no figures, the event and density statements, the restricted-prior worked question, nine distinct question links, and a collapsed proof. The event formula omitted the positive-probability condition needed to define $P(B\mid A)$.
- `sources/book/chapters/bayes-01-foundations.qmd`, `theorem_depth.py`, the article's citation map, and the linked question and answer.

## Sources opened and used

1. Thomas Bayes, [“An Essay towards solving a Problem in the Doctrine of Chances”](https://bayes.wustl.edu/Manual/an.essay.pdf), *Philosophical Transactions* (1763), pp. 370–372. Price's opening letter names the repeated-success question and the posthumous communication. Key `bayes1763` is used only for this history.
2. He Wang, [*Foundations of Probability and Statistical Theory*](https://wanghemath.github.io/Book-ProbabilityStatisticalTheory/chapters/chapter-01-basic-probability.html), Chapter 1 §2.11.2, Theorem 45 and §2.12.1, Example 46. Read the finite-partition formula, proof and diagnostic-test interpretation. [Chapter 20 §23](https://wanghemath.github.io/Book-ProbabilityStatisticalTheory/chapters/chapter-20-bayesian-inference.html), Definitions 1–4, gives the prior, likelihood, marginal and posterior. Key `wang2025_foundations`.
3. Peter Hoff, [“Bayes estimators”](https://www2.stat.duke.edu/~pdh10/Teaching/581/LectureNotes/Static/bayes.pdf), §2.2, pp. 3–4. Read the prior-predictive and posterior-density definitions. Key `hoff2013_bayes_estimators`.
4. Robert Kass and Adrian Raftery, [“Bayes Factors”](https://sites.stat.washington.edu/courses/stat527/s13/readings/KassRaftery_jasa1995.pdf), *JASA* **90** (1995), §3.1, pp. 777–778. Read the posterior-odds and marginal-likelihood model-comparison passage. Key `kass_raftery1995`.

The inherited Laplace and Jeffreys references were bibliography-only citations with no checked passage for this article; the generated article now uses the opened Wang and Hoff passages. Gelman's book was read during the normal-distribution pass, but the Bayes statements here use more precise locations in Wang and Hoff.

## Changes and checks

- Added a reader-facing lead context, symbol definitions, a finite-partition result, the prior-support consequence, one collapsed proof of the event and density forms, a numerical diagnostic-test example, statistical applications, and two sourced history paragraphs. The earlier repetitive history sentence and sketch were replaced by a complete, located account and proof.
- Corrected the event formula's conditions in the shared source chapter and added located citations there. The theorem template gained page-specific research slots because result articles did not previously read `research/content/<slug>.md`; the other result pages retain their existing order and content.
- The original restricted-prior question, its answer, the infobox values, and all nine question links remain. No figures existed. `checks/bayes-rule.py` verifies the exact printed counts and rounded probabilities, the single Proof box, and the article's source keys.
- Generated article: 1,904 body words, no figures, one Proof callout. The build produced 718 articles and 557 question pages; all 67 Python tests and offline verification of 408 bibliography entries pass. The global proofs todo has 94 entries, none for this article.
