# Law of large numbers — rank 93

Type: theorem. Baseline 426 words and one figure. Preserve the coin-run figure, statement, voltage-reading example, citations and question links. New material supplies a finite-variance weak-law proof in one collapsed box; the general strong law remains unproved and is logged in pending.

## Sources opened

- **Checked:** Siegrist, *Probability, Mathematical Statistics, and Stochastic Processes*, §6.3, full online chapter, especially “Sample Mean,” “Weak and Strong Laws,” “Empirical Probability” and “Empirical Distribution Function.” The chapter derives variance of the sample mean, Chebyshev's weak law, a finite-variance strong-law proof, notes the integrable extension, and applies the result to indicators.
- **Checked:** authorized Dodge (2008), printed p. 39, “Bernoulli's Theorem,” for Bernoulli's 1713 history and the repeated-trial frequency interpretation. Dodge p. 297 discusses the law more generally.
- **Checked:** question answers `ex-inf-poisson-mle` and `ex-norm-mean`: the first invokes the law for a Poisson average; the second discusses a normal sample mean's limiting behavior. The voltage-reading question is embedded already.
- **Assumed:** the worked coin tosses are iid fair Bernoulli draws. The finite-variance weak-law proof applies to that model.
- **Disputed:** the source statement omits the iid assumptions and could imply the theorem for arbitrary identically distributed data. The added Statement section supplies them. The source's strong law needs an integrable common distribution; a finite variance is only needed for its displayed weak-law argument.

## Mathematical checks

For fair Bernoulli observations, mean 1/2, variance 1/4, Chebyshev bounds at tolerance 0.1 are 0.25 for 100 and 0.0625 for 400. Exact inclusive binomial tails are 0.05688793364098089 and 0.00007426568076372613 respectively. The page explicitly distinguishes strict bound from inclusive exact event. The perfect-dependence counterexample and the Cauchy stability claim were cross-checked against the law's assumptions and stable-distribution property.
