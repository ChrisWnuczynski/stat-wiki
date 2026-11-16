# Central limit theorem

Type: Theorem. Rank 43.

## Material checked

- Frozen baseline: 1,329 body words, two figures, four related questions. The generated page also had a binomial worked example and three linked worked answers.
- Read `sources/stat2003/chapters/prob-05-transforms-and-limits.qmd` and the multivariate continuation in `sources/stat3006/chapters/sl-02-normal-inference.qmd` before editing their extracted statements.

## Sources opened and used

1. Kyle Siegrist, [“The Central Limit Theorem”](https://www.randomservices.org/random/sample/CLT.html), *Random Services*, §5.4. Its characteristic-function proof and normal-approximation discussion support the iid theorem and proof. Key `siegrist2022_clt` points to the author's site.
2. He Wang, [*Foundations of Probability and Statistical Theory*](https://wanghemath.github.io/Book-ProbabilityStatisticalTheory/), Ch. 9 §§14, 18, 20–21, for the iid statement, convergence modes and Slutsky's theorem, and Ch. 2 §3.9.5 for the exponential-sum Gamma relation. Existing key `wang2025_foundations` points to the author's site.
3. A. Colin Cameron, [*Asymptotic Theory for OLS*](https://cameron.econ.ucdavis.edu/e240a/asymptotic.pdf), §4.2 pp. 7–8 and §7 pp. 10–11, for the nonidentical-summand condition and the Cramér–Wold route to a vector limit. Key `cameron2004_asymptotic` points to the author's university PDF.
4. The page-located secondary histories already checked for rank 30: R. H. Daw, [“Why the Normal Distribution”](https://doi.org/10.1017/S0020269X00008008), pp. 3–4, and M. J. de Oliveira, [“Structure of the theories of probability”](https://doi.org/10.1590/1806-9126-RBEF-2022-0087), §9 pp. e20220087-15–16. These support the de Moivre and Laplace history without an invented original-page claim.
5. The existing binomial approximation source, Siegrist [§11.2](https://stats.libretexts.org/Bookshelves/Probability_Theory/Probability_Mathematical_Statistics_and_Stochastic_Processes_(Siegrist)/11:_Bernoulli_Trials/11.02:_The_Binomial_Distribution), supports the inherited continuity-correction example. The 1922 Lindeberg article remains cited for its documented historical extension, alongside Cameron's located modern account.

All new URLs are author, institutional, publisher, or licensed textbook pages.

## Changes and checks

- Added a motivating exponential-sum example, precise sum and mean scaling, a full collapsed characteristic-function proof, multivariate and studentised extensions, limitations, historical context, a worked numerical example and a hidden “Your turn” answer.
- Replaced unlocated copied theorem citations with opened sources and locations. The dependent multivariate CLT and Hotelling-limit extracts retain three inline citations after the replacement. The original de Moivre and Lindeberg citation keys needed by other distribution pages remain present.
- The exact Gamma tail in the worked example was checked against the Poisson CDF identity and direct numerical computation. The page check also recomputes the inherited binomial probabilities and preserves the two figures and eight distinct question links. Two relevant answered bank questions appear in “Check yourself.”

## Verification

The generator completed 718 articles and 557 question pages. The article has 3,512 body words versus 1,329 before and two figures versus two before. All 43 page arithmetic checks, 67 Python tests, offline verification of 434 bibliography entries, the overview link check, and `git diff --check` pass. Quarto is unavailable here; the generator uses the Pandoc shim for its conversion step.
