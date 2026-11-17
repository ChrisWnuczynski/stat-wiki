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

## Intuition
A full-batch step looks at every case before it moves. An online step looks at one case, or a small batch, and moves immediately. If the case is drawn uniformly from a fixed data set, the gradient of that one case is a noisy version of the average gradient. Its expectation, at a frozen weight, equals the gradient of the average loss. It does not equal the gradient of the sum unless it is multiplied by the sample size. A particular draw can point uphill on the full loss. Unbiasedness is a statement about the average over draws, not a promise about the next draw.{{cite:goodfellow_bengio_courville2016}} (§8.1.3, pp. 274–275)

## Definition
Let $L(w)=n^{-1}\sum_{i=1}^n L_i(w)$ be the average loss and let $I$ be uniform on the $n$ cases, drawn independently of the current weight. Then $E\{\nabla L_I(w)\mid w\}=\nabla L(w)$. If the objective being optimized is the sum $nL(w)$, the unbiased single-case estimate is $n\nabla L_I(w)$. For $b$ independent draws with replacement, the covariance of the averaged gradient is the one-draw covariance divided by $b$. Sampling without replacement from a finite data set is more precise: the two-case calculation below cuts the variance from $4/3$ to $2/3$. Nonuniform sampling needs importance weights if the target is still the ordinary average gradient.{{cite:zhang_d2l2023}} (§12.4.1, stochastic gradient expectation){{cite:goodfellow_bengio_courville2016}} (§8.1.3, eqs. 8.4–8.6)

## Statistical use
The learning rate has to be read in the same units as the objective. In the three-point example the average gradient at $w=1$ is $-1$ and the sum gradient is $-3$. Rate $0.1$ on the average moves the weight to $1.1$. The same rate on the sum moves it to $1.3$. Rate $1/30$ on the sum matches the average-objective step. Comparing algorithms by their nominal rates is meaningless until this convention is fixed. Larger batches reduce gradient noise at a fixed weight and cost more computation per step. They do not change the identity of the minimizer of a fixed empirical loss. A streaming problem, in which the distribution of new cases can change, is a different target from reshuffling one fixed data set.{{cite:goodfellow_bengio_courville2016}} (§8.3.1, pp. 290–291, SGD step sizes)

## Common misconceptions
One uphill step does not refute unbiasedness. In the example, using the first case moves the weight from $1$ to $0.9$ and raises the average loss from $1.83333$ to $1.93833$. The full gradient would have lowered it to $1.73833$. The unlucky case is one of three equally likely draws; the average of the three gradients is still the full gradient. A second confusion is to treat a pass through a shuffled epoch as a sequence of conditionally unbiased draws. After the first case has been used, the weight depends on that case, and the next draw is taken from the remaining cases. A third confusion is to keep a constant step size and expect a theorem that assumed a diminishing step size. Unbiased noisy gradients can orbit a minimizer forever if the step size does not go to zero.{{cite:zhang_d2l2023}} (§12.4.1, “Stochastic Gradient Updates”)

## Interpretation
Read the learning rate in the units of the objective that is being differentiated. In the three-point example the average gradient at weight $1$ is $-1$ and the sum gradient is $-3$. A step of size $0.1$ along the average gradient moves the weight to $1.1$ and lowers the average loss from $1.83333$ to $1.73833$. The same nominal step along the sum gradient moves the weight to $1.3$. Matching the average-objective step with the sum objective requires the rate $1/30$. Comparing two algorithms by the number written next to the step size is meaningless until that convention is fixed.

The noise calculation has the same bookkeeping. One uniform draw from the three gradients has variance $8/3$ at the frozen weight. Averaging two draws with replacement cuts that variance to $4/3$. Drawing two distinct cases without replacement cuts it further, to $2/3$. A larger batch buys a quieter gradient at a frozen weight and costs more computation per move. It does not change the minimizer of a fixed empirical loss. A draw can still point uphill on that loss. The unlucky first case moves the weight from $1$ to $0.9$ and raises the average loss to $1.93833$. The average of the three possible gradients remains the full gradient.{{cite:goodfellow_bengio_courville2016}} (§8.1.3, eqs. 8.4–8.6)
