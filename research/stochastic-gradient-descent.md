# Stochastic gradient descent

Rank 308. Lighter tier. Concept page.

## Sources read

- Hastie, Tibshirani and Friedman, *The Elements of Statistical Learning*, 12th printing (2017 author PDF). Chapter 11, §11.4, p. 397: online learning replaces the batch sum by one summand; a training epoch is one sweep; stochastic approximation asks for $\gamma_r\to 0$, $\sum\gamma_r=\infty$ and $\sum\gamma_r^2<\infty$, with $\gamma_r=1/r$ as an example. §§11.5.1–11.5.2, pp. 397–398, read for the neighbouring initialisation and early-stopping paragraphs.
- Dodge (2008) index has no stochastic-gradient or gradient-descent entry. No Dodge citation.

## Checked

- Case gradient of $\tfrac12(x-w)^2$ is $w-x$. At $w=3$ the observations $2,4,6$ give gradients $1,-1,-3$, sum $-3$, mean $-1$.
- Steps of size $0.5$: single third case and the full sum both go to $4.5$; the average-gradient step goes to $3.5$.
- At $w=2$, gradients $0,-2,-4$, sum $-6$; step $0.2$ on observation $4$ goes to $2.4$; full-sum step goes to $3.2$.
- The factor-$n$ unbiasedness identity is proved on the page from uniform sampling.

## Assumed

- The training criterion is a sum of case losses, as in the ESL online-learning paragraph. No claim is made for a loss that does not separate across cases.

## Disputed or not used

- Robbins and Monro (1951) is the paper ESL cites for the step-size conditions. The Project Euclid PDF was blocked, so the article cites the conditions as ESL states them and does not cite Robbins–Monro.
- Convergence under those conditions is not proved. Logged in `research/pending/stochastic-gradient-descent.json`.

## Preserved

- The generated page keeps the source paragraph on online updates, the unbiasedness display, and the learning-rate warning. New prose adds the factor-$n$ distinction with a three-point calculation.
