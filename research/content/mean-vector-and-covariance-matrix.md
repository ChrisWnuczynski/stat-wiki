## Lead context
When each observation has several measurements, an average for each coordinate gives its centre and covariances show which coordinates move together. These two summaries are the starting point for multivariate normal modelling, principal components, and linear combinations of measurements. They describe only first and second moments; they need not determine the whole joint distribution.{{cite:nist_covariance2002}} (§6.5.4.1) {{cite:golub_vanloan2013}} (§4.2)

## Motivating example
A laboratory records length and width on the same item. Its two averages describe a typical length and width, but they do not say whether unusually long items also tend to be wide. The off-diagonal covariance answers that linear-association question. Keeping both coordinates in one vector preserves the pairing of measurements from each item, which separate one-variable summaries would hide.{{cite:nist_covariance2002}} (§6.5.4.1)

## Intuition
Think of the mean vector as the centre of a point cloud and the covariance matrix as a summary of its spread and tilt. Each diagonal entry gives spread along one measurement axis. A positive off-diagonal entry means the two coordinates tend to deviate from their means in the same direction; a negative one means opposite directions. The matrix says how the spread changes when axes are combined, but a zero covariance alone does not establish independence.{{cite:nist_covariance2002}} (§6.5.4.1) {{cite:golub_vanloan2013}} (§4.2)

## Definition
For a $p$-coordinate random column vector, the transpose symbol makes the outer product of centred vectors a $p\times p$ matrix. Expectations are taken entry by entry. Finite second moments ensure that each covariance is defined.{{cite:nist_covariance2002}} (§6.5.4.1)

For $n\ge2$ independently observed copies $\mathbf X_1,\ldots,\mathbf X_n$ of this vector, let $\overline{\mathbf X}=n^{-1}\sum_i\mathbf X_i$ and

$$
S=\frac1{n-1}\sum_{i=1}^n(\mathbf X_i-\overline{\mathbf X})(\mathbf X_i-\overline{\mathbf X})^\top.
$$

Here $n$ is the number of observations, $S$ is the sample covariance matrix, and realised observations are written $\mathbf x_i$, with realised summaries $\overline{\mathbf x}$ and $s$. This distinction keeps the population matrix $\Sigma$ separate from its data-based estimate. Under independent identical sampling, $\mathbb E\overline{\mathbf X}=\boldsymbol\mu$ and $\mathbb E S=\Sigma$.{{cite:nist_covariance2002}} (§6.5.4.1)

## Properties
$\Sigma$ is symmetric and positive semi-definite: $\mathbf a^\top\Sigma\mathbf a=\operatorname{Var}(\mathbf a^\top\mathbf X)\ge0$ for every fixed $p$-vector $\mathbf a$. This gives the exact variance of any weighted total or contrast, including the $X_1-X_2$ calculation. A positive-definite $\Sigma$ has strictly positive variance for every nonzero linear combination; a singular one has at least one zero-variance combination.{{cite:nist_covariance2002}} (§6.5.4.1) {{cite:golub_vanloan2013}} (§4.2)

For a fixed matrix $A$ and vector $\mathbf b$ of compatible dimensions, $\mathbf Y=A\mathbf X+\mathbf b$ has mean $A\boldsymbol\mu+\mathbf b$ and covariance $A\Sigma A^\top$. Multiplying $X_1$ by ten multiplies its variance by one hundred and its covariances with the other coordinates by ten. Adding a constant vector shifts the mean but leaves the covariance unchanged. If $\mathbf X$ and $\mathbf X'$ are independent copies, their sum has covariance $2\Sigma$.{{cite:nist_covariance2002}} (§6.5.4.1) {{cite:golub_vanloan2013}} (§4.2)

The trace $\operatorname{tr}(\Sigma)=\sum_j\sigma_{jj}$ is total coordinate variance and also the sum of the matrix's eigenvalues. These eigenvalues are nonnegative because $\Sigma$ is positive semi-definite. When all coordinate variances are positive, $\rho_{jk}=\sigma_{jk}/\sqrt{\sigma_{jj}\sigma_{kk}}$ is their unit-free correlation, which is bounded between $-1$ and $1$. These facts make covariance matrices the input to [principal component analysis](../notes/sl-03-principal-components.qmd).{{cite:nist_covariance2002}} (§6.5.4.1) {{cite:golub_vanloan2013}} (§4.2)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The $(j,k)$ entry of $\Sigma$ is $\mathbb E[(X_j-\mu_j)(X_k-\mu_k)]$, unchanged when $j$ and $k$ are swapped; hence $\Sigma$ is symmetric. For any $\mathbf a$, centring $\mathbf a^\top\mathbf X$ gives $\operatorname{Var}(\mathbf a^\top\mathbf X)=\mathbb E[(\mathbf a^\top(\mathbf X-\boldsymbol\mu))^2]=\mathbf a^\top\Sigma\mathbf a\ge0$. Strict positivity for nonzero $\mathbf a$ is exactly positive definiteness. If the quadratic form is zero, the corresponding linear combination is constant almost surely.{{cite:nist_covariance2002}} (§6.5.4.1) {{cite:golub_vanloan2013}} (§4.2)

Linearity gives $\mathbb E(A\mathbf X+\mathbf b)=A\boldsymbol\mu+\mathbf b$. Substituting $\mathbf Y-\mathbb E\mathbf Y=A(\mathbf X-\boldsymbol\mu)$ in the outer-product definition gives $\operatorname{Cov}(\mathbf Y)=A\Sigma A^\top$. Independence makes the cross-covariance of $\mathbf X$ and $\mathbf X'$ zero, giving $\operatorname{Cov}(\mathbf X+\mathbf X')=2\Sigma$. The diagonal sum is the trace by definition; an orthogonal eigendecomposition $\Sigma=Q\Lambda Q^\top$ gives $\operatorname{tr}(\Sigma)=\operatorname{tr}(\Lambda)=\sum_j\lambda_j$, with each eigenvalue $\lambda_j\ge0$ from the quadratic-form condition. Applying that condition to two coordinates gives $\sigma_{jk}^2\le\sigma_{jj}\sigma_{kk}$, proving the correlation bound.{{cite:nist_covariance2002}} (§6.5.4.1) {{cite:golub_vanloan2013}} (§4.2)

Finally, write $\mathbf Z_i=\mathbf X_i-\boldsymbol\mu$ and $\overline{\mathbf Z}=\overline{\mathbf X}-\boldsymbol\mu$. Expanding and cancelling the cross terms yields $\sum_i(\mathbf X_i-\overline{\mathbf X})(\mathbf X_i-\overline{\mathbf X})^\top=\sum_i\mathbf Z_i\mathbf Z_i^\top-n\overline{\mathbf Z}\overline{\mathbf Z}^\top$. The two terms have expectations $n\Sigma$ and $\Sigma$ under independent identical sampling, respectively, so division by $n-1$ proves $\mathbb E S=\Sigma$. Linearity also proves $\mathbb E\overline{\mathbf X}=\boldsymbol\mu$.{{cite:nist_covariance2002}} (§6.5.4.1)
:::
:::

## Statistical use
Compute $\overline{\mathbf x}$ and $s$ to describe paired measurements before fitting a multivariate model. Their diagonals and off-diagonals reveal which axes have large variation and which measured quantities co-vary. A principal-component direction is an eigenvector of $s$; its associated eigenvalue is the sample variance along that direction.{{cite:nist_covariance2002}} (§6.5.4.1) {{cite:golub_vanloan2013}} (§4.2)

## Worked example
Suppose three paired measurements are $\mathbf x_1=(1,2)^\top$, $\mathbf x_2=(3,4)^\top$, and $\mathbf x_3=(5,0)^\top$. Their sample mean is $\overline{\mathbf x}=(3,2)^\top$. The centred vectors are $(-2,0)^\top$, $(0,2)^\top$, and $(2,-2)^\top$. Dividing the sum of their outer products by $3-1$ gives{{cite:nist_covariance2002}} (§6.5.4.1)

$$
s=\begin{pmatrix}4&-2\\-2&4\end{pmatrix}.
$$

The negative covariance says that larger first coordinates tend to go with smaller second coordinates in this three-pair sample. The observed contrasts $x_{i1}-x_{i2}$ are $-1,-1,5$, whose sample variance is $12$; matrix multiplication agrees, since $(1,-1)s(1,-1)^\top=4+4-2(-2)=12$.{{cite:nist_covariance2002}} (§6.5.4.1)

**Your turn.** For the same three pairs, find the sample variance of their sums $x_{i1}+x_{i2}$ using $s$. Would the answer be the same if the within-pair covariance were discarded?

::: {.callout-tip collapse="true" title="Answer"}
With $\mathbf a=(1,1)^\top$, the variance is $\mathbf a^\top s\mathbf a=4+4+2(-2)=4$. Discarding covariance would give $4+4=8$, so preserving pairs matters.
:::

The [sample mean and covariance exercise](../questions/ex-sl-01-1.qmd) calculates each matrix entry from observed vectors.{{cite:nist_covariance2002}} (§6.5.4.1)

## Common misconceptions
Zero covariance means no linear association when the variances are positive, while nonlinear dependence may remain. For example, a centred symmetric $X$ and $Y=X^2$ have zero covariance despite their deterministic relationship. Different joint distributions can share the same means and covariance matrix.{{cite:grinstead_snell1997}} (Ch. 6, Exs. 6.3.17–20)

## Assumptions and limits
The population matrix requires finite second moments. The unbiased sample-covariance claim requires independent observations from the same distribution; the formula can still be computed descriptively when that sampling model is not justified. Covariance depends on measurement units, so comparing raw off-diagonal entries across differently scaled variables can mislead; correlation standardises them. A singular covariance matrix cannot be inverted, which matters for Mahalanobis distances and some normal-density formulas.{{cite:nist_covariance2002}} (§6.5.4.1) {{cite:golub_vanloan2013}} (§4.2)

## Connections
Each entry of $\Sigma$ is an ordinary [covariance](covariance.qmd), with [variance](variance.qmd) on the diagonal. [Correlation](correlation.qmd) rescales those entries when the variances are positive. [Principal components](../notes/sl-03-principal-components.qmd) use eigenvectors of a covariance matrix as new axes.{{cite:nist_covariance2002}} (§6.5.4.1) {{cite:golub_vanloan2013}} (§4.2)

## History
Francis Galton's 1886 study of hereditary stature compared paired family measurements to understand regression toward an average. He analysed parents' and children's heights together, asking how the expected child height changed with parental height.{{cite:galton1886}} (pp. 246–247)
