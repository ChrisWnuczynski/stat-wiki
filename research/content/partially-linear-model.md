## Motivating example
A treatment comparison may need a coefficient that can be reported per unit, while age requires a curved adjustment. Making both terms linear risks misrepresenting age; making both terms free curves loses a simple treatment contrast. A partially linear model assigns the two roles separately.{{cite:hastie_tibshirani1986}} (§1, pp. 297–298)

## Definition — A coefficient beside a function
For an identity link, write
$$
Y=X^\top\beta+f(Z)+\varepsilon,\qquad E(\varepsilon\mid X,Z)=0.
$$
For a generalised response, the corresponding additive predictor is $g(\mu)=X^\top\beta+f(Z)$. The first model concerns the conditional mean directly; the second concerns it through the specified link. The response family and link must be stated along with the predictor.{{cite:hastie_tibshirani1986}} (§1, semiparametric additive models, p. 298){{cite:nelder_wedderburn1972}} (§§1.1–1.3, pp. 371–372)

If $X$ includes an intercept, a centring constraint on $f$ prevents its constant from being traded against that intercept. If another component of $X$ is entirely determined by a function of $Z$, the coefficient and the function can become inseparable. The data need variation in the linear predictor beyond the variation explained by the smooth variables.

## Properties — Partialling out a chosen basis
For the Gaussian least-squares model, approximate $f$ by columns of a full-rank matrix $B$ and set $M_B=I-B(B^\top B)^{-1}B^\top$. If $X^\top M_BX$ is nonsingular, the fitted linear coefficient is
$$
\widehat\beta=(X^\top M_BX)^{-1}X^\top M_By.
$$
To derive it, minimise $\|y-X\beta-B\gamma\|^2$ first over $\gamma$. The residual is $M_B(y-X\beta)$; differentiating its squared norm with respect to $\beta$ gives the stated normal equations. This finite-basis identity explains residualisation. Smoothing penalties change the relevant fitting operator, and non-Gaussian responses require an appropriate likelihood fit.{{cite:hastie_tibshirani1986}} (§2, additive regression and backfitting){{cite:nelder_wedderburn1972}} (§2.1, pp. 372–374)

## Worked example
Take six values $z=(-2,-1,0,1,2,3)$ and $x=(0,1,0,1,0,1)$, with responses $y=2x+z^2$. Regressing $y$ on an intercept and $x$ alone gives coefficient $3$ on $x$. The group with $x=1$ also has a larger mean of $z^2$, and that difference contaminates the simple comparison.

Now let $B$ contain $1,z,z^2$. The residualised products are
$$
x^\top M_Bx=\frac{48}{35},\qquad
x^\top M_By=\frac{96}{35},
$$
so the adjusted coefficient is exactly $2$. These data contain no random error; the example isolates the algebra of adjustment from sampling uncertainty. Allowing linear terms to coexist with smooth terms is the semiparametric additive construction.{{cite:hastie_tibshirani1986}} (§1, p. 298)

For a logit model with a treatment indicator and coefficient $0.4$, the treatment odds ratio at a fixed $Z$ is $e^{0.4}=1.491825$. The corresponding probability difference depends on the baseline value of the smooth term. A constant conditional odds ratio does not imply a constant risk difference.{{cite:nelder_wedderburn1972}} (§3.3, binomial link, pp. 379–380)

**Your turn.** If the linear predictor at baseline is $-1$ and treatment adds $0.4$, compute both probabilities.

::: {.callout-tip collapse="true" title="Answer"}
They are $\operatorname{expit}(-1)=0.268941$ and $\operatorname{expit}(-0.6)=0.354344$. The increase is about $0.085402$.
:::

