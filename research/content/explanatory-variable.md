## Lead context
Choosing the explanatory variable makes clear what is being used to predict and what outcome is being predicted. The role belongs to the research question and model; causal effects require a study design that addresses confounding.{{cite:nist_process_model2002}} (§4.1.2) {{cite:dicker2025_cdc}} (“Analyzing and Interpreting Data”)

## Motivating example
Suppose a school studies whether practice time predicts a student's exam score. Practice time is the explanatory variable and score is the response. A fitted line might predict higher scores for students who practise longer, but students also differ in prior knowledge and support at home. Recording those other variables can improve prediction and help assess possible confounding; it does not turn the original observation into a randomized experiment.{{cite:nist_process_model2002}} (§4.1.2) {{cite:dicker2025_cdc}} (“Analyzing and Interpreting Data”)

## Intuition
An explanatory variable supplies a model's input, while the [response variable](response-variable.qmd) is the outcome whose pattern the model tries to describe. It may be a numerical measurement such as temperature, a category such as treatment group, or a constructed quantity such as the logarithm of area. “Predictor” and “covariate” often name the same role. The label “independent variable” is also used, but it does **not** assert that observations or model variables are probabilistically independent.{{cite:nist_process_model2002}} (§4.1.2)

## Definition
In a simple linear regression with a fixed observed input $x_i$ for case $i$, a possible model is $Y_i=\beta_0+\beta_1x_i+\varepsilon_i$. Here $Y_i$ is the random response, $\beta_0$ the intercept, $\beta_1$ the slope, and $\varepsilon_i$ the error with mean zero at the specified input. The explanatory variable supplies the $x_i$ values; $y_i$ denotes a realised response. The model's mean response at that fixed input is $\mathbb E(Y_i)=\beta_0+\beta_1x_i$. If the explanatory quantity is itself random, write it as $X$ and describe the analogous conditional mean $\mathbb E(Y\mid X=x)$. A categorical predictor can be represented by indicator variables; it need not be numerical in its original form.{{cite:nist_process_model2002}} (§4.1.2)

## Properties
The slope in the simple line is measured in response units per explanatory-variable unit. If height is in centimetres and shoe size is the input, a fitted slope of $1.0048$ means a predicted increase of about one centimetre for a one-unit larger shoe size **within that fitted model**; it is not a causal claim. Replacing an explanatory scale $x$ by $z=a+cx$ with $c\ne0$ changes the slope to $\beta_1/c$ and the intercept to $\beta_0-a\beta_1/c$, while leaving fitted values at the same observations unchanged. This is why the slope's number depends on units but predictions do not.{{cite:nist_process_model2002}} (§4.1.2)

For the one-predictor least-squares example, the test of a zero slope has $F=t^2$ when the same residual variance estimate is used. The $F$ test has numerator degrees of freedom one, so it gives the same **two-sided** slope-test $p$-value as $t$ under the usual normal-error model. The reported $R^2=17.8\%$ describes the fraction of response variation accounted for by that fitted line in the sample. Residual plots help assess model fit.{{cite:nist_model_fit2002}} (§4.4.4) {{cite:siegrist2022_normals}} (§6.08)

A linear change of input coordinates leaves straight-line predictions unchanged. In one-predictor least squares, the sum of squares explained by the slope is its squared estimate times the input sum of squares.{{cite:nist_process_model2002}} (§4.1.2)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Substitute $x=(z-a)/c$ into $\beta_0+\beta_1x$ to get $(\beta_0-a\beta_1/c)+(\beta_1/c)z$. Thus the re-expressed line has the same prediction at every observed case. For the simple-regression test, let $S_{xx}=\sum_i(x_i-\overline x)^2>0$ and $S_{xy}=\sum_i(x_i-\overline x)(y_i-\overline y)$. The fitted slope is $\widehat\beta_1=S_{xy}/S_{xx}$, its estimated standard error under the homoscedastic model is $\sqrt{\mathrm{MSE}/S_{xx}}$, and the regression sum of squares is $\mathrm{SSR}=\widehat\beta_1^2S_{xx}$. Hence $t^2=\widehat\beta_1^2S_{xx}/\mathrm{MSE}=\mathrm{SSR}/\mathrm{MSE}=F$, since the numerator mean square has one degree of freedom. Under independent normal errors, $t$ has a symmetric $t_{n-2}$ null law and its square has the corresponding $F_{1,n-2}$ law, giving the same two-sided tail probability. Here $n$ is the number of observed pairs, $\overline x$ and $\overline y$ are their means, and $\mathrm{MSE}$ is the residual sum of squares divided by $n-2$.{{cite:nist_process_model2002}} (§4.1.2) {{cite:siegrist2022_normals}} (§6.08)
:::
:::

## Statistical use
An analyst specifies explanatory variables before interpreting a regression: they determine what values are held fixed when a coefficient is described. With several predictors, a coefficient compares modelled responses as one input changes and the others are held fixed. In observational data, that conditional association may still reflect unmeasured confounding or selection; describe it as an association unless the study design and assumptions support a causal interpretation. For prediction, examine residuals, out-of-sample error, and whether new inputs lie in the range of the data.{{cite:dicker2025_cdc}} (“Analyzing and Interpreting Data”) {{cite:nist_model_fit2002}} (§4.4.4)

## Worked example
Three students practise for $0$, $1$, and $2$ hours, with scores of $50$, $60$, and $65$. Let $x$ be hours and $y$ score, so $\overline x=1$ and $\overline y=175/3$. The input sum of squares is $S_{xx}=(-1)^2+0^2+1^2=2$, and the cross-product sum is $S_{xy}=15$. The least-squares slope is $15/2=7.5$ score points per hour, and the intercept is $175/3-7.5=305/6\approx50.83$. At $x=1.5$ hours the fitted score is $305/6+7.5(1.5)=745/12\approx62.08$. The prediction interpolates within the observed input range; assigning extra practice time would call for a causal study rather than this fitted association.{{cite:nist_process_model2002}} (§4.1.2) {{cite:dicker2025_cdc}} (“Analyzing and Interpreting Data”)

**Your turn.** For three observations with input values $0,1,2$ and responses $5,8,11$, find the fitted slope and the predicted response at input $1.5$.

::: {.callout-tip collapse="true" title="Answer"}
The observations lie on $\widehat y=5+3x$, so the slope is $3$ response units per input unit and the prediction at $x=1.5$ is $9.5$.{{cite:nist_process_model2002}} (§4.1.2)
:::

## Common misconceptions
An explanatory variable need not itself be random: an experimenter may set its levels. Conversely, calling a measured variable “independent” does not make it independent of other predictors, errors, or hidden causes. A small slope-test $p$-value is evidence against a zero slope within the fitted model, not evidence that the input alone explains most response variation. The shoe-size example on this page has a strong slope test yet a modest $R^2$.{{cite:nist_process_model2002}} (§4.1.2) {{cite:nist_model_fit2002}} (§4.4.4)

## Assumptions and limits
A straight-line mean may be inadequate if the response changes nonlinearly with the input. Residual patterns, varying spread, dependence between cases, and extreme predictor values can make the simple model's standard errors or predictions unreliable. Predictions beyond the observed input range require extra care because the model has not been checked there. In observational research, adjustment for recorded variables cannot by itself eliminate confounding by unrecorded factors.{{cite:nist_model_fit2002}} (§4.4.4) {{cite:dicker2025_cdc}} (“Analyzing and Interpreting Data”)

## Connections
The [response variable](response-variable.qmd) is what a model predicts from explanatory inputs. A [treatment](treatment.qmd) is an input assigned by a designed experiment, whereas an observational covariate is recorded as it occurs. The [regression slope](regression-slope.qmd) measures change in a fitted mean per input unit; [least squares](least-squares.qmd) chooses the coefficients that minimize squared residuals. [Confounding variables](confounding-variable.qmd) can produce or distort an observed explanatory-response association.{{cite:nist_process_model2002}} (§4.1.2) {{cite:dicker2025_cdc}} (“Analyzing and Interpreting Data”)

## Check yourself
Try [alcohol and school attendance](../questions/ex-da-alcohol-attendance.qmd), then [interpreting Poisson regression coefficients](../questions/q-31.qmd). The first asks you to identify explanatory and response roles in an observational study; the second asks how transformed inputs affect coefficient interpretation.{{cite:nist_process_model2002}} (§4.1.2)

::: {.callout-tip collapse="true" title="Answers"}
In the attendance study, hours missed is the response; frequent intoxication is the explanatory variable of interest, while age, sex, socioeconomic status, and mental health are adjustment variables. The association is observational. In the Poisson model, `distance` and `log(area)` are explanatory terms; holding area fixed, one extra unit of distance multiplies the fitted mean by $e^{-0.04}\approx0.961$, while doubling area multiplies it by $2^{0.60}\approx1.516$ rather than adding 60 percent per hectare.{{cite:nist_process_model2002}} (§4.1.2)
:::

## History
Francis Galton's 1886 paper on hereditary stature asked how adult children's heights varied with their parents' heights. He used family records for 930 adult children and 205 parentages, after earlier experiments with seed size, to describe the tendency of extreme parental heights to be followed by less extreme child heights on average. In this setting parental height was the explanatory measurement and child height the response, though the paper used the language of regression rather than today's term “predictor.”{{cite:galton1886}} (pp. 246–247)

Modern regression uses explanatory variables far beyond heredity, including controlled inputs in experiments and recorded covariates in observational studies. NIST's process-model description explicitly separates predictor values, response, regression function, and random error. That separation matters because an input's predictive role and its causal role require different evidence.{{cite:nist_process_model2002}} (§4.1.2) {{cite:dicker2025_cdc}} (“Analyzing and Interpreting Data”)
