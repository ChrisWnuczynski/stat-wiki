## Motivating example
A sensor calibration curve can bend without having a useful polynomial formula. Before fitting a neural network to calibration pairs, it is reasonable to ask whether sums of ridge-shaped hidden units can track that curve at all. Representation, optimisation and statistical error are different questions. An existence theorem can remove the first obstacle for a continuous target on a compact set and still say nothing about how many units a sample of a given size can estimate.{{cite:goodfellow_bengio_courville2016}} (§6.4.1, pp. 194–195)

The relevant function class is a finite linear combination of shifted and scaled hidden activations. Each hidden unit is constant on hyperplanes and changes only along one direction. The output weights are free to be positive or negative, so the network value is not trapped inside the range of a single activation.{{cite:bishop2006}} (Ch. 5, §5.1, feed-forward architecture)

## Statement

**Uniform approximation by one hidden layer.**
Fix a continuous function $\sigma:\mathbb R\to\mathbb R$ with limits zero at negative infinity and one at positive infinity. For every $f\in C([0,1]^p)$ and every $\varepsilon>0$, some finite width $m$ and real coefficients satisfy
$$\left\|f-\sum_{j=1}^m a_j\sigma(w_j^Tx+b_j)\right\|_\infty<\varepsilon.$$
The same activation is used in every unit. The width, directions, shifts and output weights may all depend on the target and on the tolerance. Compactness of the cube is part of the hypothesis: uniform control on an unbounded domain is a stronger demand.{{cite:cybenko1989}} (Theorem 2, p. 308)

The activation hypothesis is a limit condition, not a requirement that $\sigma$ equal the logistic formula. Any continuous sigmoidal function with those two limits is allowed. The logistic map $\sigma(t)=(1+e^{-t})^{-1}$ is one example: it is continuous, strictly increasing, and has the required limits. A linear output layer is essential. Coefficients $a_j$ may be negative and large, so the network can represent values outside $(0,1)$. Placing a final sigmoid on the output would exclude targets such as an unrestricted calibration curve.{{cite:goodfellow_bengio_courville2016}} (§6.4.1, pp. 193–195)

The order of the quantifiers is part of the result. The theorem says that each continuous target and each tolerance has some finite network. It does not say that one fixed finite network approximates every continuous function. A statement with those quantifiers reversed would be false: the unit cube contains continuous functions with arbitrarily fine oscillation.

## Intuition — Shifts locate changes and slopes set their scale
For the logistic function, $\sigma(k(x-c))$ changes most rapidly near $c$. Increasing a positive slope $k$ narrows the transition. A difference of two shifted sigmoids can form a smooth window: the combination rises near the first centre and falls near the second. Weighted sums of such windows can follow several changes of level on an interval. This picture explains useful one-dimensional constructions. The general argument on the cube uses ridge functions and a separating measure, rather than an explicit window for every target.{{cite:cybenko1989}} (§2, Theorem 1 and Lemma 1, pp. 305–308)

Each hidden feature $\sigma(w_j^Tx+b_j)$ is constant on hyperplanes normal to $w_j$. The vector $w_j$ selects a direction, the bias $b_j$ slides the transition along that direction, and the output weight $a_j$ sets the feature's contribution. A one-hidden-layer network learns these features together with the output weights. If every activation were affine, the whole map would collapse to one affine function, and the hidden layer would add no new shapes.{{cite:bishop2006}} (Ch. 5, §5.1){{cite:goodfellow_bengio_courville2016}} (Chapter 6, pp. 164–166)

Zero input weights give a constant hidden value. For the logistic activation that constant is $\sigma(0)=1/2$. An output weight then scales the constant, so a single hidden unit can represent any constant function. The same device shows why the output weights must be unrestricted: a bounded final activation could not produce an arbitrary constant.

## Key results — A jump stops uniform approximation
Finite networks built from continuous activations are continuous. A uniform limit of continuous functions on a compact interval is continuous. Suppose a target $s$ on $[0,1]$ equals $0$ on $[0,1/2)$ and equals $1$ on $[1/2,1]$. If a continuous $F$ satisfied $\|F-s\|_\infty<1/2$, then $F(x)<1/2$ for every $x<1/2$ and $F(1/2)>1/2$. Continuity at $1/2$ would force values just to the left of $1/2$ to lie above $1/2$ as well. That contradiction shows that every continuous approximation has uniform error at least $1/2$. The constant function $1/2$ attains this error, so the greatest lower bound is exactly $1/2$. Steep sigmoidal transitions can make the region of large error very narrow. They cannot make the uniform error smaller than $1/2$, because the value at the jump remains a half-unit away from at least one of the two limits.

A different mode of approximation applies to some discontinuous targets. Approximation in measure, or outside a set of small measure, can tolerate a thin transition zone whose pointwise error stays large. That claim uses its own hypotheses and its own error. It is a separate theorem from the uniform result for continuous targets.{{cite:cybenko1989}} (Theorem 3 and discussion, pp. 308–309)

## Worked example
### A smooth window with two units
Consider
$$F(x)=\sigma(10(x-0.25))-\sigma(10(x-0.75)).$$
At $x=0.5$, the two inputs are $2.5$ and $-2.5$, so the output is $0.848284$. At $x=0$ and $x=1$ it is $0.075305$. The output coefficients are $1$ and $-1$, so the difference forms a window even though both activations are positive. Symmetry $\sigma(-t)=1-\sigma(t)$ shows that replacing $x$ by $1-x$ leaves $F$ unchanged. This is one explicit function in the network class. Two units produce this particular window; the uniform theorem still lets the required width depend on the target.

Differentiation gives $\sigma'(t)=\sigma(t)(1-\sigma(t))\le 1/4$. The absolute derivative of the displayed window is therefore at most $5$. A narrow transition uses a large input coefficient, which can also make an optimisation problem poorly scaled. Approximation, parameter size and training stability are separate considerations.

### A centred sigmoid and a step
Let $s$ be the jump above, and let $F_k(x)=\sigma(k(x-1/2))$. Then $F_k(1/2)=1/2$, so the error at the jump is exactly $1/2$ for every finite $k$. On the rest of $[0,1]$ the error is strictly smaller: left of $1/2$ the sigmoid lies in $(0,1/2)$, and right of $1/2$ it lies in $(1/2,1)$. The uniform error is therefore exactly $1/2$ for every slope. At slope $20$, the endpoint value $\sigma(-10)$ is about $0.00004540$, and symmetry gives the same error at $x=1$. The transition has become visually sharp, and the uniform distance to $s$ has not improved.

**Your turn.** Keep the shifts of the two-unit window but change the input coefficient from 10 to 20. What is the output at the midpoint?

::: {.callout-tip collapse="true" title="Answer"}
It is $\sigma(5)-\sigma(-5)=0.986614$. The centre becomes closer to one while the transition becomes steeper.
:::

## Generalizations — Other activations and other norms
The logistic calculations illustrate a sigmoidal unit. The uniform theorem applies to every continuous activation with the same limits, and a different activation needs its own argument. Rectified linear units are continuous but do not tend to a finite positive limit at positive infinity, so they sit outside the sigmoidal hypothesis even though other approximation theorems cover them. Changing the error from a uniform norm to an integral norm, or asking for approximation of derivatives as well as values, changes the theorem again.{{cite:goodfellow_bengio_courville2016}} (§6.4.1, pp. 194–196, activation classes and depth)

Depth can sometimes represent a repeated composition with fewer units than a shallow expansion of the same map. Universality of one hidden layer does not supply a useful width bound for every continuous target, and it does not name a sample size that learns every such target. A learning guarantee needs further restrictions on the target, the noise and the design.

## Statistical use — Choose width through the fitting objective
The uniform theorem can rule out a purely representational objection to a continuous calibration curve on a compact domain. Architecture choice still needs a statistical objective. In a regression analysis, compare candidate widths under a training and validation scheme that includes regularisation and any early stopping. A good validation score describes the fitted procedure on the observations in hand. It does not convert an existence result into a finite-sample error bound. When scientific knowledge supplies smoothness or a low-dimensional formula, that structure can be a more economical model than an unrestricted universal approximator.{{cite:goodfellow_bengio_courville2016}} (§6.4.1, approximation capacity, training and generalisation)

Three errors should stay distinct. Approximation error is the distance from the target to the best network of a chosen size. Optimisation error is the failure of a training run to find those weights. Statistical error is the effect of seeing finitely many noisy pairs rather than the target itself. Increasing the width can shrink the first term while making the other two harder.

## Common misconceptions — Representation does not identify a fitted model
An approximation theorem does not establish that gradient descent will find the approximating coefficients. It also does not choose a width, a regularisation strength, a training sample or a validation procedure. A very wide network may represent both a smooth target and an interpolation of noisy observations. Selecting between those fits requires statistical information that the existence theorem does not contain.{{cite:goodfellow_bengio_courville2016}} (§6.4.1, pp. 194–196)

A small pointwise error on a fine grid is not, by itself, a uniform bound. The centred sigmoids above have tiny error at the endpoints of the step and error $1/2$ at the jump. A network that matches a classification label except on a thin strip can still have a large uniform error on that strip. The norm used in the conclusion decides which of those statements has been made.

## History
Idealised neural events were described as all-or-none threshold units in the 1943 logical model of McCulloch and Pitts. A hard threshold can represent a sharp decision, and its lack of a useful derivative away from the jump is a separate obstacle for gradient training.{{cite:mcculloch_pitts1943}} (p. 115, neural threshold model)

Differentiable hidden units made internal features trainable by back-propagated errors. Rumelhart, Hinton and Williams developed that account in 1986, with a smooth activation whose local derivative could be chained through the hidden layer. Their construction concerns learning representations, not a uniform density theorem for every continuous target.{{cite:rumelhart_hinton_williams1986}} (pp. 533–534)

The uniform approximation result stated above is Cybenko's 1989 theorem for continuous sigmoidal units on the unit cube. Later accounts of the same theorem keep the separation between the existence of some network and the statistical problem of estimating its weights.{{cite:goodfellow_bengio_courville2016}} (§6.4.1, pp. 194–195)
