## Lead context
After a multinomial sample, a Dirichlet prior is updated by adding the observed category counts to its concentrations.

## Intuition
**Counts add, and the shares stay on the simplex.** A Dirichlet draw is a vector of category probabilities that sum to \(1\). A multinomial likelihood contributes a factor \(p_k^{x_k}\) for each category. The Dirichlet density already contains \(p_k^{\alpha_k-1}\). The product is another Dirichlet density, with concentrations \(\alpha_k+x_k\). The normalising constant changes, and the probabilities are still forced to sum to \(1\). The posterior mean of coordinate \(k\) pulls the sample proportion toward the prior proportion, with weights \(n\) and \(\alpha_0=\sum_j\alpha_j\).

## Statement
**The updated concentrations.** If \(x_k\) are the category counts in \(n\) trials and every prior concentration \(\alpha_k\) is positive, the posterior is Dirichlet\((\alpha_1+x_1,\ldots,\alpha_K+x_K)\). The coordinate mean is \((\alpha_k+x_k)/(\alpha_0+n)\). When every \(\alpha_k+x_k>1\), the posterior mode is \((x_k+\alpha_k-1)/(n+\alpha_0-K)\).

## Worked example — Three categories, prior concentrations \(2,2,2\)
The prior is symmetric, so each prior mean is \(2/6=1/3\). The counts are \(3,1,2\), and \(n=6\). The posterior concentrations are \(5,3,4\), with total \(12\). The posterior means are
\[
\frac{5}{12},\qquad \frac{3}{12}=\frac14,\qquad \frac{4}{12}=\frac13.
\]
Every posterior concentration exceeds \(1\), so the mode is
\[
\frac{3+2-1}{6+6-3}=\frac49,\qquad
\frac{1+2-1}{9}=\frac29,\qquad
\frac{2+2-1}{9}=\frac39.
\]
These three fractions sum to \(1\). The probability that a new trial falls in the first category is the posterior mean \(5/12\), which lies between the prior mean \(1/3\) and the sample proportion \(3/6=1/2\):
\[
\frac{6}{12}\cdot\frac13+\frac{6}{12}\cdot\frac12=\frac{5}{12}.
\]

**Your turn.** Keep the prior concentrations at \(2,2,2\), and replace the counts by \(0,0,6\). Give the posterior means, and say whether the interior-mode formula applies.

::: {.callout-tip collapse="true" title="Answer"}
The posterior concentrations are \(2,2,8\), and the means are \(2/12\), \(2/12\) and \(8/12\). Each concentration is greater than \(1\), so the mode formula applies and returns \((0+2-1)/9=1/9\), again \(1/9\), and \((6+2-1)/9=7/9\).
:::

**Check yourself.** Prior concentrations \(1,1,1\) and counts \(4,1,1\). What are the three posterior means?

::: {.callout-tip collapse="true" title="Answer"}
Posterior concentrations \(5,2,2\) total \(9\), so the means are \(5/9\), \(2/9\) and \(2/9\).
:::

Prior concentrations \(2,2,2\) and counts \(3,1,2\), as in the worked example. The second posterior concentration is \(3\). What goes wrong if someone still plugs a coordinate with concentration \(1\) into the mode formula?

::: {.callout-tip collapse="true" title="Answer"}
Nothing is wrong in this particular example, because every concentration is at least \(3\). The formula \((x_k+\alpha_k-1)/(n+\alpha_0-K)\) is the interior mode only when every posterior concentration exceeds \(1\). A concentration of \(1\) puts a coordinate on the boundary of the region where that expression was derived, and the density need not have an interior mode.
:::

## Related concepts
**Beta, pseudo-counts, and the next trial.**
The two-category Dirichlet is a [beta distribution](beta-distribution.qmd), and the same addition of counts is the beta–binomial update. The concentrations act as [pseudo-counts](pseudo-counts-and-sequential-updating.qmd) in the posterior mean. The probability of the next category is that mean, because the predictive probability is the posterior expectation of \(p_k\).
