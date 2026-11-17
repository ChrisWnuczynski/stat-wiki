## Motivating example
A classifier separates measurements from two labelled groups by drawing a hyperplane. Many hyperplanes may classify every training observation correctly, yet some pass very close to an observation. A small perturbation could then change its label. The hard-margin criterion selects the separator with the largest clearance in the chosen feature coordinates. Its optimization variable is a normal vector and an intercept; the observations and their labels are fixed inputs.{{cite:cortes_vapnik1995}} (§2.1, pp. 277–279)

Correct classification and confidence are different notions. Multiplying a decision score by a positive constant preserves every predicted label, so its raw magnitude cannot measure clearance without a scale convention. The geometric distance divides the score by the normal vector's length. This is why a norm appears in the optimization problem.{{cite:goodfellow_bengio_courville2016}} (§5.7.2, pp. 138–140)

## Definition — Functional constraints fix the scale
Write $f(x)=w^\top x+b$ and $y_i\in\{-1,+1\}$. Assume that both classes occur and there is a strictly separating affine hyperplane. For a finite sample, strict separation gives a positive minimum signed score. Rescaling makes that minimum one, so the optimization can be written
$$\min_{w,b}\frac12\lVert w\rVert^2\quad\text{subject to}\quad y_i f(x_i)\ge1.$$
The inequalities are affine in the unknowns. The objective is convex, hence a feasible local minimum is a global minimum. Strict convexity in $w$ makes the minimizing normal vector unique, although a general convex quadratic objective need not be strictly convex in every variable.{{cite:cortes_vapnik1995}} (§2.1, eqs. 8–13, pp. 277–279)

The intercept translates the hyperplane and is unpenalised. It cannot be folded into a penalised augmented coefficient without changing the problem. At the optimum the closest observation in each class reaches its corresponding margin plane; otherwise translating or shrinking the slab would improve the objective. This statement presumes that both classes are represented.

## Properties — A geometric and algebraic certificate
For a unit direction $u=w/\lVert w\rVert$, moving a distance $d$ normal to the boundary changes $w^\top x+b$ by $d\lVert w\rVert$. The two planes with scores $-1$ and $1$ therefore lie $2/\lVert w\rVert$ apart. Minimising the squared norm maximises that distance. The distance is measured after the chosen feature transformations, so changing units of only one coordinate can change the fitted classifier.{{cite:cortes_vapnik1995}} (§2.1, eqs. 12–13, p. 278)

A useful optimality certificate uses nonnegative multipliers $\alpha_i$. Stationarity of the Lagrangian gives $w=\sum_i\alpha_i y_ix_i$ and $\sum_i\alpha_i y_i=0$. Complementary slackness gives $\alpha_i\{y_if(x_i)-1\}=0$. Thus an observation strictly outside the margin has zero multiplier. A point on the margin can also have zero multiplier in a degenerate sample, so being geometrically on a margin does not force a strictly positive coefficient. These identities explain why a small subset can determine a boundary.{{cite:cortes_vapnik1995}} (Appendix A.1, pp. 291–293)

## Worked example — Unequal locations, equal clearance
Take one negative observation at $x=-2$ and one positive observation at $x=4$. The constraints become $2w-b\ge1$ and $4w+b\ge1$. Adding them gives $6w\ge2$, hence $w\ge1/3$. Equality is feasible with $b=-1/3$. It minimizes the objective because every feasible weight is at least this large. The objective value is $1/18$, the decision boundary is $x=1$, and each observation lies three units from that boundary. The full gap is six units. This calculation is an instance of the margin geometry above.{{cite:cortes_vapnik1995}} (§2.1, pp. 277–279)

The multipliers $\alpha_1=\alpha_2=1/18$ certify the solution: their signed sum is zero and $\alpha_1(-1)(-2)+\alpha_2(1)(4)=1/3=w$. Both constraints hold with equality. Moving the negative observation farther left need not move the boundary if other negative support observations still determine the nearest class edge.

**Your turn.** Replace the positive observation at $4$ by one at $2$, leaving the negative observation at $-2$. Find $w$, $b$, the objective and the gap.

::: {.callout-tip collapse="true" title="Answer"}
The constraints give $4w\ge2$. Thus $w=1/2$, $b=0$, the objective is $1/8$, and the gap is $2/(1/2)=4$.
:::

## Assumptions and limits — Exact separation is a demanding model
If identical feature vectors carry opposite labels, the two constraints require the same score to be at least one and at most minus one. The feasible set is empty. Less obvious geometric overlap can create the same problem. A hard-margin method therefore needs a feasibility check; a numerical optimizer's failure should not automatically be interpreted as slow convergence. Soft-margin constraints allow violations at a specified cost.{{cite:cortes_vapnik1995}} (§3, pp. 280–282)

A wider training margin alone does not establish reliable out-of-sample accuracy. Feature scaling, feature selection, contamination and the sampling population affect its meaning. The fitted sign also supplies a class label rather than a calibrated posterior probability. Probability estimation requires a further statistical model or a calibration step.{{cite:goodfellow_bengio_courville2016}} (§5.7.2, pp. 138–140)
