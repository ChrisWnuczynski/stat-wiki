## Motivating example
A patient's continuous severity measurement and binary survival outcome are different responses recorded on the same person. Each response needs a suitable mean model, but their errors can be associated. Treating them as two independent people would misrepresent the unit that supplied the information. Marginal estimating equations allow dependence within a unit while using independence across units to estimate uncertainty.{{cite:liang_zeger1986}} (§§1–3, pp. 13–16)

## Definition — A vector observation with distinct margins
For independent units $i$, write $Y_i=(Y_{i1},Y_{i2})^\top$. A continuous margin might use an identity link and a binary margin a logit link. The coefficient vectors and variance functions can differ. A working covariance describes how the two components are weighted together in an estimating equation. Correct specification of the marginal means is a separate requirement from a convenient choice of working correlation.{{cite:liang_zeger1986}} (§3.1, pp. 15–16)

## Properties — Covariance enters even a simple contrast
If $A$ and $B$ are random measurements, then
$$\operatorname{Var}(A-B)=\operatorname{Var}(A)+\operatorname{Var}(B)-2\operatorname{Cov}(A,B).$$
For independent people observed once on each margin, the covariance of their sample means is the within-person covariance divided by the number of people. Thus increasing the number of components measured on a fixed person does not provide independent replication of their covariance. Linear variance propagation keeps the cross term explicit.{{cite:nist_error_propagation2002}} (§3.1.3.3)

In a sandwich covariance, the middle matrix is formed from each person's complete estimating-function contribution. Its cross-products preserve empirical association between the two responses. Replacing those cross-products by zeros changes the covariance estimate. Robust covariance estimation allows a working association to differ from the true association under regularity and independent-unit assumptions; it does not correct a wrong marginal mean or arbitrary missing-data mechanisms.{{cite:liang_zeger1986}} (§2, Theorem 1 and §3.1, Theorem 2, pp. 15–16)

## Interpretation — Joint uncertainty requires cross-covariance
Two marginal confidence intervals do not specify a joint confidence region. The covariance between estimated slopes determines the rotation and shape of an ellipse. Marginal standard errors alone give its axis scales only when a zero cross-covariance is additionally imposed. A diagram drawn under that assumption is a schematic comparison of region geometry, rather than an estimate of an unreported cross-covariance.{{cite:nist_error_propagation2002}} (§3.1.3.3); {{cite:liang_zeger1986}} (§3.1, covariance of the estimator)

## Worked example — A shared observation changes a standard error
Suppose two component measurements have variances four and nine and covariance three, with one hundred independent people. The variance of their mean difference is $(4+9-2\times3)/100=0.07$, so its standard error is $\sqrt{0.07}\approx0.264575$. Ignoring covariance gives variance $0.13$ and standard error $0.360555$. Positive covariance reduces uncertainty in a difference; it increases uncertainty in a sum.

For the illustrative burn slopes, the arithmetic ratios are $0.0035/0.0017\approx2.058824$ and $0.0508/0.0051\approx9.960784$. Those are marginal standardised slope comparisons. Under a joint normal approximation and zero slope cross-covariance, the 95% ellipse has squared standardised radius $\chi^2_{2;0.95}=-2\log(0.05)\approx5.991465$. Its axis multiplier $2.447747$ exceeds the marginal 95% multiplier $1.959964$, whereas a rectangle corner has squared radius $2(1.959964)^2\approx7.682918$ and lies outside the ellipse. These calculations explain the different boundaries in the figure. They do not determine the covariance between the two estimated slopes, which is needed for a joint comparison.

**Your turn.** Keep the two component variances but change their covariance from three to minus three. What is the variance of the mean difference for one hundred independent people?

::: {.callout-tip collapse="true" title="Answer"}
It is $(4+9-2(-3))/100=0.19$. The standard error is $\sqrt{0.19}\approx0.435890$.
:::

## Assumptions and limits — Marginal distributions constrain association
A declared pair of variances and covariance must form a positive semidefinite matrix. Discrete margins impose further restrictions. For Bernoulli means $0.2$ and $0.8$, the joint success probability lies between zero and $0.2$. Their covariance lies between $-0.16$ and $0.04$, so correlation lies between minus one and $0.25$. Correlation one is impossible for these margins. A convenient working correlation can weight an estimating equation without defining a fully specified joint probability model, but its use does not establish that every nominal correlation is attainable by those margins.{{cite:liang_zeger1986}} (§3.1, working correlation); {{cite:nist_error_propagation2002}} (§3.1.3.3, covariance terms)
