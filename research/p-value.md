# p-value — rank 91

Type: concept/definition. Baseline: 731 words, 2 figures. Preserve the gene and caffeine examples, both figures, infobox and citation links. Their numerical results were independently recomputed.

## Sources opened

- **Checked:** Siegrist, *Probability, Mathematical Statistics, and Stochastic Processes*, §9.1 “Introduction to Hypothesis Testing,” especially P-value and Power. Read full online textbook section. The p-value is the smallest level in nested rejection regions and is a null-tail probability when a direction of extremeness is defined.
- **Checked:** American Statistical Association, 7 March 2016 press release “American Statistical Association Releases Statement on Statistical Significance and P-Values,” full official PDF. Read all six principles, especially model incompatibility, no posterior probability, no effect magnitude, and transparency. The underlying Wasserstein–Lazar (2016) publisher paper was also opened for the statement's context.
- **Checked:** Dodge (2008) printed pp. 434–435 for orientation and its one-sided normal illustration; its history and one sentence about the rejection rule are disputed below.
- **Checked:** question-bank answers `ex-da-brexit-poll` (two-sided normal tail), `ex-da-possums` (chi-square tail), `q-37` (what an approximate smooth-term p-value tests).
- **Checked:** printed baseline gene example: doubled lower binomial tail 0.198895; normal approximation 0.161429 and continuity-corrected 0.207578. Caffeine example: t=2.575, one-sided t39 tail 0.006966, 99% lower bound 19.033, two-sided 99% interval (18.971,20.169). All retain their existing rounding.
- **Assumed:** the new coin example uses 20 independent Bernoulli(1/2) trials under its null; its prechosen one-sided and two-sided tails have their stated meanings.
- **Disputed:** Dodge says the p-value was introduced by Gibbens and Pratt in 1975, which conflicts with earlier statistical use, and says p is the smallest level at which the null “cannot” be rejected, the opposite of its own decision rule. The page does not repeat these claims.

## Mathematical checks

For n=20, k=15, `P(K>=15)=21700/1048576=0.0206947327`; two-sided symmetry doubles it to 0.0413894653. For n=12, k=9, one-sided tail `299/4096=0.0729980469`, two-sided 0.1459960938. Twenty independent level-0.05 tests have family-wise false-positive chance `1-.95**20=0.641514`. The collapsed proof establishes null superuniformity for a prespecified tail.
