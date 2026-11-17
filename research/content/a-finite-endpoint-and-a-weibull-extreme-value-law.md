## Motivating example — A maximum squeezed against a ceiling
For independent uniform observations between zero and one, a sample maximum approaches one. The unscaled maximum therefore has an uninformative point-mass limit. Multiplying its gap below one by the sample size reveals a nondegenerate limiting law. This is a direct finite-endpoint example within the broader study of extreme-value limits, where the normalisation and tail behaviour matter.{{cite:nist_extreme_value}} (§8.1.6.3, extreme-value setting)

## Definition — Start with the exact maximum distribution
Let $M_n=\max(X_1,\ldots,X_n)$ for iid uniform observations on $(0,1)$. For $0\le x\le1$,
$$P(M_n\le x)=P(X_1\le x,\ldots,X_n\le x)=x^n.$$
Independence gives the product. Put $Y_n=n(1-M_n)$. For fixed $y\ge0$ and $n>y$,
$$P(Y_n>y)=P(M_n<1-y/n)=(1-y/n)^n.$$
Continuity makes the strict-versus-nonstrict endpoint irrelevant in this model. A statement about convergence of these distribution functions determines the limiting law at continuity points.{{cite:siegrist_convergence_dist}} (“Distributions on R”, definition)

## Properties — Derive the gap limit and its sign
Take logarithms: $n\log(1-y/n)\to-y$. Exponentiation gives $P(Y_n>y)\to e^{-y}$. For negative $y$, $Y_n\ge0$ gives a zero lower tail. Thus $Y_n$ converges in distribution to a rate-one exponential variable $E$. Equivalently $n(M_n-1)\Rightarrow-E$, whose distribution function is $e^x$ for $x\le0$ and one for $x>0$. The positive gap and the centred maximum have opposite signs and opposite supports; confusing them reverses a tail probability.{{cite:siegrist_convergence_dist}} (“Distributions on R”, “Definition”; “Examples and Applications”)

The reversed exponential is a finite-endpoint extreme-value law of Weibull type. The word *Weibull* here describes the extreme-value shape after normalisation; the positive gap in this uniform example has exponential shape one. Extreme-value terminology depends on whether maxima, minima or reflected variables are being described.{{cite:nist_extreme_value}} (§8.1.6.3, maxima/minima and bounded support)

## Worked example — Assess a finite-sample approximation
With $n=50$ and $y=2$, the exact probability that the maximum lies below $0.96$ is $0.96^{50}\approx0.129886$. The limiting gap approximation is $e^{-2}\approx0.135335$, about $0.005449$ larger. These are probabilities of a gap *greater* than two after scaling, so a larger gap corresponds to a smaller maximum.

For comparison, the probability that the maximum lies below $0.95$ is $0.95^{50}\approx0.076945$. The exact expected maximum is $n/(n+1)$, obtained by integrating its density $n x^{n-1}$. Hence $E(Y_n)=n/(n+1)$, which is $50/51\approx0.980392$ for this sample size and tends to the rate-one exponential mean.

**Your turn.** At $n=100$, what is the exact probability that the scaled gap exceeds two, and what is its limiting approximation?

::: {.callout-tip collapse="true" title="Answer"}
The exact probability is $0.98^{100}\approx0.132620$, and the approximation is $e^{-2}\approx0.135335$.
:::

## Interpretation — A finite endpoint alone does not choose the scaling
More generally, suppose $F$ has upper endpoint $x_F$ and satisfies $1-F(x_F-t)\sim c t^a$ as $t\downarrow0$, with $c,a>0$. Put $a_n=(cn)^{-1/a}$. Then $n\{1-F(x_F-a_n y)\}\to y^a$, giving $P((x_F-M_n)/a_n>y)\to e^{-y^a}$. This follows from the same product-and-log calculation. The uniform example has $c=a=1$. Different endpoint tails produce different scaling exponents; a finite endpoint by itself supplies neither $a$ nor this regularity condition.{{cite:siegrist_convergence_dist}} (“Distributions on R”, “Definition”); {{cite:nist_extreme_value}} (§8.1.6.3)

## Assumptions and limits — Dependence and endpoint atoms change the calculation
The product $F(x)^n$ requires independent observations with a common distribution. An atom at the upper endpoint changes how quickly the maximum reaches that endpoint. Dependent observations can require additional extreme-value conditions and a different effective clustering of exceedances. The exact uniform derivation is useful because its assumptions and finite-sample error can both be checked directly.{{cite:nist_extreme_value}} (§8.1.6.3, identically distributed extreme observations)

The normalisation also specifies the units of the conclusion. If $X_i$ is uniform on $(a,b)$ with $a<b$, transform it to $(X_i-a)/(b-a)$ before applying the unit-interval calculation. The dimensionless gap is $n(b-M_n)/(b-a)$, and its survival limit is again $e^{-y}$. Thus doubling the measurement unit doubles both the endpoint gap and the interval width, leaving the normalised law unchanged. By contrast, the unnormalised gap has a scale that shrinks with sample size. The limit approximates probabilities at thresholds that move toward the endpoint at that scale; it does not assert that one fixed absolute distance has a nonvanishing exceedance probability as the sample grows.
