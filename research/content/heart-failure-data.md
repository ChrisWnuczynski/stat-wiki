## Motivating example
A researcher wants to study whether patient characteristics are associated with death during follow-up. Before fitting a classifier, the observational unit, outcome and time horizon must be made explicit. Here one row is one patient and `DEATH_EVENT` records death during that patient's recorded follow-up. Different follow-up durations prevent treating that binary outcome as a common one-year risk.{{cite:chicco_jurman2020}} (“Dataset”, Table 1)

## Definition
The records concern 299 patients with left ventricular systolic dysfunction recruited in Faisalabad, Pakistan, during April–December 2015 at the Faisalabad Institute of Cardiology and Allied Hospital. The tabular release has thirteen columns, including follow-up time and the outcome, rather than thirteen baseline predictors. The public description reports 96 deaths and 203 survivors. Its scope is this clinical cohort, so generalization to other settings requires additional evidence.{{cite:chicco_jurman2020}} (“Dataset”, Tables 1–3)

## Statistical use — Define the prediction time first
A model intended for use at admission should use information available at admission. A completed follow-up duration can encode later information, including when death occurred. Including it as an ordinary predictor can answer a different question from predicting future death at a fixed horizon. A survival analysis instead models event time and accounts explicitly for censoring. The published analyses distinguish models that exclude follow-up time from an analysis stratified by follow-up month.{{cite:chicco_jurman2020}} (“Methods”, “Stratified logistic regression”)

For the binary logistic example, the model is
$$\log\frac{p_i}{1-p_i}=\beta_0+\beta_1\,\mathrm{age}_i+\beta_2\,\mathrm{hbp}_i.$$
The logit is linear in age at fixed blood-pressure status; the probability itself follows a nonlinear curve. Independent patient outcomes and an adequate conditional mean specification are model assumptions. An observational association need not equal an intervention effect.{{cite:openintro2019}} (§9.5.2–9.5.4, logistic models and diagnostics)

## Properties — From a logit change to a probability
If a change in predictors adds $\delta$ to the linear predictor, it multiplies the odds by $a=e^\delta$. Starting at probability $p$, the odds become $ap/(1-p)$, and solving $p'/(1-p')=ap/(1-p)$ gives
$$p'=\frac{ap}{1-p+ap}.$$
The same odds multiplier has different absolute probability effects at different baseline risks. Thus a ten-year age odds ratio cannot be read as a ten-year probability ratio.{{cite:openintro2019}} (§9.5.2, modeling the probability of an event)

## Worked example — Reproducing the cohort fit
Reading the repository's patient CSV and fitting death on age and high-blood-pressure status reproduces the coefficients, standard errors, profile likelihood intervals and deviances below. The annual age odds multiplier is $1.0473$ and the ten-year multiplier is $1.5869$. At a hypothetical baseline probability $0.2$, that ten-year multiplier gives $p'=0.2840$, rather than $0.2(1.5869)$. The overall death fraction is $96/299=0.3211$; always predicting survival would achieve accuracy $203/299=0.6789$ while detecting none of the deaths. This arithmetic illustrates why accuracy alone is an incomplete classifier assessment.{{cite:chicco_jurman2020}} (“Dataset”; “Survival prediction classifiers”)

**Your turn.** A fitted covariate contrast doubles the odds from baseline probability $0.25$. Find the new probability and its absolute increase.

::: {.callout-tip collapse="true" title="Answer"}
The new probability is $2(0.25)/(0.75+2(0.25))=0.4$. Its absolute increase is $0.15$, not $0.25$.
:::

## Assumptions and limits
A small age $p$-value under the two-predictor model does not validate its risk calibration or resolve confounding by omitted clinical variables. Prediction performance should be measured on patients outside model fitting and tuning. Coefficient uncertainty and predictive performance answer different questions: precise association estimates can coexist with limited classification ability. The cohort has unequal class frequencies, and sensitivity as well as overall accuracy matters when evaluating a classifier.{{cite:openintro2019}} (§9.5, logistic regression and diagnostics)
