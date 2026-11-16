## Intuition — Start near zero, and not all at zero
A sigmoid is steepest at zero and almost flat far out in either tail. If the first net inputs are huge, the hidden units start saturated and the chain rule has little slope to pass backward. If every weight is exactly zero, symmetric units stay interchangeable: a deterministic update that treats them alike has nothing to break the tie. The usual start is therefore small random weights, centred at zero, with a scale chosen so that the net input is neither tiny nor enormous.{{cite:hastie_esl2009}} (Ch. 11, §11.5.1, p. 397)

## Definition — Two variance rules
Let the non-bias inputs have mean zero and variance one, and let the weights into one unit be independent, mean zero, and variance $\sigma^2$, independent of the inputs. With a bias input $x_0=1$ and $p$ further inputs,
$$
\operatorname{Var}(u)=(p+1)\sigma^2.
$$
The choice $\sigma=(p+1)^{-1/2}$ makes this marginal variance $1$. Glorot and Bengio study a different target for deep networks with a symmetric activation whose derivative at zero is $1$: they keep both the forward activation variance and the backward gradient variance from blowing up or vanishing by setting
$$
\operatorname{Var}(W^i)=\frac{2}{n_i+n_{i+1}}
$$
at a layer with $n_i$ incoming and $n_{i+1}$ outgoing units. The uniform draw on $[-\sqrt{6/(n_j+n_{j+1})},\sqrt{6/(n_j+n_{j+1})}]$ has that variance. The logistic sigmoid is a poor match to this scheme in a deep stack, because its mean is not zero and it saturates.{{cite:hastie_esl2009}} (Ch. 11, §11.5.1, p. 397){{cite:glorot_bengio2010}} (eqs. 12 and 16, pp. 252–253)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write $u=\sum_{j=0}^{p} w_j x_j$ with $x_0=1$. Independence and centred weights kill the cross terms, and each summand has second moment $\sigma^2$ when the non-bias inputs have variance one and the bias input has square one. There are $p+1$ such summands, so the variance is $(p+1)\sigma^2$.

A uniform law on $[-a,a]$ has variance $a^2/3$. Set $a=\sqrt{6/(n_j+n_{j+1})}$. Then $a^2/3=2/(n_j+n_{j+1})$, which is the variance in Glorot and Bengio's equation (12).{{cite:glorot_bengio2010}} (eqs. 12 and 16, pp. 252–253)
:::
:::

## Worked example — Four weights, and a square layer
For $p=3$ non-bias inputs the fan-in rule uses $\sigma=1/2$. The marginal variance of the net input is $4\cdot(1/2)^2=1$. Conditional on an input with $\lVert x\rVert^2=3$, the same weights give conditional variance $\sigma^2(1+3)=1$ as well. A standard normal with that variance satisfies $\mathbb P(|U|\le 1)=2\Phi(1)-1=0.6827$ to four decimal places.

For a square layer with $n_j=n_{j+1}=4$, the uniform half-width is $\sqrt{6/8}=\sqrt{3}/2\approx 0.8660$, and the weight variance is $2/8=0.25$.{{cite:glorot_bengio2010}} (eq. 16, p. 253){{cite:siegrist2022_normal_distribution}} (§5.6, standard normal density)

**Your turn.** For $p=8$ non-bias inputs, find the fan-in $\sigma$ that makes the marginal net-input variance $1$, and the Glorot weight variance for a layer with $8$ units on each side.

::: {.callout-tip collapse="true" title="Answer"}
There are $9$ incoming weights including the bias, so $\sigma=1/3$. The marginal variance is $9\cdot(1/3)^2=1$. The Glorot variance for $n_j=n_{j+1}=8$ is $2/16=0.125$, and the uniform half-width is $\sqrt{6/16}=\sqrt{6}/4\approx 0.6124$.
:::

## Check yourself
### Exact zeros
All incoming and outgoing weights of two hidden units are zero. A batch gradient step treats the two units symmetrically. Do the units separate?

::: {.callout-tip collapse="true" title="Answer"}
No. Equal weights stay equal under a symmetric deterministic update, so the units remain copies of each other. Independent random starts break that tie.{{cite:hastie_esl2009}} (Ch. 11, §11.5.1, p. 397)
:::

### Which rule is which
A layer has $100$ inputs and $4$ outputs, ignoring bias. Which is larger, $(100)^{-1/2}$ or $\sqrt{2/(100+4)}$?

::: {.callout-tip collapse="true" title="Answer"}
$(100)^{-1/2}=0.1$. The Glorot standard deviation is $\sqrt{2/104}\approx 0.1387$, which is larger for these two widths. The comparison is only the two formulas: a narrow output layer changes the symmetric rule, and it does not by itself say which scale will train better.
:::

## Connections — Scale before the first step
The [sigmoid function](sigmoid-function.qmd) is the nonlinearity whose flat tails make the scale matter. [Stochastic gradient descent](stochastic-gradient-descent.qmd) then moves the weights, and [early stopping](early-stopping.qmd) decides how far that move is allowed to go. A [regularisation](regularisation.qmd) penalty pulls weights toward zero during training; initialisation only chooses where that path starts.{{cite:hastie_esl2009}} (Ch. 11, §§11.5.1–11.5.2, pp. 397–398){{cite:glorot_bengio2010}} (eq. 16, p. 253)
