## Motivating example

Suppose a classifier predicts one of three species. Coding the labels as the numbers one, two and three would suggest an ordering and numerical distances between species. A separate indicator coordinate for each species supplies labels without that artificial scale.{{cite:zhang_d2l2023}} (§4.1.1)

## Definition — Categories as coordinate vectors

For a category $c\in\{1,\ldots,K\}$, its one-hot vector is the basis vector $e_c$: coordinate $c$ equals one and the others equal zero. Every such vector sums to one, and distinct category vectors have the same Euclidean distance $\sqrt2$. The coordinate order is a coding convention; permuting it consistently leaves the represented categories unchanged. One-hot response coding is used with a categorical probability model.{{cite:zhang_d2l2023}} (§4.1.1)

For predicted probabilities $s_k>0$ summing to one, the log likelihood of a one-hot response is $\sum_k y_k\log s_k$. Its negative is the cross-entropy loss. Exactly one term contributes, so the loss on class $c$ is $-\log s_c$.{{cite:goodfellow_bengio_courville2016}} (§6.2.2.3, pp. 180–183)

## Properties — Redundancy and gradients

In a linear predictor with an intercept and all $K$ indicator columns, the indicators sum to the intercept column. The parameterisation is redundant: adding a constant to the intercept and subtracting it from every category coefficient leaves fitted values unchanged. A reference level or an explicit constraint makes the coefficients unique. This is an algebraic issue distinct from representing the response. With softmax output scores, adding the same constant to all class scores also leaves probabilities unchanged.{{cite:goodfellow_bengio_courville2016}} (§6.2.2.3, pp. 182–183)

Write $s_k=e^{z_k}/\sum_j e^{z_j}$. For one observed label $c$,
$$
L(z)=-z_c+\log\sum_j e^{z_j},\qquad
\frac{\partial L}{\partial z_k}=s_k-1_{\{k=c\}}.
$$
The gradient coordinates sum to zero, consistently with invariance to a common score shift. An indicator target does not require the fitted probability vector itself to contain a single one.{{cite:zhang_d2l2023}} (§4.1.2.2)

## Worked example

Let the probabilities for three species be $(0.2,0.5,0.3)$, and suppose the observed species is the second. The target is $(0,1,0)$, the loss is $-\log0.5\approx0.693147$, and the score gradient is $(0.2,-0.5,0.3)$. For scores $(0,0.5,-0.2)$, the corresponding probabilities instead are approximately $(0.288396,0.475485,0.236119)$. The class-three log odds against class two are $-0.2-0.5=-0.7$. The probabilities and the one-hot target occupy the same simplex, but they play different roles in the likelihood.{{cite:zhang_d2l2023}} (§§4.1.1.2–4.1.2.2)

**Your turn.** For a four-category label equal to category three, write its vector and the loss when its predicted probability is $0.25$.

::: {.callout-tip collapse="true" title="Answer"}
The vector is $(0,0,1,0)$ and the loss is $-\log0.25=\log4\approx1.386294$.
:::

## Connections — One label and several labels

One-hot coding describes one mutually exclusive category. A response with several simultaneously true attributes can have several indicator coordinates equal to one; a single categorical softmax model does not describe that outcome space. Independent Bernoulli outputs are one possible model for such multiple labels, with a different likelihood.{{cite:goodfellow_bengio_courville2016}} (§§6.2.2.2–6.2.2.3, pp. 176–183)

