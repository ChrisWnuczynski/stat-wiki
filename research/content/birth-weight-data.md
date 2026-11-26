## Lead context
Birth weight can be analysed as a continuous response in grams or thresholded into a low-weight indicator. Those are different outcomes and require different models. The `MASS::birthwt` table contains both `bwt` and `low`.{{cite:r_birthwt_data2026}} (§Format, variables `bwt` and `low`)

## Motivating example
A researcher asks whether smoking is associated with birth weight after adjusting for maternal weight, age and the recorded race category. A multiple linear regression compares fitted means for records with equal values of the other predictors. Those adjusted comparisons do not by themselves identify effects of an intervention.{{cite:openintro2019}} (§9.1, “Introduction to multiple regression”)

## Interpretation — Read the units and reference category
In $\E(\mathrm{bwt}\mid x)=\beta_0+\beta_1\mathrm{lwt}+\beta_2\mathrm{age}+\beta_3 1\{\mathrm{race}=2\}+\beta_4 1\{\mathrm{race}=3\}+\beta_5\mathrm{smoke}$, maternal weight is measured in pounds and birth weight in grams. The first race category is the reference for the displayed treatment coding. Each coefficient compares fitted means conditional on the other included variables; changing coding changes individual coefficient interpretations while leaving fitted values unchanged.{{cite:r_birthwt_data2026}} (§Format){{cite:openintro2019}} (§9.1, “Indicator and categorical variables as predictors”)

The age estimate is $-1.948$ g per year with standard error $9.820$ and probability $0.843$ for the zero-coefficient test. That is weak evidence of an age association conditional on this model, rather than evidence that age can have no relationship with birth weight. The intercept corresponds to zero maternal weight and age in the reference category, outside a useful scientific comparison. Regression coefficients can be estimable even when an intercept's literal covariate combination is not meaningful.{{cite:openintro2019}} (§9.1, interpreting coefficients)

## Worked example
Refitting all $189$ records gives the displayed six coefficient estimates and $183=189-6$ residual degrees of freedom. For maternal weight $130$ pounds, age $25$, race category $1$ and no smoking, the fitted mean is
$$
2839.433435+3.999938486(130)-1.947840724(25)=3310.72942\text{ g}.
$$
Changing smoking from $0$ to $1$ lowers the fitted mean by $401.72049$ g, to $2909.00893$ g. This is a conditional mean comparison, not a prediction interval for two individual babies. The smoking coefficient's normal-model $95\%$ interval uses $t_{183,0.975}$ and is $[-617.25379,-186.18718]$ g. The standard-error calculation relies on the fitted linear model's error assumptions.{{cite:dodge2008}} (pp. 492–493, regression standard errors and Student comparison)

The residual standard deviation is $682.1065$ g, and $R^2=0.14830$. Thus substantial individual variation remains after these predictors. Small coefficient probabilities can coexist with modest explained variation because they address different questions.{{cite:openintro2019}} (§9.1, adjusted $R^2$ and coefficient inference)

**Your turn.** At equal age, race and smoking, what fitted birth-weight difference corresponds to a $10$-pound maternal-weight difference? Is it a ten-gram difference?

::: {.callout-tip collapse="true" title="Answer"}
It is $10\times3.999938486=39.99938$ g, approximately $40$ g. The maternal predictor is measured in pounds, so its fitted slope is grams per pound.
:::

## Assumptions and limits
These observations do not randomise smoking or the other predictors. Unmeasured causes, functional-form errors, unequal variance and influential records can alter the interpretation and uncertainty. The race variable describes recorded categories and can stand for many social and environmental differences; its coefficient does not isolate a biological cause. A low-birth-weight analysis uses a binary response and a different likelihood from this continuous Gaussian regression.{{cite:openintro2019}} (§9.1, conditional interpretation; §9.5, logistic regression response)

## Intuition
Birth weight in grams and a low-weight indicator are two different responses stored in the same table. A linear regression of `bwt` compares fitted means. A logistic regression of `low` compares fitted probabilities of falling below a threshold. A coefficient in the linear fit is a difference in grams at fixed values of the other included predictors. It is not an effect of an intervention, because smoking, maternal weight, age, and the recorded race category were not assigned by the analyst.{{cite:r_birthwt_data2026}} (§Format, variables `bwt` and `low`)

## Definition
The table has $189$ records. The displayed mean model uses an intercept, maternal weight in pounds, age, two indicators for the non-reference race categories, and a smoking indicator, six coefficients in all. The residual degrees of freedom are $189-6=183$. Maternal weight enters in pounds and the response is in grams, so the slope $3.999938486$ is grams per pound. A difference of $10$ pounds, with age, race category, and smoking held fixed, changes the fitted mean by about $39.999$ grams. The reference race category is the one omitted by the two indicators. Swapping which category is omitted changes the numerical coefficients and leaves the fitted means unchanged.{{cite:openintro2019}} (§9.1, “Indicator and categorical variables as predictors”){{cite:r_birthwt_data2026}} (§Format)

## Properties
At maternal weight $130$, age $25$, race category $1$, and no smoking, the fitted mean is $3310.72942$ grams. Switching smoking on lowers that fitted mean by $401.72049$ grams, to $2909.00893$. The normal-model $95\%$ interval for the smoking coefficient, using $t_{183,0.975}$, is $[-617.25379,-186.18718]$. The residual standard deviation is about $682$ grams and $R^2$ is about $0.148$, so most of the variation among births remains after these predictors. The age coefficient is about $-1.95$ grams per year with a coefficient probability near $0.84$. That probability is weak evidence against a zero linear coefficient in this specification. It is not a proof that age and birth weight are unrelated in every population or every functional form.{{cite:openintro2019}} (§9.1, interpreting coefficients){{cite:dodge2008}} (pp. 492–493, regression standard errors and Student comparison)

## Common misconceptions
The intercept is the fitted mean at zero maternal weight and zero age in the reference category. That covariate combination is not a mother in the table, so the intercept is a bookkeeping term rather than a scientific prediction. A small coefficient probability for age does not say that the smoking comparison is unaffected by how age was coded; it says that, once the other included terms are present, the linear age term adds little. The race coefficients compare recorded categories and can stand in for many social differences. They do not isolate a biological mechanism. A binary low-weight analysis uses a different likelihood, and its coefficients are log odds ratios rather than gram differences.{{cite:openintro2019}} (§9.1, conditional interpretation; §9.5, logistic regression response){{cite:openintro2019}} (§9.1, adjusted $R^2$ and coefficient inference)

## Statistical use
The fitted mean is a comparison at stated values of the included predictors. At maternal weight $130$ pounds, age $25$, the reference race category, and no smoking, the fit is $3310.72942$ grams. Turning smoking on subtracts $401.72049$ grams and leaves $2909.00893$ grams. The $95\%$ interval for that smoking coefficient, on $183$ residual degrees of freedom, is $[-617.25379,-186.18718]$. Both endpoints are negative in this fit. The interval is a statement about the coefficient in the linear specification, under the normal-error model used to form it.

The residual standard deviation is $682.1065$ grams and $R^2$ is $0.14830$. Most of the gram-to-gram variation among the $189$ births remains after weight, age, race category, and smoking are included. The age coefficient, about $-1.95$ grams per year, has a coefficient probability near $0.84$. That probability and the modest $R^2$ answer different questions. One asks whether the linear age term, given the other included terms, is distinguishable from zero. The other asks what fraction of the variance the whole specification captures. A ten-pound difference in maternal weight, with the other included predictors held fixed, moves the fitted mean by about $39.999$ grams because the slope is about $3.9999$ grams per pound.{{cite:openintro2019}} (§9.1, interpreting coefficients)
