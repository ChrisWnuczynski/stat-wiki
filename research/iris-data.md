# Iris data — research record

Dataset page, rank 86. Baseline 1,769 words and zero figures; preserve extensive R code, covariance matrices, means, Hotelling result, PCA/clustering/mixture examples, infobox, related links and supported citations.

## Sources opened

- R Core Team, `datasets::iris` official documentation, https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/iris.html , read Description, Format, Source, References and Examples. It gives 150 rows, four measurements in cm, 50 from each of three species, Anderson data collection in 1935 and Fisher (1936) as source. New bibliography entry in pending JSON.
- Fisher (1936), “The Use of Multiple Measurements in Taxonomic Problems,” full paper read through Wiley's authorized historical archive at https://onlinelibrary.wiley.com/doi/pdf/10.1111/j.1469-1809.1936.tb02137.x . Sections I–II on printed p. 179 state the taxonomic discrimination aim and identify Anderson's flower measurements. The publisher DOI page at https://onlinelibrary.wiley.com/doi/10.1111/j.1469-1809.1936.tb02137.x confirms the bibliographic record.
- scikit-learn developers, `adjusted_rand_score` official documentation, https://scikit-learn.org/stable/modules/generated/sklearn.metrics.adjusted_rand_score.html , read the definition, return-value description and examples. It verifies chance correction, invariance to permuting cluster labels, perfect agreement at 1, and possible negative values. The original Hubert–Arabie article was accessible only as a Springer abstract and was not used as substantive evidence. Proposed bibliography key: `sklearn_ari2026`.
- scikit-learn developers, `brier_score_loss` official documentation, https://scikit-learn.org/stable/modules/generated/sklearn.metrics.brier_score_loss.html , read the definition and Notes. It verifies that the score uses squared differences between predicted probabilities and observed labels. The original Brier paper was inaccessible from the publisher and was not used as substantive evidence. Proposed bibliography key: `sklearn_brier2026`.
- Dodge index searched for Iris/Anderson; none. No Dodge citation used.
- Installed scikit-learn `load_iris()` rows used to verify actual values and new threshold example. No claim about scikit-learn provenance is made.
- Question-bank `ex-sl-03-7`, `ex-sl-08-7`, `ex-ur-held-out-label` read, each with a worked answer and a distinct use of the data.

## Fact audit

- **Checked**: 150 flowers, three species of 50; four centimetre measurements and one species factor: official R docs Description/Format and code.
- **Checked**: sample petal-length ranges and mean differences with `sklearn.datasets.load_iris` in `checks/iris-data.py`.
- **Checked**: existing species means, pooled covariance and setosa covariance against installed data; check script also verifies preserved printed summaries.
- **Checked**: Anderson collection and Fisher 1936 analysis as stated by official R documentation Source/References. The full free-access 1936 paper was read in Wiley's authorized historical archive: §§I–II, printed p. 179, states the taxonomic discrimination aim and Table I identifies four flower measurements from 50 setosa and 50 versicolor plants measured by E. Anderson.
- **Checked**: inherited adjusted Rand index and Brier score explanations against the full official scikit-learn metric documentation listed above; the numerical results remain preserved and are checked by `checks/iris-data.py` where possible.
- **Assumed**: the installed standard iris dataset and R's `datasets::iris` have the same measurement table; this is supported by their matching printed group means and covariance matrices.
- **Disputed/limited**: perfect separation of setosa by a petal threshold is an empirical property of these 150 rows, not a future error guarantee. The sample is historically selected, not shown to be a random sample of all irises. R-based mixture and clustering output in inherited text was not re-run because R is absent; preserved as baseline.
