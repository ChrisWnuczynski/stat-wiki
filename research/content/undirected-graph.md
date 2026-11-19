## Lead context
An undirected graph records which pairs of variables are joined, and a missing edge is a statement that those two variables carry no further dependence once the separating variables are known.{{cite:grinstead_snell1997}} (p. 164, conditional probability)

## Motivating example
Three laboratory readings are taken on each sample. The first and the third move together in the raw data, and both move with the second. If that shared movement is the whole story, then once the second reading is known the first and the third should be uninformative about each other. The graph is a path of two edges, $1-2-3$. The missing edge is the pair $\{1,3\}$. The vertex $2$ sits on the only path between them.{{cite:grinstead_snell1997}} (p. 164, conditioning)

## Intuition
An undirected edge has no arrow. The pair $\{j,k\}$ is either present once or absent. A path is a sequence of distinct vertices with an edge between each consecutive pair. A set $C$ separates $A$ from $B$ when every path from $A$ to $B$ meets $C$. On the path $1-2-3$, the singleton $\{2\}$ separates $\{1\}$ from $\{3\}$. The graph does not contain the joint distribution. It records which conditional-independence restrictions the distribution is being asked to satisfy.{{cite:grinstead_snell1997}} (p. 164, events and conditioning)

## Definition
An undirected graph $G=(V,E)$ has a finite vertex set $V$ and a set $E$ of unordered pairs of distinct vertices. There is no self-loop, and each pair is present at most once. The neighbours of $j$ are the vertices joined to $j$. The degree of $j$ is the number of neighbours. A clique is a subset in which every pair is joined. On the path $1-2-3$ the cliques are the two edges, the degrees are $1$, $2$ and $1$, and $\{2\}$ is a separator of the endpoints.{{cite:grinstead_snell1997}} (p. 164)

## Interpretation
In a statistical model on this graph, the missing edge is read as $X_1\perp X_3\mid X_2$: the conditional distribution of $(X_1,X_3)$ given $X_2$ factors. For a nonsingular Gaussian vector the same restriction is a zero in the precision matrix. Take

$$
K=\begin{pmatrix}1&-1/2&0\\ -1/2&1&-1/2\\ 0&-1/2&1\end{pmatrix}.
$$


The $(1,3)$ entry is $0$. The quadratic form is $x_1^2+x_2^2+x_3^2-x_1 x_2-x_2 x_3$. Completing the square in $x_1$ and in $x_3$ leaves no product $x_1 x_3$, so the conditional density of $(X_1,X_3)$ given $X_2$ factors. The marginal correlation of $X_1$ and $X_3$ need not be zero: both can still depend on $X_2$.{{cite:grinstead_snell1997}} (p. 164, a conditional probability factors when the variables are independent given the condition)

## Properties
The separator is not unique in a larger graph. On a triangle every pair is joined, there is no missing edge, and the empty set does not separate any pair. Adding the edge $\{1,3\}$ to the path destroys the conditional-independence restriction that the zero in $K$ expressed. A zero in the covariance matrix is a different restriction: it says the marginal covariance is zero, not the conditional one. The precision zero is the conditional statement.{{cite:grinstead_snell1997}} (p. 164)

The matrix $K$ above has determinant $1\cdot(1-1/4)-(-1/2)(-1/2)=1/2>0$, and the leading minors $1$ and $1-1/4=3/4$ are positive, so $K$ is a covariance precision: it is positive definite and can be the precision of a Gaussian vector.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write the quadratic form as

$$
(x_1-\tfrac12 x_2)^2+(x_3-\tfrac12 x_2)^2+\tfrac12 x_2^2.
$$


Expanding recovers $x_1^2+x_2^2+x_3^2-x_1 x_2-x_2 x_3$, and the cross term $x_1 x_3$ does not appear. In the Gaussian density the conditional exponent of $(x_1,x_3)$ given $x_2$ is therefore a sum of a function of $(x_1,x_2)$ and a function of $(x_3,x_2)$. The conditional joint density factors, which is $X_1\perp X_3\mid X_2$.{{cite:grinstead_snell1997}} (p. 164, conditional probability and independence)

The leading minors of $K$ are $1$, $\det\begin{pmatrix}1&-1/2\\-1/2&1\end{pmatrix}=3/4$, and $\det K=1/2$. All are positive, so $K$ is positive definite.
:::
:::

## Statistical use — Read a missing edge as a conditional statement
Report a missing edge together with the conditioning set. On this path the set is $\{2\}$, not the empty set. A marginal scatter of $X_1$ against $X_3$ can still slope. That slope is not a violation of the missing edge. A violation would be residual association after $X_2$ has been conditioned on. The numerical precision above is one Gaussian law with that property. Other distributions can share the graph and use a different conditional distribution.{{cite:grinstead_snell1997}} (p. 164)

The conditional-independence reading of a missing edge, for every distribution with a positive density and not only for the Gaussian example, is a theorem that needs positivity on a product space. The calculation above is the Gaussian quadratic form for one matrix. A discrete distribution on the same path can satisfy $X_1\perp X_3\mid X_2$ with a different parameterisation. And a sample precision with a small $(1,3)$ entry is not the same object as a model that sets the entry to zero.{{cite:grinstead_snell1997}} (p. 164, the conditional-probability definition used for one law)

## Worked example
The path has edges $\{1,2\}$ and $\{2,3\}$. Degrees are $1,2,1$. The precision $K$ has a zero in position $(1,3)$. Its determinant is $1/2$. The completed square shows the conditional exponent splits. Suppose instead the covariance, not the precision, had a zero in position $(1,3)$. That would say $\operatorname{Cov}(X_1,X_3)=0$, a marginal statement. The precision zero does not say that. For this $K$, the covariance is $K^{-1}$. The $(1,3)$ entry of the inverse need not be zero; the completed square already shows $X_1$ and $X_3$ both load on $X_2$.{{cite:grinstead_snell1997}} (p. 164)

Compute the $(1,3)$ covariance. Solving $K\Sigma=I$ gives $\Sigma_{13}=1/2$. The marginal covariance is not zero, while the precision entry is. Both numbers belong in the same example: $K_{13}=0$ and $\Sigma_{13}=1/2$.{{cite:grinstead_snell1997}} (p. 164, conditional versus unconditional information)

**Your turn.** Add the edge $\{1,3\}$, so the graph is a triangle. Does $\{2\}$ still separate $\{1\}$ from $\{3\}$?

::: {.callout-tip collapse="true" title="Answer"}
No. The direct edge is a path from $1$ to $3$ that does not meet $2$. A separator has to meet every path. The triangle has no missing edge between those endpoints.
:::

## Common misconceptions
An undirected edge is not a causal arrow. Nothing in the path says that $X_2$ causes $X_1$. The edge says that the model is not forcing a conditional independence for that pair.{{cite:grinstead_snell1997}} (p. 164)

A zero correlation is not a missing edge. The example has $K_{13}=0$ and $\Sigma_{13}=1/2$. The marginal association is $1/2$ in the covariance scale of this precision.{{cite:grinstead_snell1997}} (p. 164)

The graph is not the distribution. Two different positive definite matrices can share the same zero pattern and differ in the nonzero entries. The graph constrains which entries may be nonzero. It does not fix their values.{{cite:grinstead_snell1997}} (p. 164)

## Connections
[Conditional independence](conditional-independence.qmd) is the relation a separator is meant to encode. A [precision matrix](partial-correlation.qmd) zero is the Gaussian form of a missing edge. The path on three vertices is the smallest graph in which a marginal association and a conditional independence coexist, as $K_{13}=0$ and $\Sigma_{13}=1/2$ show.{{cite:grinstead_snell1997}} (p. 164)

## Check yourself

1. On the path $1-2-3$, what is the degree of vertex $2$?

::: {.callout-tip collapse="true" title="Answer"}
$2$. It has neighbours $1$ and $3$. The endpoints each have degree $1$.
:::

2. For the precision $K$ in the example, what is $K_{13}$, and what is $\Sigma_{13}$?

::: {.callout-tip collapse="true" title="Answer"}
$K_{13}=0$ and $\Sigma_{13}=1/2$. The missing edge is the precision zero. The marginal covariance is not zero.
:::

3. Does a self-loop appear in this definition of an undirected graph?

::: {.callout-tip collapse="true" title="Answer"}
No. An edge is a pair of distinct vertices. A loop at a vertex is excluded.
:::

## History
The path and the separator are combinatorial. The probability reading uses conditional independence: a product of conditional probabilities. Grinstead and Snell set conditional probability and independence side by side in the continuous chapter that also treats the memoryless property. The Gaussian calculation here is the same product, read off a quadratic form whose cross term $x_1 x_3$ is absent. The general equivalence between a positive density's factorisation and its missing edges is a further theorem.{{cite:grinstead_snell1997}} (p. 164, conditional probability)
