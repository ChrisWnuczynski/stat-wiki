# Chi-squared test of independence

Rank 320. Lighter tier. Concept page.

## Sources read

- Dodge (2008), printed pp. 79–80. Expected frequency $n_{i\cdot}n_{\cdot j}/n_{\cdot\cdot}$, the chi-squared sum of squared gaps over those frequencies, degrees of freedom $(r-1)(c-1)$, rejection when the calculated value exceeds the table value, and the warning for estimated frequencies below $5$. The entry also requires a random sample and one cell per individual.
- The $0.95$ quantile of $\chi^2_1$ is computed from that reference law, not read off Dodge's table.

## Checked

- Margins $30$, $30$, $28$, $32$, $n=60$. Fitted counts $14,16,14,16$.
- Contributions sum to $30/7=4.2857\ldots$, printed $4.286$.
- $\chi^2_{1;0.95}$ rounds to $3.841$. Upper tail past $30/7$ rounds to $0.0384$.
- A table equal to the fitted counts has $T=0$.
- A $3\times 4$ table has $6$ degrees of freedom.
- The degrees-of-freedom count $rc-1-(r-1)-(c-1)$ is proved on the page. The chi-squared limit is not.

## Not opened

- Pearson (1900), Fisher (1922) and Agresti were not reopened. The source definition still cites them. The anaemia figure is untouched.
