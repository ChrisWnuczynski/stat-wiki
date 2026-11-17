# Generalised linear mixed model

Rank 484. Depth pass, batch AB.

## Scope and calculations

Read the generated article and all its source excerpts before extending the generator input. Baseline body contains 1091 whitespace-delimited words and 1 figures. Preserve definitions, examples, code, mathematical results and figures while correcting the specifically identified errors in pending substitutions.

The independent numerical script `checks/generalised-linear-mixed-model.py` recomputes the new worked example, its practice answer, selected question answers and numerical claims in the source excerpt. Symbolic or direct algebra checks support derivatives, recurrences, variance identities or decision inequalities where applicable.

## Actually read proper sources

- `bolker2009_glmm`: (pp. 127–128); (pp. 127–130, Box 2); (p. 130, Box 2); (pp. 129–130, Estimation); (pp. 127–130, random effects and Box 2). Full text: https://sciences.ucf.edu/biology/d4lab/wp-content/uploads/sites/23/2020/02/Bolker-et-al-2009-TREE.pdf.
- `nelder_wedderburn1972`: (§§1.1–1.3, pp. 371–372). Full text: https://www.maths.usyd.edu.au/u/jchan/GLM/Nelder1972GLM.pdf.
- `wuthrich_merz2022_glm`: (§5.3.5, pp. 155–156, eqs. 5.36–5.37); (§5.3.5, p. 156); (§5.3.5, pp. 155–156). Full text: https://link.springer.com/content/pdf/10.1007/978-3-031-12409-9_5.pdf.

Public data provenance: CRAN mlmRev mirror https://raw.githubusercontent.com/cran/mlmRev/master/data/Contraception.rda and its man/Contraception.Rd were read outside the repository. The check embeds only the compressed public numeric dataset, not reference text, and independently reconstructs/optimises one- and two-dimensional random-effects Laplace likelihoods in SciPy. Refit log likelihoods −1186.59284819728 and −1180.48800322357 reproduce every displayed coefficient/SD/correlation to stated rounding. Central-difference Hessians reproduce all random-intercept SE/z values and random-slope urban z4.69. The dataset description and report title disagree on survey year; the article avoids choosing an unsupported date.

## Shared proposals

Exact source/metadata/citation substitutions are in the ignored per-slug pending JSON; orchestrator reviews and applies them. These include 8 exact old/new substitutions.

## Encyclopedia orientation

Dodge orientation additionally checked printed219 (pdf-0222). Its Generalized Linear Regression entry concerns nonconstant/correlated linear-model errors, distinct from the conditional exponential-family GLMM researched here; it is not cited for the GLMM definition.

## Validation

The final build passed: 718 articles, 626 question pages, 88 figures. All 15 AB numerical/generated-article checks passed, including this page's independent check. Offline verification passed for 665 bibliography entries. The full 72-test run passed 71 tests, including all 517 completed-page calculation scripts. Its sole failure was a custom heading in another batch's Wold decomposition page; a further audit identified the same alias issue in law of total probability. After both inputs were corrected, the failed citation/structure test passed in a focused rerun. All AB citation locators, hidden answers, self-check links, custom heading aliases and prose/figure preservation audits passed. Global `git diff --check` passed. The orchestrator will run the fresh full build and suite after merging the batches. Exact logs and page-level counts are in `/workspace/statwiki-run/report-ab.json`.
