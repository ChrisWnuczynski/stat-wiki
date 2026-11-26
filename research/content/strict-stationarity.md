## Lead context
Every finite block, rather than only its average and variance, must have a law invariant under a common time shift.

## Motivating example
A monitoring process can have the same average and variance every day while its chance of an extreme observation changes between days. Comparing only a mean plot and a covariance plot would miss that change. Strict stationarity requires the entire joint distribution to be unchanged by shifting the time labels. It applies to a single observation, to a pair, and to blocks of arbitrary finite length.{{cite:pishro_nik2014}} (§10.1.4)

## Definition — Shifting the finite-dimensional laws
For a process indexed by integers, strict stationarity means that for every finite list $t_1,\ldots,t_k$ and every integer shift $h$,
$$
(X_{t_1},\ldots,X_{t_k})\overset{d}{=}
(X_{t_1+h},\ldots,X_{t_k+h}).
$$
The times must remain in the process's index set. On a one-sided sequence, this restricts the admissible shifts. Equality in distribution concerns probabilities of sets of values, and does not say that the observed blocks themselves are equal.{{cite:durrett2019}} (§6.1, pp. 331–332)

An iid sequence is strictly stationary: for distinct times the joint law is the same product of the common marginal law before and after a shift. Repeated time indices cause repeated coordinates in both blocks and preserve the same conclusion. Independence is sufficient in this example; it is absent from the definition.{{cite:pishro_nik2014}} (§10.1.4, iid example)

## Interpretation — Moments reveal only part of a law
If a strictly stationary process has finite second moments, its mean is constant and its covariance depends only on the time difference. The one-coordinate equality gives the common mean and variance; shifting a pair gives the covariance identity. Thus strict stationarity together with finite second moments implies weak stationarity. A strictly stationary sequence of iid Cauchy variables has no finite variance, so its strict stationarity alone does not satisfy the moment requirements of weak stationarity.{{cite:pishro_nik2014}} (§10.1.4, weak-sense stationarity)

Conversely, equal means and covariances do not determine an arbitrary joint distribution. They do determine a jointly Gaussian law, so a Gaussian process with constant mean and covariance depending only on lag is strictly stationary. The Gaussian qualification concerns every finite vector, rather than each observation being individually normal.{{cite:pishro_nik2014}} (§10.1.5)

## Worked example
Let observations at different times be independent. At even times let $X_t$ equal either $-1$ or $1$, each with probability $1/2$. At odd times let it equal $0$ with probability $1/2$, and each of $-\sqrt2,\sqrt2$ with probability $1/4$. At both parities,
$$
\E(X_t)=0,\qquad \E(X_t^2)=1.
$$
Independence makes $\operatorname{Cov}(X_t,X_{t+h})=0$ for $h\ne0$. These facts satisfy weak stationarity. Strict stationarity fails already for a block of length one:
$$
P(X_{2t}=0)=0,\qquad P(X_{2t+1}=0)=1/2.
$$
No longer-block calculation can repair that difference. This example isolates the distinction between invariance of moments and invariance of the full distribution.{{cite:pishro_nik2014}} (§10.1.4, stationarity definitions)

**Your turn.** Find the fourth moment at even and odd times. Which aspect of the law changes while the variance stays fixed?

::: {.callout-tip collapse="true" title="Answer"}
At even times $\E(X_t^4)=1$. At odd times it is $(1/4)4+(1/4)4=2$. The fourth moments differ, recording a change in the shapes of the one-time distributions that their equal second moments do not reveal.
:::

## Properties — Dependence can persist forever
A stationary Markov chain need not have independent coordinates. For example, start a deterministic alternating chain on $\{0,1\}$ with a fair random starting state. The two possible infinite paths have equal probability, and shifting time swaps them. The process is strictly stationary even though its next state is determined by its current state.{{cite:durrett2019}} (§6.1, Ex. 6.1.2, pp. 331–332)

An even stronger dependence example is $X_t=Z$ for every $t$, with one Bernoulli draw $Z$ shared across all times. Every shifted block is literally the same random vector, so stationarity holds. Yet the sample mean is $Z$ for every sample size. For $P(Z=1)=1/2$, it stays either zero or one instead of approaching the ensemble mean $1/2$. Strict stationarity therefore supplies no general independence or averaging guarantee. Such guarantees need additional conditions, such as ergodicity.{{cite:durrett2019}} (§6.1, stationary sequences and measure-preserving transformations)

## Check yourself
Identify whether the question compares distributions or only moments.

### Two definitions {#self-check-c-43}
[Two stationarity definitions](../questions/c-43.qmd): state the extra moment requirements in weak stationarity.

::: {.callout-tip collapse="true" title="Answer"}
Weak stationarity requires finite second moments, one constant mean, and a covariance function depending only on the lag. Strict stationarity instead requires invariance of every finite-dimensional law and does not itself require those moments to exist.
:::

### Alternating laws {#self-check-depth-stationarity-changing-laws}
[Equal moments with changing laws](../questions/depth-stationarity-changing-laws.qmd): which probability disproves strict stationarity?

::: {.callout-tip collapse="true" title="Answer"}
The probability of the value zero alternates between zero and one half. Hence the one-time distributions differ under a shift by one, even though their means are zero, variances are one, and all nonzero-lag covariances vanish.
:::
