## Lead context

The log-rank test, also called the Mantel–Cox test, is a non-parametric test for comparing the survival distributions of two or more groups. It is the standard companion to the Kaplan–Meier curve: where the Kaplan–Meier estimator draws one survival curve per group, the log-rank test asks whether the curves differ by more than chance alone. It compares the groups' whole survival experience, from the start of follow-up to its end, rather than survival at any single chosen time point.

Let $T$ denote a subject's true event time, for example time to death or relapse, and let $S(t) = P(T > t)$ be the survival function and $h(t)$ the hazard function, the instantaneous event rate among subjects still at risk at time $t$. For two groups, labelled $1$ and $2$, the null hypothesis of the log-rank test is

$$H_0: h_1(t) = h_2(t) \quad \text{for all } t,$$

which is equivalent to $S_1(t) = S_2(t)$ for all $t$. The test is built by laying a $2 \times 2$ table at every distinct event time and adding the evidence across times, as in the conditional two-group comparison derived by Cox {{cite:cox1972}} (§7, p. 193). It makes no assumption about the shape of $S(t)$ or $h(t)$: it is valid, in large samples, whatever the underlying survival distribution, provided censoring is non-informative. It is a test of significance only. It estimates no effect size and supplies no confidence interval, so a significant result must be followed by an estimate, usually a hazard ratio from a Cox model, if the size of the difference matters.

## Motivating example — Two glioma survival curves

Bland and Altman illustrate the test with 51 adults with recurrent malignant gliomas, 20 with astrocytoma and 31 with glioblastoma, followed until death or censoring {{cite:bland_altman2004}} (p. 1073). The two Kaplan–Meier curves differ, but the gap is wider at some times than at others and eventually disappears, so no single time point gives a fair summary of the difference. The log-rank test instead accumulates the comparison over the whole follow-up period. Summing over all event times, the observed numbers of deaths were $14$ in the astrocytoma group and $28$ in the glioblastoma group, against $22.48$ and $19.52$ expected if there were truly no difference between the groups. For historical context, their published expected-count shortcut is

$$\frac{(14 - 22.48)^2}{22.48} + \frac{(28 - 19.52)^2}{19.52} = 6.88,$$

as reported by Bland and Altman {{cite:bland_altman2004}} (p. 1073). This shortcut $\sum (O-E)^2/E$, summed over groups, does not generally have the same chi-squared null reference as the standard log-rank statistic.

For inference here, use the standard risk-set variance derived by Cox {{cite:cox1972}} (§7, p. 193, eqs. (25)–(27)) and defined in the next section. Recomputing the $36$ distinct event-time risk sets from Bland and Altman's Table 1 gives $O_1=14$, an expected count $E_1\approx22.48116$, and a sum of conditional hypergeometric variances $V\approx9.59503$. Subjects censored at an event time are included in that risk set but are not counted as events. Thus

$$Z^2=\frac{(O_1-E_1)^2}{V}\approx7.49659.$$

The large-sample $\chi^2_1$ reference gives an approximate $p$-value of $0.00618$, providing evidence against equal survival in the two groups. The test says nothing about *how much* better one group fares. For that, Bland and Altman point to the hazard ratio and the Cox model {{cite:bland_altman2004}} (p. 1073).

## Definition — One $2 \times 2$ table at every event time

Let each subject contribute an observed time $Y = \min(T, C)$, where $C$ is the censoring time, and an indicator $\delta$ with $\delta = 1$ if the event was observed ($T \le C$) and $\delta = 0$ if the observation was censored ($T > C$). Let the distinct event times in the pooled data be $\tau_1 < \tau_2 < \cdots < \tau_K$. Only event times matter: a time at which nothing happens, or at which someone is merely censored, contributes no table.

At event time $\tau_j$, define the risk set as the subjects still under observation just before $\tau_j$, that is, those with $Y \ge \tau_j$. A subject censored exactly at $\tau_j$ is in the risk set at $\tau_j$ but in no later risk set. Let $n_j$ be the total number at risk at $\tau_j$, let $n_{1j}$ and $n_{2j}$ be the numbers at risk in groups $1$ and $2$, so that $n_{1j} + n_{2j} = n_j$, and let $d_j$ be the total number of events at $\tau_j$, of which $d_{1j}$ occur in group $1$ and $d_{2j} = d_j - d_{1j}$ in group $2$. The information at $\tau_j$ is then the $2 \times 2$ table

|  | Group 1 | Group 2 | Total |
|---|---:|---:|---:|
| Events at $\tau_j$ | $d_{1j}$ | $d_{2j}$ | $d_j$ |
| No event at $\tau_j$ | $n_{1j} - d_{1j}$ | $n_{2j} - d_{2j}$ | $n_j - d_j$ |
| At risk at $\tau_j$ | $n_{1j}$ | $n_{2j}$ | $n_j$ |

Conditional on the row and column totals of this table, and under $H_0$, the count $d_{1j}$ has a hypergeometric distribution: if the two groups truly share one hazard, then the $d_j$ events at $\tau_j$ fall into group $1$ in proportion to its share of the risk set. Hence the exact conditional mean and variance of $d_{1j}$ under $H_0$ are

$$E_j = d_j \frac{n_{1j}}{n_j}, \qquad V_j = d_j \frac{n_{1j}}{n_j}\left(1 - \frac{n_{1j}}{n_j}\right)\frac{n_j - d_j}{n_j - 1}.$$

The variance formula applies when $n_j>1$. If $n_j=1$, the group event count is fixed by the margins and its variance is zero; more generally any table with a deterministic group event count contributes no information. The standardized statistic below requires $V>0$.

The factor $(n_j - d_j)/(n_j - 1)$ is the finite-population correction of the hypergeometric variance; when only one event occurs at $\tau_j$, so $d_j = 1$, it simplifies to $V_j = (n_{1j}/n_j)(1 - n_{1j}/n_j)$ {{cite:james_islr2021}} (§11.4, pp. 466–468). Cox derives these same finite-population quantities from conditional likelihood for tied failures {{cite:cox1972}} (§§6–7, pp. 192–193).

Write $O_j = d_{1j}$ for the observed events in group $1$ at $\tau_j$, and add across all event times:

$$O = \sum_{j=1}^{K} O_j, \qquad E = \sum_{j=1}^{K} E_j, \qquad V = \sum_{j=1}^{K} V_j.$$

Here $O$ is simply the total number of events observed in group $1$, and $E$ is the total number expected in group $1$ if $H_0$ were true. The log-rank statistic is

$$Z = \frac{O - E}{\sqrt{V}} = \frac{\sum_{j=1}^{K} (O_j - E_j)}{\sqrt{\sum_{j=1}^{K} V_j}}.$$

Under $H_0$, and when the number of events is large, $Z$ is approximately standard normal, $Z \approx N(0, 1)$, and therefore $Z^2$ is approximately chi-squared on $1$ degree of freedom, $Z^2 \approx \chi^2_1$ {{cite:james_islr2021}} (§11.4, pp. 466–468). Three distinctions matter. First, the hypergeometric mean and variance at each single time are exact, given the margins; it is the normal and chi-squared reference distributions that are approximate, and the approximation needs enough events to be trustworthy. Second, risk sets evolve after events and censoring, so the successive tables are not independent fixed experiments. Under independent censoring and the null event-intensity model, the observed-minus-expected increments have conditional mean zero; the summed conditional variances estimate their accumulated variation. This does not make the final statistic exactly normal. Third, the sign of $Z$ carries the direction: $Z > 0$ means group $1$ had more events than expected under $H_0$, hence worse survival, while $Z < 0$ means fewer events than expected. The usual test is two-sided, referring $|Z|$ to the standard normal distribution, or equivalently $Z^2$ to the $\chi^2_1$ distribution.

## Properties

**Non-parametric and rank-based.** The test assumes no parametric form for the survival or hazard functions. In fact it depends only on the ordering of the event and censoring times, not on the numerical gaps between them: any strictly increasing transformation of time leaves the risk sets, event counts and statistic unchanged. Ties must be preserved under the transformation.

**Directional, not omnibus.** The log-rank test is not equally sensitive to every way two survival curves can differ. It is most powerful when the hazard ratio is approximately constant over time, that is, when $h_1(t)/h_2(t) = \theta$ for a single constant $\theta$, the proportional-hazards or Lehmann-type alternative. Peto and Peto showed that for such alternatives the log-rank test has greater local power than any other rank-invariant test procedure {{cite:peto_peto1972}} (p. 185). It is therefore the right test when a roughly constant relative benefit or harm is expected, and the wrong emphasis when the difference is concentrated early or late, or when the curves cross. See the section on assumptions and limits below.

**The $O/E$ ratio is informative but is not an estimate with a confidence interval.** For group $1$, the ratio $O/E$ estimates its relative event rate: $O/E > 1$ means events arrived faster than the common hazard would predict. Peto and Peto note that these ratios are proportional to the relative incidence rates in the groups {{cite:peto_peto1972}} (§10, pp. 192–193). But the test itself attaches no standard error or confidence interval to that ratio, and it is not a hazard-ratio estimate in the sense of a Cox model. A $p$-value from the log-rank test and a hazard ratio from a Cox model answer different questions and should not be substituted for one another.

**More than two groups.** With $g$ groups, summing the group event counts minus their conditional expectations gives a vector $U$; summing the multivariate hypergeometric covariance matrices gives $V$. The components of $U$ sum to zero, and $V\mathbf{1}=0$, so the full matrix cannot be inverted. The statistic is $U^T V^+U$, where $V^+$ is a generalized inverse on the estimable contrast space. Its asymptotic null degrees of freedom are $r=\operatorname{rank}(V)$, under the usual conditions for a multivariate normal approximation. Normally $r=g-1$, and one may equivalently use $g-1$ independent components with an invertible covariance submatrix {{cite:peto_peto1972}} (§9, p. 192). In degenerate cases, such as a group leaving observation before any informative event comparison, $r$ can be smaller. The reference distribution must then use that actual rank; if $r=0$, there is no informative comparison. For two groups with positive variance this reduces to $Z^2$. The test compares all groups jointly without identifying which pairs differ; ordered groups can instead be assessed with a prespecified trend contrast {{cite:bland_altman2004}} (p. 1073).

**Stratification.** If a categorical factor such as sex or study centre is prognostic, the test can be stratified: the $O - E$ contributions and their variances are computed separately within each stratum and then added across strata, so that comparisons are made only between subjects in the same stratum. The resulting comparison permits different baseline hazards across strata while testing a common direction of group difference.

**Weighted variants.** The ordinary log-rank statistic weights every event time equally, $w_j = 1$. A weighted log-rank statistic replaces $O - E$ by $\sum_j w_j (O_j - E_j)$ and $V$ by $\sum_j w_j^2 V_j$, for weights $w_j$ determined from information available just before each event. Dividing the weighted sum by the square root of its estimated variance gives an approximately standard normal statistic under the same large-sample null conditions. For example, $w_j=n_j$, the total number at risk, gives greater weight to early event times as the risk sets shrink. Peto and Peto derived a censored-data generalisation of Wilcoxon's test by scoring observations through the pooled experimental survival curve; they distinguished its behaviour under censoring from Gehan's earlier scoring procedure {{cite:peto_peto1972}} (§6, p. 190). Weights must be chosen before seeing the data: trying several weighted tests and reporting the smallest $p$-value inflates the type I error rate.

**Relation to the Cox model.** For one binary group covariate with no additional adjustment, the exact conditional tied partial likelihood gives the ordinary log-rank score and information at the null, provided the two analyses use the same risk sets and tie conventions {{cite:cox1972}} (§§6–7, pp. 192–193). To see this, condition on the $d_j$ events in the risk set at time $\tau_j$. At $\beta=0$, every subset of $d_j$ failing subjects has equal probability. The number from group $1$ is consequently hypergeometric: differentiating the log likelihood gives $O_j-E_j$, and the negative second derivative gives $V_j$. Adding these contributions over times produces the ordinary log-rank statistic.

This equality is distinct from the result under Breslow's or Efron's approximations, which generally differ when events are tied. For $2$ subjects at risk in each group and $2$ tied events, both in group $1$, the six possible failing pairs contain $0$, $1$, or $2$ group-$1$ subjects with probabilities $1/6$, $4/6$, and $1/6$. The exact conditional information is therefore the hypergeometric variance $1/3$, whereas Breslow's information is $2(1/2)(1/2)=1/2$. The score is $1$ under both exact conditional and Breslow calculations, so their score statistics are $3$ and $2$. With no ties, all three likelihood choices agree. Here the likelihood calculation is exact conditionally; the usual chi-squared calibration of the resulting statistic remains an approximation.

## Statistical use

**When to use it.** The log-rank test is the default first test when two or more Kaplan–Meier curves are to be compared and no covariates need adjustment. It is the right choice when a roughly constant hazard ratio is plausible, it is routinely reported alongside the curves themselves, and it agrees with the null score test for one binary group covariate with no additional adjustment when risk sets and tie conventions agree and the exact conditional tied likelihood is used. It is also the natural test in a randomised trial analysed by intention to treat, where the groups are defined by randomisation and no adjustment is required.

## Worked example — Two small groups, month by month

Two groups of five patients each are followed in months. A $+$ marks a censored time.

- Group A: $1, 2, 3, 4{+}, 5$ (events at $1, 2, 3, 5$; one censoring at $4$).
- Group B: $6, 7, 8, 9, 10{+}$ (events at $6, 7, 8, 9$; one censoring at $10$).

Take group A as the focal group, so $O_j$ counts A's events. The distinct event times are $1, 2, 3, 5, 6, 7, 8, 9$.

| $\tau_j$ | $n_{Aj}$ | $n_{Bj}$ | $n_j$ | $d_{Aj}$ | $d_j$ | $E_j = d_j n_{Aj}/n_j$ | $V_j$ | $O_j - E_j$ |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 5 | 5 | 10 | 1 | 1 | $1/2 = 0.5000$ | $1/4 = 0.2500$ | $0.5000$ |
| 2 | 4 | 5 | 9 | 1 | 1 | $4/9 \approx 0.4444$ | $20/81 \approx 0.2469$ | $0.5556$ |
| 3 | 3 | 5 | 8 | 1 | 1 | $3/8 = 0.3750$ | $15/64 \approx 0.2344$ | $0.6250$ |
| 5 | 1 | 5 | 6 | 1 | 1 | $1/6 \approx 0.1667$ | $5/36 \approx 0.1389$ | $0.8333$ |
| 6 | 0 | 5 | 5 | 0 | 1 | $0$ | $0$ | $0$ |
| 7 | 0 | 4 | 4 | 0 | 1 | $0$ | $0$ | $0$ |
| 8 | 0 | 3 | 3 | 0 | 1 | $0$ | $0$ | $0$ |
| 9 | 0 | 2 | 2 | 0 | 1 | $0$ | $0$ | $0$ |

A few rows deserve a comment. At $\tau_j = 5$, only one A patient is still at risk: the other three have had events and the fourth was censored at month $4$, so $n_{A} = 1$ and $E_j = 1/6$. From month $6$ onwards no A patient remains at risk at all, so $E_j = 0$ and $V_j = 0$: once a group's risk set is empty, later event times contribute nothing to the test, however many events occur in the other group. Adding the rows,

$$O = 4, \qquad E = \frac{107}{72} \approx 1.486, \qquad V = \frac{4511}{5184} \approx 0.870,$$

so that

$$O - E = \frac{181}{72} \approx 2.514, \qquad Z = \frac{181/72}{\sqrt{4511/5184}} = \frac{181}{\sqrt{4511}} \approx 2.695,$$

and

$$Z^2 = \frac{32761}{4511} \approx 7.262 \approx \chi^2_1.$$

For a chi-squared distribution on $1$ degree of freedom, the two-sided $p$-value is $p = 0.0070$ (computed as $\text{erfc}(\sqrt{7.262/2})$ to four decimal places). At the $5\%$ level, and indeed at the $1\%$ level, we reject the null hypothesis of equal survival: group A has substantially more events, earlier, than the common hazard would predict.

One warning: this is a teaching example with only ten patients and eight events. The normal and chi-squared reference distributions are large-sample approximations, and with so few events the $p$-value of $0.0070$ should be read as illustrative rather than exact; an exact calculation would be preferable at this sample size — but a permutation $p$-value is not automatically the answer. Permuting the observed (time, status) pairs between groups is justified only when those pairs are exchangeable under the null, and a null of equal event-time distributions plus independent censoring within each group does not by itself give exchangeability: the censoring distributions must also be the same in both groups (or the permutation must be restricted within strata with a common censoring pattern). Otherwise, prefer an exact conditional (hypergeometric-based) calculation. The arithmetic, not the $p$-value's third decimal place, is the point of the example. All numbers above were recomputed independently in the accompanying check script.

### Your turn — Two new groups

Two new groups of five patients each are followed in months ($+$ marks censoring):

- Group C: $2, 3, 5, 7{+}, 8$.
- Group D: $4, 6, 9, 10, 12{+}$.

Taking group C as the focal group, compute $O$, $E$ and $V$ from the $2 \times 2$ table at each distinct event time, and hence $Z$, $Z^2$ and the two-sided $p$-value. Do you reject the null hypothesis of equal survival at the $5\%$ level?

::: {.callout-tip collapse="true" title="Answer"}
The distinct event times are $2, 3, 4, 5, 6, 8, 9, 10$. The per-time contributions for group C are:

| $\tau_j$ | $n_{Cj}$ | $n_{Dj}$ | $d_{Cj}$ | $E_j$ | $V_j$ | $O_j - E_j$ |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 5 | 5 | 1 | $1/2 = 0.5000$ | $1/4 = 0.2500$ | $0.5000$ |
| 3 | 4 | 5 | 1 | $4/9 \approx 0.4444$ | $20/81 \approx 0.2469$ | $0.5556$ |
| 4 | 3 | 5 | 0 | $3/8 = 0.3750$ | $15/64 \approx 0.2344$ | $-0.3750$ |
| 5 | 3 | 4 | 1 | $3/7 \approx 0.4286$ | $12/49 \approx 0.2449$ | $0.5714$ |
| 6 | 2 | 4 | 0 | $1/3 \approx 0.3333$ | $2/9 \approx 0.2222$ | $-0.3333$ |
| 8 | 1 | 3 | 1 | $1/4 = 0.2500$ | $3/16 = 0.1875$ | $0.7500$ |
| 9 | 0 | 3 | 0 | $0$ | $0$ | $0$ |
| 10 | 0 | 2 | 0 | $0$ | $0$ | $0$ |

Adding the rows, $O = 4$, $E = 1175/504 \approx 2.331$, $V = 352043/254016 \approx 1.386$, and $O - E = 841/504 \approx 1.669$. Hence $Z \approx 1.417$, $Z^2 \approx 2.009$ on $1$ degree of freedom, and the two-sided $p$-value is $p \approx 0.156$. At the $5\%$ level we do not reject the null hypothesis of equal survival: the excess of $1.67$ events in group C over expectation is well within chance variation. Note the contrast with the worked example, where a similar-sized excess was significant because the variance was smaller and the events were concentrated in one group.
:::

## Common misconceptions

**"A non-significant log-rank test shows the treatments are equally effective."** It does not. It shows only that the data are compatible with equal survival; with few events the test may have little power, and a real difference may be present but undetected. Absence of evidence is not evidence of absence.

**"A significant log-rank test shows a large or clinically important difference."** It does not. The test measures only whether a difference is distinguishable from chance. With thousands of patients, a trivial difference can be highly significant; with few patients, a large difference can be non-significant. Size must come from an estimate, such as the hazard ratio, with a confidence interval.

**"The $p$-value is the probability that the null hypothesis is true."** It is not. The $p$-value is the probability, computed under the null hypothesis of equal hazards, of a statistic at least as extreme as the one observed. It is a statement about the data under $H_0$, not about the probability of $H_0$ itself.

**"The log-rank test compares median survival times."** It does not. It compares the whole survival experience, event time by event time. Two groups can have identical medians and still differ significantly by the log-rank test, and two groups can have different medians with a non-significant log-rank result, particularly if the curves cross.

**"A significant log-rank test means the proportional-hazards assumption holds."** It does not. The test is *most powerful* under proportional hazards, but it can reject the null for many other patterns of difference, and it can fail to reject when hazards are grossly non-proportional. Checking proportional hazards is a separate task, for example with Schoenfeld residuals from a Cox model.

**"Mantel–Cox, Mantel–Haenszel and Cochran–Mantel–Haenszel are three different tests."** They are names for one family of ideas. The log-rank test is also known as the Mantel–Haenszel test or the Cochran–Mantel–Haenszel test, after the stratified $2 \times 2$ table procedure it adapts {{cite:james_islr2021}} (§11.4, pp. 466–468). "Mantel–Cox" records the same lineage through Mantel and the connection to Cox's model; "log-rank" is the name Peto and Peto gave it.

## Assumptions and limits

**Assumptions.** The test rests on the same assumptions as the Kaplan–Meier curve: censoring is unrelated to prognosis, the survival probabilities are the same for subjects recruited early and late in the study, and events happened at the times specified {{cite:bland_altman2004}} (p. 1073). In the language of the construction above, within each group the event time $T$ and the censoring time $C$ must be independent, so that the risk set at each event time is a representative sample of the survivors. The groups must be independent of one another. Deviations matter most when they differ between the groups, for example if censoring is heavier, or differently related to prognosis, in one group than in the other {{cite:bland_altman2004}} (p. 1073). The normal and chi-squared approximations additionally require a reasonable number of events; with very few events the $p$-value is approximate. An exact permutation calculation is safer only under an extra condition: permuting the observed (time, status) pairs between groups requires those pairs to be exchangeable under the null, and equal event-time distributions plus independent censoring within each group do not by themselves give exchangeability — the censoring distributions must also be the same in both groups (or permutation must be restricted within strata with a common censoring pattern). When exchangeability is unavailable, a small-sample procedure must justify its own conditioning and censoring assumptions; the hypergeometric calculation at a single event time alone does not supply an exact null distribution for the statistic across the full follow-up.

**What it cannot do.** The test is purely a test of significance: it cannot provide an estimate of the size of the difference between the groups or a confidence interval {{cite:bland_altman2004}} (p. 1073). A hazard ratio and its interval come from a model, not from this test. It does not compare survival at a particular time, medians, or mean survival, and it does not adjust for covariates; for adjustment, use a stratified log-rank test or a Cox model. It also has no power to spare against alternatives it is not aimed at.

**Crossing curves and non-proportional hazards.** The test is most likely to detect a difference when the risk of an event is consistently greater for one group than for the other, and it is unlikely to detect a difference when the survival curves cross, as can happen when comparing a medical with a surgical intervention {{cite:bland_altman2004}} (p. 1073). When curves cross, the early contributions $O_j - E_j$ have one sign and the late contributions the opposite sign, and they cancel in the sum $O - E$ even though the curves differ markedly. The same cancellation weakens the test whenever the hazard ratio changes substantially over follow-up, for instance with a delayed treatment effect. The curves should always be plotted before the test is run {{cite:bland_altman2004}} (p. 1073): if they cross, or if the proportional-hazards assumption fails, a weighted log-rank test aimed at the part of follow-up where the difference lives, or a different summary such as restricted mean survival time, may be more informative. The choice among these must be made before looking at the data, not by trying each in turn and keeping the smallest $p$-value.

## Connections

- [Kaplan–Meier estimator](kaplan-meier-estimator.qmd): the log-rank test compares the curves this estimator draws. The two share the risk-set construction and the non-informative-censoring assumption: at each event time, the Kaplan–Meier estimator multiplies by $1 - d_j/n_j$ using the same $d_j$ and $n_j$ that appear in the log-rank table.
- [Cox proportional hazards model](cox-proportional-hazards-model.qmd): for one binary group covariate with no additional adjustment, the exact conditional Cox score test at the null agrees with ordinary log-rank for the same risk sets and tie conventions; Breslow and Efron need not agree when events are tied {{cite:cox1972}} (§§6–7, pp. 192–193). The Cox model adds what the log-rank test lacks: a hazard-ratio estimate with a confidence interval, covariate adjustment, and a formal check of proportional hazards.
- [Survival function](survival-function.qmd): the null hypothesis can be stated as $S_1(t) = S_2(t)$ for all $t$; the test compares entire survival functions, not survival at one time.
- [Hazard rate](hazard-rate.qmd): the null hypothesis can equally be stated as $h_1(t) = h_2(t)$ for all $t$, and the test is most powerful when the ratio $h_1(t)/h_2(t)$ is constant.
- [Censoring statistics](censoring-statistics.qmd): censored subjects leave the risk set after their censoring time and contribute no event; the test is valid only under non-informative, independent censoring, the same assumption the Kaplan–Meier estimator requires.
- [Chi-squared test of independence](chi-squared-test-of-independence.qmd): at each event time the log-rank test is a $2 \times 2$ table test, and the combined statistic is a Mantel–Haenszel-style sum over tables; the asymptotic reference distribution is chi-squared with degrees of freedom equal to the covariance rank, normally $g-1$ for $g$ groups.
- [Wilcoxon rank-sum test](wilcoxon-rank-sum-test.qmd): the log-rank test and the Gehan–Wilcoxon and Peto–Peto tests are all weighted log-rank tests, differing only in the weights $w_j$. The Wilcoxon generalisations weight early event times more heavily and are the better choice when the difference between curves is concentrated early in follow-up.

## Check yourself

1. In the worked example, the group A patient censored at month $4$ is in the risk set at month $3$ but not at month $5$. Why is a censored observation counted as at risk at event times up to and including its censoring time, but at no later event time?

::: {.callout-tip collapse="true" title="Answer"}
The risk set at an event time $\tau_j$ is the set of subjects still under observation just before $\tau_j$. A subject censored at month $4$ was under observation until month $4$: had the event occurred at month $4$, it would have been seen, so the subject was genuinely at risk of an observed event up to that point. After month $4$ the subject is no longer followed, so nothing is known about whether or when an event occurred, and the subject cannot contribute to the risk set at month $5$ or later. The same convention applies to the event times themselves: a subject who has the event at $\tau_j$ is in the risk set at $\tau_j$ and leaves it immediately afterwards.
:::

2. Suppose the survival curves of two groups cross: group 1 does worse early in follow-up and better late, so that the contributions $O_j - E_j$ are mostly positive at early event times and mostly negative at late ones. What happens to the log-rank statistic, and what should be done instead?

::: {.callout-tip collapse="true" title="Answer"}
The positive early contributions and the negative late contributions cancel when they are added into $O - E$, so the total can be close to zero and the statistic $Z$ small even though the curves differ substantially. The test therefore has little power against crossing curves. The curves should be plotted first so the crossing is seen. A weighted log-rank test aimed at the part of follow-up where the difference is expected, chosen before seeing the data, or a summary that does not rely on a single signed sum, such as restricted mean survival time, is more appropriate. A non-significant log-rank result in this setting must not be reported as evidence that the groups have equal survival.
:::

3. A log-rank test comparing two groups gives $O - E = 6$ and $V = 9$. Compute $Z$ and $Z^2$, and the approximate two-sided $p$-value. Is the result significant at the $5\%$ level?

::: {.callout-tip collapse="true" title="Answer"}
$Z = 6 / \sqrt{9} = 6 / 3 = 2$, so $Z^2 = 4$ on $1$ degree of freedom. The two-sided $p$-value is the probability that a standard normal variable has absolute value at least $2$, which is approximately $0.0455$. Equivalently, the upper tail of a $\chi^2_1$ distribution above $4$ is about $0.0455$. The result is significant at the $5\%$ level, but only just: the $p$-value is barely below $0.05$, so the evidence is weak and the conclusion is sensitive to small changes in the data.
:::

## History

The log-rank test developed from methods for comparing life tables. Cox's account identifies Mantel's 1966 test as the two-group procedure recovered by his conditional-likelihood calculation, connecting the earlier table-based comparison to regression {{cite:cox1972}} (§7, p. 193).

The name "log-rank" and the test's optimality theory came from Peto and Peto in 1972. They derived the log-rank scores from a Lehmann family of survival curves, in which one group's survival function is a power of the other's, and showed the resulting test to be the locally most powerful rank-invariant test against such alternatives {{cite:peto_peto1972}} (§5.1, pp. 189–190). In the same paper they generalised Wilcoxon's rank-sum test to censored data and compared the three rank tests' efficiencies, reporting asymptotic efficiencies in the absence of censoring: $100\%$ for log-rank against Lehmann alternatives and $82\%$ against normal alternatives, compared with $95\%$ for Wilcoxon's test against normal alternatives {{cite:peto_peto1972}} (§7, p. 191). They also compared their censored-data generalisation of Wilcoxon's test with Gehan's earlier procedure and explained how the censoring pattern affects Gehan's scores {{cite:peto_peto1972}} (§6, p. 190).

Cox's 1972 derivation connected the comparison of survival curves to regression: for one binary group covariate with no additional adjustment, the exact conditional partial likelihood yields the ordinary log-rank score and hypergeometric information at the null, including tied events under matching risk-set and tie conventions {{cite:cox1972}} (§§6–7, pp. 192–193). Breslow and Efron tie approximations do not generally preserve that equality. Bland and Altman's 2004 account illustrates the test's use in clinical survival comparisons and stresses its distinction from estimating the size of a group difference {{cite:bland_altman2004}} (p. 1073).
