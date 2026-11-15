# Linear predictor

Type: Concept/topic.

## Existing material read

- articles/linear-predictor.qmd before the edit: the GLM predictor formula and two retained GLM components, the interpretation of input columns and links, a numerical interaction example, three inline cited works, and twelve linked questions. Leading body: 520 words; no figures.
- sources/book/chapters/01-introduction-to-glms.qmd, especially §“The three components of a GLM”; questions/q-30.qmd, questions/q-40.qmd, and questions/c-16.qmd, including worked answers.

## Sources opened and facts used

1. Nelder and Wedderburn, [“Generalized Linear Models” (1972)](https://www.maths.usyd.edu.au/u/jchan/GLM/Nelder1972GLM.pdf), original full paper, pp. 370–373. Read its motivation, linear model for systematic effects, indicator and mixed input columns, link, and fitting result. Existing bibliography key nelder_wedderburn1972.
2. B. D. Ripley, [Oxford course chapter “Observing Count Data”](https://www.stats.ox.ac.uk/~ripley/StatMethods/Counts.pdf), Poisson-regression section. Checked the log-exposure offset and its fixed coefficient of one. Used for corroboration; the article gives the algebra and cites the existing GLM references.
3. The local source chapter cites Davison (2003) and McCullagh–Nelder (1989); their full book texts were not opened. The user waived the missing local McCullagh–Nelder PDF. Existing citations remain, and new algebra is proved in the article.

## Verification and decisions

- Replaced the tautological hand-specified lead with a specific one naming inputs, weighted sum, response mean, and link. Added precise Definition, Properties, Statistical use, a Bernoulli logit Worked example, misconceptions, limits, connections, self-check, and two cited History paragraphs.
- One collapsed Proof box covers identity, log, and logit predictor contrasts, interaction slopes, inverse logit, and the fixed-coefficient exposure offset. The original interaction example and its arithmetic remain.
- The page originally mixed capital X and lowercase x for the covariate vector. The relevant topic data and GLM source-chapter formulas now use lowercase x for observed covariates, leaving capital Y for the random response and capital X for random variables elsewhere.
- checks/linear-predictor.py recomputes the original interaction example and new response probabilities, odds multiplier, and offset relation.
- The original GLM component statements, interaction example, three citations, and twelve question links remain. No figure, definition, example, or practice question was removed.
