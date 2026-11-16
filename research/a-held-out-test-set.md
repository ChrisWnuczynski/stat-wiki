# A held-out test set

Type: Method/concept. Rank 58.

## Material checked

- Frozen baseline: 721 body words, zero figures. Read the inherited split discussion, conditional binomial error claim, two formulas, 18-in-120 test-size example, infobox and ten question links. The generated lead was grammatically broken (“is the apparent rate fails”); corrected its generator input in `article_leads.json` so the article starts with one specific sentence.
- **Checked:** Cawley and Talbot (2010), open-access original in *JMLR*, pp. 2079–2081 and §5.3, distinguishes fitting/selection from evaluation and explains optimistic selection bias. Official scikit-learn §12.2 describes test leakage through preprocessing or feature selection and prescribes split-before-fit practice. Efron (1983) publisher abstract states the future-error target for a fitted prediction rule.
- **Checked by code:** the inherited 18/120 interval and required test size, the worked and practice confusion-matrix rates, and the approximate intervals are recalculated in `checks/a-held-out-test-set.py`.
- **Assumed:** For the binomial proof, test cases are independent draws from one target population conditional on the fixed trained rule. Class-specific rates condition additionally on class membership. The worked classifiers are already fixed before test outcomes are observed.
- **Disputed:** A test score for one fixed fit does not directly evaluate a new model refitted on the test cases. A random row split is not automatically a valid test for grouped or time-ordered deployment. The article states those limitations directly.

## Sources opened and used

1. Gavin Cawley and Nicola Talbot, [*On Over-fitting in Model Selection and Subsequent Selection Bias in Performance Evaluation*](https://jmlr.org/papers/volume11/cawley10a/cawley10a.pdf), *JMLR* **11** (2010), pp. 2079–2107, especially pp. 2079–2081 and §5.3. Existing key `cawley_talbot2010`.
2. scikit-learn developers, [*Common pitfalls and recommended practices*](https://scikit-learn.org/stable/common_pitfalls.html), §12.2, Data leakage, official documentation. New key `sklearn_common_pitfalls2026`.
3. Bradley Efron, [*Estimating the Error Rate of a Prediction Rule: Improvement on Cross-Validation*](https://doi.org/10.1080/01621459.1983.10477973), *JASA* **78** (1983), publisher abstract checked for the stated future-error objective. Existing key `efron1983`.
4. Hastie, Tibshirani and Friedman, [*The Elements of Statistical Learning*](https://link.springer.com/chapter/10.1007/978-0-387-84858-7_7), Ch. 7 publisher page inspected; it identifies model assessment and selection but the preview did not expose the technical text. The author-hosted full-PDF URL was found but inaccessible through the research tools, so new technical claims do not cite it. Earlier inherited citations were replaced in the source paragraph with the opened sources above.

Dodge index directory was absent from `~/statwiki-sources/dodge2008`.

## Changes and checks

- Add a precise lead, target-risk distinction, conditional binomial proof, worked and practice confusion-matrix calculations, distinct leakage and sampling failures, and two answered bank questions. Preserve the original formulas and test-width example.
- The generated body has 3,055 words and zero figures. The original two formulas, 18-in-120 example, infobox and ten question links remain. The corrected source paragraph appears in the held-out article and its parent chapter. The lead fix uses `article_leads.json`, which is the generator input that supplies the page's opening sentence.
- Updating the checkpoint ledger made the citation-location test cover ranks 48–57. Replaced locator formats on their generator inputs and located the copied deviance, neural-unit and Gamma-link citations using opened sources. Ran numeric page checks for discrete distribution, skewness, dispersion parameter, sigmoid function, log link, deviance, hidden layer and held-out test set; all passed. The dependent inverse-link, link-function, positive-continuous-responses and null-deviance articles also rebuild with their shared paragraphs intact.
- Verification: the generator builds 718 articles and 557 questions; all 67 Python tests pass; offline verification covers 443 bibliography entries; and `git diff --check` passes. Full Quarto HTML rendering is unavailable because Quarto is not installed; the generator used the system Pandoc shim.
