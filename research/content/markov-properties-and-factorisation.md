## Lead context
Markov properties turn missing edges of a graph into conditional independences, and a factorisation into clique functions is one way to build a distribution with those independences.

## Motivating example
Blood pressure, a drug dose, and a later lab result can be dependent as a pair even when, given the dose, the lab result adds nothing about the pressure. The graph is a path of length two. The missing edge is a conditional independence. The two outer variables can still be dependent when the middle variable is not held fixed.

## Intuition — Separation in the graph, independence in the distribution
Evans attaches a random variable $X_v$ to each vertex. The pairwise Markov property says that a missing edge between $i$ and $j$ means $X_i$ and $X_j$ are conditionally independent given the rest. The global Markov property says the same for every separation: if a set $S$ meets every path from $A$ to $B$, then $X_A$ and $X_B$ are conditionally independent given $X_S$. The global property implies the pairwise one, because the other vertices separate two non-adjacent vertices.{{cite:evans2025_graphical}} (§4.2, Def. 4.3 and Def. 4.4; Prop. 4.1)

A distribution factorises according to the graph when its density is a product of potentials, one for each clique. That product forces the global conditional independences. The converse, from pairwise independence back to a factorisation, needs the density to be positive.{{cite:evans2025_graphical}} (§4.3, Def. 4.6, eq. (4.1); Thm. 4.1 and Thm. 4.2)

## Definition — A path of three variables
Let the graph be the path $1-2-3$, so the cliques are $\{1,2\}$ and $\{2,3\}$. A density of the form
$$
p(x_1,x_2,x_3)=g(x_1,x_2)\,h(x_2,x_3)
$$
factorises on that graph. Given $X_2=x_2$, the joint splits into a factor in $x_1$ and a factor in $x_3$, so $X_1\perp X_3\mid X_2$.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The conditional density is $p(x_1,x_3\mid x_2)\propto g(x_1,x_2)h(x_2,x_3)$, and $x_2$ is fixed, so the right-hand side is a product of a function of $x_1$ and a function of $x_3$. That is conditional independence. The same cancellation is the path case of Evans’s theorem that a clique factorisation implies the global Markov property.{{cite:evans2025_graphical}} (Thm. 4.1)
:::
:::

## Worked example
Let $X_2$ be a fair coin, $\Pr(X_1=1\mid X_2=1)=3/4$, $\Pr(X_1=1\mid X_2=0)=1/4$, $\Pr(X_3=1\mid X_2=1)=2/3$, and $\Pr(X_3=1\mid X_2=0)=1/3$, with $X_1$ and $X_3$ conditionally independent given $X_2$. Then
$$
\Pr(X_1=X_2=X_3=1)=\frac34\cdot\frac12\cdot\frac23=\frac14.
$$
The marginal
$$
\Pr(X_1=1,X_3=1)=\frac34\cdot\frac23\cdot\frac12+\frac14\cdot\frac13\cdot\frac12=\frac{7}{24}
$$
is not the product of the marginals. Each marginal equals $1/2$, so the product is $1/4=6/24$, which is smaller than $7/24$. Conditional independence given $X_2$ does not imply marginal independence.

**Your turn.** In this same distribution, compute $\Pr(X_1=1)$.

::: {.callout-tip collapse="true" title="Answer"}
$\Pr(X_1=1)=\frac34\cdot\frac12+\frac14\cdot\frac12=\frac12$.
:::

## Connections — Precision zeros
For a regular multivariate normal, a zero in the precision matrix is the pairwise Markov property for the missing edge. The chain $1-2-3$ with
$$
K=\begin{pmatrix}2&-1&0\\-1&3&-1\\0&-1&2\end{pmatrix}
$$
has $k_{13}=0$, so $X_1\perp X_3\mid X_2$, while the marginal correlation is $1/5=0.2$.{{cite:evans2025_graphical}} (§4.2, Def. 4.3)

## Check yourself

### Precision to graph {#self-check-ex-sl-19-2}

For the precision matrix above, what is $\Sigma=K^{-1}$, and what are the partial correlations?

::: {.callout-tip collapse="true" title="Answer"}
$\det K=8$ and
$$
\Sigma=\frac18\begin{pmatrix}5&2&1\\2&4&2\\1&2&5\end{pmatrix}.
$$
The partial correlations are $1/\sqrt{6}\approx 0.408$ for the two edges and $0$ for the missing edge. The marginal correlation of $X_1$ and $X_3$ is $0.2$.
:::

### Cliques and separators {#self-check-ex-sl-19-1}

On the graph with edges $12,13,23,24,34,45,46,56$, what is the boundary of $\{1,2\}$, and is $\{2\}$ a separator of $1$ and $4$?

::: {.callout-tip collapse="true" title="Answer"}
The boundary of $\{1,2\}$ is $\{3,4\}$. The set $\{2\}$ does not separate $1$ from $4$, because the path $1-3-4$ avoids $2$. One global statement is $X_{\{1,2,3\}}\perp X_{\{5,6\}}\mid X_4$.
:::
