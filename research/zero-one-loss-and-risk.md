# Zero–one loss and risk: source and verification notes

Type: concept/definition. Baseline: 507 words, zero figures. Preserve its indicator and one-hot form, conditional-risk formula, three-class $(0.7,0.2,0.1)$ and unequal-cost comparison $(1.1,0.8,1.7)$, infobox and existing Wald/ESL citations. The new collapsed proof covers the population risk identity and pointwise Bayes optimality. The new example integrates conditional errors over a discrete feature distribution.

## Checked

- Shalev-Shwartz and Ben-David (2014), *Understanding Machine Learning*, author-hosted full text at https://www.cs.huji.ac.il/~shais/UnderstandingMachineLearning/understanding-machine-learning-theory-algorithms.pdf. Read §§2.1–2.2 pp. 33–37 (population and empirical classification error), §3.2.1 pp. 45–47 (Bayes optimal predictor and irreducible error), and §12.3 pp. 167–168 (nonconvex zero–one loss and convex surrogate). The PDF is explicitly linked by its authors for personal use.
- Young and Smith (2005), *Essentials of Statistical Inference*, Cambridge University Press official excerpt https://assets.cambridge.org/97805218/39716/excerpt/9780521839716_excerpt.pdf. Read Introduction pp. 2–3 on the history of formal decision problems and Ch. 2 pp. 4–7 on action spaces, loss and risk. The excerpt supports the general decision framework; it is not used for a claim about a specific classifier's empirical performance.
- Dodge index searched for relevant entries; “Risk” is a different epidemiological entry, and no zero–one classification or statistical-learning risk entry is available. No Dodge claim used.
- New posterior/risk calculations and all original three-class cost numbers are recalculated by `checks/zero-one-loss-and-risk.py`.

## Assumed or qualified

- The illustrative binary target probabilities and deployment shift are constructed counterexamples, not observed clinical studies.
- A fresh test error fraction estimates risk only when the sample represents the target joint distribution and the fitted rule was fixed before the test labels were used.
- A plug-in classifier based on estimated posteriors is generally not the ideal Bayes rule, although the decision formula is the same.

## Disputed or unavailable

- Wald's 1950 book and the 2009 ESL chapter were not available in full at authorised publisher pages. Their existing citations remain, but new claims cite the two sources actually read above.
