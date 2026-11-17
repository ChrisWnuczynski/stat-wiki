## Motivating example
A normalized sum of many independent variables can have an awkward density or probability mass function. Its characteristic function is often easier: independence turns a convolution into a product, and normalization changes the argument. Lévy's continuity theorem converts a pointwise limit of those functions into convergence of probability laws, provided the limit is continuous at zero. That last condition prevents probability from escaping to arbitrarily distant regions.{{cite:durrett2019}} (§3.3.2, thm. 3.3.17, pp. 132–133)

A characteristic function $\varphi_X(t)=E(e^{itX})$ always exists because the integrand has modulus one. Unlike an ordinary moment-generating function, it does not require exponential moments. It also determines the probability law uniquely, so it can identify a limit even for heavy-tailed variables.{{cite:grinstead_snell1997}} (§10.3, characteristic functions, pp. 397–401)

## Definition — Pointwise convergence plus continuity at zero
Let $\varphi_n$ be characteristic functions of real-valued random variables. If $\varphi_n(t)\to\varphi(t)$ for every real $t$ and $\varphi$ is continuous at zero, there is a probability law with characteristic function $\varphi$, and the corresponding laws converge weakly to it. Conversely, weak convergence implies pointwise convergence of the characteristic functions to that of the weak limit. Weak convergence means convergence of distribution functions at every continuity point of the limiting distribution function.{{cite:durrett2019}} (§3.3.2, thm. 3.3.17)

The theorem asserts existence as well as convergence. A proposed pointwise limit is not automatically a characteristic function. Since every $\varphi_n(0)=1$, its limit at zero is one; continuity there ties that value to the values at nearby frequencies. No convergence of moments is assumed or implied merely by this statement.

## Properties — Tightness is the central step
::: {.callout-note collapse="true" title="Proof"}
For the forward direction, $e^{itx}$ is bounded and continuous in $x$, so weak convergence gives convergence of its real and imaginary expectations. For the converse, write $\operatorname{sinc}(z)=\sin(z)/z$, with value one at zero. Fubini gives
$$\frac1h\int_{-h}^h[1-\operatorname{Re}\varphi_n(t)]\,dt=2E[1-\operatorname{sinc}(hX_n)].$$
For $|hX_n|>2$, the expression $2[1-\operatorname{sinc}(hX_n)]$ is at least one. Consequently the integral bounds $P(|X_n|>2/h)$. Dominated convergence passes its limit through the finite $t$ integral. Continuity of $\varphi$ at zero makes the limiting bound arbitrarily small for sufficiently small $h$. This bounds the tails uniformly for sufficiently large indices; the finitely many earlier laws can also be enclosed in a larger bounded interval. The laws are therefore tight. Every subsequence has a weakly convergent further subsequence; the forward direction identifies its characteristic function as $\varphi$. Uniqueness of the law with that characteristic function makes all these limits identical, proving convergence of the full sequence.{{cite:durrett2019}} (§3.3.2, proof of thm. 3.3.17, pp. 132–133)
:::

The uniqueness step matters. Transform calculations do not identify only a few moments; they identify an entire distribution. This differs from matching a finite list of moments, which can leave many different distributions possible. Characteristic functions remain useful when the corresponding moment-generating integral diverges.{{cite:grinstead_snell1997}} (§10.3, pp. 397–401)

## Worked example — A symmetric two-point sum
Let $X_1,X_2,\ldots$ independently take values $-1$ and $1$ with equal probabilities. For $Z_n=n^{-1/2}\sum_iX_i$, independence gives
$$\varphi_{Z_n}(t)=\{\cos(t/\sqrt n)\}^{n}.$$
For each fixed $t$, Taylor expansion gives $\cos(t/\sqrt n)=1-t^2/(2n)+O(n^{-2})$. Taking the logarithm for sufficiently large $n$ yields $n\log\cos(t/\sqrt n)\to-t^2/2$. The limiting transform is $e^{-t^2/2}$, continuous at zero and equal to the characteristic function of a standard normal variable. Hence $Z_n$ converges in distribution to that normal law.{{cite:durrett2019}} (§§3.3.2, 3.4.1)

At $t=1$, the transforms for $n=1,10,100$ are $0.540302$, $0.601359$ and $0.606024$; the limit is $0.606531$. Checking these values illustrates the transform calculation without treating three numerical evaluations as a proof of convergence for every frequency.

**Your turn.** For $Y_n=X_1/n$, find its characteristic function and limiting distribution.

::: {.callout-tip collapse="true" title="Answer"}
Its characteristic function is $\cos(t/n)$, which tends to one at every fixed $t$. The constant-one transform corresponds to a point mass at zero, so $Y_n$ converges in distribution to zero.
:::

## Assumptions and limits — A discontinuous transform limit
If $X_n\sim N(0,n)$, then $\varphi_n(t)=e^{-nt^2/2}$. It tends to zero for every nonzero $t$ and remains one at zero. The limiting function is discontinuous there. The variances spread the laws over increasing distances; their distribution functions tend to $1/2$ at each finite point, which is not a distribution function on the real line. Pointwise transform convergence alone therefore does not provide weak convergence.{{cite:durrett2019}} (§3.3.2, remark following thm. 3.3.17)

Even a valid weak limit does not imply convergence of expected values of unbounded functions. Such moment conclusions need additional tail control, for example uniform integrability. The continuity theorem addresses convergence of laws and should be used at that level unless stronger conditions are supplied.

Pointwise convergence of characteristic functions, together with continuity of the limit at the origin, is the hypothesis the theorem uses. Convergence of densities is a stronger conclusion and is not part of that hypothesis.
