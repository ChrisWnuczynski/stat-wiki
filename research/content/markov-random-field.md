## Lead context
A Markov random field uses an undirected graph to say which variables are conditionally independent once the variables on a separating set are known.

## Motivating example
Three binary measurements stand in a line, $X-Y-Z$. The two ends need not be independent: they can share the middle. Given the middle, each end is drawn independently of the other. The missing edge between $X$ and $Z$ is that conditional independence. The graph is recording a factorisation, not a physical wire.

## Intuition — A missing edge is a conditional product
On an undirected graph, the pairwise Markov property says that variables at non-adjacent vertices are independent given all the remaining variables. The local property says that a variable is independent of the non-neighbours given its neighbours. The global property says that a set $S$ which separates $A$ from $B$ makes $X_A$ independent of $X_B$ given $X_S$. The global property implies the local one, which implies the pairwise one. The converses need extra conditions. A convenient sufficient condition is a factorisation of the joint density into functions of the cliques. {{cite:hastie_esl2009}} (§17.2, pp. 628–629, pairwise Markov property and the clique product) {{cite:pishro_nik2014}} (§5.1, conditional probability and independence)

## Definition — One line of three variables
Let $Y$ be Bernoulli$(1/2)$. Given $Y=y$, let $X$ and $Z$ be independent Bernoulli variables with success probability $0.8$ if $y=1$ and $0.2$ if $y=0$. The joint distribution factorises as
$$
\Pr(X=x,Y=y,Z=z)=\Pr(Y=y)\,\Pr(X=x\mid Y=y)\,\Pr(Z=z\mid Y=y).
$$
No factor depends on $X$ and $Z$ together. Given $Y$, the conditional joint probability of $(X,Z)$ is the product of the conditional marginals, so $X\perp Z\mid Y$.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
By construction, $\Pr(X=x,Z=z\mid Y=y)=\Pr(X=x\mid Y=y)\Pr(Z=z\mid Y=y)$. That is the definition of conditional independence of $X$ and $Z$ given $Y$. The same product is the factorisation over the two edges of the path. The marginal joint probability need not factor. Averaging the conditional product over $Y$ mixes two different success probabilities, and a mixture of products is not in general a product.{{cite:pishro_nik2014}} (§5.1, independent random variables)
:::
:::

## Worked example
Given $Y=1$, $\Pr(X=1,Z=1\mid Y=1)=0.8\times 0.8=0.64$, which equals the product of the conditional probabilities. The marginal probability is
$$
\Pr(X=1,Z=1)=\tfrac12(0.64)+\tfrac12(0.2\times 0.2)=0.32+0.02=0.34.
$$
Each end has marginal success probability $\tfrac12(0.8)+\tfrac12(0.2)=0.5$, so $\Pr(X=1)\Pr(Z=1)=0.25$. The margin $0.34$ disagrees with $0.25$, so $X$ and $Z$ are not independent. They are conditionally independent given $Y$. The missing edge does not say the ends are independent. It says they are independent once $Y$ is known.

**Your turn.** Find $\Pr(X=1\mid Y=0)$ and $\Pr(X=1,Z=1\mid Y=0)$.

::: {.callout-tip collapse="true" title="Answer"}
Given $Y=0$ the success probability is $0.2$, so $\Pr(X=1\mid Y=0)=0.2$ and $\Pr(X=1,Z=1\mid Y=0)=0.04$. The conditional probability matches the product $0.2\times 0.2$.
:::

## Connections — Graphs and conditional independence
[Conditional independence](conditional-independence.qmd) is the probability statement. [Markov properties and factorisation](markov-properties-and-factorisation.qmd) is the list of pairwise, local and global versions, together with the clique factorisation. A [Markov chain](markov-chain.qmd) in time is the special case of this line graph, with the past and the future independent given the present. The Hammersley–Clifford theorem says that a positive density has the pairwise property if and only if it factorises over the graph. The proof above covers a path graph; the general equivalence uses a longer inclusion of cliques.

## Check yourself

### Reading the graph
On the path $X-Y-Z$, which pair is conditionally independent given the third variable, and which pairs are neighbours?

::: {.callout-tip collapse="true" title="Answer"}
$X$ and $Z$ are the non-adjacent pair, so the pairwise property says $X\perp Z\mid Y$. The edges are $X-Y$ and $Y-Z$. The pairwise property does not say that an adjacent pair is conditionally independent given the remaining variable.
:::

### A numerical check of the margin
Using the worked example, compute $\Pr(X=1,Z=0)$.

::: {.callout-tip collapse="true" title="Answer"}
Given $Y=1$ the probability is $0.8\times 0.2=0.16$. Given $Y=0$ it is $0.2\times 0.8=0.16$. The marginal is $\tfrac12(0.16)+\tfrac12(0.16)=0.16$.
:::
