## Lead context
The logistic sigmoid turns an unrestricted score into a smooth value between zero and one, making it useful for binary probabilities and trainable neural units.{{cite:bishop2006}} (Ch. 4, §4.3.2; Ch. 5, §5.1)

## Motivating example
Imagine a binary classifier that assigns a score $z=-1+2x$ from one measured feature $x$. At $x=0$ its sigmoid output is about $0.269$, whereas at $x=1$ it is about $0.731$. The score has moved by two units, but the output has moved on a bounded probability scale. If the model is a Bernoulli logistic regression, the corresponding odds have been multiplied by $e^2\approx7.389$. A hard threshold would instead report only zero or one at these points and would give no gradient with which to adjust its coefficients.{{cite:bishop2006}} (Ch. 4, §4.3.2; Ch. 5, §5.1)

## Intuition
The sigmoid is steepest where the score is near zero, the region in which the two outcomes compete most closely. Far to either side it flattens: further evidence changes the output less. This shape makes the same function suitable as a soft version of a step and as the inverse of the log-odds transformation. Its bounded output can represent a probability in a specified statistical model; the shape of the function by itself does not establish that a fitted model is calibrated.{{cite:bishop2006}} (Ch. 4, §4.3.2, Eqs. 4.57–4.61; Ch. 5, §5.1)

## Definition
In this article *sigmoid* means the logistic sigmoid $g:\mathbb R\to(0,1)$, $g(z)=1/(1+e^{-z})$. “Sigmoidal” more generally describes an S-shaped curve, so it need not mean this precise formula. The logistic curve is strictly increasing, approaches zero as $z\to-\infty$ and one as $z\to+\infty$, and never attains either endpoint at a finite score. A threshold at zero, displayed below from the neural-units chapter, has those endpoints as its only outputs and jumps at the origin.{{cite:bishop2006}} (Ch. 4, §4.3.2, Eqs. 4.57–4.61; Ch. 5, §5.1)

## Properties
The center is $g(0)=1/2$, and symmetry gives $g(-z)=1-g(z)$. Differentiation yields $g'(z)=g(z)\{1-g(z)\}$: the derivative is positive but no greater than $1/4$, attaining that maximum at $z=0$. Thus a large change in score can give only a small output change in either tail. The calculation at $z=2$ makes the flattening visible. On $0<p<1$, the inverse is the logit $g^{-1}(p)=\log\{p/(1-p)\}$; a unit increase in the score multiplies the odds by $e$.{{cite:bishop2006}} (Ch. 4, §4.3.2, Eqs. 4.57–4.61; Ch. 5, §5.1)

For a binary target $y\in\{0,1\}$ and output $o=g(z)$, Bernoulli negative log-likelihood is $L=-y\log o-(1-y)\log(1-o)$. Its derivative with respect to the score is $o-y$. The sigmoid derivative cancels the reciprocal factors from the logarithms; this does not mean the sigmoid has no derivative. Under half squared error, $L=\tfrac12(o-y)^2$, the derivative is instead $(o-y)o(1-o)$. A confidently wrong output can therefore have a tiny score gradient under squared error, as the saturation question illustrates.{{cite:bishop2006}} (Ch. 4, §4.3.2, Eq. 4.88; Ch. 5, §5.2)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write $u=e^{-z}>0$. Then $g(z)=(1+u)^{-1}$ and $u'=-u$, so $g'(z)=u/(1+u)^2=g(z)\{1-g(z)\}>0$. Since $p(1-p)=1/4-(p-1/2)^2\leq1/4$ for $0<p<1$, the maximum occurs when $p=g(z)=1/2$, or $z=0$. Direct substitution gives $g(-z)=e^{-z}/(1+e^{-z})=1-g(z)$. Solving $p=1/(1+e^{-z})$ gives $e^z=p/(1-p)$ and the inverse-logit formula. The limits follow by taking $e^{-z}$ to infinity and zero respectively.{{cite:bishop2006}} (Ch. 4, §4.3.2, Eqs. 4.57–4.61)

For $0<o<1$, $dL/do=-y/o+(1-y)/(1-o)$. Multiplying by $do/dz=o(1-o)$ gives $dL/dz=-y(1-o)+(1-y)o=o-y$. With $L=\tfrac12(o-y)^2$, the same chain rule gives $(o-y)o(1-o)$. If $z=w^\top x+b$, another application gives $\nabla_wL=(o-y)x$ for Bernoulli loss.{{cite:bishop2006}} (Ch. 4, §4.3.2, Eq. 4.88; Ch. 5, §5.2)
:::
:::

## Statistical use — Logistic scores in models
In binary logistic regression, the score $w^\top x+b$ is a linear predictor for log odds and the sigmoid converts it to the Bernoulli success probability. Its coefficient scale is therefore multiplicative on the odds scale, not additive on the probability scale. Reading $g(z)$ as a success probability requires a binary outcome model and an interpretation of $z$ as its log odds; if the fitted score is wrong, an exactly calculated output can still be misleading. The one-layer interpretation below carries this into a neural-network setting. With hidden layers, sigmoid activations transform intermediate scores; those intermediate values are not automatically probabilities of observed events. Backpropagation multiplies local derivatives across layers, so repeated saturated sigmoid factors can make gradients small.{{cite:bishop2006}} (Ch. 4, §4.3.2; Ch. 5, §§5.1–5.2){{cite:rumelhart_hinton_williams1986}} (pp. 533–534)

## Worked example
Take $z=-1+2x$. At $x=0$, $z=-1$, $o=g(-1)=0.268941$ and $g'(-1)=o(1-o)=0.196612$. At $x=1$, $z=1$, $o=0.731059$ and $g'(1)$ is again $0.196612$ by symmetry. The change in log odds is $2$, corresponding to an odds ratio $e^2=7.389056$. If the observed target at $x=0$ is $y=1$, the Bernoulli score gradient is $o-y=-0.731059$; half squared error gives $(o-y)o(1-o)=-0.143735$. A negative gradient asks gradient descent to raise the score. These gradients differ because the losses differ, although the output function is identical.{{cite:bishop2006}} (Ch. 4, §4.3.2, Eq. 4.88; Ch. 5, §5.2)

**Your turn.** Suppose a unit has score $z=\log 3$ and target $y=1$. Find its output, its derivative with respect to the score, and the score gradients for Bernoulli loss and half squared error.{{cite:bishop2006}} (Ch. 4, §4.3.2, Eq. 4.88)

::: {.callout-tip collapse="true" title="Answer"}
Because $e^z=3$, the odds are $3:1$, so $o=g(z)=3/4=0.75$ and $g'(z)=(3/4)(1/4)=3/16=0.1875$. Bernoulli loss gives $dL/dz=o-y=-1/4=-0.25$. Half squared error gives $(o-y)o(1-o)=(-1/4)(3/16)=-3/64=-0.046875$. Both call for increasing the score, but the squared-error gradient is smaller.{{cite:bishop2006}} (Ch. 4, §4.3.2, Eq. 4.88)
:::

## Common misconceptions
A sigmoid output is not automatically a well-calibrated probability: a classifier that predicts $0.9$ for every case while successes occur only half the time is badly calibrated, however smooth its final activation. Saturation does not mean that a confidently wrong example has little error; it means the output changes little with the score, which can suppress a squared-error gradient. Finally, a sigmoid hidden unit is not a logistic regression on the original features: the latter has one sigmoid applied directly to a linear predictor, whereas a network composes transformations before its final output.{{cite:bishop2006}} (Ch. 4, §4.3.2; Ch. 5, §§5.1–5.2)

## Assumptions and limits — Saturation and vanishing gradients
For $z=-8$ and target $y=1$, the saturation example gives $o\approx0.000335$ and a no-half squared-error gradient near $-0.000670$, despite an error near one; Bernoulli loss gives a score gradient near $-0.999665$. Large sigmoid networks can suffer the same local flattening repeatedly in their hidden layers. A hard threshold has a different failure: its derivative is zero away from its jump, so ordinary gradient descent cannot tune it through that derivative.{{cite:bishop2006}} (Ch. 4, §4.3.2; Ch. 5, §§5.1–5.2){{cite:rumelhart_hinton_williams1986}} (pp. 533–534)

## Connections
The [logit link](logit-link.qmd) takes probabilities back to the score scale. [Binary logistic regression](binary-logistic-regression.qmd) uses one sigmoid as a mean function; [artificial neurons](artificial-neuron.qmd) and [hidden layers](hidden-layer.qmd) use it as an activation. [Cross-entropy](cross-entropy.qmd) is the Bernoulli loss whose score gradient simplifies to $o-y$. The [perceptron](perceptron.qmd) instead uses a threshold decision.{{cite:bishop2006}} (Ch. 4, §4.3.2; Ch. 5, §§5.1–5.2)

## History
McCulloch and Pitts described idealized neural events as “all-or-none” in their 1943 logical model, a historical starting point for threshold units. The 1986 account by Rumelhart, Hinton and Williams used differentiable units and propagated error derivatives backward to learn internal representations. The logistic sigmoid supplied a smooth activation with a particularly simple derivative; their paper did not invent the logistic curve, and its statistical log-odds role is distinct from the biological idealization.{{cite:mcculloch_pitts1943}} (p. 115, neural threshold model){{cite:rumelhart_hinton_williams1986}} (pp. 533–534){{cite:bishop2006}} (Ch. 4, §4.3.2; Ch. 5, §5.1)
