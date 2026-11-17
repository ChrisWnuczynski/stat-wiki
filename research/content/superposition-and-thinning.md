## Motivating example
A service desk receives requests from two independent sources and then sends each request to a specialist with a fixed probability. Superposition combines the incoming rates; thinning splits the combined stream into new streams. Both operations preserve the Poisson model when their independence assumptions hold.{{cite:siegrist2022_poisson_splitting}} (§ “Superposition”)

## Properties — Add counts, then check increments
Let $N_1,N_2$ be independent homogeneous Poisson processes with rates $\lambda_1,\lambda_2$. On an interval of length $t$, the probability generating function of their sum is
$$
E\{z^{N_1(t)+N_2(t)}\}=e^{\lambda_1t(z-1)}e^{\lambda_2t(z-1)}
=e^{(\lambda_1+\lambda_2)t(z-1)}.
$$
Thus the summed count is Poisson with mean $(\lambda_1+\lambda_2)t$. Counts on disjoint intervals remain independent, since the summands on those intervals form independent groups. Together these properties prove that the superposition is a Poisson process, rather than merely giving the right one-time count distribution.{{cite:siegrist2022_poisson_splitting}} (§ “Superposition”, Two Processes)

For thinning, independently mark every arrival with probability $r$, independently also of the arrival process. Write $A(t)$ for selected arrivals and $B(t)$ for the rest. Given $N(t)=n$, their joint generating function is $(rs+(1-r)u)^n$. Averaging over the Poisson total yields
$$
E\{s^{A(t)}u^{B(t)}\}=\exp\{\lambda rt(s-1)\}\exp\{\lambda(1-r)t(u-1)\}.
$$
The factorisation establishes independent Poisson counts of rates $r\lambda$ and $(1-r)\lambda$. Applying the same argument to disjoint intervals establishes independence of the two entire processes.{{cite:durrett2019}} (§3.7.2, Thm. 3.7.4, eq. 3.7.2, pp. 178–179)

## Interpretation — Conditioning changes the dependence
Unconditionally the two thinned streams are independent. Given a fixed total $n$, however, $B(t)=n-A(t)$, so they are negatively related unless the marking probability is an endpoint. These statements concern different conditioning information and are compatible. The conditional selected count is binomial with parameters $n,r$.{{cite:siegrist2022_poisson_splitting}} (§ “Thinning”, The Two-Type Process)

Independent time-dependent marking with probability $r(s)$ produces a nonhomogeneous process of intensity $\lambda r(s)$. Its expected count on an interval is the integral of that intensity. Selecting arrivals according to their history or imposing a fixed selected count does not satisfy this independent-marking argument.{{cite:durrett2019}} (§3.7.2, Thm. 3.7.5, p. 179)

## Worked example — Reconstructing two streams
Independent request streams at rates three and five per hour combine to rate eight. Independently assign each combined arrival a type-one label with probability $3/8$. The resulting rates are three and five, and the two labelled streams are independent. The probability of no arrivals of either type in an hour is $e^{-3}e^{-5}=e^{-8}=0.000335463$. Given eight total requests, the type-one count is binomial with mean three and variance $15/8$.

Independence is essential for superposition. Combining a process of rate four with an identical copy gives counts $2N(t)$, which are always even. Their mean is eight per hour, but their distribution is not Poisson with that rate.

**Your turn.** A detector independently observes each arrival with probability $0.6$ from a rate-ten process. What are the observed and missed rates, and their one-hour covariance?

::: {.callout-tip collapse="true" title="Answer"}
The rates are six and four per hour. The two processes are independent, so the covariance of their one-hour counts is zero.
:::

## Check yourself

### A rate and an interval {#self-check-ex-sp-poisson-half-hour}

[Practice question](../questions/ex-sp-poisson-half-hour.qmd)

At rate three per hour, find the probability of two arrivals in half an hour and of waiting more than twenty minutes.

::: {.callout-tip collapse="true" title="Answer"}
The half-hour count has mean $1.5$, so its probability at two is $e^{-1.5}1.5^2/2=0.251021$. The no-arrival probability for twenty minutes is $e^{-1}=0.367879$.
:::

### Condition on the total {#self-check-ex-sp-conditional-times}

[Practice question](../questions/ex-sp-conditional-times.qmd)

Given exactly three arrivals in two hours, what is the probability that all occur in the first hour?

::: {.callout-tip collapse="true" title="Answer"}
Conditional locations are independent uniform points on the two-hour interval before ordering. Each falls in the first half with probability $1/2$, giving $(1/2)^3=1/8$.
:::
