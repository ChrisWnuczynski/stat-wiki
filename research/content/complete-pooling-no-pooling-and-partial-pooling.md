## Motivating example

A school has many tutorial classes but only a few marks from some of them. Estimating each class mean alone makes the small classes look unusually high or low by chance; forcing every class to share one mean hides real differences. A hierarchical model gives each class a mean and lets their estimates learn from the common population of classes. The amount of borrowing depends on how noisy each class mean is and how different classes are believed to be. {{cite:gelman_bda2013}} (Ch. 5, §5.4, pp. 113–116)

## Definition — Three models for related groups

Complete pooling imposes one common parameter for all groups. No pooling fits separate group parameters with no shared distribution connecting them. Partial pooling retains separate parameters but links them through a population distribution, often governed by a common centre and between-group variance. These are model assumptions, not three ways of averaging the same fitted numbers after analysis. They answer different questions about which observations carry information for a particular group. {{cite:gelman_bda2013}} (Ch. 5, §5.4, pp. 114–116)

For normally distributed observations, let $\overline Y_j\mid\theta_j\sim N(\theta_j,\sigma^2/n_j)$ and $\theta_j\mid\mu,\tau^2\sim N(\mu,\tau^2)$. Here $\sigma^2$ describes variation within a group, whereas $\tau^2$ describes genuine variation in group means. Conditional on fixed $\mu,\tau^2,\sigma^2$, the posterior mean is $w_j\overline y_j+(1-w_j)\mu$ with $w_j=n_j\tau^2/(\sigma^2+n_j\tau^2)$. The weight tends toward one as the group gains precise observations and toward zero when its own mean is very noisy. In a full Bayesian analysis, $\mu$ and $\tau$ are also learned from all groups, so this conditional formula is a building block rather than the whole posterior calculation. {{cite:gelman_bda2013}} (Ch. 5, §5.4, pp. 115–117, eq. 5.17)

## Properties — Where the shrinkage comes from

The conditional posterior variance is $\sigma^2\tau^2/(\sigma^2+n_j\tau^2)$, smaller than either the prior variance $\tau^2$ or the sampling variance $\sigma^2/n_j$ when both are finite and positive. Increasing $n_j$ or decreasing $\sigma^2$ makes a group more data-driven. Increasing $\tau^2$ expresses more heterogeneity and reduces sharing. As $\tau^2$ tends to zero, all group parameters collapse toward $\mu$; as it grows without bound, the conditional means approach the separate sample means. These limits explain the three labels, though an improper infinite-variance prior needs care in a full probability model. {{cite:gelman_bda2013}} (Ch. 5, §5.4, pp. 115–117)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The likelihood for $\theta_j$ contributes $\exp\{-n_j(\overline y_j-\theta_j)^2/(2\sigma^2)\}$ and its normal population prior contributes $\exp\{-(\theta_j-\mu)^2/(2\tau^2)\}$. Multiplying and completing the square gives posterior precision $A_j=n_j/\sigma^2+1/\tau^2$ and precision-weighted mean $(n_j\overline y_j/\sigma^2+\mu/\tau^2)/A_j$. Multiply numerator and denominator by $\sigma^2\tau^2$ to obtain $w_j\overline y_j+(1-w_j)\mu$, with $w_j=n_j\tau^2/(\sigma^2+n_j\tau^2)$. The variance is $1/A_j=\sigma^2\tau^2/(\sigma^2+n_j\tau^2)$. The stated limits follow directly from the ratio.{{cite:gelman_bda2013}} (Ch. 5, §5.4, p. 116, eq. 5.17){{cite:lindley_smith1972}} (pp. 2–3, eq. 1)
:::
:::

## Statistical use

Partial pooling is useful when the groups are plausibly related but differ, such as classrooms in one course or small clinical studies of a similar treatment. The population distribution transfers information indirectly: groups help estimate $\mu$ and $\tau$, which in turn inform each group parameter. A group with many observations mostly follows its own data; a sparse group borrows more. The scientific task is to specify why these groups belong together and which predictors explain systematic differences, then check that the model predicts the observed spread. {{cite:gelman_bda2013}} (Ch. 5, §§5.2, 5.4, pp. 104–107, 113–117)

If one class follows a different curriculum, exchangeability with the others may be implausible; shrinking its mean toward the common centre can hide a real difference. A group with a mixture of two distinct student populations is also poorly summarized by one normal mean. If within-class variance is far larger than the fixed value used in the example, the reported weights overtrust the data. Adding curriculum, teacher or other relevant predictors, allowing subgroup structures, and estimating variance parameters can address some of these failures, but the need for those choices is a modelling judgment. {{cite:gelman_bda2013}} (Ch. 5, §§5.1–5.2, pp. 102–107)
## Worked example

Suppose two classes have sample means $80$ and $68$ from $4$ and $25$ students, respectively. If individual marks have known within-class variance $\sigma^2=100$, a complete-pooling estimate based on all $29$ marks is $(4\cdot80+25\cdot68)/29=2020/29\approx69.66$. No pooling gives the two observed means, $80$ and $68$. Neither extreme takes both sampling noise and class heterogeneity into account. {{cite:gelman_bda2013}} (Ch. 5, §5.4, pp. 114–115, pooled and unpooled estimates)

For a partial-pooling illustration, fix the population centre at $\mu=70$ and the between-class variance at $\tau^2=25$. The small class has weight $4(25)/(100+4(25))=0.5$ and conditional posterior mean $0.5(80)+0.5(70)=75$. The large class has weight $25(25)/(100+25(25))=625/725\approx0.86207$ and mean $0.86207(68)+0.13793(70)\approx68.28$. The high mean from only four students moves more than the well-measured class mean. These conditional estimates assume the population parameters are known; estimating them would use all available classes and add uncertainty. {{cite:gelman_bda2013}} (Ch. 5, §5.4, pp. 115–117, eq. 5.17)

**Your turn.** Under $\mu=70$, $\tau^2=25$, and $\sigma^2=100$, a third class has $n=9$ students with sample mean $78$. Find its shrinkage weight, conditional posterior mean, and variance.

::: {.callout-tip collapse="true" title="Answer"}
The weight is $9(25)/(100+9(25))=225/325=9/13\approx0.69231$. The posterior mean is $70+(9/13)(78-70)=70+72/13\approx75.54$. The variance is $100(25)/(100+225)=2500/325=100/13\approx7.69$. This class gets more weight on its own mean than the four-student class but less than the 25-student class.
:::

## Common misconceptions

Partial pooling does not set all group means equal: it retains a separate $\theta_j$ for each class. Shrinkage is not a fixed percentage applied to every group; the weight changes with sample size and variance. Nor is a small-group estimate being discarded: its data still contribute to its posterior and to the population-level fit. Finally, a narrow conditional posterior interval calculated at fixed $\mu$ and $\tau$ understates the uncertainty in a full model when those quantities are unknown. {{cite:gelman_bda2013}} (Ch. 5, §§5.3–5.4, pp. 108–117)

## Connections

The [hierarchical Bayesian model](hierarchical-bayesian-model.qmd) supplies the shared population distribution. [Normal hierarchical shrinkage](normal-hierarchical-shrinkage.qmd) derives the conditional formula; [exchangeability](exchangeability.qmd) states the symmetry assumption behind assigning groups a common distribution. [Empirical Bayes](empirical-bayes.qmd) plugs estimates of population parameters into a shrinkage rule, while a full Bayesian analysis propagates their posterior uncertainty. {{cite:gelman_bda2013}} (Ch. 5, §§5.2–5.4, pp. 104–117)

## History

Lindley and Smith's 1972 analysis used exchangeable normal parameters to replace separate least-squares estimates with precision-weighted Bayesian estimates. Efron and Morris's 1975 applications of multivariate shrinkage, including baseball averages and disease prevalence, showed the practical appeal of borrowing strength across related estimates. The modern hierarchical presentation makes the assumed population distribution and its uncertainty explicit. {{cite:lindley_smith1972}} (pp. 1–3, introduction and eq. 1){{cite:efron_morris1975}} (pp. 311–312, §1){{cite:gelman_bda2013}} (Ch. 5, §5.4, pp. 113–117)
