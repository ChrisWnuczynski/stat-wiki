## Lead context
Softmax turns a vector of scores into class probabilities, and cross-entropy scores those probabilities by the negative log probability of the class that actually occurred.

## Motivating example
Three scores $0$, $1$, and $-1$ are not probabilities: they do not lie in $(0,1)$ and they do not sum to $1$. Exponentiating and dividing by the total gives approximately $0.2447$, $0.6652$, and $0.0900$, which do sum to $1$. If the true class is the second, the cross-entropy is $-\log 0.6652\approx 0.4076$ nats. The gradient of that loss in the scores is the probability vector minus the one-hot label, about $(0.2447,-0.3348,0.0900)$. The correct score is pushed up. The other two are pushed down in proportion to the probability they wrongly received.{{cite:hastie_esl2009}} (§11.3–11.4, eqs. 11.6 and 11.10, pp. 393–395)

## Intuition
Separate sigmoid outputs, one per class, need not sum to $1$. They are scores. A single class label needs a distribution. Softmax is the map
$$
s_k=\frac{e^{z_k}}{\sum_{l=1}^{m} e^{z_l}}.
$$
It is unchanged if the same constant is added to every $z_k$, because that constant factors out of every exponential and cancels. Cross-entropy for a one-hot label with a $1$ in position $c$ collapses to $-\log s_c$. Shannon's entropy is the same kind of average surprise when the weights are a distribution rather than a single label.{{cite:shannon1948}} (Thm. 2){{cite:hastie_esl2009}} (§11.3, eq. 11.6, p. 393)

## Definition
For $K$ classes, Hastie, Tibshirani and Friedman set the output unit to
$$
g_k(T)=\frac{e^{T_k}}{\sum_{\ell=1}^{K} e^{T_\ell}}
$$
and, for classification, the cross-entropy
$$
R(\theta)=-\sum_{i=1}^{N}\sum_{k=1}^{K} y_{ik}\log f_k(x_i).
$$
With this pair, a network with no hidden layer is multinomial logistic regression. The predicted class is the largest output. A confidently wrong output has a small $s_c$ and therefore a large $-\log s_c$.{{cite:hastie_esl2009}} (§11.3–11.4, eqs. 11.6 and 11.10, pp. 393–395)

## Interpretation — The gradient cancels the Jacobian
Let $y$ be a probability vector, $\sum_k y_k=1$, and let $E=-\sum_k y_k\log s_k$. Differentiating the softmax gives $\partial s_k/\partial z_j=s_k(\delta_{kj}-s_j)$. Then
$$
\frac{\partial E}{\partial z_j}=\sum_k y_k(s_j-\delta_{kj})=s_j-y_j,
$$
because $\sum_k y_k=1$. For a one-hot label the same identity is $s-y$. There is no extra sigmoid slope at this layer. A correct and confident prediction has $s_c$ near $1$ and a small gradient. A wrong and confident prediction keeps an error signal of size about $1$ on the true class.

## Properties
The cancellation, the shift invariance, and the two-class reduction are algebra.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write $Z=\sum_l e^{z_l}$ and $s_k=e^{z_k}/Z$. Adding $c$ to every coordinate multiplies each exponential by $e^{c}$ and multiplies $Z$ by $e^{c}$, so $s$ is unchanged.

For two classes,
$$
\frac{e^{z_1}}{e^{z_1}+e^{z_2}}=\frac{1}{1+e^{-(z_1-z_2)}},
$$
which is the logistic function of the difference. With $z_1-z_2=1$ the value is $1/(1+e^{-1})\approx 0.7311$.

For the gradient, $\partial\log s_k/\partial z_j=\delta_{kj}-s_j$. Therefore
$$
\frac{\partial}{\partial z_j}\Bigl(-\sum_k y_k\log s_k\Bigr)=-\sum_k y_k(\delta_{kj}-s_j)=s_j\sum_k y_k-y_j.
$$
If $\sum_k y_k=1$ this is $s_j-y_j$.{{cite:hastie_esl2009}} (§11.3, eq. 11.6)
:::
:::

## Statistical use — Codes and a linear model on learned features
A one-hot code uses one output per class and puts a $1$ on the true class. Coding classes $1,2,3$ as a single numeric input would invent an order the labels do not have. Softmax undoes that mistake at the output: the class probabilities are a function of $m$ free scores, with the redundant level absorbed because adding a constant does not change $s$.

Minimising the cross-entropy on a training set, with $z_k=\beta_k^\top h(x)$ and features $h$ learned in earlier layers, is maximum likelihood for a multinomial logistic model on those features. The hidden layers are what make the features. The output layer is the logistic regression.{{cite:hastie_esl2009}} (§11.4, p. 395)

## Worked example
Scores $z=(0,1,-1)$, true class $2$. The exponentials are $1$, $e$, and $e^{-1}$, and their sum is $1+e+e^{-1}\approx 4.0862$. The probabilities are
$$
s\approx(0.2447,\ 0.6652,\ 0.0900).
$$
The cross-entropy is $-\log 0.6652\approx 0.4076$. The error signals $s-y$ are approximately $(0.2447,-0.3348,0.0900)$.

The same arithmetic on $z=(2,1,0.1)$, with the true class first, gives $s\approx(0.659,0.242,0.099)$, cross-entropy $-\log 0.659\approx 0.417$, and error signals approximately $(-0.341,0.242,0.099)$. Adding $5$ to every coordinate of $z$ leaves both probability vectors unchanged.

**Your turn.** Two scores are $z_1=1.5$ and $z_2=0.5$, and the true class is the first. Find the softmax probability of class $1$, and the cross-entropy.

::: {.callout-tip collapse="true" title="Answer"}
The difference is $1$, so the probability is $1/(1+e^{-1})\approx 0.7311$. The cross-entropy is $-\log 0.7311\approx 0.3133$. The error on the first score is $0.7311-1=-0.2689$, and the error on the second is $0.2689$.{{cite:hastie_esl2009}} (§11.3, eq. 11.6)
:::

## Common misconceptions
Softmax outputs are not independent probabilities. They sum to $1$. Raising one score lowers the others.

Cross-entropy is not squared error. Squared error on a probability treats a prediction of $0.01$ when the label is $1$ as an error of $0.99^2\approx 0.980$. Cross-entropy treats it as $-\log 0.01\approx 4.605$ nats. The gradient $s-y$ stays large. A squared-error gradient on a saturated sigmoid can be small because of the sigmoid slope. That slope is absent from $s-y$.

A numeric code $1,2,3$ for three classes is not a softmax. Softmax consumes a vector of scores. The integers would impose gaps of $1$ between classes that the labels do not state.

## Assumptions and limits — Overflow, and a label that is not one-hot
Exponentiating a score of $1000$ overflows ordinary floating-point arithmetic. Subtracting $\max_k z_k$ before the exponential does not change $s$, because of the shift invariance, and it keeps the largest exponential equal to $1$. The mathematical function is the same. The computed function is the one that remains finite.

If the target is a probability vector rather than a one-hot label, the identity $\partial E/\partial z_j=s_j-y_j$ still holds as long as the target coordinates sum to $1$. If they do not, the factor $\sum_k y_k$ remains in the gradient and the simple residual $s-y$ is wrong.

Softmax on the outputs does not stop a hidden unit from saturating. The missing slope is a fact about the output layer. Earlier layers still multiply by the derivatives of their own activations.

## Connections
The [sigmoid function](sigmoid-function.qmd) is the two-class case of softmax. [Cross-entropy](kullback-leibler-divergence.qmd) in the population sense is the extra surprise of using one distribution in place of another; the training loss here is the empirical version for a one-hot label. The [learning rate](learning-rate.qmd) multiplies the residual $s-y$ when the scores are updated by gradient descent. A [logit link](logit-link.qmd) is the two-class linear model obtained when the score difference is linear in the inputs and there is no hidden layer.{{cite:hastie_esl2009}} (§11.3–11.5, pp. 393–397)

## Check yourself
### Three scores
For $z=(0,1,-1)$ and true class $2$, what are the softmax probabilities to four decimals, and the cross-entropy to four decimals?

::: {.callout-tip collapse="true" title="Answer"}
The probabilities are $0.2447$, $0.6652$, and $0.0900$. The cross-entropy is $0.4076$.{{cite:hastie_esl2009}} (§11.3, eq. 11.6)
:::

### A shift
Add $5$ to every coordinate of $(2,1,0.1)$. Do the probabilities change?

::: {.callout-tip collapse="true" title="Answer"}
No. Each exponential is multiplied by $e^{5}$, and so is their sum. The probabilities stay about $(0.659,0.242,0.099)$.
:::

### Two classes
Scores $1.5$ and $0.5$. What is the probability of the first class, to four decimals?

::: {.callout-tip collapse="true" title="Answer"}
It equals $1/(1+e^{-1})\approx 0.7311$.{{cite:hastie_esl2009}} (§11.3, eq. 11.6)
:::

## History
Shannon's entropy measures the average surprise of a discrete source by $-\sum p\log p$. The training loss on this page is that surprise when $p$ is a one-hot label and the logarithm is applied to the predicted probability.{{cite:shannon1948}} (Thm. 2) Hastie, Tibshirani and Friedman write the softmax as the normalised exponential used for $K$-class outputs, and they pair it with cross-entropy so that the network, restricted to linear scores, is a multinomial logistic regression fitted by maximum likelihood.{{cite:hastie_esl2009}} (§11.3–11.4, pp. 393–395)
