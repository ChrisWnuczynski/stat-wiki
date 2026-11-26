## Lead context

A rule that predicts a later case from earlier cases, or that describes how those cases are arranged, is the object of statistical learning. Machine learning, in that statistical sense, is this enterprise: estimate the rule from data, and keep separate the error that a better rule could still remove from the error that the measured features cannot remove. The same activity is one of the places where statistics meets artificial intelligence. Hastie, Tibshirani, and Friedman put the science of learning in statistics, data mining, and artificial intelligence at once, and they treat neural networks as a class of models developed separately in statistics and in artificial intelligence from essentially the same idea: linear combinations of the inputs, then a nonlinear function of those combinations. {{cite:james_islr2021}} (Ch. 2, pp. 17–19, (2.3)) {{cite:hastie_esl2009}} (p. 1; Ch. 11, §11.1, p. 389)

## Motivating example

A laboratory can measure several properties of a blood sample and cannot, without exposing the patient, see whether a drug will cause a severe reaction. The measured properties are the inputs. The reaction is the output. A fitted rule takes the properties and returns a predicted risk. Even a perfect version of the rule, one that used the true dependence of risk on the measured properties, would still miss. The reaction also depends on things the sample did not record. The fitted rule’s extra miss, beyond that floor, is the part a different fit might shrink. {{cite:james_islr2021}} (Ch. 2, pp. 17–19)

## Definition

Statistical learning is a set of approaches for estimating a function $f$ in a relationship such as $Y=f(X)+\varepsilon$. Machine learning, as the term is used for that activity, is the same project described with inputs $X$, an output $Y$, and a learner fitted on a [training set](training-set.qmd) in which both are seen, or on features alone when no output is seen. In the statistical literature the inputs are called predictors, or classically the independent variables. In the pattern-recognition literature they are called features. The outputs are the responses. The wording differs. The split between what is measured and what is predicted does not. {{cite:james_islr2021}} (Ch. 2, p. 17) {{cite:hastie_esl2009}} (Ch. 2, §2.1, p. 9)

Two purposes are usual. In prediction, $Y$ is expensive or delayed, $X$ is in hand, and the forecast is $\hat Y=\hat f(X)$. The accuracy of that forecast splits, for squared error with $X$ and $\hat f$ held fixed, as

$$
\mathbb E(Y-\hat Y)^2=\bigl(f(X)-\hat f(X)\bigr)^2+\operatorname{Var}(\varepsilon).
$$


The first term is reducible error. The second is irreducible error, the variance of the remainder, which does not depend on how $\hat f$ was chosen. In inference, the form of $\hat f$ is the object: which inputs are associated with $Y$, and whether a straight line is enough. A flexible estimate can follow the sample more closely and can also follow noise that will not recur. {{cite:james_islr2021}} (Ch. 2, pp. 17–20, (2.3))

The problems divide again into [supervised learning](supervised-learning.qmd), where each training case has a response, and [unsupervised learning](unsupervised-learning.qmd), where the task is to describe the features. A qualitative response makes the supervised problem a [classification](classification.qmd). A quantitative response makes it regression. Hastie, Tibshirani, and Friedman’s additive model $Y=f(X)+\varepsilon$, with $\E(\varepsilon)=0$ independent of $X$, is the statistical model underneath the squared-error split: $f(x)$ is then the conditional mean. {{cite:hastie_esl2009}} (Ch. 2, §2.6.1, pp. 28–29) {{cite:james_islr2021}} (Ch. 2, pp. 26–29)

## Interpretation

Assume $Y=f(X)+\varepsilon$ with $\mathbb E(\varepsilon)=0$, and hold both $X$ and $\hat f(X)$ fixed, so that the only randomness left in the squared error is $\varepsilon$. Expanding the square gives

$$
\mathbb E\bigl(f(X)+\varepsilon-\hat f(X)\bigr)^2=\bigl(f(X)-\hat f(X)\bigr)^2+\operatorname{Var}(\varepsilon),
$$


because the cross term contains a factor $\mathbb E(\varepsilon)=0$. If $f(X)=10$ and $\hat f(X)=7$, the reducible term is $(10-7)^2=9$. If $\operatorname{Var}(\varepsilon)=9$, the expected squared error equals $18$. If instead $\hat f(X)=10$, the reducible term is $0$ and the expected squared error equals $9$, the irreducible floor. Replacing $10$ and $7$ by $4$ and $1$, with $\operatorname{Var}(\varepsilon)=4$, gives reducible error $9$ and expected squared error equals $13$. {{cite:james_islr2021}} (Ch. 2, p. 19, (2.3))

The split is an expectation at a fixed input and a fixed fit. It is not the gap between a training error and a test error on one sample, and it is not a statement about classification error. A training error of zero does not imply that the reducible error is zero. The identity scores a new response at a fixed $X$. Equation (2.3) assumes additive noise with mean zero, and it holds $X$ and $\hat f(X)$ fixed. If the fit was computed from data that include the response being predicted, the cross term need not vanish. If the loss is a misclassification count rather than a square, the split into a squared gap and a noise variance is a different result. The irreducible piece can also contain features that were simply never measured. Improving $\hat f$ does not recover them. {{cite:james_islr2021}} (Ch. 2, pp. 18–19, (2.3)) {{cite:hastie_esl2009}} (Ch. 2, §2.6.1, p. 28)

Choose the estimate of $f$ according to the purpose. A campaign that only needs to know who will respond can treat $\hat f$ as a black box. A scientific question about which measurements move the response cannot: the form of $\hat f$ has to be readable. Flexible tools, including trees, support vector machines, and neural networks, buy a wider class of functions and give up a simple reading. They do not automatically buy a smaller prediction error. [Overfitting](overfitting.qmd) is the name for a flexible fit that has made the reducible error worse on new cases by chasing the sample. The most flexible procedure is not always the best predictor. A less flexible $\hat f$ can have a smaller value of $(f-\hat f)^2$ on new draws because it varies less from sample to sample. {{cite:james_islr2021}} (Ch. 2, pp. 17–26)

## Worked example

Take $f(X)=10$, $\hat f(X)=7$ and $\operatorname{Var}(\varepsilon)=9$, with $X$ and $\hat f$ fixed and $\mathbb E(\varepsilon)=0$. The reducible error is $(10-7)^2=9$. The irreducible error is $9$. The expected squared prediction error equals $18$. A fit that recovered $f(X)$ exactly would have expected squared error $9$, not $0$.

**Your turn.** Now take $f(X)=4$, $\hat f(X)=1$ and $\operatorname{Var}(\varepsilon)=4$, again with the fit and the input fixed. What is the expected squared error?

::: {.callout-tip collapse="true" title="Answer"}
The reducible term is $(4-1)^2=9$. Added to the irreducible term $4$, the expected squared error equals $13$.
:::

## Connections

[Supervised learning](supervised-learning.qmd) and [unsupervised learning](unsupervised-learning.qmd) are the two main organisations of problems. [Classification](classification.qmd) is the supervised problem with a qualitative response. [Cluster analysis](cluster-analysis.qmd) and [dimensionality reduction](dimensionality-reduction.qmd) are unsupervised summaries. The [training set](training-set.qmd) is the sample the learner is allowed to use, and [overfitting](overfitting.qmd) is what a comparison of training error with later error is designed to catch. Artificial intelligence, in the sense Hastie, Tibshirani, and Friedman use when they introduce neural networks, is one of the fields in which those same input–output models were built, alongside the statistical development of projection pursuit and related smoothers. The statistical account is the function $f$, the loss, and the split of error into a part the fit can still reduce and a part it cannot. {{cite:james_islr2021}} (Ch. 2, pp. 26–29) {{cite:hastie_esl2009}} (Ch. 11, §11.1, p. 389; Ch. 2, §2.1, p. 9)

## History

Least squares, at the beginning of the nineteenth century, is the oldest of these fitting rules, built for a quantitative response and first applied in astronomy. Linear discriminant analysis, in 1936, and logistic regression, in the 1940s, extended the project to qualitative responses. The generalised linear model, in the early 1970s, collected linear and logistic regression as special cases. By the 1980s, computation had made nonlinear fits practical: classification and regression trees, generalised additive models, and neural networks. Support vector machines followed in the 1990s. Statistical learning became the name of the subfield concerned with supervised and unsupervised modelling and prediction. *The Elements of Statistical Learning* is the account of the more mathematical development of the same material, written for readers in statistics and also for readers in artificial intelligence. Neural networks are the chapter in which that overlap is sharpest: one family of models, two histories, the same extracted features. {{cite:james_islr2021}} (Ch. 1, pp. 6–7) {{cite:hastie_esl2009}} (p. 1; Ch. 11, §11.1, p. 389)
