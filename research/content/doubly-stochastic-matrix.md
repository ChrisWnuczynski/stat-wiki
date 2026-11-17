## Lead context
For a finite transition matrix, column sums determine whether a uniform starting distribution remains uniform after one step.

## Motivating example
Suppose an object occupies one of three positions. At each update it either stays in its position or moves one position around a cycle, each with probability one half. No position is distinguished by this rule. A uniform distribution over positions remains uniform after an update, even though the transition matrix is asymmetric. Stationary distributions describe such invariance of the starting law.{{cite:pishro_nik2014}} (§11.2.6)

## Definition — Two directions of summation
A square matrix $P$ is doubly stochastic when its entries are nonnegative, each row sums to one, and each column sums to one. With row distributions, the transition rule is $\pi_{n+1}=\pi_nP$. Row sums ensure that each row specifies transition probabilities. Column sums are a separate condition: they describe the total probability entering each destination when starting mass is spread equally over the source states.{{cite:pishro_nik2014}} (§11.2.6, stationary equation)

On $m$ states let $u=(1/m,\ldots,1/m)$. Then
$$
(uP)_j=\frac1m\sum_iP_{ij}.
$$
Hence $uP=u$ if and only if every column sum equals one. For a finite row-stochastic matrix, having the uniform stationary law is therefore equivalent to double stochasticity. It does not imply that every stationary law is uniform unless uniqueness also holds.{{cite:grinstead_snell1997}} (§11.3, fixed probability vectors)

## Properties — Products and randomised choices
If $P$ and $Q$ are doubly stochastic matrices of the same size, then $PQ$ is doubly stochastic. In vector notation, with $\mathbf1$ the all-ones column,
$$
PQ\mathbf1=P\mathbf1=\mathbf1,
\qquad \mathbf1^\top PQ=\mathbf1^\top Q=\mathbf1^\top.
$$
Its entries are nonnegative because they are sums of products of nonnegative entries. Repeating the argument shows that every transition power $P^n$ is doubly stochastic. The same row and column identities show that $aP+(1-a)Q$ is doubly stochastic for $0\leq a\leq1$. Such a mixture corresponds to randomly choosing between two update rules.{{cite:grinstead_snell1997}} (§11.1, powers of a transition matrix);{{cite:pishro_nik2014}} (§11.2.6)

Symmetry of a stochastic matrix is sufficient for double stochasticity, since a column then has the same sum as the corresponding row. Symmetry is a stronger restriction: the cyclic update below is doubly stochastic without being symmetric. With a uniform distribution, detailed balance requires $P_{ij}=P_{ji}$, so double stochasticity alone does not ensure reversibility.{{cite:grinstead_snell1997}} (§11.3, fixed vectors)

## Worked example
For the stay-or-cycle update, with states in cyclic order,
$$
P=\begin{pmatrix}1/2&1/2&0\\0&1/2&1/2\\1/2&0&1/2\end{pmatrix}.
$$
Every row and every column sums to one. Starting with the uniform row gives $uP=u$. Starting in the first state instead gives a different law after four steps:
$$
(1,0,0)P^4=(5/16,5/16,3/8).
$$
This is not uniform. A stationary distribution describes an invariant starting law; it does not make every finite-time law stationary. The square $P^2$ has strictly positive entries, so this example is a regular finite chain and its powers converge to the uniform stationary row.{{cite:grinstead_snell1997}} (§11.3, regular chains and their limiting matrices)

**Your turn.** Replace the stay-or-cycle update by moving clockwise with probability one. Is the matrix still doubly stochastic, and does a point starting distribution converge?

::: {.callout-tip collapse="true" title="Answer"}
The update is a permutation matrix: every row and column contains exactly one entry equal to one. It is doubly stochastic and preserves the uniform law. A point starting law rotates around the three states and returns every three steps, so it has no limit.
:::

## Interpretation — Invariance does not establish convergence
[]{#property-regular-chain-convergence}

The identity matrix is also doubly stochastic. Every distribution is stationary for it, since no state changes. A deterministic cycle has a unique stationary law but periodic point-start behaviour. These examples separate three questions: whether a stationary law exists, whether it is unique, and whether transition probabilities converge to it. Conditions involving communication and periodicity address the latter two questions.{{cite:grinstead_snell1997}} (§11.3, ergodic and regular chains)

## Check yourself
Check both the matrix sums and the behaviour from the stated initial law.

### Column sums {#self-check-ex-sp-doubly-stochastic}
[A doubly stochastic matrix](../questions/ex-sp-doubly-stochastic.qmd): prove uniform invariance directly.

::: {.callout-tip collapse="true" title="Answer"}
For each destination $j$, $(uP)_j=m^{-1}\sum_iP_{ij}=m^{-1}$. Thus every coordinate of $uP$ agrees with $u$.
:::

### A three-cycle {#self-check-ex-sp-deterministic-cycle}
[A deterministic three-cycle](../questions/ex-sp-deterministic-cycle.qmd): what is the probability of returning to the initial state after $n$ steps?

::: {.callout-tip collapse="true" title="Answer"}
It equals one when $n$ is divisible by three and zero otherwise. Its failure to converge is compatible with the uniform distribution being stationary.
:::
