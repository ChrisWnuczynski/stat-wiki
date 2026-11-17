# kyphosis-data

## Sources opened

- `hastie_tibshirani1986`: https://pdodds.w3.uvm.edu/files/papers/others/1986/hastie1986a.pdf
- `r_kyphosis2026`: https://stat.ethz.ch/R-manual/R-devel/library/rpart/html/kyphosis.html (software data definitions only)
- `nelder_wedderburn1972`: https://www.maths.usyd.edu.au/u/jchan/GLM/Nelder1972GLM.pdf

The locators are recorded immediately after each citation in the article source. The numerical script recomputes the worked example and reads the generated article. No external source files are committed.

## Verification items

- kyphosis-data: the age-only mgcv edf, intercept and smooth-test statistics in the source chapter need a reproducible fit with recorded package version.

The 81 built-in rpart records were read from the Rdatasets export. Ages and binary outcomes are embedded in the check for reproducibility; no patient identifiers are used. R/mgcv was unavailable locally, so version-specific GAM outputs require the separate follow-up recorded above.

Reproduced full age-smooth fit using portable R4.5.0, mgcv1.9-3, rpart4.1.24 from Debian packages (runtime outside repo). edf2.22344180416414, refdf2.80557721914319, chi-sq6.35590636926641, p.0762373466512047; intercept−1.50919301706596, SE.315970050052515, z−4.77637996644027. Exact R call is rerun by checks/kyphosis-data.py. Opened official gam and s help solely to verify software defaults: thin plate basis and known-scale UBRE selection. Staged removal of older unverified printout claims.
