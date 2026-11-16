# Complete-data likelihood

Rank 321. Lighter tier. Concept page.

## Sources read

- Bishop, *Pattern Recognition and Machine Learning*, equations (9.35) and (9.36) on printed p. 443: the complete-data likelihood is the product $\prod_n\prod_k \pi_k^{z_{nk}} \mathcal N(x_n\mid\mu_k,\Sigma_k)^{z_{nk}}$, and the log is linear in the indicators. Equation (9.30), the $Q$ function, is on pp. 440–441.

## Checked

- Weights $0.4$ and $0.6$. First case densities $0.5$ and $0.1$; second $0.2$ and $0.8$.
- Complete contributions $0.2$ and $0.48$; product $0.096$. $\ln 0.096$ rounds to $-2.343$.
- Observed contributions $0.26$ and $0.56$; product $0.1456$. $\ln 0.1456$ rounds to $-1.927$.
- Switched first label: $0.06$, and $0.06\times 0.48=0.0288$.
- The one-case product with a zero exponent is proved on the page.

## Not claimed

The numerical densities are stand-ins for $f_h(x_i)$, not evaluations of a fitted normal. Bishop's displayed equation specialises $f_h$ to the normal density.
