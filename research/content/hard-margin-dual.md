## Motivating example

A separating hyperplane can be described by a coefficient for each feature or by multipliers attached to training observations. The dual representation makes the inner products between observations explicit and identifies which observations contribute to the fitted normal vector.{{cite:deisenroth_faisal_ong2020}} (§12.3, pp.383–385)

## Definition — Multipliers for separation constraints

For a finite separable dataset $(x_i,y_i)$ with labels $y_i\in\{-1,1\}$ and both labels present, the primal minimizes $\|w\|^2/2$ subject to $y_i(w^Tx_i+b)\ge1$. Its dual is
$$\max_{\alpha_i\ge0,\ \sum_i\alpha_i y_i=0}
\left\{\sum_i\alpha_i-\frac12\sum_{i,j}\alpha_i\alpha_jy_iy_jx_i^Tx_j\right\}.$$
The hard-margin problem places no upper bound $C$ on its multipliers. Such a bound belongs to the usual soft-margin formulation.{{cite:burges1998}} (§§3.1–3.2; §3.5)

## Properties — Derivation and complementary slackness

The Lagrangian is $L=\|w\|^2/2+\sum_i\alpha_i[1-y_i(w^Tx_i+b)]$. Its infimum over $b$ is finite only if $\sum_i\alpha_i y_i=0$, and minimisation over $w$ gives $w=\sum_i\alpha_i y_ix_i$. Substitution proves the dual objective. Its quadratic matrix is positive semidefinite because $\alpha^TH\alpha=\|\sum_i\alpha_i y_ix_i\|^2\ge0$.{{cite:deisenroth_faisal_ong2020}} (§12.3.1, pp.383–385)

At an optimum, $\alpha_i[y_i(w^Tx_i+b)-1]=0$. Thus a positive multiplier puts an observation on a margin plane, while an observation strictly beyond its margin has multiplier zero. A margin observation may also have zero multiplier in a degenerate solution. A positive multiplier gives $b=y_i-w^Tx_i$. Finite strict separability permits rescaling a separator to make every constraint strict; convex duality then gives equal primal and dual optimal values.{{cite:burges1998}} (§§3.1–3.2)

## Worked example — Two support observations

In one dimension take $x_1=-1,y_1=-1$ and $x_2=1,y_2=1$. The equality constraint requires $\alpha_1=\alpha_2=a\ge0$. The dual becomes $2a-2a^2$, maximised at $a=1/2$. Recover $w=1,b=0$, with objective $1/2$ and geometric margin width $2/|w|=2$. Each labelled margin is one, and the primal and dual values agree.{{cite:burges1998}} (§§3.1–3.2)

If the two feature values are instead $-2$ and $2$, the maximizing multipliers are $1/8$, the normal coefficient is $1/2$, the objective is $1/8$, and the slab width is four. Feature units therefore affect the norm-based margin problem; scaling is part of specifying its geometry.{{cite:deisenroth_faisal_ong2020}} (§12.2.2, pp.376–377)

**Your turn.** For points $(1,0)$ with label $-1$ and $(3,1),(3,-1)$ with label $+1$, check $w=(1,0)$, $b=-2$, and multipliers $(1/2,1/4,1/4)$.

::: {.callout-tip collapse="true" title="Answer"}
All labelled margins equal one. The weighted labelled points sum to $(1,0)$ and the multipliers satisfy $-1/2+1/4+1/4=0$. Both objectives are $1/2$, so these feasible values are optimal.
:::

## Assumptions and limits

Separation is essential to the hard-margin primal. Two observations at the same feature vector with opposite labels demand both $w^Tx+b\ge1$ and $w^Tx+b\le-1$. For this conflicting pair, setting both dual multipliers to $t$ satisfies the equality constraint, cancels the quadratic term and gives objective $2t\to\infty$. A soft margin changes the constraints and objective to allow violations.{{cite:burges1998}} (§§3.1–3.2; §3.5)


## Check yourself

### [Interpreting multipliers](../questions/ex-sl-17-6.qmd) {#self-check-ex-sl-17-6}

::: {.callout-tip collapse="true" title="Answer"}
For soft-margin $C=2$, a zero multiplier implies zero slack and margin at least one. A multiplier $1.3$ lies strictly between zero and $C$, hence has margin one and zero slack and can determine the intercept. A multiplier equal to $C$ has margin at most one and slack $1-yf$, possibly zero; its multiplier alone does not determine the slack.
:::

### [Kernel as an inner product](../questions/ex-sl-17-4.qmd) {#self-check-ex-sl-17-4}

::: {.callout-tip collapse="true" title="Answer"}
With $\phi(x)=(1,\sqrt2x,x^2)$, the inner product is $1+2xx'+x^2x'^2=(1+xx')^2$. Middle observations with $|x|\le0.9$ have squared coordinate at most $0.81$; tails with $|x|\ge1.5$ have squared coordinate at least $2.25$. A threshold $1.53$ in that coordinate separates them with equal coordinate gaps $0.72$.
:::
