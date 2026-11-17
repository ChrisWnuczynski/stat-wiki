## Motivating example
An analyst has five measurements on only three cases and wants a Mahalanobis distance based on the ordinary sample covariance. The dimensions already settle one question: that covariance cannot be inverted. More precise arithmetic or a more powerful optimiser cannot supply the missing rank. The rank bound identifies an algebraic limitation before distributional assumptions or estimation algorithms enter the discussion.{{cite:jolliffe_cadima2016}} (§2(a), centred data and SVD, equations 2.2–2.4)

## Statement

**Centring limits the available column space.**
For $n>1$ observations in an $n\times p$ data matrix $X$, let $H=I_n-\mathbf1\mathbf1^T/n$ and $X_c=HX$. The sample covariance is $S=X_c^TX_c/(n-1)$, and
$$\operatorname{rank}(S)=\operatorname{rank}(X_c)\le\min(n-1,p).$$
The inequality is an upper bound, not an assertion of equality. Exact duplicate columns, linear combinations or a smaller affine support can reduce rank further. A full-rank population covariance does not remove the sample-size restriction on its empirical estimate.{{cite:jolliffe_cadima2016}} (§2(a), SVD of the column-centred data)

## Proof
The centring matrix satisfies $H^T=H$ and $H^2=H$. Its null space is the span of $\mathbf1$, so its rank is $n-1$. Every column of $X_c$ lies in $\mathbf1^\perp\subset\mathbb R^n$, giving $\operatorname{rank}(X_c)\le n-1$; its $p$ columns also bound its rank by $p$. Finally, for any $a\in\mathbb R^p$,
$$a^TX_c^TX_ca=\|X_ca\|^2.$$
Thus $X_c^TX_ca=0$ implies $X_ca=0$, and the reverse implication is immediate. The two matrices have the same null space and therefore the same rank. Multiplication by the positive scalar $1/(n-1)$ does not change it. The singular-value interpretation counts one positive covariance eigenvalue per nonzero singular value of $X_c$.{{cite:zhang_d2l2023}} (Appendix, “Eigendecompositions”, “Operations on Eigendecompositions”)

## Worked example
### Three cases and five variables
Take rows
$$(1,0,1,2,0),\quad(0,1,1,0,2),\quad(1,1,2,2,2).$$
The third column is the sum of the first two, the fourth is twice the first and the fifth is twice the second. After centring, the first two columns are linearly independent, so the covariance has rank exactly 2. Its positive eigenvalues are $7/6$ and $5/2$, with three zero eigenvalues. Their sum $11/3$ equals the trace. The nullity is therefore 3, matching the number of directions with zero empirical variance.

Adding $0.1I_5$ makes every eigenvalue positive: the three zeros become $0.1$, while the positive values become $19/15$ and $13/5$. This is a regularised covariance, with a different definition and different inferential behaviour. It does not mean the sample covariance gained information in three unobserved directions.{{cite:goodfellow_bengio_courville2016}} (§2.7, positive definite matrices and eigenvalues)

**Your turn.** If there are 12 observations on 20 variables and the centred data attain their largest possible rank, how many sample covariance eigenvalues are zero?

::: {.callout-tip collapse="true" title="Answer"}
The maximum rank is min(11,20)=11. Therefore 20−11=9 eigenvalues are zero.
:::

## Generalizations — More fitted means use more dimensions
Suppose a residual maker projects off a design matrix of rank $q$. Its rank is $n-q$, so the cross-product matrix of the residuals has rank at most $\min(n-q,p)$. Group centring is one example: with $G$ nonempty groups, estimating a separate group mean removes $G$ dimensions from the observation space. The pooled within-group scatter therefore has rank at most $\min(n-G,p)$. For $n=100$ and two groups the observation-space bound is 98. The argument is the same projection calculation with a different fitted subspace.{{cite:zhang_d2l2023}} (Appendix, “Eigendecompositions”, rank and nonzero eigenvalues)

## Statistical use — Distinguish an inverse from a chosen replacement
A pseudoinverse acts only on directions supported by the matrix. A ridge inverse assigns a positive denominator to every direction through the added penalty. These choices answer different questions and can lead to different distances or classification boundaries. Using either requires explaining the corresponding regularisation or restriction, rather than describing it as the ordinary inverse of a singular covariance.{{cite:goodfellow_bengio_courville2016}} (§2.9, Moore–Penrose pseudoinverse)

The bound should be checked inside each training fold too. A full dataset may contain enough rows for an invertible covariance while a smaller training fold does not. Algebraic diagnostics, sensible scaling and a clearly specified covariance estimator are therefore part of constructing a reproducible procedure. The theorem alone does not say which regularisation level will predict well or which confidence calibration remains valid.

## Key results — The bound is sharp, and it counts zero eigenvalues
The inequality $\operatorname{rank}(X_c)\le\min(n-1,p)$ is attained when the centred columns span a subspace of that dimension. With $12$ observations and $20$ variables, the largest possible rank is $\min(11,20)=11$. A covariance that attains the bound then has $20-11=9$ zero eigenvalues. Those zeros are required by the dimensions. They remain if the population covariance is full rank, because the sample matrix is a cross-product of centred rows that live in an $11$-dimensional subspace of $\mathbb R^{12}$. Extra observations remove the obstruction only when they increase $n-1$ past $p$ and the centred columns actually span $\mathbb R^p$.{{cite:jolliffe_cadima2016}} (§2(a), centred data and SVD, equations 2.2–2.4)

Having more rows than columns is not enough for invertibility. Thirty observations and five variables allow rank $5$, since $\min(29,5)=5$. Five centred columns can still be linearly dependent. Duplicate measurements, a variable that copies a sum of others, or a sample that happens to lie in a lower-dimensional affine subspace all leave a zero eigenvalue inside the allowance $n-1$. The sample-size bound rules some matrices out. It does not certify the matrices it allows.{{cite:zhang_d2l2023}} (Appendix, “Eigendecompositions”, rank and nonzero eigenvalues)

### Worked example — Group means spend dimensions before the covariance is formed
A pooled within-group scatter that uses $40$ observations in four nonempty groups has observation-space rank at most $40-4=36$. If the number of variables exceeds $36$, at least that excess is a lower bound on the nullity. If there are only $10$ variables, the matrix is at most $10\times10$ and the observation-space allowance of $36$ does not force any zero eigenvalue. The tighter statement is $\operatorname{rank}\le\min(36,10)=10$. Empty groups should not be counted in the $G$ of this formula: a group with no rows does not add a fitted mean. Two groups that are present do, even when one of them contains a single observation.{{cite:zhang_d2l2023}} (Appendix, “Eigendecompositions”, rank and nonzero eigenvalues)

In the three-by-five numerical example the positive eigenvalues $7/6$ and $5/2$ sum to $11/3$, the trace. The three exact zeros are the nullity. Adding $0.1$ to each eigenvalue preserves the eigenvectors and moves the trace by $0.5$. The new matrix is positive definite and its inverse exists. Distances computed from that inverse mix the two observed directions with three directions in which the original sample variance was zero. Any report of those distances needs to name the added ridge.{{cite:goodfellow_bengio_courville2016}} (§2.7, positive definite matrices and eigenvalues)

## Related concepts
The zero eigenvalues are the zero singular values of the centred data matrix, up to the covariance divisor $n-1$. The [singular value decomposition](singular-value-decomposition.qmd) makes that correspondence explicit. [Principal component directions](principal-component-directions.qmd) can still be computed in the positive-eigenvalue subspace. A Mahalanobis distance that inverts the full sample covariance cannot, until a pseudoinverse or a ridge rule states what happens on the null space.{{cite:jolliffe_cadima2016}} (§2(a), SVD of the column-centred data){{cite:goodfellow_bengio_courville2016}} (§2.9, Moore–Penrose pseudoinverse)
