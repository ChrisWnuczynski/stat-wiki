# Linear predictor

Type: Concept/topic.

## Existing material read

- articles/linear-predictor.qmd before the depth pass: the GLM predictor formula and two GLM components, the interpretation of input columns and links, a numerical interaction example, three inline cited works, and twelve linked questions. Leading body: 520 words; no figures.
- sources/book/chapters/01-introduction-to-glms.qmd, especially §“The three components of a GLM”; questions/q-30.qmd, questions/q-40.qmd, and questions/c-16.qmd, including worked answers.

## Sources opened and facts used

1. Nelder and Wedderburn, [“Generalized Linear Models” (1972)](https://www.maths.usyd.edu.au/u/jchan/GLM/Nelder1972GLM.pdf), full paper, pp. 370–384. Read its motivation, systematic linear model, indicator and mixed input columns, link, and iterative fitting method. Bibliography key `nelder_wedderburn1972`.
2. B. D. Ripley, [Oxford course chapter “Observing Count Data”](https://www.stats.ox.ac.uk/~ripley/StatMethods/Counts.pdf), pp. 28–29. Checked the log-exposure offset and its fixed coefficient of one. Used to check the algebra, without a citation in the article because the note's publication year was not established.
3. Berkson, [“Application of the Logistic Function to Bio-Assay” (1944)](https://www.jstor.org/stable/3001865), p. 358, and Cox, [“The Regression Analysis of Binary Sequences” (1958)](https://www.jstor.org/stable/2983890), Summary and reproduced excerpt p. 216. Opened during the logit-link pass; checked the logit and binary-response interpretation again for this page.
4. Davison (2003) and McCullagh–Nelder (1989) books were not available for checking. Their citations were removed from this article and its inherited GLM component block.

## Verification and decisions

- Replaced the tautological hand-specified lead with a specific one naming inputs, weighted sum, response mean, and link. Added precise Definition, Properties, Statistical use, a Bernoulli logit Worked example, misconceptions, limits, connections, and two cited History paragraphs. Removed a link-only self-check section; the question links remain in the generated question list.
- One collapsed Proof box covers identity, log, and logit predictor contrasts, interaction slopes, inverse logit, and the fixed-coefficient exposure offset. The interaction example and its arithmetic remain.
- The page originally mixed capital X and lowercase x for the covariate vector. The relevant topic data and GLM source-chapter formulas now use lowercase x for observed covariates, leaving capital Y for the random response and capital X for random variables elsewhere.
- checks/linear-predictor.py recomputes the interaction example, response probabilities, odds multiplier, and offset relation, and asserts the rounded numbers displayed in the generated article.
- The GLM component statements, interaction example, and twelve question links remain. The reference list now uses sources opened for the claims. No figure, definition, example, or practice question was removed.
