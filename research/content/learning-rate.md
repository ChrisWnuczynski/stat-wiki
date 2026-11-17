## Lead context
The learning rate is the step length in a gradient update: it decides how far the weights move along the negative gradient of the training loss.

## Motivating example
The bowl $E(w)=(w-3)^2$ has derivative $2(w-3)$. A step of length $\varepsilon$ from $w$ lands at $w-2\varepsilon(w-3)$, which multiplies the error $w-3$ by $1-2\varepsilon$. From $w=5$ with $\varepsilon=0.1$ the multiplier is $0.8$, and the next four values are $4.6$, $4.28$, $4.024$, and $3.8192$, walking toward $3$. The same start with $\varepsilon=1.1$ multiplies the error by $-1.2$, so the distance to $3$ grows by $20\%$ at every step. The derivative did not change. The step length did.{{cite:hastie_esl2009}} (§11.4, eq. 11.13, p. 396)

## Intuition
Gradient descent replaces a weight by itself minus the learning rate times the partial derivative of the loss. A steep slope and a long step produce the same movement if their product agrees. On a quadratic bowl the safe lengths are visible: the error shrinks when the multiplier has absolute value below $1$, which for $E(w)=(w-3)^2$ is $0<\varepsilon<1$. At $\varepsilon=1$ the multiplier is $-1$ and the iterate oscillates. Above $1$ it diverges.

In a network the same symbol is the $\gamma_r$ in a back-propagation update. A batch step subtracts $\gamma_r$ times the sum of per-case derivatives. An online step uses one training case at a time.{{cite:hastie_esl2009}} (§11.4, eqs. 11.12–11.13, pp. 396–397)

## Definition
For a loss $E$ and a weight $w$, one update is
$$
w\leftarrow w-\varepsilon\frac{\partial E}{\partial w},\qquad \varepsilon>0.
$$
Hastie, Tibshirani and Friedman write the network version, at iteration $r$, as
$$
\beta^{(r+1)}_{km}=\beta^{(r)}_{km}-\gamma_r\sum_{i=1}^{N}\frac{\partial R_i}{\partial\beta^{(r)}_{km}},
$$
and the same pattern for the hidden-layer weights. The positive number $\gamma_r$ is the learning rate. For batch learning it is often held constant. For online learning it should tend to zero.{{cite:hastie_esl2009}} (§11.4–11.5, pp. 396–397)

## Interpretation — Constant steps and decreasing steps
A constant step that is stable on a shallow part of a neural-network loss can be too long near a steep sigmoid. The quadratic calculation makes the threshold obvious because the second derivative is constant. A logistic loss is only locally quadratic, so a single $\varepsilon$ does not carry a global guarantee.

Online updates with a fixed $\varepsilon$ keep jiggling after the weights are near a minimiser, because each case pulls in its own direction. Decreasing $\gamma_r$ damps that noise. The classical sufficient conditions are $\gamma_r\to 0$, $\sum_r\gamma_r=\infty$, and $\sum_r\gamma_r^2<\infty$. The schedule $\gamma_r=1/r$ meets them. A schedule that decays so fast that the sum of steps is finite can stop short of the minimiser.{{cite:hastie_esl2009}} (§11.5, p. 397)

## Properties
The quadratic contraction, and the two series that justify $1/r$, are elementary.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For $E(w)=(w-3)^2$ the update is $w-\varepsilon\cdot 2(w-3)=(1-2\varepsilon)w+6\varepsilon$. The error $e=w-3$ satisfies $e\leftarrow(1-2\varepsilon)e$. Hence $|e|$ shrinks at every step if and only if $|1-2\varepsilon|<1$, that is $0<\varepsilon<1$. At $\varepsilon=1$ the error changes sign and keeps its size. At $\varepsilon=1.1$ the factor is $-1.2$, so the absolute error grows by the factor $1.2$.

For $\gamma_r=1/r$, the partial sums of $\gamma_r$ are the harmonic numbers. The integral test gives $\sum_{r=2}^{N}1/r\ge\int_2^{N+1}\mathrm{d}x/x=\log((N+1)/2)\to\infty$. The squared steps satisfy $\sum_{r=2}^{N}1/r^2\le\int_1^{N}\mathrm{d}x/x^2=1-1/N<1$, so $\sum 1/r^2$ converges. Thus $1/r$ meets the three conditions named above.{{cite:hastie_esl2009}} (§11.5, p. 397)
:::
:::

## Statistical use — Batch, online, and the loss scaling
A factor of $1/2$ in front of a sum of squares is absorbed into $\varepsilon$. Two implementations that disagree about that factor, or about whether the gradient is of the total loss or of the average loss, are using different effective step lengths even when both display the number $0.1$. Confusing the total loss with the average loss rescales the learning rate.

Line search can replace a preset $\gamma_r$ in batch learning by minimising the loss along the gradient direction. That search is still a choice of step length. It is not available, in the same form, for a single noisy online case.{{cite:hastie_esl2009}} (§11.5, p. 397)

## Worked example
Start at $w=5$ with $E(w)=(w-3)^2$ and $\varepsilon=0.1$. The error is $2$ and the multiplier is $0.8$.

$$
\begin{align*}
w_1&=3+0.8\cdot 2=4.6,\\
w_2&=3+0.8\cdot 1.6=4.28,\\
w_3&=3+0.8\cdot 1.28=4.024,\\
w_4&=3+0.8\cdot 1.024=3.8192.
\end{align*}
$$
Four steps cut the error from $2$ to $0.8192$. With $\varepsilon=0.4$ the multiplier is $0.2$, and the same start gives $3.4$, then $3.08$. Two steps leave an error of $0.08$, against $1.28$ after two steps at $\varepsilon=0.1$. The larger stable step is faster on this bowl. It is not a recommendation for a loss whose curvature changes.{{cite:hastie_esl2009}} (§11.4, eq. 11.13)

**Your turn.** From $w=5$ and $\varepsilon=1.1$, compute the next weight and the absolute error. By what factor did the absolute error grow?

::: {.callout-tip collapse="true" title="Answer"}
The multiplier is $1-2\cdot 1.1=-1.2$. The error $2$ becomes $-2.4$, so the next weight is $3-2.4=0.6$. The absolute error grew from $2$ to $2.4$, a factor of $1.2$.
:::

## Common misconceptions
The learning rate is not a property of the data set. It is a choice in the optimiser. Two runs with the same data and different step lengths can converge, oscillate, or diverge.

A step that reduces a full-batch loss need not reduce the loss on the next single case. Online learning with a constant step can wander after the average gradient is already small.

Decreasing the step is not, by itself, a proof of convergence. The sum of the steps has to diverge, or the walk can stall, and the sum of the squared steps has to converge for the usual stochastic-approximation guarantee. A constant step has a divergent sum of squares.

## Assumptions and limits — When the bowl is a poor picture
The exact threshold $0<\varepsilon<1$ belongs to $E(w)=(w-3)^2$, whose second derivative is $2$. A loss with second derivative $L$ along the line of the step shrinks for $0<\varepsilon<2/L$. Using $1$ as a universal cutoff imports the second derivative of this particular bowl.

A non-convex network loss has directions in which the gradient step increases the loss even for a tiny $\varepsilon$, once the current point is at a saddle or the gradient is computed on a batch that does not match the full loss. The quadratic picture is local.

If the inputs are not scaled, a weight on a large input has a large partial derivative and a weight on a small input has a small one. One shared $\varepsilon$ is then long for the first weight and short for the second. Scaling the inputs, or using a separate step for each weight, is a response to that mismatch. It is not implied by writing down $\varepsilon$.

## Connections
Back-propagation is the chain-rule computation of the partial derivatives that the learning rate multiplies. [Gradient descent](gradient-descent.qmd) is the update itself. A [sigmoid function](sigmoid-function.qmd) is one source of curvature that changes with the weights, so a constant step can be stable in one region and unstable in another. Early stopping is a different control on the fit: it limits how many steps are taken, rather than how long each step is.{{cite:hastie_esl2009}} (§11.4–11.5, pp. 396–397)

## Check yourself
### The multiplier
For $E(w)=(w-3)^2$, which constant learning rates make the error shrink at every step?

::: {.callout-tip collapse="true" title="Answer"}
Those with $0<\varepsilon<1$. The absolute value of $1-2\varepsilon$ is then below $1$. At $\varepsilon=1$ the error keeps its size and changes sign.
:::

### Two steps from 5
From $w=5$ with $\varepsilon=0.4$, what are the next two weights?

::: {.callout-tip collapse="true" title="Answer"}
The multiplier is $0.2$. The error $2$ becomes $0.4$, so the first weight is $3.4$. The error $0.4$ becomes $0.08$, so the second weight is $3.08$.
:::

### A finite sum of steps
Why can $\gamma_r=1/r^2$ fail a descent that $\gamma_r=1/r$ is built to finish?

::: {.callout-tip collapse="true" title="Answer"}
The sum $\sum 1/r^2$ converges, so the total distance the updates are allowed to travel is finite. The schedule can stop short of the minimiser. The harmonic schedule $\sum 1/r$ diverges, so the total step length is unlimited, while $\sum 1/r^2$ still converges.
:::

## History
Widrow and Hoff's 1960 delta rule is the name Hastie, Tibshirani and Friedman attach to the two-pass update that back-propagation implements. In that update the learning rate is the factor in front of the gradient. Robbins and Monro's stochastic approximation supplies the decreasing-step conditions $\gamma_r\to 0$, $\sum\gamma_r=\infty$, and $\sum\gamma_r^2<\infty$, with $1/r$ as a schedule that satisfies them.{{cite:hastie_esl2009}} (§11.5, p. 397)
