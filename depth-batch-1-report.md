# Distribution depth pass — batch 1

Baseline: generated pages from commit `5dc5301`. This batch covers all 25 named distribution articles. Counts use the same substantive-word measure as the retention test.

## Per-article changes

All listed sections were added or expanded by the generator. The proof column identifies the new collapsed proof on each page.

| Article | Words before → after | Sections added or expanded | New proof |
|:--|--:|:--|:--|
| Bernoulli | 561 → 997 | Lead, Properties and proof, Related distributions, Statistical inference, History, Examples | Mean and variance of one trial |
| Beta | 2,758 → 3,183 | Lead, Properties and proof, Related distributions, Statistical inference, Examples | Mean of a beta probability |
| Binomial | 2,930 → 3,548 | Lead, Properties and proof, Related distributions, Statistical inference, History, Examples | Mean and variance of a trial count |
| Cauchy | 568 → 910 | Lead, Properties and proof, Related distributions, Statistical inference, Examples | Why the mean does not exist |
| Chi-squared | 1,010 → 1,544 | Lead, Properties and proof, Related distributions, Statistical inference, History, Examples | Mean and variance of squared normals |
| Conway–Maxwell–Poisson | 447 → 1,001 | Lead, Definition, Properties and proof, Related distributions, Statistical inference, History, Examples | The Poisson special case |
| Dirichlet | 2,662 → 3,099 | Lead, Definition, Properties and proof, Related distributions, Statistical inference, Examples | Beta marginal of one component |
| Exponential | 2,274 → 2,662 | Lead, Properties and proof, Related distributions, Statistical inference, Examples | Memorylessness |
| F | 762 → 1,130 | Lead, Properties and proof, Related distributions, Statistical inference, Examples | When the mean of an F ratio exists |
| Gamma | 2,725 → 3,282 | Lead, Definition, Properties and proof, Related distributions, Statistical inference, Examples | Mean and variance in shape-rate form |
| Geometric | 2,006 → 2,352 | Lead, Properties and proof, Related distributions, Statistical inference, Examples | Survival and expected trial count |
| Hypergeometric | 783 → 1,165 | Lead, Properties and proof, Related distributions, Statistical inference, Examples | Finite-population mean and variance |
| Inverse gamma | 1,959 → 2,296 | Lead, Properties and proof, Related distributions, Statistical inference, Examples | The inverse-gamma mode |
| Inverse Gaussian | 293 → 639 | Lead, Properties and proof, Related distributions, Statistical inference, Examples | Mean and variance of the positive law |
| Lognormal | 327 → 680 | Lead, Properties and proof, Related distributions, Statistical inference, Examples | Moments from a normal logarithm |
| Multinomial | 2,234 → 2,666 | Lead, Definition, Properties and proof, Related distributions, Statistical inference, Examples | Binomial marginals and dependent counts |
| Multivariate normal | 759 → 1,220 | Lead, Definition, Properties and proof, Related distributions, Statistical inference, Examples | Affine images remain jointly normal |
| Negative binomial | 310 → 768 | Lead, Definition, Properties and proof, Related distributions, Statistical inference, Examples | Extra variance from rate mixing |
| Normal | 3,291 → 3,806 | Lead, Properties and proof, Related distributions, Statistical inference, History, Examples | Affine changes preserve normality |
| Pareto | 644 → 1,021 | Lead, Properties and proof, Related distributions, Statistical inference, History, Examples | Power-law survival |
| Poisson | 3,051 → 3,550 | Lead, Properties and proof, Related distributions, Statistical inference, History, Examples | Adding independent Poisson counts |
| Student t | 1,008 → 1,431 | Lead, Properties and proof, Related distributions, Statistical inference, History, Examples | The Cauchy special case |
| Uniform | 633 → 957 | Lead, Properties and proof, Related distributions, Statistical inference, Examples | Mean and variance on an interval |
| Weibull | 686 → 1,128 | Lead, Definition, Properties and proof, Related distributions, Statistical inference, History, Examples | Survival and hazard in shape-scale form |
| Wishart | 1,114 → 1,640 | Lead, Definition, Properties and proof, Related distributions, Statistical inference, History, Examples | Mean of a scatter matrix |

Total: **35,795 → 46,675 words**. Prior figure placements: **16 → 16**; none were lost. The retention test also checks existing citation keys, question links, example headings, and infobox row values.

## Proofs and pending work

There are **25 new distribution proofs**, one for each article, named in the table. The generated `proofs-todo.json` retains the **78** prior theorem/proposition todos and now records **37** copied distribution-property results without a proof on that distribution page:

- `beta-distribution#property-beta-binomial-conjugacy` — Beta–Binomial conjugacy
- `beta-distribution#property-the-beta-distribution-is-the-two-category-dirichlet` — The Beta distribution is the two-category Dirichlet
- `beta-distribution#property-beta-binomial-posterior-prediction` — Beta–Binomial posterior prediction
- `beta-distribution#property-two-pseudo-count-conventions` — Two pseudo-count conventions
- `binomial-distribution#property-beta-binomial-conjugacy` — Beta–Binomial conjugacy
- `binomial-distribution#property-beta-binomial-posterior-prediction` — Beta–Binomial posterior prediction
- `binomial-distribution#property-poisson-limit-of-the-binomial` — Poisson limit of the binomial
- `binomial-distribution#property-central-limit-theorem` — Central limit theorem
- `chi-squared-distribution#property-normal-sample-theorem` — Normal sample theorem
- `chi-squared-distribution#property-pearson-chi-squared-approximation` — Pearson chi-squared approximation
- `chi-squared-distribution#property-pearson-test-with-estimated-parameters` — Pearson test with estimated parameters
- `dirichlet-distribution#property-dirichlet-moments` — Dirichlet moments
- `dirichlet-distribution#property-interior-dirichlet-mode` — Interior Dirichlet mode
- `dirichlet-distribution#property-dirichlet-multinomial-conjugacy` — Dirichlet–Multinomial conjugacy
- `dirichlet-distribution#property-the-beta-distribution-is-the-two-category-dirichlet` — The Beta distribution is the two-category Dirichlet
- `exponential-distribution#property-memoryless-property` — Memoryless property
- `f-distribution#property-variance-ratio-f-pivot` — Variance-ratio F pivot
- `f-distribution#property-anova-f-distribution` — ANOVA F distribution
- `gamma-distribution#property-generic-exponential-family-conjugate-update` — Generic exponential-family conjugate update
- `geometric-distribution#property-memoryless-property` — Memoryless property
- `inverse-gamma-distribution#property-normal-inverse-gamma-variance-update` — Normal–inverse-Gamma variance update
- `inverse-gamma-distribution#property-normal-inverse-gamma-conjugacy` — Normal–inverse-Gamma conjugacy
- `inverse-gamma-distribution#property-marginal-variance-posterior` — Marginal variance posterior
- `multinomial-distribution#property-multinomial-central-limit-theorem` — Multinomial central limit theorem
- `multinomial-distribution#property-dirichlet-multinomial-conjugacy` — Dirichlet–Multinomial conjugacy
- `multivariate-normal-distribution#property-affine-images-of-normal-vectors` — Affine images of normal vectors
- `normal-distribution#property-normal-normal-conjugacy` — Normal–Normal conjugacy
- `normal-distribution#property-normal-inverse-gamma-variance-update` — Normal–inverse-Gamma variance update
- `normal-distribution#property-full-conditionals-under-independent-priors` — Full conditionals under independent priors
- `normal-distribution#property-precision-weighting` — Precision weighting
- `normal-distribution#property-normal-sample-theorem` — Normal sample theorem
- `poisson-distribution#property-generic-exponential-family-conjugate-update` — Generic exponential-family conjugate update
- `poisson-distribution#property-poisson-limit-of-the-binomial` — Poisson limit of the binomial
- `student-t-distribution#property-one-sample-t-pivot` — One-sample t pivot
- `student-t-distribution#property-two-sample-t-pivot` — Two-sample t pivot
- `student-t-distribution#property-slope-t-pivot` — Slope t pivot
- `uniform-distribution#property-inverse-transform-method` — Inverse-transform method

Historical attribution was left out of **15** articles pending a verified primary source and modern historical account (`distribution-history-todo.json`): beta-distribution, cauchy-distribution, dirichlet-distribution, exponential-distribution, f-distribution, gamma-distribution, geometric-distribution, hypergeometric-distribution, inverse-gamma-distribution, inverse-gaussian-distribution, lognormal-distribution, multinomial-distribution, multivariate-normal-distribution, negative-binomial-distribution, uniform-distribution.

## Citations and consistency

Newly used citation keys, relative to the prior 25 pages: `agresti2002`, `anderson2003_mva`, `bernoulli1713`, `casella_berger2002`, `forbes2011`, `mccullagh_nelder1989`, `ross2019`, `shmueli2005`, `venables_ripley2002`. All are already in `bibliography.json`; no bibliography records were added. New source fields contain 208 citation markers across leads, definitions, properties, related distributions, statistical use, examples, and history.

Reciprocal distribution relationships are held in `distribution_relationships.json`. The Weibull source expansion was converted to shape `k` and scale `λ` to agree with its infobox and examples. Its preserved source figure labels shape as `β`; the generated caption now explains `β = k` and unit scale. The generator was changed only to render the new distribution fields, reciprocal relationships, this caption clarification, and the property-proof todo entries.

**Corrective removal:** the old Weibull source expansion repeated the alternate rate/scale convention and claimed that mixing the two always multiplies the mean by `λ²`. That statement is dimensionally misleading and was removed. The alternate convention is now explained once in Definition. No figure, citation, infobox value, definition, example, or practice-question link was removed.

## Verification

- Wiki generator completed: 718 concept articles and 557 question pages.
- `python -m unittest discover -q`: 60 tests passed. The existing count warning reports 17 articles site-wide with fewer than three inline citations.
- `python check_overview_links.py`: 115 internal overview targets valid; the test suite also checks generated local link targets.
- `python verify_citations.py --offline`: all 380 bibliography entries passed schema and provenance checks.
- Live `verify_citations.py` could not reach Crossref, OpenLibrary, or OpenAlex: the network tunnel returned HTTP 403 for all 380 requests. This is a verification limit, not a bibliography finding.
- All 25 worked numerical examples were checked against SciPy or independent arithmetic.
- `git diff --check` passed.
