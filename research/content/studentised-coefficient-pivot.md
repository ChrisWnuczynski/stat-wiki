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
The coefficient vector does not acquire a $t$ sampling law when $\sigma^2$ is unknown. Its conditional-on-parameter sampling law remains normal. Exact studentisation also needs independence of numerator and scale estimator; an arbitrary estimated standard error does not produce a Student law. With non-Gaussian or heteroscedastic errors, an asymptotic normal comparison or a separately justified robust procedure may be appropriate.{{cite:siegrist2022_normals}} (§6.8, “The T Variable”)
