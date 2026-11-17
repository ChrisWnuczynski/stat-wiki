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
