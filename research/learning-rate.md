# Learning rate

Type: Concept. Rank 239. Tier: full.

## Material checked

- **Checked:** Frozen baseline 436 body words and no figures. The page keeps the quadratic $E(w)=(w-3)^2$, the multiplier $1-2\varepsilon$, the five steps from $0$ at $\varepsilon=0.1$, and the oscillation at $\varepsilon=1$.
- **Checked:** Hastie, Tibshirani and Friedman, *The Elements of Statistical Learning*, pp. 396–397. Equation (11.13) is the gradient step with learning rate $\gamma_r$. The online schedule is required to satisfy $\gamma_r\to 0$, $\sum\gamma_r=\infty$, and $\sum\gamma_r^2<\infty$, with $1/r$ as an example, in the stochastic-approximation paragraph on p. 397.
- **Checked by code:** From $w=5$ and $\varepsilon=0.1$ the iterates are $4.6$, $4.28$, $4.024$, $3.8192$. From the same start and $\varepsilon=0.4$ they are $3.4$ and $3.08$. At $\varepsilon=1.1$ the next weight is $0.6$ and the absolute error is $2.4$.
- **Assumed:** The quadratic has a constant second derivative $2$, so the contraction threshold is exactly $0<\varepsilon<1$. A neural-network loss is only locally of that form.
- **Disputed:** None. Widrow and Hoff (1960) and Robbins and Monro (1951) are named as ESL names them on p. 397. Those two papers were not reopened.

## Sources opened and used

1. Hastie, Tibshirani and Friedman, *The Elements of Statistical Learning*, 12th printing, §§11.4–11.5, pp. 396–397. Key `hastie_esl2009`.
