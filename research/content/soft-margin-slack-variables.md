## Motivating example
Two observations can have identical predictors and opposite labels. No hyperplane can separate both with a positive margin. Slack variables allow the optimisation to remain feasible, while assigning an explicit cost to violations of the desired margin.{{cite:scholkopf_smola2003_intro}} (§4, eqs. 37–40, pp. 50–51)

## Interpretation — A slack measures a margin shortfall
For score $f_i=w^\top x_i+b$ and label $y_i\in\{-1,+1\}$, the constraints are $\xi_i\ge0$ and $y_if_i\ge1-\xi_i$. When $C>0$, the smallest feasible slack at fixed $(w,b)$ is optimal:
$$
\xi_i=(1-y_if_i)_+.
$$
Substituting this expression into the primal objective gives a squared-normal penalty plus $C$ times the sum of hinge losses. A correct classification with $0<y_if_i<1$ still has positive loss. A negative margin has slack greater than one, while zero margin has slack exactly one.{{cite:burges1998}} (§3.5, The Non-Separable Case)

The slack is measured in score units. For $w\ne0$, its corresponding shortfall from the required signed geometric margin is $\xi_i/\|w\|$. It is not the distance to the decision plane: for a misclassified point that distance is $-y_if_i/\|w\|$. Mixing these two quantities misinterprets the penalty.{{cite:burges1998}} (§§3.1, 3.5)

## Properties — What the multiplier reveals
The stationarity condition for a slack is $C-\alpha_i-\mu_i=0$. Since $\mu_i\ge0$, it gives the dual bound $0\le\alpha_i\le C$. Complementarity further gives $\mu_i\xi_i=0$ and $\alpha_i(y_if_i-1+\xi_i)=0$. Hence $\alpha_i<C$ implies zero slack, and $0<\alpha_i<C$ places the observation exactly at margin one. The converse need not hold: degeneracy can put a point on a boundary with multiplier zero.{{cite:burges1998}} (§3.5, eqs. 48–56)

Increasing $C$ changes the relative cost of margin violations and normal length. The optimum can trade a narrower margin for smaller aggregate hinge loss. The numerical value of $C$ also depends on whether the empirical loss is a sum or an average, so comparisons across different sample-size conventions require rescaling.{{cite:scholkopf_smola2003_intro}} (§4, eq. 39, p. 51)

## Worked example — Three margins and a contradictory pair
Margins $1.5,0.4,-0.2$ require optimal slacks $0,0.6,1.2$. Their sum is $1.8$, and at $C=2$ their contribution to the objective is $3.6$, before adding $\|w\|^2/2$. Only the third observation is strictly misclassified, though two have positive hinge loss.

For two opposite labels at the same predictor vector zero, $w$ cannot help. The total hinge loss is $(1-b)_++(1+b)_+$. It equals two for every $b\in[-1,1]$ and exceeds two outside that interval. Thus $w=0$ and any such intercept minimise the objective at $2C$. This example exhibits a unique normal vector and a range of optimal intercepts; neither feasibility nor convexity ensures every fitted parameter is unique.{{cite:scholkopf_smola2003_intro}} (§4, soft-margin objective)

**Your turn.** A point has margin $0.25$. Find its minimum slack and its penalty contribution at $C=4$.

::: {.callout-tip collapse="true" title="Answer"}
The minimum slack is $0.75$, and the contribution is $4(0.75)=3$. The point is correctly classified but lies inside the margin.
:::

## Check yourself

### Read the multiplier cases {#self-check-ex-sl-17-6}

[Practice question](../questions/ex-sl-17-6.qmd)

At $C=2$, interpret multipliers $0$, $1.3$ and $2$.

::: {.callout-tip collapse="true" title="Answer"}
For $\alpha=0$, the margin is at least one and slack is zero. For $\alpha=1.3$, the margin is exactly one and slack is zero, so this point can determine the intercept. For $\alpha=2$, the margin is at most one and slack equals $1-yf$; it can be zero at the boundary.
:::

### A point beyond the margin {#self-check-ex-sl-17-3}

[Practice question](../questions/ex-sl-17-3.qmd)

A new positive point has score four under a fitted separator. Can it be assigned zero multiplier without changing the optimum?

::: {.callout-tip collapse="true" title="Answer"}
Yes. Its slack is zero and its margin constraint is strict, so its multiplier is zero. The previous primal and dual solutions remain feasible and satisfy the same optimality conditions.
:::
