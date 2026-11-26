## Lead context
A learning algorithm maps a labelled sample to a prediction rule; the fitted classifier maps a new predictor vector to a label. Classification requires a defined target label and a loss for incorrect predictions.{{cite:goodfellow_bengio_courville2016}} (§5.1.1, p. 97)

## Motivating example
A threshold can label the four training points perfectly and still fail at the next point. Zero apparent error describes those observed pairs. Generalisation asks how the trained rule performs on a fresh pair drawn from the population of interest. A separate test sample estimates that latter quantity when it represents the same target distribution.{{cite:goodfellow_bengio_courville2016}} (§5.2, pp. 107–108)

## Statistical use — Specify what randomness is averaged
Write the random training sample as $D$ and the rule it produces as $g_D$. Under zero–one loss the conditional risk is
$$
R(g_D\mid D)=\mathbb{P}\{g_D(X)\ne Y\mid D\},
$$
where $(X,Y)$ is independent of $D$ and has the target law. The risk of the learning procedure is $\E_D R(g_D\mid D)$. Apparent error instead evaluates $g_D$ on the pairs that determined it. Conditioning on $D$ fixes both the classifier and those pairs, so the apparent-error average cannot generally be treated as independent test observations. Decision trees are one concrete family of rules obtained by recursively partitioning predictor space.{{cite:loh2011_trees}} (p. 14, Introduction)

For a fixed $x$, conditional zero–one risk from choosing class $k$ is $1-\mathbb{P}(Y=k\mid X=x)$. Minimising it chooses a class with largest posterior class probability. This derivation identifies the optimal population rule once those probabilities are known; training is the separate task of estimating a useful rule from finite observations. Classification and probability estimation are therefore related tasks with different outputs.{{cite:goodfellow_bengio_courville2016}} (§5.1.1, pp. 97–99)

## Worked example
Give the five predictor values $(-2,-1,0.1,1,2)$ target probabilities $(0.1,0.1,0.2,0.3,0.3)$ and deterministic labels $(1,1,1,2,2)$. The threshold $g(x)=1$ for $x<0$ and $2$ otherwise errs only at $0.1$, so its population risk is $0.2$. The always-class-$1$ rule errs at $1$ and $2$, giving risk $0.6$. On the four training values $(-2,-1,1,2)$, their apparent errors are $0$ and $0.5$. The training comparison favours the threshold, but neither apparent error equals its target risk.

The population-optimal rule here assigns label $1$ through $0.1$ and label $2$ at $1$ and $2$, obtaining zero risk. The training points alone do not reveal the label at $0.1$. A decision boundary can therefore be underdetermined even when every training label is fitted. Tree boundaries likewise depend on predictor splits selected from the data.{{cite:loh2011_trees}} (§2, pp. 14–15)

**Your turn.** Move the threshold from $0$ to $0.5$, keeping this five-point population. Compute its risk and its apparent error on the four training points.

::: {.callout-tip collapse="true" title="Answer"}
Both are zero: $-2,-1,0.1$ are assigned class $1$, and $1,2$ class $2$. The training error alone could not distinguish the two thresholds.
:::

## Assumptions and limits
Evaluation follows the way the classifier will be used. Repeated measurements from the same person are split by person when the target is a new person. A future population can have different class proportions or a different predictor distribution, and then the risk $R(g_D\mid D)$ is computed under that future law. The fresh-pair calculation assumes the target law and independence from the training sample. The five-point example isolates a finite-sample ambiguity with deterministic labels, so every probability in the risk is a probability on the predictor.{{cite:goodfellow_bengio_courville2016}} (§5.2, test-set generalisation)

## Definition — Separate the procedure from the fitted rule
A learning procedure is a map $D\mapsto g_D$ from labelled samples to prediction rules. A classifier is the fitted rule $x\mapsto g_D(x)$ once $D$ has been observed. The conditional risk $R(g_D\mid D)=\mathbb{P}\{g_D(X)\ne Y\mid D\}$ treats the training sample as fixed and the next pair $(X,Y)$ as a fresh draw. The risk of the procedure averages that conditional risk over training samples. Apparent error averages the zero–one loss on the pairs inside $D$. Because those pairs determined $g_D$, the apparent-error average is a property of the fit, and the fresh-pair probability is a property of the target law.{{cite:goodfellow_bengio_courville2016}} (§5.1.1, p. 97){{cite:goodfellow_bengio_courville2016}} (§5.2, pp. 107–108)

For a fixed predictor value $x$, the conditional probability of an error from predicting class $k$ is $1-\mathbb{P}(Y=k\mid X=x)$. The smallest conditional error chooses a class with maximal posterior probability. That population rule is available when the conditional probabilities are known. Training is the construction of a rule from finitely many labelled pairs, and the gap between the population rule and $g_D$ is what the risk measures.

## Interpretation — Two thresholds can share a training error
On the five-point population with predictor values $(-2,-1,0.1,1,2)$, probabilities $(0.1,0.1,0.2,0.3,0.3)$ and labels $(1,1,1,2,2)$, the threshold at $0$ misclassifies only $0.1$ and has risk $0.2$. The threshold at $0.5$ classifies $(-2,-1,0.1)$ as class $1$ and $(1,2)$ as class $2$, so its risk is $0$. On the four training points $(-2,-1,1,2)$ both thresholds have apparent error $0$. The training comparison cannot see the point $0.1$, which carries probability $0.2$ and is the only place the two rules disagree.

The always-class-$1$ rule has population risk $0.3+0.3=0.6$ and apparent error $0.5$ on those four training points, since it misses the two points labelled $2$. Zero–one risk here is the total probability of the predictor values that the rule labels incorrectly. With deterministic labels that probability is a sum of the listed masses, and a noisy label would replace each mass by the mass times the conditional error probability.

A probability estimator and a classifier can be built from the same fit and still be scored differently. If a model outputs $(0.8,0.2)$ at a point whose label is class $1$, the zero–one classifier that takes the larger coordinate is correct, while a log-loss score still charges $-\log0.8$. The worked comparison uses zero–one loss, so only the final label enters the risk.

## Intuition — The training sample fixes the rule and hides its own points
Once $D$ is observed, $g_D$ is an ordinary function. Its mistakes on new $x$ are ordinary events in the target population. Averaging those events gives $R(g_D\mid D)$. Averaging further over the draw of $D$ gives the risk of the learning procedure, which is the right summary when the scientific question is about the method before a particular sample is in hand. After the sample is in hand, the conditional risk is the summary that matches deployment of this fitted rule.

Apparent error looks smaller in the example because the training points are the ones the threshold was free to fit. The point with probability $0.2$ was held out of training, and that is exactly the point on which the threshold at $0$ fails. Adding that point to the training set would change the apparent-error calculation and could change the selected threshold. The numerical split between the four training values and the five-point population is what makes the two error rates differ.

## Common misconceptions
A training error of zero is compatible with many rules. Both thresholds have apparent error zero and population risks $0.2$ and $0$. The smaller risk belongs to the threshold that matches the label at $0.1$. Selecting the threshold from training error alone leaves both rules tied, so a further choice among zero-training-error rules needs a penalty, a validation sample, or knowledge of the target probabilities.

A small gap between training error and a validation estimate is a comparison of two error rates. Both rates can be large. In this population the constant classifier has risk $0.6$. A validation estimate near $0.6$ would agree with training and would still describe a weak rule. The target risk of the population-optimal classifier is the benchmark: here that optimum has risk $0$, because each listed $x$ has a determined label.{{cite:loh2011_trees}} (§2, pp. 14–15)

## Connections
Decision trees produce classifiers by recursive splits of the predictor space. A split is chosen from the training sample, so the fitted tree is a $g_D$ in the sense above, and its training impurity is an apparent-error calculation on the nodes. Surrogate splits later route a case with a missing predictor; they do not change the definition of the risk, which is still a probability on a fresh pair. Reporting the fresh-pair risk, or an estimate of it from data that did not choose the splits, keeps the fitted tree and the procedure that grew it in their separate roles.{{cite:loh2011_trees}} (p. 14, Introduction){{cite:goodfellow_bengio_courville2016}} (§5.2, test-set generalisation)
