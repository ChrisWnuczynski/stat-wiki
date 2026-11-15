## Lead context
When each observation has several measurements, an average for each coordinate gives its centre and covariances show which coordinates move together. These two summaries are the starting point for multivariate normal modelling, principal components, and linear combinations of measurements. They describe only first and second moments; they need not determine the whole joint distribution.{{cite:anderson2003_mva,nist_covariance2002}}

## Motivating example
A laboratory records length and width on the same item. Its two averages describe a typical length and width, but they do not say whether unusually long items also tend to be wide. The off-diagonal covariance answers that linear-association question. Keeping both coordinates in one vector preserves the pairing of measurements from each item, which separate one-variable summaries would hide.{{cite:nist_covariance2002}}

## Intuition
Think of the mean vector as the centre of a point cloud and the covariance matrix as a summary of its spread and tilt. Each diagonal entry gives spread along one measurement axis. A positive off-diagonal entry means the two coordinates tend to deviate from their means in the same direction; a negative one means opposite directions. The matrix says how the spread changes when axes are combined, but a zero covariance alone does not establish independence.{{cite:anderson2003_mva}}

## Definition
Use $p$ consistently for the number of coordinates of one random column vector $\mathbf X=(X_1,\ldots,X_p)^\top$; the final sentence of the retained definition above uses $n$ for the same coordinate count. Suppose every coordinate has a finite second moment. Then $\boldsymbol\mu=\mathbb E\mathbf X$ is the $p$-component mean vector and $\Sigma=\mathbb E[(\mathbf X-\boldsymbol\mu)(\mathbf X-\boldsymbol\mu)^\top]$ is the $p\times p$ covariance matrix. Its $(j,k)$ entry, $\sigma_{jk}$, is the covariance of $X_j$ and $X_k$; $\sigma_{jj}$ is the variance of $X_j$. The transpose symbol makes the outer product a matrix, while $\mathbb E$ takes expectations entry by entry.{{cite:anderson2003_mva,nist_covariance2002}}

For $n\ge2$ independently observed copies $\mathbf X_1,\ldots,\mathbf X_n$ of this vector, let $\overline{\mathbf X}=n^{-1}\sum_i\mathbf X_i$ and

$$
S=\frac1{n-1}\sum_{i=1}^n(\mathbf X_i-\overline{\mathbf X})(\mathbf X_i-\overline{\mathbf X})^\top.
$$

Here $n$ is the number of observations, $S$ is the sample covariance matrix, and realised observations are written $\mathbf x_i$, with realised summaries $\overline{\mathbf x}$ and $s$. This distinction keeps the population matrix $\Sigma$ separate from its data-based estimate. Under independent identical sampling, $\mathbb E\overline{\mathbf X}=\boldsymbol\mu$ and $\mathbb E S=\Sigma$.{{cite:nist_covariance2002}}

## Properties
As the retained interpretation states, $\Sigma$ is symmetric and positive semi-definite: $\mathbf a^\top\Sigma\mathbf a=\operatorname{Var}(\mathbf a^\top\mathbf X)\ge0$ for every fixed $p$-vector $\mathbf a$. This gives the exact variance of any weighted total or contrast, including the old $X_1-X_2$ calculation. A positive-definite $\Sigma$ has strictly positive variance for every nonzero linear combination; a singular one has at least one zero-variance combination.{{cite:anderson2003_mva}}

For a fixed matrix $A$ and vector $\mathbf b$ of compatible dimensions, $\mathbf Y=A\mathbf X+\mathbf b$ has mean $A\boldsymbol\mu+\mathbf b$ and covariance $A\Sigma A^\top$. This contains the retained rescaling rule as a special case: multiplying $X_1$ by ten multiplies its variance by one hundred and its covariances with the other coordinates by ten. Adding a constant vector shifts the mean but leaves the covariance unchanged. If $\mathbf X$ and $\mathbf X'$ are independent copies, their sum has covariance $2\Sigma$.{{cite:anderson2003_mva}}

The trace $\operatorname{tr}(\Sigma)=\sum_j\sigma_{jj}$ is total coordinate variance and also the sum of the matrix's eigenvalues. These eigenvalues are nonnegative because $\Sigma$ is positive semi-definite. When all coordinate variances are positive, $\rho_{jk}=\sigma_{jk}/\sqrt{\sigma_{jj}\sigma_{kk}}$ is their unit-free correlation, which is bounded between $-1$ and $1$. These facts make covariance matrices the input to [principal component analysis](../notes/sl-03-principal-components.qmd).{{cite:anderson2003_mva}}

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The $(j,k)$ entry of $\Sigma$ is $\mathbb E[(X_j-\mu_j)(X_k-\mu_k)]$, unchanged when $j$ and $k$ are swapped; hence $\Sigma$ is symmetric. For any $\mathbf a$, centring $\mathbf a^\top\mathbf X$ gives $\operatorname{Var}(\mathbf a^\top\mathbf X)=\mathbb E[(\mathbf a^\top(\mathbf X-\boldsymbol\mu))^2]=\mathbf a^\top\Sigma\mathbf a\ge0$. Strict positivity for nonzero $\mathbf a$ is exactly positive definiteness. If the quadratic form is zero, the corresponding linear combination is constant almost surely.{{cite:anderson2003_mva}}

Linearity gives $\mathbb E(A\mathbf X+\mathbf b)=A\boldsymbol\mu+\mathbf b$. Substituting $\mathbf Y-\mathbb E\mathbf Y=A(\mathbf X-\boldsymbol\mu)$ in the outer-product definition gives $\operatorname{Cov}(\mathbf Y)=A\Sigma A^\top$. Independence makes the cross-covariance of $\mathbf X$ and $\mathbf X'$ zero, giving $\operatorname{Cov}(\mathbf X+\mathbf X')=2\Sigma$. The diagonal sum is the trace by definition; an orthogonal eigendecomposition $\Sigma=Q\Lambda Q^\top$ gives $\operatorname{tr}(\Sigma)=\operatorname{tr}(\Lambda)=\sum_j\lambda_j$, with each eigenvalue $\lambda_j\ge0$ from the quadratic-form condition. Applying that condition to two coordinates gives $\sigma_{jk}^2\le\sigma_{jj}\sigma_{kk}$, proving the correlation bound.{{cite:anderson2003_mva}}

Finally, write $\mathbf Z_i=\mathbf X_i-\boldsymbol\mu$ and $\overline{\mathbf Z}=\overline{\mathbf X}-\boldsymbol\mu$. Expanding and cancelling the cross terms yields $\sum_i(\mathbf X_i-\overline{\mathbf X})(\mathbf X_i-\overline{\mathbf X})^\top=\sum_i\mathbf Z_i\mathbf Z_i^\top-n\overline{\mathbf Z}\overline{\mathbf Z}^\top$. The two terms have expectations $n\Sigma$ and $\Sigma$ under independent identical sampling, respectively, so division by $n-1$ proves $\mathbb E S=\Sigma$. Linearity also proves $\mathbb E\overline{\mathbf X}=\boldsymbol\mu$.{{cite:nist_covariance2002}}
:::
:::

## Statistical use
Compute $\overline{\mathbf x}$ and $s$ to describe paired measurements before fitting a multivariate model. Their diagonals and off-diagonals reveal which axes have large variation and which measured quantities co-vary. A principal-component direction is an eigenvector of $s$; its associated eigenvalue is the sample variance along that direction. A model that uses a multivariate normal distribution treats a mean vector and covariance matrix as its parameters, so estimates of them enter prediction, classification, and distance calculations.{{cite:anderson2003_mva,nist_covariance2002}}

## Worked example
Suppose three paired measurements are $\mathbf x_1=(1,2)^\top$, $\mathbf x_2=(3,4)^\top$, and $\mathbf x_3=(5,0)^\top$. Their sample mean is $\overline{\mathbf x}=(3,2)^\top$. The centred vectors are $(-2,0)^\top$, $(0,2)^\top$, and $(2,-2)^\top$. Dividing the sum of their outer products by $3-1$ gives

$$
s=\begin{pmatrix}4&-2\\-2&4\end{pmatrix}.
$$

The negative covariance says that larger first coordinates tend to go with smaller second coordinates in this tiny sample. The observed contrasts $x_{i1}-x_{i2}$ are $-1,-1,5$, whose sample variance is $12$; matrix multiplication agrees, since $(1,-1)s(1,-1)^\top=4+4-2(-2)=12$. This is a check on the matrix calculation, not a claim that three observations establish a population relationship.{{cite:nist_covariance2002}}

**Your turn.** For the same three pairs, find the sample variance of their sums $x_{i1}+x_{i2}$ using $s$. Would the answer be the same if the within-pair covariance were discarded?

::: {.callout-tip collapse="true" title="Answer"}
With $\mathbf a=(1,1)^\top$, the variance is $\mathbf a^\top s\mathbf a=4+4+2(-2)=4$. Discarding covariance would give $4+4=8$, so preserving pairs matters.
:::

## Common misconceptions
Zero covariance rules out a linear association, not every kind of dependence. The linked normal example with $Y=X^2$ has covariance zero but a deterministic nonlinear relationship. A covariance matrix also does not usually specify a full joint distribution: different distributions can share the same means and second moments. In the *multivariate normal* family, however, the mean vector and covariance matrix do determine that family's distribution.{{cite:anderson2003_mva}}

## Assumptions and limits
The population matrix requires finite second moments. The unbiased sample-covariance claim requires independent observations from the same distribution; the formula can still be computed descriptively when that sampling model is not justified. Covariance depends on measurement units, so comparing raw off-diagonal entries across differently scaled variables can mislead; correlation standardises them. A singular covariance matrix cannot be inverted, which matters for Mahalanobis distances and some normal-density formulas.{{cite:anderson2003_mva,nist_covariance2002}}

## Connections
Each entry of $\Sigma$ is an ordinary [covariance](covariance.qmd), with [variance](variance.qmd) on the diagonal. [Correlation](correlation.qmd) rescales those entries when the variances are positive. A [multivariate normal distribution](multivariate-normal-distribution.qmd) is determined by its mean vector and covariance matrix, while a [pooled covariance](pooled-covariance.qmd) combines within-group sample matrices under a shared-covariance assumption. [Principal components](../notes/sl-03-principal-components.qmd) use eigenvectors of a covariance matrix as new axes.{{cite:anderson2003_mva}}

## Check yourself
Try [variances of linear combinations](../questions/ex-sl-01-2.qmd) to practise quadratic forms, then [uncorrelated but dependent](../questions/ex-sl-01-3.qmd) to test the limit of covariance as a dependence measure. The [positive semi-definiteness question](../questions/ex-sl-01-1.qmd) checks whether a proposed matrix could be a covariance or correlation matrix.

## History
Francis Galton's 1886 study of hereditary stature compared paired family measurements to understand regression toward an average. That is an early setting in which location and association had to be considered together. Karl Pearson's 1896 paper on regression and heredity belongs to this same line of work; its publication and subject are documented, but this page does not attribute the modern covariance-matrix notation to either paper.{{cite:galton1886,pearson1896}}

Modern multivariate analysis writes those component means and covariances as a vector and matrix. The NIST e-Handbook demonstrates this with length, width, and height measured together on five items and calculates their sample mean vector and covariance matrix. Current multivariate treatments build linear-combination and normal-model methods on these summaries.{{cite:nist_covariance2002,anderson2003_mva}}
