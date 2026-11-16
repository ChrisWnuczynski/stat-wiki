# Generalised linear model

Type: Concept/definition.

## Material checked

- The generated article before this edit had 2,613 body words, three figure instances (inverse-link comparison, fish counts, and fitted latitude smooth), the three-component definition, the exponential-family mean–variance result, three worked exercises, and six linked questions.
- `sources/book/chapters/01-introduction-to-glms.qmd`, the fish-species question and answer in `sources/prep/chapters/alan*.qmd`, the linear-predictor and logit-link articles, and the bibliography mapping.

## Sources opened and used

1. J. A. Nelder and R. W. M. Wedderburn, [“Generalized Linear Models”](https://www.maths.usyd.edu.au/u/jchan/GLM/Nelder1972GLM.pdf), *JRSS A* **135** (1972), pp. 370–384. Read the Summary and Introduction, §1.1 on the random component, §§1.2–1.3 on predictor and link, §§2.1–2.4 on fitting and deviance, and §§3.1–3.3 on normal, Poisson and binomial members. Key `nelder_wedderburn1972`.
2. SAS Institute Inc., [*SAS/STAT® 12.1 User’s Guide*](https://support.sas.com/documentation/cdl/en/statug/65328/HTML/default/statug_intromod_sect011.htm), Chapter 3, “Generalized Linear Models.” Read its three-part model description and distinction between linking a mean and transforming data. The [official 2012 introduction](https://support.sas.com/documentation/onlinedoc/stat/121/intro.pdf) gives the complete manual's author, year and title on its cover page. New key `sas2012_glm`.
3. The [R `glm` documentation](https://www.stat.ethz.ch/R-manual/R-devel/library/stats/html/glm.html) and [family documentation](https://www.stat.ethz.ch/R-manual/R-devel/library/stats/html/family.html) were opened to check the inherited code example's family, link and iterative fitting. The article uses the original paper and SAS guide for located citations; no year was assigned to the rolling R-development documentation.
4. Simon Wood, [*mgcv* 1.9-4](https://www.stat.math.ethz.ch/CRAN/web/packages/mgcv/index.html), published 7 November 2025 according to CRAN. Read the package's [`gam` Description](https://stat.ethz.ch/R-manual/R-devel/library/mgcv/html/gam.html) and [`summary.gam` Details and Value](https://stat.ethz.ch/R-manual/R-devel/library/mgcv/html/summary.gam.html) for the inherited smooth-model worked answer. Key `wood2025_mgcv_docs`.

The McCullagh–Nelder and Davison books were unavailable for this pass and are no longer cited by the generated GLM article. The user waived the missing local McCullagh–Nelder PDF.

## Changes and checks

- Replaced the self-referential field in the lead. Added precise notation, the shared density convention, the response/link interpretation, a collapsed proof for the mean–variance formulas and link-scale effects, statistical-use advice, a numerical comparison of Poisson and Bernoulli fits, misconceptions, limits, connections, and two sourced History paragraphs.
- The linked fish-species exercise now uses lowercase $\mathbf x_i$ for a fixed covariate row and defines the fixed design matrix before its first use. Its original numerical outputs, worked answers and both figures remain. The answer paragraphs have located citations to the opened GLM paper or the `mgcv` documentation. The two other inherited worked answers cite the opened GLM paper.
- The shared mean–variance source now cites the opened Nelder–Wedderburn passages and its proof carries its own citation. The generator no longer adds a generic McCullagh–Nelder citation to a source proof that already has an inline citation. Other linked pages retain the explanation and proof.
- `checks/generalised-linear-model.py` verifies the printed contrasts, rounded inherited fish coefficients, all three figures, citations and single proof callout. The original three worked exercises and six question links remain.

## Verification

Generated article: 4,437 body words versus 2,613 before; three figure instances versus three before; six distinct question links; one collapsed Proof box. The exact-value check passes. The generator produced 718 articles and 557 question pages, all 67 Python tests pass, and offline validation passes for 410 bibliography entries. `git diff --check` is clean. The container lacked Quarto's executable for the final rebuild, so a temporary `/tmp/quarto` shim invoked the installed Pandoc for the generator's sole `quarto pandoc` call; no repository build command was changed. No rendered HTML build was attempted.

## Rank 28–37 practice correction

- Kept the worked example and added a “Your turn” problem with its answer in a collapsed callout.
- After rebuilding, the generated body has 4,501 words by the progress-table method.
