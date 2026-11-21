## Lead context
The soft-margin primal asks for a wide separating slab and charges a cost for every training point that falls short of the margin.

## Motivating example
Take $\beta=(1,0)^\top$, $\beta_0=0$ and $C=2$. Then $\tfrac12\|\beta\|^2=0.5$ and the margin is $1$. Three labelled points give functional margins $2$, $0.5$ and $-0.25$, so the smallest feasible slacks are $0$, $0.5$ and $1.25$. Their sum is $1.75$, and the primal cost is

$$
0.5+2\times 1.75=4.
$$

The third point is misclassified, because its functional margin is negative and its slack exceeds $1$. This plane is feasible. Feasibility of this plane does not make it the minimiser.

## Intuition — A budget for overlap
With labels $Y_i\in\{-1,+1\}$, a hard-margin plane asks for $Y_i f(X_i)\ge 1$ at every training index. Overlapping classes make that list impossible. A slack $\xi_i\ge 0$ records the shortfall, and the cost $C\sum_i\xi_i$ trades those shortfalls against the squared weight norm. A small $C$ buys a wider slab. A large $C$ spends more to push points back across the margin, and $C=\infty$ is the separable problem.{{cite:hastie_esl2009}} (Ch. 12, §12.2, pp. 419–420, Eqs. 12.7–12.8)

## Definition — The primal cost
For a coefficient vector $\beta$ and an intercept $\beta_0$, the soft-margin primal is

$$
\min_{\beta,\beta_0,\xi}\ \frac12\|\beta\|^2+C\sum_{i=1}^{N}\xi_i
$$

subject to $\xi_i\ge 0$ and $Y_i(X_i^\top\beta+\beta_0)\ge 1-\xi_i$. The geometric margin of the resulting plane is $1/\|\beta\|$.{{cite:hastie_esl2009}} (Ch. 12, §12.2.1, p. 420, Eq. 12.8)

## Properties — The smallest feasible slack
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Fix $\beta$ and $\beta_0$, and write $f(x)=x^\top\beta+\beta_0$. The objective increases with each $\xi_i$, and the constraints on that slack are $\xi_i\ge 0$ and $\xi_i\ge 1-Y_i f(X_i)$. The smallest feasible choice is therefore

$$
\xi_i=\max\{0,\ 1-Y_i f(X_i)\}.
$$

If $Y_i f(X_i)\ge 1$, the point is outside the margin or on it and the slack is zero. If $0\le Y_i f(X_i)<1$, the point is inside the margin but on the correct side, and the slack is $1-Y_i f(X_i)\le 1$. If $Y_i f(X_i)<0$, the point is on the wrong side of the plane and the slack exceeds $1$.{{cite:hastie_esl2009}} (Ch. 12, §12.2, p. 419)
:::
:::

At a solution, the weight is a combination of the training points, $\hat\beta=\sum_i\hat\alpha_i Y_i X_i$, with $0\le\hat\alpha_i\le C$. Points with $0<\hat\alpha_i<C$ sit on the margin with slack zero. Points with $\hat\alpha_i=C$ have positive slack.{{cite:hastie_esl2009}} (Ch. 12, §12.2.1, pp. 420–421, Eqs. 12.12 and 12.17)

## Worked example — A feasible plane, not yet the optimum

**Your turn.** Use the same plane and the same three slacks, but set $C=1$. What is the primal cost, and which point is misclassified?

::: {.callout-tip collapse="true" title="Answer"}
The weight term is still $0.5$ and the total slack is still $1.75$, so the cost is $0.5+1.75=2.25$. The third point, with functional margin $-0.25$, is the misclassified one. Lowering $C$ does not move that point; it only charges less for the shortfall.
:::

## Connections — Dual bounds and the hinge
The [hard-margin primal](hard-margin-primal.qmd) is the same programme with every slack forced to zero. The [hinge loss](hinge-loss.qmd) is what remains after each slack is replaced by $\max\{0,1-Y_i f(X_i)\}$. In the dual, $C$ becomes the upper bound on the multipliers, and a [kernel](kernel.qmd) replaces $X_i^\top X_j$ by a [Gram matrix](gram-matrix.qmd) entry.{{cite:hastie_esl2009}} (Ch. 12, §12.2.1, p. 420, Eq. 12.13; §12.3, p. 424)
