# Kullback–Leibler divergence

Type: Concept. Rank 238. Tier: full.

## Material checked

- **Checked:** Frozen baseline 538 body words and no figures. The page keeps the Bernoulli comparison of $0.9$ against $0.5$, whose values round to $0.368$ and $0.511$ nats.
- **Checked:** Shannon, *A Mathematical Theory of Communication*, Bell System Technical Journal, 1948, the reprinted text. Theorem 2 states that the entropy satisfying his assumptions has the form $H=-K\sum p_i\log p_i$.
- **Checked:** Hastie, Tibshirani and Friedman, *The Elements of Statistical Learning*, p. 561. Mutual information is identified with the Kullback–Leibler discrepancy between a joint density and the product of its marginals. Differential entropy is equation (14.82) on that page.
- **Checked by code:** For $p=(0.8,0.2)$ and $q=(0.5,0.5)$, the divergences round to $0.1927$ and $0.2231$ nats, the first is $0.2781$ bits, and $D(p\,\Vert\,(0.9,0.1))$ rounds to $0.0444$.
- **Assumed:** Natural logarithms unless a base is named. The support condition $q_i>0$ when $p_i>0$ is in force for a finite value.
- **Disputed:** None. Dodge has no entry under this name.

## Sources opened and used

1. C. E. Shannon, *A Mathematical Theory of Communication*, Bell System Technical Journal **27** (1948), Theorem 2. Key `shannon1948`. Reprint read from the PDF beginning “Reprinted with corrections”.
2. Hastie, Tibshirani and Friedman, *The Elements of Statistical Learning*, 12th printing, p. 561. Key `hastie_esl2009`.
