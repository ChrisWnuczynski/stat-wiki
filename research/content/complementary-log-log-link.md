## Motivating example

Suppose a study records whether at least one failure occurred during an observation period. The probability of an event is bounded by one, but a change in exposure can multiply the underlying event intensity. A complementary log-log model links those two ideas: it models the log of the negative log of the *no-event* probability as a linear function of predictors. A coefficient can then represent a multiplicative change in an intensity-like quantity, provided the event mechanism and observation period justify that interpretation. McCullagh derived the same transformation for grouped survival probabilities in his proportional-hazards model.{{cite:mccullagh1980}} (§3.1, pp. 113–114, eqs. 3.1–3.5)

## Intuition

A binary GLM needs a map from any real linear predictor to a probability strictly between zero and one. Here the inverse map is $p=1-\exp\{-\exp(\eta)\}$. First $\exp(\eta)$ makes a positive event intensity or cumulative-hazard scale; then $\exp\{-\exp(\eta)\}$ gives a no-event probability; finally its complement gives the event probability. At $\eta=0$, $p=1-e^{-1}\approx0.63212$. The halfway probability is reached at $\eta=\log(\log 2)\approx-0.36651$, so the curve is not centred like a logistic curve.{{cite:mccullagh1980}} (§§3.1, 4.1–4.2, pp. 113–116)

## Definition — Probability and inverse link

For $0<p<1$, the complementary log-log link is $g(p)=\log\{-\log(1-p)\}$. Its inverse gives the conditional event probability $p_i=1-\exp\{-\exp(\boldsymbol x_i^\top\boldsymbol\beta)\}$ in a Bernoulli GLM. The link is increasing and maps $(0,1)$ onto the real line. It is not the canonical link for Bernoulli data; the logit has that role. Which link is scientifically useful depends on what the response and predictors mean, not just on whether both yield valid probabilities.{{cite:mccullagh1980}} (§§3.1, 4.1, pp. 113–116)

## Properties — Why a coefficient multiplies a hazard scale

Write $H=-\log(1-p)$, the negative log of the no-event probability. The model is $\log H=\eta$. If a predictor rises by one unit and its coefficient is $\beta_j$, then $H$ is multiplied by $e^{\beta_j}$. In a grouped-time survival model derived from a continuous proportional-hazards model, $H$ is the cumulative hazard over the relevant interval (conditional on survival to its start); the multiplier then has a hazard interpretation under the model's assumptions. In an ordinary cross-sectional binary regression, $H$ is still a mathematical transform of $p$, but a literal instantaneous hazard need not exist. The coefficient is not a log odds ratio.{{cite:mccullagh1980}} (§3.1, pp. 113–114, eqs. 3.1–3.5)

::: {.callout-note collapse="true" title="Proof"}
For $0<p<1$, $0<1-p<1$, so $H=-\log(1-p)>0$ and $\eta=\log H$ ranges across all real values. Exponentiating gives $H=e^\eta$ and then $1-p=e^{-e^\eta}$, hence $p=1-e^{-e^\eta}$. Differentiation gives $dp/d\eta=e^\eta e^{-e^\eta}>0$, establishing monotonicity. If $\eta_1-\eta_0=\beta_j$, then $H_1/H_0=e^{\eta_1-\eta_0}=e^{\beta_j}$. The argument proves the transformed-probability ratio; a physical hazard interpretation additionally requires a survival mechanism.{{cite:mccullagh1980}} (§3.1, p. 114, eqs. 3.4–3.5)
:::

## Interpretation — Asymmetric tails

The link is asymmetric in the event label. At $\eta=-2$, $p\approx0.12658$; at $\eta=2$, $p\approx0.99938$. These are not mirror probabilities about one half. Reversing which outcome is coded as the event changes a complementary log-log model into a log-log model, not merely a sign reversal of the same link. McCullagh highlighted this lack of reversal invariance when comparing ordinal links. It matters whenever “event” and “no event” have different scientific meanings, as in failure before a deadline versus survival beyond it.{{cite:mccullagh1980}} (§4.2, p. 116)

## Statistical use

For counts that are Poisson with mean $\lambda$ but are recorded only as zero versus positive, $\Pr(N>0)=1-e^{-\lambda}$, so the link equals $\log\lambda$. For interval-censored event histories under proportional hazards, the link acts on the conditional probability of an event during an interval and a fitted time effect can absorb the baseline cumulative hazard. These are distinct modelling stories that lead to the same probability formula. If neither story is plausible, the link is still a valid binomial regression but its coefficients should be described on the transformed-probability scale.{{cite:mccullagh1980}} (§3.1, pp. 113–114, eqs. 3.1–3.5)

Compare fitted probabilities and predictive adequacy for the scientific question. The logit, probit, and complementary log-log links can fit similarly in the middle while differing sharply in the tails. A small change in a rare-event probability can be important even when overall classification is unchanged. A link choice should also respect event coding: replacing an event by its complement changes the shape of this model.{{cite:mccullagh1980}} (§§4.1–4.2, pp. 115–116)

## Worked example

Suppose the event probability at a baseline exposure is $p_0=0.20$. Its no-event probability is $0.80$, so $H_0=-\log(0.80)\approx0.22314$ and $\eta_0=\log H_0\approx-1.49994$. Let a one-unit exposure increase have coefficient $\beta=\log 2\approx0.69315$. The transformed scale doubles to $H_1=2H_0\approx0.44629$, giving $p_1=1-e^{-H_1}=1-(0.80)^2=0.36$. Thus the event probability rises from $0.20$ to $0.36$, while the no-event probability is squared. The probability itself did *not* double, and its odds did not necessarily double.{{cite:mccullagh1980}} (§3.1, p. 114, eqs. 3.4–3.5)

**Your turn.** If the baseline event probability is $0.10$ and a covariate triples $H=-\log(1-p)$, find the new event probability and the coefficient on the complementary log-log scale.

::: {.callout-tip collapse="true" title="Answer"}
The baseline no-event probability is $0.90$. Tripling $H$ cubes that probability: $1-p_1=(0.90)^3=0.729$, so $p_1=0.271$. The coefficient is $\log 3\approx1.09861$. The event probability is less than three times $0.10$ because the probability scale is bounded, while $H$ is not.{{cite:mccullagh1980}} (§3.1, p. 114, eqs. 3.4–3.5)
:::

## Common misconceptions

A coefficient is not a log odds ratio; that belongs to the logit link. The curve's asymmetry does not mean it is always a better fit for rare outcomes; data and the event mechanism still matter. A binomial model using this link does not, by itself, establish an underlying continuous-time hazard process. Reversing event and nonevent labels does not leave the model family unchanged under a simple coefficient sign change. Finally, $e^{\beta_j}$ multiplies $H$, not $p$, so it should not be reported as a risk ratio.{{cite:mccullagh1980}} (§§3.1, 4.1–4.2, pp. 113–116)

## Assumptions and limits — Where the interpretation breaks

If a patient can have recurrent events but the record says only whether any occurred, a zero-versus-positive Poisson account assumes a count mechanism that may be wrong when events cluster. If the effect of exposure changes over time, one constant proportional-hazards coefficient need not describe all intervals. For a cross-sectional survey with no time at risk, calling $e^{\beta_j}$ an instantaneous hazard ratio invents a time process absent from the data. Complete separation can also drive a binomial likelihood toward an infinite coefficient, whatever monotone link is used. The algebra still maps real predictors to probabilities; these examples concern model interpretation and estimation.{{cite:mccullagh1980}} (§§3.1, 4.1–4.2, pp. 113–116)

## Connections

The [logit link](logit-link.qmd) is symmetric under event-label reversal and yields odds ratios; the [probit link](probit-link.qmd) also has a symmetric inverse curve. A [survival function](survival-function.qmd) leads to cumulative hazard through $-\log S$. [Binary responses in a GLM](binary-responses-in-a-glm.qmd) supplies the Bernoulli likelihood, while the link specifies how its mean depends on predictors.{{cite:mccullagh1980}} (§§3.1, 4.1–4.2, pp. 113–116)

## Check yourself

**1. Event coding.** If $p=0.20$ for an event, can the same fitted complementary log-log equation for $p$ be turned into one for the nonevent probability merely by negating all coefficients?

::: {.callout-tip collapse="true" title="Answer"}
No. The complementary log-log inverse is asymmetric; reversing the response exchanges it with a log-log link. A fresh model can be fitted to the complemented response, but simple sign reversal is the logit's symmetry, not this link's.{{cite:mccullagh1980}} (§4.2, p. 116)
:::

**2. What doubles?** A fitted coefficient is $\log 2$. What quantity doubles after a one-unit predictor increase, and what further assumption would make it a hazard ratio?

::: {.callout-tip collapse="true" title="Answer"}
The transformed quantity $H=-\log(1-p)$ doubles. In a suitable grouped-time proportional-hazards model, this is an interval cumulative-hazard multiplier; the corresponding continuous-time hazard-ratio interpretation requires the proportional-hazards model. The event probability and its odds do not generally double.{{cite:mccullagh1980}} (§3.1, pp. 113–114, eqs. 3.1–3.5)
:::

## History

McCullagh's 1980 treatment of ordinal regression placed the complementary log-log transform beside the logit as an interpretable link. He derived it from proportional hazards and used grouped family-income data to show how a nearly constant difference on that scale could summarize shifts across income categories. His comparison also noted that the link changes its form when the order of categories is reversed, a feature that remains relevant in binary event coding.{{cite:mccullagh1980}} (§§3.1–3.2, 4.2, pp. 113–116)
