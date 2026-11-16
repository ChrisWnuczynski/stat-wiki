# Gini index

Rank 316. Lighter tier. Concept page.

## Sources read

- ESL, Chapter 9, §9.2.3, printed pp. 309–310. The Gini index is $\sum_{k\neq k'}\hat p_k\hat p_{k'}=\sum_k\hat p_k(1-\hat p_k)$. It is the error of a randomised classification by the node proportions, and the sum of the Bernoulli variances. Page 593 mentions Gini decrease as one forest importance.
- Dodge (2008), printed p. 231. The income Gini coefficient is the area between the Lorenz curve and the diagonal, in $[0,1]$, and the index multiplies it by $100$. That is a different object.

## Checked

- Proportions $0.6,0.2,0.2$: both Gini expressions equal $0.56$. Misclassification $0.4$. Natural-log entropy rounds to $0.9503$.
- Eight and two: $2\cdot 0.8\cdot 0.2=0.32$, misclassification $0.2$.
- Two-class value at $p=1/2$ is $1/2$.
- The algebraic identity is proved on the page.

## Not opened

- Gini (1912) and Breiman, Friedman, Olshen and Stone (1984) are cited by the source definition and were not reopened.
