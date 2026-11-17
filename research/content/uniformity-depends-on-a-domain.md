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
E(T)=\int_1^2v^{-2}\,dv=\tfrac12,
\qquad P(T\ge1/2)=P(V\le\sqrt2)=\sqrt2-1=0.41421.
$$
This prior gives a uniform mean fraction $U$ but a nonuniform concentration $T$. The distinction can also be seen from $f_T(t)=\tfrac12t^{-3/2}$ on $[1/4,1]$, obtained by one-dimensional change of variables.{{cite:durrett2019}} (§1.2, exer. 1.2.5, p. 14)

**Your turn.** Restrict instead to $0<u<1$ and $2\le v\le4$. Find the constant density in $(u,v)$, the range of $t$, and $E(t)$.

::: {.callout-tip collapse="true" title="Answer"}
The rectangle has area $2$, so its density is $1/2$. The range is $1/16\le t\le1/4$, and $E(t)=\tfrac12\int_2^4v^{-2}\,dv=1/8$.
:::

## Assumptions and limits
A finite posterior normalising integral is necessary when an improper prior is used; formal multiplication by the likelihood does not establish that integral. Reference analysis also imposes conditions on approximating proper priors, rather than identifying every improper weight as an objective prior. The coordinate calculation and the choice of a scientifically meaningful prior domain are separate mathematical steps.{{cite:bernardo2005_reference}} (§2.3, def. 3)
