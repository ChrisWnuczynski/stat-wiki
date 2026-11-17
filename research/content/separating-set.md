## Motivating example
Suppose two groups of variables communicate through one measured variable. Conditioning on that variable may break their dependence, even when their marginal association is strong. In an undirected graphical model this question becomes a path problem: every route between the groups must pass through the conditioning set.{{cite:goodfellow_bengio_courville2016}} (§16.2.5, pp. 569–570)

## Interpretation — Blocking every route
A set $S$ separates disjoint sets $A$ and $B$ when deleting $S$ and its incident edges leaves no path from $A$ to $B$. Blocking one path is insufficient when another route remains. A separator need not be minimal; adding vertices outside $A\cup B$ preserves separation. Cliques describe complete subsets of vertices, whereas separators describe how portions of the graph disconnect.{{cite:wainwright_jordan2008}} (§2.2, pp. 11–12; §A.1, pp. 259–260)

For a distribution Markov with respect to an undirected graph, separation implies $X_A\perp X_B\mid X_S$. The graph can encode fewer independences than the distribution actually possesses. Therefore a path that survives deletion prevents this graphical argument, but does not prove dependence for every compatible distribution. Directed graphs require their own blocking rules, including the treatment of colliders.{{cite:goodfellow_bengio_courville2016}} (§16.2.5, pp. 569–570)

## Properties — Why factorisation gives independence
Consider a finite-state model with a density proportional to a product of clique potentials. Delete $S$ and group all potentials by the resulting connected components, assigning factors involving only $S$ separately. For a fixed value $s$ with positive marginal probability, each remaining factor depends on variables from at most one component. Its normalising sum factorises into the product of the component sums. The conditional distribution given $X_S=s$ consequently factorises across these components. Marginalising within components proves the asserted independence for separated subsets. This argument establishes the direction from factorisation to separation; it does not require every permitted potential to be strictly positive.{{cite:wainwright_jordan2008}} (§2.1.2, eq. 2.2, pp. 9–10; §2.2, pp. 11–12)

## Worked example — A bridge vertex and a Gaussian chain
Take edges $12,13,23,24,34,45,46,56$. The maximal cliques are $\{1,2,3\}$, $\{2,3,4\}$ and $\{4,5,6\}$. Removing vertex $4$ separates $\{1,2,3\}$ from $\{5,6\}$. Removing only vertex $2$ does not separate $1$ from $4$: the path $1,3,4$ survives. These claims can be checked without estimating any probabilities.{{cite:wainwright_jordan2008}} (§A.1, pp. 259–260)

For a centred Gaussian vector let
$$
K=\Sigma^{-1}=\begin{pmatrix}2&-1&0\\-1&3&-1\\0&-1&2\end{pmatrix},\qquad
\Sigma=\frac18\begin{pmatrix}5&2&1\\2&4&2\\1&2&5\end{pmatrix}.
$$
The marginal correlation of coordinates one and three is $1/5$. Conditional on coordinate two, their covariance is $1/8-(1/4)(1/2)^{-1}(1/4)=0$. Equivalently, fixing $x_2$ in the Gaussian exponent leaves separate terms in $x_1$ and $x_3$, so the conditional density factorises. Thus a nonzero marginal association coexists with conditional independence through the middle variable.{{cite:rasmussen_williams2006}} (§A.2, eqs. A.2–A.3, pp. 200–201)

**Your turn.** Does deleting vertex $3$ alone separate vertices $1$ and $4$ in the six-vertex graph?

::: {.callout-tip collapse="true" title="Answer"}
No. The route $1,2,4$ remains. Deleting both $2$ and $3$ does separate $1$ from $4$.
:::

## Check yourself

### Find the boundary and separator {#self-check-ex-sl-19-1}

[Practice question](../questions/ex-sl-19-1.qmd)

Find the boundary of $\{1,2\}$ and the closure of $\{5\}$ in the six-vertex graph.

::: {.callout-tip collapse="true" title="Answer"}
The boundary of $\{1,2\}$ is $\{3,4\}$. The closure of $\{5\}$ is $\{4,5,6\}$. Vertex $4$ separates the left and right groups, and $\{2,3\}$ separates $1$ from $4$.
:::

### Read the Gaussian graph {#self-check-ex-sl-19-2}

[Practice question](../questions/ex-sl-19-2.qmd)

For the displayed precision matrix, identify the missing edge and the adjacent partial correlations.

::: {.callout-tip collapse="true" title="Answer"}
The missing edge is $1$–$3$. Conditional on the remaining coordinate, the partial correlations on edges $1$–$2$ and $2$–$3$ are $-K_{ij}/\sqrt{K_{ii}K_{jj}}=1/\sqrt6=0.408248$. The conditional correlation between $1$ and $3$ is zero.
:::
