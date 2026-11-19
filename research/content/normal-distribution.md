## Lead context
Its two parameters locate the centre and set the spread. Standardising an observation turns a probability under any member of the family into a probability under the single standard-normal curve.{{cite:siegrist2022_normal_distribution}} (§5.6, “The General Normal Distribution”)

## Motivating example
A filling machine aims for 500 g per packet, with a 4 g standard deviation. If packet weights are independent draws from a normal model, a packet below 496 g is one standard deviation below the target: $P(X<496)=\Phi(-1)\approx0.1587$. This is a probability for a randomly selected packet under the model, not a guarantee about the fraction in a particular small batch. The model should be checked against the observed weights before using that probability for production decisions.{{cite:siegrist2022_normal_distribution}} (§5.6, “The General Normal Distribution”)

## Definition
Write $X\sim\operatorname N(\mu,\sigma^2)$, where $X$ is a random variable, $\mu$ is its mean, and $\sigma>0$ is its standard deviation. A realised value is written $x$. The density in the infobox determines probabilities by integration; its height at one value is not the probability of that value. Let $\phi$ and $\Phi$ be the standard-normal density and distribution function. Then $Z=(X-\mu)/\sigma\sim\operatorname N(0,1)$, $F_X(x)=\Phi((x-\mu)/\sigma)$, and the $u$-quantile is $\mu+\sigma\Phi^{-1}(u)$ for $0<u<1$.{{cite:siegrist2022_normal_distribution}} (§5.6, “The General Normal Distribution”)

The convention on this page is that the second argument of $\operatorname N$ is the **variance**. Thus $\operatorname N(100,16^2)$ has standard deviation $16$, while $\operatorname N(100,16)$ has standard deviation $4$. State which parameter is meant when a source writes $N(\mu,\sigma)$ without explaining its convention.{{cite:siegrist2022_normal_distribution}} (§5.6, “The General Normal Distribution”)

## Properties
The density is symmetric about $\mu$, and its mean, median, and mode all equal $\mu$. Its variance is $\sigma^2$, skewness is zero, and excess kurtosis is zero. The density changes curvature at $\mu-\sigma$ and $\mu+\sigma$; those locations are not cutoffs on its support, which is the whole real line.{{cite:siegrist2022_normal_distribution}} (§5.6, “The Standard Normal Distribution”; “The General Normal Distribution”)

For independent $X\sim\operatorname N(\mu_X,\sigma_X^2)$ and $Y\sim\operatorname N(\mu_Y,\sigma_Y^2)$, the sum is $X+Y\sim\operatorname N(\mu_X+\mu_Y,\sigma_X^2+\sigma_Y^2)$. Independence matters to this variance formula. The result explains why the sample mean of $n$ independent normal observations is itself exactly normal, with variance $\sigma^2/n$.{{cite:siegrist2022_normal_distribution}} (§5.6, “The General Normal Distribution”) {{cite:siegrist2022_normals}} (§6.08, “The One Sample Model”)

For one observation, the Fisher information matrix for the parameter pair $(\mu,\sigma)$ is $\operatorname{diag}(1/\sigma^2,2/\sigma^2)$. This is information about the mean and the **standard deviation**; changing the second parameter to $\sigma^2$ changes the matrix. Differential entropy is $\tfrac12\log(2\pi e\sigma^2)$, in natural-log units. Both formulas follow from the density and moments below.{{cite:siegrist2022_normal_distribution}} (§5.6, “The General Normal Distribution”)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Let $Z$ have density $\phi(z)=(2\pi)^{-1/2}e^{-z^2/2}$. Squaring its integral and changing to polar coordinates gives $(\int_{\mathbb R}e^{-z^2/2}\,dz)^2=2\pi$, so $\phi$ integrates to one. Symmetry gives $\mathbb E Z=0$. Since $\phi'(z)=-z\phi(z)$, integration by parts gives $\mathbb E Z^2=1$ and $\mathbb E Z^4=3$. Odd centred moments vanish. Hence $X=\mu+\sigma Z$ has mean $\mu$, variance $\sigma^2$, skewness zero, and kurtosis $3$, or excess kurtosis zero. The derivative of the normal density vanishes only at $\mu$, and its second derivative changes sign at $\mu\pm\sigma$, proving the stated mode and inflection points. Symmetry puts half the mass on either side of $\mu$, proving the median claim.{{cite:siegrist2022_normal_distribution}} (§5.6, “The Standard Normal Distribution”; “The General Normal Distribution”)

Completing the square in $\mathbb E e^{tZ}$ gives $e^{t^2/2}$. Therefore $M_X(t)=\mathbb E e^{tX}=e^{\mu t+\sigma^2t^2/2}$ and $\varphi_X(t)=M_X(it)=e^{i\mu t-\sigma^2t^2/2}$. Replacing $t$ by $at$ and multiplying by $e^{ibt}$ proves the affine rule for $aX+b$. Multiplying the MGFs of independent normals proves the stated sum law. Substituting $z=(x-\mu)/\sigma$ in the density integral gives the CDF and quantile formulas.{{cite:siegrist2022_normal_distribution}} (§5.6, “The General Normal Distribution”)

For entropy, $-\log p(X)=\tfrac12\log(2\pi\sigma^2)+Z^2/2$; taking expectations gives $\tfrac12\log(2\pi e\sigma^2)$. For information, the two score components are $S_\mu=Z/\sigma$ and $S_\sigma=(Z^2-1)/\sigma$. Their expected squares are $1/\sigma^2$ and $(3-2+1)/\sigma^2=2/\sigma^2$; their cross-product has expectation zero by symmetry. This proves the matrix displayed above.{{cite:siegrist2022_normal_distribution}} (§5.6, “The Standard Normal Distribution”; “The General Normal Distribution”)

For a normal sample, apply an orthogonal transformation to the vector of independent standardised observations. One coordinate is $\sqrt n(\overline X-\mu)/\sigma$; the other $n-1$ coordinates are residual contrasts. The transformed coordinates remain independent standard normals. Their residual sum of squares is $(n-1)s^2/\sigma^2$, proving its $\chi^2_{n-1}$ law and independence from $\overline X$.{{cite:siegrist2022_normals}} (§6.08, “The One Sample Model”)

For the binomial relationship, write a binomial count as the sum of independent Bernoulli indicators. Their mean and variance are $p$ and $p(1-p)$, so the central limit theorem gives convergence of $(B_n-np)/\sqrt{np(1-p)}$ to $\operatorname N(0,1)$ for fixed $0<p<1$ as $n$ grows. Shifting a discrete boundary by half a count is the continuity correction used for finite-sample tail calculations. For a multivariate normal vector, selecting one coordinate is a linear map; its marginal is therefore a one-dimensional normal law.{{cite:siegrist2022_binomial_distribution}} (§11.2, “The Normal Approximation”) {{cite:gelman_bda2013}} (Ch. 3, §3.5, pp. 70–72)

For the conjugate updates shown above, multiply a normal likelihood for a known variance by a normal prior for $\mu$, and collect the terms in $\mu^2$ and $\mu$. The posterior precision is $n/\sigma^2+1/\sigma_0^2$, and the linear coefficient is $n\overline x/\sigma^2+\mu_0/\sigma_0^2$; completing the square gives the printed mean and variance. With $\mu$ known instead, the likelihood as a function of $v=\sigma^2$ is proportional to $v^{-n/2}\exp[-S_\mu/(2v)]$. Multiplying it by an inverse-gamma density with shape $\alpha_0$ and scale $\beta_0$ adds $n/2$ to the shape and $S_\mu/2$ to the scale. The two full conditionals follow by holding the other parameter fixed in the same two calculations.{{cite:gelman_bda2013}} (Ch. 2, §§2.5–2.6, pp. 39–43) {{cite:raiffa_schlaifer1961}} (Ch. 3, §3.3.4; Ch. 11, §11.1.3)

For Box–Muller sampling, take independent uniforms $U,V$ and set $R=\sqrt{-2\log U}$, $\Theta=2\pi V$. The radius has density $r e^{-r^2/2}$ for $r>0$, independently of the uniform angle. The polar Jacobian is $r$, so $(R\cos\Theta,R\sin\Theta)$ has joint density $(2\pi)^{-1}e^{-(z_1^2+z_2^2)/2}=\phi(z_1)\phi(z_2)$: the two outputs are independent standard normals.{{cite:box_muller1958}} (pp. 610–611)
:::
:::

## Statistical inference
The phrase “normal data” means the observations themselves follow a normal law under the model. A central-limit approximation concerns a statistic such as an average, and can apply when the individual observations have another distribution. For exact small-sample $t$ and chi-squared calculations, the normal-sample assumptions behind the theorem above matter.{{cite:gelman_bda2013}} (Ch. 2, §2.5, pp. 39–41) {{cite:siegrist2022_normals}} (§6.08, “The One Sample Model”)

When a normal model is used for a measured response, inspect its scale, extreme observations, and dependence before treating a familiar interval formula as exact. In a normal-mean model with known variance, the sample mean is a natural likelihood summary; with unknown variance, the sample spread also enters the interval.{{cite:siegrist2022_normals}} (§6.08, “The One Sample Model”) {{cite:gelman_bda2013}} (Ch. 2, §2.5, pp. 39–41)

## Worked example
Suppose two independent measurements each follow $\operatorname N(50,10^2)$. What is the probability that their average exceeds 60? The sum rule gives $\overline X\sim\operatorname N(50,10^2/2)$, so its standard deviation is $10/\sqrt2$. Therefore

$$
P(\overline X>60)=1-\Phi\!\left(\frac{60-50}{10/\sqrt2}\right)=1-\Phi(\sqrt2)\approx0.07865.
$$


The probability is smaller than for one observation because averaging reduces the spread. Independence is required for the variance $10^2/2$.{{cite:siegrist2022_normals}} (§6.08, “The One Sample Model”)

::: {.callout-tip collapse="true" title="Your turn"}
If four independent measurements follow the same $\operatorname N(50,10^2)$ model, find $P(\overline X>60)$. What changes in the standard deviation?

**Answer.** The average has variance $10^2/4$ and standard deviation 5. Thus $P(\overline X>60)=1-\Phi(2)\approx0.02275$. Doubling the number of observations from two to four multiplies the average's standard deviation by $1/\sqrt2$.{{cite:siegrist2022_normals}} (§6.08, “The One Sample Model”)
:::
