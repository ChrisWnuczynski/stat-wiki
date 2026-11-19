## Lead context
The logit, probit and complementary log-log links are three ways to turn an unrestricted linear predictor into a probability.{{cite:nelder_wedderburn1972}} (§§1.1, 2.1–2.2, pp. 371–374)

## Motivating example
At $\eta=1/2$,

$$
\frac{e^{1/2}}{1+e^{1/2}}=0.6225,\qquad
\Phi(1/2)=0.6915,\qquad
1-\exp\{-e^{1/2}\}=0.8077,
$$


each to four decimals. The logit and the probit both sit above $1/2$ by a modest amount. Complementary log-log is already $0.8077$, because the double exponential rises quickly for positive $\eta$. The logit probability $0.6225$ has odds $e^{1/2}=1.6487$ to four decimals: one unit of $\eta$ multiplies the odds by $e$, which is a sentence the probit and complementary log-log probabilities do not support.

## Intuition — Three curves through the unit interval
A binary mean has to lie in $(0,1)$, while a linear predictor $\eta$ can be any real number. Each link is a strictly increasing map from that interval onto the line, and the success probability is the inverse map. The logit and the probit are symmetric about $1/2$: replacing $\eta$ by $-\eta$ replaces $p$ by $1-p$. Complementary log-log is not symmetric in the two tails. It stays nearer $1/2$ on the negative side and climbs faster once $\eta$ is positive.

## Definition — The three inverses
Write $p$ for a success probability and $\eta$ for the linear predictor.

- Logit: $\log\{p/(1-p)\}=\eta$, so $p=e^{\eta}/(1+e^{\eta})$.{{cite:hastie_esl2009}} (Ch. 9, §9.1, p. 296, Eq. 9.2)
- Probit: $p=\Phi(\eta)$, where $\Phi$ is the standard normal distribution function, and the link is $\Phi^{-1}(p)$.{{cite:hastie_esl2009}} (Ch. 9, §9.1, p. 296)
- Complementary log-log: $\log\{-\log(1-p)\}=\eta$, so $p=1-\exp\{-e^{\eta}\}$.

## Properties — Range and symmetry
::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For every real $\eta$, $e^{\eta}>0$, so $e^{\eta}/(1+e^{\eta})$ lies in $(0,1)$. The same bounds hold for $\Phi(\eta)$. For complementary log-log, $e^{\eta}>0$, so $\exp(-e^{\eta})$ lies in $(0,1)$ and $p=1-\exp(-e^{\eta})$ does too.

The logit satisfies $e^{-\eta}/(1+e^{-\eta})=1/(1+e^{\eta})=1-e^{\eta}/(1+e^{\eta})$. The probit satisfies $\Phi(-\eta)=1-\Phi(\eta)$. Complementary log-log does not: the calculations below give $1-\exp\{-e^{-1/2}\}=0.4548$ and $1-\bigl(1-\exp\{-e^{1/2}\}\bigr)=0.1923$, to four decimals, and those are not equal.
:::
:::

## Worked example — One predictor, three probabilities

**Your turn.** Repeat the three inverses at $\eta=-1/2$, to four decimals, and check the logit against $1-0.6225$.

::: {.callout-tip collapse="true" title="Answer"}
The values are $0.3775$, $0.3085$ and $0.4548$. The logit equals $1-0.6225$. The probit equals $1-0.6915$. Complementary log-log, $0.4548$, is not $1-0.8077=0.1923$.
:::

## Connections — One linear predictor, three mean functions
All three links sit on the same [linear predictor](linear-predictor.qmd). The [logit link](logit-link.qmd) is the canonical link for a Bernoulli or binomial [generalised linear model](generalised-linear-model.qmd). The probit is the normal quantile of the same probability. A [log link](log-link.qmd) is the analogous map for a positive mean, not for a probability. Two of these binary links are not nested, so a likelihood-ratio comparison does not choose between them; a criterion such as AIC can, when the random component is held fixed.

## Check yourself
### A zero predictor
Give the logit and probit probabilities at $\eta=0$, and the complementary log-log probability to four decimals.

::: {.callout-tip collapse="true" title="Answer"}
The logit and the probit both equal $1/2$. Complementary log-log equals $1-\exp(-1)=0.6321$ to four decimals. Symmetry about $1/2$ fails at the origin for that link.
:::

### A large positive predictor
As $\eta\to\infty$, what happens to each of the three probabilities?

::: {.callout-tip collapse="true" title="Answer"}
Each tends to $1$. The logit ratio $e^{\eta}/(1+e^{\eta})$ does, $\Phi(\eta)$ does, and $\exp(-e^{\eta})$ tends to $0$, so complementary log-log tends to $1$. The limits agree; the speed at a finite $\eta$ does not.
:::
