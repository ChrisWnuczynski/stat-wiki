## Motivating example

A hospital follows patients after discharge, but some move away before their outcome is known. A raw proportion still alive at one year treats everyone lost to follow-up as though their later outcome were observed. The survival function instead states the probability that an event time exceeds a specified duration. It is a property of the event-time distribution; an estimator such as Kaplan–Meier uses the observed follow-up, with assumptions about censoring, to recover it. The same probability describes whether a component still works at a given age. {{cite:kaplan_meier1958}} (pp. 457–458, introduction){{cite:cox1972}} (pp. 187–188, §1)

## Definition — Meaning and interpretation

For an event time $T$, write $S(t)=\Pr(T>t)=1-F(t)$; the reliability chapter also denotes this function by $R(t)$. Here the inequality is strict: a failure exactly at $t$ is not counted as surviving beyond $t$. Some continuous-time accounts use $\Pr(T\ge t)$; the distinction disappears at times with no probability mass, but it matters for a discrete lifetime. Since $F$ is nondecreasing, $S$ is nonincreasing, lies between zero and one, and approaches zero as $t$ grows when $T$ is finite almost surely. A fall in $S$ between two times measures the probability of an event in that interval, not the risk faced only by those who reached its start. {{cite:cox1972}} (pp. 187–188, §1){{cite:kaplan_meier1958}} (pp. 457–458, introduction)

The distinction between a probability and a conditional risk is useful. Provided $S(s)>0$, $\Pr(T>t\mid T>s)=S(t)/S(s)$ for $t\ge s$. If $S(2)=0.8$ and $S(5)=0.5$, half the original cohort lasts beyond five years, whereas $0.5/0.8=0.625$ of those who lasted beyond year two also last beyond year five. A survival curve is therefore read both from its starting cohort and, by ratios, among current survivors. {{cite:cox1972}} (pp. 187–189, §1)

## Properties — Hazard and mean lifetime

When $T$ has a density $f$ and $S(t)>0$, the hazard is $h(t)=f(t)/S(t)$. It is a rate per unit time, obtained as the limit of $\Pr(t<T\le t+\Delta\mid T>t)/\Delta$ as $\Delta$ decreases to zero. It need not lie below one; treating it as a probability is a unit error. Differentiating $\log S(t)$ where appropriate gives $h(t)=-S'(t)/S(t)$ and hence $S(t)=\exp\{-\int_0^t h(u)\,du\}$ if $S(0)=1$. The integral is the cumulative hazard. These equalities connect a displayed survival curve to the changing risk among those still under observation. {{cite:cox1972}} (pp. 188–189, §§1–2)

For any nonnegative lifetime, $\mathbb ET=\int_0^\infty S(t)\,dt$, with infinite mean when the area diverges. To see why, write each realized lifetime as the area under the indicator $\mathbf1\{T>t\}$ and exchange expectation and integration. This identity shows why a single survival probability, however high, does not by itself determine mean lifetime: the whole curve matters. The system-survival figure illustrates curves that cross. {{cite:kaplan_meier1958}} (pp. 467–468, §2.3)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For $t\ge s$, the event $\{T>t\}$ is contained in $\{T>s\}$; division by $\Pr(T>s)$ proves the conditional-survival ratio. With a density, $F'(t)=f(t)$ almost everywhere and $S=1-F$, so $S'=-f$ and $-\frac{d}{dt}\log S=f/S=h$. Integrating from zero to $t$ proves the hazard representation when $S(0)=1$. Finally $T=\int_0^\infty\mathbf1\{T>t\}\,dt$ for each nonnegative $T$; Tonelli's theorem gives $\mathbb ET=\int_0^\infty\Pr(T>t)\,dt$, including the case where both sides are infinite. The conditional-survival ratio requires only $t\ge s$ and $S(s)>0$, not continuity; the density-based hazard representation uses the stated density, positive-survival and $S(0)=1$ conditions; the last does not require a density.
:::
:::

## Worked example

Suppose an electronic component has an exponential lifetime with rate $0.02$ failures per hour. Its survival after $50$ hours is $S(50)=e^{-0.02(50)}=e^{-1}\approx0.367879$, and its mean lifetime is $1/0.02=50$ hours. If it has already lasted $20$ hours, its chance of lasting beyond hour $70$ is $S(70)/S(20)=e^{-0.02(50)}\approx0.367879$. The equality with the original 50-hour survival is the exponential law's memoryless property, not a feature of every survival distribution. {{cite:cox1972}} (pp. 187–189, §§1–2, hazard definition)

Now place two such independent components in series, so both must work. The system survival at hour $50$ is $S(50)^2=e^{-2}\approx0.135335$. In parallel, at least one must work, giving $1-[1-S(50)]^2\approx0.600424$. Those calculations require independent component lifetimes. A common power surge could make both fail together and invalidate either product calculation. The system-survival figure places these curves beside the single-component curve. {{cite:nist_reliability2002}} (§8.1.2.2, independent-system calculation)

**Your turn.** A lifetime has survival probabilities $S(3)=0.9$ and $S(6)=0.72$. What is the chance of surviving beyond year six given survival beyond year three? What proportion of the original cohort experiences the event in $(3,6]$?

::: {.callout-tip collapse="true" title="Answer"}
The conditional chance is $S(6)/S(3)=0.72/0.9=0.8$. The original-cohort event probability is $S(3)-S(6)=0.18$. The values refer to different denominators: $0.8$ uses those who reached year three, whereas $0.18$ uses the original population.
:::

## Statistical use — Incomplete follow-up

With fully observed independent lifetimes, the empirical fraction exceeding $t$ estimates $S(t)$. Under right censoring, a person who leaves at time $c$ establishes only that their lifetime exceeds $c$. Kaplan and Meier's product-limit estimator multiplies conditional survival fractions at observed event times: $\widehat S(t)=\prod_{t_j\le t}(1-d_j/n_j)$, where $n_j$ is the number still at risk just before time $t_j$ and $d_j$ is the number of events there. A censoring time removes someone from later risk sets without producing an event drop. The estimator relies on censoring being independent of the unobserved event time under the relevant model. {{cite:kaplan_meier1958}} (pp. 457–458, introduction; pp. 462–465, §2.1)

If patients who become ill are more likely to leave follow-up, the censoring mechanism is informative and the usual product-limit curve may overstate survival. If two components share a power source, multiplying their individual survival probabilities may overstate series-system survival. And if events can occur only on numbered days, a smooth density and hazard-rate formula does not describe jumps at the event times; use conditional event probabilities instead. Each is a failure of a different assumption, not a defect in the definition $S=1-F$. {{cite:kaplan_meier1958}} (p. 457, independence of loss time){{cite:cox1972}} (pp. 187–188, discrete and continuous lifetimes)
## Common misconceptions

A survival probability is not a hazard: $S(5)=0.5$ describes the original population at year five, whereas $h(5)$ is an instantaneous rate among those still event-free. A curve estimated from a group is not the path of a particular individual. Nor does censoring mean failure: recording a patient as censored at year two does not assert an event at year two. These errors change either the denominator, the unit, or the meaning of the observation. {{cite:cox1972}} (pp. 187–189, §§1–2){{cite:kaplan_meier1958}} (pp. 457–458, introduction)

## Connections

The [CDF](cumulative-distribution-function.qmd) and survival function are complements. Hazard modelling describes the same distribution through its instantaneous event rate; the reliability chapter applies survival probabilities to component systems.

## History

Kaplan and Meier's 1958 paper gave a product-limit estimate for incompletely observed lifetimes and explicitly scrutinized the independent-loss assumption. Cox's 1972 regression model then connected covariates to the hazard while leaving the baseline time pattern unspecified. These methods address estimation and comparison; the survival function itself remains simply a probability attached to an event-time distribution. {{cite:kaplan_meier1958}} (pp. 457–458, introduction; pp. 462–465, §2.1){{cite:cox1972}} (pp. 187–190, §§1–2)
