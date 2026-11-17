## Lead context
A coefficient estimate has a normal sampling law under Gaussian errors. A ratio that estimates its unknown scale has a Student law. The simple-regression slope test is the one-predictor instance of this construction.{{cite:dodge2008}} (p. 493)

## Motivating example
A fitted coefficient is $1.5$, but a test concerns whether its population value is $0.5$. Reporting the difference $1$ does not account for the design or residual variation. With an estimated standard error of $1$, the comparison becomes $t=1$. The reference law needs residual degrees of freedom as well as the observed ratio.{{cite:dodge2008}} (pp. 492–493)

## Statement
Condition on a fixed full-rank design $X\in\mathbb R^{n\times p}$ with $n>p$, and assume $Y\sim N_n(X\beta,\sigma^2 I_n)$, $\sigma^2>0$. Put $C=(X^\top X)^{-1}$ and $s^2=\|Y-X\widehat\beta\|^2/(n-p)$. Then the displayed ratio is exact for each coefficient $j$. The denominator uses the residual divisor $n-p$, and $c_{jj}>0$ follows from positive definiteness of $C$. The normal/independent-chi-squared construction is the defining route to the Student law.{{cite:siegrist2022_normals}} (§6.8, “The T Variable”)

## Proof
Let $H=X(X^\top X)^{-1}X^\top$. The coefficient error is $C X^\top\varepsilon$, and the residual is $(I-H)\varepsilon$. Their cross-covariance is $\sigma^2 C X^\top(I-H)=0$. Since both are linear functions of one Gaussian vector, they are independent. Choose an orthonormal basis whose first $p$ vectors span the column space of $X$. In this basis $(I-H)\varepsilon/\sigma$ has $n-p$ independent standard normal coordinates and $p$ zero coordinates. Therefore $U=\mathrm{SSE}/\sigma^2\sim\chi^2_{n-p}$. Meanwhile $Z=(\widehat\beta_j-\beta_j)/(\sigma\sqrt{c_{jj}})\sim N(0,1)$ independently of $U$. Substitution gives $Z/\sqrt{U/(n-p)}$, which has the required $t_{n-p}$ law.{{cite:siegrist2022_normals}} (§6.8, “The Sample Variance” and “The T Variable”)

## Worked example
For $n=8$, $p=3$, $\mathrm{SSE}=20$ and $c_{jj}=1/4$, $s^2=4$ and $s\sqrt{c_{jj}}=1$. If $\widehat\beta_j=1.5$, testing $\beta_j=0.5$ gives $t=1$ on $5$ degrees of freedom and two-sided probability $0.3632$. The $0.975$ quantile is $2.5706$, giving a $95\%$ interval $1.5\pm2.5706$, or approximately $[-1.0706,4.0706]$. Inverting the acceptance condition $|t|\le t_{5,0.975}$ derives this interval; no new distributional argument is needed.{{cite:dodge2008}} (p. 493)

**Your turn.** Test $\beta_j=0$ with the same summaries. What changes if SSE doubles while the design and coefficient stay fixed?

::: {.callout-tip collapse="true" title="Answer"}
The first test gives $t=1.5$, with two-sided probability $0.1939$. Doubling SSE multiplies the standard error by $\sqrt2$, divides either $t$ ratio by $\sqrt2$, and widens the interval by that factor.
:::

## Common misconceptions — The random coefficient and its pivot
The coefficient estimator $\widehat\beta$, with $\beta$ and $X$ held fixed, keeps a normal sampling law when the errors are Gaussian, whether or not $\sigma^2$ is known. The Student law belongs to the ratio that divides a centred coefficient by an independent residual scale. That independence is part of the Gaussian calculation: the coefficient error and the residual vector are jointly normal with cross-covariance zero, and joint normality turns the zero cross-covariance into independence. With non-Gaussian or heteroscedastic errors, the same least-squares algebra still produces $\widehat\beta$ and $s^2$, while the exact $t_{n-p}$ reference is replaced by a large-sample normal approximation or by a covariance estimator matched to the error structure.{{cite:siegrist2022_normals}} (§6.8, “The T Variable”)

## Intuition — Cancel $\sigma$ between two independent pieces
The numerator $\widehat\beta_j-\beta_j$ has standard deviation $\sigma\sqrt{c_{jj}}$. Dividing by that standard deviation removes $\sigma$ and leaves a standard normal variable, but only when $\sigma$ is known. When $\sigma$ is unknown, the residual mean square estimates $\sigma^2$ from the directions orthogonal to the column space of $X$. The ratio of the normal numerator to the square root of an independent chi-squared variable, after the chi-squared variable is divided by its degrees of freedom, is Student's $t$ on $n-p$ degrees of freedom. The unknown scale appears in both the numerator's true standard deviation and the residual sum of squares, and it cancels in the ratio.

The degrees of freedom count those orthogonal directions. Each linearly independent column of $X$ spends one dimension of the response space on the fitted mean. With $n=8$ and three independent columns, five directions remain for $s^2$. The worked numerical example uses that count: $\mathrm{SSE}=20$ gives $s^2=20/5=4$ and $s\sqrt{c_{jj}}=1$ when $c_{jj}=1/4$.

## Key results — The same residual scale serves every fixed contrast
Let $c\in\mathbb R^p$ be a nonzero vector chosen without reference to $Y$. The contrast error $c^\top(\widehat\beta-\beta)$ is normal with variance $\sigma^2 c^\top C c$, and it is a linear image of the same Gaussian error vector that produces the residual. The cross-covariance with $(I-H)\varepsilon$ is still zero, so
$$
\frac{c^\top\widehat\beta-c^\top\beta}{s\sqrt{c^\top C c}}\sim t_{n-p}.
$$
A single coefficient is the case $c=e_j$, where $c^\top C c=c_{jj}$. For a numerical check, take $n=8$, $p=3$, $s=2$ and $c^\top C c=1/2$, and suppose the estimated contrast exceeds its target by $1.2$. The denominator is $2\sqrt{1/2}=\sqrt2=1.414214$, and the statistic is $1.2/1.414214=0.848528$ on $5$ degrees of freedom. The two-sided Student probability is $0.434875$. The residual degrees of freedom stay $n-p$ because every contrast in this model shares the same residual scale.{{cite:dodge2008}} (p. 493){{cite:siegrist2022_normals}} (§6.8, “The T Variable”)

If $\sigma$ is known, the denominator $\sigma\sqrt{c^\top C c}$ is a constant and the reference distribution is standard normal. In the worked example the estimated scale happened to equal $2$. Knowing that the true $\sigma$ equals $2$ would replace $t_5$ with $N(0,1)$ while leaving the numerical ratio unchanged. The change is in the reference distribution, which is a change in the probability attached to the same ratio.

## Statistical use — Invert one inequality
A two-sided level-$\alpha$ test accepts $\beta_j=\beta_{j0}$ when the absolute Student statistic is at most the $1-\alpha/2$ quantile of $t_{n-p}$. Rearrangement of that inequality is the interval
$$
\widehat\beta_j\pm t_{n-p;1-\alpha/2}\,s\sqrt{c_{jj}}.
$$
The worked summaries give the quantile $2.5706$ and the interval $[-1.0706,4.0706]$ for the coefficient whose estimate is $1.5$. The same rearrangement, with $c^\top C c$ in place of $c_{jj}$, gives an interval for a prechosen linear combination. A collection of intervals formed by applying the single-contrast quantile to many contrasts has a joint coverage below the nominal level of each piece, and a simultaneous region uses a larger critical value from the joint law.{{cite:dodge2008}} (pp. 492–493)

The design enters only through $C=(X^\top X)^{-1}$ and through the residual degrees of freedom. Rescaling the response by a positive constant rescales $\widehat\beta$, $s$ and the interval endpoints by that constant, and it leaves the Student statistic for a zero contrast unchanged. Rescaling a predictor column rescales the corresponding coefficient and its standard error in the opposite direction. The scientific contrast, expressed in the original units, keeps its statistic.

## Related concepts
The simple-regression slope pivot is the case $p=2$, with $c_{jj}=1/S_{xx}$ for the slope column after an intercept has been included. The one-sample Student statistic is the case $p=1$, $X$ a column of ones, and $c_{11}=1/n$. In both reductions the proof is the same orthogonal split of a Gaussian vector. Hotelling's $T^2$ extends the construction from one contrast to a vector of means with an estimated covariance; its null law is a scaled $F$, and the square of a $t_{n-p}$ variable is the $F_{1,n-p}$ law for a single contrast.{{cite:siegrist2022_normals}} (§6.8, “The Sample Variance” and “The T Variable”)

## Generalizations — What the Gaussian calculation supplies
Zero correlation between $\widehat\beta$ and the residual vector follows from $X^\top(I-H)=0$ as soon as the errors have covariance $\sigma^2 I$, Gaussian or otherwise. Independence of the coefficient estimator and $s^2$, the chi-squared law of $\mathrm{SSE}/\sigma^2$, and the exact Student reference are the additional conclusions from joint normality. A sandwich covariance estimates $c^\top A\Omega A^\top c$ when $\operatorname{Var}(\varepsilon)=\Omega$ is more complicated, and a normal reference for that estimated standard error is an asymptotic statement. The finite-sample pivot derived from that orthogonal split is the Gaussian equal-variance pivot.{{cite:siegrist2022_normals}} (§6.8, “The Sample Variance” and “The T Variable”)
