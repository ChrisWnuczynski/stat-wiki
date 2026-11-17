

## Lead context

When each recorded case carries both the measurements and the outcome, the outcome can be used to score a proposed rule. Supervised learning is that use: fit a rule that predicts the outcome from the measurements, on cases where the outcome was observed.{{cite:hastie_esl2009}} (pp. 1–2, 9) {{cite:james_islr2021}} (Ch. 2, §2.1.4, pp. 26–27)

## Motivating example

Three training cases sit on a line: a feature $0$ with label $0$, a feature $1$ with label $0$, and a feature $4$ with label $1$. A one-nearest-neighbour rule, asked about a new feature $3$, finds the training feature $4$ as the nearest and returns the label $1$. Asked about a new feature $2$, it finds the training feature $1$ and returns the label $0$. The labels on the three training cases are what make those two answers possible. Without the labels, the distances would still be defined and the prediction would not.{{cite:james_islr2021}} (Ch. 2, §2.1.4, p. 26) {{cite:hastie_esl2009}} (pp. 9–11)

## Definition

Supervised learning starts from inputs $X$ and one or more outputs $Y$, observed together on a training sample $(x_i,y_i)$. The fitted rule predicts $Y$ from $X$ on a new case. Formally, if $(X,Y)$ has a joint distribution, the target is a property of the conditional distribution of $Y$ given $X$, often the value $\mu(x)$ that minimises the expected loss at that $x$. The marginal distribution of $X$ is not the object.{{cite:hastie_esl2009}} (pp. 485–486, (14.1))

In the usual division, each observation $i=1,\ldots,n$ has predictors $x_i$ and a response $y_i$. The fit aims at prediction of a future response, or at inference about how the response is associated with the predictors. [Binary logistic regression](binary-logistic-regression.qmd), [linear discriminant analysis](linear-discriminant-analysis.qmd), generalised additive models, boosting, and support vector machines are supervised methods. So is ordinary regression of a quantitative response.{{cite:james_islr2021}} (Ch. 2, §2.1.4, pp. 26–27; Ch. 12, p. 495)

The inputs are also called predictors, features, or, in older writing, independent variables. The outputs are responses, or dependent variables. A quantitative output is a regression problem. A qualitative output is a [classification](classification.qmd).{{cite:hastie_esl2009}} (pp. 9–10) {{cite:james_islr2021}} (Ch. 2, §2.1.5, pp. 28–29)

The response supervises the fit. In the metaphor used for this problem, a teacher supplies the correct output, or the error of the student's output, for each training input. The mathematical version of that metaphor is a loss $L(y,\hat y)$ whose average one wants to be small on a new pair $(X,Y)$. Regression uses a quantitative $Y$. Classification uses a qualitative $Y$. Both are supervised, because both have a $Y$ on the training cases.{{cite:hastie_esl2009}} (pp. 485–486; pp. 9–10)

The conditional-risk target assumes future cases come from the same joint distribution as the training pairs, and that the loss used in fitting is the loss of the decision. A sample of labels that were assigned by a different process, or a loss that ignores a costly kind of mistake, supervises the wrong problem.{{cite:hastie_esl2009}} (pp. 485–486)

One-nearest neighbour, used above because its arithmetic is visible, stores the whole training sample and treats the closest label as the truth. In a region where the two classes overlap, that rule has a larger error than a rule based on the conditional probabilities. The example's training error of $0$ does not measure that overlap.{{cite:hastie_esl2009}} (pp. 9–11; p. 348)

Semi-supervised problems, with responses missing on part of the sample, sit outside the plain definition.{{cite:james_islr2021}} (Ch. 2, p. 28)

## Properties

For the three training pairs $(0,0)$, $(1,0)$ and $(4,1)$, the nearest training feature to a query $x$ determines the one-nearest-neighbour label. The distances from $3$ are $|3-0|=3$, $|3-1|=2$ and $|3-4|=1$, so the label is $1$. The distances from $2$ are $2$, $1$ and $2$, so the nearest training feature is $1$ and the label is $0$. The distances from $2/5$ are $2/5$, $3/5$ and $18/5$, so the label is $0$.

On the training points themselves, each point is at distance $0$ from itself and at a positive distance from the others. The one-nearest-neighbour label of each training point is the label that was recorded there, and the training error is $0$. That identity uses the labels twice: once to store them, and once to score them.{{cite:hastie_esl2009}} (pp. 9–11)

A partial version of the same structure is semi-supervised learning: responses are observed for $m$ of the $n$ cases and missing for the rest, and a method may use both parts. That extension is named as a separate case, outside the basic split into fully labelled and fully unlabelled samples.{{cite:james_islr2021}} (Ch. 2, §2.1.4, p. 28)

## Statistical use

Use a supervised method when the response on future cases is the decision and a sample of past responses exists. A binary clinical outcome is a setting for [binary logistic regression](binary-logistic-regression.qmd) or [linear discriminant analysis](linear-discriminant-analysis.qmd). A local rule, with no global formula, is a setting for [nearest neighbours](nearest-neighbours.qmd) or a [decision tree](decision-tree.qmd). The training cases estimate the rule. A later case, or a [cross-validation](cross-validation.qmd) fold, estimates the loss of the rule.{{cite:james_islr2021}} (Ch. 4, p. 129; Ch. 12, p. 495) {{cite:hastie_esl2009}} (pp. 485–486)

The loss should match the decision. Squared error fits a conditional mean. A misclassification count fits a class label. Estimating the conditional probabilities and then choosing the most probable class is the [Bayes classifier](bayes-classifier.qmd) when those probabilities are known, and it is the target of many fitted classifiers when they are not.{{cite:hastie_esl2009}} (p. 348, (10.20); pp. 485–486)

## Worked example

Training pairs $(0,0)$, $(1,0)$ and $(4,1)$ define a one-nearest-neighbour rule. At a new feature $3$ the distances to the training features are $3$, $2$ and $1$. The nearest training feature is $4$, so the predicted label is $1$. At a new feature $2$ the distances are $2$, $1$ and $2$. The nearest training feature is $1$, so the predicted label is $0$. At each training feature the nearest neighbour is the point itself, so all three training labels are reproduced and the training error is $0$.

**Your turn.** What label does this rule return at the feature $2/5$?

::: {.callout-tip collapse="true" title="Answer"}
The distances from $2/5$ to $0$, $1$ and $4$ are $2/5$, $3/5$ and $18/5$. The nearest training feature is $0$, so the label is $0$.
:::

## Common misconceptions

A supervised analysis is not any analysis that uses a computer, and it is not a clustering of the features. Clustering does not have a response to predict. If the labels in the example are thrown away, the distances remain and the predicted label does not.{{cite:james_islr2021}} (Ch. 2, §2.1.4, pp. 26–28) {{cite:hastie_esl2009}} (pp. 485–486)

Logistic regression is supervised classification, not a reason to call a binary problem a regression and stop. The response is qualitative. The fitted probability is a means to a class, and also a regression for that probability.{{cite:james_islr2021}} (Ch. 2, §2.1.5, pp. 28–29)

A training error of $0$, as in the one-nearest-neighbour calculation above, is not an estimate of the error on a feature that was not in the training set. The query at $3$ is a different question from the query at $4$.{{cite:hastie_esl2009}} (pp. 2, 9–11)

## History

The early supervised methods were linear: least squares for a quantitative response, linear discriminant analysis in 1936, and logistic regression in the 1940s. Trees in the mid-1980s, neural networks, and support vector machines in the 1990s enlarged the class of rules once the computing allowed it. The organised division into supervised and unsupervised problems is the framework of the modern statistical-learning texts.{{cite:james_islr2021}} (Ch. 1, p. 6; Ch. 2, §2.1.4) {{cite:hastie_esl2009}} (pp. xi, 1–2)

## Connections

[Classification](classification.qmd) is supervised learning with a qualitative response. [Simple linear regression](simple-linear-regression.qmd) is supervised learning with a quantitative response. [Unsupervised learning](unsupervised-learning.qmd) drops the response. Inside classification, [linear discriminant analysis](linear-discriminant-analysis.qmd), [binary logistic regression](binary-logistic-regression.qmd), [nearest neighbours](nearest-neighbours.qmd) and [decision trees](decision-tree.qmd) are different supervised rules for the same kind of $Y$. The [training set](training-set.qmd) is the collection of pairs the rule may use.{{cite:james_islr2021}} (Ch. 2, pp. 26–29; Ch. 4, p. 129) {{cite:hastie_esl2009}} (pp. 9–10)
