# Fisher scoring

Type: Concept. Rank 223. Tier: full.

## Material checked

- **Checked:** Baseline 520 words and no figures. The source chapter already derives the GLM score and the weighted update. The added example is a two-observation Poisson log-link iteration that the source chapter does not compute.
- **Checked:** R `glm` manual. `glm.fit` uses iteratively reweighted least squares. The fitted object stores `iter`, working `weights`, `prior.weights` and `converged`. The manual says the design was inspired by Hastie and Pregibon and lists McCullagh and Nelder among its references. That list was not opened.
- **Checked by code:** from $\boldsymbol\beta=\mathbf 0$, one step reaches slope $2$ and mean $e^2=7.389056$, printed $7.3891$. The next slope is $1+3e^{-2}=1.406006$, printed $1.4060$, with second mean $4.079628$, printed $4.0796$. The interpolating slope is $\log 3=1.098612$, printed $1.0986$.
- **Assumed:** Independent Poisson counts and a log link. Under that link the observed and expected Hessians agree.
- **Disputed:** Nothing in the manual contradicts the hand iteration. The manual names the loop IWLS; the page name Fisher scoring is the expected-information form of that step, which coincides with Newton here.

## Sources opened and used

1. R Core Team, `glm` manual, `https://stat.ethz.ch/R-manual/R-devel/library/stats/html/glm.html`. Existing key `rstats_glm2026`.

## Skipped

Nelder and Wedderburn (1972) and McCullagh and Nelder (1989) were not opened. No claim is sourced to their pages.
