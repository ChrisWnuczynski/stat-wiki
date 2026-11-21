## Lead context
AdaBoost builds a classifier by giving more weight, at each round, to the training cases the previous round got wrong.

## Motivating example
Four equally weighted cases, one of them wrong, have weighted error $1/4$. The vote is $\tfrac12\log 3\approx 0.549$. After the update, half of the weight sits on the single mistake.

## Intuition — A weak rule is asked to fix the current mistakes
Start with equal weights on the training pairs $(x_i,y_i)$, where $y_i\in\{-1,+1\}$. At round $t$ a weak classifier $h_t$, with values in $\{-1,+1\}$, is chosen to have a small weighted error $\varepsilon_t$. Its vote is $\alpha_t=\frac12\log((1-\varepsilon_t)/\varepsilon_t)$, with the natural logarithm, and the vote is positive only when $\varepsilon_t<1/2$. The weights are then multiplied by $e^{-\alpha_t y_i h_t(x_i)}$ and rescaled so that they sum to one. A mistake is multiplied by $e^{\alpha_t}$ and a correct call by $e^{-\alpha_t}$, so the next round sees a harder weighted sample.{{cite:schapire2013_explaining_adaboost}} (Fig. 1, p. 2)

## Definition — The reweighted vote
Given $m$ training pairs, set $D_1(i)=1/m$. After $h_t$ is chosen,
$$
\varepsilon_t=\Pr_{i\sim D_t}\{h_t(x_i)\ne y_i\},\qquad
\alpha_t=\frac12\log\frac{1-\varepsilon_t}{\varepsilon_t},
$$
and $D_{t+1}(i)\propto D_t(i)\exp(-\alpha_t y_i h_t(x_i))$. The classifier returns the sign of $\sum_t\alpha_t h_t(x)$. The same choices of $h_t$ and $\alpha_t$ greedily reduce the exponential loss $m^{-1}\sum_i\exp(-y_i F(x_i))$, where $F$ is the weighted sum inside the sign.{{cite:schapire2013_explaining_adaboost}} (Fig. 1, p. 2; exponential loss, p. 7)

## Properties — The coefficient balances the two kinds of case
For a fixed classifier with weighted error $\varepsilon\in(0,1)$, the exponential-loss factor in the new coefficient $\alpha$ is $(1-\varepsilon)e^{-\alpha}+\varepsilon e^{\alpha}$.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Differentiate $(1-\varepsilon)e^{-\alpha}+\varepsilon e^{\alpha}$ with respect to $\alpha$. The derivative is $-(1-\varepsilon)e^{-\alpha}+\varepsilon e^{\alpha}$, which is zero when $e^{2\alpha}=(1-\varepsilon)/\varepsilon$. Hence $\alpha=\frac12\log((1-\varepsilon)/\varepsilon)$, the AdaBoost coefficient. The second derivative $(1-\varepsilon)e^{-\alpha}+\varepsilon e^{\alpha}$ is positive, so the critical point is a minimum. If $\varepsilon>1/2$ the coefficient is negative and the vote is reversed.{{cite:schapire2013_explaining_adaboost}} (Fig. 1, p. 2; exponential loss, p. 7)
:::
:::

## Worked example
Four equally weighted cases give $\varepsilon=1/4$ when one case is wrong. Then $\alpha=\frac12\log 3\approx 0.549$, $e^{\alpha}=\sqrt 3\approx 1.732$ and $e^{-\alpha}\approx 0.577$. The normalising constant is
$$
Z=2\sqrt{\varepsilon(1-\varepsilon)}=\sqrt 3/2\approx 0.866.
$$
The updated weight on the mistake is $(1/4)\sqrt 3\big/(\sqrt 3/2)=1/2$. Each correct case has updated weight $(1/4)/\sqrt 3\big/(\sqrt 3/2)=1/6$. The three correct weights sum to $1/2$, so the next distribution still sums to one, and half of it sits on the single mistake.{{cite:schapire2013_explaining_adaboost}} (Fig. 1, p. 2)

**Your turn.** Keep four equal initial weights and suppose the weak classifier is wrong on two of them, so $\varepsilon=1/2$. What is $\alpha$, and what happens to the weights?

::: {.callout-tip collapse="true" title="Answer"}
$\alpha=\frac12\log(1)=0$. Every multiplier $e^{0}$ equals $1$, so the weights stay at $1/4$. A rule that is no better than a coin toss on the current weights receives no vote.
:::

## Connections
The exponential loss is a smooth stand-in for the zero–one training error, and it is related to the loss used for logistic regression. Minimising that loss is not, by itself, a guarantee of a small error on new cases: other procedures can drive the same loss down and still classify poorly. The sign of the weighted sum is the class label; the sum itself is not a calibrated probability.{{cite:schapire2013_explaining_adaboost}} (pp. 7–8, exponential loss and generalisation)
