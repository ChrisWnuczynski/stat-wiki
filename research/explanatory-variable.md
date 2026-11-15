# Explanatory variable

Type: Concept/topic.

## Existing material read

- `articles/explanatory-variable.qmd` before the edit: a definition with an observational-versus-designed distinction, Galton history lines, and the shoe-size regression output interpretation. Leading body: 415 words; no figures; 28 linked questions.
- `sources/stat2004/chapters/inf-06-regression.qmd`, regression introduction and fixed-input model, and `sources/stat1301/chapters/da-07-regression-examples.qmd`, the shoe-size model and its diagnostics.
- `questions/ex-da-alcohol-attendance.qmd` and `questions/q-31.qmd`, including their worked answers.

## Sources opened and facts used

1. Francis Galton, [“Regression towards Mediocrity in Hereditary Stature”](https://pdf.galton.org/essays/1880-1889/galton-1886-jaigi-regression-stature.pdf), *Journal of the Anthropological Institute* 15 (1886), pp. 246–263, especially pp. 246–247. Read his motivation, earlier seed experiments, and the family records of 930 adult children and 205 parentages. Used for History. Citation key `galton1886`.
2. NIST/SEMATECH, [e-Handbook §4.1.2](https://www.itl.nist.gov/div898/handbook/pmd/section1/pmd12.htm), first published 2002. Read the response/predictor/error decomposition, fixed-input line, and alternative names for explanatory variables. Used for Definition and relationships. Citation key `nist_process_model2002`, added here.
3. NIST/SEMATECH, [e-Handbook §4.4.4](https://itl.nist.gov/div898/handbook/pmd/section4/pmd44.htm), first published 2002. Read the residual definition and the warning that $R^2$ alone does not validate a fitted model. Used for statistical use and limits. Citation key `nist_model_fit2002`, added here.
4. Richard C. Dicker, [“Analyzing and Interpreting Data”](https://www.cdc.gov/field-epi-manual/php/chapters/analyze-interpret-data.html), CDC *Field Epidemiology Manual*, 6 January 2025. Read the analysis-planning and interpretation guidance, including the distinction between association and causation and possible confounding. Used for the observational-study caveat. Citation key `dicker2025_cdc`, added here.

## Verification and decisions

- The definition, original shoe-size output, Galton citations, and 28 question links remain. No content or figure was removed.
- The collapsed proof derives the unchanged-prediction identity under affine recoding and the stated $F=t^2$ identity for one full-rank slope. The conditions for the $t$ and $F$ reference laws are stated explicitly.
- New worked scores, interpolation, challenge, and the existing rounded shoe-size $t$, $F$, and $R^2$ relationship were recomputed by `checks/explanatory-variable.py`.
- The lead now says “an explanatory variable” and includes assigned as well as recorded values.
