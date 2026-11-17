## Motivating example
A running balance adds gains and losses. A small favorable average per transaction can eventually dominate ordinary random fluctuation, but that does not make short-term losses impossible. Separating the linear drift from the square-root spread helps decide which horizon matters. Variances of independent increments add, whereas their standard deviations do not.{{cite:dodge2008}} (p. 558, variance properties)

## Properties — Deriving the two scales
Linearity gives $E(S_n)=x+\sum_iE(Y_i)=x+n\mu$. Expanding the centered square gives
$$\operatorname{Var}(S_n)=\sum_i\operatorname{Var}(Y_i)+2\sum_{i<j}\operatorname{Cov}(Y_i,Y_j).$$
Independent increments have zero cross-covariances, leaving $n\sigma^2$. Thus the drift-to-standard-deviation ratio, when $\mu\ne0$, is $\sqrt n\,|\mu|/\sigma$. This ratio grows even though the absolute standard deviation also grows. The same variance algebra applies to discrete and continuous increments with finite second moments.{{cite:dodge2008}} (p. 558)

For iid increments with finite absolute mean, the strong law gives $(S_n-x)/n\to\mu$ almost surely. Under finite positive variance, the central limit theorem describes the centered fluctuations on scale $\sigma\sqrt n$. These statements have different hypotheses and modes of convergence. They do not assert that the path stays inside any fixed normal band forever.{{cite:durrett2019}} (§2.4, strong law; §3.4, central limit theorems)

## Worked example — A favorable walk can still finish down
With $P(Y_i=1)=0.6$ and $P(Y_i=-1)=0.4$, let $B_n$ count positive steps. Then $B_n\sim\operatorname{Bin}(n,0.6)$ and $S_n-x=2B_n-n$. Hence $\mu=0.2$ and $\sigma^2=4(0.6)(0.4)=0.96$. At one hundred steps the mean gain is twenty and the standard deviation is $\sqrt{96}=9.7980$. The exact probability of finishing strictly below the start is $P(B_{100}\le49)=0.01676$. An endpoint calculation uses a binomial tail, without deciding whether the walk crossed below its start earlier.{{cite:grinstead_snell1997}} (§5.1, binomial distribution; §9.1, normal approximation)

**Your turn.** With the same step probabilities, calculate the mean gain and standard deviation after twenty-five steps. At what horizon does the mean gain equal twice its standard deviation?

::: {.callout-tip collapse="true" title="Answer"}
At twenty-five steps the mean is $25(0.2)=5$ and standard deviation $\sqrt{25(0.96)}=\sqrt{24}=4.8990$. Solving $0.2n=2\sqrt{0.96n}$ for positive $n$ gives $n=96$.
:::

## Statistical use — A diffusion-scale comparison
For the symmetric unit-step walk, the standardized endpoint is $(S_n-x)/\sqrt n$. At one hundred steps the uncorrected normal approximation to finishing more than twenty units above the start is $P(Z>2)=0.02275$. The exact lattice event is $B_{100}\ge61$ and has probability $0.01760$; the continuity correction respects the attainable endpoints. A normal approximation describes typical endpoint fluctuations, not exact lattice probabilities or rare-event accuracy at every moving threshold.{{cite:grinstead_snell1997}} (§9.1, continuity correction)

## Assumptions and limits
If increments are correlated, the covariance sum can change the growth rate of variance. Infinite variance also invalidates the finite-variance normal scaling. A deterministic increment has $\sigma=0$, so the standardized CLT expression is undefined although its drift formula remains meaningful. With finite absolute mean and negative drift the strong law implies eventual negative linear growth; it does not specify a finite-horizon ruin probability.{{cite:durrett2019}} (§2.4 and §3.4)
