## Motivating example
A data matrix can have many columns but only a few directions with appreciable variation. Forming its covariance matrix hides the distinction between the observation and feature spaces and squares its singular values. The singular value decomposition describes both spaces directly. It supplies a factorisation for rectangular matrices, a route to principal components and a way to identify low-rank approximations without assuming a Gaussian sampling distribution.{{cite:goodfellow_bengio_courville2016}} (§2.8, pp. 42–43)

## Definition — Separate observation and feature coordinates
For a real $n\times p$ matrix $A$ of rank $r>0$, a compact SVD is
$$A=U\Sigma V^T,$$
where $U$ is $n\times r$, $V$ is $p\times r$, $U^TU=V^TV=I_r$, and $\Sigma=\operatorname{diag}(\sigma_1,\ldots,\sigma_r)$ with $\sigma_1\ge\cdots\ge\sigma_r>0$. A full SVD completes both sets of singular vectors to square orthogonal matrices and puts the singular values in a rectangular diagonal factor. The compact version includes only positive singular values; an economy implementation can also return zero values unless those are explicitly removed.{{cite:jolliffe_cadima2016}} (§2(a), equation 2.3 and dimensions)

Multiplication gives $A^TA=V\Sigma^2V^T$ and $AA^T=U\Sigma^2U^T$. Thus the right singular vectors describe feature-space directions and the left singular vectors describe observation-space directions. Their positive eigenvalues agree, even though the two cross-product matrices may have very different dimensions.{{cite:goodfellow_bengio_courville2016}} (§2.8, equations 2.43–2.45)

## Properties — Scores, approximation and the pseudoinverse
For centred observations $X_c$, the sample covariance eigenvalues are $\sigma_j^2/(n-1)$ and the nonzero principal component score columns are $X_cV=U\Sigma$. This identifies exactly where the divisor $n-1$ belongs. A singular value is on the scale of the data matrix; its square divided by the covariance divisor is a component variance.{{cite:jolliffe_cadima2016}} (§2(a), equations 2.2–2.4)

The rank-$q$ truncated factorisation, $A_q=U_q\Sigma_qV_q^T$, minimises squared Frobenius reconstruction error among matrices of rank at most $q$. The squared error is $\sum_{j>q}\sigma_j^2$. The pseudoinverse is $A^+=V\Sigma^{-1}U^T$, inverting only positive singular values. Very small values make an inverse-sensitive calculation unstable, so a numerical rank threshold is part of a practical procedure.{{cite:jolliffe_cadima2016}} (§2(a), equation 2.5){{cite:goodfellow_bengio_courville2016}} (§2.9, pseudoinverse)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The cross-product identities follow from $U^TU=V^TV=I_r$. Orthogonal changes of coordinates preserve the Frobenius norm, so the error of the truncated SVD equals the squared norm of the discarded diagonal entries. For optimality, let $B$ be any candidate of rank at most $q$ and let $P$ project orthogonally onto its row space. Since $B(I-P)=0$, orthogonality gives
$$\|A-B\|_F^2=\|(A-B)P\|_F^2+\|A(I-P)\|_F^2\ge\operatorname{tr}(A^TA)-\operatorname{tr}(PA^TA).$$
If $v_j$ are right singular vectors, then $\operatorname{tr}(PA^TA)=\sum_j\sigma_j^2v_j^TPv_j$. Each weight $v_j^TPv_j$ lies in $[0,1]$, and their sum over an orthonormal basis is $\operatorname{rank}(P)\le q$. Because the squared singular values are ordered, this weighted sum is at most $\sum_{j\le q}\sigma_j^2$. Every candidate therefore has squared error at least $\sum_{j>q}\sigma_j^2$, and the truncated SVD attains the bound. Existence of the SVD itself follows from the spectral theorem applied to $A^TA$.
:::
:::

## Worked example — A rectangular matrix
Let
$$A=\begin{pmatrix}3&0\\0&2\\0&0\end{pmatrix}.$$
Its compact factors are $V=I_2$, $\Sigma=\operatorname{diag}(3,2)$ and $U$ consisting of the first two columns of $I_3$. The nonzero cross-product eigenvalues are 9 and 4. Keeping the first singular direction gives
$$A_1=\begin{pmatrix}3&0\\0&0\\0&0\end{pmatrix},$$
with squared reconstruction error 4 and fraction of squared matrix norm preserved $9/13=0.692308$. Its pseudoinverse is the $2\times3$ matrix with diagonal entries $1/3$ and $1/2$ and a zero final column.

These rows were not centred, so 9 and 4 are eigenvalues of $A^TA$, not automatically sample covariance eigenvalues. To perform PCA on observations represented by these rows, centring must precede the decomposition. The mathematical factorisation itself does not choose a preprocessing convention.

**Your turn.** If the singular values are 5, 3 and 1, what is the squared Frobenius error of the best rank-one approximation?

::: {.callout-tip collapse="true" title="Answer"}
It is 3²+1²=10. The first squared singular value, 25, is the captured part of the total 35.
:::

## Assumptions and limits — A factorisation is not a population model
The SVD exists for every finite real matrix and requires no positive-definite covariance. Statistical claims about stability, sampling distributions or prediction need additional assumptions. Tied singular values permit rotation inside their common subspace; sign reversals of matching left and right singular vectors also leave the matrix unchanged. Comparing two implementations should therefore focus on reconstructions or subspaces when individual vectors are not uniquely determined.{{cite:goodfellow_bengio_courville2016}} (§§2.7–2.8, eigendecomposition and SVD)

Reducing dimension by squared reconstruction error also sets a particular objective. A small singular direction may contain useful information for a response, and an outlier can create a large singular value. Assess the approximation against the intended use rather than treating the ordering alone as a guarantee of scientific relevance.{{cite:jolliffe_cadima2016}} (§2(a), descriptive PCA and low-rank approximation)

## Statistical use — Singular values, covariance eigenvalues and dimensions
A centred matrix with $n=6$ rows and a singular value $10$ contributes covariance eigenvalue $10^2/(6-1)=20$. The divisor belongs to the sample covariance, not to the singular value. In the rectangular example the singular values are $3$ and $2$, the squared values $9$ and $4$ sum to $13$, and the best rank-one approximation keeps $9/13=0.692308$ of the squared Frobenius norm. The discarded part is $4$. If the singular values were $5,3,1$, the best rank-one squared error would be $3^2+1^2=10$, and the captured part would be $25$ out of a total $35$. The ordering of squared singular values is what makes the leading terms optimal for this norm.{{cite:jolliffe_cadima2016}} (§2(a), equations 2.2–2.5)

A $20\times5$ matrix of rank $3$ has compact factors $U$, $\Sigma$ and $V$ of shapes $20\times3$, $3\times3$ and $5\times3$. The economy factorisation that also returns two zero singular values would use five columns and then require a separate decision to drop the zeros. The compact statement above keeps only the positive singular values, so the products $U^TU$ and $V^TV$ are $3\times3$ identities. Sign flips of a matched pair of columns in $U$ and $V$ leave $U\Sigma V^T$ unchanged. A comparison of two programs should check the reconstructed matrix, or the subspace, when the vectors themselves are defined only up to those signs.{{cite:goodfellow_bengio_courville2016}} (§2.8, equations 2.43–2.45){{cite:jolliffe_cadima2016}} (§2(a), equation 2.3 and dimensions)

## Interpretation — The pseudoinverse inverts the retained scale
For the worked matrix the pseudoinverse puts $1/3$ and $1/2$ on the diagonal of a $2\times3$ matrix. It sends the first standard basis vector in $\mathbb R^3$ to $(1/3,0)$, and $A$ sends that coefficient vector back to $(1,0,0)$. It sends the third standard basis vector to zero, so the composition $AA^+$ removes the left-null-space coordinate. A tiny singular value would instead be inverted to a huge coefficient. The numerical rank cutoff is the decision that such a direction is discarded rather than inverted.{{cite:goodfellow_bengio_courville2016}} (§2.9, pseudoinverse)

## Connections
Centring the rows before the decomposition is the step that makes the right singular vectors into [principal component directions](principal-component-directions.qmd) and the squared singular values, divided by $n-1$, into component variances. The [rank bound](rank-bound.qmd) on a centred matrix is the reason a covariance computed from too few rows has exact zero eigenvalues. Those zeros are zero singular values of the centred matrix, and the pseudoinverse leaves them inverted as zeros rather than as infinities.{{cite:jolliffe_cadima2016}} (§2(a), equations 2.2–2.4)
