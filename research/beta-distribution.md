# Beta distribution — rank 92

Type: distribution. Baseline 2,597 words, 4 figures. Preserve all infobox formulas, the four figures, the source proof of the mean, the two embedded question examples, citations and question links. The existing generated `proofs-todo.json` already logs its unproved conjugacy, Dirichlet, posterior-prediction and pseudo-count property blocks. The gamma-ratio relation added below is recorded in pending proof overrides.

## Sources opened

- **Checked:** Siegrist, *Probability, Mathematical Statistics, and Stochastic Processes*, §5.17 “The Beta Distribution,” full online chapter: beta function and normalization, shape cases, moments, symmetry, gamma-ratio construction, and F transformation.
- **Checked:** Gelman et al., *Bayesian Data Analysis* (3rd ed.), author-hosted full book, §2.1 pp. 29–31: binomial sampling, uniform-prior beta posterior, and Bayes/Laplace historical note. The existing bibliography key is `gelman_bda2013`.
- **Checked:** NIST Engineering Statistics Handbook, §1.3.6.6.17: standard and scaled beta density, incomplete beta CDF and mode.
- **Checked:** MacTutor History of Mathematics, “BETA DISTRIBUTION” entry: early beta posterior in Bayes's problem and Gini's 1911 `Distribuzione β` term. The full entry was read; historical prose is limited to these points.
- **Checked:** Dodge (2008), printed p. 40 “Beta Distribution” for a bounded-interval variant, beta mean and variance, and gamma/uniform connections.
- **Checked:** bank answers `q-17`, `q-44`, `ex-geom-beta`, each substantively uses the beta family without repeating the embedded `q-06` example.
- **Assumed:** the worked binomial sequence is conditionally independent at a common success probability and the Beta(2,3) prior describes uncertainty before those trials.
- **Disputed:** Dodge says the beta family itself “tends towards the standard normal” as both shapes grow; unscaled beta laws instead concentrate inside (0,1), and a suitable centered and scaled beta can have a normal approximation. This unqualified claim is omitted.

## Mathematical checks

Beta(2,3) has mean 2/5=0.4, variance 6/(25·6)=0.04, and probability above 1/2 equal to 5/16=0.3125. After 8/10 successes the posterior is Beta(10,5), mean 2/3=0.666667, mode 9/13=0.692308, and probability above 1/2 is 0.910217. After 3/4 successes the posterior is Beta(5,4), mean 5/9=0.555556 and probability above 1/2 is 0.636719. Checked with SciPy beta CDF, integration and direct beta-function ratios. The existing figures and examples are retained.

## Shared generator issue

`distributions.json["beta-distribution"].lead_context` adds a second full sentence to the generated lead. During integration move its factual claim into `statistical_use` and set `lead_context` to citation-only `{{cite:gelman_bda2013}}`; the latter must remain nonempty for the distribution test. This leaves a single plain-language lead and preserves the source citation.
