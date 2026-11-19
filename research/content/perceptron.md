## Motivating example

A binary detector should fire when a weighted combination of measurements crosses a threshold. Its prediction changes discontinuously when that boundary is crossed. Learning by correcting misclassified examples provides a direct way to construct such a detector. Rosenblatt's perceptron was developed as a learning system whose responses depend on changing connections.{{cite:rosenblatt1958}} (pp. 386–389)

## Definition — A threshold rule and its boundary

For inputs $x\in\mathbb R^p$, weights $w$ and intercept $b$, use output $o(x)=1_{\{b+w^\top x\ge0\}}$. The equality convention assigns a boundary point to class one. The decision surface is a hyperplane whenever $w\ne0$. A single linear threshold cannot represent every binary labelling: the XOR pattern is a basic example requiring a nonlinear representation or additional units.{{cite:goodfellow_bengio_courville2016}} (§6.1, pp. 166–170)

## Properties — What a correction changes

Augment the input by an initial one and write $a=(1,x^\top)^\top$ and $v=(b,w^\top)^\top$. For target $y\in\{0,1\}$, the correction is $v\leftarrow v+(y-o)a$. Taking its inner product with the same $a$ shows that the score changes by $(y-o)\|a\|^2$. A false negative therefore moves its score upward, and a false positive moves it downward. Other examples have score changes $(y-o)a^\top a_j$, which can have either sign: fixing one pattern can spoil another. The algorithm applies this correction repeatedly to the finite training set.{{cite:shalev_bendavid2014}} (§9.1.2, pp. 92–93)

The intercept must be updated along with the other weights when that augmented rule is used. Omitting its update gives a different algorithm restricted to hyperplanes through a fixed intercept. The separating boundary also gives a class decision rather than an estimated class probability; a score of two need not mean any particular odds. Linear decision functions and probabilistic output models are distinct modelling choices.{{cite:goodfellow_bengio_courville2016}} (§§6.1–6.2, pp. 166–183)

For a finite training set with a strict separating hyperplane, the corrections stop after finitely many mistakes. With zero initial weights, augmented input norms at most $R$, and a unit separator having signed margins at least $\gamma>0$, the mistake count is at most $R^2/\gamma^2$.{{cite:shalev_bendavid2014}} (§9.1.2, Thm. 9.1, pp. 92–93)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write signed labels as $s_i=2y_i-1$. On a mistake $s_i v^\top a_i\le0$ and the update is $v+s_i a_i$. After $T$ corrections from zero, projection on a unit separator $u$ is at least $T\gamma$, while $\|v\|^2\le TR^2$. Cauchy–Schwarz gives $T\gamma\le R\sqrt T$. For arbitrary fixed initial $v_0$, the corresponding inequality is $u^\top v_0+T\gamma\le\sqrt{\|v_0\|^2+TR^2}$, which also permits only finitely many corrections.
:::
:::

## Worked example

Take the ordered points $(0,0)$ with label zero, $(1,0)$ with label one, and $(0,1)$ with label one. Start with $v=(0,0,0)$ and use output one at a zero score. Repeated passes through that order produce these five corrections:

| Corrected point | New $(b,w_1,w_2)$ |
|:--|:--|
| $(0,0)$ | $(-1,0,0)$ |
| $(1,0)$ | $(0,1,0)$ |
| $(0,0)$ | $(-1,1,0)$ |
| $(0,1)$ | $(0,1,1)$ |
| $(0,0)$ | $(-1,1,1)$ |

At the final weights, the three scores are $-1,0,0$. Under the stated boundary convention these give the correct three labels. The resulting line is $x_1+x_2=1$. Multiplying all weights and the intercept by a positive constant gives the same labels, demonstrating that a separating representation need not be unique. Threshold-based decisions are consistent with the linear-model limitations discussed for the XOR example.{{cite:goodfellow_bengio_courville2016}} (§6.1, pp. 166–170)

**Your turn.** At weights $(b,w_1,w_2)=(-1,0,0)$, how much does the score of $(1,0)$ increase when its false-negative label is corrected?

::: {.callout-tip collapse="true" title="Answer"}
Its augmented vector is $(1,1,0)$ with squared length two. The score rises from $-1$ to $1$, an increase of two.
:::

## Connections — Representations determine separability

A nonlinear feature map can make a threshold linear in the features while nonlinear in the measured inputs. Multiple layers likewise compose simple units into a richer function. Changing the representation changes which labelled samples are separable; it does not follow merely from running more corrections with a fixed representation. The modern multilayer construction is treated separately from the historical perceptron's connectionist formulation.{{cite:goodfellow_bengio_courville2016}} (§6.1, pp. 166–170){{cite:rosenblatt1958}} (pp. 387–389)
