## Lead context
Birth weight can be analysed as a continuous response in grams or thresholded into a low-weight indicator. Those are different outcomes and require different models. The `MASS::birthwt` table contains both `bwt` and `low`.{{cite:r_birthwt_data2026}} (§Format, variables `bwt` and `low`)

## Motivating example
A researcher asks whether smoking is associated with birth weight after adjusting for maternal weight, age and the recorded race category. A multiple linear regression compares fitted means for records with equal values of the other predictors. Those adjusted comparisons do not by themselves identify effects of an intervention.{{cite:openintro2019}} (§9.1, “Introduction to multiple regression”)

## Interpretation — Read the units and reference category
In $E(\mathrm{bwt}\mid x)=\beta_0+\beta_1\mathrm{lwt}+\beta_2\mathrm{age}+\beta_3 1\{\mathrm{race}=2\}+\beta_4 1\{\mathrm{race}=3\}+\beta_5\mathrm{smoke}$, maternal weight is measured in pounds and birth weight in grams. The first race category is the reference for the displayed treatment coding. Each coefficient compares fitted means conditional on the other included variables; changing coding changes individual coefficient interpretations while leaving fitted values unchanged.{{cite:r_birthwt_data2026}} (§Format){{cite:openintro2019}} (§9.1, “Indicator and categorical variables as predictors”)

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
