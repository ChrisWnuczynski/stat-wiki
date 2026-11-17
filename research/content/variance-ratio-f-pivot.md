## Motivating example
Two measurement devices can have similar average readings but different precision. A confidence interval for the ratio of their population variances quantifies this comparison. Under independent normal sampling, division by the unknown variance ratio produces an exact distribution that does not depend on either mean or scale.{{cite:siegrist2022_normals}} (§ “Ratios of Sample Variances”) The $F$ law is also called the Fisher distribution.{{cite:dodge2008}} (p. 199, Fisher Distribution)

## Key results — Why both degrees of freedom lose one
For independent normal samples of sizes $n_1,n_2\ge2$, let $S_i^2$ use denominator $n_i-1$ and let $\rho=\sigma_1^2/\sigma_2^2>0$. Then
$$
Q=\frac{S_1^2/S_2^2}{\rho}\sim F_{n_1-1,n_2-1}.
$$
An $F$ variable is the ratio of independent chi-square variables after dividing each by its degrees of freedom. The denominator degrees of freedom determine its mean, which exceeds one when that mean is finite. A pivot need not have expectation one.{{cite:siegrist2022_normals}} (§ “Ratios of Sample Variances”)

## Proof
Standardise one normal sample to independent $Z_j\sim N(0,1)$. Choose an orthogonal coordinate system whose first direction is $\mathbf1/\sqrt n$. Rotational invariance of the joint standard normal density gives independent standard normal coordinates in this basis.{{cite:rasmussen_williams2006}} (§A.2, pp. 200–201) The first coordinate is $\sqrt n\overline Z$; the sum of squares of the other $n-1$ coordinates is $\sum_j(Z_j-\overline Z)^2$. Hence $(n-1)S^2/\sigma^2$ is chi-square with $n-1$ degrees of freedom and independent of the sample mean. Applying this construction separately to the two independent samples gives independent chi-square residual sums. Their scaled ratio is precisely $Q$, proving its $F$ law.{{cite:siegrist2022_normals}} (§ “The One-Sample Model”, The Sample Mean and Variance; § “Ratios of Sample Variances”)

## Generalizations — Invert the pivot for an interval
Write $r=S_1^2/S_2^2$ and let $q_u$ be the lower-tail $u$ quantile of $F_{n_1-1,n_2-1}$. The event $q_{\alpha/2}\le r/\rho\le q_{1-\alpha/2}$ is equivalent to
$$
\frac{r}{q_{1-\alpha/2}}\le\rho\le\frac{r}{q_{\alpha/2}}.
$$
The quantiles change sides when solving for $\rho$, since all quantities are positive. The coverage is exact under the stated sampling model. Nonnormal sampling generally changes the distribution of the residual sums and invalidates this exact calibration.{{cite:siegrist2022_normals}} (§ “Ratios of Sample Variances”)

## Worked example
With nine observations per device and observed variance ratio four, the pivot has eight degrees of freedom in both positions. Its $0.025$ and $0.975$ quantiles are $0.225568$ and $4.433260$. A $95\%$ interval for the population variance ratio is therefore $(0.902271,17.733040)$. The point estimate four is compatible with equality at this level, and the wide interval shows the limited precision of small samples.

For equal numerator and denominator degrees of freedom, the reciprocal has the same distribution. Continuity then places the median at one, although the mean for eight denominator degrees of freedom is $8/6=4/3$. This distinction explains why a ratio centred multiplicatively at one can have an arithmetic mean above one.{{cite:siegrist2022_normals}} (§ “Ratios of Sample Variances”)

**Your turn.** Reverse the devices in the example. What happens to the interval and degrees of freedom?

::: {.callout-tip collapse="true" title="Answer"}
The sample ratio becomes $1/4$ and the interval becomes $(1/17.733040,1/0.902271)$, approximately $(0.056392,1.108315)$. The degrees of freedom remain $(8,8)$; with unequal sample sizes their order would swap.
:::
