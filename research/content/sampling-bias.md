## Lead context
A larger sample can reduce random fluctuation around a respondent mean while leaving a systematic selection error relative to the target population.

## Motivating example
An online survey can collect many responses and still overrepresent people who are particularly interested in its subject. The key question is which population mean the respondents' average estimates. Sampling selects part of a population; inference requires a reason that the selected part can stand in for the target.{{cite:dodge2008}} (pp. 468–470, Sampling)

## Definition — Selection and the target mean
Estimator bias is an expectation over a specified sampling process, $\mathbb E(\widehat\theta)-\theta$. A realised difference between a sample mean and a population mean is an error; it need not equal that bias. Sampling bias arises when a selection mechanism makes the expected estimator differ systematically from its target. Unequal selection probabilities can cause it for an unweighted mean, but unequal probabilities do not force bias for every variable or every estimator.{{cite:dodge2008}} (p. 41, Bias){{cite:meng2018_big_data}} (§2, pp. 689–692)

## Properties — An exact selection identity
For a finite population of $N$ values $Y_i$, let $R_i$ indicate inclusion and let $n=\sum_iR_i$, with $0<n<N$ and nonconstant $Y_i$. Use population averages with denominator $N$ to calculate variances, covariance and correlation. Then
$$
\overline Y_{\rm sample}-\overline Y_{\rm population}
=\frac{\operatorname{Cov}_N(R,Y)}{n/N}
=\rho_{R,Y}\,\sigma_Y\sqrt{\frac{N-n}{n}}.
$$
The first equality follows by expanding $N^{-1}\sum R_iY_i-(n/N)\overline Y$. The second uses $\operatorname{Var}_N(R)=(n/N)(1-n/N)$. This is an algebraic identity for the realised selection vector, with no random-sampling assumption.{{cite:meng2018_big_data}} (§2.2, eqs. 2.2–2.4, pp. 690–691)

If all $Y_i$ are equal, the sample error and the inclusion–outcome covariance are both zero; the correlation is undefined and the covariance form supplies the identity.

The identity separates the association of inclusion with the outcome, the sample fraction, and population variability. A large absolute $n$ cannot determine the error without the other factors. If inclusion is uncorrelated with a particular outcome, its sample mean can equal the population mean even when selection is highly unequal. That equality does not establish representativeness for other outcomes.{{cite:meng2018_big_data}} (§2.2–2.3, pp. 690–694)

## Worked example
Consider a population of $1000$ people: $500$ have $Y=0$ and $500$ have $Y=1$. Select $100$ of the first group and $400$ of the second. The population mean is $0.5$, while the selected mean is $400/500=0.8$. Here $\sigma_Y=0.5$, the sample fraction is $1/2$ and $\rho_{R,Y}=0.6$. The identity gives
$$
0.6(0.5)\sqrt{\frac{1000-500}{500}}=0.3,
$$
which is exactly the difference between the means. Replicating every population and selected record leaves this discrepancy unchanged.

If the respective inclusion probabilities are $0.2$ and $0.8$, inverse-probability weights are $5$ and $1.25$. In this constructed sample, the weighted proportion is
$$
\frac{400(1.25)}{100(5)+400(1.25)}=0.5.
$$
The calculation illustrates what correct weighting can accomplish; in a general sample, estimated weights add uncertainty and do not automatically remove selection effects.{{cite:meng2018_big_data}} (§2.3, weighting and data quality)

**Your turn.** Keep $100$ selected people with $Y=0$, but select $100$ with $Y=1$. Find the sample mean and the inclusion–outcome covariance.

::: {.callout-tip collapse="true" title="Answer"}
The sample mean is $1/2$, matching the population. Since $\mathbb E_N(RY)=0.1$, $\mathbb E_NR=0.2$ and $\mathbb E_NY=0.5$, the covariance is $0.1-0.2(0.5)=0$.
:::

## Connections — Coverage, response and measurement
A sampling frame may omit part of the target population; selected people may decline to respond; recorded answers may measure a different quantity from the intended outcome. These are distinct mechanisms. Random selection from a restricted frame supports inference about that frame, and further assumptions are needed to extrapolate beyond it. A reported standard error under simple random sampling quantifies the stated random mechanism; it does not by itself quantify nonresponse or coverage effects.{{cite:meng2018_big_data}} (§2.1–2.2, pp. 688–691){{cite:dodge2008}} (pp. 468–470, Sampling)

