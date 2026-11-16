## Intuition — A cheap, noisy step
Full-batch gradient descent waits until every training loss has been differentiated, then takes one step along their sum. Stochastic gradient descent draws one training case, or a small mini-batch, and steps on that piece alone. The step is cheap, so the weights move many times in the time a batch method makes one update. The direction is noisy: a single case can point uphill on the full loss even when the average of the cases points downhill.{{cite:hastie_esl2009}} (Ch. 11, §11.4, p. 397)

## Definition — The one-case gradient
Write the training criterion as a sum of case losses, $E(w)=\sum_{i=1}^n E_i(w)$. At the current weights, draw an index $I$ uniformly from $1,\ldots,n$ and replace the sum of gradients by the single summand $\nabla E_I(w)$. The update is $w\leftarrow w-\eta\,\nabla E_I(w)$, with learning rate $\eta>0$. Because the draw is uniform,
$$
\mathbb E\bigl[n\nabla E_I(w)\bigm|w\bigr]=\nabla E(w).
$$
The factor $n$ matters. Using $\nabla E_I$ in place of the average gradient $\nabla E/n$, with the same $\eta$, multiplies the typical step by $n$. Online training is a stochastic approximation: Hastie, Tibshirani and Friedman record that convergence arguments ask for a step size $\gamma_r$ with $\gamma_r\to 0$, $\sum_r\gamma_r=\infty$ and $\sum_r\gamma_r^2<\infty$, a pattern satisfied by $\gamma_r=1/r$. A fixed positive rate does not meet the first of those conditions.{{cite:hastie_esl2009}} (Ch. 11, §11.4, p. 397)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Condition on the current weights, so each $\nabla E_i(w)$ is a fixed vector. Uniform sampling gives $\mathbb P(I=i)=1/n$, and
$$
\mathbb E\bigl[\nabla E_I(w)\bigm|w\bigr]=\frac1n\sum_{i=1}^n\nabla E_i(w)=\frac1n\nabla E(w).
$$
Multiplying by $n$ recovers $\nabla E(w)$. The identity is unbiasedness of one gradient for the full sum, not a guarantee that the next step decreases $E$.{{cite:hastie_esl2009}} (Ch. 11, §11.4, p. 397)
:::
:::

## Worked example — Three squared errors
Suppose the parameter is a single number $w$ and the case loss is $\tfrac12(x_i-w)^2$, so the case gradient is $w-x_i$. The observations are $2$, $4$ and $6$, and the current value is $w=3$. The three gradients are $1$, $-1$ and $-3$. Their sum is $-3$, and the average of one uniformly chosen gradient is $-1$. Three times that average is $-3$, the full gradient.

A step of size $\eta=0.5$ on the third observation uses gradient $-3$ and moves to $3-0.5(-3)=4.5$. The same step size on the sum of the three gradients also moves to $4.5$. The same step size on the average gradient moves only to $3-0.5(-1)=3.5$. The two conventions differ by the factor $n=3$.{{cite:hastie_esl2009}} (Ch. 11, §11.4, p. 397)

**Your turn.** Keep the same three observations and the case gradient $w-x_i$. Start at $w=2$ and take one step of size $0.2$ using only the observation $4$. Report the three gradients at $w=2$, their sum, and the updated weight.

::: {.callout-tip collapse="true" title="Answer"}
The gradients are $2-2=0$, $2-4=-2$ and $2-6=-4$, with sum $-6$. The observation $4$ contributes $-2$, so the update is $2-0.2(-2)=2.4$. The full-sum step of the same size would be $2-0.2(-6)=3.2$.{{cite:hastie_esl2009}} (Ch. 11, §11.4, p. 397)
:::

## Check yourself
Two short calculations. Open an answer only after you have a number.

### The flat point
All three observations equal $5$, and $w=5$. What is every case gradient, and does a step of any size move $w$?

::: {.callout-tip collapse="true" title="Answer"}
Each gradient is $5-5=0$, so the update subtracts zero and $w$ stays at $5$. Unbiasedness is not the issue: the full gradient is zero as well.
:::

### A constant step size
Hastie, Tibshirani and Friedman ask for $\gamma_r\to 0$, $\sum_r\gamma_r=\infty$ and $\sum_r\gamma_r^2<\infty$. Which of $\gamma_r=1/r$ and $\gamma_r=0.1$ meets $\gamma_r\to 0$?

::: {.callout-tip collapse="true" title="Answer"}
The sequence $1/r$ tends to zero. The constant $0.1$ does not, so it fails the first condition. The harmonic choice is the example they give of a rate that meets all three.{{cite:hastie_esl2009}} (Ch. 11, §11.4, p. 397)
:::

## Connections — Where the noise is spent
One pass through the training cases is an [epoch](epoch.qmd); online updates make many steps inside one epoch, while batch [gradient descent](gradient-descent.qmd) makes one. The step length is the [learning rate](learning-rate.qmd). A [mini-batch](mini-batch.qmd) averages a few case gradients and sits between the two extremes. [Early stopping](early-stopping.qmd) watches a validation curve along this path and may halt before the training loss has finished falling. The starting [weight initialisation](weight-initialisation.qmd) decides which noisy path is followed.{{cite:hastie_esl2009}} (Ch. 11, §§11.4–11.5, pp. 397–398)
