# Pooled covariance — rank 161

Type: concept/section. Baseline 426 words, zero figures. Preserve the source two-sample covariance formula, Wishart and Hotelling statements, theorem link, all citations until opened replacements are integrated, the infobox, and three practice backlinks.

## Sources opened

- Fisher (1936), full publisher Wiley PDF, pp. 179–181, §§I–II. Read its within-species sums of squares/products and 98 degrees of freedom for two groups of 50, plus the discriminant goal. This directly supports the historical connection to within-group pooling, not the later general matrix formula's exact presentation.
- NIST Dataplot, *Pooled Variance-Covariance Matrix*, complete official reference page (Description; Program 2, lines for `SPOOL` and `DENOM`). It defines the divisor `sum(n_g−1)=n−G` and supplies a Fisher iris application.
- Clemmensen, Hastie, Witten and Ersbøll (2011), full author-hosted *Sparse Discriminant Analysis* PDF, §2.1, pp. 3–4; it uses pooled within-class covariance in LDA and states the high-dimensional singularity issue. Its Gaussian MLE uses divisor `n`; the article distinguishes that from the unbiased `n−G` divisor.
- Jonathan Taylor, Stanford STATS305C *Hotelling T2* lecture, complete university-hosted course page, “Hotelling’s T² test” and “Distribution of test statistic”. It states the pooled Wishart law, the exact two-sample rescaling and its F degrees of freedom. The course index identifies Taylor as instructor and dates its current schedule with a 9 June 2025 final exam, which establishes the 2025 course version; the lecture page itself has no separate date.
- Strimmer (2025), full author-hosted *Multivariate Statistics and Machine Learning*, Ch. 2 §2.4, read for the Gaussian sample-covariance Wishart law. Combined with an orthogonal-residual argument in the source chapter, this supports the pooled residual law.
- Source `sl-02-normal-inference.qmd` two-sample section and `sl-08-discriminant-analysis.qmd` worked example inspected for preservation.

## Fact ledger

- **Checked:** Within-group scatter divided by `n−G` is the weighted average of sample covariance matrices using weights `n_g−1` (NIST Description/Program 2). Algebra, unbiasedness under independent groups with shared covariance, and rank bound proved in one collapsed box.
- **Checked:** Grand-mean covariance includes between-group scatter and can differ sharply from pooled within-group covariance. Exact decomposition and 2D numeric example checked with SymPy.
- **Checked:** Fisher formed within-species cross-products, with 98 degrees of freedom for 50 setosa and 50 versicolor flowers, in his discrimination analysis (1936 pp. 179–181).
- **Checked:** LDA uses a shared covariance and becomes singular in high dimension without regularization (Clemmensen et al. §2.1, pp. 3–4).
- **Checked:** Under independent multivariate-normal groups with common covariance, pooled scatter is Wishart with `n_1+n_2−2` degrees of freedom; an orthogonal projection of each group gives the pooled residual representation (Strimmer Ch. 2 §2.4; Taylor STATS305C, “Hotelling’s T² test”).
- **Checked:** With `m=n_1+n_2−2`, the two-sample statistic obeys `[(m−p+1)/(mp)]T²~F_(p,m−p+1)` under the null, provided the pooled inverse exists (Taylor STATS305C, “Hotelling’s T² test” and “Distribution of test statistic”).
- **Assumed:** Covariance equality across groups for pooled estimator of a common population covariance. Without equality, the arithmetic is still defined but the single-Σ interpretation fails.
- **Disputed:** The original Wishart/Hotelling papers and Anderson book were not opened in this batch; the new university and author sources support the two-sample claims. Full derivations of Wishart independence and the normal/Wishart-to-F quadratic-form law remain proof debt in pending. The NIST Dataplot two-sample Hotelling page was also opened but omits the required F scale factor in its prose, so it is not cited for the exact law.

## Arithmetic

The focused check asserts all displayed matrices, means, degrees of freedom, singularity bounds and inherited question links. It confirms no figure loss.
