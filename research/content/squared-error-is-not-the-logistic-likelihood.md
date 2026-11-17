## Motivating example — A confidently wrong prediction can have a tiny square-loss gradient
Suppose a binary label is one but a sigmoid output is close to zero. Squared error recognises a large probability error, yet its gradient with respect to the logit can be tiny because the sigmoid has saturated. Bernoulli negative log-likelihood has a different derivative: the same sigmoid factor cancels. The loss and output transformation must be analysed together.{{cite:goodfellow_bengio_courville2016}} (§6.2.2.2, sigmoid units for Bernoulli outputs)

## Statement
Let $z=w^\top x$, $o=\sigma(z)=1/(1+e^{-z})$ and $y\in\{0,1\}$. Define half squared error $L_S=\tfrac12(o-y)^2$ and Bernoulli negative log-likelihood $L_B=-y\log o-(1-y)\log(1-o)$. Then
$$\nabla_wL_S=(o-y)o(1-o)x,\qquad\nabla_wL_B=(o-y)x.$$
Without the factor $1/2$ in the square loss, its gradient doubles. The score is the gradient of the positive log-likelihood, so it has the opposite sign from the negative-log-likelihood gradient.{{cite:zhang_d2l2023}} (§4.1, cross-entropy loss and its derivatives){{cite:goodfellow_bengio_courville2016}} (§6.2.1.1, maximum-likelihood costs)

## Proof
The derivative of the sigmoid is $do/dz=o(1-o)$. The chain rule therefore gives $dL_S/dz=(o-y)o(1-o)$. For Bernoulli loss,
$$\frac{dL_B}{do}=-\frac y o+\frac{1-y}{1-o}=\frac{o-y}{o(1-o)}.$$
Multiplying by $do/dz$ cancels its denominator. Finally $\nabla_wz=x$, giving the two displayed vector formulas. The cancellation is algebraic and is valid for finite logits, where $0<o<1$.{{cite:goodfellow_bengio_courville2016}} (§6.2.2.2, Bernoulli cross-entropy and sigmoid)

## Key results — Convexity also depends on the chosen parameterisation
For a linear logit, Bernoulli loss has second derivative $d^2L_B/dz^2=o(1-o)>0$. Its weight Hessian is $o(1-o)xx^\top$, positive semidefinite, and summing cases preserves convexity. For half squared error,
$$\frac{d^2L_S}{dz^2}=[o(1-o)]^2+(o-y)o(1-o)(1-2o),$$
which can be negative. A convex function of the output probability need not remain convex after the nonlinear sigmoid transformation. Hidden layers introduce further nonlinear parameters even with Bernoulli loss, so the linear-logit convexity conclusion does not imply a convex neural-network problem.{{cite:zhang_d2l2023}} (§4.1, likelihood and gradient){{cite:goodfellow_bengio_courville2016}} (§6.2, gradient-based learning)

## Worked example — Compare losses at both ends of the sigmoid
For $y=1$, $x=1$ and output $o=0.01$, the Bernoulli gradient is $-0.990000$ whereas the half-square gradient is $-0.009801$. The unhalved-square gradient is $-0.019602$. The Bernoulli loss is $4.605170$ and the half-square loss is $0.490050$. A small gradient here is not evidence that the prediction is close to the observed label.

At $o=0.9$ with the same label, the Bernoulli gradient is $-0.100000$ and the unhalved-square gradient is $-0.018000$, agreeing with the extra factor $2o(1-o)=0.180000$. Near correct saturation both gradients become small because the prediction error is small; near incorrect saturation the extra sigmoid factor suppresses the square-loss update despite a large error.{{cite:goodfellow_bengio_courville2016}} (§6.2.2.2, saturation and loss choice)

**Your turn.** Change the label to zero while holding $o=0.99$ and $x=1$. Give the Bernoulli and half-square gradients.

::: {.callout-tip collapse="true" title="Answer"}
The gradients are $0.990000$ and $0.009801$. Gradient descent subtracts either gradient, reducing the logit and hence reducing the probability of label one.
:::

## Statistical use — Different optimisation losses can share a population target
For a fixed input, let the actual success probability be $p\in(0,1)$. Expected squared error is $p(1-o)^2+(1-p)o^2=p(1-p)+(o-p)^2$, so its unique probability-scale minimiser is $o=p$. Expected Bernoulli loss is also minimised at $o=p$, as differentiation gives $(o-p)/\{o(1-o)\}$. Thus different sample objectives and gradients can agree on an unconstrained population probability target. This does not make their finite-sample estimates or optimisation paths identical under a restricted model.{{cite:goodfellow_bengio_courville2016}} (§6.2.1.2, learning conditional statistics)

The loss convention also affects numerical step sizes: multiplying a loss by a constant multiplies its gradient and can be offset by a reciprocal learning-rate change for ordinary gradient descent. The observation-dependent factor $o(1-o)$ cannot be removed by one fixed rescaling across cases. A well-defined comparison states both the loss normalisation and the optimisation update, then evaluates calibration or predictive performance on the intended target.
