# Output coding, softmax, and cross-entropy

Type: Concept. Rank 247. Tier: full.

## Material checked

- **Checked:** Frozen baseline 750 body words and no figures. The page keeps the one-hot coding, the softmax definition, the cross-entropy loss, the gradient identity $s-y$, and the worked scores $(2,1,0.1)$.
- **Checked:** Hastie, Tibshirani and Friedman, pp. 393–395. Equation (11.6) is the softmax. Equation (11.10) is the cross-entropy. The text states that softmax plus cross-entropy makes the output layer a linear logistic regression in the hidden units.
- **Checked:** Shannon, Theorem 2, the entropy $-\sum p\log p$ as average surprise. The training loss is that expression with a one-hot weight.
- **Checked by code:** Scores $(0,1,-1)$ give probabilities $0.2447$, $0.6652$, $0.0900$ and cross-entropy $0.4076$. Scores $(2,1,0.1)$ give $0.659$, $0.242$, $0.099$ and cross-entropy $0.417$. Two scores differing by $1$ give probability $0.7311$ and cross-entropy $0.3133$.
- **Assumed:** The logarithm is natural. The label coordinates sum to $1$ in the gradient identity.
- **Disputed:** None. Bridle (1990) is cited on the copied derivation and was not reopened.

## Sources opened and used

1. Hastie, Tibshirani and Friedman, *The Elements of Statistical Learning*, §§11.3–11.4, pp. 393–395. Key `hastie_esl2009`.
2. C. E. Shannon, *A Mathematical Theory of Communication* (1948), Theorem 2. Key `shannon1948`.
