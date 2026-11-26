## Motivating example
For independent uniform observations between zero and one, a sample maximum approaches one. The unscaled maximum therefore has an uninformative point-mass limit. Multiplying its gap below one by the sample size reveals a nondegenerate limiting law. This is a direct finite-endpoint example within the broader study of extreme-value limits, where the normalisation and tail behaviour matter.{{cite:nist_extreme_value}} (§8.1.6.3, extreme-value setting)

## Definition — Start with the exact maximum distribution
Let $M_n=\max(X_1,\ldots,X_n)$ for iid uniform observations on $(0,1)$. For $0\le x\le1$,
$$P(M_n\le x)=P(X_1\le x,\ldots,X_n\le x)=x^n.$$
Independence gives the product. Put $Y_n=n(1-M_n)$. For fixed $y\ge0$ and $n>y$,
$$P(Y_n>y)=P(M_n<1-y/n)=(1-y/n)^n.$$
Continuity makes the strict-versus-nonstrict endpoint irrelevant in this model. A statement about convergence of these distribution functions determines the limiting law at continuity points.

## Properties — Derive the gap limit and its sign
Take logarithms: $n\log(1-y/n)\to-y$. Exponentiation gives $P(Y_n>y)\to e^{-y}$. For negative $y$, $Y_n\ge0$ gives a zero lower tail. Thus $Y_n$ converges in distribution to a rate-one exponential variable $E$. Equivalently $n(M_n-1)\Rightarrow-E$, whose distribution function is $e^x$ for $x\le0$ and one for $x>0$. The positive gap and the centred maximum have opposite signs and opposite supports; confusing them reverses a tail probability.

The reversed exponential is a finite-endpoint extreme-value law of Weibull type. The word *Weibull* here describes the extreme-value shape after normalisation; the positive gap in this uniform example has exponential shape one. Extreme-value terminology depends on whether maxima, minima or reflected variables are being described.{{cite:nist_extreme_value}} (§8.1.6.3, maxima/minima and bounded support)

## Worked example — Assess a finite-sample approximation
With $n=50$ and $y=2$, the exact probability that the maximum lies below $0.96$ is $0.96^{50}\approx0.129886$. The limiting gap approximation is $e^{-2}\approx0.135335$, about $0.005449$ larger. These are probabilities of a gap *greater* than two after scaling, so a larger gap corresponds to a smaller maximum.

For comparison, the probability that the maximum lies below $0.95$ is $0.95^{50}\approx0.076945$. The exact expected maximum is $n/(n+1)$, obtained by integrating its density $n x^{n-1}$. Hence $\E(Y_n)=n/(n+1)$, which is $50/51\approx0.980392$ for this sample size and tends to the rate-one exponential mean.

**Your turn.** At $n=100$, what is the exact probability that the scaled gap exceeds two, and what is its limiting approximation?

::: {.callout-tip collapse="true" title="Answer"}
The exact probability is $0.98^{100}\approx0.132620$, and the approximation is $e^{-2}\approx0.135335$.
:::

## Interpretation — A finite endpoint alone does not choose the scaling
More generally, suppose $F$ has upper endpoint $x_F$ and satisfies $1-F(x_F-t)\sim c t^a$ as $t\downarrow0$, with $c,a>0$. Put $a_n=(cn)^{-1/a}$. Then $n\{1-F(x_F-a_n y)\}\to y^a$, giving $P((x_F-M_n)/a_n>y)\to e^{-y^a}$. This follows from the same product-and-log calculation. The uniform example has $c=a=1$. Different endpoint tails produce different scaling exponents; a finite endpoint by itself supplies neither $a$ nor this regularity condition.; {{cite:nist_extreme_value}} (§8.1.6.3)

## Assumptions and limits — Dependence and endpoint atoms change the calculation
The product $F(x)^n$ requires independent observations with a common distribution. An atom at the upper endpoint changes how quickly the maximum reaches that endpoint. Dependent observations can require additional extreme-value conditions and a different effective clustering of exceedances. The exact uniform derivation is useful because its assumptions and finite-sample error can both be checked directly.{{cite:nist_extreme_value}} (§8.1.6.3, identically distributed extreme observations)

The normalisation also specifies the units of the conclusion. If $X_i$ is uniform on $(a,b)$ with $a<b$, transform it to $(X_i-a)/(b-a)$ before applying the unit-interval calculation. The dimensionless gap is $n(b-M_n)/(b-a)$, and its survival limit is again $e^{-y}$. Thus doubling the measurement unit doubles both the endpoint gap and the interval width, leaving the normalised law unchanged. By contrast, the unnormalised gap has a scale that shrinks with sample size. The limit approximates probabilities at thresholds that move toward the endpoint at that scale; it does not assert that one fixed absolute distance has a nonvanishing exceedance probability as the sample grows.

## Connections — The uniform maximum has an exact variance
The density of $M_n$ on $(0,1)$ is $n x^{n-1}$. Integrating $x$ and $x^2$ against that density gives
$$\E(M_n)=\frac{n}{n+1},\qquad \E(M_n^2)=\frac{n}{n+2}.$$
The variance is therefore
$$\operatorname{Var}(M_n)=\frac{n}{(n+1)^2(n+2)}.$$
The scaled gap is the linear image $Y_n=n(1-M_n)$, so $\operatorname{Var}(Y_n)=n^2\operatorname{Var}(M_n)$. At $n=50$ the maximum has variance $50/(51^2\cdot 52)=50/135252\approx 0.000370$, and the scaled gap has variance $125000/135252\approx 0.924201$. The limiting exponential law has variance $1$. The finite-sample gap variance is already close to that limit, while the unscaled maximum is concentrating at the endpoint: its variance is of order $1/n^2$.

The same integrals recover $\E(Y_n)=n/(n+1)$. At $n=50$ this is $50/51\approx 0.980392$, short of the exponential mean $1$ by $1/51$. Convergence of distribution functions at continuity points does not by itself prove convergence of means. Here the moments can be computed exactly, and they do converge. A heavier endpoint tail can change that rate.

### Properties — A quadratic endpoint tail changes the scale
The uniform tail is linear: $1-F(1-t)=t$ for $0<t<1$, so $c=a=1$ and $a_n=1/n$. A different endpoint shape uses a different power. Let $F(x)=1-(1-x)^2$ on $[0,1]$. Then $F(0)=0$, $F(1)=1$, and the density $2(1-x)$ is nonnegative and integrates to one. The endpoint tail is $1-F(1-t)=t^2$, so $c=1$ and $a=2$. The scale in the general formula is $a_n=n^{-1/2}$.

For $0\le y<\sqrt n$,
$$P\bigl((1-M_n)/\sqrt{1/n}>y\bigr)=\bigl(1-y^2/n\bigr)^n.$$
The elementary limit $(1-y^2/n)^n\to e^{-y^2}$ is the survival function of a Weibull law with shape $2$ and scale $1$. At $n=100$ and $y=1$ the exact probability is $0.99^{100}\approx 0.366032$, and $e^{-1}\approx 0.367879$. At $y=2$ the exact probability is $0.96^{100}\approx 0.016870$, and $e^{-4}\approx 0.018316$. The approximation is already close, and the limit is not exponential. Shape $1$, the uniform case, is the special Weibull law that is exponential.

The scale identity behind the general formula is algebraic. If $a_n=(cn)^{-1/a}$ with $c,a>0$, then
$$n\cdot c\cdot(a_n y)^a=y^a$$
for every $y>0$. Whenever $1-F(x_F-t)\sim c t^a$, the expected number of observations beyond $x_F-a_n y$ tends to $y^a$. Raising the distribution function to the $n$th power then produces the survival limit $e^{-y^a}$, by the same logarithm used for $(1-y/n)^n$. The symbol $a_n$ is a scale for the gap. It is not a centring constant added to the maximum.

### Interpretation — Weibull type is a statement about the maximum
Write $Z_n=n(M_n-1)$ for the uniform sample. Then $Z_n=-Y_n$, and the limit of $Z_n$ is supported on $(-\infty,0]$. Its distribution function equals $e^{x}$ for $x\le 0$ and equals $1$ for $x>0$. That is the Weibull extreme-value law of shape $1$: in the usual type classification it is $\exp\{-(-x)^a\}$ on the negative half-line, here with $a=1$. The positive gap $Y_n$ carries the ordinary Weibull, or exponential, survival function $e^{-y}$. Negating the variable moves one description into the other. Quoting a positive exceedance probability for $Z_n$ reverses the event.

The same endpoint geometry is not the only extreme-value type. An exponential tail, after centring at a multiple of $\log n$, produces the Gumbel limit $e^{-e^{-x}}$ on the whole line.{{cite:durrett2019}} (§3.2, Ex. 3.2.2(iii), p. 123) A Pareto tail of index $\alpha$, scaled by $n^{1/\alpha}$, produces the Fréchet limit $e^{-x^{-\alpha}}$ on the positive line.{{cite:durrett2019}} (§3.2, Ex. 3.2.2(i), p. 123) Those limits are unbounded on the side where the original tail is unbounded. The finite-endpoint limit is bounded on the side of the endpoint. A sample maximum can suggest which picture is plausible only after the tail, the endpoint, and the normalisation have been specified. A finite endpoint by itself does not choose $a$.

## Common misconceptions
The limiting statement is about a moving threshold. For the uniform law, $P(M_n\le 0.99)$ equals $0.99^n$, which tends to zero. The event $\{Y_n>3\}$ is the event $\{M_n<1-3/n\}$, and the threshold $1-3/n$ moves toward $1$. At $n=50$ that threshold is $0.94$, and $0.94^{50}\approx 0.045331$. Treating $0.045331$ as the probability of falling short of a fixed level such as $0.5$ misreads the scaling.

Shape and type are also easy to swap. The uniform calculation has extreme-value shape $1$, and the gap limit is exponential. The quadratic-tail calculation has extreme-value shape $2$, and the gap limit has survival $e^{-y^2}$. Both are Weibull-type limits for the maximum. Neither calculation estimates a shape from data. Dependence, a hard measurement ceiling that is not the distributional endpoint, or a distribution that changes with the sample, all sit outside the independent identical-distribution product $F(x)^n$.
