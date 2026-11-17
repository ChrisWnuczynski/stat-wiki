## Motivating example

If four independent trials each succeed with probability $0.3$, the expected number of successes is easy to add, but the distribution of the total takes more work. A moment generating function packages the probability law into an exponential expectation. For independent variables these functions multiply, so the four-trial total follows from one trial by raising its function to the fourth power. Derivatives at zero then recover the total's moments.

## Intuition — Why exponential moments encode a distribution

The transform $e^{tX}$ gives more weight to large values when $t>0$ and to small values when $t<0$. Taking its expectation records how the distribution responds to that tilt. Near zero, the exponential's power series contains $1$, $X$, $X^2/2!$ and higher powers, which explains the name: derivatives of the transform reveal ordinary moments. This picture is valid only where the expectation exists. A random variable always has $M(0)=1$, but that single value says almost nothing about its law.

Independence is the other useful ingredient. Exponentiating a sum turns it into a product, $e^{t(X+Y)}=e^{tX}e^{tY}$. Only for independent $X,Y$ can the expectation be split into $M_X(t)M_Y(t)$. A product of transforms can therefore identify a sum distribution when a known family's transform has the same form. This often avoids a convolution integral.

## Definition

For a real random variable $X$, its moment generating function is $M_X(t)=\mathbb E(e^{tX})$ on the set of real $t$ for which that expectation is finite. A useful existence condition is finiteness throughout some open interval containing zero. Under that condition $M_X^{(k)}(0)=\mathbb E(X^k)$ for each nonnegative integer $k$, and the function determines the probability law. If the function is finite only at zero, the usual derivative and uniqueness arguments cannot be invoked from it.

The domain is part of the answer. An exponential variable of rate $\lambda$ has $M(t)=\lambda/(\lambda-t)$ only for $t<\lambda$; the algebraic expression beyond that range does not equal a finite expectation. A probability generating function instead uses powers $z^N$ for nonnegative integer-valued $N$, and a characteristic function uses $e^{itX}$ and exists for every real $t$. They answer related but distinct questions.

## Properties

Differentiation under the expectation near zero yields $M'_X(0)=\mathbb E X$ and $M''_X(0)=\mathbb E X^2$. Thus $\operatorname{Var}(X)=M''_X(0)-M'_X(0)^2$. More generally, the logarithm $K_X(t)=\log M_X(t)$ has $K'_X(0)=\mathbb E X$ and $K''_X(0)=\operatorname{Var}(X)$. The logarithm changes the product rule for independent sums into addition, which is why cumulants add across independent components.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
If $M_X$ is finite on an interval around zero, choose $a>0$ with $\mathbb E(e^{aX})$ and $\mathbb E(e^{-aX})$ finite. For $|t|$ sufficiently smaller than $a$, the derivatives $X^k e^{tX}$ are bounded in absolute value by a constant times $e^{aX}+e^{-aX}$. Dominated differentiation therefore gives $M_X^{(k)}(t)=\mathbb E(X^k e^{tX})$ and the moment formula at zero. For independent $X,Y$, $\mathbb E[e^{t(X+Y)}]=\mathbb E[e^{tX}]\mathbb E[e^{tY}]$.{{cite:siegrist2022_chisq}} (§5.9, density, distribution functions, moments and relations) Differentiating $K=\log M$ gives $K'=M'/M$ and $K''=M''/M-(M'/M)^2$; because $M(0)=1$, these give the mean and variance identities. The assertion that a transform on a neighbourhood determines the law uses the separate uniqueness theorem for Laplace transforms; it does not follow merely from equality of a few derivatives.
:::
:::

## Interpretation

For Bernoulli $X$ with success probability $p$, $M_X(t)=1-p+pe^t$. For independent Bernoulli variables with the same $p$, multiplying their transforms gives $(1-p+pe^t)^n$, the binomial transform. For independent Poisson variables, the same operation adds their rates; for independent Gamma variables it adds their shapes only when their rate parameter is common. The matching of transforms is what identifies these sum laws, not mere addition of their means.

A transform may fail to exist where its moments all exist. If $Z$ is standard normal and $X=e^Z$ is lognormal, $\mathbb E X^k=e^{k^2/2}$ is finite for every positive integer $k$, yet $\mathbb E(e^{tX})=\infty$ for every $t>0$. The exponential of $e^Z$ eventually overwhelms the normal density's quadratic tail. Thus a formal power series of moments need not define an MGF around zero.

## Statistical use

Use an MGF to derive moments, identify sums of independent components, or check a proposed distributional calculation. State the range of $t$ and the independence assumptions. The function is particularly convenient for normal, Poisson and Gamma families because their parameters appear in simple exponent or power forms. For heavy-tailed laws with no MGF near zero, use the characteristic function or direct probability calculations instead.

A Cauchy variable has no finite first absolute moment and no MGF for nonzero $t$, so differentiation at zero cannot supply a mean. A lognormal variable has all positive integer moments but no MGF at positive $t$, defeating the neighbourhood condition in a subtler way. If two Bernoulli trials are perfectly dependent rather than independent, their sum is either zero or two; multiplying their individual MGFs falsely assigns positive probability to one success. These examples expose moment existence, transform existence and independence as separate requirements.
## Worked example

Let $X_1,\ldots,X_4$ be independent Bernoulli variables with success probability $0.3$, and let $S=\sum_iX_i$. One trial has $M_X(t)=0.7+0.3e^t$, so $M_S(t)=(0.7+0.3e^t)^4$. Differentiating at zero, or using additivity, gives $\mathbb E S=4(0.3)=1.2$ and $\operatorname{Var}(S)=4(0.3)(0.7)=0.84$. The probability of no successes is $0.7^4=0.2401$. The transform identifies the whole binomial law, while the first two derivatives summarize only its centre and spread.

**Your turn.** If $N$ is Poisson with rate $2$, write its MGF, find its mean and variance from derivatives, and evaluate $M_N(\log2)$. Explain why the last value is not a probability.

::: {.callout-tip collapse="true" title="Answer"}
The MGF is $M_N(t)=\exp\{2(e^t-1)\}$. Its first derivative at zero is $2$, and the second derivative is $6$, so its variance is $6-2^2=2$. At $t=\log2$, $M_N(t)=e^2\approx7.3891$. This is the expectation of $2^N$, which can exceed one; it is not the probability of an event.
:::

## Common misconceptions

The existence of all moments does not guarantee an MGF on a neighbourhood of zero, as the lognormal example shows. Writing down a rational expression beyond the transform's domain does not extend the expectation there. A transform for a sum is a product of individual transforms only under independence. Finally, equality of the first two derivatives says only that two distributions share a mean and variance; it does not identify their entire laws.

## Connections

The [probability generating function](probability-generating-function.qmd) is tailored to nonnegative integer counts. A [characteristic function](characteristic-functions.qmd) always exists and is useful when an MGF does not. [Expectation](expectation.qmd) and [variance](variance.qmd) arise from the first two derivatives, while [convolution](convolution.qmd) is the direct alternative for sums. The statistical term *moment* comes from a mechanical analogy with moments of forces.{{cite:dodge2008}} (p. 358, “Moment”)

## History

The language of moments predates the exponential transform: it is tied to the mechanical moment of a force, and later formulas corrected moments computed from grouped data.{{cite:dodge2008}} (p. 358, “Moment”) The MGF organizes those moments through derivatives of one function, a development aligned with the wider use of generating functions in probability.
