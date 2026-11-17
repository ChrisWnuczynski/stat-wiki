## Motivating example
The `sleepstudy` dataset distributed with lme4 has 180 records: ten indexed observations for each of eighteen subjects. Reaction time is recorded in milliseconds. Plotting each subject's measurements against the day index reveals variation in both level and trend. Treating all 180 records as independent subjects would ignore the repeated-measurement structure.{{cite:bates_lme4_2015}} (§1.2, sleep-deprivation example)

## Definition — Distinguish the packaged data from the study protocol
The associated experiment measured psychomotor vigilance using responses to a visual stimulus. Its volunteers held commercial motor-vehicle licences. The experimental protocol included seven days assigned to a sleep-opportunity condition; the most restricted group had three hours of time in bed per experimental night. The dataset's ten records per subject should not be interpreted as ten experimental nights of three-hour sleep. Time in bed is an assigned opportunity rather than an assertion that precisely that many hours were slept.{{cite:belenky2003}} (pp. 2–3, Subjects, Design and Psychomotor vigilance test)

For the packaged example, index subjects by $j$ and recorded days by $d$. A random-intercept, random-slope model is
$$Y_{jd}=\beta_0+\beta_1d+b_{0j}+b_{1j}d+\varepsilon_{jd},$$
where subject effects are independent across subjects with distribution $N_2(0,G)$ and conditional errors are independent $N(0,\sigma^2)$. Subject effects and errors are independent. The fixed coefficients describe the population regression mean; the subject effects describe deviations within this model.{{cite:bates_lme4_2015}} (§§1.1–1.2 and 2.2)

## Properties — A random slope changes within-person covariance
Write $G_{00}=\tau_0^2$, $G_{11}=\tau_1^2$ and $G_{01}=\tau_{01}$. Two records from the same subject have covariance
$$\operatorname{Cov}(Y_{jd},Y_{je})=\tau_0^2+(d+e)\tau_{01}+de\tau_1^2+\sigma^2\mathbf1\{d=e\}.$$
This is obtained by expanding the two linear combinations of the same subject effects. Different subjects have zero covariance under the model. A random slope therefore allows covariance to depend on both recorded days, rather than merely imposing one common correlation on all pairs of within-subject measurements.{{cite:bates_lme4_2015}} (§1.1, covariance specification)

The conditional mean for a particular subject is $(\beta_0+b_{0j})+(\beta_1+b_{1j})d$. Its empirical predictor uses estimated covariance parameters and shrinkage; it is distinct from the population line. Prediction for a new subject integrates a fresh subject-effect vector, whereas prediction for another response from an observed subject uses information about that subject's effects. This target distinction matters even when the future day is the same.{{cite:bates_lme4_2015}} (§5.1.4, conditional modes of random effects)

### A balanced covariance calculation
Let $m=18$. Every subject uses the same full-rank design $X$. The individual coefficient estimator satisfies $\hat b_j=\beta+b_j+(X^\top X)^{-1}X^\top\varepsilon_j$, so its covariance is $H=G+\sigma^2(X^\top X)^{-1}$. Its fitted coefficients are independent of its orthogonal residual contrasts under the Gaussian model. Thus the within-subject residual sum of squares concerns $\sigma^2$, while the scatter of the coefficient vectors concerns $H$.{{cite:bates_lme4_2015}} (§1.1, Gaussian mixed-model covariance)

Apart from constants, the negative restricted log likelihood separates into
$$\frac{m(10-2)}2\log\sigma^2+\frac{\mathrm{RSS}_{\mathrm{within}}}{2\sigma^2}
+\frac{m-1}2\log|H|+\frac12\sum_j(\hat b_j-\bar b)^\top H^{-1}(\hat b_j-\bar b).$$
The first two terms are minimised at $\hat\sigma^2=\mathrm{RSS}_{\mathrm{within}}/[m(10-2)]$. Define $C_b=(m-1)^{-1}\sum_j(\hat b_j-\bar b)(\hat b_j-\bar b)^\top$. The last two terms give $H=C_b$: differentiating with respect to $H^{-1}$ equates $(m-1)H$ with the coefficient scatter sum. Subtracting $\hat\sigma^2(X^\top X)^{-1}$ then gives the estimate $\hat G=C_b-\hat\sigma^2(X^\top X)^{-1}$. This solution is valid when that matrix is positive definite; a boundary solution requires constrained fitting. Maximum likelihood replaces the divisor $m-1$ in $C_b$ by $m$, while the orthogonal within-subject residual estimate is unchanged for this design.

## Worked example — Refit the Gaussian likelihood and interpret the scales
The balanced-design REML calculation for the packaged values gives fixed coefficients $251.405105$ and $10.467286$. The subject-intercept variance is approximately $612.089939$, the subject-slope variance $35.071660$, their covariance $9.604333$ and the residual variance $654.941027$. These estimates reproduce the rounded model output and separate three different forms of variation. For the common within-subject design matrix $X$, fit a separate least-squares coefficient vector $\hat b_j$ to each subject. The fixed coefficient vector is their mean. The residual estimate is $\hat\sigma^2=\sum_j\|y_j-X\hat b_j\|^2/[m(10-2)]$ with $m=18$. If $C_b$ is the sample covariance of these eighteen coefficient vectors using divisor $m-1$, the interior REML estimate is $\hat G=C_b-\hat\sigma^2(X^\top X)^{-1}$. Here the resulting matrix is positive definite. The balanced calculation separates within-subject residual contrasts from the between-subject coefficient covariance.{{cite:bates_lme4_2015}} (§1.2 and §5.2.2, fitted model summary)

The population mean at day five is $251.405105+5(10.467286)=303.741535$ milliseconds. At day zero, the model's marginal response variance is $612.089939+654.941027=1267.030966$. At day five it is $612.089939+10(9.604333)+25(35.071660)+654.941027=2239.865796$. Increasing marginal variance over the day index follows from the fitted random slope; it is different from claiming that the conditional residual variance has increased.

**Your turn.** Using the fitted coefficients, what is the population mean change from day two to day seven?

::: {.callout-tip collapse="true" title="Answer"}
The day difference is five, so the predicted population mean change is $5(10.467286)=52.336430$ milliseconds. The intercept cancels from the comparison.
:::

## Statistical use — Compare likelihoods on the same basis
The random-intercept and random-slope models have the same fixed mean structure. Refitting both by maximum likelihood gives log likelihoods approximately $-897.039322$ and $-875.969672$, a likelihood-ratio statistic $42.139299$. The corresponding chi-square reference with two nominal parameter differences gives $7.072413\times10^{-10}$. It is a reference calculation; a variance component equal to zero is a boundary restriction, and exact finite-sample calibration requires a procedure that represents that restriction.{{cite:bates_lme4_2015}} (§5.2.5, likelihood comparisons and computing p-values)

A parametric bootstrap can fit the smaller model, simulate complete subject trajectories under it, refit both candidate models to each simulated dataset and compare their likelihood-ratio statistics with the observed one. Simulation should preserve the observed design and the subject grouping. Its numerical precision and convergence behaviour are part of assessing that calculation, rather than features of the scientific study protocol.{{cite:bates_lme4_2015}} (§5.2.5, parametric bootstrap)

## Assumptions and limits — Model trends do not reconstruct individual sleep
A fitted line summarises the observed index range under a Gaussian mixed model. Extending it past the recorded days is an extrapolation. Between-subject variation, conditional residual variation and measurement aggregation are three separate contributions to a trajectory. A flat fitted trajectory, or a negative subject slope, is a feature of the reaction-time measurements; a claim about hours slept uses the sleep measurements themselves.{{cite:belenky2003}} (pp. 2–4, study design and performance measures)

## Connections — Marginal correlation grows with the shared slope
Under the fitted random-slope model the covariance of two days $d$ and $e$ on the same subject is $\tau_0^2+(d+e)\tau_{01}+de\tau_1^2$, plus $\sigma^2$ when $d=e$. At days $0$ and $5$ the covariance is $612.089939+5(9.604333)=660.111604$. The marginal variances are $1267.030966$ and $2239.865796$, so the marginal correlation is $660.111604/\sqrt{1267.030966\times2239.865796}=0.391844$. The conditional correlation given the subject effects is zero at distinct days, because the residual errors are independent. The positive marginal correlation is produced by sharing the subject intercept and slope. A model with only a random intercept would have had covariance $\tau_0^2$ at every pair of distinct days, and the correlation would have declined as the residual variance stayed in the denominator while the covariance stayed fixed.{{cite:bates_lme4_2015}} (§1.1, covariance specification)
