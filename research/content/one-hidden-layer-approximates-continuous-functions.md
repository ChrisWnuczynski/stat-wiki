## Motivating example
A sensor calibration curve can bend without having a useful polynomial formula. Before fitting a neural network to calibration pairs, it is reasonable to ask whether the model family can approximate the curve at all. A universal approximation theorem answers that representational question for a continuous target on a compact set. It quantifies over every positive tolerance, allowing the width and all coefficients to depend on the target and tolerance. It supplies no finite-sample accuracy guarantee.{{cite:cybenko1989}} (Theorem 2, p. 308)

## Statement

**The order of the quantifiers matters.**
Fix a continuous function $\sigma:\mathbb R\to\mathbb R$ with limits zero at negative infinity and one at positive infinity. For every $f\in C([0,1]^p)$ and $\varepsilon>0$, some finite width $m$ and coefficients satisfy
$$\left\|f-\sum_{j=1}^m a_j\sigma(w_j^Tx+b_j)\right\|_\infty<\varepsilon.$$
The same activation is used for every unit. The coefficients, biases and width may change when either the target or the requested tolerance changes. A statement that one fixed finite network approximates all continuous functions would have a different, false quantifier order. Compactness also matters: uniform control over an unbounded domain is a stronger requirement.{{cite:cybenko1989}} (Theorem 2, p. 308)

A linear output permits negative and arbitrarily large values even when each hidden activation lies between zero and one. The sigmoid therefore belongs in the hidden layer; imposing it on the final output would exclude targets outside that range. More general approximation results for measurable functions require an explicit error measure and are distinct from this uniform statement.{{cite:goodfellow_bengio_courville2016}} (§6.4.1, pp. 193–195)

## Intuition — Shifts locate changes and slopes set their scale
For the logistic function $\sigma(t)=(1+e^{-t})^{-1}$, the term $\sigma(k(x-c))$ changes most rapidly near $c$. Increasing positive $k$ narrows the transition. A difference of two shifted sigmoids can create a smooth window: it rises near the first shift and falls near the second. Weighted sums of such functions can express several changes of level. This explains useful one-dimensional examples, while the multidimensional density theorem requires a more general argument involving ridge functions and separating measures.{{cite:cybenko1989}} (§2, Theorem 1 and Lemma 1, pp. 305–308)

The distinction between hidden features and output coefficients is helpful. Each $\sigma(w_j^Tx+b_j)$ is constant along hyperplanes normal to $w_j$. Choosing $w_j$ selects a direction, choosing $b_j$ moves the transition, and choosing $a_j$ controls how that feature contributes to the final function. A network learns these features jointly rather than choosing only coefficients for a fixed dictionary.{{cite:goodfellow_bengio_courville2016}} (Chapter 6, pp. 164–166)

## Worked example — A smooth window with two units
Consider
$$F(x)=\sigma(10(x-0.25))-\sigma(10(x-0.75)).$$
At $x=0.5$, the two inputs are $2.5$ and $-2.5$, so the output is $0.848284$. At $x=0$ and $x=1$ it is $0.075305$. The two hidden units have output coefficients $1$ and $-1$, so their difference forms a window despite both activations being positive. Symmetry follows from $\sigma(-t)=1-\sigma(t)$: replacing $x$ by $1-x$ leaves $F$ unchanged. This is an explicit representable function, rather than a claim that two units approximate every target.

Differentiation gives $\sigma'(t)=\sigma(t)(1-\sigma(t))\le1/4$. Thus the absolute derivative of the displayed window is at most $5$ by the triangle inequality. A narrow transition uses a large input coefficient, which can also make an optimisation problem poorly scaled. Approximation, parameter size and training stability are separate considerations.

**Your turn.** Keep the shifts but change the input coefficient from 10 to 20. What is the output at the midpoint?

::: {.callout-tip collapse="true" title="Answer"}
It is $\sigma(5)-\sigma(-5)=0.986614$. The centre becomes closer to one while the transition becomes steeper.
:::

## Common misconceptions — Representation does not identify a fitted model
An approximation theorem does not establish that gradient descent will find the approximating coefficients. It also does not choose a width, regularisation strength, training sample or validation procedure. A very wide network may represent both a smooth target and an interpolation of noisy observations. Selecting between those fits requires statistical information absent from the existence theorem.{{cite:goodfellow_bengio_courville2016}} (§6.4.1, pp. 194–196)

Uniform limits of continuous functions are continuous. Consequently, continuous sigmoid networks cannot converge uniformly to a genuine jump on a domain containing that jump: any continuous approximation must compromise near the discontinuity. They can approximate classification decisions outside a set of small measure under a different theorem, which explains why the choice of norm is part of the mathematical statement.{{cite:cybenko1989}} (Theorem 3 and discussion, pp. 308–309)

## Statistical use — Choose width through the fitting objective
The theorem can rule out a representational obstacle for a continuous target, but architecture selection still needs a statistical objective. In a regression analysis, compare candidate widths under a training and validation scheme that includes any regularisation and stopping choices. A good validation score assesses the fitted procedure on the observations available; it does not turn an existence result into a finite-sample error bound. Where scientific knowledge suggests smoothness or shape constraints, those assumptions can guide a more economical model family than an unrestricted universal approximator.{{cite:goodfellow_bengio_courville2016}} (§6.4.1, approximation capacity, training and generalisation)
