# Cross-validation

Type: Concept/topic.

## Material checked

- `articles/cross-validation.qmd`: initial 1,410 words, zero figures, eleven linked questions, three nested definitions, and a five-fold schedule.
- `sources/stat3006/chapters/sl-09-error-rates.qmd`: the leave-one-out, K-fold, and nested cross-validation explanations that generate the article and several related pages.

## Sources opened and used

1. Mervyn Stone, [“Cross-Validatory Choice and Assessment of Statistical Predictions”](https://sites.stat.washington.edu/courses/stat527/s14/readings/Stone1974.pdf), *Journal of the Royal Statistical Society B* **36** (1974), pp. 111–133. Read pp. 111–116, especially the distinction between choice and assessment and the “two-deep” assessment on pp. 114–115. Key `stone1974`.
2. Trevor Hastie, Robert Tibshirani, and Jerome Friedman, [*The Elements of Statistical Learning*](https://mcube.lab.nycu.edu.tw/~cfung/docs/books/hastie2009elements_of_statistical_learning.pdf), 2nd ed. (2009), Chapter 7 §§7.10.1–7.10.2, pp. 241–246, and §7.12, pp. 255–257. Read the K-fold and leave-one-out definitions, target and variance discussion, and preprocessing guidance. Key `hastie_esl2009`.
3. Gavin Cawley and Nicola Talbot, [“On Over-fitting in Model Selection and Subsequent Selection Bias in Performance Evaluation”](https://jmlr.org/papers/volume11/cawley10a/cawley10a.pdf), *Journal of Machine Learning Research* **11** (2010), pp. 2079–2107. Read §1, pp. 2079–2081, the criterion-selection discussion, and §5.3, p. 2102, on assessing selection within outer folds. Key `cawley_talbot2010`.

The Geisser 1975 journal text was unavailable in full. Its attribution to K-fold cross-validation and the extra bibliography-only entry were removed from the generated article and citation mapping. The source chapter had also called a selected validation minimum a “test” error and produced the broken sentence “studied by .”; both are corrected.

## Changes and checks

- Added a reader-facing introduction, target and weighted-score explanation, one collapsed proof of fold weighting and equal-risk minimum selection bias, practical splitting advice, a worked eleven-case example, and two historical paragraphs.
- Defined every symbol in the new formula and linked the three more specific cross-validation articles with exact relationships. The source chapter retains its leave-one-out and K-fold formulas, five-fold schedule, nested algorithm, and question links.
- Corrected the lead’s grammatical article through `article_leads.json`, because the generator reads its hand-specified subject there. Corrected unsupported attribution, unlocated citations, and selection terminology in the shared source; removed the unopened Geisser key from the citation map.
- `checks/cross-validation.py` recomputes the values printed in the generated article. No figures or questions were removed.
- The generated page has 2,716 words, zero figures, one Proof callout, eleven distinct question links, and three bibliography entries. The build produced 718 articles and 557 question pages; all 67 Python tests, the exact-value check, and offline verification of 405 bibliography records pass.
