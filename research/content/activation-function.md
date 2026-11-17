## Motivating example

Suppose a network must classify four combinations of two binary switches, lighting up when exactly one is on. If every hidden unit merely passes on its weighted sum, stacking units still produces one affine score and cannot express the alternating pattern. A nonlinear activation can bend the representation: a unit may be silent below a threshold and respond above it, giving the next layer a feature that the raw inputs did not contain.{{cite:goodfellow_bengio_courville2016}} (Ch. 6, §6.1, pp. 166–171; §6.3, pp. 187–191)

## Intuition

A unit first forms a net input $z=w^\top x+b$, then applies a fixed function $g$ to obtain $h=g(z)$. The weights and bias are learned; the activation rule determines how that learned score is transformed. A step function gives a hard decision, a logistic sigmoid compresses a score into the interval $(0,1)$, and a rectified linear unit (ReLU) returns zero for negative inputs but passes positive inputs through. The three choices express different shapes and transmit different derivatives during training.{{cite:goodfellow_bengio_courville2016}} (Ch. 6, §6.3, pp. 187–191)

The activation is local to a unit; it does not itself assign a probability to every hidden value. A sigmoid output can be interpreted as a Bernoulli probability when fitted with an appropriate probabilistic model and loss, but the same function in a hidden layer is only an intermediate feature. Likewise, a ReLU output of two is an activation value, not a probability. This separation between representation and statistical interpretation avoids reading too much into a unit's numerical output. {{cite:goodfellow_bengio_courville2016}} (Ch. 6, §6.2–6.3, output and hidden units)

## Definition

An activation function $g$ maps a unit's net input $z$ to its output $g(z)$. For the logistic function, $g(z)=1/(1+e^{-z})$; for ReLU, $g(z)=\max(0,z)$. A threshold activation gives zero when $z<0$ and one when $z\geq0$. The logistic function is smooth, while the threshold has a jump and ReLU has a corner at zero. Each form has a useful role, and “nonlinear” by itself does not say whether the resulting network will train effectively.{{cite:goodfellow_bengio_courville2016}} (Ch. 6, §6.3, pp. 187–191){{cite:glorot_bordes_bengio2011}} (§3.1, pp. 317–318, rectifier definition)

## Interpretation — Shape and gradients

The sigmoid derivative is $g'(z)=g(z)\{1-g(z)\}$. It reaches $1/4$ at zero and approaches zero in both tails. Thus a very positive or negative hidden score transmits a small gradient through that unit, even if a downstream error remains. ReLU's derivative is zero for $z<0$ and one for $z>0$; at zero the classical derivative is undefined, and a training implementation must choose a convention for that isolated point. Active ReLUs do not saturate on the positive side, but inactive ones supply no gradient through the activation.{{cite:goodfellow_bengio_courville2016}} (Ch. 6, §6.3.1–6.3.2, pp. 187–191){{cite:glorot_bordes_bengio2011}} (§3.1, pp. 317–318, active paths and hard zeros)

For example, $g(2)\approx0.8808$ and $g'(2)\approx0.1050$; at zero, $g(0)=0.5$ and $g'(0)=0.25$. A weight update passing through a sigmoid unit with score two therefore receives a smaller local derivative than one passing through a unit near zero, all else equal. “Vanishing gradients” in a deep network concern products of several such factors along a computational path, not just one small derivative. Back-propagation makes that chain explicit. {{cite:goodfellow_bengio_courville2016}} (Ch. 6, §6.3.2, saturation; Ch. 6, §6.5, back-propagation)

## Properties

If $g(z)=z$ in every hidden layer, composing the layer maps remains affine: $W_2(W_1x+b_1)+b_2=(W_2W_1)x+(W_2b_1+b_2)$. Extra width or depth alone then cannot create a nonlinear decision boundary. A ReLU network instead partitions the input space according to which units are active. Within one fixed active pattern its output is affine, but crossing a unit's zero boundary changes the formula. This is the precise sense in which a network can be piecewise linear and still be nonlinear overall.{{cite:goodfellow_bengio_courville2016}} (Ch. 6, §6.1 and §6.3.1, nonlinear representation){{cite:glorot_bordes_bengio2011}} (§3.1, p. 318, active subsets and piecewise linearity)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For $g(z)=1/(1+e^{-z})$, differentiation gives $g'(z)=e^{-z}/(1+e^{-z})^2=g(z)\{1-g(z)\}$. Since $0<g(z)<1$, the product is at most $1/4$, with equality at $g(z)=1/2$, or $z=0$. For identity activations, the composition of two affine layers is $(W_2W_1)x+(W_2b_1+b_2)$; induction gives the same form for any number of such layers. A ReLU changes between the two affine rules $0$ and $z$ at zero, so a network containing it need not reduce to one global affine function.{{cite:goodfellow_bengio_courville2016}} (Ch. 6, §6.1 and §6.3, activation and composition)
:::
:::

## Statistical use

The hidden activation is a modelling choice to evaluate with the task and training method. ReLU is often effective because its active-side derivative does not decay as the input grows; Glorot, Bordes and Bengio found sparse representations and useful deep-network performance in their rectifier experiments. This is evidence about tested architectures and datasets, not a universal ranking of activation functions. For a binary response, the output layer often uses a logistic sigmoid with a suitable loss, even when the hidden layers use ReLU. The output link and the hidden feature map serve different purposes.{{cite:goodfellow_bengio_courville2016}} (Ch. 6, §6.2–6.3, output and hidden units){{cite:glorot_bordes_bengio2011}} (§3.1 and §4, pp. 317–322, rectifier properties and experiments)

If every hidden activation is the identity, a stack of layers collapses to one affine map. Tracking sigmoid derivatives from the loss back to a hidden weight shows where a saturated unit shrinks the update. The function's role is that local slope, not a list of activation names.

If every training input to one ReLU stays negative, that unit returns zero and sends no local gradient back through its activation; a different initialisation or an activation with a small negative-side slope may help. If a sigmoid receives an input of $20$, its output is extremely close to one and its derivative is about $2.06\times10^{-9}$, so repeated sigmoid factors can greatly shrink a gradient. If all hidden activations are identity maps, a deeper network remains affine and still misses XOR. The useful choice depends on the data, architecture and training method.{{cite:goodfellow_bengio_courville2016}} (Ch. 6, §6.1 and §6.3.1–6.3.2, inactive and saturated units)
## Worked example

Let $z=2x-1$ for a unit receiving $x=1$. Then $z=1$. The threshold unit outputs one; the sigmoid outputs $g(1)\approx0.7311$; ReLU outputs one. At $x=0$, the same unit has $z=-1$: the threshold and ReLU both output zero, but the sigmoid outputs $g(-1)\approx0.2689$. The equal hard outputs at negative input conceal a training difference: a threshold has zero derivative away from its jump, ReLU has zero derivative on its inactive side, and the sigmoid derivative at $-1$ is approximately $0.1966$. The numerical output and the learning signal answer different questions.{{cite:goodfellow_bengio_courville2016}} (Ch. 6, §6.3.1–6.3.2, activation forms and derivatives)

**Your turn.** For $z=-2$, compute the ReLU output, the logistic sigmoid output to four decimals, and the sigmoid derivative to four decimals. State which of the two units supplies a nonzero local derivative there.

::: {.callout-tip collapse="true" title="Answer"}
ReLU gives $\max(0,-2)=0$ and has derivative zero at this negative input. The sigmoid gives $1/(1+e^2)\approx0.1192$ and derivative $0.1192(1-0.1192)\approx0.1050$. Only the sigmoid passes a nonzero local derivative at $z=-2$.
:::

## Common misconceptions

Nonlinearity is necessary for a multilayer affine-score network to gain expressive power, but it does not guarantee successful training or generalisation. A sigmoid hidden activation is not automatically a calibrated probability. ReLU is not differentiable at zero, yet this isolated corner does not prohibit gradient-based training. Conversely, its active-side derivative of one does not mean gradients can never vanish: inactive ReLUs and other layers can still block a path. These errors concern expressiveness, interpretation and optimisation, respectively.{{cite:goodfellow_bengio_courville2016}} (Ch. 6, §6.1, §6.3 and §6.5)

## Assumptions and limits
A unit's output is not automatically a probability. A hidden activation is a feature, and some activations, such as ReLU, are unbounded above.{{cite:goodfellow_bengio_courville2016}} (Ch. 6, §6.3, pp. 187–191)

## Connections

An [artificial neuron](artificial-neuron.qmd) combines a weighted sum with an activation. [Hidden layers](hidden-layer.qmd) use nonlinear outputs as features for later units. [The XOR problem](xor-problem.qmd) shows why affine composition alone is insufficient. [Backpropagation](backpropagation-batch-form.qmd) multiplies derivatives through these functions, while the [sigmoid function](sigmoid-function.qmd) is one smooth choice for an output or hidden unit. The [perceptron](perceptron.qmd) uses a hard threshold, which is useful as a decision rule but not as an ordinary smooth training path.{{cite:goodfellow_bengio_courville2016}} (Ch. 6, §6.1–6.5)

## History

Threshold units appear in the early formal neuron model of McCulloch and Pitts. Later multilayer work used smooth nonlinear units so that derivatives could guide changes to hidden weights; Rumelhart, Hinton and Williams made back-propagation of errors a practical account of learning internal representations. Rectifier research then showed that a kinked, partly linear activation can train useful deep networks and yield sparse hidden representations. This sequence tracks changes in how hidden features were represented and learned, rather than a single invention of “the” activation function.{{cite:mehlig_neural_networks2022}} (§1.2, pp. 7–8, early threshold neuron){{cite:rumelhart_hinton_williams1986}} (pp. 533–536, hidden representations){{cite:glorot_bordes_bengio2011}} (§1 and §3–4, pp. 315–322, rectifier motivation and experiments)
