# Linear discriminant analysis — rank 89

Type: method. Baseline: 1,542 words, 0 figures. Preserve the long pooled-covariance derivation and two-class numerical example in the source chapter, along with its citations and infobox.

## Sources opened

- **Checked:** James, Witten, Hastie and Tibshirani (2013), author-hosted *An Introduction to Statistical Learning*, §4.4.1–4.4.4, printed pp. 138–149. Read the Gaussian model, posterior score (4.19), plug-in estimates, three-class geometry, and comparison with QDA.
- **Checked:** Fisher (1936), Wiley publisher-hosted full original PDF, §§I–II, printed p. 179. Read the discriminant-function introduction, the four-measurement optimization, and the first two Iris species; the DOI page supplies title and date.
- **Checked:** the existing source chapter's two-class data and printed computations against a new NumPy calculation in `checks/linear-discriminant-analysis.py`.
- **Checked:** question-bank worked answers `ex-sl-08-3`, `ex-sl-08-7`, `ex-sl-18-7`; each directly exercises a different LDA feature.
- **Assumed:** deployment priors may differ from training frequencies in a deliberately balanced sample; the text treats the shift as a model input, not an empirical estimate.
- **Disputed:** none. Dodge has a Fisher biographical entry but no substantive LDA entry; its bibliography points to other discriminant-function work, so it is not cited for this article.

## Mathematical checks

For means 0 and 2, common variance 1 and priors 0.8 and 0.2, score difference class 2 minus class 1 is `2*x-2-log(4)`. Boundary 1.693147; at 1.4 the class-2 posterior is 0.357486, versus 0.689974 with equal priors; at 1.8 it is 0.553224. Verified independently by multiplying normal densities. Shared covariance cancellation and pooled-covariance rank bound are proved in the collapsed box.
