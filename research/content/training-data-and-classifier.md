## Lead context
A learning algorithm maps a labelled sample to a prediction rule; the fitted classifier maps a new predictor vector to a label. Classification requires a defined target label and a loss for incorrect predictions.{{cite:goodfellow_bengio_courville2016}} (§5.1.1, p. 97)

## Motivating example
A threshold can label the four training points perfectly and still fail at the next point. Zero apparent error describes those observed pairs. Generalisation asks how the trained rule performs on a fresh pair drawn from the population of interest. A separate test sample estimates that latter quantity when it represents the same target distribution.{{cite:goodfellow_bengio_courville2016}} (§5.2, pp. 107–108)

## Statistical use — Specify what randomness is averaged
Write the random training sample as $D$ and the rule it produces as $g_D$. Under zero–one loss the conditional risk is
$$
R(g_D\mid D)=P\{g_D(X)\ne Y\mid D\},
$$
where $(X,Y)$ is independent of $D$ and has the target law. The risk of the learning procedure is $E_D R(g_D\mid D)$. Apparent error instead evaluates $g_D$ on the pairs that determined it. Conditioning on $D$ fixes both the classifier and those pairs, so the apparent-error average cannot generally be treated as independent test observations. Decision trees are one concrete family of rules obtained by recursively partitioning predictor space.{{cite:loh2011_trees}} (p. 14, Introduction)

For a fixed $x$, conditional zero–one risk from choosing class $k$ is $1-P(Y=k\mid X=x)$. Minimising it chooses a class with largest posterior class probability. This derivation identifies the optimal population rule once those probabilities are known; training is the separate task of estimating a useful rule from finite observations. Classification and probability estimation are therefore related tasks with different outputs.{{cite:goodfellow_bengio_courville2016}} (§5.1.1, pp. 97–99)

## Worked example
Give the five predictor values $(-2,-1,0.1,1,2)$ target probabilities $(0.1,0.1,0.2,0.3,0.3)$ and deterministic labels $(1,1,1,2,2)$. The threshold $g(x)=1$ for $x<0$ and $2$ otherwise errs only at $0.1$, so its population risk is $0.2$. The always-class-$1$ rule errs at $1$ and $2$, giving risk $0.6$. On the four training values $(-2,-1,1,2)$, their apparent errors are $0$ and $0.5$. The training comparison favours the threshold, but neither apparent error equals its target risk.

The population-optimal rule here assigns label $1$ through $0.1$ and label $2$ at $1$ and $2$, obtaining zero risk. The training points alone do not reveal the label at $0.1$. A decision boundary can therefore be underdetermined even when every training label is fitted. Tree boundaries likewise depend on predictor splits selected from the data.{{cite:loh2011_trees}} (§2, pp. 14–15)

**Your turn.** Move the threshold from $0$ to $0.5$, keeping this five-point population. Compute its risk and its apparent error on the four training points.

::: {.callout-tip collapse="true" title="Answer"}
Both are zero: $-2,-1,0.1$ are assigned class $1$, and $1,2$ class $2$. The training error alone could not distinguish the two thresholds.
:::

## Assumptions and limits
Evaluation must reflect how the classifier will be used. Repeated measurements from the same person may need splitting by person; a future population can have different class proportions or predictor distributions. The iid fresh-pair calculation explicitly assumes the target law and independence from training. The numerical example isolates finite-sample ambiguity without needing noisy class labels.{{cite:goodfellow_bengio_courville2016}} (§5.2, test-set generalisation)
