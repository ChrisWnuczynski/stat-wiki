## Motivating example
When measurements are noisy, the population centre is harder to estimate. A normal–inverse-Gamma prior builds that relationship into a joint model: the conditional prior variance of the centre is proportional to the unknown observation variance. The resulting prior is dependent, even though it is specified by two familiar distributions. Its attraction is that combining it with a normal likelihood preserves the joint family and permits direct posterior calculations.{{cite:prado_ferreira_west2021}} (§1.5.3.2, p. 24, eq. 1.23)

## Interpretation — State the inverse-Gamma convention first
Write $v=\sigma^2$ and use $p(v)=\beta_0^{\alpha_0}v^{-\alpha_0-1}e^{-\beta_0/v}/\Gamma(\alpha_0)$ for $v>0$. Given $v$, take $\mu\mid v\sim N(\mu_0,v/\kappa_0)$, with $\alpha_0,\beta_0,\kappa_0>0$. The joint density has power $v^{-\alpha_0-3/2}$ because the conditional normal contributes another factor $v^{-1/2}$. This extra factor distinguishes a conditional prior from an independent normal prior with a fixed variance. The sampling model remains the ordinary normal density with positive variance.{{cite:dodge2008}} (p. 378, Normal Distribution)

The parameter $\kappa_0$ controls the precision of the prior centre relative to one observation at the same $v$. It can be interpreted as an equivalent sample size for the mean update. The inverse-Gamma parameters separately control uncertainty in the observation variance. Making $\kappa_0$ small does not by itself specify a noninformative prior on the whole pair, because the variance prior and the dependence structure still matter.{{cite:prado_ferreira_west2021}} (§1.5.3.2, p. 24)

## Properties — Complete both squares before integrating
For iid observations, put $\bar x=n^{-1}\sum_i x_i$ and $S=\sum_i(x_i-\bar x)^2$. The quadratic identity
$$S+n(\mu-\bar x)^2+\kappa_0(\mu-\mu_0)^2=S+\kappa_n(\mu-\mu_n)^2+\frac{\kappa_0n}{\kappa_n}(\bar x-\mu_0)^2$$
uses $\kappa_n=\kappa_0+n$ and $\mu_n=(\kappa_0\mu_0+n\bar x)/\kappa_n$. It gives $\alpha_n=\alpha_0+n/2$ and
$$\beta_n=\beta_0+S/2+\frac{\kappa_0n}{2\kappa_n}(\bar x-\mu_0)^2.$$
The joint posterior factors as $v\mid x\sim\operatorname{InvGamma}(\alpha_n,\beta_n)$ and $\mu\mid v,x\sim N(\mu_n,v/\kappa_n)$. The disagreement term between prior and sample centres is nonnegative; omitting it would suppress variance uncertainty when those centres differ.{{cite:prado_ferreira_west2021}} (§1.5.3.2, p. 24, conjugate Gaussian update)

To verify the marginal shape, integrate the joint kernel over $\mu$. Its Gaussian integral contributes $\sqrt{2\pi v/\kappa_n}$ and cancels the conditional-normal factor $v^{-1/2}$. The marginal inverse-Gamma shape is therefore $\alpha_n$, while the full conditional $v\mid\mu,x$ has shape $\alpha_n+1/2$ and scale $\beta_n+\kappa_n(\mu-\mu_n)^2/2$. Marginalisation and conditioning are different operations on the same joint posterior.

## Worked example — Prior disagreement adds variance uncertainty
Take prior parameters $(\mu_0,\kappa_0,\alpha_0,\beta_0)=(0,2,3,4)$ and observations $1,2,3$. Then $n=3$, $\bar x=2$ and $S=2$. The posterior parameters are $\kappa_n=5$, $\mu_n=6/5$, $\alpha_n=9/2$ and $\beta_n=37/5$. The scale combines prior scale four, within-sample contribution one and disagreement contribution $12/5$.

The posterior mean variance is $\mathbb E(v\mid x)=\beta_n/(\alpha_n-1)=74/35$. The marginal posterior of $\mu$ is Student with nine degrees of freedom, location $6/5$ and squared scale $\beta_n/(\alpha_n\kappa_n)=74/225$. Its variance is $74/175$, which exceeds its squared scale. The posterior predictive distribution adds a new observation's noise to the uncertainty in the centre, giving the same nine degrees of freedom and squared scale $148/75$.{{cite:prado_ferreira_west2021}} (§1.5.3.2, p. 24, marginal Student distributions)

**Your turn.** If the prior centre were changed to the sample mean two with the other prior parameters fixed, what would happen to $\beta_n$?

::: {.callout-tip collapse="true" title="Answer"}
The disagreement term would be zero. The posterior scale would be $4+2/2=5$, rather than $37/5$. The conditional posterior centre would also equal two.
:::

## Assumptions and limits — A scale need not be a variance
A Student distribution's scale parameter is not its standard deviation. For the marginal centre distribution, variance exists only if $\alpha_n>1$ and equals $\beta_n/[\kappa_n(\alpha_n-1)]$. Its mean exists when $\alpha_n>1/2$; otherwise the symmetry centre remains meaningful without a finite first moment. Likewise the inverse-Gamma posterior mean of $v$ needs $\alpha_n>1$. A Student density with $\nu$ degrees of freedom has tails proportional to $|u|^{-\nu-1}$, so its absolute moment of order $r$ is finite precisely when $r<\nu$. Integrating the inverse-Gamma tail $v^{-\alpha_n-1}$ similarly gives its positive-moment condition. These are integrability conditions, not software conventions.{{cite:prado_ferreira_west2021}} (§1.5.3.2, p. 24, inverse-Gamma and Student posterior families)

The iid model also uses a common variance and a shared mean. Correlation, changing means, censoring or a likelihood for transformed measurements require a different likelihood. Proper positive hyperparameters ensure a proper prior in the stated family; an improper limiting prior needs an independent posterior-propriety analysis. A small numerical hyperparameter is still a proper prior parameter and cannot be identified with an improper limit without checking that limiting operation.

## Statistical use — State which functional of the posterior is being reported

After the variance has been integrated, the marginal posterior of the centre is Student. A prediction for a new observation from the same normal sampling model has the same degrees of freedom and a larger scale, because the new draw adds a fresh noise term to the uncertainty already present in the centre. Quoting the marginal variance of the centre as if it were the variance of a new measurement leaves that noise out. The inverse-gamma posterior mean of the variance exists only when the updated shape exceeds one. Below that threshold the scale remains well defined and the mean does not. A Student variance exists only when the degrees of freedom exceed two, and it equals those degrees of freedom divided by their excess over two, times the squared scale. The symmetry centre of the Student law remains meaningful when the variance does not exist. These are different functionals of one joint posterior. [Inverse-gamma distribution](inverse-gamma-distribution.qmd) is the law used for the variance. [Marginal Student posterior](marginal-student-posterior.qmd) is the law of the centre after the variance is integrated. [Normal–inverse-gamma variance update](normal-inverse-gamma-variance-update.qmd) isolates the scale recursion.{{cite:prado_ferreira_west2021}} (§1.5.3.2, p. 24, marginal Student distributions){{cite:prado_ferreira_west2021}} (§1.5.3.2, p. 24, inverse-Gamma and Student posterior families)
