# Dispersion parameter

Type: Concept/topic. Rank 51.

## Material checked

- Frozen baseline: 256 body words, zero figures. Read the generated article, the clotting-time GLM source paragraph and its eight question links; q-47 and q-55 have worked answers. The notation page uses $\phi(x)$ for the standard normal density, so every occurrence of dispersion $\phi$ is explicitly contextualized as a parameter rather than a function of $x$.
- **Checked:** McCullagh's 1992 introduction to the Nelder–Wedderburn paper gives the exponential-dispersion form, $\operatorname{Var}(Y)=\phi V(\mu)$, a common dispersion independent of covariates, its distinction from the mean function, and the historical “scale factor” terminology (pp. 543–545). This PDF is on McCullagh's University of Chicago publications page.
- **Checked:** official R `family` documentation says Poisson/binomial families fix dispersion at one while quasi versions free it; `summary.glm` documentation states its default Pearson chi-squared/residual-df estimate and that coefficient covariance is scaled by dispersion.
- **Checked by code:** the Gamma shape–rate conversion, the count worked example and the practice arithmetic are asserted in `checks/dispersion-parameter.py`. The inherited Gamma GLM formula matches shape $1/\phi$ and rate $1/(\phi\mu)$.
- **Assumed:** worked counts are illustrative independent observations, not a fitted clinical dataset.
- **Disputed:** “dispersion” sometimes means a different parameter in other families, notably negative-binomial size. The article specifies the exponential-dispersion GLM convention and does not identify all uses of the word with $\phi$.

## Sources opened and used

1. Peter McCullagh, [“Introduction to Nelder and Wedderburn (1972): Generalized Linear Models”](https://www.stat.uchicago.edu/~pmcc/pubs/paper32.pdf), in *Breakthroughs in Statistics*, vol. II (1992), pp. 543–545. Opened the author-hosted PDF and its [publication listing](https://www.stat.uchicago.edu/~pmcc/publications.html). New key `mccullagh1992_glm_intro`.
2. R Core Team, [“Family Objects for Models”](https://search.r-project.org/R/refmans/stats/html/family.html), “Details” and “Value”. Opened the official manual. Existing key `rstats_family2026`.
3. R Core Team, [“Summarizing Generalized Linear Model Fits”](https://search.r-project.org/R/refmans/stats/html/summary.glm.html), “Details” and “Value”. Opened the official manual. New key `rstats_summary_glm2026`.
4. Nelder and Wedderburn, [“Generalized Linear Models”](https://academic.oup.com/jrsssa/article/135/3/370/7110572), 1972, DOI 10.2307/2344614. Opened the publisher metadata; full text was unavailable there. Used with McCullagh's history of the paper, not for an unchecked formula.

## Changes and checks

- Preserved the inherited clotting-time Gamma model and its infobox, questions and citations to the underlying claim; replaced unlocated textbook citation markers in the source paragraph with the opened McCullagh source and its page number. Added the Gamma-to-$\phi$ conversion, a Pearson estimate example, one collapsed derivation, hidden practice and two answered bank questions.
- The generated page grows from 256 to 3,134 body words and retains zero figures. The source-paragraph dependent Clotting-time data article has 1,256 words and one figure, above its 1,249-word and one-figure baseline. The source edit is limited to that paragraph; other GLM chapter citations are unchanged. The one collapsed proof covers the Gamma moments and common-scale quasi-score result, with no newly unproved result to log.
- Verification: `checks/dispersion-parameter.py` passes the Gamma, Pearson, worked, practice and inherited question arithmetic; the generator builds 718 articles and 557 questions; all 67 Python tests pass; offline bibliography verification passes for 441 entries; and `git diff --check` passes. Full Quarto HTML rendering is unavailable because Quarto is not installed; the generator used the system Pandoc shim.
