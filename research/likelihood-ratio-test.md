# Likelihood-ratio test — research record

Method page, rank 88. Baseline 1,499 words and zero figures. Existing multivariate-normal determinant derivation, GLM deviance discussion, links and citations preserved.

## Sources opened

- Kyle Siegrist, *Probability, Mathematical Statistics, and Stochastic Processes*, §9.5 “Likelihood Ratio Tests,” https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/09:_Hypothesis_Testing/9.05:_Likelihood_Ratio_Tests . Read Basic Theory, simple hypotheses and Bernoulli example. Pending bibliography key `siegrist2022_lrt`.
- Penn State course notes, Lesson 2, “Binomial and Multinomial Inference,” https://online.stat.psu.edu/stat504/Lesson02 . Read indexed section on deviance/likelihood-ratio statistic and its chi-square approximation under the null. Not cited on the page because its course-code URL is rejected by visible-text checks.
- Marco Taboga, “Likelihood ratio test,” *Lectures on Probability Theory and Mathematical Statistics* (2021), https://statlect.com/fundamentals-of-statistics/likelihood-ratio-test . Read the statistic, regularity assumptions, asymptotic chi-square result and test sections. The page cites this source; the Penn State course URL is not used in the page because its course code is rejected by the wiki's visible-text checks.
- R Core Team, `glm` documentation, https://stat.ethz.ch/R-manual/R-devel/library/stats/html/glm.html , read Value/deviance for the GLM connection. Existing `rstats_glm2026` key.
- Wilks (1938), publisher DOI metadata https://doi.org/10.1214/aoms/1177732360 , confirming paper title and 1938 publication. Full original paper inaccessible via Project Euclid security check, so the page does not cite it.
- Alan Agresti (2021), author-hosted full paper, *The foundations of statistical science: A history of textbook presentations*, §5, printed p. 668, https://users.stat.ufl.edu/~aa/articles/Agresti_BJPS.pdf . It independently corroborates the 1938 date; it is not a page citation because its title would fail the wiki's visible-text gate.
- Anastasiou and Reinert (2020), author-hosted full published paper, *Bounds for the asymptotic distribution of the likelihood ratio*, §1 printed p. 608 and reference 25 printed p. 643, https://www.andreasanastasiou-statistics.com/_files/ugd/24cdcc_ca5285583f6d4acdaddbf7aab0a86d28.pdf . It describes Wilks's chi-square result and cites the 1938 original. The article cites this source because its precise title also satisfies the wiki's visible-text gate.
- Dodge (2008), authorized PDF “Likelihood Ratio Test,” printed pp. 309–310 (PDF pp. 310–311). It attributes likelihood-ratio testing to Neyman and Pearson (1928), but dates Wilks asymptotics to 1962, contradicted by Wilks's 1938 original-paper record. New prose cites Dodge only for Neyman–Pearson history and notes the accurate 1938 date separately.
- Question bank `ex-inf-glrt-two-means`, `ex-inf-pearson-one-cell`, `q-47` inspected with worked answers; they respectively test normal-model ratio, Pearson/deviance comparison and lack of ordinary LRT for quasi-likelihood.

## Fact audit

- **Checked**: null/unrestricted likelihood ratio in $[0,1]$ for nested models, small values as evidence, and calibration by null distribution: Siegrist §9.5.
- **Checked**: $G^2=-2\log\Lambda$ and approximate chi-square under standard regularity: Taboga, “The likelihood ratio statistic” and “Asymptotic distribution.” The approximation is not exact for small discrete samples.
- **Checked**: binomial $n=10,k=8$ statistic $3.854895$, ratio $0.145519$, chi-square tail $0.049601$, exact two-sided LRT tail $0.109375$. `checks/likelihood-ratio-test.py` recomputes with SciPy and direct combinatorics.
- **Checked**: Neyman–Pearson history in Dodge p. 309; Wilks paper in 1938 from Anastasiou and Reinert's fully read published paper, §1 and reference 25, corroborated by Agresti §5 and the original publisher DOI record.
- **Assumed**: for chi-square calibration, nested regular parametric models, identifiable interior null, nonsingular information and suitable large sample. Degrees of freedom count independent restrictions.
- **Disputed**: Dodge's Wilks 1962 date conflicts with original paper published 1938; use 1938. Its ratio orientation also varies by passage, so this page fixes the null-over-full convention.
