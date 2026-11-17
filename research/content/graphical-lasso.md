## Lead context
The penalty acts on precision entries, while a common coordinate algorithm updates the covariance matrix.

## Motivating example
Several measured variables can have large pairwise correlations merely because they share neighbours in a network. To estimate conditional associations in a Gaussian model, the relevant zeros belong to the inverse covariance matrix. When the number of variables is large, unrestricted covariance inversion may be unstable or unavailable. Penalising precision entries combines estimation with selection of a sparse graph.{{cite:friedman_glasso2008}} (§§1–2)

## Definition — The penalised Gaussian likelihood
Let $S$ be the empirical covariance matrix and $K$ a positive definite precision matrix. One convention maximises
$$
\log\det K-\operatorname{tr}(SK)-\lambda\sum_{i,j}|K_{ij}|,
\qquad \lambda\geq0.
$$
The sum here includes diagonal entries and both symmetric off-diagonal entries. Stating this convention matters: omitting the diagonal penalty gives a different estimate. The Gaussian log-likelihood supplies the first two terms, while the absolute-value penalty encourages zero precision entries.{{cite:friedman_glasso2008}} (§2, eq. 1);{{cite:banerjee_elghaoui_daspremont2008}} (§2.1, eq. 1)

For a Gaussian vector, a zero off-diagonal precision entry expresses conditional independence given the other coordinates. This is a model-based conditional relationship. Neither a nonzero marginal correlation nor an estimated graph edge alone identifies a causal effect.{{cite:banerjee_elghaoui_daspremont2008}} (§1)

## Intuition — A corner permits an exact zero
Write $W=K^{-1}$. The optimality equation for the displayed convention is
$$
W-S-\lambda Z=0,
$$
where $Z_{ij}=\operatorname{sign}(K_{ij})$ for nonzero entries and $Z_{ij}\in[-1,1]$ at zero. At a zero, the interval of admissible subgradients can absorb a nonzero score. A smooth quadratic penalty has no such interval. Positive definiteness is part of the optimisation domain and must also hold at any candidate solution.{{cite:friedman_glasso2008}} (§2, subgradient equations)

The diagonal entries of a positive definite $K$ are positive. Their subgradients are therefore one, giving $W_{ii}=S_{ii}+\lambda$ under the all-entry convention. This identity helps distinguish covariance estimates from precision estimates: a diagonal of $W$ fixed by the optimisation does not mean that the same diagonal entries occur in $K$.{{cite:banerjee_elghaoui_daspremont2008}} (§2.2, pp. 487–488)

## Worked example
Take
$$
S=\begin{pmatrix}1&0.6\\0.6&1\end{pmatrix},\qquad\lambda=0.2.
$$
A candidate covariance and its inverse are
$$
W=\begin{pmatrix}1.2&0.4\\0.4&1.2\end{pmatrix},\qquad
K=\begin{pmatrix}15/16&-5/16\\-5/16&15/16\end{pmatrix}.
$$
Indeed $W-S=0.2\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$, which equals $\lambda\operatorname{sign}(K)$ entry by entry. The eigenvalues of $K$ are $5/8$ and $5/4$, so the candidate is positive definite. The negative penalised log-likelihood is convex, making this subgradient solution a global optimum.{{cite:banerjee_elghaoui_daspremont2008}} (§§2.1–2.2)

If $\lambda=0.6$, choose $W=1.6I$ and $K=0.625I$. The off-diagonal score is $-0.6$, allowed by a zero-entry subgradient $Z_{12}=-1$. The estimated edge disappears. Thresholding the empirical correlation and then inverting the resulting matrix is generally a different procedure; the calculation above checks the precision likelihood's own optimality equation.{{cite:friedman_glasso2008}} (§2)

**Your turn.** For the first estimate, find the partial correlation $-K_{12}/\sqrt{K_{11}K_{22}}$.

::: {.callout-tip collapse="true" title="Answer"}
The equal positive diagonal entries cancel in the denominator, leaving $(5/16)/(15/16)=1/3$. The empirical correlation was $0.6$, while the penalised estimate of this conditional association is $1/3$.
:::

## Properties — Covariance updates and precision recovery
The coordinate algorithm partitions the covariance estimate around one variable, solves a lasso-type subproblem, and updates the corresponding row and column. Repeating over variables solves a joint matrix problem; independently fitting neighbourhood regressions is a related approximation and need not give the same penalised likelihood solution. Recovering precision entries requires the block-inverse relation as well as the regression coefficients.{{cite:friedman_glasso2008}} (§2);{{cite:banerjee_elghaoui_daspremont2008}} (§3)

## Check yourself
Distinguish a marginal association from a conditional association.

### Thresholding correlations {#self-check-ex-sl-19-6}
[A tempting wrong turn](../questions/ex-sl-19-6.qmd): why does thresholding a correlation matrix fail to estimate Gaussian conditional independences directly?

::: {.callout-tip collapse="true" title="Answer"}
Marginal correlations belong to the covariance matrix, whereas Gaussian conditional independences correspond to zeros of the precision matrix. A sparse precision model estimates the latter pattern while respecting positive definiteness.
:::

### Reading the precision matrix {#self-check-ex-sl-19-8}
[Conditional association and sparsity](../questions/ex-sl-19-8.qmd): interpret the zeros and calculate its two partial correlations.

::: {.callout-tip collapse="true" title="Answer"}
The graph has edges $1$–$2$ and $2$–$3$. Coordinates $1$ and $3$ are conditionally independent given coordinate $2$. With diagonal entries one, the two partial correlations are $0.2$ and $-0.3$. Marginal association between coordinates $1$ and $3$ can still arise through coordinate $2$.
:::
