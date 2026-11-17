## Lead context
The Hammersley–Clifford theorem ties the missing edges of an undirected graph to a factorisation of a positive joint distribution.

## Motivating example
Three binary coordinates sit on the path $1-2-3$. The unnormalised weight $\exp(0.5\,x_1 x_2+0.3\,x_2 x_3)$ factors across the two edges. Given $x_2=1$, the conditional odds of $x_1=1$ against $x_1=0$ equal $e^{0.5}$.

## Statement
**Positive laws factorise on the cliques.** Let $G$ be an undirected graph on the coordinates of a random vector. The pairwise Markov property says that if two coordinates are not joined by an edge, they are conditionally independent given the rest. For a distribution that is positive on a product space, that property is equivalent to a factorisation of the joint density into clique potentials,
$$
f(x)=\frac1Z\prod_{C}\psi_C(x_C),
$$
where each potential $\psi_C$ depends only on the coordinates in one clique and $Z$ makes the product sum or integrate to one. The potentials need not themselves be densities. The positivity condition matters: a zero in the support can separate pairwise conditional independence from this product form.{{cite:hastie_esl2009}} (§17.2, pp. 628–629, pairwise Markov property and the clique product)

## Intuition — A missing edge drops a variable from the conditional odds
In the product, a coordinate that does not share a clique with another coordinate cannot appear in that other coordinate's factors. Conditioning on the shared neighbours therefore removes the distant coordinate from the conditional odds. The graph is a picture of which variables are allowed to sit inside the same factor.{{cite:hastie_esl2009}} (§17.2, pp. 628–629)

## Worked example
Take three binary coordinates and the chain graph $1-2-3$, whose maximal cliques are the edges $\{1,2\}$ and $\{2,3\}$. The unnormalised weight
$$
\psi(x)=\exp(0.5\,x_1 x_2+0.3\,x_2 x_3)
$$
is a product of a function of $(x_1,x_2)$ and a function of $(x_2,x_3)$. Given $x_2=1$, the conditional odds of $x_1=1$ against $x_1=0$ equal $e^{0.5}\approx 1.649$, whether $x_3$ is $0$ or $1$. Given $x_2=0$ those odds equal $1$ for both values of $x_3$. The eight unnormalised weights sum to about $10.224$, and
$$
\Pr(X_1=1\mid X_2=1,X_3=0)=\frac{e^{0.5}}{1+e^{0.5}}\approx 0.622.
$$
The same conditional probability is obtained if $X_3$ is $1$ instead of $0$. The missing edge has removed $X_3$ from the conditional distribution of $X_1$.{{cite:hastie_esl2009}} (§17.2, p. 629, clique product)

**Your turn.** In this factorisation, find $\Pr(X_3=1\mid X_2=1,X_1=0)$ and check that it does not change if $X_1$ is set to $1$.

::: {.callout-tip collapse="true" title="Answer"}
Given $x_2=1$, the conditional odds of $x_3=1$ against $x_3=0$ equal $e^{0.3}\approx 1.350$, with or without $x_1$. The conditional probability is $e^{0.3}/(1+e^{0.3})\approx 0.574$. The factor $e^{0.5 x_1}$ is common to both values of $x_3$ and cancels.
:::

## Check yourself

A complete graph on three vertices can be written with a single three-way potential or with three pairwise potentials. Do those two writings have to be the same distribution?

::: {.callout-tip collapse="true" title="Answer"}
No. A product of three pairwise potentials is a special case of a three-way potential. The complete graph does not say which of those dependence orders is present.
:::

If one of the eight binary atoms is given probability zero, does the pairwise calculation above still guarantee a clique factorisation for every other pattern of conditional independence?

::: {.callout-tip collapse="true" title="Answer"}
No. The equivalence uses a positive distribution. A zero atom can break the step from pairwise conditional independence to a product of clique potentials.
:::

## Related concepts
The pairwise statement is conditional independence of two coordinates given the others, the relation drawn as a missing edge. For a non-singular multivariate normal, that edge is also a zero in the precision matrix. The global Markov property, that a separating set makes the two sides conditionally independent, agrees with the pairwise property when the distribution is positive.{{cite:hastie_esl2009}} (§17.2, pp. 628–629)
