# Gibbs sampling

Type: Method/topic. Rank 46.

## Material checked

- Frozen baseline: 1,180 body words and one figure. The generated article contains the systematic update definition, an exponential-target derivation, R code, normal-mean-and-variance guidance, and warm-up discussion.
- Read sources/book/chapters/bayes-04-mcmc.qmd and the rank-41 systematic-scan article to keep the general method distinct from the fixed-order special case.

## Sources opened and used

1. Charles J. Geyer, [Some Markov Chain Theory](https://www.stat.umn.edu/geyer/f05/8931/theo.pdf), University of Minnesota (2005), §§5, 8, 10, pp. 9–10, 20–21, 27–30. Read the update, composition and invariance arguments, block/generalised updates, sampler definition and normal/precision example. Existing key: geyer2005_markov_chain.
2. Stuart and Donald Geman, [“Stochastic Relaxation, Gibbs Distributions, and the Bayesian Restoration of Images”](https://doi.org/10.1109/TPAMI.1984.4767596), *IEEE TPAMI* PAMI-6 (1984), §§XI–XII, pp. 731–733. The page-located scan opened during ranks 37 and 41 supports local conditional updates and finite-state convergence. The author/course-hosted scan was reopened for this pass; it is image-only in the web text extraction. Existing key: geman_geman1984.
3. Alan Gelfand and Adrian Smith, [“Sampling-Based Approaches to Calculating Marginal Densities”](https://doi.org/10.1080/01621459.1990.10476213), *JASA* 85 (1990), §§1–2.3, pp. 398–401. The earlier depth-pass research log records the opened source and its Bayesian applications. Existing key: gelfand_smith1990.
4. Charles Geyer, [“Practical Markov Chain Monte Carlo”](https://doi.org/10.1214/ss/1177011137), *Statistical Science* 7 (1992), §§3.3–3.7, pp. 477–480, for dependent-chain error and warm-up practice. Existing key: geyer1992.

No unauthorised copy was used or added. The user-supplied Dodge index has no Gibbs-sampling entry.

## Changes and checks

- Added a motivating coupled-parameter example, exact update-kernel and invariance explanation, finite-state proof, practical limits, a distinct binary-sweep worked calculation, and a hidden “Your turn” reverse-transition answer.
- Located two inherited MCMC-chapter citations and replaced an unlocated reference to unopened Bayesian Data Analysis in the trace/autocorrelation paragraph.
- Added located Geyer and Gelman–Rubin citations to the dependent Trace plot article after that shared-source edit exposed its citation gap.
- Selected two answered bank questions, q-59 and q-26, for “Check yourself.” The page check uses exact fractions to verify both printed transitions and stationary invariance of the toy sweep, and retains the exponential example, figure and question links.

## Verification

The generator completed 718 articles and 557 question pages. The article has 3,536 body words versus 1,180 before and retains its figure. All 46 page checks, 67 Python tests, 11 Node tests, offline verification of 435 bibliography entries, the overview link check, and git diff --check pass. Quarto is unavailable in this workspace; the generator uses a local Pandoc command shim for its conversion step. No full Quarto HTML render was run.
