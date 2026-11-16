# Chi-squared distribution — rank 164

Type: distribution. Baseline 1,009 words and two figures. Preserve PDF/CDF plots, infobox, normal-sample theorem, Pearson results, three worked examples, squared-normal example, links and source citations where supported.

## Sources opened

- Siegrist (2022), *Probability, Mathematical Statistics, and Stochastic Processes*, authorized full LibreTexts §5.9 *Chi-Square and Related Distribution*: density, CDF, gamma relation, MGF, sums, positive real degrees of freedom, shape and normal approximation. §6.8 *Special Properties of Normal Samples*: normal sample mean/variance independence and exact variance pivot.
- NIST/SEMATECH, *e-Handbook of Statistical Methods*, full §1.3.6.6.6 *Chi-Square Distribution*: density, CDF, shape, moments. Full §1.3.5.15 *Chi-Square Goodness-of-Fit Test*: binned multinomial statistic, expected counts, count-based MLE, parameter penalty, sample-size requirements.
- Dodge (2008), printed pp. 70–72, *Chi-square Distribution* and adjacent *Chi-square Goodness of Fit Test*: sum-of-squares and moment statements, uses, and historical accounts of Bienaymé, Abbe, Maxwell, Boltzmann and Pearson. Pearson 1900 for testing is also documented there.

## Fact ledger

- **Checked:** For positive real `nu`, chi-square is Gamma(shape `nu/2`, rate `1/2`) with stated density, CDF, MGF, mean `nu`, variance `2nu`, skewness `sqrt(8/nu)` and mode `nu-2` for `nu>2` (Siegrist §5.9; NIST §1.3.6.6.6). For integer `nu`, it is a sum of independent squared standard normals.
- **Checked:** Independent chi-square variables add their degrees of freedom; a normalized ratio gives F when independent. Orthogonal Gaussian rotation yields the exact `n-1` sample variance pivot and independence from sample mean (Siegrist §§5.9, 6.8).
- **Checked:** Fixed positive multinomial probabilities yield asymptotic `chi2_(k-1)` Pearson statistic; fitting `r` regular free parameters by binned-count MLE gives `chi2_(k-1-r)` under regularity and sufficiently large counts (NIST §1.3.5.15). Projection argument in single Proof box.
- **Checked:** Existing aspirin and tuning-fork numerics and new four-normal and Your-turn calculations verified in `checks/chi-squared-distribution.py` with SciPy.
- **Assumed:** Independent normal sampling for exact sample-variance inference; sufficiently large expected cells, identifiable smooth model, and binned-count MLE for the usual fitted-parameter Pearson limit.
- **Disputed:** Dodge p. 71 reports conflicting historical priority accounts for the distribution (Bienaymé 1838 versus Maxwell 1860/Abbe 1863). The article makes no single-discoverer claim. Pearson's 1900 approximation with fitted parameters was later corrected; the plain fitted-parameter rule needs the stated regular estimation assumptions.
