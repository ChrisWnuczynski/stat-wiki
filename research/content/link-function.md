## Lead context
A link function is the map that ties a response mean, which lives on a restricted range, to a linear predictor that can be any real number.

## Motivating example
At $\eta=1.5$ the identity mean is $1.5$. The log-link mean is $e^{1.5}=4.4817$ to four decimals. The logit mean is

$$
\frac{e^{1.5}}{1+e^{1.5}}=0.8176
$$


to four decimals. The same number $\eta$ is a legal probability under the logit, a positive mean under the log, and an unrestricted mean under the identity. It is not a probability under the identity, because $1.5>1$.

## Intuition — Choose the scale on which the covariates act
The linear predictor $\eta=x^\top\beta$ is unrestricted. A probability cannot be negative, and a mean count cannot be negative either. The link $g$ is the function the model inverts: $g(\mu)=\eta$, so $\mu=g^{-1}(\eta)$. Changing the link changes the meaning of a coefficient and leaves the columns of $x$ as they were. The identity, the logit and the log are the classical choices for an unrestricted mean, a probability and a positive mean.{{cite:hastie_esl2009}} (Ch. 9, §9.1, p. 296)

## Definition — Three classical links
For a mean $\mu$ and a predictor $\eta$,{{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374)

- the identity link is $g(\mu)=\mu$, so $\mu=\eta$;
- the logit link is $g(\mu)=\log\{\mu/(1-\mu)\}$, so $\mu=e^{\eta}/(1+e^{\eta})$;
- the log link is $g(\mu)=\log\mu$, so $\mu=e^{\eta}$.

{{cite:hastie_esl2009}} (Ch. 9, §9.1, p. 296) The probit, $g(\mu)=\Phi^{-1}(\mu)$, is the other binomial link recorded there. A link is part of the model choice. It is not a coefficient estimated from the responses.

## Properties — Which means stay legal
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
The identity returns $\eta$ itself, so a negative predictor is a negative mean. The exponential $e^{\eta}$ is positive for every real $\eta$, so a log link cannot produce a negative mean. The logistic $e^{\eta}/(1+e^{\eta})$ lies in $(0,1)$ for every real $\eta$, because the numerator and the denominator are positive and the denominator is larger. A probability model can therefore use the logit for every finite predictor. The identity cannot.
:::
:::

## Worked example — One predictor, three means

**Your turn.** Repeat the three inverses at $\eta=-1$, to four decimals for the log and logit means.

::: {.callout-tip collapse="true" title="Answer"}
The identity mean is $-1$, which is illegal for a probability and for a count mean. The log-link mean is $e^{-1}=0.3679$. The logit mean is $1/(1+e)=0.2689$.
:::

## Connections — The GLM pieces around the link
The link is the middle piece of a [generalised linear model](generalised-linear-model.qmd): a random component supplies the variance function, the [linear predictor](linear-predictor.qmd) builds $\eta$, and $g$ joins them. The [logit link](logit-link.qmd) and the [log link](log-link.qmd) are the two inverses in the example. [Logit, probit and complementary log-log links](logit-probit-and-complementary-log-log-links.qmd) are three maps into a probability; only the first two appear on the ESL page cited here. A canonical link is the choice that makes $\eta$ the natural parameter of a one-parameter exponential family. It is convenient, and it is not the only legal link.

## Check yourself
### A zero predictor
Give the identity, log and logit means at $\eta=0$.

::: {.callout-tip collapse="true" title="Answer"}
The identity mean is $0$. The log-link mean is $e^{0}=1$. The logit mean is $1/2$. Zero is a legal log mean only in the limit $\eta\to-\infty$; at $\eta=0$ the log mean is $1$.
:::

### A coefficient on the log scale
Under a log link, $\eta=\beta_0+\beta_1 x$ and $\beta_1=0.2$. By what factor does the mean change when $x$ increases by $1$?

::: {.callout-tip collapse="true" title="Answer"}
The mean is multiplied by $e^{0.2}=1.2214$ to four decimals. The identity link would have added $0.2$ instead of multiplying.
:::
