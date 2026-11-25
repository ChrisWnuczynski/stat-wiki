## Motivating example
If a treatment is associated with a lower chance of an adverse event, a report may compare the two groups using an odds ratio. The number is compact and fits naturally into logistic regression, but it is easy to mistake it for a ratio of event probabilities. Interpreting it starts with the event, the reference group, and the two underlying risks.{{cite:dodge2008}} (pp. 391–393, “Odds and Odds Ratio”){{cite:agresti_tarantola_varriale2023}} (§5.1, pp. 155–156)

## Intuition
For an event with probability $p$, the odds $p/(1-p)$ compare its probability with the probability of *not* seeing it. An odds ratio divides one group's odds by another's. A value above one says the chosen event has higher odds in the first group; a value below one says it has lower odds. The neutral value is one, rather than zero. Which group is in the numerator and which outcome counts as the event are part of the statement, not cosmetic labels.{{cite:dodge2008}} (p. 391, definition and treatment table)

## Definition
Let $p_E=\Pr(Y=1\mid E)$ be the event probability in an exposed group and $p_U=\Pr(Y=1\mid U)$ in an unexposed group. If both lie strictly between zero and one, their population odds ratio is
$$
\operatorname{OR}_{E:U}
=\frac{p_E/(1-p_E)}{p_U/(1-p_U)}.
$$
For a two-by-two sample table with event and non-event counts $(a,b)$ in the exposed row and $(c,d)$ in the unexposed row, the plug-in estimate is the cross-product ratio $\widehat{\operatorname{OR}}=ad/(bc)$. The ratio is finite, and possibly zero, whenever $bc>0$. When $bc=0$ and $ad>0$ it takes the boundary value $+\infty$: one group's sample odds are infinite or the other group's are zero. When both products are zero the ratio is undefined. That case does not in general leave the individual odds undetermined: if both event cells are zero ($a=c=0$) while both rows are nonempty ($b>0$ and $d>0$), each group's sample odds are determined and equal to zero, $0/b$ and $0/d$, yet their ratio is still the indeterminate form $0/0$. The cross-product form makes clear that the odds ratio compares *within-group* event odds. It is an association measure; the table alone does not show that exposure caused the event.{{cite:dodge2008}} (p. 391, mathematical aspects)

## Interpretation — Odds, risks, and coding
The risk ratio is $\operatorname{RR}=p_E/p_U$, and the risk difference is $p_E-p_U$. Algebra gives $\operatorname{OR}=\operatorname{RR}(1-p_U)/(1-p_E)$. Thus the odds ratio is close to the risk ratio when both event probabilities are small, but the two can differ substantially for a common event. For example, if $p_U=1/2$ and $p_E=3/4$, then $\operatorname{RR}=3/2=1.5$ while $\operatorname{OR}=3$. Saying “three times as likely” for this odds ratio would overstate the probability ratio.{{cite:dodge2008}} (pp. 391–392, domains and limitations){{cite:agresti_tarantola_varriale2023}} (§5.1, p. 156)

Reversing the exposure contrast replaces OR by its reciprocal. Redefining the event as its complement also takes the reciprocal; reversing both leaves it unchanged. These symmetries are useful checks on table arithmetic. They also explain why a report needs to identify the reference group and the outcome coding before a direction such as “protective” is assigned.

If the reference-group risk $p_U$ is known, an odds ratio $r$ can be translated back to an event probability: $p_E=rp_U/(1-p_U+rp_U)$. This conversion shows why an odds ratio alone does not specify an absolute change. At $r=3$, a reference risk of $1/10$ corresponds to exposed risk $1/4$, whereas a reference risk of $1/2$ corresponds to exposed risk $3/4$. The same odds multiplier can therefore describe quite different probability differences, and the baseline risk should accompany an odds ratio when practical impact is the question.{{cite:agresti_tarantola_varriale2023}} (§5.1, pp. 155–156)

## Statistical use — Logistic models and sampling
In a logistic regression with a binary group indicator $z$ and other covariates $x$, write $\operatorname{logit}\Pr(Y=1\mid z,x)=\alpha+\beta z+g(x)$. At the *same* value of $x$, changing $z$ from zero to one multiplies the event odds by $e^{\beta}$. The model coefficient is therefore a conditional log odds ratio. It is not a fixed difference in probability: the probability change depends on the starting probability.{{cite:agresti_tarantola_varriale2023}} (§5.1, pp. 155–156)

Odds ratios are also useful when sampling deliberately selects cases and controls rather than a representative fraction of each outcome group. Multiplying all event counts by one sampling factor and all non-event counts by another leaves the table's cross-product ratio unchanged. The sampled event fractions, however, are not population risks without additional sampling information. This is a property of the sampling design, not permission to read a case-control odds ratio as an absolute risk.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The sample odds are $a/b$ and $c/d$, so their ratio is $(a/b)/(c/d)=ad/(bc)$. Since $\operatorname{RR}=p_E/p_U$,
$$
\frac{\operatorname{OR}}{\operatorname{RR}}
=\frac{1-p_U}{1-p_E}.
$$
This approaches one when both probabilities are near zero. Interchanging the rows changes $ad/(bc)$ to $bc/(ad)$. Interchanging event and non-event columns does the same; doing both changes it twice and restores the original value. If event counts are multiplied by $s_1$ and non-event counts by $s_0$, the sampled ratio is $(s_1a)(s_0d)/[(s_0b)(s_1c)]=ad/(bc)$.

For logistic regression, subtraction of the two linear predictors at a fixed $x$ gives $\log\{\operatorname{odds}(z=1,x)/\operatorname{odds}(z=0,x)\}=\beta$, hence the ratio is $e^\beta$. The conditional-to-marginal distinction can also be checked directly. Suppose a binary stratum is equally frequent in both groups. In its first level, $(p_U,p_E)=(1/10,1/4)$, so OR is $(1/3)/(1/9)=3$. In the second, $(p_U,p_E)=(1/2,3/4)$, giving OR $3$ again. After averaging equally over strata, $p_U=3/10$ and $p_E=1/2$, giving marginal OR $1/(3/7)=7/3\approx2.3333$. Equal conditional odds ratios do not force the same marginal odds ratio, even when stratum membership is balanced across exposure groups.{{cite:agresti_tarantola_varriale2023}} (§5.2, p. 158, collapsibility discussion)
Solving $r=p_E(1-p_U)/[p_U(1-p_E)]$ for $p_E$ yields $p_E=rp_U/(1-p_U+rp_U)$, the baseline-risk conversion of the Interpretation section.
:::
:::

## Worked example
Imagine 100 exposed people, of whom 30 have the event and 70 do not, and 100 unexposed people, of whom 10 have the event and 90 do not. The exposed odds are $30/70=3/7\approx0.4286$; the unexposed odds are $10/90=1/9\approx0.1111$. Their ratio is
$$
\widehat{\operatorname{OR}}=\frac{30\times90}{70\times10}=\frac{27}{7}\approx3.8571.
$$
The risks are $0.30$ and $0.10$, so their ratio is $3$ and their difference is $0.20$. In this hypothetical table, exposure is associated with nearly four times the *odds* but three times the *risk*. The absolute difference is 20 percentage points; reporting all three scales makes the magnitude easier to understand.{{cite:dodge2008}} (p. 391, treatment and reference table)

**Your turn.** In another hypothetical study, 8 of 100 exposed people and 4 of 100 unexposed people have the event. Compute the odds ratio, risk ratio, and risk difference. Why are the first two closer than in the worked example?

::: {.callout-tip collapse="true" title="Answer"}
The exposed and unexposed non-event counts are 92 and 96. Hence $\widehat{\operatorname{OR}}=(8\times96)/(92\times4)=48/23\approx2.0870$. The risk ratio is $0.08/0.04=2$, and the risk difference is $0.08-0.04=0.04$, or four percentage points. Both risks are small, so the non-event probabilities in the odds denominator are close to one; this makes OR close to the risk ratio.
:::

## Common misconceptions
An odds ratio is not generally a risk ratio: the common-event example has values three and 1.5 on those two scales. It is not a probability and need not lie between zero and one. A conditional odds ratio from an adjusted logistic model need not equal the marginal odds ratio in an unadjusted table, even when the adjustment variable is balanced across groups, as the stratified example proves. Finally, an observed odds ratio is not automatically causal; selection and confounding can create association without a treatment effect.{{cite:agresti_tarantola_varriale2023}} (§§5.1–5.2, pp. 156–158)

## Assumptions and limits — When the ratio misleads
If an event is common, replacing OR by a risk ratio can badly exaggerate the change in probability: probabilities $1/2$ and $3/4$ give OR $3$ but risk ratio only $1.5$. A sample cell of zero can make $ad/(bc)$ zero, infinite, or undefined; this does not establish a literally zero or infinite population effect. In a case-control sample, the row totals reflect outcome-based recruitment, so its event fractions cannot be used as population risks. And when adjusted and unadjusted analyses are compared, the odds ratio's noncollapsibility means that a change in the number can occur without confounding. The appropriate interpretation therefore names the outcome, contrast, conditioning variables, and sampling design.{{cite:agresti_tarantola_varriale2023}} (§§5.1–5.2, pp. 156–158)

## Connections
[Odds](odds.qmd) are the building block. [The logit link](logit-link.qmd) turns odds into the additive scale of [binary logistic regression](binary-logistic-regression.qmd); the exponentiated slope is interpreted in [interpreting a logistic regression](interpreting-a-logistic-regression.qmd). For an applied report, predicted probabilities and their differences often make the substantive size of an effect clearer beside the odds ratio.{{cite:agresti_tarantola_varriale2023}} (§5.1, pp. 155–156)

## History
The odds ratio sits beside relative risk as a comparison of event rates across treated and reference groups, and the two measures differ. Cox's 1958 binary-response analysis identified $e^\beta$ as the odds ratio for a two-level covariate, linking regression coefficients to two-by-two tables. The present use of $e^\beta$ extends that comparison while holding other covariates fixed.{{cite:dodge2008}} (pp. 391–393, “Odds and Odds Ratio”){{cite:cox1958_logistic}} (§4.2, p. 221){{cite:agresti_tarantola_varriale2023}} (§5.1, pp. 155–156)
