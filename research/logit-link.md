# Logit link

Type: Concept/topic.

## Existing material read

- `articles/logit-link.qmd` before the edit: link and inverse-link formulas, canonical-link and coefficient statements, an interpretation comparing doubled odds with probability change, separation caveat, 21 question links, and three inline citations. Leading body: 543 words; no figures.
- `sources/book/chapters/01-introduction-to-glms.qmd`, especially the binary-response model, canonical-link definition, three link functions, coefficient interpretation, and Bernoulli likelihood.
- `questions/c-20.qmd`, `questions/ex-sl-10-2.qmd`, and `questions/q-38.qmd`, including their available answers.

## Sources opened and facts used

1. Joseph Berkson, [“Application of the Logistic Function to Bio-Assay”](https://assets.super.so/934de54e-7de8-4a8b-ba45-0cc6967ed8f7/files/4c4d2123-d4b0-422e-9537-292819e1e055/berkson1944.pdf), original 1944 full text, especially pp. 357–363. Verified his dose-response setting, logistic curve, and use of the term *logit*. Existing key `berkson1944`.
2. David Cox, [“The Regression Analysis of Binary Sequences”](https://academic.oup.com/jrsssb/article/20/2/215/7027376), 1958 publisher record and article description. [Reproduced excerpt](https://www.ma.imperial.ac.uk/~hbattey/lshtmSh20221108.pdf) shows his binary regression and logistic-law motivation. Existing key `cox1958_logistic`; the complete original article was not available from the publisher.
3. Nelder and Wedderburn, [“Generalized Linear Models”](https://www.maths.usyd.edu.au/u/jchan/GLM/Nelder1972GLM.pdf), original 1972 full text, consulted for the unified binomial GLM context. Existing key `nelder_wedderburn1972`.
4. Germán Rodríguez, [“Binomial Errors and Link Logit”](https://grodri.github.io/glms/notes/a2s4), Princeton University course material, opened for an explicit derivation of the binomial natural parameter and inverse logit. It is corroboration only; the article's derivation is written out and cites the primary GLM paper.
5. The existing source chapter's citations to Agresti (2002) for odds-ratio interpretation and Bliss (1935) for the probit comparison. Existing keys `agresti2002` and `bliss1935`; full texts were unavailable, so new arithmetic and properties were independently proved and checked.

## Verification and decisions

- The original formulas, doubled-odds example, complete-separation description, citations, and 21 linked questions remain. No figure or example was removed.
- A single collapsed proof establishes monotonicity and symmetry, inverse-link derivative, the binomial canonical parameter, the covariate odds multiplier, and the no-finite-MLE result under the strict scalar separation condition in the original article.
- `checks/logit-link.py` recomputes the original doubled-odds example, the new group and reader exercises, inverse-logit identities, derivative, and a separated-sample likelihood sequence.
- The waived local McCullagh–Nelder PDF was not used. The chapter already cites it, and its existing citation is preserved; the new discussion uses the opened primary papers and an independently checked derivation.
