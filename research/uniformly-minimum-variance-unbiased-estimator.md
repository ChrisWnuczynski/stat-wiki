# Uniformly minimum-variance unbiased estimator

Type: Concept. Rank 281. Tier: lighter.

## Facts

- **Checked by code:** For \(n=4\), \(k=1\), \(T=3\), \(U=27/64=0.421875\) and the plug-in is \(0.3543\) to four decimals. For \(T=2\), \(k=0\), \(U=0.5625\) and \(e^{-1/2}=0.6065\) to four decimals. For \(n=2\), \(k=0\), \(T=1\), \(U=1/2\).
- **Checked:** The conditional law \(X_1\mid T=t\sim\operatorname{Binomial}(t,1/n)\) for independent identical Poisson variables follows by writing the joint and marginal masses and cancelling \(e^{-\theta}\theta^{t}\). The tower property then gives unbiasedness. Jensen's inequality for the strictly convex map \(e^{-x}\) shows that \(e^{-\overline X}\) is biased high for \(e^{-\theta}\).
- **Assumed:** Independent Poisson observations with a common mean, and a non-degenerate sample mean when Jensen is applied.
- **Disputed:** Nothing numerical. Lehmann–Scheffé (1950) was not opened. Completeness, and therefore uniqueness, is not proved.

## Sources opened

The Poisson conditional-probability algebra was derived in this note. Dodge's Estimator entry (printed p. 185) is a historical pointer and does not state the UMVU definition, so it is not cited.

## Proofs

Unbiasedness of \(U(T)\) and the plug-in bias for \(e^{-\theta}\) are proved. Uniqueness under completeness is logged.
