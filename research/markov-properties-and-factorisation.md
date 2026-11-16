# Markov properties and factorisation

Type: concept. Rank 303. Tier: lighter.

## Facts

- **Checked:** Evans, *Graphical Models*, §4.2 Definitions 4.3 and 4.4 and Proposition 4.1; §4.3 Definition 4.6, equation (4.1), Theorems 4.1 and 4.2. Factorisation implies the global Markov property. The converse uses positivity.
- **Checked by code:** The chain example has joint probability $1/4$ and marginal joint $7/24$, against a product $6/24$. The precision matrix has determinant $8$, inverse as displayed, marginal correlation $0.2$, and partial correlation $1/\sqrt{6}\approx 0.408$.
- **Assumed:** The three binary conditionals are a valid conditional specification because they are defined from $X_2$ outward.
- **Disputed:** None. The Hammersley–Clifford converse is cited and not proved.

## Sources read

1. Robin J. Evans, Graphical Models, https://www.stats.ox.ac.uk/~evans/gms/_book/ug.html, sections 4.2 and 4.3.
