## Motivating example
For a million independent Poisson counts, inference about a common rate uses their sum and the known sample size rather than their order. In a normal model with unknown mean and variance, two sums suffice. The dimension of these summaries does not grow with the sample size. The Pitman–Koopman–Darmois characterisation asks when a regular family can admit such a reduction for every sample size.{{cite:brown1964_sufficiency}} (§1, pp. 1456–1457)

## Statement
An informal version says that suitable regular families of independent, identically distributed observations admitting fixed-dimensional sufficient statistics for all sample sizes are exponential families. “Fixed-dimensional” must describe genuine regular data reduction: a discontinuous encoding of an entire vector into one real number does not give the smooth reduction intended by the theorem. Common support and restrictions on the density and statistic prevent such counterexamples. Different formal versions put different regularity requirements on those objects.{{cite:brown1964_sufficiency}} (§2, Assumption 2.1 and thm. 2.1, pp. 1457–1458)

The scalar theorem stated by Brown assumes densities equivalent to Lebesgue measure on a common interval and conditions on the sufficient statistic including continuity and a null-set condition. Its conclusion is a one-parameter exponential family. That is a specific formal result, whereas the broad fixed-dimensional formulation also includes multivariate summaries under corresponding regularity conditions. The number of model parameters and the number of natural sufficient statistics need not be identical in a curved exponential family.{{cite:brown1964_sufficiency}} (§§1–2, pp. 1456–1458)

## Key results — Factorisation proves the forward direction
Suppose a density on a common support is
$$f_\theta(x)=h(x)\exp\{\eta(\theta)^\top T(x)-A(\theta)\}.$$
Its iid sample likelihood is
$$\prod_i h(x_i)\exp\{\eta(\theta)^\top\sum_iT(x_i)-nA(\theta)\}.$$
The factorisation criterion therefore gives sufficiency of $\sum_iT(X_i)$ for every $n$. This calculation proves the exponential-family-to-sufficiency direction directly. It does not prove the reverse characterisation, which is the difficult content of the theorem.{{cite:siegrist2022_sufficient_complete}} (§7.06, Fisher–Neyman factorisation theorem)

For a Poisson rate, $T(x)=x$ and the sum is one-dimensional. With normal observations and both mean and variance unknown, the natural statistic can be taken as $(x,x^2)$, giving two sums. A re-expression such as $(\bar X,\sum(X_i-\bar X)^2)$ carries the same information when $n$ is known, since each pair of summaries can be recovered from the other by algebra.

## Worked example
### Equal sufficient summaries give equal likelihood ratios
Take two samples of size three, $(1,2,6)$ and $(0,4,5)$, each with total $9$. Under a common Poisson rate $\lambda$, their likelihood ratio is
$$\frac{L(\lambda;1,2,6)}{L(\lambda;0,4,5)}=\frac{0!4!5!}{1!2!6!}=2.000.$$
The ratio is constant in $\lambda$. Their different arrangements and values can affect a data-only factor, but their likelihoods have the same dependence on the rate. Factorisation formalises this parameter-information reduction.{{cite:siegrist2022_sufficient_complete}} (§7.06, sufficiency and likelihood ratios)

**Your turn.** Append a count of four to each sample. What are the new sample sizes and sufficient totals, and does the likelihood ratio change?

::: {.callout-tip collapse="true" title="Answer"}
Both sample sizes become four and both totals become thirteen. The identical added Poisson likelihood factor cancels from the ratio, which remains $2.000$.
:::

## Generalizations — Moving support defeats the simple converse
For iid $U(0,\theta)$ observations, the joint density is $\theta^{-n}\mathbf1\{0<\min x_i,\max x_i<\theta\}$. The maximum is sufficient: the parameter enters through its value and the factor $\theta^{-n}$. Yet the support varies with $\theta$, so the regular common-support exponential-family characterisation does not apply. This example demonstrates exactly why a condition is needed, without declaring every sufficient maximum an exponential-family statistic.{{cite:siegrist2022_sufficient_complete}} (§7.06, uniform-family sufficient statistics)

Brown also constructs examples showing that support and continuity conditions cannot simply be dropped from the specific theorems he studies. Such conditions concern both the family of distributions and the mathematical regularity of the proposed summary. A finite-dimensional sufficient statistic for one fixed sample size is much weaker than a reduction whose dimension stays bounded as the sample size increases.{{cite:brown1964_sufficiency}} (§3, ex. 3.1–3.3, pp. 1459–1460)

## Statistical use — Compression does not choose a prior
Sufficiency concerns what the sampling model allows the data to say about a parameter. Conjugacy concerns a relationship between a prior family and that likelihood. Exponential-family structure often makes conjugate updates convenient, but sufficiency alone does not prescribe the prior or require one. Conversely, the moving-support uniform model admits useful Pareto prior updates even though it lies outside the regular common-support characterisation. Keeping these questions separate prevents a computational convenience from being mistaken for a universal distributional theorem.{{cite:brown1964_sufficiency}} (§1, characterisation through the likelihood)
