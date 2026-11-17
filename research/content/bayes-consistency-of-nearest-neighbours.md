## Motivating example
A nearest-neighbour classifier uses nearby labels to estimate the class probabilities at a query. With one neighbour, a noisy label remains noisy even when that neighbour is very close. With a fixed positive fraction of the whole sample, many labels are averaged but the neighbourhood may remain too broad. Consistency balances these effects by increasing the number of neighbours while shrinking the fraction of the sample used.{{cite:cerou_guyader2006}} (§1, pp. 341–342)

## Statement
For independent identically distributed training pairs in a fixed-dimensional Euclidean space, standard $k_n$-nearest-neighbour classification is weakly universally consistent when $k_n\to\infty$ and $k_n/n\to0$, with an appropriate label-independent distance-tie rule. Weak consistency means that the expected future error, averaged over training samples, tends to the Bayes error. Universality means that the result holds for every underlying joint distribution within the stated setting. It is not a uniform finite-sample convergence rate over those distributions.{{cite:cerou_guyader2006}} (§1, p. 342, weak consistency)

The metric is part of the hypothesis. Merely counting a fixed number of coordinates while using an arbitrary pathological distance does not preserve the Euclidean conclusion. General metric spaces need additional conditions. A theorem about fixed dimension also does not automatically cover a feature dimension that grows with sample size.{{cite:cerou_guyader2006}} (§2.1, pathological distance; §2.2, Besicovitch condition)

## Key results — Turn probability estimation into classification
In binary classification, write $\eta(x)=\Pr(Y=1\mid X=x)$, and classify as one when an estimate $\widehat\eta(x)$ is at least $1/2$. If the estimated rule disagrees with a Bayes rule, the threshold $1/2$ lies between $\eta$ and $\widehat\eta$. The conditional excess error is then $|2\eta-1|\le2|\eta-\widehat\eta|$. Integrating proves the plug-in bound
$$0\le E\{R(\widehat g)\}-R^*\le2E|\widehat\eta(X)-\eta(X)|.$$
This shows why consistency of the local class-probability estimate is sufficient for Bayes-risk consistency. The geometric part of the nearest-neighbour theorem establishes the needed probability-estimation behaviour under the sample-size conditions.{{cite:cerou_guyader2006}} (§1, p. 341, excess-risk bound)

## Proof
The preceding excess-error inequality follows pointwise by considering whether the two classification decisions agree. If they agree the excess is zero. If they disagree, their decisions are on opposite sides of $1/2$, so $|\eta-1/2|\le|\eta-\widehat\eta|$. Multiplying by two and averaging gives the displayed bound. For a feature space consisting of finitely many distinct points of positive mass, the strong law makes the number of training observations at each point grow proportionally to $n$. Eventually there are more than $k_n$ exact matches, and the average of their independent labels estimates the conditional class probability because $k_n\to\infty$. The bounded excess-error identity then gives risk convergence for that finite setting. The full Euclidean result additionally needs a geometric locality argument.{{cite:cerou_guyader2006}} (§1, pp. 341–342, risk bound and consistency)

## Worked example
### No features, only label noise
Suppose every feature vector is identical and labels are independent Bernoulli with success probability $0.7$. The Bayes classifier always predicts one and has error $0.3$. A one-neighbour classifier copies an independent training label, giving error $2(0.7)(0.3)=0.42$. For three neighbours, the probability that the majority is one is $\binom32(0.7)^2(0.3)+(0.7)^3=0.784$. Its test error is $0.7(1-0.784)+0.3(0.784)=0.3864$. Increasing an odd neighbour count makes the majority increasingly reliable and drives error towards $0.3$. This isolates voting noise without a spatial approximation problem.{{cite:grinstead_snell1997}} (§5.1, binomial distribution; §8.1, law of large numbers)

**Your turn.** Is the constant choice $k_n=3$ enough to satisfy the theorem's two sample-size conditions?

::: {.callout-tip collapse="true" title="Answer"}
No. Although $3/n$ tends to zero, the neighbour count does not tend to infinity. The worked example shows the resulting persistent voting noise.
:::

## Common misconceptions — Asymptotic success is not a tuning prescription
A choice such as an odd integer near $\sqrt n$ satisfies the two growth conditions, but the theorem does not identify the best finite-sample choice. Feature scaling, irrelevant coordinates, computation and validation still matter for actual data. A finite sample with a small ratio $k/n$ is only one point on a sequence; it does not establish the sequence's limiting behaviour.{{cite:cerou_guyader2006}} (§§1–2)


## Statistical use — Tune finite-sample rules with a separate assessment
The consistency conditions identify permissible limiting sequences rather than an optimal neighbour count for a particular dataset. A validation set can compare candidate counts and feature scalings, followed by a separate test set for the chosen rule. Repeatedly inspecting the final test score while tuning makes that score part of the selection process. Report the fitted rule's assessment separately from the asymptotic theorem that motivated the family of rules.{{cite:goodfellow_bengio_courville2016}} (§5.3, hyperparameters and validation sets)

## Intuition
A nearest-neighbour vote is a local average of labels. Two errors pull that average away from the conditional class probability $\eta(x)$. The first is voting noise: even at the true $x$, a finite number of labels fluctuates. The second is location noise: the neighbours are not quite at $x$, so they carry $\eta$ at nearby points rather than at the query. The condition $k_n\to\infty$ averages away the voting noise. The condition $k_n/n\to 0$ forces the neighbourhood to shrink, so the neighbours eventually sit where $\eta$ is close to its value at the query, under the regularity the Euclidean argument uses.

One neighbour satisfies only the second condition. In the worked example every feature vector is the same point, so location noise is absent and voting noise is the whole problem. The Bayes rule predicts class one and has error $0.3$. Copying a single independent label has error $2\cdot 0.7\cdot 0.3=0.42$. Three neighbours reduce the error to $0.3864$ and still do not satisfy $k_n\to\infty$. A fixed neighbour count, however large, leaves a fixed amount of voting noise. The theorem asks the count to grow.

### Key results — The plug-in bound is an inequality, not a rate
If a classifier predicts class one when $\widehat\eta(x)\ge 1/2$, and a Bayes rule predicts class one when $\eta(x)\ge 1/2$, the two rules disagree only when $1/2$ lies between $\eta(x)$ and $\widehat\eta(x)$. On that event the conditional excess error equals $|2\eta(x)-1|$, and that quantity is at most $2|\eta(x)-\widehat\eta(x)|$. Integrating gives
$$0\le E\{R(\widehat g)\}-R^*\le 2E|\widehat\eta(X)-\eta(X)|.$$
At a point where $\eta=0.9$ and $\widehat\eta=0.3$, the decisions disagree. The conditional excess error is $|1.8-1|=0.8$, and the bound $2|0.9-0.3|=1.2$ sits above it. Where the two decisions agree, the excess error is zero even if $\widehat\eta$ is not exactly $\eta$. The factor $2$ is therefore a uniform majorant, not the excess error at every $x$.

The finite-point argument in the proof is the case in which location noise eventually disappears for a simpler reason. If the feature space is a finite set of atoms, the strong law puts more than $k_n$ training points on each atom once $n$ is large, because $k_n/n\to 0$ keeps the neighbour count below the count of exact matches. The vote is then a binomial average of $k_n$ fresh labels from $\eta$ at that atom, and $k_n\to\infty$ makes the average consistent. The Euclidean theorem extends the same excess-risk bound to a continuous feature space by showing that the neighbours still concentrate.{{cite:cerou_guyader2006}} (§1, pp. 341–342, risk bound and consistency)

### Common misconceptions
The pair of limit conditions is not a formula for the best $k$ at a given $n$. An odd integer near $\sqrt n$ satisfies both conditions along the sequence, and so does $\log n$ once $n$ is large enough that $\log n\ge 1$. The theorem is silent about which sequence has smaller finite-sample risk. Irrelevant coordinates make the Euclidean neighbourhood large in the original units even when $k/n$ is small, because distance is dominated by the noise coordinates. Standardising features, or discarding coordinates, changes the metric. The theorem's Euclidean hypothesis has to be read in the coordinates the algorithm actually uses.

A single sample with $k=5$ and $n=500$ has a small ratio $k/n$. That one ratio is not a sequence tending to zero, and it does not prove that the classifier's risk is close to the Bayes risk. Consistency is a statement about a sequence of experiments. A validation estimate of risk is a statement about one experiment. Both can be reported. The validation number is the one that refers to the fitted rule.{{cite:cerou_guyader2006}} (§§1–2)

## Related concepts
The cover–Hart calculation for one neighbour is the boundary the growing-$k$ theorem leaves behind. With $k=1$ the asymptotic error can be as large as $2R^*(1-R^*)$, which exceeds the Bayes risk whenever $0<R^*<1/2$. Growing $k$ is what removes that extra factor, at the price of a neighbourhood that must still shrink. Kernel classifiers and local polynomial regressions make the same bias–variance compromise with a bandwidth instead of a neighbour count. The $k_n$ conditions are the nearest-neighbour form of that compromise. They do not choose the loss, the metric, or the feature map. A change in any of those ingredients needs its own argument.
