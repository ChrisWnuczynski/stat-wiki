## Lead context
A mini-batch is a small group of training cases whose average gradient replaces the gradient of the whole training set for one weight update.

## Motivating example
A full pass through a large training set, before a single step, recomputes almost the same gradient many times when the cases are redundant. A step from one case is cheap and noisy. A mini-batch sits between those extremes: it averages a handful of cases, so the step is cheaper than a full pass and less noisy than a single case.{{cite:lecun_efficient_backprop1998}} (§4.1, mini-batches){{cite:hastie_esl2009}} (§11.4, pp. 396–397)

## Intuition — Noise against cost
Write the training loss as the average of per-case losses. The gradient of that average is the average of the per-case gradients. Batch learning uses the whole average. Online learning uses one case. A mini-batch uses the average over a subset. If the subset is a simple random sample, that subset average is an unbiased estimate of the full gradient, and its variance falls as the subset grows. LeCun, Bottou, Orr and Müller describe one use of this knob: start with a small batch, while the noise helps the search leave poor basins, and enlarge the batch as training proceeds, so the updates can settle. The batch size and the learning rate play similar roles. A larger batch is a less noisy step.{{cite:lecun_efficient_backprop1998}} (§4.1, stochastic versus batch){{cite:hastie_esl2009}} (§11.4, p. 397)

## Definition — The subset gradient
Let the average loss be $L(w)=n^{-1}\sum_{i=1}^n \ell_i(w)$, and let $B$ be a subset of size $m$. The mini-batch gradient is
$$
g_B(w)=m^{-1}\sum_{i\in B}\nabla\ell_i(w).
$$
One update is $w\leftarrow w-\gamma g_B(w)$. If $B$ is drawn uniformly from the subsets of size $m$, then $\E[g_B(w)]=\nabla L(w)$ at the current $w$. An epoch is one sweep that has, between its subsets, used each training case once.{{cite:hastie_esl2009}} (§11.4, p. 397){{cite:lecun_efficient_backprop1998}} (§4.1)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For the squared loss $\ell_i(w)=\tfrac12(w-y_i)^2$ in one dimension, $\nabla\ell_i(w)=w-y_i$, so $g_B(w)=w-m^{-1}\sum_{i\in B} y_i$. At $w=0$ this is minus the mean of the selected responses. Averaging $g_B(0)$ over every subset of size $m$, each point appears equally often, so the average of the subset means equals the mean of all $n$ responses. Hence the average of the subset gradients equals the full gradient.{{cite:hastie_esl2009}} (§11.4, batch and online updates)
:::
:::

## Worked example
Take responses $1,3,5,7$ and $w=0$, with $\ell_i(w)=\tfrac12(w-y_i)^2$. The full gradient is
$$
g=0-\frac{1+3+5+7}{4}=-4.
$$
The mini-batch $\{1,5\}$ has gradient $-(1+5)/2=-3$. The complementary batch $\{3,7\}$ has gradient $-5$. The average of these two gradients is $-4$, the full gradient. There are $\binom{4}{2}=6$ batches of size $2$, with gradients $-2,-3,-4,-4,-5,-6$. Their mean is $-24/6=-4$. A single batch is not the full gradient. The uniform draw of a batch is unbiased for it.

**Your turn.** At the same $w=0$, find the gradient of the batch $\{1,3,7\}$.

::: {.callout-tip collapse="true" title="Answer"}
The batch mean is $(1+3+7)/3=11/3$, so the gradient is $-11/3=-3.66667$. It is closer to $-4$ than the single-case gradient $-1$ is, and it is not equal to $-4$.
:::

## Connections — Batch, online, and the learning rate
[Batch and online learning](batch-and-online-learning.qmd) are the two extremes this average sits between. The [backpropagation batch form](backpropagation-batch-form.qmd) is the full sum that a mini-batch replaces by a partial sum. Online learning is stochastic approximation: the learning rate should decrease, with $\sum \gamma_r=\infty$ and $\sum \gamma_r^2<\infty$, if one wants the noise to die out. Enlarging the mini-batch is another way to reduce that noise without changing $\gamma$.{{cite:hastie_esl2009}} (§11.4, p. 397){{cite:lecun_efficient_backprop1998}} (§4.1, learning rate and batch size)

## Check yourself

### One case
For the responses $1,3,5,7$ at $w=0$, what is the online gradient on the case $y=7$?

::: {.callout-tip collapse="true" title="Answer"}
The gradient is $0-7=-7$. It is an unbiased draw from the four case gradients $-1,-3,-5,-7$, whose mean is $-4$, but this particular draw is far from $-4$.
:::

### A deterministic partition
Why is the average of the gradients on $\{1,5\}$ and $\{3,7\}$ exactly $-4$, even though neither batch was drawn at random?

::: {.callout-tip collapse="true" title="Answer"}
The two batches partition the sample, so the average of their means is the mean of all four responses. Random sampling is not required for that identity. Unbiasedness of one batch requires the random draw.
:::
