# Three components of a GLM — rank 130

Type: Concept/section. Baseline: 624 body words, zero figures, one direct question link. Read the generated page and its source section in the introduction to GLMs. Preserved the inherited three-part definition, canonical-link examples, infobox, question link, and source citations.

## Material checked

- **Checked:** Hua Zhou's [UCLA GLM lecture](https://ucla-biostat-200c-2020spring.github.io/slides/09-glm/glm.html), “Introduction,” “Exponential family distribution” Examples 1–4 and Moments, and “Link function,” was opened in full. It gives the family form, moments, natural parameters and normal, Bernoulli, Poisson and gamma link examples.
- **Checked:** R Core Team's official [`glm` manual](https://search.r-project.org/R/refmans/stats/html/glm.html), “Description,” “Arguments” and “Details,” was opened. It distinguishes formula, family and link, describes offsets, and states the default IWLS fitter. Existing key `rstats_glm2026`.
- **Checked:** R Core Team's official [family manual](https://search.r-project.org/R/refmans/stats/html/family.html), “Usage,” “Arguments,” “Details” and “Value,” was opened. It lists family defaults and alternative links. Existing key `rstats_family2026`.
- **Checked:** Bailey's author-hosted [Nelder lecture](https://webspace.maths.qmul.ac.uk/r.a.bailey/neldbeam.pdf), slide 23/32, records the 1972 paper's normal, binomial, Poisson and gamma framework. Citation metadata is in rank 128's pending manifest.
- **Checked by code:** the Bernoulli probabilities, odds, variance and risk ratio in the worked example; Poisson means and variances in the hidden practice; and canonical-link algebra are asserted in `checks/three-components-of-a-glm.py`.
- **Assumed:** the infection example and coefficients are illustrative, not an estimated study. Its binary observations are conditionally independent under the model.
- **Disputed:** some expositions count distribution and link as two essential GLM choices, treating the linear predictor as part of the link specification; this page uses the conventional three-part pedagogic separation. Gamma inverse-link sign conventions differ, as Zhou notes. The inherited source's formula uses its own natural-parameter notation and is preserved with its context.

## Dodge and question bank

Dodge's `index.tsv` entry “Generalized Linear Regression,” printed p. 219, was opened. It discusses generalized *least squares* regression with heteroscedasticity and correlated errors, not the exponential-family GLM, so it is not cited. Answered bank questions `q-45` (gamma family, log mean and score) and `q-54` (Poisson family, log predictor and quasi-Poisson alternative) require readers to identify all three GLM components without repeating the page's Bernoulli numerical example. Their IDs are recorded in the pending manifest.

## Result

One collapsed proof derives Bernoulli and Poisson canonical parameters, links, means and variances. No new theorem is left unproved. The page-local manifest also records a shared lead correction: the generated sentence currently uses singular “is” for the plural components.
