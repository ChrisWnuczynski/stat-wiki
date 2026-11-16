# Systematic-scan Gibbs sampler

Type: Concept/definition. Rank 41.

## Material checked

- Frozen baseline: 2,043 body words and one figure. The generated page already contained the fixed-order update definition, two linked properties, five worked examples (including a correlated-normal problem), and 21 question links.
- Read the MCMC chapter `sources/book/chapters/bayes-04-mcmc.qmd`, the linked normal-model chapter, the completed Full conditional distribution research page, and the answered Gibbs questions. The inherited material explains the algorithm but does not independently prove full-sweep invariance or work through a scan-order comparison.

## Sources opened and used

1. Stuart and Donald Geman, [“Stochastic Relaxation, Gibbs Distributions, and the Bayesian Restoration of Images”](https://doi.org/10.1109/TPAMI.1984.4767596), *IEEE TPAMI* **PAMI-6** (1984), pp. 721–741. The text previously opened for rank 37 at §§XI–XII, pp. 731–733, supports sequential site updates and the finite-state convergence result. Existing key `geman_geman1984` uses the DOI.
2. Alan Gelfand and Adrian Smith, [“Sampling-Based Approaches to Calculating Marginal Densities”](https://doi.org/10.1080/01621459.1990.10476213), *JASA* **85** (1990), pp. 398–409. Previously opened §§1–2.3, pp. 398–401, for conditional simulation and Bayesian marginal calculations. Existing key `gelfand_smith1990` uses the DOI.
3. Charles Geyer, [*Some Markov Chain Theory*](https://www.stat.umn.edu/geyer/f05/8931/theo.pdf), University of Minnesota, 2005. Previously opened §§9–10.6, pp. 25–30, for invariant kernels, finite-state convergence and a normal-model Gibbs example. Existing key `geyer2005_markov_chain` links to the author's university site.
4. Charles Geyer, [“Practical Markov Chain Monte Carlo”](https://doi.org/10.1214/ss/1177011137), *Statistical Science* **7** (1992), pp. 473–483; Andrew Gelman and Donald Rubin, [“Inference from Iterative Simulation Using Multiple Sequences”](https://doi.org/10.1214/ss/1177011136), *Statistical Science* **7** (1992), pp. 457–472. The first text's §§1–3 and second text's §§1–2 were opened in earlier depth passes for dependent-chain error and multiple-chain diagnostics. Reopened Geyer §3.6–3.7, p. 480, for spacing and warm-up. Existing DOI keys `geyer1992` and `gelman_rubin1992`.
5. Shyh-Huei Chen and Edward Ip, [“Behavior of the Gibbs Sampler When Conditional Distributions Are Potentially Incompatible”](https://pmc.ncbi.nlm.nih.gov/articles/PMC4572746/), *Journal of Statistical Computation and Simulation* **85** (2015), pp. 3266–3275. Previously opened Abstract and §§1, 3 for the effect of incompatible conditionals and scan order. Existing key `chen_ip2015` links to the legal PubMed Central article.

No new bibliography entry or unauthorised-copy link is needed.

## Changes and checks

- Added motivation from the existing staircase figure, an explicit fixed-order explanation, kernel invariance and finite-state convergence, a scan-order comparison, simulation diagnostics, a binary worked example with hidden “Your turn” answer, misconceptions, limitations, connections and sourced history.
- The collapsed proof establishes invariance of each coordinate update and any fixed-order sweep, finite positive-state convergence, and the fact that opposite orders can give different one-sweep transitions while sharing a stationary target. The new arithmetic check computes every displayed probability from exact fractions.
- Located inherited warm-up and thinning citations in the shared MCMC chapter against Geyer and Gelman–Rubin, replacing unlocated citations to *Bayesian Data Analysis*. Dependent pages are regenerated and checked for retention.
- Preserved the figure, two linked properties, five original worked examples and all 21 question links. Added two answered question-bank checks with hidden answers.

## Verification

The generator completed 718 articles and 557 questions. The generated page has 4,935 body words versus 2,043 before, one figure versus one before, one collapsed proof, 21 distinct question links, and two embedded self-checks with hidden answers. The numerical page check, 67 Python tests, offline verification of 428 bibliography entries, and overview link check pass. The dependent Thinning a Markov chain page now has one inline citation to Geyer; its later depth pass is recorded in `citations-todo.md`. A full HTML render is unavailable because Quarto is not installed in this workspace; the generator uses the Pandoc shim for its conversion step.
