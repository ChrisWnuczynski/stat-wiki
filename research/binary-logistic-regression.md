# Binary logistic regression research

## Checked
- Dodge, authorized *Encyclopedia of Statistics* extraction, pp. 319–320: logit model, inverse transform, Bernoulli likelihood, binary and continuous predictor interpretation, epidemiology example.
- Rodríguez, Princeton GLM lecture notes §B.4.1–B.4.2, equations B.14–B.19, opened in full: Bernoulli exponential-family form, inverse logit, mean, variance and fitting weights.
- Berkson 1944 publisher DOI record: bibliographic metadata only. The full article was inaccessible, so the new article does not cite this record; its bioassay setting and regression account cite the full Dodge entry instead.
- Existing answered questions ex-sl-10-7 and ex-sl-18-6 test model interpretation and end-to-end validation. All new numeric examples are checked by checks/binary-logistic-regression.py.

## Assumed
- The independence model is an explicit modelling condition; it is not inferred from the observed binary labels.

## Disputed
- Dodge p. 319 describes a continuous predictor coefficient as “relative risk”; p. 320 correctly describes its exponent as an odds ratio and notes the rare-event approximation. The new page states odds ratio, avoiding this conflation.
- Dodge p. 320 prints an inconsistent worked confidence interval and a seemingly mistaken sign/scale for the age model. These numbers were not copied.
