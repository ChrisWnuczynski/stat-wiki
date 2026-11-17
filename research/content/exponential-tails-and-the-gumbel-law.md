## Motivating example
The largest waiting time in a growing collection is usually larger than a typical waiting time. For exponential observations its location grows logarithmically with sample size, allowing a stable probability approximation after centring. The relevant limit is the Gumbel distribution.{{cite:durrett2019}} (§3.2, Ex. 3.2.2, p. 123)

## Definition — A moving threshold for the maximum
Let the observations be independent exponential variables with rate $\lambda>0$. Their survival function is $e^{-\lambda t}$ for $t\ge0$.{{cite:dodge2008}} (p. 194, Exponential Distribution) At a threshold $u$, independence gives $\Pr(M_n\le u)=(1-e^{-\lambda u})^n$ when $u\ge0$. Choose $b_n=(\log n)/\lambda$ and $a_n=1/\lambda$. Then the exceedance probability at $b_n+a_nx$ is $e^{-x}/n$, of the order of one exceedance in the whole sample.{{cite:durrett2019}} (§3.2, Ex. 3.2.2(iii), p. 123)

## Properties — From an exact probability to a limit
For fixed $x$, $n$ eventually exceeds $e^{-x}$ and the threshold is positive. Writing $a=e^{-x}$ gives
$$
\log\Pr((M_n-b_n)/a_n\le x)=n\log(1-a/n)\longrightarrow-a.
$$
Exponentiating yields $G(x)=\exp(-e^{-x})$. A first-order logarithm expansion establishes this special exponential case directly. The exponential law's scale change from rate one to rate $\lambda$ only divides both centring and scale by $\lambda$.{{cite:durrett2019}} (§3.2, Ex. 3.2.2(iii), p. 123) The mean of a single observation, $1/\lambda$, is a different quantity from the centring of a sample maximum.{{cite:dodge2008}} (p. 194, Exponential Distribution)

## Worked example — Exact and limiting medians
For $n=100$ and rate one, $b_n=4.605170$ and the median of $G$ is $-\log\log2=0.366513$. The approximation to the maximum's median is $4.971683$. The exact median solves $(1-e^{-u})^{100}=1/2$, giving $u=-\log(1-2^{-1/100})=4.975147$. The approximation is close for this sample size, but the finite-sample distribution still has a left endpoint. At the centred threshold $x=0$, the exact probability is $0.99^{100}=0.366032$, compared with the limit $e^{-1}=0.367879$.

**Your turn.** For rate two and the same sample size, what is the approximate median of the maximum?

::: {.callout-tip collapse="true" title="Answer"}
Divide the rate-one location and scale by two. The approximate median is $2.485842$, with $b_n=(\log100)/2$ and $a_n=1/2$.
:::

## Connections — Tail shape determines the normalisation

[]{#property-normal-gumbel-limit}
The formula above uses the exact exponential tail. A normal maximum also has a Gumbel limit, but needs different centring and scaling; its leading centring is of order $\sqrt{2\log n}$. A power-law maximum instead grows at a power rate. These comparisons require the tail assumptions of each case.{{cite:durrett2019}} (§3.2, Exs. 3.2.2–3.2.3, pp. 123–124)

