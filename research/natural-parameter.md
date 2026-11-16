# Natural parameter — rank 132

Type: Concept. Baseline: 316 body words, zero figures, three question links. Read the generated page and its short source section. Preserved the inherited GLM notation, Poisson and Bernoulli examples, completeness qualification, infobox, links and supported citations.

## Material checked

- **Checked:** Will Fithian's licensed [Berkeley Stat 210A exponential-families chapter](https://www.stat.berkeley.edu/~wfithian/courses/stat210a/exponential-families.html), published August 29, 2023, “Exponential family structure” and “Differential identities,” was opened in full. It gives the natural parameter and its space, Poisson representation, nonuniqueness under affine statistic transformations, and log-normalizer moment identities.
- **Checked:** Charles Geyer's licensed [University of Minnesota notes](https://www.stat.umn.edu/geyer/f22/5421/notes/expfam.html), §§3.1–3.4, 4–5 and 7.1–7.5, was opened in full. It explicitly discusses natural/canonical terminology, fixed dispersion conventions and examples. Existing key `geyer2022_exp_family`.
- **Checked:** Hua Zhou's [UCLA GLM lecture](https://ucla-biostat-200c-2020spring.github.io/slides/09-glm/glm.html), “Exponential family distribution” and “Link function,” was opened earlier in this batch; its normal, Bernoulli and Poisson examples support the GLM convention. Existing key `zhou2020_glm`.
- **Checked by code:** Bernoulli odds, natural parameter, normalizer, probabilities, derivatives and variance; Poisson natural parameter, alternate-statistic scaling and derivative moments are asserted in `checks/natural-parameter.py`.
- **Assumed:** the Bernoulli and Poisson worked examples are illustrative model parameters, not estimates from a dataset. Differentiation under the normalizing integral is used only at regular interior parameter values.
- **Disputed:** the word “canonical” sometimes names the same coefficient as “natural,” while the GLM dispersion-scaled convention uses a different numerical scale. The page states both conventions. Natural parameters are representation-dependent; no unique numerical value should be inferred without a specified statistic and base factor.

## Dodge and proof status

The authorized Dodge index has no direct entry for natural parameter. The single collapsed proof establishes log-normalizer mean and covariance identities, Poisson/Bernoulli representations, and nonuniqueness under statistic scaling. The inherited full-rank completeness assertion needs a separate Laplace-transform uniqueness argument; it is logged in the pending proof override rather than claimed proved here.

## Question bank

Answered `c-17` asks what a canonical link does to the natural parameter, while answered `q-32` derives the Poisson log-likelihood in which the count multiplies the log mean. Neither repeats the page's Bernoulli numeric example. Both IDs are in the pending self-check manifest.
