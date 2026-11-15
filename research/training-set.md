# Training set

Type: Concept/topic.

## Existing material read

- `articles/training-set.qmd` before the edit: topic lead, the apparent-error warning, the opening of the error-rate chapter, and the training/validation/test sentence from the networks chapter. Citations present: Efron 1983, Stone 1974, Hastie–Tibshirani–Friedman 2009, Bishop 2006, and Cawley–Talbot 2010. Fifteen linked questions. No figures. Leading body: 221 words under the `PROGRESS.md` count.
- `sources/stat3006/chapters/sl-09-error-rates.qmd`, especially the opening, the apparent-error definition, and the one-nearest-neighbour training-error argument; `sources/stat3006/chapters/sl-16-networks-in-practice.qmd`, section on training, validation, and test sets.

## Sources opened and facts used

1. Trevor Hastie, Robert Tibshirani, and Jerome Friedman, *The Elements of Statistical Learning*, 2nd edition, 12th printing (January 2017), PDF reached from [the authors' download page](https://hastie.su.domains/ElemStatLearn/download.html). Read p. 11 (training data as the measurements used to construct the prediction rule), p. 15 (one-nearest neighbour has training error 0), pp. 228–230 (conditional error, training error, in-sample error, optimism, and the covariance and trace formulas), and pp. 245–246 (selection before cross-validation; the reported simulation with average cross-validated error 3% against a true error of 50%). Existing key `hastie_esl2009`.
2. Bradley Efron, [“Estimating the Error Rate of a Prediction Rule: Improvement on Cross-Validation” (1983)](https://people.eecs.berkeley.edu/~jordan/sail/readings/archive/efron-improve_cv.pdf), *Journal of the American Statistical Association* 78(382), 316–331. The file is an image scan; the text was read from the extracted pages. Read the introduction on p. 316, where the observed cases are called the training set and the apparent error is their average loss, and §2 on pp. 316–317, where the true error is conditional on the training set and optimism is true error minus apparent error. Existing key `efron1983`.
3. M. Stone, [“Cross-Validatory Choice and Assessment of Statistical Predictions” (1974)](https://sites.stat.washington.edu/courses/stat527/s14/readings/Stone1974.pdf), *Journal of the Royal Statistical Society B* 36(2), 111–147. Read pp. 111–112: division into a construction subsample and an assessment subsample, and the leave-one-out construction of size \(n-1\). Existing key `stone1974`.
4. Gavin C. Cawley and Nicola L. C. Talbot, [“On Over-fitting in Model Selection and Subsequent Selection Bias in Performance Evaluation” (2010)](https://jmlr.org/papers/volume11/cawley10a/cawley10a.pdf), *Journal of Machine Learning Research* 11, 2079–2107. Read the abstract on p. 2079 and §5.3 on p. 2102: a test partition that has already been used to choose hyperparameters is no longer untouched, and selection should be repeated inside each training portion. Existing key `cawley_talbot2010`.
5. Thomas M. Cover and Peter E. Hart, [“Nearest neighbor pattern classification” (1967)](https://isl.stanford.edu/~cover/papers/transIT/0021cove.pdf), *IEEE Transactions on Information Theory* 13(1), 21–27. Read pp. 21–22. The paper calls the labelled cases “correctly classified samples” and does not use the phrase training set. It was not cited.

Bishop 2006 remains cited because the existing networks excerpt cites it. That book was not opened for this page, and no new sentence depends on it.

## Verification and decisions

- Added a formula-free continuation of the lead, then motivation, intuition, a conditional-error definition, interpretation of the three-way split, the nearest-neighbour and squared-error properties, one collapsed proof, a statistical-use discussion of leakage, two solved numerical examples, a hidden exercise, misconceptions, limits, connections, question links, and two history paragraphs.
- The proof covers the distinct-input one-nearest-neighbour training error, the squared-error covariance identity, the trace formula, and the intercept-only expectations. It does not claim the zero–one covariance formula stated more generally in the opened Hastie–Tibshirani–Friedman account.
- The origin of the English phrase *training set* was not established. Stone's opened pages say construction and validation subsamples. Efron's opened pages use training set as the name of the observed cases. No first use is asserted.
- `checks/training-set.py` checks the nearest-neighbour distances and error lengths, the intercept-only sample, and the expected optimism with exact fractions.
- The original definition, both chapter excerpts, five citation keys, infobox, and fifteen question links remain. No figure, definition, example, or practice question was removed.
