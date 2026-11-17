## Motivating example
Three instruments share a hidden calibration effect. Their measurements may be correlated marginally even if two become independent after conditioning on a third measurement. An undirected graph records permitted conditional associations and makes separators visible. It does not say that every drawn edge is causal, or that removing an edge leaves the marginal distribution unchanged.{{cite:wainwright_jordan2008}} (§§2.1.2–2.2, pp. 9–12)

## Intuition — What an absent edge says
In a pairwise Markov graph, an absent edge $i-j$ asserts $X_i\perp X_j\mid X_{V\setminus\{i,j\}}$. This conditions on all other variables. Global separation can give a smaller conditioning set: when $S$ intersects every path from $A$ to $B$, a distribution with the global Markov property satisfies $X_A\perp X_B\mid X_S$. A graph represents a family of distributions; a particular member may have extra independences, so an edge permits a dependence without forcing one.{{cite:wainwright_jordan2008}} (§2.2)

In a factorized model, clique potentials need not sum or integrate to one. Their product is normalized by $Z$. Multiplying a potential by a positive constant changes $Z$ by that same factor and leaves the distribution unchanged. This is why graph factors should not automatically be read as marginal distributions of their cliques.{{cite:goodfellow_bengio_courville2016}} (§3.14, Structured Probabilistic Models)

## Worked example — A positive binary chain
Let $X_1,X_2,X_3\in\{0,1\}$ and set
$$p(x_1,x_2,x_3)=Z^{-1}2^{\mathbf1\{x_1=x_2\}}2^{\mathbf1\{x_2=x_3\}}.$$
The graph is the chain $1-2-3$. For either fixed middle value, summing each neighboring factor gives $3$, hence $Z=2(3)(3)=18$. Given $X_2=0$, each endpoint independently equals zero with probability $2/3$. Thus $P(X_1=0,X_3=0\mid X_2=0)=4/9$, the product of its two conditional marginals. The same factorization holds at $X_2=1$. Marginally, $P(X_1=X_3)=5/9$, exceeding $1/2$: conditional independence has not removed the association induced by the shared middle variable.{{cite:wainwright_jordan2008}} (§§2.1.2–2.2)

The six-vertex example has maximal cliques $\{1,2,3\}$, $\{2,3,4\}$ and $\{4,5,6\}$. Removing vertex 4 disconnects the first three vertices from 5 and 6, so their subvectors are independent given $X_4$ under the global property. Removing only vertex 2 does not separate 1 from 5: the path $1-3-4-5$ remains.

**Your turn.** For the binary chain, compute $P(X_1=1,X_3=0\mid X_2=0)$ and explain its product form.

::: {.callout-tip collapse="true" title="Answer"}
The first endpoint equals one with probability $1/3$ and the last equals zero with probability $2/3$. Conditional independence gives $2/9$. Directly the unnormalized weight is $1\cdot2=2$ and the fixed-middle normalizer is $9$.
:::

## Properties — Why a separator yields a factorization
For finite discrete variables, suppose a joint mass function factorizes over the cliques and $S$ separates $A$ from $B$. After fixing $X_S=s$, no clique can contain vertices from different connected components of $G\setminus S$. Collect the remaining potentials by those components. The conditional joint mass is a product of component functions. Its finite normalizing sum is the product of their sums, so the components are conditionally independent. Marginalizing components not of interest preserves the separation between $A$ and $B$. This proves factorization implies the global property in this setting.{{cite:wainwright_jordan2008}} (§§2.1.2–2.2)

The converse direction from Markov independences to factorization needs positivity conditions. On finite product spaces a strictly positive joint mass function is sufficient. With zeros, some conditioning configurations do not occur, and the independence assertions alone can lose the information required to construct all factors. This condition is about support, rather than about the visual sparsity of a graph.{{cite:goodfellow_bengio_courville2016}} (§16.2, Using Graphs to Describe Model Structure)

::: {.callout-note collapse="true" title="Conditional-independence identities for finite variables"}
::: {.proof}
Suppose $p(x,y\mid z)=p(x\mid z)p(y\mid z)$ on conditioning events with positive probability. Symmetry is immediate. Summing over all $x$ with $h(x)=u$ gives $p(u,y\mid z)=p(u\mid z)p(y\mid z)$, proving the transformation rule. Restricting instead to such a fibre and dividing by $p(u\mid z)$ shows $p(x,y\mid z,u)=p(x\mid z,u)p(y\mid z)$, proving independence after also conditioning on the function of $X$.

For contraction, combine $X\perp Y\mid Z$ and $X\perp W\mid(Y,Z)$. By the product rule,
$$p(x,y,w\mid z)=p(x\mid y,w,z)p(w,y\mid z)=p(x\mid y,z)p(w,y\mid z)=p(x\mid z)p(w,y\mid z).$$
Thus $X\perp(W,Y)\mid Z$. The displayed density characterizations follow by multiplication, division on positive conditioning marginals, and summation. For general measurable spaces the statements use versions of conditional distributions and hold almost surely, as required by their definitions.
:::
:::

## Assumptions and limits
Conditioning and marginalizing have different graphical consequences. Removing an unobserved middle variable from a chain generally creates a marginal dependence between its endpoints. In a nonsingular Gaussian model, zeros in the precision matrix describe conditional independences, whereas zeros in the covariance matrix describe marginal independences. Confusing the two matrices changes the question being answered. A fitted graph also depends on estimation and selection uncertainty; its absent edges are model statements, not deductions from a single sample correlation.{{cite:wainwright_jordan2008}} (§3.3, ex. 3.3, Gaussian models)
