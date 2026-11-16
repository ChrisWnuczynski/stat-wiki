# Rank 63: Monte Carlo method

## Sources opened

- Metropolis and Ulam (1949), *The Monte Carlo Method*, publisher DOI landing page, journal details and original historical framing.
- Robert and Casella, *Monte Carlo Statistical Methods* (2nd ed.), Springer publisher contents: Monte Carlo integration and variance control are distinct chapters.
- Geyer, University of Minnesota Stat 5421 MCMC notes, §§8.2–8.4: independent draws, LLN, CLT, plug-in Monte Carlo standard error, square-root rate, and finite-variance limit.
- NIST DLMF §3.5(x): uniform sampling for integration, importance targeting, and dimension-independent $N^{-1/2}$ error order.

## Fact audit

- **Checked:** For iid draws $X_i\sim p$, $\widehat I_N=N^{-1}\sum h(X_i)$ is unbiased for $I=E_p h(X)$ and has variance $\operatorname{Var}_p(h)/N$ when the second moment exists; direct algebra and Geyer §8.2–8.4.
- **Checked:** A standard error estimate uses the sample variance of $h(X_i)$ divided by $N$; Geyer §8.4.
- **Checked:** Tenfold smaller standard error needs about 100 times as many iid draws at fixed variance; Geyer §8.4 and NIST §3.5(x).
- **Checked:** Monte Carlo integration can use independent draws without a Markov chain; Geyer §8.2 contrasts ordinary Monte Carlo with MCMC.
- **Assumed:** The worked finite draws illustrate arithmetic only, not convergence or a credible error estimate from four observations.
- **Disputed:** A precise account of who coined the name and the casino anecdote is not established from the opened original publisher page; omit it.

Dodge index directory was absent from `~/statwiki-sources/dodge2008`.
- **Checked numerically:** For worked draws $0.2,0.7,0.9,0.4,0.6$, the squared values sum to $1.86$, mean $0.372$, squared deviations sum $0.36108$, sample variance $0.09027$, and estimated MCSE $0.13437$. For practice draws $0.1,0.3,0.7,0.9$, the estimate is $0.35$ and error is $1/60\approx0.0167$.
- **Checked:** The inherited $100\times100=10^4$ grid count; Geyer §9.1 distinguishes direct iid and MCMC draws.

The generator's page also carries a source-chapter discussion of the 1990 move to Bayesian MCMC. Its source citations were aligned to the opened Metropolis et al. (1953) AIP abstract and Gelfand–Smith (1990) JASA publisher abstract. The inherited grid example citation was aligned to Geyer §§8.2 and 9.1.

## Result

The rebuilt article grew from 311 to 2,030 body words and retained zero figures. It has one collapsed proof, a worked integral with numbers, hidden Your turn answer, and two answered bank questions (`c-11`, `c-15`). The affected MCMC and grid pages were rebuilt; all 67 tests, the rank-specific arithmetic check, offline verification of 450 bibliography entries, and `git diff --check` passed. Quarto HTML rendering was unavailable; the existing Pandoc shim supplied the generator's `quarto pandoc` command.
