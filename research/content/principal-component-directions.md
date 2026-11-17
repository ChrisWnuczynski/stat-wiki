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

## Worked example
### A sum direction and a difference direction
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

## Key results — A loading is a direction, a score is a coordinate
In the worked matrix the leading loading is $(1/\sqrt2,1/\sqrt2)$, about $(0.707107,0.707107)$. The centred point $(2,0)$ has leading score $\sqrt2\approx1.414214$. The rank-one reconstruction multiplies that score by the loading and returns $(1,1)$. The squared length of the residual $(1,-1)$ is $2$, which equals the second score squared. Reversing the loading and the score together leaves this product unchanged, so the fitted point does not depend on the arbitrary sign. The percentage $75$ is the share of trace attached to the first eigenvalue, $3/4$. It is an average over the sample variance, and this one point still carries squared residual $2$ in a cloud whose second eigenvalue is only $1$.{{cite:jolliffe_cadima2016}} (§2(a), equations 2.1–2.4){{cite:goodfellow_bengio_courville2016}} (§2.12, principal components as reconstruction)

If the covariance is $2I$, every unit vector has variance $2$. The eigendecomposition still exists, and every orthonormal basis diagonalises the matrix. A reported first axis is then a tie-breaking convention of the numerical routine. The subspace statement is the stable one: the leading eigenspace is the whole plane, and no unique direction maximises variance. A small perturbation that splits the eigenvalues can make a unique axis appear even though the two sample variances remain nearly equal.{{cite:goodfellow_bengio_courville2016}} (§2.7, symmetric eigendecompositions, pp. 41–42)

### Statistical use — Zero scores mark a direction the centred sample does not use
A zero eigenvalue means $a^TSa=0$ for its unit eigenvector $a$. After centring, the corresponding score column has sample variance zero and sample mean zero, so every score on that axis is zero. The centred observations lie in the span of the positive-eigenvalue directions. Projecting onto a zero-variance axis contributes nothing to reconstruction and nothing to total variance. Keeping that axis in a subsequent regression adds a column of zeros. The algebraic fact does not say that the population variance in that direction is zero; it says the observed centred sample has no scatter there.{{cite:jolliffe_cadima2016}} (§2(a), equations 2.1–2.4)

## Related concepts
A [scree plot](scree-plot.qmd) displays the ordered eigenvalues whose sum is the trace preserved by the rotation. [Scaling](scaling.qmd) changes the matrix before those eigenvalues are computed, and a covariance analysis and a correlation analysis can order directions differently. The [singular value decomposition](singular-value-decomposition.qmd) of the centred data matrix carries the same directions: component variances are squared singular values divided by $n-1$. The [rank bound](rank-bound.qmd) explains why some of those singular values, and the matching eigenvalues, are exactly zero once centring and the sample size have used up the available dimensions.{{cite:jolliffe_cadima2016}} (§2(a), equations 2.2–2.4)
