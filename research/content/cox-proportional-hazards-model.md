## Lead context

The Cox proportional hazards model is a regression model for a time to an event — death, relapse, failure of a machine, publication of a study — in which covariates multiply an unspecified baseline hazard. Its central device is not the model itself but the way it is fitted: the partial likelihood. That device estimates the covariate coefficients without ever specifying, or estimating, the baseline hazard function. The model is semiparametric because it combines a finite-dimensional coefficient vector with an unrestricted baseline hazard function.

Estimation proceeds through event-time risk sets. Partial likelihood estimates $\beta$, tie methods specify how simultaneous failures contribute, and a separate step estimates the baseline cumulative hazard. Proportionality must then be assessed because a constant coefficient does not ensure that the observed association is constant over time.

## Motivating example — A coefficient that survives without a baseline

The BrainCancer data analysed by James, Witten, Hastie and Tibshirani contain $88$ patients: $45$ women and $43$ men, with $35$ observed deaths and $53$ censored observations. The sex-only Cox fit has a coefficient of $0.4077$ for men relative to women, a hazard ratio of $1.5033$, and a Wald $p$-value of $0.233$; it provides no clear evidence of a difference after making no adjustment for other covariates {{cite:james_islr2021}} (§11.8.1, pp. 483–484). This is distinct from the multivariable analysis in §11.5.3. For one binary group covariate with no additional adjustment, the Cox score test at the null agrees with the ordinary log-rank statistic when there are no tied events. With ties, the exact conditional partial likelihood retains this agreement for the same risk sets and event/censoring conventions; Breslow's and Efron's approximations need not do so {{cite:cox1972}} (§§6–7, pp. 192–193).

The estimated coefficient compares the sexes without specifying how the reference hazard changes over months since diagnosis. Cox's conditional-likelihood construction removes the common baseline hazard from each event-time comparison {{cite:cox1972}} (§5, pp. 190–191).

## Definition — The model this article fits

Let $T$ be the event time, let $x$ be a vector of $p$ covariates measured for a subject, let $\beta$ be a vector of $p$ unknown coefficients, and let $h_0(t)$ be an unspecified non-negative function of time $t$, the baseline hazard. The Cox model states that the hazard for a subject with covariates $x$ is

$$h(t \mid x) = h_0(t) \exp(x^T \beta).$$

The hazard $h(t \mid x)$ is the instantaneous event rate at time $t$ among subjects who have survived event-free up to $t$ with covariates $x$. The ratio of hazards for two subjects with covariates $x_1$ and $x_2$ is $\exp((x_1 - x_2)^T \beta)$, which does not depend on $t$: that time-independence is the proportional-hazards assumption. There is no intercept in $\beta$, because any constant factor in $\exp(x^T \beta)$ would be absorbed into the unspecified $h_0(t)$. For the definition, the hazard-ratio interpretation and the implied survival function, see [proportional-hazards-model](proportional-hazards-model.qmd).

## Properties — Estimation by partial likelihood

### The data and the risk set

Suppose $n$ subjects are observed. For subject $i$, let $y_i$ be the observed time — the event time if the event was observed, the censoring time otherwise — let $\delta_i = 1$ if the event was observed for subject $i$ and $\delta_i = 0$ if subject $i$ was censored, and let $x_i$ be the covariate vector. Assume independent subjects and censoring independent of the event process conditional on the modelled covariates. This makes the observed risk sets suitable for estimating the event-hazard ratios; censoring associated with unmodelled prognosis can invalidate those comparisons.

For any time $t$, the **risk set** $R(t)$ is the set of subjects still under observation and event-free just before $t$:

$$R(t) = \{j : y_j \ge t\}.$$

A subject censored at time $c$ belongs to $R(t)$ for every $t \le c$ and to none afterwards. It contributes no factor of its own to the partial likelihood below, but it appears in the denominators of the factors at event times before its censoring, where it constrains the comparison.

### Why the baseline cancels

Fix an event time $t$, and suppose exactly one event occurs at $t$, for subject $i$. Given that one event occurred at $t$ among the subjects in $R(t)$, the probability under the model that it was subject $i$ rather than any other subject in the risk set is the ratio of subject $i$'s hazard to the sum of the hazards in the risk set:

$$\frac{h_0(t) \exp(x_i^T \beta)}{\sum_{j \in R(t)} h_0(t) \exp(x_j^T \beta)} = \frac{\exp(x_i^T \beta)}{\sum_{j \in R(t)} \exp(x_j^T \beta)}.$$

The baseline hazard $h_0(t)$ is a common factor of numerator and denominator, so it cancels exactly. By conditioning on the occurrence of an event and comparing which subject experienced it, the nuisance function $h_0$ disappears from the estimating problem {{cite:cox1972}} (§5, pp. 190–191).

### The partial likelihood, the score, and the estimate

Multiplying the conditional probabilities above over all observed event times gives the **partial likelihood**

$$L(\beta) = \prod_{i : \delta_i = 1} \frac{\exp(x_i^T \beta)}{\sum_{j \in R(y_i)} \exp(x_j^T \beta)}.$$

Its logarithm, the partial log-likelihood, is

$$\ell(\beta) = \sum_{i : \delta_i = 1} \left[ x_i^T \beta - \log \sum_{j \in R(y_i)} \exp(x_j^T \beta) \right].$$

Three consequences follow immediately, and each is worth stating exactly.

First, $L(\beta)$ depends only on the *order* of the event times, through the risk sets, and not on the gaps between them. Stretching or compressing the time axis by any increasing transformation leaves every risk set unchanged and therefore leaves $L(\beta)$ unchanged.

Second, $L(\beta)$ is called a *partial* likelihood because it is not the probability of the observed data: the factors condition on overlapping events, and the information about the spacing of event times — the information that would identify $h_0$ — has been deliberately discarded. It is nevertheless used as if it were a likelihood: the maximum partial likelihood estimator $\hat{\beta}$ maximises $\ell(\beta)$, and its standard errors and tests are obtained from the curvature of $\ell(\beta)$, as for an ordinary likelihood. That use was contested when Cox's paper was read, and its justification was worked out in later theory; in practice the analogy is treated as sound under the usual regularity conditions, including enough events and no separation.

Third, differentiating $\ell(\beta)$ gives the **score** equation that $\hat{\beta}$ solves. For the $k$th component of $\beta$,

$$\frac{\partial \ell(\beta)}{\partial \beta_k} = \sum_{i : \delta_i = 1} \left[ x_{ik} - \bar{x}_k(\beta, y_i) \right] = 0,$$

where $\bar{x}(\beta, t)$ is the risk-set average of the covariates, weighted by $\exp(x_j^T \beta)$:

$$\bar{x}(\beta, t) = \frac{\sum_{j \in R(t)} x_j \exp(x_j^T \beta)}{\sum_{j \in R(t)} \exp(x_j^T \beta)}.$$

In words, at each event time the score compares the covariate of the subject who actually had the event with the average covariate among those who could have had it, where the average is weighted by relative risk. The estimator $\hat{\beta}$ is the value that makes these comparisons balance out — sum to zero — over all event times. The negative second derivative of $\ell(\beta)$, the observed information, is the sum over event times of the risk-set variance of $x$ under the same weights, and its inverse gives the approximate variance of $\hat{\beta}$. There is, in general, no closed form for $\hat{\beta}$; it is found numerically, usually by Newton–Raphson iteration.

For one binary group covariate with no additional adjustment, the score at $\beta = 0$ is the observed-minus-expected event count used by the ordinary log-rank test. With no ties, its information is the log-rank variance. With ties, this equality still holds for the exact conditional tied partial likelihood: at the null, every subset of the observed number of failures from the risk set is equally likely, so the group event count is hypergeometric {{cite:cox1972}} (§§6–7, pp. 192–193). Its mean and variance supply the score and information. The equality requires the same risk sets, tied event counts, and event/censoring conventions in both analyses; it does not extend in general to adjusted Cox tests or to approximate tie handling.

For example, suppose $2$ subjects are at risk in each group and $2$ events occur together, both in group $1$. Of the six possible failing pairs, one contains no group-$1$ subject, four contain one, and one contains two. Thus the null expected group-$1$ count is $1$ and its variance is $1/3$. Both the exact conditional Cox test and the ordinary log-rank test have score $2-1=1$ and information $1/3$. Breslow's approximation instead gives information $2(1/2)(1/2)=1/2$. The resulting score statistics are $3$ and $2$, respectively. Here “exact” describes the conditional likelihood and its derivatives; the usual chi-squared reference distribution for the accumulated score statistic remains asymptotic.

### Ties — When two events share a time

The partial likelihood above assumes no ties: exactly one event at each event time. For independent event times with continuous distributions, ties have probability zero, but recorded times are rounded — to days, weeks or months — and genuinely discrete times occur, so ties are common in practice. When $d$ events occur at the same time $t$, the order in which they occurred is unknown, and the partial likelihood must be modified. Let $D(t)$ be the set of the $d$ subjects with events at $t$, let $R(t)$ be the risk set just before $t$, and write $w_j = \exp(x_j^T \beta)$ for the relative-risk weight of subject $j$. All three standard methods use the same numerator, $\prod_{j \in D(t)} w_j$; they differ in the denominator.

**Breslow's approximation.** Breslow's method uses the full risk-set sum for each of the $d$ tied events:

$$L_B(t) = \frac{\prod_{j \in D(t)} w_j}{\left( \sum_{j \in R(t)} w_j \right)^d}.$$

It is as if the $d$ events were distinct and each faced the same, unreduced risk set. It is simple, it is the default in several packages, and it works best when the number of ties is small {{cite:rocke2021}} (slides 11–12).

**Efron's approximation.** Efron's method reduces the denominator in fractional steps, as if the tied events were removed from the risk set one at a time but in unknown order. With $S = \sum_{j \in R(t)} w_j$ and $E = \sum_{j \in D(t)} w_j$,

$$L_E(t) = \frac{\prod_{j \in D(t)} w_j}{\prod_{r=0}^{d-1} \left( S - \frac{r}{d} E \right)}.$$

The first factor uses the full risk set; the last subtracts a fraction $(d-1)/d$ of the event-set weight. This approximates gradual removal of the tied failing subjects from the denominator. Efron's method is the default in R's `coxph` {{cite:rocke2021}} (slides 11–12).

**The exact conditional partial likelihood.** Let $\mathcal{A}_d(R(t))$ be the collection of all subsets of size $d$ from $R(t)$. The contribution is

$$L_X(t)=\frac{\prod_{j\in D(t)}w_j}{\sum_{A\in\mathcal{A}_d(R(t))}\prod_{j\in A}w_j}.$$

This conditions on the number of events and compares possible failing subsets, not possible orders within the observed failing subset. Cox derived it for a discrete-time model with proportional odds of failure at each time {{cite:cox1972}} (§6, p. 192). It is therefore distinct from averaging continuous-time likelihoods over unknown failure orders. At $\beta=0$ every subset has equal weight; with a binary group indicator this gives the hypergeometric score and information described above. Enumerating all subsets can be expensive when both the risk set and the tied event count are large.

When there are no ties, $d = 1$ and all three methods agree exactly. When ties are few, Breslow and Efron usually give very similar estimates; when a large share of the events are tied, or when risk sets are small, the estimates and standard errors can differ enough to matter, and the choice should be reported. A small numerical comparison is given in Check yourself, question 2.

### Baseline hazard — Breslow's estimator

The partial likelihood estimates $\beta$ but says nothing about $h_0$. If absolute survival probabilities are needed — a predicted survival curve for a patient with given covariates — the baseline hazard must be estimated afterwards, with $\hat{\beta}$ treated as known. The standard estimator is Breslow's estimator of the cumulative baseline hazard $H_0(t) = \int_0^t h_0(u) \, du$.

At each distinct event time $t_i$, let $d_i$ be the number of events at $t_i$ and let $R(t_i)$ be the risk set just before $t_i$. Breslow's estimator is the step function

$$\hat{H}_0(t) = \sum_{t_i \le t} \frac{d_i}{\sum_{j \in R(t_i)} \exp(x_j^T \hat{\beta})}.$$

Each increment is the number of events at that time divided by the total relative risk of the subjects at risk — as if each subject at risk counted not once but $\exp(x_j^T \hat{\beta})$ times. With no covariates, $\hat{\beta} = 0$, every weight is $1$, and the estimator reduces to the Nelson–Aalen estimator, $\sum_{t_i \le t} d_i / n_i$, where $n_i$ is the number at risk {{cite:rocke2021}} (slide 8).

That reduction is to Nelson–Aalen, not to Kaplan–Meier, and a one-event contrast shows why the distinction matters. With one event and two subjects at risk, the Nelson–Aalen increment is $1/2$, so the estimated baseline survival obtained by exponentiating it is $\exp(-1/2) \approx 0.6065$, whereas the Kaplan–Meier factor for the same event is $1 - 1/2 = 0.5$. Exponentiating the Nelson–Aalen estimator is not the product-limit estimator.

The estimated survival function for a subject with covariates $x$ is then

$$\hat{S}(t \mid x) = \exp\left( -\hat{H}_0(t) \exp(x^T \hat{\beta}) \right).$$

Two cautions belong here. First, $\hat{H}_0(t)$ is a step function that jumps only at observed event times; it is not a smooth estimate of $h_0(t)$ itself, and differentiating it to obtain a baseline hazard is not meaningful without further smoothing. Second, the uncertainty in $\hat{S}(t \mid x)$ has two sources — the uncertainty in $\hat{\beta}$ and the uncertainty in $\hat{H}_0$ — and a confidence interval that ignores either is too narrow.

## Interpretation — Checking the proportional-hazards assumption

The proportional-hazards assumption — that every hazard ratio is constant over time — is an assumption about the model, not a consequence of the data, and a fitted Cox model does not check it by itself. Two diagnostics are standard, and they check the assumption in complementary ways.

### Schoenfeld residuals

At an untied event time $t_i$, for the subject who had the event, the **Schoenfeld residual** is the difference between that subject's covariate and the risk-set average of the covariate at $t_i$, where the average is the same weighted average $\bar{x}(\hat{\beta}, t_i)$ that appears in the score equation:

$$r_i = x_i - \bar{x}(\hat{\beta}, t_i).$$

In this untied construction there is one such residual per observed event and per covariate; censored subjects have no Schoenfeld residual, because no event was observed for them. The residuals are the individual contributions to the score, so at the estimate $\hat{\beta}$ they sum to zero over all event times. They were introduced by Schoenfeld as partial residuals for the proportional hazards model {{cite:schoenfeld1982}} (Abstract).

At the true coefficient under proportional hazards, these score contributions have conditional mean zero given the risk set. Fitted residuals approximate this behaviour, so a plot of the residuals against event time — or against a function of time, such as its rank — should show a random scatter centred on zero with no trend. A systematic trend means the covariate's effect is changing over time. Concretely: residuals that drift upward over time mean that, late in follow-up, the subjects who have events have larger values of the covariate than the risk-set average predicts — the coefficient is effectively larger late than early, so the hazard ratio is increasing with time. Residuals that drift downward mean the opposite: the effect is weakening, or reversing, over time. A trend in either direction is evidence against proportional hazards for that covariate.

Scaled Schoenfeld residuals use an estimated covariance of the covariates within risk sets to express departures on the coefficient scale. Adding $\hat{\beta}$ produces a diagnostic estimate of the time-varying coefficient $\beta(t)$, whose population target is horizontal under proportional hazards. In modern versions of R's `survival` package, `cox.zph` tests the addition of a time-dependent term $\gamma xg(t)$ to the linear predictor, where $x$ is a covariate and $g(t)$ is a chosen transformation of time. The null is $\gamma=0$. The test uses the score and information for this augmented model, accounting for estimation of the original coefficients; per-term tests and an optional global test are provided {{cite:survival_coxzph}} (§§Details, Value and Note).

The implementation computes the test statistics from the score vector and information matrix, and separately scales the Schoenfeld residuals for the diagnostic plot. The score test is therefore not obtained by correlating the plotted scaled residuals with time {{cite:survival_coxzph}} (§§Details and Value). Since `survival` version $3.0$, the function computes the actual score test; earlier versions used an approximation. A significant result provides evidence against constancy in the direction specified by $g(t)$. A non-significant result does not establish proportional hazards, particularly with few events, so the residual plot should also be examined.

### Log-log survival plots

A second, cruder check uses the survival functions themselves. Under the Cox model, $S(t \mid x) = S_0(t)^{\exp(x^T \beta)}$, so taking logarithms twice gives

$$\log(-\log S(t \mid x)) = \log(-\log S_0(t)) + x^T \beta.$$

For two groups differing in a single binary covariate, the curves of $\log(-\log \hat{S}(t))$ against $t$ (or against $\log t$) should therefore be parallel, separated by the constant $\beta$. In practice the survival curves are estimated separately in each group, usually by Kaplan–Meier, and the transformed curves are plotted. Lines that diverge, converge or cross suggest a time-varying effect and hence a violation of proportional hazards. The plot is easy to produce and easy to over-read: with heavy censoring or small risk sets late in follow-up, the tails of the transformed curves are noisy, and apparent non-parallelism there is weak evidence. It is a screening plot, not a test.

### What to do when the assumption fails

A failed check is not a reason to discard the analysis, but it is a reason not to report a single hazard ratio as if it described the whole follow-up. The standard remedies are: stratify on the offending covariate, so that each stratum has its own baseline hazard and no hazard ratio is estimated for that covariate; allow the coefficient to vary with time, for example by adding an interaction between the covariate and a function of time; or split follow-up into periods and estimate a separate hazard ratio in each. Which remedy is appropriate depends on the scientific question, and the choice, like the tie-handling choice, should be reported. A fitted constant coefficient does not establish a constant hazard ratio when the underlying proportional-hazards assumption fails.

## Worked example — Five subjects, one binary covariate, by hand

Five patients are followed after surgery. The covariate $x$ is $1$ for a new maintenance therapy and $0$ for standard care. Times are in months; $\delta = 1$ denotes recurrence, $\delta = 0$ denotes censoring.

| Subject | Time $y$ | $\delta$ | $x$ |
|---|---:|---:|---:|
| 1 | 2 | 1 | 1 |
| 2 | 4 | 1 | 0 |
| 3 | 5 | 0 | 1 |
| 4 | 7 | 1 | 1 |
| 5 | 9 | 0 | 0 |

There are three event times, $t = 2, 4, 7$. The risk sets are $R(2) = \{1, 2, 3, 4, 5\}$, $R(4) = \{2, 3, 4, 5\}$ (subject 1 has had the event) and $R(7) = \{4, 5\}$ (subject 3 was censored at $5$ and subject 2 has had the event). Writing $e^\beta$ for $\exp(\beta)$, the partial likelihood is

$$L(\beta) = \frac{e^\beta}{3e^\beta + 2} \cdot \frac{1}{2e^\beta + 2} \cdot \frac{e^\beta}{e^\beta + 1},$$

because at $t = 2$ three subjects in the risk set have $x = 1$ and two have $x = 0$; at $t = 4$ two have $x = 1$ and two have $x = 0$, and the subject with the event has $x = 0$; and at $t = 7$ one has $x = 1$ and one has $x = 0$, and the subject with the event has $x = 1$. The partial log-likelihood is

$$\ell(\beta) = 2\beta - \log(3e^\beta + 2) - \log(2e^\beta + 2) - \log(e^\beta + 1),$$

and the score is

$$U(\beta) = 2 - \frac{3e^\beta}{3e^\beta + 2} - \frac{2e^\beta}{2e^\beta + 2} - \frac{e^\beta}{e^\beta + 1}.$$

At $\beta = 0$, each contribution is the share of treated subjects in the risk set, and $U(0) = 2 - (0.600 + 0.500 + 0.500) = 0.400$, which is positive, so the estimate lies above $0$. At $\beta = 0.5$, $U(0.5) = 0.043$. Evaluating $\ell(\beta)$ on a grid confirms a maximum near there:

| $\beta$ | $0$ | $0.25$ | $0.5$ | $0.564$ | $0.75$ | $1$ |
|---|---:|---:|---:|---:|---:|---:|
| $\ell(\beta)$ | $-3.689$ | $-3.612$ | $-3.579$ | $-3.578$ | $-3.589$ | $-3.638$ |

Solving $U(\beta) = 0$ gives $\hat{\beta} = 0.564$, with hazard ratio $\exp(\hat{\beta}) = 1.76$. At that value the three partial-likelihood contributions are $0.242$, $0.181$ and $0.637$, whose product is $L(\hat{\beta}) = 0.0279$, against $L(0) = 0.200 \times 0.250 \times 0.500 = 0.0250$. The observed information at $\hat{\beta}$ is the sum of the risk-set variances of $x$, $0.662$, so the approximate standard error of $\hat{\beta}$ is $1/\sqrt{0.662} = 1.23$ — very large, as it should be with only three events. No conclusion about the therapy could be drawn from five patients; the example is an arithmetic exercise, not evidence.

The Schoenfeld residuals at $\hat{\beta}$ are the observed $x$ minus the risk-set mean at each event time: at $t = 2$, $1 - 0.725 = 0.275$; at $t = 4$, $0 - 0.637 = -0.637$; at $t = 7$, $1 - 0.637 = 0.363$. They sum to zero, as they must at the estimate, since their sum is the score. With three residuals no trend can be assessed; the calculation shows the definition, not a diagnostic conclusion.

Finally, Breslow's estimator at $\hat{\beta}$ has increments $1/(3e^{\hat{\beta}} + 2) = 0.137$ at $t = 2$, $1/(2e^{\hat{\beta}} + 2) = 0.181$ at $t = 4$ and $1/(e^{\hat{\beta}} + 1) = 0.363$ at $t = 7$, giving $\hat{H}_0(7) = 0.681$. The estimated baseline survival at $7$ months is $\hat{S}_0(7) = \exp(-0.681) = 0.506$, and for a treated subject $\hat{S}(7 \mid x = 1) = \exp(-0.681 \times 1.758) = 0.302$.

### Your turn — Four patients

Four patients are followed after the same surgery, with the same binary therapy covariate $x$ ($1$ for the new therapy, $0$ for standard care):

| Subject | Time $y$ | $\delta$ | $x$ |
|---|---:|---:|---:|
| A | 1 | 1 | 1 |
| B | 2 | 1 | 0 |
| C | 3 | 0 | 1 |
| D | 4 | 0 | 0 |

Write down the partial likelihood $L(\beta)$ and the score $U(\beta)$. Find $\hat{\beta}$ and the hazard ratio $\exp(\hat{\beta})$, evaluate $L(\hat{\beta})$, compute the Schoenfeld residual at $t = 1$ at $\hat{\beta}$, and compute Breslow's $\hat{H}_0(2)$ at $\hat{\beta}$.

::: {.callout-tip collapse="true" title="Answer"}
The risk sets are $R(1) = \{A, B, C, D\}$ and $R(2) = \{B, C, D\}$. Hence

$$L(\beta) = \frac{e^\beta}{2e^\beta + 2} \cdot \frac{1}{e^\beta + 2}, \qquad U(\beta) = 1 - \frac{2e^\beta}{2e^\beta + 2} - \frac{e^\beta}{e^\beta + 2}.$$

Setting $U(\beta) = 0$ gives $e^\beta = \sqrt{2}$ exactly, so $\hat{\beta} = \log \sqrt{2} = 0.347$ and the hazard ratio is $\exp(\hat{\beta}) = \sqrt{2} = 1.414$. Both partial-likelihood contributions at $\hat{\beta}$ are $0.293$, so $L(\hat{\beta}) = 0.0858$. The Schoenfeld residual at $t = 1$ is $1 - 2\sqrt{2}/(2\sqrt{2} + 2) = 0.414$. Breslow's increments are $1/(2\sqrt{2} + 2) = 0.207$ at $t = 1$ and $1/(\sqrt{2} + 2) = 0.293$ at $t = 2$, so $\hat{H}_0(2) = 0.500$.
:::

## Common misconceptions

**"A hazard ratio of $2$ means twice the risk."** It does not. A hazard ratio is a ratio of instantaneous event rates, not a ratio of probabilities of ever having the event. The risk ratio — the ratio of cumulative incidences by a given time — depends on the follow-up time and on the baseline hazard, and it moves towards $1$ as follow-up lengthens and most subjects in both groups have had the event.

A concrete, exact illustration makes the point. Suppose hazards are constant, $0.20$ per year in the control group and $0.14$ per year in the treated group, so the hazard ratio is $0.70$ at every time. The cumulative risk by time $t$ is $1 - \exp(-0.20 t)$ and $1 - \exp(-0.14 t)$ respectively. After $1$ year the risks are $0.181$ and $0.131$, a risk ratio of $0.72$; after $5$ years they are $0.632$ and $0.503$, a risk ratio of $0.80$; after $10$ years they are $0.865$ and $0.753$, a risk ratio of $0.87$. The hazard ratio never changed; the risk ratio did, because it is a different quantity. The same example shows the median-survival point: median survival is $\log 2 / 0.20 = 3.47$ years in the control group and $\log 2 / 0.14 = 4.95$ years in the treated group, a ratio of $1.43$, which equals $1/0.70$ only because the hazards are constant in this special case. In general a hazard ratio is not a median-survival ratio, and it is not a ratio of mean survival times either.

**"A hazard ratio is a probability, so it cannot exceed $1$ in the wrong direction."** A hazard is a rate, not a probability: it can exceed $1$ per unit time, and its size depends on the time unit. A hazard ratio of $0.5$ and a hazard ratio of $2$ are equally strong effects in opposite directions, on the log scale, which is why confidence intervals for a hazard ratio are computed on the log scale and are not symmetric around the estimate.

**"The Cox model makes no assumptions because the baseline is unspecified."** The baseline is unspecified, but the model still assumes proportional hazards, log-linearity in the covariates and non-informative censoring. Semi-parametric means one component is left free; it does not mean assumption-free.

**"A non-significant Schoenfeld test means the assumption holds."** It means the data did not reject constancy of the coefficient. With few events the test has little power, and a non-significant result is weak evidence. The plot matters as much as the $p$-value.

**"The partial likelihood is a likelihood, so $\hat{\beta}$ is a maximum likelihood estimator."** It is a maximum *partial* likelihood estimator. It behaves like a maximum likelihood estimator in large samples under the model, but it is not the maximiser of the probability of the observed data, because the spacing of the event times was conditioned away.

## Assumptions and limits

The Cox model rests on the following assumptions, and its limits follow from them.

**Proportional hazards.** The hazard ratio for any two covariate patterns is constant over time. This is the model's defining assumption, and it is testable only in the sense described above: a diagnostic can reject it, but no diagnostic can prove it. When it fails, a fitted constant hazard ratio need not describe the association at any particular time.

**Non-informative censoring.** Censoring must be independent of the event time given the covariates. If subjects are censored because they are about to have the event — for example, if sicker patients drop out — the risk sets are no longer representative, and both $\hat{\beta}$ and the Breslow baseline are biased. See [censoring-statistics](censoring-statistics.qmd).

**Log-linear effect on the hazard.** The model assumes the log hazard is linear in the covariates, $x^T \beta$. A covariate whose effect on the log hazard is curved, or has a threshold, is misspecified; martingale residuals, which compare observed events with the fitted cumulative hazard, are the usual check for functional form, and a misspecified form can also masquerade as non-proportional hazards.

**No unmeasured confounding, for a causal reading.** The model estimates an association conditional on the covariates in the model. A hazard ratio is not a causal effect unless the covariates suffice to control confounding, the model is correctly specified, and the other assumptions hold. The partial likelihood machinery says nothing about causation.

**Enough events, and no separation.** The estimator needs enough observed events relative to the number of coefficients. With very few events, $\hat{\beta}$ is unstable and its normal approximation is poor, as the worked example's standard error of $1.23$ shows. If a covariate perfectly separates early events from late ones, $\hat{\beta}$ can diverge.

### Time-dependent covariates

A covariate may change during follow-up: treatment started, a biomarker measured repeatedly, a transplant received. The model extends directly to $h(t \mid x(t)) = h_0(t) \exp(x(t)^T \beta)$, where $x(t)$ is the covariate value in force just before $t$, and the partial likelihood uses each subject's current value in each risk set. The risk-set covariates are evaluated at the current event time {{cite:james_islr2021}} (§11.7.3, pp. 481–482).

Two warnings matter. First, a covariate must not be defined using the future: classifying a patient as "treated" from the start because they eventually received treatment counts pre-treatment time, during which they could not have had the event as a treated patient, as treated time. That is immortal-time bias, and the time-dependent formulation is the remedy, not the cause. Second, covariates are of two kinds. An *external* covariate is defined outside the subject — a planned dose schedule, calendar time, air pollution — and its future path is known whether or not the subject survives. An *internal* covariate is measured on the subject — a biomarker, blood pressure, transplant status — and is observed only while the subject survives and is uncensored, so its value carries information about the survival time itself. With internal time-dependent covariates, the hazard ratio can still be estimated, but the survival function can no longer be recovered from the fitted model in the usual way: the cumulative hazard integral involves the whole future path of $x(t)$, which is unknown for a subject who has not yet been observed to follow it, and the risk-set interpretation that underlies prediction breaks down {{cite:austin2020}} (§§2.1 and 2.3). In particular, do not report a predicted survival curve from a Cox model containing an internal time-dependent covariate as if it were the survival curve of a patient following a specified covariate path.

## Connections

- [proportional-hazards-model](proportional-hazards-model.qmd) — the definition of the model, the hazard ratio and the survival function; this article takes that definition as given and covers estimation and diagnostics.
- [hazard-rate](hazard-rate.qmd) — the hazard function itself, the instantaneous event rate that the model multiplies by $\exp(x^T \beta)$.
- [survival-function](survival-function.qmd) — the survival function $S(t)$ and its relation to the cumulative hazard, which the Breslow estimator is used to recover.
- [kaplan-meier-estimator](kaplan-meier-estimator.qmd) — the non-parametric product-limit estimator of the survival function, used for the separate-group curves in a log-log plot. With no covariates, Breslow's estimator reduces to the Nelson–Aalen estimator of the cumulative baseline hazard, not to the Kaplan–Meier estimator.
- [log-rank-test](log-rank-test.qmd) — the non-parametric test comparing survival curves, which agrees with the score test at $\beta=0$ for one binary group covariate with no additional adjustment, including ties when the exact conditional partial likelihood and the same risk sets and tie conventions are used.
- [censoring-statistics](censoring-statistics.qmd) — right censoring and the non-informative-censoring assumption on which the risk sets, and therefore the partial likelihood, depend.

## Check yourself

1. At an event time $t$, the partial-likelihood contribution is $\exp(x_i^T \beta) / \sum_{j \in R(t)} \exp(x_j^T \beta)$, and the baseline hazard $h_0(t)$ does not appear. Explain in words why $h_0(t)$ cancels, and state one piece of information about the data that the partial likelihood discards as a result.

::: {.callout-tip collapse="true" title="Answer"}
The contribution is a conditional probability: given that exactly one event occurred at $t$ among the subjects in the risk set, the probability that it was subject $i$ is the ratio of subject $i$'s hazard to the sum of the hazards in the risk set. Every hazard in that ratio contains the same factor $h_0(t)$, so it cancels from numerator and denominator. The price is the spacing of the event times: the partial likelihood uses only the order of the events, through the risk sets, and discards how far apart in time the events were, which is the information that would identify $h_0$.
:::

2. At one event time, $d = 2$ events are tied. The sum of the relative-risk weights over the risk set is $S = 10$, and the sum over the two subjects with events is $E = 4$. The numerator of the partial-likelihood contribution is the same under Breslow's and Efron's methods. Compute the denominator under each method, and say which method gives the larger contribution and why.

::: {.callout-tip collapse="true" title="Answer"}
Breslow's denominator is $S^d = 10^2 = 100$. Efron's denominator is $S(S - E/2) = 10 \times (10 - 2) = 80$. Efron's method gives the larger contribution, because its denominator is smaller: it removes a fraction of the tied subjects' weight from the risk set for the second tied event, instead of reusing the full risk set for both events as Breslow's method does.
:::

3. A plot of scaled Schoenfeld residuals for a treatment covariate trends steadily upward over follow-up, and the score test for an added treatment-by-time interaction is significant. What does this mean for the hazard ratio, and what is one appropriate response?

::: {.callout-tip collapse="true" title="Answer"}
It means the treatment's coefficient, and therefore its hazard ratio, is not constant over time: the effect is larger later in follow-up than earlier, so a single hazard ratio does not describe the whole follow-up period. An appropriate response is to allow the coefficient to vary with time, for example by adding an interaction between treatment and a function of time, or to estimate separate hazard ratios in different follow-up periods, or to stratify if the covariate is a nuisance variable rather than the effect of interest. Reporting the single fitted hazard ratio as if it applied at all times would be misleading.
:::
## History

Cox introduced the model and the conditional likelihood underlying its estimation in his 1972 paper: D. R. Cox, "Regression models and life-tables", read to the Royal Statistical Society in March 1972 and published in the *Journal of the Royal Statistical Society, Series B*, volume 34, pages 187–202. Cox's abstract states the programme plainly: the hazard is a function of the explanatory variables and unknown regression coefficients multiplied by an arbitrary and unknown function of time, and a conditional likelihood is obtained, leading to inferences about the regression coefficients {{cite:cox1972}} (§5, pp. 190–191). The paper's other contribution was to extend Kaplan and Meier's product-limit idea to the comparison of life tables and to regression-like arguments for censored failure times.

Schoenfeld introduced partial residuals in 1982 for examining the proportional-hazards model {{cite:schoenfeld1982}} (Abstract). Current implementations distinguish the graphical diagnostic based on scaled residuals from a formal score test for time-varying coefficients. The documentation of `survival::cox.zph` records the change from an approximate test to the actual score test in version $3.0$ {{cite:survival_coxzph}} (§Note).
