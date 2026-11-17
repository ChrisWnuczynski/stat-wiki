## Lead context

A digit on a cheque, a cell on a slide, and a customer who will or will not default are presented to the statistician as vectors of features. The task is to assign the vector to a class, or to describe the kinds of vectors that occur. Pattern recognition is that task. The name is shared with engineering and with machine learning. In statistics it means a probability model for the features and a rule that turns the model into a decision.

## Definition — Scope

Pattern recognition is the construction of rules that assign observations to classes, or that describe the structure of observations when no class is given. In the statistical-learning vocabulary the inputs are called features, the word the pattern-recognition literature prefers for what regression calls predictors. A classifier is a function $G(x)$ taking values in a finite set of classes. It partitions the feature space into regions, one label to each region. The boundaries may be linear or irregular. When no label is observed, the problem is unsupervised: the features are still there, and the response that would have defined a class is not.{{cite:hastie_esl2009}} (Ch. 2, §2.2, p. 9; Ch. 4, §4.1, p. 101){{cite:james_islr2021}} (Ch. 2, p. 26)

The scope includes images, signals, and ordinary tabular measurements. It does not include every regression. A mean income predicted from age is not a pattern-recognition problem unless the scientific object is a class or a discovered grouping. Clustering, discriminant analysis, and neural classifiers are inside the scope. A national account is not.

## Statistical use

The reference rule is the [Bayes classifier](bayes-classifier.qmd), which assigns the class with the highest posterior probability given the features. [Linear discriminant analysis](linear-discriminant-analysis.qmd) and [quadratic discriminant analysis](quadratic-discriminant-analysis.qmd) are the versions of that rule when the features are normal with shared or separate covariances. [Nearest neighbours](nearest-neighbours.qmd) estimates the class locally, without a global linear boundary. [Decision trees](decision-tree.qmd) and [random forests](random-forest.qmd) cut the feature space into rectangles. A [perceptron](perceptron.qmd) and a [kernel support vector machine](kernel-support-vector-machine.qmd) are further ways to state a boundary. Unsupervised companions are [principal component directions](principal-component-directions.qmd) and clustering, used when the goal is to describe the feature distribution rather than to name a class. Error rates belong on data that were not used to build the rule.{{cite:hastie_esl2009}} (Ch. 4, §4.1, p. 101){{cite:james_islr2021}} (Ch. 2, p. 26)

Features are a choice. Two measurements that are rearrangements of each other can make a linear rule succeed or fail. The statistical problem starts after that choice and includes the uncertainty of the resulting error rate.{{cite:hastie_esl2009}} (Ch. 2, §2.2, p. 9)

## History

Discriminant methods and early neural rules grew up as ways to automate classification that a specialist could do by eye: species, letters, military targets. The statistical-learning synthesis of the last two decades treats those rules as one catalogue, with a common language of features, losses, and test error. Textbooks written for that synthesis cite the pattern-recognition literature as a parallel vocabulary rather than as a rival subject. The practical change was computational. A support-vector machine or a forest can be fit to feature vectors that no linear discriminant of the 1930s was asked to handle, and the evaluation standard is still a predictive error, not a significant coefficient.{{cite:hastie_esl2009}} (Ch. 2, §2.2, p. 9; Ch. 4, §4.1, p. 101){{cite:james_islr2021}} (Ch. 2, p. 26)

## Connections

Pattern recognition is the classification face of [multivariate statistics](multivariate-statistics.qmd). It shares latent-variable models with [factor analysis](factor-analysis.qmd) when the features are treated as noisy views of a smaller set of causes. A rule with a tiny training error and a large test error has fit the sample, not the pattern. [Cross-validation](cross-validation.qmd) is the usual check. The Bayes rule is optimal for a known distribution and is not what is computed from a finite sample. Reporting the training accuracy as if it were that optimum is the mistake the held-out evaluation exists to prevent.{{cite:james_islr2021}} (Ch. 2, p. 26){{cite:hastie_esl2009}} (Ch. 4, §4.1, p. 101)
