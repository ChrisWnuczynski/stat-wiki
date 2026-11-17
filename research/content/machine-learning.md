

## Lead context

A rule that predicts a later case from earlier cases, or that describes how those cases are arranged, is the object of statistical learning. Machine learning, in that statistical sense, is this enterprise: estimate the rule from data, and keep separate the error that a better rule could still remove from the error that the measured features cannot remove.{{cite:james_islr2021}} (Ch. 2, pp. 17–19, (2.3)) {{cite:hastie_esl2009}} (pp. 1–2, 9)

## Motivating example

A laboratory can measure several properties of a blood sample and cannot, without exposing the patient, see whether a drug will cause a severe reaction. The measured properties are the inputs. The reaction is the output. A fitted rule takes the properties and returns a predicted risk. Even a perfect version of the rule, one that used the true dependence of risk on the measured properties, would still miss. The reaction also depends on things the sample did not record. The fitted rule's extra miss, beyond that floor, is the part a different fit might shrink.{{cite:james_islr2021}} (Ch. 2, pp. 17–19)

## Definition

Statistical learning is a set of approaches for estimating a function $f$ in a relationship such as $Y=f(X)+\varepsilon$. Machine learning, as the term is used for that activity, is the same project described with inputs $X$, an output $Y$, and a learner fitted on a [training set](training-set.qmd) in which both are seen, or on features alone when no output is seen.{{cite:james_islr2021}} (Ch. 1, pp. 6–7; Ch. 2, p. 17) {{cite:hastie_esl2009}} (pp. 1–2, 9)

Two purposes are usual. In prediction, $Y$ is expensive or delayed, $X$ is in hand, and the forecast is $\hat Y=\hat f(X)$. The accuracy of that forecast splits, for squared error with $X$ and $\hat f$ held fixed, as
\[
\mathbb E(Y-\hat Y)^2=\bigl(f(X)-\hat f(X)\bigr)^2+\operatorname{Var}(\varepsilon).
\]
The first term is reducible error. The second is irreducible error, the variance of the remainder, which does not depend on how $\hat f$ was chosen. In inference, the form of $\hat f$ is the object: which inputs are associated with $Y$, and whether a straight line is enough.{{cite:james_islr2021}} (Ch. 2, pp. 17–20, (2.3))

The problems divide again into [supervised learning](supervised-learning.qmd), where each training case has a response, and [unsupervised learning](unsupervised-learning.qmd), where the task is to describe the features. A qualitative response makes the supervised problem a [classification](classification.qmd). A quantitative response makes it a regression.{{cite:hastie_esl2009}} (pp. 1–2, 9–10) {{cite:james_islr2021}} (Ch. 2, pp. 26–29)

Write the response as a systematic piece that depends on the features, plus a remainder. Learning estimates the systematic piece. Prediction cares whether the estimate is close on a new case. Inference cares which features enter the systematic piece and in what form. A flexible estimate can follow the sample more closely and can also follow noise that will not recur. The language of inputs and outputs is the machine-learning wording for the same split that statistics has long called predictors and responses.{{cite:hastie_esl2009}} (p. 9) {{cite:james_islr2021}} (Ch. 2, pp. 17–20, 26)

Assume $Y=f(X)+\varepsilon$ with $\mathbb E(\varepsilon)=0$, and hold both $X$ and $\hat f(X)$ fixed, so that the only randomness left in the squared error is $\varepsilon$. Expanding the square gives
\[
\mathbb E\bigl(f(X)+\varepsilon-\hat f(X)\bigr)^2=\bigl(f(X)-\hat f(X)\bigr)^2+\operatorname{Var}(\varepsilon),
\]
because the cross term contains a factor $\mathbb E(\varepsilon)=0$.{{cite:james_islr2021}} (Ch. 2, p. 19, (2.3))

If $f(X)=10$ and $\hat f(X)=7$, the reducible term is $(10-7)^2=9$. If $\operatorname{Var}(\varepsilon)=9$, the expected squared error equals $18$. If instead $\hat f(X)=10$, the reducible term is $0$ and the expected squared error equals $9$, the irreducible floor. Replacing $10$ and $7$ by $4$ and $1$, with $\operatorname{Var}(\varepsilon)=4$, gives reducible error $9$ and expected squared error equal to $13$.

The split is an expectation at a fixed input and a fixed fit. It is not the gap between a training error and a test error on one sample, and it is not a statement about classification error.{{cite:james_islr2021}} (Ch. 2, pp. 18–19)

Choose the estimate of $f$ according to the purpose. A campaign that only needs to know who will respond can treat $\hat f$ as a black box and spend its effort on prediction error. A scientific question about which measurements move the response cannot: the form of $\hat f$ has to be readable. Flexible tools, including trees, support vector machines, and neural networks, buy a wider class of functions and give up a simple reading. They do not automatically buy a smaller prediction error. [Overfitting](overfitting.qmd) is the name for a flexible fit that has made the reducible error worse on new cases by chasing the sample.{{cite:james_islr2021}} (Ch. 2, pp. 17–26)

The irreducible term is a bound. No choice of learner, and no increase in the size of the training set, reduces $\operatorname{Var}(\varepsilon)$ if the unmeasured contribution sits in $\varepsilon$. A new feature that pulls part of $\varepsilon$ into $f$ is a change of the problem, not a better fit of the old one.{{cite:james_islr2021}} (Ch. 2, pp. 18–19)

Machine learning, in this statistical sense, is not a refusal of probability models. The decomposition above is a probability calculation. The wording of inputs, outputs, and learners is another vocabulary for predictors, responses, and fitted rules.{{cite:hastie_esl2009}} (p. 9) {{cite:james_islr2021}} (Ch. 2, p. 17)

A training error of zero does not imply that the reducible error is zero. The identity scores a new response at a fixed $X$. The training responses have already been used to build $\hat f$ when the fit is not held fixed in that way.{{cite:james_islr2021}} (Ch. 2, pp. 18–19) {{cite:hastie_esl2009}} (p. 2)

The most flexible procedure is not always the best predictor. A less flexible $\hat f$ can have a smaller value of $(f-\hat f)^2$ on new draws because it varies less from sample to sample.{{cite:james_islr2021}} (Ch. 2, pp. 24–26)

Equation (2.3) assumes additive noise with mean zero, and it holds $X$ and $\hat f(X)$ fixed. If the fit was computed from data that include the response being predicted, the cross term need not vanish. If the loss is a misclassification count rather than a square, the split into a squared bias and a noise variance is a different theorem. The irreducible piece can also contain features that were simply never measured. Improving $\hat f$ does not recover them.{{cite:james_islr2021}} (Ch. 2, pp. 18–19, (2.3))

The decomposition requires an $f$ and a loss. A procedure whose only description is a software default has not yet been given either one. The statistical theory covers the rules that can be written in that form, not every algorithm that has been marketed under the same name.{{cite:james_islr2021}} (Ch. 1, pp. 6–7) {{cite:hastie_esl2009}} (pp. 1–2)

## Worked example

Take $f(X)=10$, $\hat f(X)=7$ and $\operatorname{Var}(\varepsilon)=9$, with $X$ and $\hat f$ fixed and $\mathbb E(\varepsilon)=0$. The reducible error is $(10-7)^2=9$. The irreducible error is $9$. The expected squared prediction error equals $18$. A fit that recovered $f(X)$ exactly would have expected squared error $9$, not $0$.

**Your turn.** Now take $f(X)=4$, $\hat f(X)=1$ and $\operatorname{Var}(\varepsilon)=4$, again with the fit and the input fixed. What is the expected squared error?

::: {.callout-tip collapse="true" title="Answer"}
The reducible term is $(4-1)^2=9$. Added to the irreducible term $4$, the expected squared error equals $13$.
:::

## Connections

[Supervised learning](supervised-learning.qmd) and [unsupervised learning](unsupervised-learning.qmd) are the two main organisations of problems. [Classification](classification.qmd) is the supervised problem with a qualitative response. [Cluster analysis](cluster-analysis.qmd) and [dimensionality reduction](dimensionality-reduction.qmd) are unsupervised summaries. The [training set](training-set.qmd) is the sample the learner is allowed to use, and [overfitting](overfitting.qmd) is what a comparison of training error with later error is designed to catch.{{cite:james_islr2021}} (Ch. 2, pp. 26–29) {{cite:hastie_esl2009}} (pp. 1–2, 9–10)

## History

Least squares, in the early nineteenth century, is the oldest of these fitting rules, built for a quantitative response. Linear discriminant analysis, in 1936, and logistic regression, in the 1940s, extended the project to qualitative responses. Generalised linear models, classification and regression trees, neural networks, and support vector machines followed as computation allowed nonlinear fits. Statistical learning became the name of the subfield concerned with supervised and unsupervised modelling and prediction. Statistical machine learning is the name of the more mathematical development of the same material.{{cite:james_islr2021}} (Ch. 1, pp. 6–7)

Learning from data is the name for the whole activity, split into supervised prediction of an outcome and unsupervised description of associations among inputs. Machine learning is the wording for inputs and outputs in that development.{{cite:hastie_esl2009}} (pp. xi, 9)
