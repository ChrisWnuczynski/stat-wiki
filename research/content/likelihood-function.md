## Lead context
It keeps the data fixed while asking which parameter values make those data more or less compatible with a chosen statistical model. Likelihood ratios drive many estimates and tests, but a likelihood is not itself a probability distribution over parameters.{{cite:fisher1922}} (pp. 323–327)

## Motivating example
Suppose a factory inspects ten items and finds two defective. A model with a defect chance of one fifth makes that outcome more plausible than a model with a defect chance of one half. Likelihood is the tool for comparing those two explanations using the same observed count. It does not say that the chance itself was randomly drawn from one of those values.{{cite:fisher1922}} (pp. 323–327)

## Intuition
Before observing anything, a probability model tells you how the possible data are distributed at a specified parameter. After observing data, turn the same expression around: hold the observation still and vary the parameter. The height at one parameter matters only relative to the height at another parameter under the same observation rule. For continuous measurements that height is a density value, because the probability of one exact measurement is zero.{{cite:fisher1922}} (pp. 323–327)

## Definition
In the displayed definition, $\theta$ is a possible parameter value, $\Theta$ is its parameter space, $f$ is the joint probability mass or density under that value, $X_i$ denotes a random measurement, and $x_i$ its realised value. The joint form is essential: a product of individual masses or densities is justified only when the measurements are independent. For a fixed observed sample, multiplying $L(\theta)$ by a positive factor that does not depend on $\theta$ preserves every likelihood ratio and the locations of all maxima.{{cite:fisher1922}} (pp. 323–327)

## Properties
The log-likelihood $\ell(\theta)=\log L(\theta)$ orders positive likelihood values exactly as $L$ does, and a factor constant in $\theta$ becomes an additive constant in $\ell$. This is why products from independent data are usually computed as sums of logs. For a target $\eta=g(\theta)$, the [invariance of maximum likelihood](invariance-of-maximum-likelihood.qmd) says that if $\widehat\theta$ is a global maximiser of $L$ over $\Theta$, then $g(\widehat\theta)$ maximises the profile likelihood $L_g(\eta)=\sup_{\theta:g(\theta)=\eta}L(\theta)$ over attainable $\eta$. The function $g$ need not be one-to-one.{{cite:fisher1922}} (pp. 323–327)

Proof idea: increasing transforms and parameter-independent factors preserve rankings; for a transformed target, group the original parameter values by their image under $g$.{{cite:fisher1922}} (pp. 323–327)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For $L(\theta)>0$, the logarithm is strictly increasing, so $L(\theta_1)\geq L(\theta_2)$ exactly when $\ell(\theta_1)\geq\ell(\theta_2)$. If $c(x)>0$ depends on the observed data but not on $\theta$, then $c(x)L(\theta_1)/[c(x)L(\theta_2)]=L(\theta_1)/L(\theta_2)$, and both functions have the same maximisers. For the transformed target, suppose $L(\widehat\theta)\geq L(\theta)$ for every $\theta\in\Theta$. Every fibre of $g$ has likelihood supremum at most $L(\widehat\theta)$, whereas the fibre at $\eta=g(\widehat\theta)$ contains $\widehat\theta$ and therefore has supremum $L(\widehat\theta)$. Thus $g(\widehat\theta)$ is a global maximiser of $L_g$, even when several original parameter values map to it.{{cite:fisher1922}} (pp. 323–327)
:::
:::

## Statistical use
One way to estimate a parameter is to maximise its likelihood, often by maximising the log-likelihood numerically. A [likelihood-ratio test](generalised-likelihood-ratio-test.qmd) compares the best fit under a restricted model with the best fit under a broader model. Likelihood also enters Bayesian inference, but [Bayes' rule](bayes-rule.qmd) multiplies it by a prior and then normalises; a high likelihood at one parameter is not by itself a high posterior probability. For censored observations, the likelihood must reflect what was actually observed, such as a survival past a threshold rather than an exact failure time.{{cite:nist_handbook_mle2002}} (§1.3.6.5.2)

## Worked example
Three independent shifts produce $1$, $3$, and $2$ defects. Suppose each shift count is Poisson with the same mean $\lambda>0$. For these data, the likelihood is $L(\lambda)=e^{-3\lambda}\lambda^{1+3+2}/(1!3!2!)=e^{-3\lambda}\lambda^6/12$. Its log is $\ell(\lambda)=6\log\lambda-3\lambda-\log 12$, whose derivative $6/\lambda-3$ vanishes at $\widehat\lambda=2$; the second derivative $-6/\lambda^2$ is negative. Comparing the fitted mean with $\lambda=1$ gives $L(2)/L(1)=2^6e^{-3}\approx3.186$. The same counts are about 3.19 times as likely under mean 2 as under mean 1, within this Poisson model.{{cite:fisher1922}} (pp. 323–327)

**Your turn.** In three new independent Poisson shifts, the counts are $0$, $2$, and $1$. Find the maximum likelihood estimate of $\lambda$, then compare the likelihood at $\lambda=1$ with that at $\lambda=2$.

::: {.callout-tip collapse="true" title="Answer"}
The counts total $3$, so $L(\lambda)\propto e^{-3\lambda}\lambda^3$ and the derivative of its log is $3/\lambda-3$. Hence $\widehat\lambda=1$. The ratio is $L(1)/L(2)=e^3/8\approx2.511$.
:::

For a random sample from $\operatorname{Poisson}(\theta)$, the maximum likelihood estimator of $\theta$ is to be found, together with its unbiasedness, its mean squared error, and its consistency. For a random sample from the exponential density $\lambda e^{-\lambda x}$ on $x>0$, the same comparison yields the maximum likelihood estimator of the rate $\lambda$, the method-of-moments estimator of that rate, and, by invariance, the maximum likelihood estimator of the median lifetime $(\log 2)/\lambda$.

::: {.callout-tip collapse="true" title="Answers"}
For the Poisson sample, $\widehat\lambda=\overline X$; it is unbiased, has mean squared error $\lambda/n$, and is consistent. For independent exponential lifetimes with rate $\lambda$, $\widehat\lambda=1/\overline X$ and the fitted median is $\overline X\log 2$.{{cite:fisher1922}} (pp. 323–327)
:::

**Your turn.** One Poisson observation equals 4. What is the maximum-likelihood value of $\lambda$, and what is $L(4)/L(2)$?

::: {.callout-tip collapse="true" title="Answer"}
The likelihood is proportional to $e^{-\lambda}\lambda^4$, and the score $4/\lambda-1$ vanishes at $\widehat\lambda=4$. The ratio is $e^{-2}\times 16\approx 2.165$.
:::

**Your turn.** Two independent Bernoulli trials are both successes. Where is the likelihood maximised, and what is $L(1)/L(1/2)$?

::: {.callout-tip collapse="true" title="Answer"}
The likelihood is $p^2$ on $[0,1]$, which is largest at $1$. The ratio is $1/(1/2)^2=4$.
:::

**Your turn.** The likelihood in the Poisson question is multiplied by 7, a factor that does not depend on $\lambda$. What happens to the maximiser and to $L(4)/L(2)$?

::: {.callout-tip collapse="true" title="Answer"}
A positive factor that does not depend on the parameter cancels in every ratio and leaves the maximiser unchanged. The maximiser is still 4, and the ratio is still $e^{-2}\times 16$.
:::

## Common misconceptions
A likelihood is not a posterior distribution: without a prior and a normalising integral it assigns no probability to a region of parameter values. For continuous data, $L(\theta)$ is based on a density, not the probability of one exact observation. Nor does a larger maximised likelihood by itself prove that the chosen model is true; it only identifies its best-fitting member for the data and model family being compared.{{cite:fisher1922}} (pp. 323–327)

## Assumptions and limits
Writing $L(\theta)=\prod_i f(x_i;\theta)$ assumes independence; serial correlation or repeated measurements on the same subject require their joint law instead. Parameter boundaries also matter. If three observed Poisson counts are all zero, $L(\lambda)=e^{-3\lambda}$ decreases for $\lambda\geq0$, so its maximum is at $0$. If the parameter space is instead $\lambda>0$, the likelihood has a supremum as $\lambda$ approaches zero but no maximiser in that space. A score equation seeking only an interior zero would miss both facts. Numerical optimisation can also be sensitive to starting values in complex models.{{cite:nist_handbook_mle2002}} (§1.3.6.5.2)

## Connections
[Maximum likelihood](maximum-likelihood.qmd) chooses a maximiser of this function, while [likelihood-ratio testing](generalised-likelihood-ratio-test.qmd) compares maximised values under two nested parameter sets. A [sufficient statistic](sufficient-statistic.qmd) retains all likelihood information about the parameter when the factorisation criterion holds; in a Poisson sample, the sum of the counts contains every $\lambda$-dependent factor of the likelihood. [Bayesian updating](bayes-rule.qmd) uses the same likelihood, now multiplied by a prior to obtain a posterior.{{cite:fisher1922}} (pp. 323–327)

## History
Fisher's 1912 paper sought a principled way to fit a theoretical frequency curve to observed values. He proposed maximising the product of the model's densities, or equivalently the sum of their logarithms, rather than choosing among competing curve-fitting criteria. His wording then still treated the relative weights of parameter values as if they were probabilities.{{cite:fisher1912_curve}} (pp. 155–157)

In 1922 Fisher explicitly separated likelihood from probability: the data were observed, the parameter values were compared, and the relative likelihood did not have to sum or integrate to one. He used this distinction to formulate maximum likelihood estimation and to argue that changing the parameter's scale should not change which underlying model value fits best. The same construction now underlies optimisation for many models, including censored-data models in reliability analysis.{{cite:fisher1922}} (pp. 323–327) {{cite:nist_handbook_mle2002}} (§1.3.6.5.2)
