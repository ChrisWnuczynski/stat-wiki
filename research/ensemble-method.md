# Ensemble method — research record

Full sources opened: Breiman, “Bagging Predictors” (1996), author-hosted full paper at stat.berkeley.edu/~breiman/bagging.pdf, §§1, 4, 6; Breiman, “Random Forests” (2001), author-hosted full paper at stat.berkeley.edu/~breiman/randomforest2001.pdf, §§1, 5–6; Freund and Schapire (1997), full *Journal of Computer and System Sciences* paper hosted at McGill University, §§4.1–4.2. Local chapter: `sources/stat3006/chapters/sl-13-ensembles.qmd`, §§“Why averaging helps”, “Bagging and random forests”, “Boosting”. Dodge index has no relevant entry used for history.

- **Checked:** Breiman (1996), §1 pp. 123–124 defines bootstrap aggregation: resample the learning set, average numerical predictions or vote on classes. §4 pp. 131–132 proves that population aggregation lowers expected squared error against a random single fit and cautions that bootstrap aggregation may fail for stable procedures.
- **Checked:** Breiman (2001), §1 and §5 describe random-forest trees with randomized feature choices at nodes, and discuss strength/correlation tradeoffs.
- **Checked:** Freund and Schapire (1997), §4 pp. 125–128 derive AdaBoost using sequentially reweighted examples and a weighted final vote. Boosting is not merely bootstrap voting.
- **Checked algebraically and by Python:** variance of the mean of $T$ equally variable predictions with pairwise error correlation $\rho$ is $\sigma^2[\rho+(1-\rho)/T]$. At $T=5$, $\sigma^2=1$, $\rho=.3$, this is $.44$; independence gives $.20$; at $T=4$, $\rho=.5$ it is $.625$. Predicted values 2, 4, 6 average to 4.
- **Assumed:** the illustrative error variance/correlation model has a common variance and a common pairwise correlation; real ensemble members need not satisfy it.
- **Disputed/limited:** The variance formula is for a numerical average, not for classification zero-one loss. Correlated bias is not removed by averaging, and performance on training data is not external validation. Breiman (1996), §4 explicitly notes bagging may hurt stable predictors.

Page type: Topic (concept). Preserve baseline definition, classification/regression distinction, $T$-model average formula, source citations and link to the chapter theorem.
