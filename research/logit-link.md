# Logit link

Type: Concept/topic.

## Existing material read

- `articles/logit-link.qmd` before the edit: link and inverse-link formulas, canonical-link and coefficient statements, an interpretation comparing doubled odds with probability change, separation caveat, 21 question links, and three inline citations. Leading body: 543 words; no figures.
- `sources/book/chapters/01-introduction-to-glms.qmd`, especially the binary-response model, canonical-link definition, three link functions, coefficient interpretation, and Bernoulli likelihood.
- `questions/c-20.qmd`, `questions/ex-sl-10-2.qmd`, and `questions/q-38.qmd`, including their available answers.

## Sources opened and facts used

1. Joseph Berkson, [“Application of the Logistic Function to Bio-Assay”](https://assets.super.so/934de54e-7de8-4a8b-ba45-0cc6967ed8f7/files/4c4d2123-d4b0-422e-9537-292819e1e055/berkson1944.pdf), original 1944 full text, especially pp. 357–363. Verified his dose-response setting, logistic curve, and use of the term *logit*. Existing key `berkson1944`.
2. David Cox, [“The Regression Analysis of Binary Sequences”](https://academic.oup.com/jrsssb/article/20/2/215/7027376), 1958 publisher summary, and a [reproduced excerpt](https://www.ma.imperial.ac.uk/~hbattey/lshtmSh20221108.pdf) from p. 216. These support the history paragraph about binary sequences, explanatory variables, and the logistic law. Citation key `cox1958_logistic`.
3. Nelder and Wedderburn, [“Generalized Linear Models”](https://www.maths.usyd.edu.au/u/jchan/GLM/Nelder1972GLM.pdf), original 1972 full text, especially §§2.2 and 3.3, pp. 374, 379–380. The binomial log likelihood, logit, and probit links are shown there. Citation key `nelder_wedderburn1972`.
4. Albert and Anderson, [“On the existence of maximum likelihood estimates in logistic regression models”](https://citeseerx.ist.psu.edu/document?doi=358552a30531c785796a3ab041bc702e17f1d09a&repid=rep1&type=pdf), original 1984 full text, §2 Theorem 1, p. 3. This proves the no-finite-MLE claim under complete separation. Citation key `albert_anderson1984`.
5. Germán Rodríguez, [“Binomial Errors and Link Logit”](https://grodri.github.io/glms/notes/a2s4), Princeton University course material, opened for an explicit derivation of the binomial natural parameter and inverse logit. It is corroboration only; the article cites the primary GLM paper.

Agresti (2002), Bliss (1935), and McCullagh and Nelder (1989) were not opened. The correction removes citations to them from this article, including its inherited definition and interpretation.

## Verification and decisions

- The formulas, doubled-odds example, complete-separation description, and 21 linked questions remain. No figure or example was removed.
- A single collapsed proof establishes monotonicity and symmetry, inverse-link derivative, the binomial canonical parameter, the covariate odds multiplier, and the no-finite-MLE result under the strict scalar separation condition in the original article.
- `checks/logit-link.py` recomputes the doubled-odds example, the group and reader exercises, inverse-logit identities, derivative, and a separated-sample likelihood sequence; it also asserts the exact rounded values printed on the page.
