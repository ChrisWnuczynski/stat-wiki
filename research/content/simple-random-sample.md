## Motivating example
A business register contains every eligible firm and an analyst can afford to contact only a fixed number. Simple random sampling without replacement gives a precise meaning to selecting that fixed-size group fairly: every subset of the required size has the same probability. This is stronger than merely arranging equal marginal chances for each firm, and it makes the sampling distribution of estimators computable from the randomisation design.{{cite:dodge2008}} (Simple Random Sampling, pp. 497–498)

## Definition — Uniform over subsets of a fixed size
For a finite population of $N$ labelled units, a simple random sample without replacement of size $n$ selects each of the $\binom Nn$ subsets with probability $1/\binom Nn$. No unit appears twice in a selected subset. Sequential uniform draws from the units not yet selected give the same design, because each ordered sample has the same probability and every unordered subset has $n!$ orderings.{{cite:statistics_canada2003_survey}} (§6.2.2, simple random sampling)

Sampling with replacement is a related but different design: a unit can appear more than once, and independent uniform draws form an ordered sequence. Without replacement, inclusion indicators are dependent. When the sampling fraction is small the two designs can give similar precision, but they do not become the same finite randomisation mechanism.{{cite:dodge2008}} (Simple Random Sampling, p. 497, domains and limitations)

## Properties — Equal inclusion and a finite-population correction
A given unit belongs to $\binom{N-1}{n-1}$ subsets, so its inclusion probability is $n/N$. For two distinct units, the joint inclusion probability is $n(n-1)/[N(N-1)]$. With fixed population values $y_i$, the sample mean is unbiased for the population mean. If
$$S^2=\frac1{N-1}\sum_{i=1}^N(y_i-\bar Y)^2,$$
then its design variance is
$$\operatorname{Var}(\bar y)=\left(1-\frac nN\right)\frac{S^2}{n}.$$
The factor $1-n/N$ reflects the reduced uncertainty from observing a substantial fraction of the finite population. It reaches zero for a census. The divisor in the definition of $S^2$ matters when comparing equivalent variance formulas.{{cite:statistics_canada2003_survey}} (§7.3.2.3, estimating precision for simple random sampling)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write $I_i$ for the indicator that unit $i$ is sampled and $f=n/N$. The combinatorial probabilities give $\E(I_i)=f$, $\operatorname{Var}(I_i)=f(1-f)$ and, for distinct units, $\operatorname{Cov}(I_i,I_j)=-f(1-f)/(N-1)$. Since $\bar y=n^{-1}\sum_iI_i y_i$, linearity gives $\E(\bar y)=\bar Y$. Substituting the indicator variances and covariances into the variance of this sum, and using $\sum_i(y_i-\bar Y)=0$, gives $(1-f)S^2/n$. This is a design calculation: the population values themselves remain fixed.
:::
:::

## Worked example — Enumerate every possible sample
Take population values $(1,3,5,7)$ and sample size two. The six equally likely samples have means $2,3,4,4,5,6$. Their average is $4$, agreeing with the population mean. Their sampling variance is $(4+1+0+0+1+4)/6=5/3$. Thus the SRS sampling variance is $5/3$. The population variance with divisor $N-1$ is $20/3$, so the formula gives $(1-2/4)(20/3)/2=5/3$ as well.

Each unit belongs to three of the six samples, giving inclusion probability $1/2$. Each pair is itself exactly one of the six possible samples, giving joint inclusion probability $1/6$. These two probabilities are different, showing why treating inclusion indicators as independent would give an incorrect variance.

**Your turn.** Choose either the pair of units labelled {1,2} or the pair {3,4}, each with probability one half. Is this an SRS of two from four?

::: {.callout-tip collapse="true" title="Answer"}
No. Each unit has inclusion probability one half, but four of the six possible pairs can never be selected. Equal individual inclusion probabilities are not sufficient for simple random sampling.
:::

## Statistical use — Random selection requires an adequate frame
The frame must identify the units eligible for selection and allow the required randomisation. Duplicate entries can increase some units' inclusion chances, while omissions assign others chance zero. Uniform selection from a faulty list gives an SRS of that list, rather than automatically giving an SRS of the intended population. Nonresponse is another stage that can alter the relationship between selected and observed units.{{cite:statistics_canada2003_survey}} (§§3.3 and 6.2.2, sampling frames and SRS)

SRS is a useful reference design, but it is not always the most efficient way to spend a fixed budget. Known strata can improve representation and precision, while clusters can reduce travel costs. Such designs should be analysed according to their actual inclusion and dependence structure, rather than pretending the observed units came from an SRS because their marginal probabilities are equal.{{cite:statistics_canada2003_survey}} (§§6.2.5–6.2.6, cluster and stratified designs)

## Assumptions and limits — Design unbiasedness does not remove all uncertainty
An unbiased sample mean can differ from the population mean for a particular realised sample. Its design variance quantifies variation over the specified random samples. Measurement errors, incomplete coverage and a mismatch between the estimand and the recorded values are separate issues. A complete account of the sample therefore specifies the population, frame, selection mechanism, response process and target summary.{{cite:statistics_canada2003_survey}} (§§3.3–3.4, frames and sources of survey error)

## Common misconceptions — Equal inclusion is weaker than a uniform draw over subsets
From five labelled units the number of samples of size three is $\binom{5}{3}=10$. Each is equally likely under simple random sampling, and each unit sits in $\binom{4}{2}=6$ of them, so the inclusion probability is $6/10=3/5$, which is $n/N$. A design that gives every unit inclusion probability $3/5$ can still forbid some triples. The four-unit illustration already separates the two ideas: selecting $\{1,2\}$ or $\{3,4\}$ with equal probability gives every unit inclusion probability $1/2$, and four of the six possible pairs have probability zero. Those four pairs would each have probability $1/6$ under an SRS of size two. The variance formula uses the joint inclusions, so substituting the SRS formula for a design that only matches the marginal inclusions misstates the variance.{{cite:dodge2008}} (Simple Random Sampling, pp. 497–498)

When $n=N$ the finite-population factor $1-n/N$ is zero, and the sample mean has design variance zero. The sample is the population. For the four values $(1,3,5,7)$ and $n=2$, the factor is $1/2$ and the design variance of the mean is $5/3$. The six sample means $2,3,4,4,5,6$ average to $4$, and their mean squared deviation from $4$ is $(4+1+0+0+1+4)/6=5/3$. A census of the same four values would report $4$ with no design variance left to estimate.{{cite:statistics_canada2003_survey}} (§7.3.2.3, estimating precision for simple random sampling)

## Interpretation — Without replacement creates a small negative dependence
The covariance between two distinct inclusion indicators is $-f(1-f)/(N-1)$. It is negative because the sample size is fixed: selecting one unit slightly reduces the chance of selecting another. For $N=4$ and $n=2$, $f=1/2$ and the covariance is $-(1/2)(1/2)/3=-1/12$. The variance of an indicator is $f(1-f)=1/4$. Independence would have required covariance zero and would have given a different variance for the sample mean. The negative term is what the finite-population correction is accounting for in the aggregated formula $(1-f)S^2/n$.{{cite:statistics_canada2003_survey}} (§7.3.2.3, estimating precision for simple random sampling)

## Connections
[Stratified and cluster sampling](stratified-and-cluster-sampling.qmd) keep simple random sampling as the within-stratum draw or replace it by a draw of groups. The population-mean estimator then weights stratum means by population shares, or it follows the cluster inclusion probabilities. Calling either design a simple random sample because the final file has one row per unit drops the dependence those designs put into the variance.{{cite:statistics_canada2003_survey}} (§§6.2.5–6.2.6, cluster and stratified designs)
