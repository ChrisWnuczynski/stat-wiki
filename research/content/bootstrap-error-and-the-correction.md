## Motivating example
A classifier can memorise its training labels and attain zero apparent error while predicting fresh labels poorly. Bootstrap error estimation repeatedly refits the learning procedure and evaluates an observation using only refits whose resampled training set omitted that observation. The $.632$ correction combines this error with the apparent error to address their competing biases.{{cite:efron_tibshirani1997_632plus}} (§§2–3, pp. 549–552)

## Definition — Casewise out-of-bag error and the blend
Draw $B$ bootstrap samples of size $n$ with replacement from the training cases, and refit the complete specified learning procedure in each sample. Let $C_{-i}$ index replicates omitting case $i$. With loss $Q$ and fitted rule $\eta_b$,
$$
\widehat{\mathrm{Err}}_{\rm oob}=
\frac1n\sum_i\frac1{|C_{-i}|}\sum_{b\in C_{-i}}Q(y_i,\eta_b(x_i)),
\qquad
\widehat{\mathrm{Err}}_{.632}=0.368\,\mathrm{err}+0.632\,\widehat{\mathrm{Err}}_{\rm oob}.
$$
Every case needs at least one omitted-case replicate for this finite-$B$ formula. Averaging its losses first and then averaging cases prevents heavily evaluated cases from receiving unintended extra weight. The paper also discusses a pooled alternative whose infinite-replication limit agrees.{{cite:efron1983}} (§6, pp. 321–322){{cite:efron_tibshirani1997_632plus}} (§2, p. 550)

## Properties — Inclusion probabilities are exact; error correction is approximate
A particular case is missed on one draw with probability $1-1/n$, so it is omitted from an entire bootstrap sample with probability $(1-1/n)^n$. Linearity of expectation gives expected distinct sample size $n\{1-(1-1/n)^n\}$. The limiting fraction is $1-e^{-1}\approx0.63212$. The labels $.368$ and $.632$ are conventional rounded limiting weights. Replacing them by finite-sample inclusion probabilities does not by itself establish an unbiased error estimate.{{cite:efron1983}} (§6, pp. 321–322)

Apparent error can be optimistic because fitting and evaluation reuse outcomes. Omitted-case bootstrap rules often have higher error because their resamples contain fewer distinct training observations. That is a training-size argument, rather than a universal ordering for every learner or every dataset. The $.632$ blend is an error-estimation method with finite-sample limitations.{{cite:efron_tibshirani1997_632plus}} (§§2–3, pp. 551–552)

## Worked example — A useful blend and a memorisation failure
With apparent error $0.10$ and omitted-case error $0.25$, the $.632$ estimate is $0.368(0.10)+0.632(0.25)=0.1948$. For $n=10$, expected distinct training size is $10(1-0.9^{10})=6.51322$, while a fixed case is omitted with probability $0.348678$. With $B=200$ independent resamples it has $69.7357$ omitted-case evaluations on average.{{cite:efron1983}} (§6, pp. 321–322)

Now suppose binary labels are independent fair coin flips and features carry no information. A rule that memorises training labels has apparent error zero, while a fresh label has mismatch probability $1/2$. An omitted-case estimate near $0.5$ gives the blend $0.632(0.5)=0.316$, below the actual $0.5$ error. This explains the need for methods such as $.632+$ that adapt their weight to severe overfitting. The fixed blend does not remove all optimism.{{cite:efron_tibshirani1997_632plus}} (§3, p. 552)

**Your turn.** If apparent and omitted-case errors both equal $0.2$, what does the $.632$ estimate equal? Does that equality prove that true error is $0.2$?

::: {.callout-tip collapse="true" title="Answer"}
It equals $(0.368+0.632)0.2=0.2$. Agreement of two estimates is not knowledge of the unknown future error; sampling and model-selection uncertainty remain.
:::

## Check yourself
### Evaluate the conventional weights {#self-check-ex-sl-09-3}
[The $0.632$ rule](../questions/ex-sl-09-3.qmd) separates finite-$n$ inclusion from its limit.

::: {.callout-tip collapse="true" title="Answer"}
The inclusion probabilities are $1-0.8^5=0.67232$ and $1-0.95^{20}=0.641514$. Their limit is $1-e^{-1}$. Blending apparent error $0.05$ with omitted-case error $0.20$ gives $0.1448$.
:::

### Evaluate the whole tuning procedure {#self-check-ex-sl-09-6}
[The winning cross-validation score is optimistic](../questions/ex-sl-09-6.qmd) asks why the winning tuning score is optimistic.

::: {.callout-tip collapse="true" title="Answer"}
Selecting the smallest score also selects favourable evaluation noise. An outer held-out fold must be excluded from fitting and tuning. Repeat the inner selection within each outer training set, then evaluate the resulting procedure on the outer fold.
:::
