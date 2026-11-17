## Motivating example — The same parts can form different systems
Two components each work with probability $0.9$. If both are essential, the system works with probability $0.81$ under independence. If either can supply the required function, its probability of working is $0.99$. Component quality has not changed; the connection rule has. A system reliability function translates component probabilities through that rule.{{cite:siegrist2022_bernoulli_intro}} (§11.01, “Reliability”)

## Definition — Average a binary structure function
Let $X_i\in\{0,1\}$ indicate whether component $i$ works and let $\varphi(x)\in\{0,1\}$ indicate whether the system works for state vector $x$. For independent components with $P(X_i=1)=p_i$,
$$r(p)=E\varphi(X)=\sum_{x\in\{0,1\}^m}\varphi(x)\prod_i p_i^{x_i}(1-p_i)^{1-x_i}.$$
This finite sum is a polynomial that is linear in each individual $p_i$ when the others are fixed. The independence assumption supplies the product weights. With dependent failures, marginal component reliabilities alone generally do not determine system reliability.{{cite:siegrist2022_bernoulli_intro}} (§11.01, reliability and independent component states)

For a series system, $\varphi(x)=\prod_i x_i$, so $r(p)=\prod_i p_i$. For a parallel system, failure means that every component fails, giving $r(p)=1-\prod_i(1-p_i)$. A series lifetime is the minimum component lifetime; under independent lifetimes its survival function is the product of component survival functions.{{cite:nist_series_model2002}} (§8.1.8.2)

## Properties — Condition on one component
Conditioning on component $j$ gives
$$r(p)=p_jr(1,p_{-j})+(1-p_j)r(0,p_{-j}).$$
Therefore $\partial r/\partial p_j=r(1,p_{-j})-r(0,p_{-j})$. If making an additional component work cannot cause system failure, this derivative is non-negative. It measures the probability, over the other independent components, of a configuration in which component $j$ is decisive. This follows directly by subtracting the two conditional finite sums.

For a $k$-out-of-$m$ system with a common independent component probability $p$, the system works when at least $k$ components work, so $r(p)=\sum_{j=k}^m\binom mjp^j(1-p)^{m-j}$. The formula is a binomial tail evaluated for the system's threshold. Components need not share $p$ for the finite-sum definition, but the simple binomial expression then becomes a sum of unequal-probability Bernoulli configurations.{{cite:siegrist2022_bernoulli_intro}} (§11.01, component models){{cite:dodge2008}} (p. 44, Binomial Distribution)

## Worked example — An essential component and a backup pair
Suppose component one is essential and either component two or three must also work. With independent reliabilities $(0.9,0.8,0.7)$,
$$r=p_1\{1-(1-p_2)(1-p_3)\}=0.9(1-0.2\times0.3)=0.846.$$
Raising $p_1$ by $0.01$ raises system reliability by $0.01\times0.94=0.009400$. Raising $p_2$ by the same amount raises it by $0.01p_1(1-p_3)=0.002700$. The larger gain from improving the essential component follows from its role in this structure, rather than solely from its component reliability.

For contrast, a 2-out-of-3 system with identical component probability $0.9$ has reliability $3(0.9)^2-2(0.9)^3=0.972$. This is a different structure, even though it uses the same number of components. A comparison should keep the mission and connection requirements explicit.{{cite:siegrist2022_bernoulli_intro}} (§11.01, system-state and reliability functions)

**Your turn.** For the essential-component system, increase only $p_3$ from $0.7$ to $0.8$. What is the reliability gain?

::: {.callout-tip collapse="true" title="Answer"}
The gain is $0.1p_1(1-p_2)=0.1(0.9)(0.2)=0.018000$. Reliability rises from $0.846$ to $0.864$.
:::

## Assumptions and limits — Independence is a property of the failure model
A common power loss can disable two backup components together. Two marginal probabilities of $0.9$ then need not imply parallel reliability $0.99$. For example, if their states always agree, the parallel system works with probability $0.9$. This construction holds the marginals fixed and changes the joint distribution, demonstrating why independence cannot be inferred from component probabilities.{{cite:nist_series_model2002}} (§8.1.8.2, independence assumption)

A static reliability $r(p)$ refers to a specified time or mission condition. If $p_i(t)=P(T_i>t)$ and component lifetimes are independent, composition gives the system survival curve. Its integral, when finite, is the mean system lifetime. A higher probability of surviving one chosen time does not by itself establish a larger mean lifetime: the whole survival curve enters that integral. This separates a point-in-time probability from a duration summary.{{cite:nist_series_model2002}} (§8.1.8.2, component and system life distributions)
