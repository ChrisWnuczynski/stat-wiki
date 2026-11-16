# Likelihood and reference prior

Rank 189. Type: Concept/section. Frozen baseline: 364 body words, zero figures. The normal likelihood, conventional $1/\sigma^2$ measure, joint posterior kernel, and propriety conditions in the source-derived Definition have all been preserved.

## Checked

- **Checked in full source:** Dodge (2008), printed p. 274, “Jeffreys, Harold”, records his 1939 *Theory of Probability*. The extracted full page `/workspace/statwiki-sources/dodge2008/pages/pdf-0276.txt` was opened; this source supports the history sentence only.
- **Checked in the repository source chapter:** `sources/book/chapters/bayes-09-linear-regression.qmd`, §§“Likelihood and reference prior” and “The residual sum-of-squares decomposition”, including the derivation around lines 273–365. The source displays the likelihood, improper reference prior, posterior kernel and rank/$n>p$/positive-SSE conditions.
- **Checked by derivation:** The single collapsed proof in the article integrates the coefficient kernel, identifies the inverse-Gamma variance kernel, and shows necessity of positive residual information. `checks/likelihood-and-reference-prior.py` recalculates every added numerical claim for the two intercept examples and the pending bank questions.
- **Assumed:** Fixed full-rank design, independent Gaussian observations with common variance, and the particular joint parameterization $(\beta,\sigma^2)$ with base measure $d\beta\,d\sigma^2$.
- **Disputed:** Calling this measure simply “uninformative” can hide dependence on parameterization and the fact that it cannot generate prior predictive observations. The marginal coefficient Student scale is not its standard deviation; the worked example distinguishes them.

## Sources used

- Yadolah Dodge, *The Concise Encyclopedia of Statistics* (2008), p. 274, biographical entry; existing `dodge2008` key.
- The repository's Bayesian linear regression book chapter was read for the mathematical setting and to preserve its statements. Existing Jeffreys, Box–Tiao, Gelman, and Berger–Bernardo–Sun citations in that source-derived block remain; no new substantive claim is attributed to an unread source.

## Changes

Added motivation, parameterization, likelihood-prior interpretation, a posterior-propriety proof, numerical example with hidden answer, distinct misconceptions and counterexamples, connections, and a sourced history sentence. Two fully answered bank questions and a lead change await shared integration. No original figure or question link was removed.
