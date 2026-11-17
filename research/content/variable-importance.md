## Motivating example
A fitted forest predicts flower species well, but a user wants to know whether a particular measurement is necessary for its predictions. Permuting that measurement in held-out observations gives an operational question: how much worse does this fixed predictor perform when the measurement loses its observed relationship with the response and other inputs? The answer depends on the model, observations, loss and permutation scheme.{{cite:breiman2001_rf}} (§10, variable-permutation assessment)

## Definition — Importance is a specified comparison
For a fitted predictor $\hat f$ and assessment sample $(x_i,y_i)$, define
$$\widehat R=\frac1m\sum_{i=1}^m L(y_i,\hat f(x_i)).$$
For a permutation $\pi$ of assessment indices, replace only column $j$ by $x_{\pi(i),j}$ and recompute $\widehat R_j^\pi$. The unscaled permutation importance is $\widehat R_j^\pi-\widehat R$. Repeated shuffles estimate the average of that difference and its variation conditional on the fixed model and sample. Tree-specific out-of-bag comparisons and whole-forest held-out comparisons use related ideas but are different estimators.{{cite:breiman2001_rf}} (§10, out-of-bag permutation procedure)

Impurity importance instead totals weighted decreases in a splitting criterion attributed to a variable. It describes how the tree-growing process used that variable. Predictors offering many possible splits can receive large impurity scores by chance, so such scores are difficult to compare across variables with very different scales or numbers of categories.{{cite:strobl2007}} (sections “Simulation studies” and “Sources of variable importance bias”)

## Properties — Dependence changes the question
Permuting a column independently breaks its association with correlated predictors and can create combinations uncommon in the observed population. An importance score then partly measures how the fitted model behaves on those combinations. A conditional permutation scheme aims at a different comparison by preserving selected predictor relationships. Group permutation can assess a collection of related measurements jointly.

Redundancy also needs careful interpretation. A second copy of a predictor may allow a refitted model to do just as well after deleting the first, but a fixed model that splits on the first copy does not automatically switch its splits to the second during prediction. Therefore marginal permutation importance can be substantial even for a variable that is unnecessary after retraining. Distinguish fixed-model reliance from information available in the full variable set.{{cite:breiman2001_rf}} (§10, dependent-variable example)

The signs are not constrained. Sampling variation or a harmful fitted association can make a shuffle improve observed performance, producing a negative score. A value near zero need not establish that a variable contains no predictive information: the chosen model may fail to use it, another variable may substitute during fitting, or the assessment sample may have low precision.{{cite:strobl2007}} (section “Results and discussion”, null-case permutation importance)

## Worked example — Compute the loss before and after shuffling
Take four assessment responses $y=(0,0,1,1)$ and a fixed classifier $\hat f(x)=1\{x_1>1/2\}$, with first predictor $(0,0,1,1)$. Its baseline misclassification loss is zero. Shuffle that predictor to $(1,0,1,0)$, leaving all other measurements alone. The prediction errors are $(1,0,0,1)$, so the error rate rises to $2/4=0.5$. The unscaled importance for this shuffle is $0.5$.

Across all permutations of the four row indices, every response is paired with a success-valued predictor with probability $1/2$. Expected shuffled error is therefore $1/2$, and expected importance is $0.5$. If a second predictor is an exact duplicate, the fixed classifier's score is unchanged: its formula still uses the first predictor only. A new classifier using the duplicate could recover zero error after the first variable is deleted. This elementary construction exposes why permutation and deletion-and-refitting answer different questions.

**Your turn.** A fixed predictor makes $10$ errors on $100$ held-out cases. After shuffling one column it makes $16$ errors. Compute the absolute increase in error rate and the percentage increase relative to baseline.

::: {.callout-tip collapse="true" title="Answer"}
The absolute increase is $0.16-0.10=0.06$, or six percentage points. The relative increase is $0.06/0.10=0.60$, or $60\%$. Reporting a number without its scaling convention leaves these two quantities ambiguous.
:::

## Statistical use — Make the report reproducible
Name the fitted model, loss, assessment set, number of shuffles, score scaling and treatment of correlated variables. For out-of-bag importance, identify whether errors are averaged per tree or predictions are aggregated across out-of-bag trees before scoring. These choices can produce different values. A ranking can be useful for exploring a predictive model without being a coefficient table or a significance test.{{cite:breiman2001_rf}} (§10, prediction-error comparison and reruns)

For the illustrative error rates $0.12,0.31,0.13$, the absolute increases are $0.19$ and $0.01$. Their relative increases are about $158.3\%$ and $8.3\%$. Impurity scores such as $0.45$ and $0.05$ live on a different scale, so they cannot be equated numerically with either error increase. The scientific role of a variable also needs design information: a predictive association may reflect confounding, measurement practice or a proxy. Shuffling observations is a diagnostic perturbation of inputs, not a physical intervention on the underlying system.{{cite:strobl2007}} (sections “Background” and “Conclusion”)
