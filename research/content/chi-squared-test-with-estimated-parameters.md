## Motivating example
A Poisson model for houses per plot specifies a family of probability vectors rather than one fixed vector. Estimating its mean uses some of the same discrepancies that the goodness-of-fit statistic will measure. Calibration must account for this fitting step. The relevant estimate is obtained from the category counts used in the test.{{cite:nist_chi_square_gof2002}} (§1.3.5.15, binned-count likelihood)

## Definition
The adjustment $k-1-r$ requires an interior identifiable parameter, smooth positive cell probabilities, a full-rank $r$-dimensional derivative, and a suitable efficient fit from those multinomial counts. A redundant parameter does not remove another degree of freedom, while a parameter on a boundary can lead to a different limit. A saturated model has no residual goodness-of-fit directions.{{cite:nist_chi_square_gof2002}} (§1.3.5.15, “Critical Region”)

## Properties — What fitting removes
The standardized multinomial error has limiting covariance $I-uu^\top$, where $u_i=\sqrt{p_i(\theta_0)}$. Let the columns of $A$ be the standardized derivatives $\partial p_i/\partial\theta_j\,/\sqrt{p_i}$. Differentiating $\sum_i p_i=1$ gives $u^\top A=0$. The likelihood score equations remove the projection of the random error onto the column space of $A$. The residual is therefore a normal projection perpendicular to both $u$ and those $r$ tangent directions, leaving rank $k-1-r$. Its squared length has the stated chi-squared limit. This is an asymptotic projection argument, rather than a claim that fitting always makes the statistic smaller in every finite sample. The fixed-probability Pearson comparison supplies the starting $k-1$ directions.{{cite:openintro2019}} (§6.3.2–6.3.4, chi-square statistic and reference distribution)

## Worked example — Fitting a binomial family
Consider one hundred objects, each with two binary opportunities. The counts for zero, one and two successes are $(30,40,30)$. Under a $\operatorname{Bin}(2,p)$ family the grouped likelihood gives $\widehat p=(40+2\cdot30)/200=0.5$. Expectations are $(25,50,25)$ and
$$T=25/25+100/50+25/25=4.$$
There are three categories and one fitted parameter, leaving one degree of freedom. The approximate $p$-value is $0.0455$. Using two degrees of freedom would give $0.1353$ and a different decision. The distinction comes from fitting, not from changing the observed counts.{{cite:nist_chi_square_gof2002}} (§1.3.5.15, estimated parameters and degrees of freedom)

**Your turn.** Change those counts to $(25,50,25)$. Find the fitted probability, statistic and residual degrees of freedom.

::: {.callout-tip collapse="true" title="Answer"}
There are one hundred successes in two hundred opportunities, so $\widehat p=0.5$. Observations equal fitted expectations and $T=0$. The reference still has one degree of freedom.
:::

## Interpretation — Grouping changes the fitted likelihood
For the village table, $911/1200$ is the mean of the complete count values. Once all counts of four or more are merged, the multinomial likelihood is instead
$$\ell(\lambda)=\sum_{j=0}^3O_j\log\{e^{-\lambda}\lambda^j/j!\}+15\log P_\lambda(X\ge4).$$
Maximizing this expression gives $\widehat\lambda=0.7512$, fitted counts approximately $(566.13,425.31,159.75,40.00,8.80)$, and $T=7.7362$ on three degrees of freedom, with $p=0.05179$. The displayed figure uses the complete-data mean; the grouped fit is numerically close but its likelihood matches the theorem's premise. The count table is illustrative, with spatial independence and a common rate requiring a separate modelling justification.{{cite:nist_chi_square_gof2002}} (§1.3.5.15, maximum likelihood from observed bin counts)

## Assumptions and limits
A single Poisson goodness-of-fit test cannot establish a spatial mechanism. A mixture of different plot rates, dependence between nearby plots, and non-Poisson counts can each alter the frequencies. The test only assesses the specified distribution of plot counts under independent sampling. Category selection also affects the discrepancy being tested.{{cite:openintro2019}} (§6.3.5, evaluating goodness of fit)
