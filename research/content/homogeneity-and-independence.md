## Motivating example
A researcher can recruit a fixed number of people from each faculty and compare their computer preferences. Alternatively, a single sample can record both faculty and preference for every participant. The resulting contingency table may look identical, yet the first design fixes faculty totals while the second estimates the faculty distribution as well. The sample design determines whether the null concerns equal response distributions across groups or independence within one joint population.{{cite:dodge2008}} (pp. 244–246, Homogeneity Test)

## Interpretation — Two null models share a fitted table
For a homogeneity experiment with row sample sizes $n_i$, the rows are separate multinomial samples. Under the null they share one vector of column probabilities $b_j$. Maximising the joint likelihood gives $\widehat b_j=C_j/n$, and hence fitted cell counts $E_{ij}=n_iC_j/n$. In an independence experiment, one multinomial sample has joint cell probabilities $p_{ij}=a_i b_j$. Its likelihood estimates are $\widehat a_i=R_i/n$ and $\widehat b_j=C_j/n$, again giving $E_{ij}=R_iC_j/n$. The arithmetic agrees because the fitted probabilities share the same row-times-column form.{{cite:openintro2019}} (§6.4, Testing for independence in two-way tables)

The parameter counts also agree after accounting for the design. An unrestricted independence table has $rc-1$ probability parameters and the null has $(r-1)+(c-1)$, leaving $(r-1)(c-1)$ restrictions. A homogeneity design has $r(c-1)$ response parameters and the null has $c-1$, giving the same difference. This count motivates the degrees of freedom, while the chi-squared limit additionally requires a sampling approximation and interior probabilities. Parameter counting alone does not prove the reference distribution.{{cite:dodge2008}} (pp. 245–246, test statistic and degrees of freedom)

## Properties — Derive the fitted counts from the likelihood
For homogeneity, the null log-likelihood is $\sum_j C_j\log b_j$ plus a data-only constant. With $\sum_jb_j=1$, a Lagrange multiplier gives $C_j/b_j=n$, hence $\widehat b_j=C_j/n$ when every pooled column total is positive. Under independence, $\sum_{ij}O_{ij}\log(a_i b_j)=\sum_iR_i\log a_i+\sum_jC_j\log b_j$. The row and column optimisations separate and give the stated margins. This calculation shows which margins are estimated and which were fixed by recruitment, even when their numerical values are the same.{{cite:openintro2019}} (§6.4, expected counts from marginal totals)

Pearson's statistic is $X^2=\sum_{ij}(O_{ij}-E_{ij})^2/E_{ij}$. Each denominator must be positive. With a fixed number of cells, independent observations and growing expected counts, its limiting distribution under either null is chi-squared with $(r-1)(c-1)$ degrees of freedom. Small expected counts make this approximation unreliable, and dependent observations can invalidate the model regardless of the cell counts.{{cite:dodge2008}} (pp. 245–246)

## Worked example — Same observed table, different sampling stories
Consider counts $\left(\begin{smallmatrix}12&8&10\\8&12&10\end{smallmatrix}\right)$. Both row totals are thirty and each column total is twenty, so every fitted count is ten. The Pearson statistic is $4/10+4/10+0+4/10+4/10+0=1.6$. There are $(2-1)(3-1)=2$ degrees of freedom. The chi-squared approximation gives upper-tail probability $e^{-1.6/2}\approx0.449329$.

If thirty people were sampled separately from each of two populations, the null is homogeneity of their three-category response distributions. If sixty people were sampled jointly and then classified by two variables, the null is independence of those variables. The common test value does not turn the first design into a sample of the relative population sizes.

**Your turn.** Double every cell count while preserving the proportions. What is the new statistic and approximate p-value?

::: {.callout-tip collapse="true" title="Answer"}
Observed and fitted counts both double. Each Pearson contribution doubles, so $X^2=3.2$. The degrees of freedom stay two and the upper-tail probability is $e^{-1.6}\approx0.201897$.
:::

## Assumptions and limits — Conditioning changes which randomness is compared
For a two-by-two table, conditioning on both margins yields a hypergeometric law under either null. The pooled success probability cancels from the relative probabilities of tables with those margins. This is the basis for a conditional exact test, but it changes the reference set from all possible multinomial tables to tables sharing the observed margins. The chosen definition of two-sided extremeness must also be stated. An exact calculation removes the large-count approximation; it does not correct a dependent sampling scheme or a selected sample.{{cite:agresti1992_exact_survey}} (§§1.3–2.1, pp. 133–135)

## Common misconceptions — A non-rejection does not establish equality
Failure to reject may reflect limited precision or small effects. It does not prove that every row distribution is identical or that the two population variables are independent. Conversely, rejection establishes an incompatibility with the specified null model under its assumptions, rather than a causal relation. For descriptive follow-up, examine the cell contributions and estimated proportions, while accounting for multiplicity if those comparisons are used as additional tests.{{cite:dodge2008}} (pp. 244–246, scope of homogeneity testing)
