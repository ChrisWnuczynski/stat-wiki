# Flat prior — rank 103

Type: concept. Frozen baseline 450 body words, zero figures. The source definition, bounded-uniform remark, support and Jacobian interpretation, infobox and supported citations remain generated.

## Sources read

- **Checked:** Gelman, Carlin, Stern, Dunson, Vehtari and Rubin, *Bayesian Data Analysis*, third edition, author-hosted authorized PDF at https://sites.stat.columbia.edu/gelman/book/BDA3.pdf (book homepage explicitly permits non-commercial download), Ch. 2 §2.8, printed pp. 51–54. Read discussion of proper versus improper priors, normal-location limit, Jacobian, Jeffreys rule and binomial choices. Existing bibliography key `gelman_bda2013` is used with page locators.
- **Checked:** Dodge, *The Concise Encyclopedia of Statistics* (2008), printed p. 274 “Jeffreys, Harold” for the 1939 book history and printed p. 32 “Bayesian Statistics” for orientation.
- **Checked by code:** `checks/flat-prior.py` verifies all new posterior means, variances, intervals, beta/Jacobian identities and source bounded-uniform numbers.
- **Assumed:** Normal examples have independent observations and known variance; the likelihood is integrable in the location parameter. Binomial statements use a fixed number of independent Bernoulli trials.
- **Disputed:** Calling any density “noninformative” without naming its coordinate is misleading. The source text's other Box–Tiao and Laplace citations remain; they were not newly used for assertions.

## Proof and bank

One collapsed proof covers the normal-location posterior normalisation and the log-odds Jacobian. Answered bank questions: `ex-improper-normal`, `ex-applied-geometric`, `q-11`. They exercise improper versus proper uniform priors and a model calculation, without repeating the worked normal-location example.
