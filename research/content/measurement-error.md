## Motivating example
Suppose a study relates long-term blood pressure to an outcome, but each participant contributes one noisy reading. The observed spread combines differences between people and measurement variability. Using that reading as if it were exact can distort an estimated association. Repeated or validation measurements can provide information that the main regression alone lacks.{{cite:keogh2020_measurement_error}} (§§2.1, 4)

## Definition — The quantity and the recording mechanism
Classical additive error writes the observed value as $W=X+U$, with mean-zero $U$ independent of the true value $X$. Nondifferential error additionally requires that, given $X$ and any adjustment variables, the measurement error supplies no extra information about the outcome. These are assumptions about the measurement process; mean-zero error alone does not imply all of them.{{cite:keogh2020_measurement_error}} (§2.1, eq. 1)

Systematic calibration error, rounding, misclassification, and sampling variability describe different mechanisms. A constant calibration shift changes the mean. Random mean-zero additive error changes variance. For repeated readings of a fixed quantity, independence allows averaging to reduce the random component; a shared calibration shift survives averaging.{{cite:keogh2020_measurement_error}} (§§2.1, 4.2){{cite:grinstead_snell1997}} (§6.2, Thms. 6.7–6.9, pp. 259–260; §6.3, Thms. 6.14–6.16, p. 272)

## Properties — Deriving attenuation in one predictor
In the simple model $Y=\alpha+\beta X+\varepsilon$, assume $X,U,\varepsilon$ are mutually independent, $E(U)=E(\varepsilon)=0$, and finite variances. The population regression slope using $W$ is
$$
\beta_W=\frac{\operatorname{Cov}(W,Y)}{\operatorname{Var}(W)}
=\beta\frac{\sigma_X^2}{\sigma_X^2+\sigma_U^2}.
$$
The multiplier is the reliability ratio. It lies between zero and one when $\sigma_X^2>0$. This attenuation formula requires the stated simple model; multiple predictors, differential error, and nonlinear outcome models can give different directions and magnitudes of bias.{{cite:keogh2020_measurement_error}} (§3.1, continuous-covariate error)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Expanding $\operatorname{Cov}(X+U,\alpha+\beta X+\varepsilon)$ leaves $\beta\operatorname{Var}(X)$ because all cross covariances vanish. Independence similarly gives $\operatorname{Var}(W)=\sigma_X^2+\sigma_U^2$. Substituting in the population least-squares slope yields the ratio.{{cite:grinstead_snell1997}} (§6.3, Exercise 17, p. 281)
:::
:::

## Worked example
Take $\sigma_X^2=9$, $\sigma_U^2=3$, and $\beta=2$. A single measurement has reliability $9/12=0.75$, so the naive population slope is $1.5$. Averaging four independent readings reduces the error variance to $3/4=0.75$. The new reliability is $9/9.75=12/13$, and the slope is $24/13=1.846154$. Averaging helps but does not remove error completely.{{cite:keogh2020_measurement_error}} (§§3.1, 4.2)

If every reading also has a shared additive calibration shift, averaging leaves that shift unchanged. It therefore addresses repeatability rather than calibration. Independent mean-zero error in the response instead increases unexplained variation without causing this covariate attenuation mechanism.{{cite:keogh2020_measurement_error}} (§3.3.1, classical error in continuous outcomes)

**Your turn.** With the same variances, how many independent readings make the reliability ratio at least $0.9$?

::: {.callout-tip collapse="true" title="Answer"}
Solve $9/(9+3/m)\ge0.9$, which gives $m\ge3$. Three readings give reliability exactly $0.9$.
:::

