# Bayes classifier — research record

Concept page, rank 85. Baseline 496 words, no figures. Existing density-to-posterior derivation, class-prior treatment, plug-in distinction, infobox and question links preserved.

## Sources opened

- James, Witten, Hastie and Tibshirani, *An Introduction to Statistical Learning: with Applications in R*, first edition (Springer, 2013), author-hosted seventh printing at https://www.statlearning.com/s/ISLRSeventhPrinting.pdf . Read §2.2.3, printed pp. 37–39, especially equations (2.10)–(2.11), Bayes boundary, irreducible Bayes error and impossibility of computing it without true conditional probabilities. New bibliography entry requested.
- Same book §4.4, printed pp. 138–141, Gaussian class model and LDA as a plug-in approximation of the Bayes rule.
- Dodge (2008) authorized index searched for Bayes classifier and decision theory; no matching entry, so not cited here. No origin or priority claim is made.
- Worked question bank items `ex-sl-08-1` (unequal priors and Bayes boundary), `ex-sl-08-2` (unequal costs) and `ex-sl-11-4` (Bayes error versus nearest-neighbour error) all inspected, with worked answers.

## Fact audit

- **Checked**: under zero–one loss, predicting the largest conditional class probability minimizes conditional and overall misclassification risk; Bayes risk is $1-E[\max_g P(Y=g\mid X)]$: ISLR §2.2.3, pp. 37–39 and derivation below.
- **Checked**: class probabilities are proportional to prior times class-conditional density, and shared evidence cancels in the argmax: ISLR §4.4, pp. 138–141; existing source material.
- **Checked**: with two classes and miss cost $c_{21}$, false alarm cost $c_{12}$, compare the posterior expected costs rather than probabilities alone. Derived in one proof box; numeric examples checked in `checks/bayes-classifier.py`.
- **Assumed**: classes exhaustive, losses fixed, probabilities calibrated for the target population, class-conditional densities defined at the feature vector.
- **Disputed/limited**: Bayes-optimal is optimal only for the stated joint distribution and loss. It does not imply zero error, nor that an estimated classifier attains Bayes risk. Class-prior shift changes the decision even if class-conditional densities stay fixed.
