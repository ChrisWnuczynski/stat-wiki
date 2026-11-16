# Out-of-bag estimation and variable importance

Rank 317. Lighter tier. Concept page.

## Sources read

- ESL, Chapter 8, §8.2, printed p. 264: bootstrap datasets of size $N$ are drawn with replacement.
- ESL, Chapter 15, §§15.3.1–15.3.2, printed pp. 592–594. Out-of-bag predictions use only the trees whose bootstrap samples omitted the case. The error is described as almost $N$-fold cross-validation. Permutation importance averages the drop in out-of-bag accuracy. A refit without the variable could use a surrogate, so the drop is not that refit's effect.

## Checked

- $(4/5)^5=1024/3125=0.32768$, which rounds to $0.3277$. $e^{-1}$ rounds to $0.3679$.
- Drops $0.20$, $0.10$, $0.00$ average to $0.10$.
- $n=2$ omission probability $(1/2)^2=0.25$.
- Revised drops $0.20$, $0.10$, $0.15$ average to $0.15$.
- The limit $(1-1/n)^n\to e^{-1}$ is proved from the derivative of $\log$ at $1$.

## Illustration

The three accuracies are an arithmetic illustration of the average ESL defines. They are not the output of a fitted forest.
