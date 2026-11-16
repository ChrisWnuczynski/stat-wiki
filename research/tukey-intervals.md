# Tukey intervals

Type: Concept. Rank 280. Tier: lighter.

## Facts

- **Checked by code:** `scipy.stats.studentized_range.ppf(0.95, 5, 10)` equals \(4.654\) to three decimals, matching the corn quantile already printed in the source chapter. For \(k=3\), \(\nu=8\), the same function gives \(4.041\) to three decimals. With \(S^2=6.25\) and \(r=4\), the half-width rounds to \(5.051\). Differences \(8\), \(4\), \(6\) and \(0\) produce the printed endpoints. Doubling the scale through \(S^2=25\) gives half-width \(10.103\).
- **Checked:** The coverage identity is the equality between \(\{|Z_i-Z_j|\le Q S/\sigma\ \text{for all pairs}\}\) and \(\{R\le Q\}\), using \(|Z_i-Z_j|\le\max Z-\min Z\).
- **Assumed:** Independent normal groups, equal size \(r\), common variance, and \(S^2\) the usual error mean square, independent of the means.
- **Disputed:** Nothing numerical. Tukey (1949) and Scheffé (1959) were not opened. Dodge pp. 542–543 is a biography and does not state the interval, so it is not cited for the method. The corn figure and the five-variety table stay as they are.

## Sources opened

SciPy’s studentised-range quantile, checked against the corn value \(4.654\). Dodge (2008), printed pp. 542–543, Tukey biography only.

## Proofs

Simultaneous coverage is proved as the event \(R\le Q\). The density of the studentised range is not derived.
