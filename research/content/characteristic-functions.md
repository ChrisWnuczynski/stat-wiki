## Lead context
Complex exponentials turn sums of independent random variables into products without requiring exponential moments to exist.

## Motivating example
A sum of several noise contributions can be difficult to analyse by repeated convolution. A transform can simplify the sum, but a moment generating function may be infinite. The characteristic function uses an oscillating quantity of modulus one, so it is available even for heavy-tailed laws with no mean.{{cite:durrett2019}} (§3.3.1, definition and examples)

## Definition — A bounded complex transform
For real $t$, define
$$
\varphi_X(t)=\mathbb E(e^{itX})=\mathbb E\cos(tX)+i\mathbb E\sin(tX).
$$
The expectation always exists because $|e^{itX}|=1$. In particular, $\varphi_X(0)=1$, $|\varphi_X(t)|\le1$ and $\varphi_X(-t)=\overline{\varphi_X(t)}$. Continuity follows from dominated convergence. The real and imaginary parts record cosine and sine averages rather than probabilities at the frequency value.{{cite:durrett2019}} (§3.3.1, elementary properties)

[]{#property-cf-uniqueness}

For a density $f$, the transform is $\int e^{itx}f(x)\,dx$; for a discrete law it is the corresponding probability-weighted sum. Fourier inversion explains why the transform determines the distribution. An inversion formula needs its own endpoint and integrability conditions; the existence of a characteristic function requires neither a density nor those extra conditions.{{cite:durrett2019}} (§3.3.1, Thm. 3.3.11){{cite:grinstead_snell1997}} (§10.3, characteristic functions and inversion)

## Properties — Independence, scaling and moments
For constants $a,b$,
$$
\varphi_{aX+b}(t)=e^{itb}\varphi_X(at).
$$
If $X$ and $Y$ are independent, factorisation of the expectation gives
$$
\varphi_{X+Y}(t)=\varphi_X(t)\varphi_Y(t).
$$
The independence hypothesis matters: equal marginal laws alone do not justify multiplying transforms of a sum. These identities convert convolution and affine transformations into multiplication and composition.{{cite:durrett2019}} (§3.3.1)

When $\mathbb E|X|<\infty$, differentiating under the expectation gives $\varphi_X'(0)=i\mathbb EX$. With a finite second moment, $\varphi_X''(0)=-\mathbb EX^2$. The moment assumptions justify the interchange; a transform's existence alone does not justify a derivative calculation for moments.{{cite:durrett2019}} (§3.3.3, moments and derivatives){{cite:grinstead_snell1997}} (§10.3, moments and characteristic functions)

## Worked example
Let $X$ be binomial with three trials and success probability $1/4$. A single Bernoulli transform is $3/4+e^{it}/4$, so
$$
\varphi_X(t)=\left(\frac34+\frac14e^{it}\right)^3.
$$
At $t=\pi$, this is $(1/2)^3=1/8$. At $t=\pi/2$, it equals
$$
\left(\frac34+\frac i4\right)^3=\frac9{32}+i\frac{13}{32}.
$$
Differentiating at zero recovers mean $3/4$ and variance $9/16$. These are also obtained from a direct sum over the four binomial probabilities, giving a separate numerical check of the transform.

**Your turn.** Find the characteristic function of $Y=2X-1$ from the transform above.

::: {.callout-tip collapse="true" title="Answer"}
It is $\varphi_Y(t)=e^{-it}(3/4+e^{2it}/4)^3$. The multiplier records the shift by minus one; replacing $t$ by $2t$ records the rescaling.
:::

## Connections — Distributional limits and escaping moments
[]{#property-cf-continuity}

The continuity theorem says that pointwise convergence of characteristic functions to a function continuous at zero implies convergence in distribution to the law with that transform. Continuity at zero also guarantees that the limiting function is a characteristic function; it need not be assumed separately.{{cite:durrett2019}} (§3.3.2, Thm. 3.3.17, pp. 132–133)

For independent symmetric signs, the normalised sum has transform $[\cos(t/\sqrt n)]^n$. At $t=1$, it is $0.593133$ for $n=4$ and $0.606024$ for $n=100$, approaching $e^{-1/2}=0.606531$. The transform limit is the standard normal characteristic function. The continuity theorem concerns distributions; convergence of means or variances requires further control of the tails.{{cite:durrett2019}} (§3.4.1, independent identically distributed central limit theorem)

