# Precision — research record

Page type: concept. Rank 83. Baseline: 203 words, no figures. Existing definition, comparison with log-normal and bounded uniform priors, posterior update, navigation and supported Gelman citation retained and expanded.

## Sources opened

- Gelman et al., *Bayesian Data Analysis*, 3rd ed., author-hosted electronic edition, §2.5, printed p. 40, equations (2.9)–(2.10): https://sites.stat.columbia.edu/gelman/book/BDA3.pdf . Read text of p. 40 via web index. Explicitly calls inverse variance precision, derives prior plus data precision and weighted posterior mean for normal-normal model. `gelman_bda2013` exists.
- Dodge (2008), supplied PDF index and entry on Bayesian statistics, printed p. 32 (PDF p. 39): orientation only; no precision entry and no historical claim used.
- Existing question-bank worked answers in `questions/ex-norm-mean.qmd` and `questions/q-07.qmd` checked for relevant distinct questions. These are not bibliographic sources.

## Fact audit

- **Checked**: positive variance has reciprocal precision, with inverse-squared physical units. Gelman et al. §2.5 p. 40.
- **Checked**: under independent normal observations with known common variance and a proper normal prior, posterior precision is prior precision plus $n/\sigma^2$; posterior mean is their precision-weighted average. Derived below and Gelman et al. §2.5 p. 40, eq. (2.10) for one observation; independent-sample extension follows by likelihood product.
- **Checked**: predictive variance for a fresh observation is observation variance plus posterior variance. Direct law of total variance; existing chapter and question `ex-norm-mean` confirm.
- **Checked**: numerical worked and practice examples by exact rational arithmetic in `checks/precision.py`.
- **Assumed**: model variance and prior variance are known positive constants when applying simple precision addition. Stated explicitly.
- **Disputed/limited**: reciprocal-variance precision does not measure accuracy against bias; 0 variance is degenerate rather than a normal distribution with ordinary finite precision. Simple sum fails if measurements share correlated errors or the variance is unknown and integrated out.

No historical priority is asserted for the terminology: Dodge did not establish one, so the page describes its use in modern Bayesian normal analysis rather than attributing invention.
