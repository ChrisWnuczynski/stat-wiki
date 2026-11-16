# Significance level

Type: Topic. Rank 251. Tier: full.

## Material checked

- **Checked:** Baseline 186 words and no figures. NIST §1.3.5.2 was read for the definition of $\alpha$, the critical region, and the numerical normal-mean example. The $t_{194}$ quantile 1.9723 and the one-sided quantile 1.6527 match SciPy. The interval endpoints were recomputed as $(9.258241,\ 9.264679)$. NIST's printed statistic 2611.284 was not reproduced exactly from the printed mean and standard deviation; the article says "about 2611" and the recomputed value is 2611.26.
- **Checked:** Dodge pp. 250–251 lists the significance level as step 2 of a test and gives the Neyman–Pearson history used on the page. The 1928 and 1933 papers were not reopened.
- **Checked by code:** binomial size 0.0271, power 0.8159, blood-pressure cutoff 1.365, chi-squared boundary 0.2998.

## Sources opened

1. NIST/SEMATECH §1.3.5.2. Key `nist_mean_limits2002`.
2. Dodge (2008), pp. 250–251, local `pdf-0252.txt`. Key `dodge2008`.
