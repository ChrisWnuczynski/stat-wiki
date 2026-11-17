## Motivating example
Two instruments may measure nearly the same feature with different noise. Plotting their measurements often gives an elongated cloud rather than independent variation along the recorded axes. Principal component directions provide an orthogonal coordinate system adapted to that cloud. The first direction captures the greatest sample variance achievable by a unit-length linear combination, and each subsequent direction captures the greatest variance remaining under orthogonality to its predecessors.{{cite:jolliffe_cadima2016}} (§2(a), equation 2.1)

## Statement

**Directions, scores and repeated eigenvalues.**
For a centred data matrix $X_c$ with $n>1$ rows, set $S=X_c^TX_c/(n-1)$. If $a$ is a unit vector, the score column $X_ca$ has sample variance $a^TSa$. Let the eigenvalues satisfy $\lambda_1\ge\cdots\ge\lambda_p\ge0$. A unit eigenvector for $\lambda_1$ maximises this variance; successive orthonormal eigenvectors solve the corresponding constrained problems. The direction $a_j$ is a vector of loadings in feature coordinates, while $X_ca_j$ contains one score per observation. They have different dimensions and different roles.{{cite:jolliffe_cadima2016}} (§2(a), equations 2.1–2.4)

If $\lambda_j$ is simple, its unit eigenvector is unique up to sign. Reversing a direction reverses all its scores and leaves the represented axis unchanged. If eigenvalues tie, rotations inside their common eigenspace also preserve the criterion. The subspace can be identified even when a preferred basis inside it cannot.{{cite:goodfellow_bengio_courville2016}} (§2.7, symmetric eigendecompositions, pp. 41–42)

## Proof
Write $S=Q\Lambda Q^T$ with $Q$ orthogonal. For any unit $a$, let $c=Q^Ta$. Then $\sum_i c_i^2=1$ and
$$a^TSa=\sum_i\lambda_i c_i^2\le\lambda_1.$$
Equality holds for a leading eigenvector. Restricting $a$ to the orthogonal complement of the chosen leading eigenvectors sets the corresponding $c_i$ to zero and repeats the argument for the largest remaining eigenvalue. For the score matrix $T=X_cQ$, direct multiplication gives $T^TT/(n-1)=Q^TSQ=\Lambda$, so score columns are uncorrelated and have the claimed variances. Taking traces proves preservation of total variance. This algebra requires no Gaussian assumption.

## Worked example — A sum direction and a difference direction
For
$$S=\begin{pmatrix}2&1\\1&2\end{pmatrix},$$
the eigenvalues are 3 and 1. The unit directions can be chosen as $a_1=(1,1)^T/\sqrt2$ and $a_2=(1,-1)^T/\sqrt2$. A centred observation $(2,0)$ therefore has scores $(\sqrt2,\sqrt2)$. Projecting onto the first component reconstructs it as $(1,1)$, with squared reconstruction error $2$. The first component explains $3/(3+1)=75\%$ of the sample variance; the second explains $25\%$.

The 75% figure describes an average variance criterion over the sample, rather than a promise that every observation has small error. An individual point can have substantial variation along a discarded direction even when that direction has a small overall eigenvalue. Which approximation is useful depends on what the analysis needs to preserve.{{cite:goodfellow_bengio_courville2016}} (§2.12, principal components as reconstruction)

**Your turn.** For the same observation, reverse the sign of the first direction. Does its rank-one reconstruction change?

::: {.callout-tip collapse="true" title="Answer"}
The first score changes from sqrt(2) to −sqrt(2), and the direction changes sign too. Their product stays (1,1), so the reconstruction and its error are unchanged.
:::

## Statistical use — Variance preservation is a declared objective
PCA can compress, visualise or remove exact linear redundancy without observing a response variable. A direction with high explanatory variance need not be important for predicting a response, and a direction with little variance can still carry predictive information. Selecting a number of components for prediction therefore requires an assessment of predictive performance as well as the variance summary.{{cite:jolliffe_cadima2016}} (§2(a), descriptive purpose and variance criterion)

Scale also enters the objective. Multiplying one feature by a large constant changes $S$ and can change its leading direction. Correlation-based PCA applies the criterion to standardised features, while covariance-based PCA preserves the chosen measurement units. Neither transformation removes the need to identify the scientific question.{{cite:jolliffe_cadima2016}} (§2(c)(i), covariance and correlation matrix PCA)

## Common misconceptions — Uncorrelated scores need not be independent
The diagonal covariance of component scores proves only a second-moment property. Independence follows for a jointly Gaussian vector under an orthogonal diagonalisation of its covariance, but it need not hold for arbitrary distributions. For example, a symmetric variable $U$ can have zero covariance with $U^2$ even though the latter is determined completely by the former. Rotating data does not create a Gaussian distribution or eliminate nonlinear dependence.{{cite:goodfellow_bengio_courville2016}} (§3.8, independence; §3.9, covariance)
