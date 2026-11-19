## Motivating example
Two components each work with probability $0.9$. If both are essential, the system works with probability $0.81$ under independence. If either can supply the required function, its probability of working is $0.99$. Component quality has not changed; the connection rule has. A system reliability function translates component probabilities through that rule.

## Definition — Average a binary structure function
Let $X_i\in\{0,1\}$ indicate whether component $i$ works and let $\varphi(x)\in\{0,1\}$ indicate whether the system works for state vector $x$. For independent components with $P(X_i=1)=p_i$,
$$r(p)=E\varphi(X)=\sum_{x\in\{0,1\}^m}\varphi(x)\prod_i p_i^{x_i}(1-p_i)^{1-x_i}.$$
This finite sum is a polynomial that is linear in each individual $p_i$ when the others are fixed. The independence assumption supplies the product weights. With dependent failures, marginal component reliabilities alone generally do not determine system reliability.

For a series system, $\varphi(x)=\prod_i x_i$, so $r(p)=\prod_i p_i$. For a parallel system, failure means that every component fails, giving $r(p)=1-\prod_i(1-p_i)$. A series lifetime is the minimum component lifetime; under independent lifetimes its survival function is the product of component survival functions.{{cite:nist_series_model2002}} (§8.1.8.2)

## Properties — Condition on one component
Conditioning on component $j$ gives
$$r(p)=p_jr(1,p_{-j})+(1-p_j)r(0,p_{-j}).$$
Therefore $\partial r/\partial p_j=r(1,p_{-j})-r(0,p_{-j})$. If making an additional component work cannot cause system failure, this derivative is non-negative. It measures the probability, over the other independent components, of a configuration in which component $j$ is decisive. This follows directly by subtracting the two conditional finite sums.

For a $k$-out-of-$m$ system with a common independent component probability $p$, the system works when at least $k$ components work, so $r(p)=\sum_{j=k}^m\binom mjp^j(1-p)^{m-j}$. The formula is a binomial tail evaluated for the system's threshold. Components need not share $p$ for the finite-sum definition, but the simple binomial expression then becomes a sum of unequal-probability Bernoulli configurations.{{cite:dodge2008}} (p. 44, Binomial Distribution)

## Worked example — An essential component and a backup pair
Suppose component one is essential and either component two or three must also work. With independent reliabilities $(0.9,0.8,0.7)$,
$$r=p_1\{1-(1-p_2)(1-p_3)\}=0.9(1-0.2\times0.3)=0.846.$$
Raising $p_1$ by $0.01$ raises system reliability by $0.01\times0.94=0.009400$. Raising $p_2$ by the same amount raises it by $0.01p_1(1-p_3)=0.002700$. The larger gain from improving the essential component follows from its role in this structure, rather than solely from its component reliability.

For contrast, a 2-out-of-3 system with identical component probability $0.9$ has reliability $3(0.9)^2-2(0.9)^3=0.972$. This is a different structure, even though it uses the same number of components. A comparison should keep the mission and connection requirements explicit.

**Your turn.** For the essential-component system, increase only $p_3$ from $0.7$ to $0.8$. What is the reliability gain?

::: {.callout-tip collapse="true" title="Answer"}
The gain is $0.1p_1(1-p_2)=0.1(0.9)(0.2)=0.018000$. Reliability rises from $0.846$ to $0.864$.
:::

**A further exercise.** Two independent components have reliabilities 0.9 and 0.8. What is the system reliability if they are in series, and if they are in parallel?

::: {.callout-tip collapse="true" title="Answer"}
The series reliability is $0.9\times 0.8=0.72$. The parallel reliability is $1-0.1\times 0.2=0.98$.
:::

## Assumptions and limits — Independence is a property of the failure model
A common power loss can disable two backup components together. Two marginal probabilities of $0.9$ then need not imply parallel reliability $0.99$. For example, if their states always agree, the parallel system works with probability $0.9$. This construction holds the marginals fixed and changes the joint distribution, demonstrating why independence cannot be inferred from component probabilities.{{cite:nist_series_model2002}} (§8.1.8.2, independence assumption)

A static reliability $r(p)$ refers to a specified time or mission. If $p_i(t)=P(T_i>t)$ and the component lifetimes are independent, substituting $p(t)$ into the structure polynomial gives the system survival curve. When the integral of that curve is finite, the integral equals the mean system lifetime. A higher survival probability at one time and a higher mean lifetime are different summaries, because the mean uses the whole curve.{{cite:nist_series_model2002}} (§8.1.8.2, component and system life distributions)

## Intuition — Multiply along series paths, complement along parallel paths
Under independence, a series system works when every component works, so its reliability is the product of the component reliabilities. Three components at $0.9$, $0.8$ and $0.7$ give $0.9\times0.8\times0.7=0.504$. A parallel system of the same three works when at least one works, so its failure probability is the product of the failure probabilities: $0.1\times0.2\times0.3=0.006$, and the reliability is $0.994$. The worked system, an essential component in series with a parallel pair, sits between these extremes at $0.846$. The $2$-out-of-$3$ system at a common reliability $0.9$ equals $0.972$, which is the binomial probability of at least two successes. Each formula is the structure function averaged against an independent Bernoulli product measure.{{cite:dodge2008}} (p. 44, Binomial Distribution)

The partial derivative $\partial r/\partial p_j$ equals the probability that the other components are in a state where component $j$ decides the system. For the worked structure that probability is $0.94$ for the essential component and $0.27$ for component two. Raising the essential reliability by $0.01$ therefore raises system reliability by $0.009400$, and the same increase in component two raises it by $0.002700$. The derivatives add up the configurations; they are consequences of writing $r$ as a multilinear polynomial.

## Common misconceptions
Component reliabilities of $0.9$ and $0.9$ determine the parallel reliability $1-0.1\times0.1=0.99$ when the components fail independently. If the two components always fail together, the parallel system works with probability $0.9$. The marginals are unchanged and the joint distribution has changed, so the system probability has changed. Independence is an assumption about the joint law of the state vector, and the marginal catalogue of $p_i$ does not encode it.{{cite:nist_series_model2002}} (§8.1.8.2, independence assumption)

A mission reliability at a single time is the value of the survival function at that time. The mean time to failure integrates the survival function. Two systems can be ordered one way at $t=100$ hours and the other way in the integral. Reporting the time, or the whole curve, keeps those summaries distinct.{{cite:nist_series_model2002}} (§8.1.8.2, component and system life distributions)

## Connections
The finite-sum definition is an expectation of a Bernoulli structure function. For exchangeable components with a common $p$ it reduces to a binomial tail, which is why the $k$-out-of-$m$ formula matches a binomial probability. Series and parallel lifetimes, under independent component lifetimes, turn the same algebra into a product of survival functions or a complement of a product of failure functions, evaluated at each $t$. The static number $r(p)$ is that construction at one fixed mission.
