## Motivating example

Two patients can be equally far from an average profile in raw units, yet one combination of measurements may be routine and the other rare. Blood pressure and pulse, for example, have different scales and may vary together. Squared Mahalanobis distance measures departure from a centre in units set by the full covariance pattern, so it can distinguish those two cases{{cite:dodge2008}} (pp. 325–326, Mahalanobis Distance).

## Definition

For a vector $x\in\mathbb R^p$, centre $\mu$ and positive-definite covariance matrix $\Sigma$, the **squared Mahalanobis distance** from $x$ to $\mu$ is $D^2(x,\mu;\Sigma)=(x-\mu)^{\mathsf T}\Sigma^{-1}(x-\mu)$. The square root is the Mahalanobis distance. Unlike ordinary squared Euclidean distance, it makes a one-unit displacement along a high-variance direction count less, and it accounts for correlations between coordinates. The covariance must refer to the population or reference group whose departures are being judged.{{cite:dodge2008}} (pp. 325–326, Mahalanobis Distance)

## Intuition

If $\Sigma=BB^{\mathsf T}$ is a Cholesky factorization, then $B^{-1}(x-\mu)$ is a whitened displacement and $D^2=\|B^{-1}(x-\mu)\|^2$. Whitening removes scale and linear correlation, so spheres in whitened coordinates become ellipsoids in the original coordinates. With $\Sigma=\operatorname{diag}(4,1)$, the points $(2,0)$ and $(0,2)$ both have Euclidean distance $2$ from the origin, but squared Mahalanobis distances $1$ and $4$. A movement of two units is ordinary along the first, more variable axis and more unusual along the second{{cite:dodge2008}} (pp. 325–326, Mahalanobis Distance).

Writing $\Sigma=SRS$ with $S=\operatorname{diag}(\sigma_1,\ldots,\sigma_p)$ and correlation matrix $R$ gives $D^2=z^{\mathsf T}R^{-1}z$ for standardized deviations $z=S^{-1}(x-\mu)$. This does not mean one may replace $\Sigma$ by $R$ while leaving the raw coordinates unchanged: standardization is essential. The geometry depends on both the scale of each coordinate and their joint alignment. {{cite:dodge2008}} (p. 325, covariance versus correlation after standardization)

## Properties

Squared Mahalanobis distance is dimensionless and unchanged by an invertible affine transformation applied consistently to $x$, $\mu$ and $\Sigma$. For any random vector with mean $\mu$, positive-definite covariance $\Sigma$ and finite second moments, its expected squared distance from that *population* mean is $p$. If the vector is multivariate normal, whitening produces $p$ independent standard-normal coordinates, so $D^2\sim\chi^2_p$. The chi-square statement is exact for the specified population parameters, not automatically for a score computed with a fitted mean and covariance from the same observations.{{cite:dodge2008}} (p. 325, expectation $p$ and normal-coordinate interpretation)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let $v=x-\mu$ and let $BB^{\mathsf T}=\Sigma$ with invertible $B$. Then $\Sigma^{-1}=B^{-\mathsf T}B^{-1}$, so $v^{\mathsf T}\Sigma^{-1}v=(B^{-1}v)^{\mathsf T}(B^{-1}v)$, proving the whitening identity and nonnegativity. For $Y=AX+b$ with invertible $A$, its mean is $A\mu+b$ and covariance is $A\Sigma A^{\mathsf T}$; using $(A\Sigma A^{\mathsf T})^{-1}=A^{-\mathsf T}\Sigma^{-1}A^{-1}$ cancels $A$ and proves affine invariance{{cite:dodge2008}} (pp. 325–326, Mahalanobis Distance).

For random $X$, put $Z=B^{-1}(X-\mu)$. It has mean zero and covariance $I_p$, so $\mathbb E(D^2)=\sum_{j=1}^p\mathbb E(Z_j^2)=p$ without assuming normality. If $X$ is multivariate normal, $Z$ is jointly normal with identity covariance; its coordinates are then independent standard normals. Their sum of squares has the $\chi^2_p$ law. Finally, substituting $\Sigma=SRS$ into the quadratic form gives $z^{\mathsf T}R^{-1}z$, with $z=S^{-1}v$. {{cite:dodge2008}} (p. 325, expected squared distance)::::::

## Statistical use — Measuring departure with the covariance

In a multivariate-normal model, equal-density contours around a mean have constant $D^2$; the $\chi^2_p$ distribution gives their probability content when the parameters are known. Gaussian discriminant analysis compares each class's squared distance to its class centre together with a covariance-determinant term and class prior, rather than choosing only the nearest centre when covariances differ. The distance also appears in outlier screening and covariance-aware clustering, where the choice of reference covariance determines what “far” means.{{cite:dodge2008}} (p. 325, classification uses)

With $p\ge n$, an ordinary sample covariance from $n$ centred observations has rank at most $n-1$, so its inverse does not exist. Two nearly collinear predictors can make an estimated inverse numerically unstable even when it exists; a small change in data then causes a large change in distances. A generalized inverse ignores directions with zero estimated variance, while regularization or dimension reduction defines a different metric that must be stated. If the data are heavy-tailed rather than normal, $\mathbb E(D^2)=p$ still holds under finite covariance, but the $\chi^2_p$ tail calibration generally fails{{cite:dodge2008}} (pp. 325–326, Mahalanobis Distance).
## Worked example

Take $\mu=(0,0)^{\mathsf T}$ and $\Sigma=\begin{pmatrix}4&1\\1&1\end{pmatrix}$, whose inverse is $\Sigma^{-1}=\frac13\begin{pmatrix}1&-1\\-1&4\end{pmatrix}$. The points $a=(2,1)$ and $b=(2,-1)$ share squared Euclidean distance $5$. Yet $D^2(a)=\frac13(4-4+4)=4/3\approx1.333$ while $D^2(b)=\frac13(4+4+4)=4$. Positive covariance makes jointly positive movements less unusual than a positive first coordinate paired with a negative second coordinate. The comparison uses a fixed, known covariance; it is a geometric comparison, not a significance test by itself{{cite:dodge2008}} (pp. 325–326, Mahalanobis Distance).

**Your turn.** Under the same $\mu$ and $\Sigma$, compare $c=(1,1)$ with $d=(1,-1)$. Both have squared Euclidean distance $2$; find their squared Mahalanobis distances.

::: {.callout-tip collapse="true" title="Answer"}
For $c$, the quadratic numerator is $1-2+4=3$, so $D^2(c)=1$. For $d$, it is $1+2+4=7$, so $D^2(d)=7/3\approx2.333$. The second point runs against the positive correlation and is farther in covariance-adjusted units.
:::

## Common misconceptions

The squared distance is not Euclidean distance with each variable merely divided by its standard deviation; correlations contribute cross-terms. A large value does not itself give an outlier $p$-value unless an appropriate reference distribution and parameters are justified. Zero correlation after whitening does not imply independence outside a joint-normal model. And a sample covariance may be singular or unstable even when the population covariance is positive definite, especially with more variables than independent observations{{cite:dodge2008}} (pp. 325–326, Mahalanobis Distance).

## Connections

The same whitening geometry underlies the multivariate-normal density, Gaussian discriminant rules and the chi-squared reference for known mean and covariance. In a normal sample, estimating the centre and covariance introduces dependencies that lead to Hotelling-type or other finite-sample calibrations, rather than the simple population $\chi^2_p$ law. Writing the covariance as scales times correlation links Mahalanobis distance to standardized variables while preserving their association{{cite:dodge2008}} (pp. 325–326, Mahalanobis Distance).

## History

Mahalanobis's group-divergence work dates to 1930, and his paper *On the Generalised Distance in Statistics* appeared in 1936. The latter gave the covariance-aware distance its enduring name and helped make a multivariate departure comparable across variables measured in different units.{{cite:dodge2008}} (pp. 325–326, history and biographical entry)
