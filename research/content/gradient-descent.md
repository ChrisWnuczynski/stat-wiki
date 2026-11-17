## Motivating example

A neural network has many weights, and its training loss changes whenever they change. Solving simultaneously for the exact best values is usually impractical. Gradient descent instead asks which small movement of the current weights most rapidly lowers the loss, then repeats that movement after recalculating the gradient. The update is simple; whether it helps depends on the step size and the shape of the objective.{{cite:goodfellow_bengio_courville2016}} (Ch. 4 §4.3, pp. 82–84; Ch. 8, introduction)

## Definition

For a differentiable objective $E(w)$ with a vector of weights $w$, **gradient descent** iterates $w_{t+1}=w_t-\varepsilon_t\nabla E(w_t)$ for a positive learning rate $\varepsilon_t$. Each component of the gradient measures local change in loss from moving that weight while the others are fixed; the vector update changes all weights using derivatives at the *same old* parameter vector. For a training loss averaged over examples, **batch** gradient descent evaluates the whole training-set gradient at each step. One pass over all examples is an epoch; a step may be an epoch or part of one, depending on the algorithm.{{cite:goodfellow_bengio_courville2016}} (Ch. 4 §4.3, update; Ch. 8 §§8.1.3, 8.3.1, batch and minibatch)

In network training one might initialize weights randomly, for example in $[-0.5,0.5]$, to break symmetry among identical hidden units. This is a network-design choice, not a condition for the mathematical gradient step; convex problems can start deterministically. The value $0.1$ is one possible learning rate, not a universal prescription. Stop according to an appropriate criterion such as a validation objective, a step or gradient tolerance, or a computation budget. A small training gradient alone does not certify good predictive performance. {{cite:goodfellow_bengio_courville2016}} (Ch. 8 §§8.1.2, 8.2 and 8.3, stopping and initialization)

## Intuition — Why the direction works

For a unit direction $u$, the instantaneous slope is $u^{\mathsf T}\nabla E(w)$. Cauchy–Schwarz makes this smallest at $u=-\nabla E(w)/\|\nabla E(w)\|$ when the gradient is nonzero. Thus negative gradient is steepest *locally in Euclidean distance*. A finite update needs more than this first-order statement: if the rate is too large, the step can cross a valley and increase the loss. A line search evaluates candidate rates along the direction; a second-order method uses curvature through a Hessian, with extra computation and different assumptions.{{cite:goodfellow_bengio_courville2016}} (Ch. 4 §4.3, pp. 82–85, steepest direction and line search)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Differentiability gives $E(w+h)=E(w)+\nabla E(w)^{\mathsf T}h+o(\|h\|)$. For a unit $u$, $\nabla E(w)^{\mathsf T}u\ge-\|\nabla E(w)\|$, with equality when $u$ is opposite the nonzero gradient. Setting $h=-\varepsilon\nabla E(w)$ makes the linear change $-\varepsilon\|\nabla E(w)\|^2$, so sufficiently small positive $\varepsilon$ lowers $E$. If the gradient is $L$-Lipschitz, integrating it along the segment yields the stronger inequality $E(w-\varepsilon g)\le E(w)-\varepsilon(1-L\varepsilon/2)\|g\|^2$ for $g=\nabla E(w)$; hence every $0<\varepsilon<2/L$ decreases loss unless $g=0$. This does not identify the type of stationary point.{{cite:goodfellow_bengio_courville2016}} (Ch. 4 §4.3, pp. 82–85, local descent and curvature)

For $E(w)=(w-3)^2$, $g=2(w-3)$ and the error relative to the minimizer obeys $w_{t+1}-3=(1-2\varepsilon)(w_t-3)$. It contracts exactly when $0<\varepsilon<1$, stays constant in magnitude at $\varepsilon=1$, and diverges for $\varepsilon>1$. For $E(w)=n^{-1}\sum_i\ell_i(w)$, a uniformly sampled minibatch $B$ of size $b$ has $\mathbb E_B[b^{-1}\sum_{i\in B}\nabla\ell_i(w)\mid w]=\nabla E(w)$ by linearity; unbiasedness alone does not make every noisy step descend. {{cite:goodfellow_bengio_courville2016}} (Ch. 8 §§8.1.3, 8.3.1, minibatch gradients)
:::
:::

## Worked example

Take $E(w)=(w-3)^2$ and start at $w_0=0$, where $E=9$ and $E'(0)=-6$. With $\varepsilon=0.1$, the first update is $w_1=0-0.1(-6)=0.6$ and $E(w_1)=5.76$. The next derivative is $-4.8$, so $w_2=0.6-0.1(-4.8)=1.08$ and $E(w_2)=3.6864$. Each step closes one fifth of the remaining distance to $3$. A rate of $1.1$ would instead send $w_0$ to $6.6$, increasing loss from $9$ to $12.96$; a correct direction is not enough when the step overshoots.{{cite:goodfellow_bengio_courville2016}} (Ch. 4 §4.3, gradient step and rate selection)

**Your turn.** Starting from $w_0=0$ for the same objective, use $\varepsilon=0.5$. Find $w_1$ and the new loss. What happens with $\varepsilon=1$ instead?

::: {.callout-tip collapse="true" title="Answer"}
At rate $0.5$, $w_1=0-0.5(-6)=3$ and $E(w_1)=0$: this quadratic reaches its minimizer in one step. At rate $1$, the update gives $w_1=6$ and loss $9$; subsequent steps alternate between $0$ and $6$, so the loss never falls. The example shows why “positive learning rate” alone is insufficient.
:::

## Statistical use — Practical variants and checks

A random minibatch replaces the full gradient with an average over selected examples. Under uniform sampling it is unbiased at fixed weights, but its variance can produce an uphill step; the learning-rate schedule and batch size affect the trajectory. Momentum adds a weighted memory of earlier directions and can help traverse narrow valleys, though it does not guarantee escape from every plateau or poor basin. Backpropagation supplies the network gradient efficiently through the chain rule; gradient descent specifies how to *use* it. The XOR runs below illustrate that exact derivatives and a finite step can still fail to produce immediate descent.{{cite:goodfellow_bengio_courville2016}} (Ch. 8 §§8.1.3, 8.2, 8.3.1–8.3.2)

A useful implementation check is the centred finite difference $[E(w+\delta)-E(w-\delta)]/(2\delta)$ for one weight at a time. At $w=0$ in the example, $\delta=0.01$ gives $(2.99^2-3.01^2)/0.02=-6$, matching the analytic derivative. Too large a perturbation introduces approximation error; too small a perturbation magnifies floating-point cancellation. Numerical differentiation is a diagnostic for a gradient implementation, not an efficient training method. {{cite:stanford_cs231n_training}} ("Gradient Checks", centred formula and numerical precision)

On the quadratic above, a rate of $1.1$ makes loss increase and iterates diverge despite a smooth convex objective. At $w=0$ for $E(w)=1-w^2$, the gradient is zero but that point is a maximum, so the method does not move. For a flat saturated neural-network unit, gradients can be so small that progress is negligible. In a narrow curved valley, one global rate can be safe across the steep direction yet slow along the shallow one. None of these difficulties disappears merely because gradients were computed exactly.{{cite:goodfellow_bengio_courville2016}} (Ch. 4 §4.3; Ch. 8 §8.2, critical points and conditioning)
## Common misconceptions

The gradient points toward a local first-order rise, so *minus* its direction is used for minimization; changing the sign performs ascent. A descent direction does not guarantee that every finite update lowers loss. A zero gradient can mark a saddle or maximum as well as a minimum. A lower training loss does not imply lower future prediction error. And an unbiased minibatch gradient does not mean each minibatch gradient points downhill for the full objective.{{cite:goodfellow_bengio_courville2016}} (Ch. 4 §4.3; Ch. 8 §§8.1, 8.2 and 8.3)

## Connections

Backpropagation computes derivatives of a composed network loss; gradient descent turns them into a parameter update. Stochastic gradient descent and minibatches trade full-gradient accuracy for cheaper steps. Early stopping uses predictive assessment to decide when to stop training, while a line search chooses a local step length from objective evaluations. The method also appears in regression and numerical equation solving, beyond neural networks.{{cite:goodfellow_bengio_courville2016}} (Ch. 4 §4.3 and Ch. 8 §§8.1–8.3)

## History

Cauchy described negative-gradient steps in 1847 while seeking solutions to simultaneous equations arising from astronomical calculations; his presentation also considered changing the step length along that direction. Modern neural-network training applies the same local idea to an empirical loss, with backpropagation supplying the many partial derivatives and stochastic variants using only part of the data per step.{{cite:lemarechal2012_cauchy}} (pp. 251–253, translation and analysis of Cauchy 1847){{cite:goodfellow_bengio_courville2016}} (Ch. 8 §§8.1.3, 8.3.1)
