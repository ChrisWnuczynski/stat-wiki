# Wald interval

Rank 311. Lighter tier. Concept page.

## Sources read

- Durrett, Theorem 3.1.3, printed p. 115: De Moivre–Laplace. For symmetric $\pm 1$ steps, $S_m/\sqrt m$ converges in distribution to standard normal. For a fair coin this is $(\widehat p-1/2)$ divided by $1/(2\sqrt n)$.
- Siegrist, §5.6: the standard normal density $(2\pi)^{-1/2}e^{-z^2/2}$. The number $1.96$ is the computed $0.975$ quantile of that density, rounded to two decimal places. Siegrist's section, as read, states the density and does not print the quantile $1.96$.

## Checked

- $n=100$, $X=40$: variance estimate $0.0024$, standard error $0.04899$ rounds to $0.0490$, half-width with $1.96$ rounds to $0.096$, interval $(0.304, 0.496)$.
- Fair coin: standard error $0.05$, half-width $0.098$, interval $(0.402, 0.598)$.
- $X=0$: standard error $0$, interval $\{0\}$.
- $X=10$: standard error $0.03$, half-width $0.0588$, interval $(0.0412, 0.1588)$.
- $p(1-p)$ is maximised at $p=1/2$ with value $1/4$.
- `norm.ppf(0.975)` rounds to $1.96$.

## Not proved

- Coverage of the plug-in interval for a general $p$ is not De Moivre–Laplace. It is logged in the pending proofs list. Brown, Cai and DasGupta (2001) and Wald (1943) are cited by the source definition; those papers were not opened for this pass.

## Disputed

- None inside the calculations. The source table for the two-group example uses $1.96$ as well; the new example uses the same multiplier.
