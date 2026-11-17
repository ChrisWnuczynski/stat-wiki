## Motivating example
Twenty training cases in batches of four make five updates in one epoch. Twelve updates are $12/5=2.4$ epochs: two full passes, then two batches of a third pass.

## Intuition — One pass, however the weights are updated
An epoch is one complete look at the training cases. In batch learning that look produces a single weight update, because the gradient sum uses every case before anything moves. In online learning the weights move after each case, so one epoch contains as many updates as there are training cases. Counting epochs, rather than counting updates, is what makes those two schedules comparable.{{cite:hastie_esl2009}} (Ch. 11, §11.4, p. 397)

## Definition — A sweep of the training set
If the training set has $n$ cases, one epoch presents each of them once. Batch gradient descent then performs one update per epoch. Online gradient descent performs $n$ updates per epoch. A mini-batch of size $m$, with $m$ dividing $n$, performs $n/m$ updates per epoch. A run of $u$ updates has lasted $u/(n/m)=um/n$ epochs under that mini-batch schedule. Shuffling the cases at the start of each epoch changes the order inside the pass; it does not change the definition of the pass.{{cite:hastie_esl2009}} (Ch. 11, §11.4, p. 397)

## Worked example — Twenty cases, batches of four
Let $n=20$ and $m=4$. One epoch is $20/4=5$ updates. Twelve updates are $12/5=2.4$ epochs: two full passes, and then two of the five batches of a third pass.

The cost is not the same thing as the epoch count. Three epochs of batch learning read $3\times 20=60$ case-gradients and produce $3$ updates. Twelve online updates read $12$ case-gradients and produce $12$ updates. The online run has seen fewer epochs and has moved the weights more often.{{cite:hastie_esl2009}} (Ch. 11, §11.4, p. 397)

**Your turn.** With $n=20$ and mini-batches of size $5$, how many updates make one epoch, and how many epochs is $8$ updates?

::: {.callout-tip collapse="true" title="Answer"}
One epoch is $20/5=4$ updates. Eight updates are $8/4=2$ epochs.
:::

## Check yourself
### Batch versus online
A training set has $5000$ cases. How many online updates equal one epoch, and how many batch updates equal one epoch?

::: {.callout-tip collapse="true" title="Answer"}
Online learning updates after every case, so one epoch is $5000$ updates. Batch learning updates once from the full sum, so one epoch is $1$ update.
:::

### A remainder
With $n=20$ and $m=4$, a run stops after $7$ updates. How many full epochs have finished, and how many batches of the next epoch have been used?

::: {.callout-tip collapse="true" title="Answer"}
Five updates finish the first epoch. The next two updates are two of the five batches of the second epoch. The run has completed $1$ epoch and $2/5$ of the next, which is $7/5=1.4$ epochs.
:::

## Connections — The unit on the training curve
[Early stopping](early-stopping.qmd) reads the validation error against this clock and keeps the epoch with the smallest validation error. [Stochastic gradient descent](stochastic-gradient-descent.qmd) is the online end of the schedule, and the [learning rate](learning-rate.qmd) is the length of each update inside the epoch. A [mini-batch](mini-batch.qmd) is the intermediate schedule whose updates per epoch are $n/m$.{{cite:hastie_esl2009}} (Ch. 11, §11.4, p. 397)
