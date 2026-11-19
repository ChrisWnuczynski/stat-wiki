## Lead context
The rule changes a linear threshold only when a labelled observation violates its classification condition.

## Motivating example
A classifier must label points as they arrive. Solving a new optimisation problem after every error may be expensive. The perceptron uses a small correction in the direction of the misclassified point, allowing successive observations to alter one separating hyperplane. Its finite convergence guarantee depends on linear separability.{{cite:shalev_bendavid2014}} (§9.1.2, pp. 92–93)

## Definition — Correcting a threshold and its intercept
For binary labels $y\in\{0,1\}$, let $\widehat y=f(b+w^\top x)$ with $f(z)=\mathbf1\{z\ge0\}$. On a mistake, use
$$
w\leftarrow w+\eta(y-\widehat y)x,\qquad b\leftarrow b+\eta(y-\widehat y),\qquad\eta>0.
$$
A missed positive adds the input; a false positive subtracts it. Appending a constant coordinate $1$ to $x$ treats the intercept as another weight. A tie convention is part of the classifier and must be used consistently when detecting mistakes.{{cite:shalev_bendavid2014}} (§9.1.2, p. 92)

With labels $t\in\{-1,+1\}$ and augmented vector $z$, the zero-start, unit-step version updates $v\leftarrow v+t z$ whenever $t v^\top z\le0$. This version demands a strictly positive signed training score at termination. The preceding $0/1$ convention permits correctly classified positive points on the boundary; its actual mistakes are still a subset of observations satisfying nonpositive signed score.{{cite:shalev_bendavid2014}} (§9.1.2, batch perceptron algorithm)

## Properties — The margin bounds the corrections
Suppose the finite augmented sample has $\|z_i\|\le R$ and a unit vector $u$ satisfies $t_i u^\top z_i\ge\gamma>0$. Start at $v_0=0$ and update only at nonpositive signed scores. After $M$ corrections,
$$
u^\top v_M=\sum_{m=1}^M t_{i_m}u^\top z_{i_m}\ge M\gamma.
$$
For each correction,
$$
\|v_{m+1}\|^2=\|v_m\|^2+2t_i v_m^\top z_i+\|z_i\|^2\le\|v_m\|^2+R^2.
$$
Thus $\|v_M\|\le R\sqrt M$. Cauchy–Schwarz implies $M\gamma\le R\sqrt M$, so $M\le(R/\gamma)^2$. This proves a finite bound for zero initial weights under the stated margin assumption. A pass must actually inspect every observation before declaring that none violates the stopping rule.{{cite:shalev_bendavid2014}} (§9.1.2, Thm. 9.1, pp. 92–93){{cite:boyd_vandenberghe2004}} (§A.1.1, inner products)

For a finite nonzero initial vector $v_0$, the same argument gives $u^\top v_M\ge u^\top v_0+M\gamma$ and $\|v_M\|^2\le\|v_0\|^2+MR^2$. Their Cauchy–Schwarz bounds cannot both hold for arbitrarily large $M$, since the projection grows linearly and the norm bound only as a square root. Thus a finite start also gives finite corrections under the same strict separability assumption; the simple displayed bound $(R/\gamma)^2$ specifically uses a zero start.

The guarantee concerns finding a training separator, not the best margin or the smallest population error. The update order can change the resulting separator. A very small margin can make the bound large, and nonseparable data can produce continuing corrections.{{cite:shalev_bendavid2014}} (§9.1.2, Rmk. 9.1, p. 93)

## Assumptions and limits — Learning cannot enlarge a halfspace
Every fitted single threshold still separates by one affine hyperplane. XOR labels on the four corners of a square cannot be represented by that hypothesis class, regardless of update count. A nonlinear feature map or hidden nonlinear layer changes the representational question; it is separate from choosing the learning rate for one unit.{{cite:goodfellow_bengio_courville2016}} (§6.1, pp. 167–170)

## Worked example
Train the $0/1$ rule on $(0,0)\mapsto0$, $(1,0)\mapsto1$, $(0,1)\mapsto1$, cycling in that order with $w=(0,0)$, $b=0$ and $\eta=1$. The five mistaken presentations produce the states
$$
(0,0;-1),\quad(1,0;0),\quad(1,0;-1),\quad(1,1;0),\quad(1,1;-1),
$$
where the semicolon separates the intercept. Their signed input scores before correction are respectively $0,-1,0,-1,0$. At the final state, scores on the three points are $-1,0,0$, giving the desired labels under $f(0)=1$. A subsequent complete pass makes no corrections.{{cite:shalev_bendavid2014}} (§9.1.2, p. 92)

This boundary convention gives a separator with two training points on the boundary. If the stricter signed-margin stopping rule is used, further corrections may occur; changing the stopping rule changes the trace. Both conventions fit in the margin argument when their corrections have nonpositive signed score.

**Your turn.** Does $(w_1,w_2;b)=(1,1;-1/2)$ classify the same three points? Are its positive scores strictly positive?

::: {.callout-tip collapse="true" title="Answer"}
The scores are $-1/2,1/2,1/2$, so the labels are $(0,1,1)$ and all signed margins are strictly positive. Separability of these data does not require a training point on the decision boundary.
:::
