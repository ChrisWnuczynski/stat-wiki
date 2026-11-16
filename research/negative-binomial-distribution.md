# Negative binomial distribution research notes

Type: distribution. Baseline: 701 words, two figures. Preserve the infobox PMF, moments, both plots, the existing mean-four/size-two example, all inherited citations, the gamma–Poisson proof and related-distribution statements. New prose adds two interpretations, comparison probabilities, regression limits and history.

## Sources opened

- Zeileis, Kleiber and Jackman (2008), “Regression Models for Count Data in R,” *Journal of Statistical Software* 27(8), DOI 10.18637/jss.v027.i08. Opened the full publisher/CRAN-hosted PDF at https://cloud.r-project.org/web/packages/pscl/vignettes/countreg.pdf and read §2 pp. 4–5 and §3 pp. 6–8. Checked mean–dispersion mass, $\mu+\mu^2/\nu$, gamma–Poisson mixture, geometric and Poisson relationships and competing hurdle/zero-inflated models.
- R MASS reference manual, `glm.nb` and `rnegbin`, https://cran.r-universe.dev/MASS/doc/manual.html, opened the complete current official HTML. Cross-checked model and simulation parameterisation; not newly cited.
- Dodge (2008), *The Concise Encyclopedia of Statistics*, “Negative Binomial Distribution,” printed pp. 369–370, `/workspace/statwiki-sources/dodge2008/pages/pdf-0369.txt` and `pdf-0370.txt`. Checked waiting-for-successes derivation, geometric sum and the account of Greenwood and Yule's repeated-accident application.
- Greenwood and Yule (1920), publisher metadata/DOI landing page https://academic.oup.com/jrsssa/article/83/2/255/7014440, DOI 10.1111/j.2397-2335.1920.tb00606.x. Full original was unavailable from the opened publisher page, so added prose cites Dodge for its historical account. The inherited original-paper citation remains intact.

## Fact ledger

- **Checked:** The mean–dispersion parameterisation has $p=\nu/(\mu+\nu)$, mean $\mu$ and variance $\mu+\mu^2/\nu$; full JSS article §2 pp. 4–5.
- **Checked:** With $\mu=3,\nu=1$, zero probability is $1/4$, upper tail from seven is $(3/4)^7=0.1334838867$; Poisson comparison is $e^{-3}=0.0497870684$ and $P(X\ge7)=0.0335085353$. `checks/negative-binomial-distribution.py` independently computes these with SciPy.
- **Checked:** With $\mu=2,\nu=2$, variance four and probabilities at zero and one both $1/4$.
- **Checked:** Existing example $\mu=4,\nu=2$ has variance twelve and zero probability $1/9$.
- **Assumed:** Help-desk examples are hypothetical; no empirical rate or gamma mixing is claimed.
- **Disputed:** The early accident-data chronology is represented through Dodge rather than inferred from an unread original full text.

## Bank selection

Answered `c-22` directly tests extra negative-binomial variance. Answered `q-57` tests conversion from success probability to mean and the canonical link at fixed size. They address different mathematical steps and neither repeats the embedded numeric examples.
