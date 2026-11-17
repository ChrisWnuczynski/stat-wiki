## Lead context
A digit on an envelope, a decision to treat, or a message marked as junk ends as a label. The features that lead to the label are measured; the label itself is one of a finite list. Classification is the statistical problem of using those features to assign the label, and of saying how often a new case will be assigned the wrong one.{{cite:james_islr2021}} (Ch. 4, p. 129) {{cite:hastie_esl2009}} (pp. 9–10)

## Motivating example
A mailbox study records, for each message, how often selected words and punctuation marks appear, together with the label email or spam. The label is known for the messages already filed. The working rule has to give a label to a message that has not been filed yet. One candidate looks at two frequencies only: if the share of the word "george" is below $0.6$ and the share of "you" is above $1.5$, call the message spam. Another candidate uses a weighted difference of the same two shares and compares it with zero. Both rules are classifiers. They differ in which messages they will mark, and the comparison that matters is the mark on a later message, not the mark on a message that was used to invent the rule.{{cite:hastie_esl2009}} (pp. 2–3)

## Intuition
Given the features, each class has a conditional probability. The class with the largest probability is the best single guess when every mistake counts the same. The probability of being wrong is then whatever probability is left over. Estimating those probabilities, or estimating a boundary that picks the same class, is the practical problem. A rule that only rearranges the cases already labelled has not yet faced that leftover probability.{{cite:hastie_esl2009}} (p. 348, (10.20)) {{cite:james_islr2021}} (Ch. 2, pp. 28–29)

## Definition
A response is qualitative, or categorical, when it takes values in a finite set of classes. Classification is the task of predicting that response from features. Assigning the predicted class is called classifying the case. Many classifiers first estimate the probability of each class and only then pick a label. In that respect they also behave like regression methods.{{cite:james_islr2021}} (Ch. 4, p. 129)

The naming follows the response, not the features. A quantitative response is a regression problem. A qualitative response is a classification problem. Logistic regression is the usual model for a binary qualitative response: despite the word regression in its name, it is a classification method, because the quantity it models is a class probability. The same method can be read as a regression for that probability. Features may themselves be quantitative or qualitative. After qualitative features are coded, most of the same fitting ideas apply.{{cite:james_islr2021}} (Ch. 2, pp. 28–29) {{cite:hastie_esl2009}} (pp. 9–10)

Write $G$ for the class and $p_k(x)=\Pr(G=k\mid X=x)$. A classifier is a map from $x$ to a class. The [Bayes classifier](bayes-classifier.qmd) selects
\[
k^\star(x)=\operatorname{argmax}_k p_k(x).
\]
Every other class is a mistake under equal misclassification costs.{{cite:hastie_esl2009}} (p. 348, (10.20))

A wider traditional use of the same word covers any grouping of similar objects, and it splits that activity into a description of groups and a prediction that leads to an action. The grouping methods that do not use a response are [cluster analysis](cluster-analysis.qmd). The prediction case is the problem above.{{cite:dodge2008}} (pp. 82–83)

## Properties
Let the class probabilities at a fixed $x$ be non-negative and sum to $1$, and let $k^\star$ attain the maximum. The conditional probability that the Bayes label is wrong is $1-p_{k^\star}(x)$. A rule that instead returns a class $\ell$ is wrong with probability $1-p_\ell(x)$, which is at least as large.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The Bayes label is wrong precisely when the realised class is not $k^\star$. Those alternatives are disjoint and exhaust the complement of $\{k^\star\}$, so their probabilities sum to $1-p_{k^\star}(x)$. For any other announced class $\ell$, the same complement has probability $1-p_\ell(x)$. Because $p_{k^\star}(x)\ge p_\ell(x)$, the second probability is at least the first.{{cite:hastie_esl2009}} (p. 348, (10.20))
:::
:::

At probabilities $7/10$, $1/5$ and $1/10$, the maximum is $7/10$ and the Bayes error is $3/10$. Announcing the class whose probability is $1/5$ has error $4/5$. At probabilities $11/20$ and $9/20$, the Bayes error is $9/20$. The two probabilities in each example sum to $1$, so none of these errors can be removed by a cleverer threshold. They are the overlap of the classes at that $x$.{{cite:hastie_esl2009}} (p. 348, (10.20))

## Statistical use
[Binary logistic regression](binary-logistic-regression.qmd) models the log odds of a binary class and classifies by the estimated probability. [Linear discriminant analysis](linear-discriminant-analysis.qmd) classifies with class means and a shared within-class covariance, which yields linear boundaries. [Nearest neighbours](nearest-neighbours.qmd) classifies by the labels of nearby cases, and a [decision tree](decision-tree.qmd) classifies by a sequence of splits. Logistic regression, linear and quadratic discriminant analysis, naive Bayes, and nearest neighbours are the usual first list of classifiers.{{cite:james_islr2021}} (Ch. 4, p. 129)

The probabilities are often the object of interest, not only the label. A screening rule can report the estimated chance of the event and let a later threshold reflect the cost of a false alarm. Squared error on a coded label is a poor substitute for that chance: it is not a monotone function of how far a case sits on the correct side of the boundary.{{cite:hastie_esl2009}} (pp. 347–348)

The cases used to build the rule are the [training set](training-set.qmd). A low error there does not answer the question asked of a new case. [Cross-validation](cross-validation.qmd) and a held-out sample are the usual ways to estimate that later error.{{cite:james_islr2021}} (Ch. 2, pp. 28–29)

## Worked example
At one feature value the three class probabilities are $7/10$, $1/5$ and $1/10$. They sum to $1$. The largest is $7/10$, so the Bayes classifier returns the first class, and the conditional error is $1-7/10=3/10$. Returning the second class instead has conditional error $1-1/5=4/5$. The gap $4/5-3/10=1/2$ is the extra error from ignoring the ordering of the probabilities.

**Your turn.** Two classes have probabilities $11/20$ and $9/20$. What is the conditional error of the Bayes classifier?

::: {.callout-tip collapse="true" title="Answer"}
The larger probability is $11/20$, so the conditional error is $1-11/20=9/20$.
:::

## Common misconceptions
Grouping unlabelled points into similar bundles is not this problem. That activity is [cluster analysis](cluster-analysis.qmd). A tradition that uses one word for both activities still separates a prediction case, in which the grouping is supposed to support an action, from a description of the groups.{{cite:dodge2008}} (pp. 82–83)

The name logistic regression does not move the binary problem out of classification. The fitted object is a class probability, and the label is read off that probability.{{cite:james_islr2021}} (Ch. 2, pp. 28–29)

A rule that matches every training label can still have conditional error $3/10$ at a new $x$ whose class probabilities are $7/10$, $1/5$ and $1/10$. The training match and the conditional error are answers to different questions.{{cite:hastie_esl2009}} (p. 2; p. 348, (10.20))

## Assumptions and limits
The error formula uses equal costs and a single predicted class. If missing one class is more costly than missing another, the probability ordering is no longer the right ordering. The formula also takes the probabilities as known. A fitted logistic model or a discriminant analysis estimates them, and a good ranking of classes can coexist with badly calibrated probabilities.{{cite:james_islr2021}} (Ch. 4, p. 129) {{cite:hastie_esl2009}} (p. 348)

When the largest probability is $7/10$, every classifier has conditional error at least $3/10$ at that $x$. Collecting a larger sample can improve the estimate of $7/10$. It cannot make the overlap itself disappear.{{cite:hastie_esl2009}} (p. 348, (10.20))

## Connections
Classification is the qualitative half of [supervised learning](supervised-learning.qmd). The quantitative half is regression, as in [simple linear regression](simple-linear-regression.qmd). The [Bayes classifier](bayes-classifier.qmd) is the probability rule above. [Unsupervised learning](unsupervised-learning.qmd) has the features and no class label; [cluster analysis](cluster-analysis.qmd) is the grouping task that is often confused with classification when the labels are absent.{{cite:james_islr2021}} (Ch. 2, pp. 26–29) {{cite:hastie_esl2009}} (pp. 9–10, 485–486)

## History
Predicting a qualitative survival or a rise and fall in a market was approached by linear discriminant analysis in 1936, and by logistic regression in the 1940s. Those two methods, and the later generalised linear model that contains logistic regression, are the classical statistical classifiers. Trees, nearest neighbours, and support vector machines were added once nonlinear fitting became practical.{{cite:james_islr2021}} (Ch. 1, p. 6)

The wider language of grouping similar objects is much older, and its probability-based branch was already called discriminating analysis. The prediction case, as against a mere description of groups, is the line that runs into the qualitative-response problem.{{cite:dodge2008}} (pp. 82–83)
