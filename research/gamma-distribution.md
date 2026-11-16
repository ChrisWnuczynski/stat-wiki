# Rank 65: Gamma distribution

## Sources opened

- Siegrist, *Probability, Mathematical Statistics, and Stochastic Processes*, LibreTexts §5.8: shape-scale density, moments, MGF, convolution, chi-square relation, and numerical CDF.
- Siegrist §14.3: gamma arrival time in a Poisson process; Erlang name and waiting-time interpretation.
- NIST/SEMATECH e-Handbook §8.1.6.5: shape-rate and shape-scale parameterizations, mean, variance, exponential and chi-square special cases.
- Pearson, “Contributions to the Mathematical Theory of Evolution II” (1895), pp. 373–374: Type III skew curve and gamma-function normalization; original university-hosted scan.
- Laplace, *Théorie analytique des probabilités* (1812), Book I preface pp. 1–4; original ETH Zürich public-domain scan.
- Gelman et al., *Bayesian Data Analysis* (3rd ed.), §§2.6–2.7, pp. 44–50, author-hosted PDF: Poisson–Gamma update and county cancer rates.
- Forbes et al., *Statistical Distributions* (4th ed.), publisher contents, chs. 15 and 21, Erlang and Gamma entries.
- Grimmett and Stirzaker, *Probability and Random Processes* (4th ed.), Oxford publisher preview contents, §§6.8, 8.3–8.4, Poisson process, renewals and queues.
- Dodge index directory absent from `~/statwiki-sources/dodge2008`.

## Fact audit

- **Checked:** Shape $k>0$, rate $r>0$ density $r^k x^{k-1}e^{-rx}/\Gamma(k)$ has mean $k/r$ and variance $k/r^2$; NIST §8.1.6.5, Siegrist §5.8 with scale $1/r$.
- **Checked:** Fixed-rate independent gammas add shapes; Siegrist §5.8 relations.
- **Checked:** Integer-shape gamma is the waiting time for that arrival in a rate-$r$ Poisson process; Siegrist §14.3.
- **Checked:** $k=1$ is exponential; $\chi^2_\nu$ is gamma shape $\nu/2$, rate $1/2$; NIST §8.1.6.5.
- **Assumed:** A concrete waiting-time story is illustrative; actual arrivals may violate Poisson independence or constant rate.
- **Checked:** Pearson (1895, pp. 373–374) used the Gamma integral to normalize his Type III skew curve; this is an early Gamma-form density.
- **Disputed:** The historical first use of the Gamma distribution is not established; the article gives a documented early instance without an origin claim.
- **Checked numerically:** Shape 3, rate 2 gives mean 1.5 and variance 0.75; survival past 2 is $13e^{-4}=0.2381033$ and CDF $0.7618967$. Practice shape 2, rate 1 has survival beyond 3 of $4e^{-3}=0.1991483$. Unequal-rate exponential sum has mean 1.5, variance 1.25 versus 1.125 for a shape-two Gamma matched on mean.
- **Checked:** SciPy official `scipy.stats.gamma` Notes: `a` is shape and `scale=1/rate`, with `rvs`, `sf`, `cdf` and `stats` methods.

The Gamma density citation in the shared probability source was aligned to opened Siegrist §5.8 and NIST §8.1.6.5. Distribution input citations for parameterization, conjugacy and the inherited two-arrival example were aligned to opened sources. The original Pearson and Laplace citations did not directly support the density parameterization and were replaced there. Both are retained in History for claims their opened passages support. Forbes and Grimmett are retained for precise chapter/section context from publisher previews; the formulas themselves cite the opened NIST and Siegrist material. The reciprocal and variance-function relationship blurbs are shared generator inputs, so the affected related distribution pages are included in the full rebuild and gate.

## Build audit

- Baseline 3,039 words and three figures; rebuilt 5,263 words and three figures.
- The inherited three figures, infobox entries, source examples and citation keys remain present.
- The one collapsed proof derives normalization, moments, MGF, convolution, mode and Poisson–Gamma update.
- `checks/gamma-distribution.py` passed; full build passed; 67 unit tests passed; offline bibliography verification passed for 457 entries; `git diff --check` passed.
