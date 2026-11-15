## Lead context
Those observations are allowed to influence the fitted rule. A score on the same observations describes that fit. It is not, by itself, an honest estimate of the error on new cases, because the rule has already adapted to the cases being scored.{{cite:efron1983}} (§2, pp. 316–317) {{cite:hastie_esl2009}} (pp. 11–15, 228–246)

## Motivating example
Suppose three labelled points on a line are used as a one-nearest-neighbour classifier, and each point is allowed to count as its own neighbour. Every training point is then labelled correctly, so the training error is zero. A new point can still fall closest to a training point whose label is wrong for the new location. The training score has answered a question the fitting rule was guaranteed to get right. The new point asks a different question.{{cite:hastie_esl2009}} (pp. 11–15, 228–246)

## Intuition
Fitting searches for a rule that looks good on the cases it is allowed to see. Scoring those same cases asks the search to mark its own work. Holding a case out, including from preprocessing and from every tuning choice, asks the question a later case will ask. The price is that the rule being scored was trained on fewer cases than a rule trained on everything. A training score and a held-out score are both useful, and they are useful for different decisions.{{cite:stone1974}} (pp. 111–112) {{cite:efron1983}} (§2, pp. 316–317)

## Definition
Let \((X_i,Y_i)\), for \(i=1,\ldots,n\), be the observed cases. The **training set** is
\[
\mathcal T=\{(X_1,Y_1),\ldots,(X_n,Y_n)\}.
\]
A training recipe produces a rule \(\eta_{\mathcal T}\). For a new pair \((X,Y)\) from the same joint distribution, drawn independently of \(\mathcal T\), the conditional error of this one fitted rule is
\[
\mathrm{Err}_{\mathcal T}=\mathbb E\bigl[L\bigl(Y,\eta_{\mathcal T}(X)\bigr)\bigm|\mathcal T\bigr].
\]
Here \(L\) is the loss: \(0\) or \(1\) for a wrong label, or a squared difference for a numerical prediction. The expectation is over the new pair only. The training set is held fixed, so \(\mathrm{Err}_{\mathcal T}\) describes that particular fit. Averaging over training sets as well gives the expected error of the whole recipe.{{cite:efron1983}} (§2, pp. 316–317) {{cite:hastie_esl2009}} (pp. 11–15, 228–246)

The apparent error, or training error, uses the same cases that built the rule:
\[
\mathrm{err}=\frac1n\sum_{i=1}^n L\bigl(Y_i,\eta_{\mathcal T}(X_i)\bigr).
\]
It is a property of the fit to \(\mathcal T\). It is a biased estimate of \(\mathrm{Err}_{\mathcal T}\) when the recipe adapts to those cases. The two averages do not become the same quantity merely by being written with the same loss.{{cite:efron1983}} (§2, pp. 316–317) {{cite:hastie_esl2009}} (pp. 11–15, 228–246)

When the inputs are treated as fixed and only the responses are random, write the inputs as \(x_i\). The in-sample error replaces each training response by a fresh response \(Y_i^{0}\) at the same \(x_i\),
\[
\mathrm{Err}_{\mathrm{in}}=\frac1n\sum_{i=1}^n\mathbb E\bigl[L(Y_i^{0},\hat Y_i)\bigm|\mathcal T\bigr],
\]
where \(\hat Y_i=\eta_{\mathcal T}(x_i)\). Optimism is the random difference \(\mathrm{op}=\mathrm{Err}_{\mathrm{in}}-\mathrm{err}\). It compares two errors at the training inputs. It does not by itself measure error at a new input.{{cite:hastie_esl2009}} (pp. 11–15, 228–246)

## Interpretation
A small training error says that the rule matches the cases it was allowed to use. It does not say how often a new case will be wrong, and it does not say how a different training set would have fitted. Those are \(\mathrm{Err}_{\mathcal T}\) and the error of the recipe, respectively. Quoting one of them as if it were the other changes the claim.{{cite:efron1983}} (§2, pp. 316–317) {{cite:hastie_esl2009}} (pp. 11–15, 228–246)

The same distinction applies inside a three-way split. The training portion is allowed to move the fitted weights or coefficients. A validation portion may be allowed to choose a tuning value or a stopping time; those cases then belong to model construction, not to a final assessment. A test portion supports an assessment only when it was excluded from every one of those choices. After the rule is refitted on training and test cases together, the old test score describes the earlier fit.{{cite:cawley_talbot2010}} (§5.3, p. 2102) {{cite:hastie_esl2009}} (pp. 11–15, 228–246)

## Properties
If the training inputs are distinct and one-nearest neighbour may use a point as its own neighbour, the apparent zero–one error is \(0\). The nearest training input to \(x_i\) is \(x_i\) itself.{{cite:hastie_esl2009}} (pp. 11–15, 228–246)

For squared error, fixed inputs, and \(Y_i=f(x_i)+\varepsilon_i\) with independent noise of mean \(0\) and variance \(\sigma^2\), the expected in-sample optimism is
\[
\mathbb E(\mathrm{op})=\frac2n\sum_{i=1}^n\operatorname{Cov}(\hat Y_i,Y_i).
\]
The covariance is large when the fit lets \(Y_i\) pull its own prediction. If \(\hat Y=SY\) for a matrix \(S\) that does not depend on \(Y\), the sum equals \(\sigma^2\operatorname{tr}(S)\), so the expected optimism is \(2\sigma^2\operatorname{tr}(S)/n\). Ordinary least squares with \(d\) linearly independent columns has \(\operatorname{tr}(S)=d\). For an intercept-only fit, \(d=1\), \(\mathbb E(\mathrm{err})=\sigma^2(n-1)/n\) and \(\mathbb E(\mathrm{Err}_{\mathrm{in}})=\sigma^2(n+1)/n\).{{cite:hastie_esl2009}} (pp. 11–15, 228–246)

This identity is an expectation. A single training sample can have \(\mathrm{err}\) above or below \(\mathrm{Err}_{\mathrm{in}}\). The usual downward bias is a repeated-sample statement, not a promise about every file of data.{{cite:efron1983}} (§2, pp. 316–317) {{cite:hastie_esl2009}} (pp. 11–15, 228–246)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Suppose the training inputs are distinct. The distance from \(x_i\) to itself is \(0\), and the distance to every other training input is positive. One-nearest neighbour therefore predicts the observed label at \(x_i\). Every zero–one summand is \(0\), and \(\mathrm{err}=0\).{{cite:hastie_esl2009}} (pp. 11–15, 228–246)

Now take squared error and fixed inputs, with \(Y_i=f(x_i)+\varepsilon_i\) independent, \(\mathbb E(\varepsilon_i)=0\) and \(\operatorname{Var}(\varepsilon_i)=\sigma^2\). Let \(\hat Y_i\) be computed from the training responses. A fresh \(Y_i^{0}\) at \(x_i\) is an independent copy of \(Y_i\), so conditionally on the training sample
\[
\mathbb E\bigl[(Y_i^{0}-\hat Y_i)^2\bigm|\mathcal T\bigr]=\sigma^2+\bigl(f(x_i)-\hat Y_i\bigr)^2.
\]
Averaging over \(i\) and then over training samples gives
\[
\mathbb E(\mathrm{Err}_{\mathrm{in}})=\sigma^2+\frac1n\sum_{i=1}^n\mathbb E\bigl(f(x_i)-\hat Y_i\bigr)^2.
\]
Expand the training square as \(\bigl(f(x_i)-\hat Y_i+\varepsilon_i\bigr)^2\). Its expectation is
\[
\mathbb E\bigl(f(x_i)-\hat Y_i\bigr)^2+\sigma^2-2\mathbb E(\varepsilon_i\hat Y_i),
\]
because \(\mathbb E(\varepsilon_i)=0\) removes the cross term that contains only \(f(x_i)\). Also \(\operatorname{Cov}(\hat Y_i,Y_i)=\mathbb E(\varepsilon_i\hat Y_i)\). Subtracting \(\mathbb E(\mathrm{err})\) from \(\mathbb E(\mathrm{Err}_{\mathrm{in}})\) therefore leaves \((2/n)\sum_i\operatorname{Cov}(\hat Y_i,Y_i)\).{{cite:hastie_esl2009}} (pp. 11–15, 228–246)

If \(\hat Y=SY\) with \(S\) free of \(Y\), uncorrelated noise of variance \(\sigma^2\) gives \(\operatorname{Cov}(\hat Y_i,Y_i)=\sigma^2 S_{ii}\). The sum of those covariances is \(\sigma^2\operatorname{tr}(S)\). For a fixed design matrix \(X\) with \(d\) linearly independent columns, the least-squares hat matrix is \(S=X(X^{\mathsf T}X)^{-1}X^{\mathsf T}\), and
\[
\operatorname{tr}(S)=\operatorname{tr}\bigl((X^{\mathsf T}X)^{-1}X^{\mathsf T}X\bigr)=\operatorname{tr}(I_d)=d.
\]
The intercept-only column of ones has \(d=1\) and \(S_{ii}=1/n\). The residual sum of squares is \(\|(I-S)Y\|^2\). For mean-zero uncorrelated noise its expectation is \(\sigma^2\operatorname{tr}(I-S)=\sigma^2(n-1)\), so \(\mathbb E(\mathrm{err})=\sigma^2(n-1)/n\). Adding the expected optimism \(2\sigma^2/n\) gives \(\mathbb E(\mathrm{Err}_{\mathrm{in}})=\sigma^2(n+1)/n\).{{cite:hastie_esl2009}} (pp. 11–15, 228–246)
:::
:::

## Statistical use
Use the training set to estimate the rule that will be deployed, and report its size. Use a separate assessment for the error of that rule. If the assessment must also choose the recipe, repeat the choice inside each training portion and score only the omitted cases. Screening predictors on every case, and only then cross-validating the classifier, lets the omitted cases influence which predictors were kept. In one published Gaussian simulation with \(50\) samples, \(5000\) pure-noise predictors and a one-nearest-neighbour rule built from the \(100\) most correlated predictors, that order produced an average cross-validated error of \(3\%\) although every classifier had true error \(50\%\). Selecting the predictors inside each fold removes that advantage. An unsupervised filter that never looks at the labels does not create the same leak.{{cite:hastie_esl2009}} (pp. 11–15, 228–246) {{cite:cawley_talbot2010}} (§5.3, p. 2102)

The same rule covers scaling, imputation, and stopping. A mean and a standard deviation used to standardise inputs are part of the training recipe. If they are computed from cases that are later treated as untouched, those cases have already entered the fit. Choosing a penalty, a tree size, or a number of neighbours by the score that will also be published has the same effect.{{cite:cawley_talbot2010}} (§5.3, p. 2102) {{cite:stone1974}} (pp. 111–112)

## Worked example
Take training pairs \((0,0)\), \((1,0)\) and \((3,1)\), and the one-nearest-neighbour rule. The three inputs are distinct, so the apparent zero–one error is \(0\). Let a new input be uniform on \([0,3]\), independently of the training set, and let its true label be \(1\) when the input is at least \(1.2\). The midpoints between the ordered training inputs are \(0.5\) and \(2\). The rule predicts \(0\) on \([0,2)\) and \(1\) on \((2,3]\). It is wrong on \([1.2,2)\), an interval of length \(0.8\). Ties at the two midpoints have probability \(0\) under a continuous distribution, whichever label a tie rule uses. The conditional error is
\[
\frac{0.8}{3}=\frac{4}{15}.
\]
At the new input \(1.5\) the distances to \(0\), \(1\) and \(3\) are \(1.5\), \(0.5\) and \(1.5\). The nearest training label is \(0\), while the true label is \(1\).{{cite:hastie_esl2009}} (pp. 11–15, 228–246)

The same distinction appears for a numerical fit. Suppose responses \(1,3,3,5\) are fitted by their mean, the true mean is \(0\), and the noise variance is \(1\). The sample mean is \(3\) and the training squared error is
\[
\frac{(-2)^2+0^2+0^2+2^2}{4}=2.
\]
A fresh response at each of the four fixed inputs has conditional expected squared error \(1+(3-0)^2=10\). This sample's optimism is \(10-2=8\). The expected optimism for an intercept-only fit of four observations is \(2(1)/4=1/2\), and the expected training error is \(3/4\). One sample can sit far from those expectations: here the sample mean is three units from the truth, and that gap is charged to every in-sample prediction.{{cite:hastie_esl2009}} (pp. 11–15, 228–246)

**Your turn.** Training pairs \((0,0)\), \((2,1)\) and \((4,0)\) are classified by one-nearest neighbour. A new input is uniform on \([0,4]\), and its true label is \(1\) only when the input is at least \(1.5\). Find the apparent error and the conditional error of this fixed rule.

::: {.callout-tip collapse="true" title="Answer"}
The inputs are distinct, so the apparent error is \(0\). The midpoints are \(1\) and \(3\), so the rule predicts \(0\) on \([0,1)\), \(1\) on \((1,3)\) and \(0\) on \((3,4]\). It disagrees with the truth on \([1,1.5)\) and on \((3,4]\), of lengths \(0.5\) and \(1\). The conditional error is \(1.5/4=3/8\). At input \(3.5\) the nearest training point is \(4\), the predicted label is \(0\), and the true label is \(1\).{{cite:hastie_esl2009}} (p. 15)
:::

## Common misconceptions
A training error of zero is not evidence that new cases will be classified correctly. One-nearest neighbour produces that zero whenever the training inputs are distinct, before any new case has been seen. A held-out score is not honest merely because the cases were omitted from the last fitting step; omission has to precede screening, scaling, imputation, and tuning as well. The training error and a test error do not estimate the same target: one scores the cases that shaped the rule, and the other scores cases that did not. In-sample optimism is not the error at a new input. Finally, a single split can put the training error above the fresh-case error. Downward bias is a statement about the average.{{cite:efron1983}} (§2, pp. 316–317) {{cite:hastie_esl2009}} (pp. 11–15, 228–246) {{cite:cawley_talbot2010}} (§5.3, p. 2102)

## Assumptions and limits
The zero training error for one-nearest neighbour uses distinct inputs and counts each point as a neighbour of itself. Duplicate inputs with conflicting labels, or a rule that refuses zero distance, need a separate calculation. The covariance formula is for squared error at the training inputs, with new responses there independent of the training sample. The trace formula also needs a fitting matrix that does not itself depend on the responses. A nearest-neighbour or tree rule changes which points it uses, so that matrix argument does not apply, even though its training error can still be optimistic. The in-sample target is convenient for comparing fits. A deployed rule is usually judged at new inputs, which is a further average over those inputs.{{cite:hastie_esl2009}} (pp. 11–15, 228–246)

The Gaussian simulation uses one noise design with no true predictors. It shows how selection before splitting can manufacture a small cross-validated error. It is not a universal numerical gap. Grouped or time-ordered observations need the held-out unit to match the unit on which the rule will be used.{{cite:hastie_esl2009}} (pp. 11–15, 228–246) {{cite:cawley_talbot2010}} (§5.3, p. 2102)

## Connections
The [apparent error](apparent-error.qmd) is the training score, and the [fixed-rule error](fixed-rule-error.qmd) is the fresh-case target conditional on one fit. [Cross-validation](cross-validation.qmd) and its [nested](nested-cross-validation.qmd) form rebuild the training set without each omitted case. A [validation set](validation-set.qmd) chooses tuning values; a [held-out test set](a-held-out-test-set.qmd) is reserved for the last assessment. [Nearest neighbours](nearest-neighbours.qmd) make the zero training error concrete, and [overfitting](overfitting.qmd) is what that zero can conceal. A [bootstrap](bootstrap.qmd) training draw is a different way to rebuild a training set from the observed cases.{{cite:stone1974}} (pp. 111–112) {{cite:efron1983}} (§2, pp. 316–317) {{cite:hastie_esl2009}} (pp. 11–15, 228–246)

## Check yourself
[A tempting wrong turn](../questions/ex-sl-09-6.qmd) asks why the cross-validation score used to choose a tuning value is not an honest future-error estimate. [Separate tuning from evaluation](../questions/ex-sl-09-7.qmd) asks for a training, validation, and test workflow. [Tuning a nearest-neighbour classifier](../questions/ex-sl-11-7.qmd) asks what happens when \(k\) is chosen by the training error.

## History
Dividing a sample so that one part constructs a predictor and another part assesses it was already treated as standard practice in Stone's 1974 paper on cross-validatory assessment. He describes both a random division, set aside before the analyst looks at it, and divisions forced by the way the data arose. His cross-validation criterion repeats that division: a construction subsample of size \(n-1\) is used to form the predictor, and the omitted case is used to assess it. The paper calls these pieces construction and validation subsamples.{{cite:stone1974}} (pp. 111–112)

Efron's 1983 paper adopts training set for the observed cases from which a prediction rule is built, and apparent error for that rule's average loss on those same cases. The true error in his account is the expected loss on a future case while the training set is held fixed, and optimism is the difference between that true error and the apparent error. The in-sample calculation separates a further point: fresh responses at the original inputs, rather than fresh inputs, are enough to display the covariance penalty for squared error. Later work on model selection makes the practical boundary explicit. If a test partition has already been used to choose a penalty or a kernel width, it retains a memory of that choice and the published score is optimistic. The selection has to be redone inside each training portion.{{cite:efron1983}} (§2, pp. 316–317) {{cite:hastie_esl2009}} (pp. 11–15, 228–246) {{cite:cawley_talbot2010}} (§5.3, p. 2102)
