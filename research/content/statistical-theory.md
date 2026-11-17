## Lead context

Statistical theory is the mathematical account of what an estimator, a test, and a prediction rule do when the data are random. It asks which procedures have a small bias, a small variance, or a small expected loss, and under which models those comparisons are valid. A single number computed from one sample is an estimate. The theory is about the procedure that would be applied to the next sample as well.{{cite:dodge2008}} (pp. 184–185, estimation and the estimator){{cite:hastie_esl2009}} (pp. 18–20, §2.4, expected prediction error)

## Definition — Scope

Estimation determines the value of a parameter associated with a population. A sample is drawn, and an estimator, a function of that sample, is evaluated. The number the function returns on one particular sample is the estimate. Point estimation returns one number. Interval estimation returns a set of plausible values. The foundations of this comparison, after the method of least squares and Pearson's method of moments, are Fisher's: maximum likelihood in 1912, and the 1922 account of what estimation is for, with the later vocabulary of biased, efficient, and sufficient estimators.{{cite:dodge2008}} (pp. 184–185)

Bias is the gap between the expected value of a statistic and the parameter. If \(T\) estimates \(\theta\) and \(\mathbb E[T]=\theta+b(\theta)\), then \(b(\theta)\) is the bias. When \(b(\theta)=0\), \(T\) is unbiased, and the mean of a large number of such estimates lands on \(\theta\). Precision, in the same entry, is a different quantity: it measures sampling error, the scatter of \(T\), and is not the bias. The divide-by-\(n\) variance
\[
S^2=\frac1n\sum_{i=1}^n(x_i-\bar x)^2
\]
has expectation \(\sigma^2-\sigma^2/n\), so its bias is \(-\sigma^2/n\). That gap is a property of the procedure. It is visible in the expectation, not in one unlucky sample.{{cite:dodge2008}} (p. 41)

Prediction adds a loss. For a quantitative response the usual loss is squared error, \(L(Y,f(X))=(Y-f(X))^2\). The expected prediction error is the expectation of that loss under the joint distribution of the inputs and the response. Conditioning on the inputs shows that the function with the smallest expected squared error is the conditional mean, \(f(x)=\mathbb E(Y\mid X=x)\). Replacing squared error by absolute error changes the target to the conditional median. The [loss and risk](loss-and-risk.qmd) of a decision are this same comparison written for an action at a fixed parameter: a loss that is zero when the action matches the parameter, and a risk that is the expected loss.{{cite:hastie_esl2009}} (pp. 18–20, §2.4)

The scope is the behaviour of procedures under an explicit probability model. [Regression analysis](regression-analysis.qmd) sits inside the subject once its coefficients are treated as estimates whose reliability can be examined, rather than only as a curve drawn through a cloud. The regression entry asks whether a fitted relation is statistically significant or only apparent, and it checks that question by residual analysis, with the standing condition that a prediction assumes the conditions of the fit still hold and that an error remains.{{cite:dodge2008}} (p. 452)

## Statistical use — The comparisons the theory licenses

Bias, variance, and expected loss rank procedures before any one sample is declared the winner. Mean squared error adds them. If \(\mathbb E[T]=\theta+b\) and \(\mathrm{Var}(T)=v\), then
\[
\mathbb E[(T-\theta)^2]=v+b^2.
\]
An estimator with bias \(2\) and variance \(1\) has mean squared error \(1+4=5\). An unbiased competitor with variance \(9\) has mean squared error \(9\). The biased procedure is closer, on average squared error, even though its expectation misses \(\theta\). Unbiasedness is one restriction that makes "best" mean something. Without a restriction, no estimator has the smallest risk at every parameter value at once, except in the trivial parameter space that contains only one point.{{cite:dodge2008}} (p. 41){{cite:hastie_esl2009}} (pp. 18–20, §2.4)

[Maximum likelihood](maximum-likelihood.qmd) is the construction that maximises the probability of the observed sample under a parametric model. A [sufficient statistic](sufficient-statistic.qmd) is the reduction that lets the rest of the sample be ignored for inference about the parameter. A [confidence interval](confidence-interval.qmd) and a test are the theory's interval and decision forms. Their coverage and their error rates are statements about repeated samples. A single interval either covers the parameter or it does not. The guarantee is attached to the method, and the [sampling distribution](sampling-distribution.qmd) is the object the guarantee is calculated from. On the prediction side, nearest neighbours try to estimate the conditional mean by an average in a neighbourhood of the query. Least squares instead assumes the regression function is approximately linear and pools the sample under that assumption. Both are approximations to the same expected-loss target. They differ in the assumption that makes the average stable.{{cite:hastie_esl2009}} (pp. 18–20, §2.4){{cite:james_islr2021}} (Ch. 2, §2.1.4, pp. 26–27)

[Parametric statistics](parametric-statistics.qmd) begins with a finite parameter. [Statistical learning theory](statistical-learning-theory.qmd) scores a class of prediction rules by future prediction error. Both inherit the expected-loss comparison. They differ in whether the unknown is a short parameter or an unspecified member of a large class. In the supervised setting the response is observed, so the loss can be scored. The fit may be used for prediction of a future response or for inference about how the response is associated with the predictors. Those are two uses of one comparison, not two subjects.{{cite:james_islr2021}} (Ch. 2, §2.1.4, pp. 26–27){{cite:hastie_esl2009}} (pp. 485–486, §14.1)

## Common misconceptions

A small variance is not a proof that the procedure is aimed at \(\theta\). The divide-by-\(n\) variance is more precise than a noisier unbiased competitor can be, and it is still biased by \(-\sigma^2/n\). Reporting only the scatter leaves the systematic gap unstated.{{cite:dodge2008}} (p. 41)

Squared error and absolute error do not pick the same summary. Squared error picks the conditional mean. Absolute error picks the conditional median. Calling both "the best prediction" without naming the loss treats two different targets as one.{{cite:hastie_esl2009}} (pp. 18–20, §2.4)

An estimate on one sample is not the sampling distribution of the estimator. The theory's coverage statement is a statement about the procedure. One realised interval is either right or wrong, and the data in hand do not reveal which.{{cite:dodge2008}} (pp. 184–185)

A regression curve that passes near the points has not, by that fact, established that the relation will persist. The reliability of the estimates, and of the predictions made from them, is a further question, and it is checked under the condition that the circumstances of the fit still hold.{{cite:dodge2008}} (p. 452)

## Connections

The applied face of the same subject is a [regression analysis](regression-analysis.qmd) whose coefficients are interpreted as estimates, a [robust](robust-statistics.qmd) alternative when the loss or the error law is in doubt, and a [resampling](resampling-statistics.qmd) calculation when the sampling distribution has no usable formula. [Loss and risk](loss-and-risk.qmd) name the scale on which an action is scored by expected loss. None of these replaces the theoretical question. Each of them is an answer to a case of it: which procedure, under which model, with what expected loss.{{cite:dodge2008}} (p. 452){{cite:hastie_esl2009}} (pp. 18–20, §2.4)

## History

The concept of estimation is as old as the first mathematical statistics. Least squares, associated with Gauss and with Legendre's 1805 publication, gave estimation a criterion. Pearson's method of moments, in papers of 1894 and 1898, gave a general construction for a parametric family. Fisher introduced maximum likelihood in 1912 and, in 1922, set out what estimation is for. In 1925 he supplied the definitions, including bias, efficiency, and sufficiency, that the subject still uses. Gauss, in 1821, in the course of the least-squares work, is the source of the unbiased estimator as a comparison of an expectation with the parameter.{{cite:dodge2008}} (pp. 41 and 184–185)

The parallel theory of tests is the contribution associated there with Neyman and Egon Pearson: the basis of hypothesis testing.{{cite:dodge2008}} (p. 372) Among the contributions listed with Rao are the Fisher–Rao theorem, the Rao–Blackwell theorem, and the Cramér–Rao inequality.{{cite:dodge2008}} (p. 450) The comparison of procedures by an explicit loss is a different development. Squared error selects the conditional mean, and absolute error selects the conditional median. That comparison is set out as statistical decision theory for a prediction rule.{{cite:hastie_esl2009}} (pp. 18–20, §2.4)
