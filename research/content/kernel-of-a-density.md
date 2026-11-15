## Lead context
The kernel keeps the terms that determine a distribution's shape while setting aside the factor that makes its total probability one. In Bayesian calculations, this lets an analyst multiply likelihood and prior, recognise a familiar posterior family, and restore the factor only when needed. Which factors may be omitted depends on the variable whose distribution is being described.{{cite:gelman_bda2013}}

## Motivating example
Imagine a coin with unknown success probability. After observing successes and failures, the posterior density for that probability contains powers of the probability and of its complement. The binomial coefficient counts possible sequences but does not vary with the unknown probability, so it can be omitted while identifying the posterior family. The remaining powers have the form of a Beta density's kernel.{{cite:gelman_bda2013}}

## Intuition
Multiplying a nonnegative curve by one positive number changes its height everywhere but leaves its relative heights, modes, and shape unchanged. That curve is a kernel. The omitted number is *not* always a universal constant: it may depend on parameters held fixed for the current calculation. For example, the normalising factor of a normal density depends on its standard deviation; it is constant when comparing values of the observation at a fixed standard deviation but cannot be discarded when estimating that standard deviation from the data.{{cite:gelman_bda2013}}

## Definition
For a density $f(x\mid\eta)$ of a continuous random variable $X$ at realised value $x$, with fixed parameter $\eta$ and support $\mathcal S$, a nonnegative function $g(x;\eta)$ is a kernel in $x$ if

$$
f(x\mid\eta)=c(\eta)g(x;\eta),\qquad
c(\eta)=\left[\int_{\mathcal S}g(u;\eta)\,du\right]^{-1}.
$$

Here $u$ is an integration variable and $c(\eta)$ is positive and independent of $x$. The integral must be finite and nonzero. We write $f(x\mid\eta)\propto_x g(x;\eta)$ to make explicit that proportionality concerns $x$ with $\eta$ held fixed; ordinary $\propto$ is common when the variable is clear. A discrete mass function uses a sum over its support in place of the integral. Multiplying $g$ by any positive factor independent of $x$ gives another kernel of the same density.{{cite:gelman_bda2013}}

For Bayesian inference, let $\Theta$ be a random parameter with realised value $\theta$, and let $Y=y$ denote the observed data. The posterior kernel is in $\theta$: $p(\theta\mid y)\propto_{\theta}p(y\mid\theta)p(\theta)$. The evidence $p(y)=\int p(y\mid u)p(u)\,du$ is constant in $\theta$ for fixed data $y$, provided it is finite and positive. A term that depends on $\theta$ must remain even if it does not depend on $y$. This is the variable-specific rule behind the original proportionality statement above.{{cite:bayes1763,gelman_bda2013}}

In the original variance-likelihood expression, $\sigma^2>0$ is the unknown variance, $n$ is the number of independent normal observations, $\mu$ is a known mean, and $S_\mu=\sum_{i=1}^n(y_i-\mu)^2$ is the sum of squared departures of the realised observations $y_i$ from that mean. Both displayed pieces depend on $\sigma^2$, so both remain in the likelihood kernel for $\sigma^2$. Constants in $\sigma^2$, such as powers of $2\pi$, may be dropped.{{cite:gelman_bda2013}}

## Properties
If $f(x)=c g(x)$ with $c>0$, every ratio $f(x_1)/f(x_2)$ equals $g(x_1)/g(x_2)$ where the denominator is positive. The same $x$ values maximise both functions over their common support. This is why a kernel suffices for comparing relative density values or locating a mode, though it cannot by itself give an absolute probability.{{cite:gelman_bda2013}}

A nonnegative kernel becomes a proper density only if its integral or sum over the whole support is finite and positive. If that total is infinite, no finite normalising constant exists. A posterior kernel may be proper even when a formal prior kernel is improper, but that conclusion requires checking the *posterior* integral rather than recognising a familiar-looking algebraic expression.{{cite:gelman_bda2013}}

For a Beta prior $\Theta\sim\operatorname{Beta}(a,b)$ and $s$ successes and $r$ failures from independent Bernoulli trials, the posterior kernel is $\theta^{a+s-1}(1-\theta)^{b+r-1}$ on $0<\theta<1$, so the posterior is $\operatorname{Beta}(a+s,b+r)$. Here $a,b>0$ are prior shape parameters, and $s,r$ are observed nonnegative counts. The matching shape identifies the family; the Beta function supplies the normalising constant.{{cite:gelman_bda2013}}

The variance likelihood above similarly matches an inverse-Gamma prior when that prior is parameterised by shape $\alpha>0$ and scale $\beta>0$ with kernel $(\sigma^2)^{-\alpha-1}\exp[-\beta/\sigma^2]$. The posterior kernel then has shape $\alpha+n/2$ and scale $\beta+S_\mu/2$. This relationship requires a *known* $\mu$ and the stated inverse-Gamma convention; changing either condition changes the calculation.{{cite:gelman_bda2013}}

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Because $f=cg$ integrates to one and $c$ does not vary with $x$, $1=\int_{\mathcal S}f(x)\,dx=c\int_{\mathcal S}g(x)\,dx$, giving the stated reciprocal normaliser whenever the integral is finite and positive. A positive common factor cancels from $f(x_1)/f(x_2)$ and preserves order, so it also preserves all maximisers. If the integral is infinite, no positive finite $c$ can make it one.{{cite:gelman_bda2013}}

For the Beta update, the likelihood in $\theta$ is proportional to $\theta^s(1-\theta)^r$ and the prior density is proportional to $\theta^{a-1}(1-\theta)^{b-1}$ on the same support. Multiplication adds the exponents, giving the stated kernel. Its integral is the finite Beta function $B(a+s,b+r)$ for $a+s,b+r>0$, so division by that number gives the claimed Beta posterior. For the variance update, multiply $(\sigma^2)^{-n/2}\exp[-S_\mu/(2\sigma^2)]$ by $(\sigma^2)^{-\alpha-1}\exp[-\beta/\sigma^2]$. Combining powers and exponents gives $(\sigma^2)^{-(\alpha+n/2)-1}\exp[-(\beta+S_\mu/2)/\sigma^2]$, the inverse-Gamma kernel under the stated parametrisation. These calculations prove the two family relationships without dropping any term that depends on the posterior variable.{{cite:gelman_bda2013}}
:::
:::

## Statistical use
Kernel algebra is useful when a likelihood-prior product belongs to a known family: the name of that family supplies its normaliser, moments, and simulation methods. When no named family matches, numerical integration or simulation can work with the unnormalised posterior. Ratios of posterior kernel values, for example, cancel the unknown common normaliser, which is useful in Metropolis–Hastings acceptance calculations. A full posterior probability or marginal likelihood still requires the appropriate integral; proportionality alone does not provide it.{{cite:gelman_bda2013}}

## Worked example
Start with a $\operatorname{Beta}(2,3)$ prior for a coin's success probability $\Theta$. Observe seven successes and three failures. The prior kernel is $\theta(1-\theta)^2$, and the likelihood kernel in $\theta$ is $\theta^7(1-\theta)^3$. Their product is $\theta^8(1-\theta)^5$, the kernel of $\operatorname{Beta}(9,6)$. Its posterior mean is $9/(9+6)=0.6$. The binomial coefficient ${10\choose7}$ changes neither posterior shape nor posterior mean because the data count is fixed in this calculation.{{cite:gelman_bda2013}}

For the other family above, suppose $\mu$ is known, $n=8$, $S_\mu=20$, and the prior for $\sigma^2$ is inverse-Gamma with shape $3$ and scale $2$. The posterior has shape $3+8/2=7$ and scale $2+20/2=12$ under the same parametrisation. The two examples illustrate the same exponent-matching method on different supports.{{cite:gelman_bda2013}}

**Your turn.** With the same $\operatorname{Beta}(2,3)$ prior, suppose the next dataset has two successes and one failure. Find the posterior family and its mean. Would you omit the factor $\theta^2$ from the likelihood when $\theta$ is the variable of interest?

::: {.callout-tip collapse="true" title="Answer"}
Multiplication gives $\theta^{2+2-1}(1-\theta)^{3+1-1}=\theta^3(1-\theta)^3$, so the posterior is $\operatorname{Beta}(4,4)$ and has mean $4/(4+4)=1/2$. The factor $\theta^2$ depends on $\theta$ and must stay.
:::

## Common misconceptions
A kernel is not automatically a probability density: without its normalising constant it need not integrate to one. Nor is a kernel unique, because any positive factor independent of the chosen variable can be moved between kernel and normaliser. The word *kernel* also has other meanings. A [kernel density estimator](kernel-density-estimator.qmd) smooths observations with a chosen bump function, and a [positive-definite kernel](kernel.qmd) measures similarity of pairs of inputs; neither is the omitted-constant meaning used here.{{cite:gelman_bda2013}}

## Assumptions and limits
Always state the support and the variable of proportionality. Dropping the indicator $0<\theta<1$ from the Beta example would falsely extend its kernel outside the allowed probabilities. Dropping the normal density's $1/\sigma$ factor while *estimating* $\sigma$ would change the likelihood, even though that factor can be ignored when comparing $x$ values at fixed $\sigma$. An improper integral cannot be repaired by assigning it a guessed constant.{{cite:gelman_bda2013}}

## Connections
The [likelihood function](likelihood-function.qmd) treats observed data as fixed and varies the parameter, so its kernel retains every parameter-dependent factor. The [Beta distribution](beta-distribution.qmd) provides the normaliser for the coin example; the [inverse-Gamma distribution](inverse-gamma-distribution.qmd) supplies one for the known-mean normal variance example. [Beta–Binomial conjugacy](beta-binomial-conjugacy.qmd) means the posterior kernel stays within the Beta family. These are specific algebraic relationships, not merely shared terminology.{{cite:gelman_bda2013}}

## Check yourself
Work through [reading conjugacy from a kernel](../questions/exr-reading-conjugacy-from-a-kernel.qmd), then [the Gamma and inverse-Gamma kernels](../questions/c-10.qmd). In each exercise, identify the variable of interest before crossing out any factor.

## History
Bayes's essay, communicated by Richard Price in 1763, asked how observations of successes and failures inform an unknown chance of success. Price's introduction describes the problem as inference about the chance from the observed event counts. The modern Beta–Binomial kernel calculation above addresses that same type of inverse problem, although the essay did not introduce today's kernel notation.{{cite:bayes1763}}

Modern Bayesian analysis routinely expresses a posterior as a likelihood times a prior divided by a normalising integral. When the product has a familiar form, the kernel makes the distribution recognisable before its constant is calculated. That computational role appears in current statistical treatments and in the older conjugate-analysis discussion already cited in this article; no particular person or date is asserted as the origin of the word *kernel*.{{cite:gelman_bda2013,raiffa_schlaifer1961}}
