# Full conditional distribution

Type: Concept/topic. Rank 37.

## Material checked

- The frozen baseline had 384 body words, no figures, a brief definition, a copied systematic-scan formula and normal-model paragraph, and 23 distinct question links. Its Gibbs citations lacked locations, and the normal-model excerpt cited two books that had not been opened.
- The Bayesian MCMC and normal-model chapters, the existing Gibbs and conditional-distribution articles, and all linked questions.

## Sources opened and used

1. Stuart Geman and Donald Geman, [“Stochastic Relaxation, Gibbs Distributions, and the Bayesian Restoration of Images”](https://cseweb.ucsd.edu/~dasgupta/291-bayes/geman-geman.pdf), *IEEE TPAMI* **PAMI-6** (1984), pp. 721–741. Read the Introduction and §§XI–XII, especially the site-update algorithm and Theorem A on p. 733. Existing key `geman_geman1984`.
2. Alan E. Gelfand and Adrian F. M. Smith, [“Sampling-Based Approaches to Calculating Marginal Densities”](https://hedibert.org/wp-content/uploads/2013/12/1990GelfandSmith.pdf), *JASA* **85** (1990), pp. 398–409. Read §§1–2.3 and the description of the applications in §3, pp. 398–404. Existing key `gelfand_smith1990`.
3. Charles J. Geyer, [*Some Markov Chain Theory*](https://www.stat.umn.edu/geyer/f05/8931/theo.pdf), University of Minnesota, 2005. Read §§9–10.6, pp. 25–30, including the invariant-distribution proof and independent normal/precision example. New key `geyer2005_markov_chain`.
4. Shyh-Huei Chen and Edward H. Ip, [“Behavior of the Gibbs Sampler When Conditional Distributions Are Potentially Incompatible”](https://pmc.ncbi.nlm.nih.gov/articles/PMC4572746/), *Journal of Statistical Computation and Simulation* **85** (2015), pp. 3266–3275. Read the Abstract and §§1, 3 for the compatibility and scan-order result. New key `chen_ip2015`.

## Changes and checks

- Added lead context, a normal-model motivation, a full posterior-density definition with symbols and normalization explained, interpretation, precise properties, statistical use, an exact binary example, limits, relationships and two History paragraphs. Every added factual paragraph cites an opened passage with a location.
- One collapsed Proof box establishes conditional normalization, cancellation of constant factors, invariance of each Gibbs update and a full sweep, and convergence for a finite product state space with strictly positive joint mass. This is the same scope as the narrowed copied convergence statement; no new proofs-todo item was needed.
- Replaced the copied unlocated Gibbs citations and unopened Robert–Casella citation with located Geman–Geman and Gelfand–Smith passages. The normal-model excerpt now cites the opened Geyer §10.6 instead of unopened Gelman and Raiffa–Schlaifer books. That source excerpt also appears on the Normal distribution and full-conditionals pages, so the dependent source-key and preservation checks now recognize the verified replacement. The copied formulas, normal and inverse-gamma identities, and all 23 question links remain.
- `checks/full-conditional-distribution.py` checks every printed binary mass, conditional fraction and transition probability against exact rational arithmetic, and asserts citation keys and locations, one Proof box and all 23 question links.

## Verification

Generated article: 1,880 body words versus 384 before; zero figures versus zero before; 23 distinct question links; one collapsed Proof box. The generator produced 718 articles and 557 question pages. All 37 page checks, 67 Python tests and offline validation of 423 bibliography entries pass. `git diff --check` is clean. The temporary Quarto-to-Pandoc shim handled the generator's `quarto pandoc` call; a full rendered HTML build was not run.

## Rank 28–37 practice correction

- Kept the worked example and added a “Your turn” problem with its answer in a collapsed callout.
- After rebuilding, the generated body has 1,975 words by the progress-table method.
