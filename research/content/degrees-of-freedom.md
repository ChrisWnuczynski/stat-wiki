## Lead context
They determine which reference distribution and divisor to use after fitting a mean, a regression, or a contingency-table model. The count depends on the constraints in the particular analysis, not just on the number of observations.{{cite:nist_residual_std2002}} (§5.5.9.9.2) {{cite:fisher1922_chisq}} (pp. 87–90)

## Motivating example
Suppose five measurements are used to estimate their own mean. Once four deviations from that mean are known, the fifth is fixed because the deviations sum to zero. Thus five data values leave four free residual deviations. The same loss of one dimension explains the divisor in the usual sample variance and the reference chi-squared law under normal sampling.{{cite:siegrist2022_normals}} (§6.08)

## Intuition
Imagine the data as a point in a space with one coordinate per observation. A fitted value or a fixed margin restricts the direction in which the remaining discrepancies may move. Degrees of freedom count the independent directions in that residual space. This dimension interpretation makes the familiar counts for a sample variance, a full-rank linear fit, and a contingency table instances of the same idea, though the corresponding sampling distributions require their own assumptions.{{cite:siegrist2022_normals}} (§6.08) {{cite:fisher1922_chisq}} (pp. 87–90)

## Definition
For a linear model, the precise count is the dimension of the space left by the fitted constraints. If an $n$-component response vector is projected onto a design space of rank $p$, the residual vector has $n-p$ degrees of freedom. Here $n$ is the number of observations and $p$ is the rank of the design matrix, including an intercept when one is fitted. If columns are redundant, $p$ means the rank rather than the raw number of columns. For a sample mean alone, $p=1$ and the residual count is $n-1$. The degrees of freedom of the chi-squared law in the definition above count independent standard-normal squares.{{cite:nist_residual_std2002}} (§5.5.9.9.2) {{cite:siegrist2022_normals}} (§6.08)

## Properties
For independent normal observations with a common mean and variance $\sigma^2$, the residual sum of squares divided by $\sigma^2$ has a chi-squared distribution with $n-1$ degrees of freedom after fitting the mean. For a full-rank linear model with fixed design, independent normal errors, and $p$ fitted coefficients, the corresponding residual sum of squares has a chi-squared law with $n-p$ degrees of freedom after division by $\sigma^2$. Thus dividing the observed residual sum of squares by its degrees of freedom yields an unbiased variance estimator under these conditions.{{cite:siegrist2022_normals}} (§6.08) {{cite:nist_residual_std2002}} (§5.5.9.9.2)

For an $r\times c$ table, $r$ and $c$ are the numbers of row and column categories. The Pearson test of independence uses $(r-1)(c-1)$ degrees of freedom in its **large-sample approximation**, because the independence model has that many fewer free cell probabilities than the unrestricted model. The formula is a dimension count; it does not make the finite-sample test statistic exactly chi-squared.{{cite:fisher1922_chisq}} (pp. 87–90)

Proof idea: express each residual as an orthogonal projection. In the table case, subtract the dimensions of the independent row and column probability parameters from the unrestricted cell-probability dimension.{{cite:fisher1922_chisq}} (pp. 87–90)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let $\mathbf D$ be the fixed design matrix, $\boldsymbol\beta$ its coefficient vector, $\mathbf Y$ the response vector, and $H$ the orthogonal projection onto the column space of $\mathbf D$, with rank $p$. Put $M=I-H$, where $I$ is the identity matrix. Since $M$ is an idempotent orthogonal projection of rank $n-p$, there is an orthonormal basis in which its first $p$ coordinates vanish and its other $n-p$ coordinates are unchanged. Under $\mathbf Y=\mathbf D\boldsymbol\beta+\boldsymbol\varepsilon$ with independent normal errors $\boldsymbol\varepsilon\sim N(\mathbf0,\sigma^2 I)$, the residual is $M\mathbf Y=M\boldsymbol\varepsilon$. Orthogonal rotation preserves independent standard-normal coordinates, so $\|M\mathbf Y\|^2/\sigma^2$ is the sum of $n-p$ independent squared standard normals, hence $\chi^2_{n-p}$. Taking expectations gives $\mathbb E\|M\mathbf Y\|^2=(n-p)\sigma^2$, proving the unbiased-divisor claim. Fitting only the mean makes $H$ projection onto the constant vector and $p=1$; this yields the $n-1$ result for a fitted mean, including the case of two observations. The sum of $m$ independent normal squares in the definition above has expectation $m$ and variance $2m$, because each square has mean one and variance two. Its moment-generating function is $(1-2t)^{-m/2}$, identifying the gamma law with shape $m/2$ and rate $1/2$.{{cite:siegrist2022_normals}} (§6.08)

For the equal-correlation case, $\sum_i(X_i-\overline X)^2=\sum_i(X_i-\mu)^2-n(\overline X-\mu)^2$. If all variances are $\sigma^2$ and each distinct pair has covariance $\rho\sigma^2$, then $\operatorname{Var}(\overline X)=\sigma^2[1+(n-1)\rho]/n$. Taking expectations of the identity gives $n\sigma^2-\sigma^2[1+(n-1)\rho]=(n-1)\sigma^2(1-\rho)$; this does not assert a chi-squared law for dependent observations. **Proof sketch for the table limit.** An unrestricted table of probabilities has $rc-1$ free values. Independence uses $r-1$ free row probabilities and $c-1$ free column probabilities, leaving $(rc-1)-(r-1)-(c-1)=(r-1)(c-1)$ dimensions for discrepancy. Under the multinomial central limit theorem with positive cell probabilities, the standardised cell-count errors become jointly normal on the fixed-total subspace. Fitting the row and column probabilities projects away their tangent directions; Pearson's quadratic statistic becomes the squared length of the remaining normal vector, giving the asymptotic chi-squared law on $(r-1)(c-1)$ degrees of freedom.{{cite:fisher1922_chisq}} (pp. 87–90)
:::
:::

## Statistical use
The divisor of a sample variance, the residual mean square in regression, and the two parameters of an $F$ reference distribution are all determined by the relevant degrees of freedom. For instance, a linear fit to 12 independent normal responses with an intercept and two nonredundant slopes has nine residual degrees of freedom. A table test uses its own row-and-column count; treating all cells as free would choose the wrong chi-squared reference law. Before using either reference distribution, check the sampling assumptions and whether the model actually has the stated rank.{{cite:nist_residual_std2002}} (§5.5.9.9.2) {{cite:fisher1922_chisq}} (pp. 87–90)

## Worked example
Five observations are $8,9,10,11,12$. Their observed mean is $\overline x=10$ and the residuals are $-2,-1,0,1,2$. Their sum is zero, so only four are free. The residual sum of squares is $4+1+0+1+4=10$, and the bias-corrected sample variance is $s^2=10/(5-1)=2.5$. Dividing by five instead would give $2$, a different estimator. If these five observations came independently from one normal distribution with variance $\sigma^2$, then $4s^2/\sigma^2=10/\sigma^2$ would follow a $\chi^2_4$ law *before the data were observed*.{{cite:siegrist2022_normals}} (§6.08)

**Your turn.** A full-rank linear regression has 12 observations and estimates an intercept and two slopes. If its residual sum of squares is 18, how many residual degrees of freedom are there, and what is the residual mean square?

::: {.callout-tip collapse="true" title="Answer"}
The design rank is three, so there are $12-3=9$ residual degrees of freedom and the residual mean square is $18/9=2$.{{cite:nist_residual_std2002}} (§5.5.9.9.2)
:::

## Common misconceptions
Degrees of freedom are not always “sample size minus one”: that count applies when one independent mean constraint is fitted. A regression with a full-rank intercept and two slopes loses three dimensions, not one. Nor does subtracting a parameter count automatically prove an exact chi-squared distribution. Exact normal-square statements need normality, independence, and the specified projection; Pearson table tests use a large-sample approximation.{{cite:nist_residual_std2002}} (§5.5.9.9.2) {{cite:fisher1922_chisq}} (pp. 87–90)

## Assumptions and limits
Rank deficiency changes the linear-model count. If two design columns are identical, fitting both cannot use two independent data directions; the rank, rather than the printed number of coefficients, determines residual degrees of freedom. A residual sum of squares divided by $n-p$ can still be calculated without normal errors, but the exact chi-squared law in the proof is then unavailable. For a sparse contingency table, the usual asymptotic chi-squared calibration may be poor even though $(r-1)(c-1)$ remains the model-dimension difference.{{cite:siegrist2022_normals}} (§6.08) {{cite:fisher1922_chisq}} (pp. 87–90)

## Connections
[Sample variance](sample-variance-and-standard-deviation.qmd) divides a residual sum of squares by $n-1$ to correct its expected value. The [chi-squared distribution](chi-squared-distribution.qmd) turns the residual-space dimension into a reference law under normal sampling, and [Student's $t$ distribution](student-t-distribution.qmd) uses that law to account for an estimated variance. In [linear regression](least-squares.qmd), the design rank sets residual degrees of freedom. In a [chi-squared test of independence](chi-squared-test-of-independence.qmd), the row and column probability constraints give a different but related dimension count.{{cite:siegrist2022_normals}} (§6.08) {{cite:fisher1922_chisq}} (pp. 87–90)

## Check yourself
Try [counting degrees of freedom](../questions/ex-inf-degrees-of-freedom.qmd) for four goodness-of-fit and independence settings, then [the basis-dimension question](../questions/ex-ur-basis-dimension.qmd), which asks why a smooth's basis size and effective degrees of freedom differ.

::: {.callout-tip collapse="true" title="Answers"}
For a $4\times5$ independence table the count is $(4-1)(5-1)=12$. Eight classes with one fitted binomial parameter give $8-1-1=6$; ten classes with two fitted normal parameters give $10-1-2=7$; ten classes with those parameters known give $10-1=9$.{{cite:fisher1922_chisq}} (pp. 87–90) For a penalised smooth, effective degrees of freedom can be below its basis dimension because the penalty shrinks the fitted function.{{cite:hastie_esl2009}} (pp. 228–230)
:::

## History
Karl Pearson's chi-squared goodness-of-fit work preceded a dispute about how to calibrate the statistic when cells in a contingency table were tied by their margins. In 1922 Ronald Fisher pointed out that the row and column restrictions reduced the independent directions of discrepancy. He obtained $(r-1)(c-1)$ degrees of freedom for an $r\times c$ independence table and explained why using the raw number of cells could give a different tail probability.{{cite:fisher1922_chisq}} (pp. 87–90)
