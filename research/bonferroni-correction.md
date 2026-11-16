# Bonferroni correction

Type: Concept. Rank 243. Tier: full.

## Material checked

- **Checked:** Frozen baseline 401 body words and one figure. The page keeps the level-$\alpha/m$ definition and the cold-sore comparison that sits in the source section.
- **Checked:** Hastie, Tibshirani and Friedman, p. 686. The Bonferroni rule is to reject $H_{0j}$ when $p_j<\alpha/M$, which makes the family-wise error at most $\alpha$. For independent tests the family-wise error is $1-(1-\alpha)^M$ before any correction.
- **Checked:** Dodge, printed pp. 50–51. Carlo Emilio Bonferroni, born 1892 in Bergamo, and the 1936 paper in which the inequalities appeared.
- **Checked:** Durrett, Theorem 1.1.1(ii), countable subadditivity, used as the union bound.
- **Checked by code:** $1-0.95^4$ rounds to $0.1855$, $1-0.9875^4$ rounds to $0.0491$, $1-e^{-0.05}$ rounds to $0.0488$, and the adjusted values $0.08$, $0.04$, and $0.06$ match $m$ times the raw $p$-values.
- **Assumed:** Each individual test has type I error exactly the nominal level when the null is true. The independent calculation adds independence on top of that.
- **Disputed:** None. Dunn (1961) is cited on the copied definition and was not reopened.

## Sources opened and used

1. Hastie, Tibshirani and Friedman, *The Elements of Statistical Learning*, §18.7, p. 686. Key `hastie_esl2009`.
2. Yadolah Dodge, *The Concise Encyclopedia of Statistics* (2008), pp. 50–51. Key `dodge2008`.
3. Rick Durrett, *Probability: Theory and Examples*, version 5, 11 January 2019, Theorem 1.1.1(ii). Key `durrett2019`.
