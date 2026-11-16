## Motivating example

A large neural network can drive training error down by fitting accidental patterns in a small sample. A squared-weight penalty makes that fit pay a cost for large connections, so the optimizer balances fit against coefficient size. The result may predict better on new observations when the training targets contain noise, as Krogh and Hertz demonstrated in a linear-network analysis and a NETtalk experiment. The penalty strength must still be selected for the task; shrinking everything is not a guarantee of generalization.{{cite:krogh_hertz1992}} (§§1, 4–6, pp. 951–956)

## Intuition

Without a penalty, an optimizer can move freely along directions where the training loss changes little. Weight decay pulls such directions toward zero. Directions that sharply improve the fit resist that pull more strongly. In a local quadratic approximation, the shrinkage is therefore larger along low-curvature directions, a useful way to understand why regularization can reduce variance. This picture depends on the parameterization: scaling an input by ten and dividing its weight by ten leaves predictions unchanged but changes the squared-weight penalty by a factor of one hundred for that connection.{{cite:goodfellow_bengio_courville2016}} (Ch. 7, §7.1.1, pp. 226–229, eqs. 7.8–7.13)

## Definition — Penalty and update

For differentiable training loss $E(w)$ and strength $\lambda>0$, an $L^2$-penalized objective is $E(w)+(\lambda/2)\lVert w\rVert_2^2$. In ordinary gradient descent with step size $\varepsilon$, its update is $w_{t+1}=w_t-\varepsilon\nabla E(w_t)-\varepsilon\lambda w_t$. Thus each step first shrinks the current weight by $1-\varepsilon\lambda$ and then applies the loss gradient. Bias parameters are often left unpenalized, so the precise set of coefficients being shrunk should be stated.{{cite:krogh_hertz1992}} (§1, p. 951, eqs. 1–2){{cite:goodfellow_bengio_courville2016}} (Ch. 7, §7.1.1, pp. 226–227, eqs. 7.2–7.5)

## Properties — Equivalence has an optimizer condition

For plain gradient descent or SGD with a common scalar learning rate, adding the quadratic penalty and applying an independent decay step can be made algebraically identical when their coefficients are scaled consistently. If an adaptive optimizer premultiplies gradients by a coordinate-dependent matrix, however, it also premultiplies the penalty gradient when that gradient is included in the loss. A separate decay step shrinks weights directly. Loshchilov and Hutter formalized the equivalence for ordinary SGD and the inequivalence for adaptive gradients; names such as “weight decay” and “$L^2$ regularization” therefore need the optimizer context.{{cite:loshchilov_hutter2019}} (§2, Propositions 1–2; Appendix A, eqs. 5–8)

::: {.callout-note collapse="true" title="Proof"}
Differentiating $(\lambda/2)\lVert w\rVert^2$ gives $\lambda w$. A plain gradient step on the penalized objective is $w^+=w-\varepsilon\{\nabla E(w)+\lambda w\}=(1-\varepsilon\lambda)w-\varepsilon\nabla E(w)$, the same as a decay factor $1-\varepsilon\lambda$ applied outside the loss gradient. With an adaptive preconditioner $M$ the penalized step is $w^+=w-\varepsilon M\nabla E(w)-\varepsilon\lambda Mw$, whereas separate decay gives $w^+=(1-\varepsilon\lambda)w-\varepsilon M\nabla E(w)$. Their difference is $\varepsilon\lambda(I-M)w$, which is generally nonzero unless $M$ acts like the required scalar on the weight vector.{{cite:loshchilov_hutter2019}} (§2, Propositions 1–2; Appendix A, eqs. 5–8)
:::

## Interpretation — Shrinkage in linear regression

With squared-error linear regression and a standardized design, minimizing $\lVert y-Xw\rVert^2+\lambda\lVert w\rVert^2$ yields $(X^\top X+\lambda I)w=X^\top y$. Adding $\lambda$ to the diagonal stabilizes directions in which the design supplies little information and shrinks fitted coefficients toward zero. In one dimension, if $X^\top X=4$, $X^\top y=8$, and $\lambda=2$, the unpenalized coefficient is $8/4=2$ while the penalized one is $8/(4+2)=4/3\approx1.33333$. The exact amount of shrinkage depends on how the loss and predictors are scaled.{{cite:goodfellow_bengio_courville2016}} (Ch. 7, §7.1.1, pp. 229–230, eqs. 7.14–7.17)

## Statistical use

Choose the penalty strength using a validation procedure that represents future prediction, keeping a final test set for the finished procedure. Centering and scaling predictors makes a common penalty more interpretable across input coordinates; otherwise units alone alter which weights appear costly. In a neural network, report whether biases and normalization parameters are excluded, and distinguish a coupled penalty from a decoupled decay step when using Adam. A stronger penalty usually lowers training flexibility, which may help noisy small samples but can underfit a real signal.{{cite:krogh_hertz1992}} (§§4–6, pp. 953–956){{cite:loshchilov_hutter2019}} (§2, pp. 2–3)

## Worked example

Consider one weight $w=4$, a current loss gradient $E'(w)=6$, step size $\varepsilon=0.1$, and penalty strength $\lambda=0.2$. Plain gradient descent without a penalty gives $4-0.1(6)=3.4$. With the squared-weight penalty, the shrinkage factor is $1-0.1(0.2)=0.98$, so the new weight is $0.98(4)-0.1(6)=3.32$. Now suppose an adaptive rule scales the gradient by $M=0.5$. Putting the penalty inside that gradient gives $4-0.1(0.5)\{6+0.2(4)\}=3.66$, while a separate decay step gives $0.98(4)-0.1(0.5)(6)=3.62$. The two adaptive updates differ even though both start from the same $w$.{{cite:krogh_hertz1992}} (§1, p. 951, eqs. 1–2){{cite:loshchilov_hutter2019}} (§2, Propositions 1–2)

**Your turn.** Let $w=-2$, $E'(w)=-3$, $\varepsilon=0.1$, and $\lambda=0.4$. Find one plain penalized-gradient step, then compare the coupled and decoupled steps if an adaptive rule scales gradients by $M=0.5$.

::: {.callout-tip collapse="true" title="Answer"}
Plain gradient descent has factor $1-0.1(0.4)=0.96$, giving $0.96(-2)-0.1(-3)=-1.62$. With $M=0.5$, the coupled penalized step is $-2-0.1(0.5)\{-3+0.4(-2)\}=-1.81$. Separate decay gives $0.96(-2)-0.1(0.5)(-3)=-1.77$. Plain SGD makes the two meanings agree after matching coefficients; adaptive scaling breaks that equality.{{cite:loshchilov_hutter2019}} (§2, Propositions 1–2; Appendix A)
:::

## Common misconceptions

“Penalty” and “decay” are not universally interchangeable names; their equivalence depends on how gradients are scaled. Shrinking coefficients does not mean removing features, since an $L^2$ penalty usually leaves them nonzero. A smaller training error does not establish better prediction, and an aggressively shrunken model can miss a real pattern. The numerical value of a penalty coefficient is not portable across a change in loss normalization or predictor units. Finally, an input rescaling that preserves predictions can change the penalty, so small weight magnitude alone is not an invariant measure of model simplicity.{{cite:krogh_hertz1992}} (§§1, 4–6, pp. 951–956){{cite:goodfellow_bengio_courville2016}} (Ch. 7, §7.1.1, pp. 226–230){{cite:loshchilov_hutter2019}} (§2, pp. 2–3)

## Assumptions and limits — When shrinkage hurts

If the true signal depends strongly on a predictor but the training sample is small, an overly large $\lambda$ can drive its weight near zero and systematically miss that signal. If two otherwise identical datasets express distance in metres versus kilometres, an unchanged penalty can act very differently because the compensating coefficient changes scale. In a network with positively homogeneous layers, rescaling adjacent layers can preserve predictions while redistributing penalty cost. An adaptive optimizer's coupled penalty can also shrink coordinates unevenly through its preconditioner. These cases require scale-aware design and validation, not a universal default decay number.{{cite:goodfellow_bengio_courville2016}} (Ch. 7, §7.1.1, pp. 226–230){{cite:loshchilov_hutter2019}} (§2, Propositions 1–2)

## Connections

[Ridge regression](ridge-regression.qmd) is the linear-model version of the squared-weight penalty. [Early stopping](early-stopping.qmd) also limits how far training adapts to noise, but it changes the training trajectory rather than adding the same objective term. [Validation sets](validation-set.qmd) help choose penalty strength; [overfitting](overfitting.qmd) is the prediction failure that regularization seeks to reduce.{{cite:goodfellow_bengio_courville2016}} (Ch. 7, §§7.1, 7.8)

### Guided practice

**1. Scales.** A predictor is multiplied by ten and its fitted weight is divided by ten, leaving every linear prediction unchanged. What happens to that weight's squared penalty contribution?

::: {.callout-tip collapse="true" title="Answer"}
It is divided by one hundred, because $(w/10)^2=w^2/100$. The penalty depends on feature units even though predictions did not change.{{cite:goodfellow_bengio_courville2016}} (Ch. 7, §7.1.1, parameter norm penalty)
:::

**2. Optimizer.** Why can a decoupled decay step differ from adding an $L^2$ penalty under Adam?

::: {.callout-tip collapse="true" title="Answer"}
The penalty gradient passes through Adam's coordinate-dependent scaling when included in the loss, whereas a separate decay step shrinks the weights directly. The update formulas agree under ordinary scalar-step SGD after matching coefficients, but not generally under adaptive scaling.{{cite:loshchilov_hutter2019}} (§2, Propositions 1–2)
:::

## History

Krogh and Hertz's 1992 analysis named weight decay for the update induced by a squared-weight cost and showed conditions under which it improved generalization in a noisy learning problem. Later, Loshchilov and Hutter's 2019 work clarified that adaptive optimizers make loss-based $L^2$ regularization different from a decoupled shrinkage step. Their distinction explains why a modern optimizer's “weight decay” setting needs a precise update definition.{{cite:krogh_hertz1992}} (§§1, 4–6, pp. 951–956){{cite:loshchilov_hutter2019}} (§2, Propositions 1–2)
