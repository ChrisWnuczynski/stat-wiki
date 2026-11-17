## Motivating example

A dose-response curve may be nearly straight at low doses and bend sharply after a threshold. One high-degree polynomial has to accommodate that bend across the whole range. A spline instead joins simpler pieces at chosen dose values called knots, allowing local changes in shape while keeping the curve smooth. The number, location and smoothness conditions at the joins determine which shapes the model can express.

## Intuition — How knots change spline flexibility

Think of a knot as a location where the algebraic description is allowed to change. It is not necessarily a point of visible sharpness. A continuous linear spline may have a corner there; a cubic spline normally joins its pieces with the same value, slope and curvature, so the change appears only in its third derivative. Knots specify the *available* flexibility, while a penalty or other fitting rule determines how much of that flexibility the estimate uses.

The position of a knot is expressed on the predictor scale. If age is measured in months, a knot at $24$ means two years; changing to years moves its numerical coordinate to $2$ without changing the physical join. A knot is not generally a threshold at which a treatment suddenly begins to work. Its interpretation depends on the model and data.

## Definition

For ordered knots $\xi_1<\cdots<\xi_M$, a spline is a function built from polynomial pieces on the intervals they delimit, subject to specified matching conditions at each join. For a cubic spline with ordinary interior knots, the pieces and their first two derivatives agree at each $\xi_m$. One convenient representation is

$$
g(x)=\beta_0+\beta_1x+\beta_2x^2+\beta_3x^3+\sum_{m=1}^M\gamma_m(x-\xi_m)_+^3,
\qquad (u)_+=\max(u,0).
$$

The truncated term is zero to the left of its knot and cubic to the right. Each coefficient $\gamma_m$ changes the shape after $\xi_m$ without making a jump in value, slope or curvature at the join. The representation describes a spline basis; individual coefficients need not have an easy causal meaning.{{cite:hastie_esl2009}} (§5.4, pp. 151–152)

## Interpretation

Moving a knot changes where a local bend can be represented efficiently. Adding a knot expands the unpenalised function space, but it need not increase the effective complexity of a penalised fit by a whole unit: a strong roughness penalty can shrink its extra wiggle. A smoothing spline typically has an available knot at each distinct observed predictor value, then controls roughness by a penalty.{{cite:hastie_esl2009}} (§5.4, pp. 151–152) A regression spline starts from a smaller chosen basis. Those are different modelling choices, even when their fitted curves look alike.

Boundary knots mark the ends of the region where the interior spline basis is defined. A natural cubic spline additionally requires linear behaviour outside its boundary knots. That constraint concerns the extrapolation tails and should not be confused with the continuity conditions at ordinary interior knots. Predicting beyond the observed range calls for attention to those tails, because data there do not determine the curve.

## Properties

The $m$th truncated cubic and its first two derivatives are all zero at $x=\xi_m$ from both sides, so adding it preserves the three matching conditions. Its third derivative changes by $6\gamma_m$ across the knot. For $M$ distinct interior knots, the displayed unrestricted truncated-power basis has $M+4$ coefficients. Extra boundary constraints reduce this dimension, and the rank of a fitted design also depends on where observations lie. Thus counting visible knots is not the same as reading effective degrees of freedom from a penalised model.{{cite:hastie_esl2009}} (§5.4, pp. 151–152)

A linear spline uses terms $(x-\xi_m)_+$ instead. These are continuous, but their derivatives jump by their coefficients at the knots. A quadratic spline uses squared truncated terms and matches values and first derivatives. The polynomial degree and imposed boundary conditions, rather than the word *knot* alone, specify smoothness.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write $h(x)=(x-\xi)_+^3$. For $x<\xi$, $h=h'=h''=h'''=0$. For $x>\xi$, $h=(x-\xi)^3$, $h'=3(x-\xi)^2$, $h''=6(x-\xi)$ and $h'''=6$. The limits of $h,h',h''$ at $\xi$ agree and equal zero; the one-sided third derivatives differ by $6$. Multiplying by $\gamma$ gives a jump of $6\gamma$ and proves the cubic joining claim. The polynomials $1,x,x^2,x^3$ and the truncated terms at distinct ordered knots are linearly independent as functions on a domain extending beyond the outer knots: restricting to the interval left of the first knot forces the polynomial coefficients to vanish, and then moving through successive intervals forces each $\gamma_m=0$. The unrestricted space therefore has dimension $M+4$. Similarly $(x-\xi)_+$ has equal zero values at its join but one-sided slopes $0$ and $1$, proving the linear-spline statement.
:::
:::

## Statistical use

Choose enough basis flexibility to express plausible structure, then use a penalty or validation procedure to control how much is fitted. Quantile-spaced knots allocate more joins where observed predictor values are dense; equally spaced knots allocate them by predictor distance. Neither rule is universally best. Inspect residual patterns and uncertainty, especially near boundaries and in sparse regions. When comparing two fitted curves, report the basis, number or locations of knots, boundary conditions and penalty selection method; a statement such as “a cubic spline was fitted” leaves important choices unspecified.

The fitted smooth in a generalized additive model contributes on its link scale. A bend in a logit-scale smooth changes the probability curve after the inverse link, but it does not imply a discontinuity in probability at a knot. Likewise, the effective degrees of freedom summarize fitted flexibility; they are neither the number of knots nor the degree of a fractional polynomial.

If all observed ages lie below a proposed knot at $200$ months, the corresponding truncated-power column is zero on the sample, so its coefficient cannot be estimated from those data. If data are sparse between $20$ and $80$ months, placing many knots there does not create observations and can make unpenalised coefficients unstable. A degree-one spline with knot at $2$ and nonzero truncated-linear coefficient has an actual slope discontinuity, so cubic smoothness must not be inferred from every spline. Beyond the boundary knots, different extrapolation rules can give very different predictions while fitting the observed range similarly.
## Worked example

Consider $g(x)=1+2x+3(x-2)_+^3$, with a knot at $x=2$. For $x\leq2$, the curve is the line $1+2x$; for $x>2$, it adds a cubic term. Thus $g(1)=3$, $g(2)=5$, $g(3)=10$ and $g(2.5)=6.375$. The value, slope and curvature meet at the knot: $g(2)=5$, $g'(2^-)=g'(2^+)=2$ and $g''(2^-)=g''(2^+)=0$. The third derivative changes from $0$ on the left to $18$ on the right. This knot permits a bend after $2$ but does not make a corner in the fitted curve.

**Your turn.** Let $f(x)=2+3x-(x-1)_+^3$. Find $f(0)$, $f(1)$, $f(2)$, the slope and curvature on both sides of $x=1$, and the third-derivative jump there.

::: {.callout-tip collapse="true" title="Answer"}
$f(0)=2$, $f(1)=5$ and $f(2)=7$. To the left of $1$, $f'=3$ and $f''=0$; to the right, $f'=3-3(x-1)^2$ and $f''=-6(x-1)$. Both one-sided slopes at $1$ are $3$ and both curvatures are $0$. The third derivative changes from $0$ to $-6$, a jump of $-6$.
:::

## Common misconceptions

A knot does not imply a visible corner: ordinary cubic joins preserve slope and curvature. More knots do not force a more wiggly *penalised* fit, because the penalty can suppress that flexibility. Effective degrees of freedom are not the number of knots. An observed bend near a knot does not prove a biological threshold there; it can reflect basis placement and sampling variation. Finally, knots alone do not specify tail behaviour—natural boundary conditions must be stated separately.

## Connections

The [spline](spline.qmd) article describes the whole piecewise-polynomial family. A [cubic smoothing spline](cubic-smoothing-spline.qmd) pairs a rich knot set with a roughness penalty. [Effective degrees of freedom](effective-degrees-of-freedom.qmd) summarize the fitted flexibility after penalisation, while [regularisation](regularisation.qmd) explains why expanding a basis need not produce an equally complex estimate.

Among curves with a square-integrable second derivative, the roughness-penalised residual sum of squares is minimised by a natural cubic spline with knots at the observations.{{cite:reinsch1967}} (§§2–3, pp. 177–179)

A cubic spline can also be written with a truncated-power basis, one extra term for each interior knot.{{cite:hastie_esl2009}} (§5.4, pp. 151–152)

Boundary conditions that force linearity outside the outer knots define a natural cubic spline.{{cite:hastie_esl2009}} (§5.4, pp. 151–152)
