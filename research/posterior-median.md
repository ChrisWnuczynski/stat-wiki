# Posterior median

Rank 191. Type: Concept. Frozen baseline: 585 body words, zero figures. The original absolute-loss derivation, Beta(3,9) odds comparison, citations and question link are retained.

## Checked

- **Checked in full source:** Dodge (2008), printed p. 346, “Median”, reports the 1748 Euler/Mayer attribution for dividing ordered data into halves. The entire extracted page `/workspace/statwiki-sources/dodge2008/pages/pdf-0346.txt` was read. This secondary history claim was not corroborated in the original 1748 works.
- **Checked in the repository source chapter:** `sources/book/chapters/bayes-01-foundations.qmd`, §§“Posterior summaries” and “Posterior summaries from draws”, particularly lines 158–225. They define the mean, MAP and quantiles and describe sample-median estimation. The inherited article's own absolute-loss derivation was compared with the source.
- **Checked mathematically:** The collapsed proof gives the median's absolute-loss optimality and monotone-transform equivariance. `checks/posterior-median.py` checks Beta$(3,9)$ quantiles and all reported numbers in the discrete and pending bank examples.
- **Assumed:** A proper scalar posterior and finite first absolute moment for the expected-loss minimization. The Beta numerical example uses the shape convention with density proportional to $\theta^{a-1}(1-\theta)^{b-1}$.
- **Disputed:** Dodge's mathematical line on p. 346 prints the median tail inequalities with $\leq1/2$; the correct weak inequalities are $\geq1/2$, as follows from the definition and proof. Dodge is cited only for its historical note, not the incorrect inequality. Its Euler/Mayer attribution is marked secondary, not independently established.

## Sources used

- Yadolah Dodge, *The Concise Encyclopedia of Statistics* (2008), p. 346, “Median”; existing `dodge2008` key for history only.
- The repository's Bayesian foundations book chapter was read for the existing posterior-summary material. Its inherited Hoff and Wang citations remain in the source-derived block; no new statement is attributed to texts not opened in this worktree.

## Changes

Added motivating use, precise median condition including atoms, interpretation of skewness, a single collapsed proof, verified Beta and discrete numerical examples, a hidden Your turn answer, distinct misconceptions, concrete failure examples, connections and sourced historical context. Two answered questions remain recorded for the shared bank. The inherited absolute-loss citation now points only to the full author-hosted Gelman et al. (2013), Ch. 4, Ex. 6(b), p. 98. No figure was present or removed.
