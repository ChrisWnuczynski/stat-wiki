# Effective degrees of freedom: source and verification notes

Type: concept. Baseline: 712 words, zero figures. Preserve the trace formula, spline matrix, spectral formula, four-direction example with edf 2.6, infobox and question backlinks, as well as existing citations. New material proves the spectral and covariance forms and separates basis size, fitted flexibility and prediction optimism.

## Checked

- Bradley Efron (2004), original full author-hosted PDF, https://efron.ckirby.su.domains/papers/2004PredictionErrorRev_May.pdf, §2 and equations (2.8)–(2.12), opened and read. It explicitly identifies trace of a fixed linear smoother as degrees of freedom, ordinary projections as dimension $p$, covariance extension to nonlinear fitting rules, and the optimism penalty.
- Simon Wood, official `mgcv` R documentation, https://stat.ethz.ch/R-manual/R-devel/library/mgcv/html/summary.gam.html, “Details” and “Value”, opened and read. It defines model edf as trace of influence matrix, term edf as a trace component, residual df as $n$ minus model df, and warns that smooth-term p-values neglect smoothing-parameter uncertainty.
- Dodge (2008), authorised extracted text `/workspace/statwiki-sources/dodge2008/pages/pdf-0160.txt`, printed p. 155, “Degree of Freedom”, read. It describes Fisher's 1925 terminology and the $n-1$ independent sample deviations. It does not discuss effective df for smoothers.
- The new four-direction multipliers and their sum were checked with `checks/effective-degrees-of-freedom.py`; the inherited $K=4$, $(d_1,d_2,d_3,d_4)=(0,0,1,9)$, $\lambda=1$ example yields 2.6, with centred term 1.6.

## Assumed or qualified

- The inherited book text says ten evenly spaced knots are a usual default; that is source- and implementation-dependent and is not used as a general recommendation in the new prose.
- The rank page's original book excerpt conflates polynomial degree with edf, says the full straight-line fit has one edf, and claims a reduced basis interpolates as $\lambda\to0$. Pending shared-source changes spell out the corrections; the new article gives the correct full-model versus centred-term distinction.
- The finite-sample covariance identity assumes fixed $S_\lambda$, independent equal-variance response errors, and a finite second moment. Data-selected smoothing parameters need the broader covariance definition for the complete rule.

## Disputed or unavailable

- The full 1990 Hastie–Tibshirani and 2017 Wood books were not accessible from publisher pages during this pass; inherited citations are preserved but new claims are supported by the opened original paper and official software documentation.
