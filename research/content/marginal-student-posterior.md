## Motivating example
A regression coefficient has a normal conditional posterior when the residual variance is fixed. The variance itself is usually estimated from the same observations. Integrating over it creates a Student posterior with heavier tails. Those tails express uncertainty about scale; they do not imply that the measurement errors were assigned a Student sampling model. Conditional and marginal distributions are distinct objects.{{cite:bernardo2005_reference}} (Example 21)

The reference-prior calculation is especially transparent. A flat coefficient prior and a reciprocal-variance prior lead to the same residual degrees of freedom that appear in classical Gaussian regression. This agreement is model-specific and depends on treating the prior as a density in the stated coordinates.{{cite:bernardo2005_reference}} (Example 16 and Example 21)

## Statement
Assume $Y\mid\beta,v\sim N_n(X\beta,vI_n)$, where $X$ has full column rank $p<n$. Use prior density $\pi(\beta,v)\propto1/v$ with respect to $d\beta\,dv$. Write $C=(X^\top X)^{-1}$, $\widehat\beta=CX^\top y$, $Q=\lVert y-X\widehat\beta\rVert^2$, $\nu=n-p$ and $s^2=Q/\nu$. When $Q>0$, the posterior is proper and
$$\beta\mid v,y\sim N_p(\widehat\beta,vC),\qquad v\mid y\sim\operatorname{InvGamma}(\nu/2,Q/2).$$
Every fixed linear contrast $a^\top\beta$ with $a\ne0$ has a Student law with location $a^\top\widehat\beta$, scale $s\sqrt{a^\top Ca}$ and $\nu$ degrees of freedom. A Student scale is not its standard deviation when that standard deviation exists.{{cite:bernardo2005_reference}} (Examples 16, 21, normal reference posterior){{cite:dodge2008}} (p. 365, Gaussian regression matrix fit)

## Proof
The least-squares identity decomposes the residual square as $\lVert y-X\beta\rVert^2=Q+(\beta-\widehat\beta)^\top C^{-1}(\beta-\widehat\beta)$. Multiply the Gaussian likelihood by $1/v$. Conditional on $v$, the quadratic term normalizes to the displayed coefficient posterior. Integrating that quadratic normal kernel over $p$ coefficients contributes a factor proportional to $v^{p/2}$, leaving $v^{-\nu/2-1}e^{-Q/(2v)}$. This is the inverse-gamma marginal.{{cite:dodge2008}} (p. 365, normal equations and residual decomposition)

Conditional on $v$, a contrast $U=a^\top\beta$ is normal with variance $v c$, where $c=a^\top Ca>0$. Integrating its normal density against the inverse-gamma variance density produces a kernel proportional to $\{1+(U-a^\top\widehat\beta)^2/(\nu s^2c)\}^{-(\nu+1)/2}$. This is the Student density with the claimed scale and degrees of freedom. The same gamma integral explains the heavier tails of normal–gamma mixtures.{{cite:bernardo2005_reference}} (Example 21)

## Key results — Scale, variance and finite moments
For $\nu>2$, the marginal variance of the contrast is $\nu s^2c/(\nu-2)$. For $\nu>1$, its posterior mean equals its location. A proper Student posterior can have no finite mean when $\nu\le1$, and no finite variance when $\nu\le2$. The location and scale still define its density and quantiles. Reporting a location as a finite posterior mean without the moment condition would be incorrect.{{cite:bernardo2005_reference}} (Example 21)

The coefficient interval with central posterior probability $1-\alpha$ is $a^\top\widehat\beta\pm t_{1-\alpha/2,\nu}s\sqrt c$. It coincides numerically with the classical t interval under this Gaussian model and reference prior, though the probability interpretations condition on different objects.{{cite:bernardo2005_reference}} (Example 21, coverage in simple normal problems)

## Worked example — An intercept with three residual degrees of freedom
For observations $(1,2,4,5)$ and an intercept-only design, $n=4$, $p=1$, $\widehat\beta=3$ and $Q=10$. Thus $\nu=3$, $s^2=10/3$ and $C=1/4$. The marginal posterior is Student with location three, scale $\sqrt{5/6}=0.912871$ and three degrees of freedom. Its variance is $3(5/6)/(3-2)=2.5$. A central 95% interval is $(0.094837,5.905163)$, using the $t_3$ quantile rather than a normal quantile.{{cite:bernardo2005_reference}} (Examples 16, 21)

If the residual variance were fixed at $10/3$, the conditional normal posterior would instead have variance $5/6$. The marginal posterior integrates uncertainty in that variance and has a larger variance as well as heavier tails. With few residual degrees of freedom the difference is substantial.

**Your turn.** Keep the location and scale in the example but suppose the degrees of freedom were two. Would the posterior variance be finite?

::: {.callout-tip collapse="true" title="Answer"}
No. A Student law with two degrees of freedom is proper and has a finite mean, but its variance diverges.
:::

## Common misconceptions — A coefficient and a future response differ
A future response contains new observational noise as well as uncertainty about its conditional mean. Its predictive scale therefore includes an additional residual-noise contribution; the coefficient scale alone cannot be used as a response prediction scale. Similarly, a simultaneous region for several coefficients is different from collecting separate marginal intervals at the same nominal probability.{{cite:bernardo2005_reference}} (Example 23, normal prediction)

The conditions $n>p$ and $Q>0$ are substantive for this improper-prior analysis. Rank deficiency prevents the flat-prior coefficient integral from being finite, while an exact zero-residual fit makes the inverse-gamma scale degenerate. These cases require a different prior or a different model treatment.
