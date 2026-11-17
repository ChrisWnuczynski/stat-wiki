## Lead context
Full-batch, minibatch and single-example updates differ in the gradient information used per step. The sum-versus-average convention must be fixed before learning rates are compared.{{cite:zhang_d2l2023}} (§12.4.1, “Stochastic Gradient Updates”)

## Motivating example
A model fitted to a million cases may make useful progress before reading all cases for one exact gradient. A randomly chosen case gives a cheap but noisy direction. That direction can increase the full loss on a particular step while remaining correct on average.{{cite:goodfellow_bengio_courville2016}} (§8.1.3, pp. 274–275)

## Properties — Conditional unbiasedness is a sampling statement
For the average objective $L(w)=n^{-1}\sum_iL_i(w)$, draw $I$ uniformly and independently of the current weight, conditional on the fixed data and weight. Then
$$
E\{\nabla L_I(w)\mid w,D\}=\frac1n\sum_i\nabla L_i(w)=\nabla L(w).
$$
For the sum objective, the unbiased estimate is instead $n\nabla L_I(w)$. This equality follows by a finite average, not by assuming that all individual gradients are close. Nonuniform sampling requires inverse-probability weights to estimate the same gradient.{{cite:zhang_d2l2023}} (§12.4.1, stochastic gradient expectation)

For $b$ independent draws with replacement, their average gradient has covariance $\Sigma_g/b$, where $\Sigma_g$ is the covariance of one random-case gradient. This follows because independent cross-covariances vanish. Sampling without replacement changes this variance through a finite-population correction. At a fixed weight, larger batches reduce this sampling noise; they also require more work per step.{{cite:goodfellow_bengio_courville2016}} (§8.1.3, eqs. 8.4–8.6)

## Worked example
Let $L_i(w)=\tfrac12(w-y_i)^2$ for $y=(0,2,4)$ and start at $w=1$. The three gradients are $(1,-1,-3)$, their average is $-1$ and their sum is $-3$. A full-average-gradient step with rate $0.1$ gives $w=1.1$. Selecting the first case instead gives $w=0.9$. The full average losses are
$$
L(1)=11/6=1.83333,\quad L(1.1)=1.73833,\quad L(0.9)=1.93833.
$$
The sampled step increases the full loss. The one-draw gradient variance is $\{(1+1)^2+(-1+1)^2+(-3+1)^2\}/3=8/3$. Averaging two independent draws reduces it to $4/3$; averaging a uniformly chosen pair without replacement reduces it to $2/3$.

**Your turn.** If the sum objective is used with the same rate $0.1$, what full-gradient update results? Which rate on the sum gives the average-objective update $1.1$?

::: {.callout-tip collapse="true" title="Answer"}
The sum-gradient update is $1-0.1(-3)=1.3$. Rate $0.1/3=1/30$ on the sum gives $1.1$.
:::

## Assumptions and limits
Unbiasedness at a fixed weight does not imply monotone progress or convergence with a fixed step size. Diminishing rates and objective regularity enter convergence theorems. Randomly shuffling a dataset each epoch uses all cases but does not make each later within-epoch draw conditionally uniform over all cases given the current weight, because that weight depends on earlier cases. True streaming learning can also face a changing data distribution; repeatedly sampling one fixed dataset is a different experiment.{{cite:goodfellow_bengio_courville2016}} (§8.3.1, pp. 290–291, SGD step sizes)
