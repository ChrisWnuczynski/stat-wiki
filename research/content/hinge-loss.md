## Lead context
Hinge loss charges nothing once a labelled point sits on the correct side of the margin, and charges the shortfall when it does not.

## Motivating example
Margins $1.4$, $0.25$ and $-0.5$ have hinges $0$, $0.75$ and $1.5$. The total is $2.25$. A point past the margin contributes nothing; a point on the wrong side of the score contributes more than $1$.

## Intuition — A flat region on the correct side
Write the margin of a labelled point as $y f(x)$, with $y\in\{-1,+1\}$ and $f(x)$ the real-valued score. The hinge is $[1-yf(x)]_+$, the positive part of $1-yf(x)$. Past margin $1$ the loss is exactly zero, so a point that is already correctly classified and far from the boundary does not pull the fit. Squared error has no such flat region: a correct point with a large score still contributes a residual.{{cite:hastie_esl2009}} (§12.3.2, pp. 426–427, hinge and squared error)

## Definition — Positive part of the margin shortfall
For labels $y_i\in\{-1,+1\}$ and a score $f(x)=h(x)^\top\beta+\beta_0$, the support-vector criterion is
$$
\sum_{i=1}^{N}[1-y_i f(x_i)]_++\frac\lambda2\lVert\beta\rVert^2.
$$
The first term is the total hinge loss. The second is a ridge penalty on the slope, with $\lambda>0$. At the population level, for a fixed $x$, the hinge is minimised by $f(x)=\operatorname{sign}\{\Pr(Y=+1\mid x)-1/2\}$, the more probable label.{{cite:hastie_esl2009}} (§12.3.2, pp. 426–427, criterion and population minimiser)

## Properties — A maximum of two linear pieces
As a function of the margin $m=yf(x)$, the hinge equals $0$ when $m\ge 1$ and equals $1-m$ when $m<1$. It is convex, because it is the maximum of the constant $0$ and the linear function $1-m$. It is not differentiable at $m=1$: the slope is $-1$ to the left of the kink and $0$ to the right.{{cite:hastie_esl2009}} (§12.3.2, p. 426, the hinge)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
By definition $[1-m]_+=\max\{0,1-m\}$. The maximum of two convex functions is convex, and both $0$ and $1-m$ are convex, so the hinge is convex in $m$. For $m>1$ the maximum is $0$, so the derivative in $m$ is $0$. For $m<1$ the maximum is $1-m$, so the derivative is $-1$. At $m=1$ every slope between $-1$ and $0$ is a subgradient.{{cite:hastie_esl2009}} (§12.3.2, p. 426)
:::
:::

## Worked example
Three margins $1.4$, $0.25$ and $-0.5$ have hinges $0$, $0.75$ and $1.5$. The total hinge is $2.25$. The first point is beyond the margin and contributes nothing. The third point is on the wrong side of the score, so its hinge exceeds $1$. A squared-error fit of a label $+1$ with score $4$ would still charge $(1-4)^2=9$, while the hinge at margin $4$ is $0$.{{cite:hastie_esl2009}} (§12.3.2, pp. 426–427)

**Your turn.** Find the hinges at margins $1$ and $-2$, and their sum.

::: {.callout-tip collapse="true" title="Answer"}
The hinge at margin $1$ is $0$. The hinge at margin $-2$ is $1-(-2)=3$. The sum is $3$. The kink itself is not charged.
:::

## Connections
The hinge is the loss that the soft-margin support-vector classifier minimises together with a penalty on the weight. Binomial deviance, the loss behind logistic regression, keeps falling as the margin grows, so it never has this exact flat region. A population hinge chooses the more probable class, whereas squared error targets a linear function of the class probability.{{cite:hastie_esl2009}} (§12.3.2, p. 427, population minimisers)

## Check yourself
**1.** What is the hinge at margin $0.2$, and what is the slope of the hinge, as a function of the margin, just to the left of $1$?

::: {.callout-tip collapse="true" title="Answer"}
The hinge is $1-0.2=0.8$. Just to the left of $1$ the slope in the margin is $-1$.
:::

**2.** In the criterion above, take $\lambda=2$ and $\lVert\beta\rVert=1$, and add the penalty to the worked total hinge of $2.25$. What is the criterion value?

::: {.callout-tip collapse="true" title="Answer"}
The penalty is $(2/2)(1)=1$. The criterion value is $2.25+1=3.25$. A larger $\lambda$ charges the same weight more heavily and tolerates more hinge.
:::
