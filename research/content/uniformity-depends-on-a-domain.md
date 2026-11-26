## Lead context
A constant density becomes a probability only after its reference measure and support are specified. A change of coordinates transforms that density together with the support.{{cite:durrett2019}} (§1.2, ex. 1.2.3, p. 12)

## Motivating example
A uniform draw on $(0,1)$ has total mass one although its support approaches both boundary points. By contrast, a constant positive density on $(0,\infty)$ has infinite integral. Boundedness of the integral, rather than contact with a boundary, is the relevant distinction.{{cite:durrett2019}} (§1.2, ex. 1.2.3 and density normalisation, p. 12)

## Properties — Carry the region through the transformation
For $u=\alpha/(\alpha+\beta)$, $v=(\alpha+\beta)^{-1/2}$, and $t=\alpha+\beta$, direct differentiation gives
$$
\frac{\partial(u,v)}{\partial(\alpha,\beta)}=
\begin{pmatrix}\beta/t^2&-\alpha/t^2\\-\tfrac12t^{-3/2}&-\tfrac12t^{-3/2}\end{pmatrix},
\qquad |J|=\tfrac12t^{-5/2}.
$$
Thus a density $c$ relative to $du\,dv$ on a region $D$ becomes $c|J|1\{(u(\alpha,\beta),v(\alpha,\beta))\in D\}$ relative to $d\alpha\,d\beta$. The indicator is part of the formula. Jacobian transformation also applies to reference priors under one-to-one reparameterisation, but it does not imply that a flat density in every coordinate is the same prior.{{cite:bernardo2005_reference}} (§3.8, discussion preceding thm. 11)

For the whole strip $D=(0,1)\times(0,\infty)$ the constant-density integral is infinite. For $D=(0,1)\times[1,2]$ its area is one, so $c=1$ gives a proper distribution. Its transformed support is $\alpha,\beta>0$ and $1/4\le\alpha+\beta\le1$. On that support the normalised density is exactly $\tfrac12(\alpha+\beta)^{-5/2}$. A missing support restriction would describe a different, improper measure.{{cite:durrett2019}} (§1.2, density normalisation)

## Worked example
Under this rectangular uniform law, $U$ and $V$ are independent and $T=\alpha+\beta=V^{-2}$. Hence
$$
\E(T)=\int_1^2v^{-2}\,dv=\tfrac12,
\qquad \mathbb{P}(T\ge1/2)=\mathbb{P}(V\le\sqrt2)=\sqrt2-1=0.41421.
$$
This prior gives a uniform mean fraction $U$ but a nonuniform concentration $T$. The distinction can also be seen from $f_T(t)=\tfrac12t^{-3/2}$ on $[1/4,1]$, obtained by one-dimensional change of variables.{{cite:durrett2019}} (§1.2, exer. 1.2.5, p. 14)

**Your turn.** Restrict instead to $0<u<1$ and $2\le v\le4$. Find the constant density in $(u,v)$, the range of $t$, and $\E(t)$.

::: {.callout-tip collapse="true" title="Answer"}
The rectangle has area $2$, so its density is $1/2$. The range is $1/16\le t\le1/4$, and $\E(t)=\tfrac12\int_2^4v^{-2}\,dv=1/8$.
:::

## Assumptions and limits
A finite posterior normalising integral is required when an improper prior is used. Multiplying the likelihood by an improper weight produces a posterior only after that integral has been shown to be finite and positive. Reference analysis adds conditions on a sequence of proper priors that approximate the target weight. The Jacobian calculation and the choice of a scientifically meaningful domain are successive steps: the first transforms a density that has already been specified, and the second decides which region carries the probability.{{cite:bernardo2005_reference}} (§2.3, def. 3)

## Definition — A uniform law names its region
A random vector is uniform on a region $D$ of finite positive volume when its density is constant on $D$ and zero outside $D$, and the constant equals the reciprocal of the volume. On the unit interval $(0,1)$ the volume is $1$ and the density is $1$. On a rectangle $(0,1)\times[1,2]$ the area is $1$ and the constant density in the coordinates $(u,v)$ is again $1$. On $(2,6)$ the length is $4$ and the density is $1/4$. In each case the phrase “uniform” is incomplete until $D$ and the coordinate measure are named. A positive constant function on the half-line $(0,\infty)$ has infinite integral, so it is a weight and not a probability density. Contact with an endpoint is irrelevant to that distinction: the uniform law on $(0,1)$ meets both endpoints in the closure of its support and still integrates to one.{{cite:durrett2019}} (§1.2, ex. 1.2.3 and density normalisation, p. 12)

## Interpretation — The Jacobian carries the volume element
If $u=g(\alpha,\beta)$ and $v=h(\alpha,\beta)$ is a one-to-one map between open regions, a density $f(u,v)$ transforms by multiplication with the absolute Jacobian determinant. The image of $D$ must be written explicitly. For the map used above,
$$
u=\frac{\alpha}{\alpha+\beta},\qquad v=(\alpha+\beta)^{-1/2},\qquad |J|=\tfrac12(\alpha+\beta)^{-5/2},
$$
a constant density $c$ on a set $D$ in the $(u,v)$ plane becomes $c|J|$ on the image of $D$ in the $(\alpha,\beta)$ plane. For $D=(0,1)\times[1,2]$ one has $c=1$ and the image is $\alpha>0$, $\beta>0$, $1/4\le\alpha+\beta\le1$. The transformed density is exactly $\tfrac12(\alpha+\beta)^{-5/2}$ on that set and zero outside it. Omitting the indicator would leave a positive function on a larger set, and the integral of that larger function is a different total mass.{{cite:bernardo2005_reference}} (§3.8, discussion preceding thm. 11)

A one-dimensional illustration makes the same point with an elementary integral. Let $X$ be uniform on $(2,6)$, with density $1/4$, and set $U=\log X$. Then $X=e^U$ and $dx/du=e^u$, so the density of $U$ is $e^u/4$ on $(\log2,\log6)$. Its integral is
$$
\int_{\log2}^{\log6}\frac{e^u}{4}\,du=\frac{6-2}{4}=1.
$$
The factor $e^u$ is the local stretching of length. The limits $\log2$ and $\log6$ are the image of the original interval. Either piece alone describes a different function: $e^u/4$ on the whole line has infinite integral, and the constant $1/4$ on $(\log2,\log6)$ integrates to $(\log6-\log2)/4=\log(3)/4=0.274653$, which is the length of the logged interval times the old density, and is not a probability for $U$.{{cite:durrett2019}} (§1.2, exer. 1.2.5, p. 14)

## Intuition — Probability is assigned to sets
Uniformity means that sets of equal volume inside $D$ receive equal probability, and sets outside $D$ receive probability zero. Changing coordinates changes which sets have equal volume. Logarithmic coordinates stretch large $x$ and compress small $x$, so a law that was flat in $x$ is tilted in $u$. The rectangular law in $(u,v)$ is flat in those coordinates and becomes the curved density $\tfrac12 t^{-5/2}$ in the concentration coordinate $t=\alpha+\beta$. Both descriptions are the same probability measure written in different variables.

The expectation calculation in the worked example is the average of $t=v^{-2}$ against the uniform law of $v$ on $[1,2]$. Because $v$ is uniform there, $\E(T)=\int_1^2 v^{-2}\,dv=1/2$. The probability $\mathbb{P}(T\ge1/2)=\mathbb{P}(V\le\sqrt2)=\sqrt2-1=0.414214$ uses the same flat density of $v$: the event is an interval of $v$-length $\sqrt2-1$, and the whole $v$-interval has length $1$, so the probability equals that length. A reader who starts from the curved density of $T$ recovers the same probability by integrating $\tfrac12 t^{-3/2}$ from $1/2$ to $1$.

## Common misconceptions
An improper flat weight is sometimes described as “the uniform distribution on the whole space.” A probability distribution integrates to one. The constant function on $(0,\infty)$, or on the strip $(0,1)\times(0,\infty)$, integrates to infinity. It can still be a useful prior weight when the posterior integral is finite, and that finiteness is a property of the weight together with the likelihood. The name “uniform” fits the proper laws whose domains have finite volume.

Including or excluding an endpoint of a continuous interval does not change the uniform law, because a single point has volume zero. The same sentence fails for a discrete uniform law on a finite set: removing a point removes a positive share of the probability. The continuous Jacobian calculation and the discrete counting calculation use different reference measures.{{cite:durrett2019}} (§1.2, density normalisation)

## Connections
The change-of-variable formula is the general fact of which these examples are cases. Reference priors transform by the same Jacobian when the parameter is rewritten, so a density that is flat in $(\alpha,\beta)$ is a different prior from a density that is flat in $(u,v)$. Posterior summaries should name the parameter in which they are computed. A probability statement about $T=\alpha+\beta$ uses the marginal density of $T$, here $\tfrac12 t^{-3/2}$ on $[1/4,1]$ for the rectangular prior, whose integral equals one by the substitution checked above.{{cite:bernardo2005_reference}} (§3.8, discussion preceding thm. 11){{cite:durrett2019}} (§1.2, ex. 1.2.3, p. 12)
