## Lead context
A digit on an envelope, a decision to treat, or a message marked as junk ends as a label. The features that lead to the label are measured; the label itself is one of a finite list. Classification is the statistical problem of using those features to assign the label, and of saying how often a new case will be assigned the wrong one.{{cite:james_islr2021}} (Ch. 4, p. 129) {{cite:hastie_esl2009}} (pp. 21–22, (2.23))

## Motivating example
A mailbox study records, for each message, how often selected words appear, together with the label email or spam. The label is known for the messages already filed. The working rule has to give a label to a message that has not been filed yet. One candidate looks at two frequencies. Another uses a weighted difference of the same two shares and compares it with zero. Both rules are classifiers. They differ in which messages they will mark, and the comparison that matters is the mark on a later message, not the mark on a message that was used to invent the rule.{{cite:hastie_esl2009}} (pp. 21–22) {{cite:james_islr2021}} (Ch. 2, pp. 28–29)

At one feature value the three class probabilities might be \(7/10\), \(1/5\) and \(1/10\). They sum to \(1\). Any rule announced at that value is wrong with the probability of the classes it does not name. The overlap is already in the probabilities. A cleverer threshold cannot remove it.

## Intuition
Given the features, each class has a conditional probability. When every mistake counts the same, the class with the largest probability is the best single guess. The probability of being wrong is then whatever probability is left over. Estimating those probabilities, or estimating a boundary that picks the same class, is the practical problem. A rule that only rearranges the cases already labelled has not yet faced that leftover probability.{{cite:hastie_esl2009}} (pp. 21–22, (2.23)) {{cite:james_islr2021}} (Ch. 2, pp. 28–29)

## Definition
A response is qualitative, or categorical, when it takes values in a finite set of classes. Classification is the task of predicting that response from features. Assigning the predicted class is called classifying the case. Many classifiers first estimate the probability of each class and only then pick a label. In that respect they also behave like regression methods.{{cite:james_islr2021}} (Ch. 4, p. 129)

The naming follows the response, not the features. A quantitative response is a regression problem. A qualitative response is a classification problem. Logistic regression is the usual model for a binary qualitative response: despite the word regression in its name, it is a classification method, because the quantity it models is a class probability. The same method can be read as a regression for that probability. Features may themselves be quantitative or qualitative. After qualitative features are coded, most of the same fitting ideas apply.{{cite:james_islr2021}} (Ch. 2, pp. 28–29)

Write \(G\) for the class and \(p_k(x)=\Pr(G=k\mid X=x)\). A classifier is a map from \(x\) to a class. Under equal misclassification costs the [Bayes classifier](bayes-classifier.qmd) selects
\[
k^\star(x)=\operatorname{argmax}_k p_k(x).
\]
With the \(0\)–\(1\) loss, that choice minimises the conditional expected loss, which is \(1-p_{k^\star}(x)\). Every other class \(\ell\) has conditional expected loss \(1-p_\ell(x)\), which is at least as large, because \(p_{k^\star}(x)\ge p_\ell(x)\).{{cite:hastie_esl2009}} (pp. 21–22, (2.22)–(2.23))

At probabilities \(7/10\), \(1/5\) and \(1/10\), the maximum is \(7/10\) and the Bayes error is \(3/10\). Announcing the class whose probability is \(1/5\) has error \(4/5\). At probabilities \(11/20\) and \(9/20\), the Bayes error is \(9/20\). The probabilities in each example sum to \(1\), so these errors are the overlap of the classes at that \(x\).

A wider traditional use of the same word covers any grouping of similar objects, and it splits that activity into a description of groups and a prediction that leads to an action. The grouping methods that do not use a response are [cluster analysis](cluster-analysis.qmd). The prediction case is the problem above.{{cite:dodge2008}} (pp. 82–83)

## Statistical use
[Binary logistic regression](binary-logistic-regression.qmd) models the log odds of a binary class and classifies by the estimated probability. [Linear discriminant analysis](linear-discriminant-analysis.qmd) classifies with class means and a shared within-class covariance, which yields linear boundaries. [Nearest neighbours](nearest-neighbours.qmd) classifies by the labels of nearby cases, and a [decision tree](decision-tree.qmd) classifies by a sequence of splits. Logistic regression, linear and quadratic discriminant analysis, naive Bayes, and nearest neighbours are the usual first list of classifiers.{{cite:james_islr2021}} (Ch. 4, p. 129)

The probabilities are often the object of interest, not only the label. A screening rule can report the estimated chance of the event and let a later threshold reflect the cost of a false alarm. When one mistake is more costly than another, the probability ordering is no longer the right ordering: the \(0\)–\(1\) loss that produces the Bayes classifier has been replaced. Squared error on a coded label is a poor substitute for the class probability, because a good ranking of classes can coexist with badly calibrated probabilities.{{cite:hastie_esl2009}} (pp. 21–22) {{cite:james_islr2021}} (Ch. 4, p. 129)

The cases used to build the rule are the [training set](training-set.qmd). A low error there does not answer the question asked of a new case. [Cross-validation](cross-validation.qmd) and a held-out sample estimate that later error. When the largest probability is \(7/10\), every classifier has conditional error at least \(3/10\) at that \(x\). A larger sample can improve the estimate of \(7/10\). It cannot make the overlap itself disappear.{{cite:james_islr2021}} (Ch. 2, pp. 28–29) {{cite:hastie_esl2009}} (pp. 21–22, (2.23))

## Worked example
At one feature value the three class probabilities are \(7/10\), \(1/5\) and \(1/10\). They sum to \(1\). The largest is \(7/10\), so the Bayes classifier returns the first class, and the conditional error is \(1-7/10=3/10\). Returning the second class instead has conditional error \(1-1/5=4/5\). The gap \(4/5-3/10=1/2\) is the extra error from ignoring the ordering of the probabilities.

**Your turn.** Two classes have probabilities \(11/20\) and \(9/20\). What is the conditional error of the Bayes classifier?

::: {.callout-tip collapse="true" title="Answer"}
The larger probability is \(11/20\), so the conditional error is \(1-11/20=9/20\).
:::

## Common misconceptions
Grouping unlabelled points into similar bundles is not this problem. That activity is [cluster analysis](cluster-analysis.qmd). A tradition that uses one word for both activities still separates a prediction case, in which the grouping is supposed to support an action, from a description of the groups.{{cite:dodge2008}} (pp. 82–83)

The name logistic regression does not move the binary problem out of classification. The fitted object is a class probability, and the label is read off that probability.{{cite:james_islr2021}} (Ch. 2, pp. 28–29)

A rule that matches every training label can still have conditional error \(3/10\) at a new \(x\) whose class probabilities are \(7/10\), \(1/5\) and \(1/10\). The training match and the conditional error are answers to different questions.{{cite:hastie_esl2009}} (pp. 21–22, (2.23))

Predicting a qualitative survival, or a rise and fall, was approached by linear discriminant analysis and by logistic regression well before trees and nearest neighbours became practical. Those later rules are further classifiers. They do not change the definition: the response is still a class.{{cite:james_islr2021}} (Ch. 4, p. 129)

## Connections
Classification is the qualitative half of [supervised learning](supervised-learning.qmd). The quantitative half is regression, as in [simple linear regression](simple-linear-regression.qmd). The [Bayes classifier](bayes-classifier.qmd) is the probability rule above, and it is the rule that minimises \(0\)–\(1\) conditional risk. [Unsupervised learning](unsupervised-learning.qmd) has the features and no class label. [Cluster analysis](cluster-analysis.qmd) is the grouping task that is often confused with classification when the labels are absent.{{cite:james_islr2021}} (Ch. 2, pp. 26–29) {{cite:hastie_esl2009}} (pp. 21–22) {{cite:dodge2008}} (pp. 82–83)

The wider language of grouping similar objects is much older than the qualitative-response problem, and its probability-based branch was already called discriminating analysis. The prediction case, as against a mere description of groups, is the line that runs into the qualitative-response problem: a finite label, features, and an error that is the probability left over after the best label.{{cite:dodge2008}} (pp. 82–83)
