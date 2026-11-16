# Pooled covariance — rank 161

Type: concept/section. Baseline 426 words, zero figures. Preserve the source two-sample covariance formula, Wishart and Hotelling statements, theorem link, all citations until opened replacements are integrated, the infobox, and three practice backlinks.

## Sources opened

- Fisher (1936), full publisher Wiley PDF, pp. 179–181, §§I–II. Read its within-species sums of squares/products and 98 degrees of freedom for two groups of 50, plus the discriminant goal. This directly supports the historical connection to within-group pooling, not the later general matrix formula's exact presentation.
- NIST Dataplot, *Pooled Variance-Covariance Matrix*, complete official reference page (Description; Program 2, lines for `SPOOL` and `DENOM`). It defines the divisor `sum(n_g−1)=n−G` and supplies a Fisher iris application.
- Clemmensen, Hastie, Witten and Ersbøll (2011), full author-hosted *Sparse Discriminant Analysis* PDF, §2.1, pp. 3–4; it uses pooled within-class covariance in LDA and states the high-dimensional singularity issue. Its Gaussian MLE uses divisor `n`; the article distinguishes that from the unbiased `n−G` divisor.
- Source `sl-02-normal-inference.qmd` two-sample section and `sl-08-discriminant-analysis.qmd` worked example inspected for preservation.

## Fact ledger

- **Checked:** Within-group scatter divided by `n−G` is the weighted average of sample covariance matrices using weights `n_g−1` (NIST Description/Program 2). Algebra, unbiasedness under independent groups with shared covariance, and rank bound proved in one collapsed box.
- **Checked:** Grand-mean covariance includes between-group scatter and can differ sharply from pooled within-group covariance. Exact decomposition and 2D numeric example checked with SymPy.
- **Checked:** Fisher formed within-species cross-products, with 98 degrees of freedom for 50 setosa and 50 versicolor flowers, in his discrimination analysis (1936 pp. 179–181).
- **Checked:** LDA uses a shared covariance and becomes singular in high dimension without regularization (Clemmensen et al. §2.1, pp. 3–4).
- **Assumed:** Covariance equality across groups for pooled estimator of a common population covariance. Without equality, the arithmetic is still defined but the single-Σ interpretation fails.
- **Disputed:** The preserved article states a pooled Wishart distribution independent of both means and a Hotelling F result. These require independent multivariate-normal group samples and dimension/sample-size restrictions; original Wishart/Hotelling papers and Anderson book were not opened in this batch. Their proofs are recorded as debt in pending, and the page supplies a clear scope distinction.

## Arithmetic

The focused check asserts all displayed matrices, means, degrees of freedom, singularity bounds and inherited question links. It confirms no figure loss.
