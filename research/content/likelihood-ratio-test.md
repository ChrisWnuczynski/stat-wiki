## Motivating example
Eight heads in ten tosses invite a comparison between a fair-coin model and a coin whose success probability is fitted to those tosses. The likelihood-ratio test measures how much better the fitted model explains the observed sequence and then asks whether that improvement would be surprising under fairness. The second step needs a null distribution; a large improvement alone is not a calibrated test.{{cite:siegrist2022_lrt}} (§9.5, Basic Theory and Bernoulli trials)

## Intuition
The null hypothesis restricts the set of parameter values; the larger model has more freedom to fit the same data. If the best null fit is nearly as good as the best unrestricted fit, the restriction costs little. If it is much worse, the data pull against the null. For nested models use $\Lambda=\sup_{\theta\in\Theta_0}L(\theta;x)/\sup_{\theta\in\Theta}L(\theta;x)$, so $0\le\Lambda\le1$ and *small* values challenge $H_0$. The equivalent statistic $G^2=-2\log\Lambda$ grows in the opposite direction. The convention matters: some authors reverse the ratio and reverse the rejection tail.{{cite:siegrist2022_lrt}} (§9.5, Basic Theory)

## Definition — Compare the best allowed fits
In a parametric model with null parameter set $\Theta_0\subseteq\Theta$, the likelihood-ratio statistic compares the largest likelihood under $H_0$ with the largest likelihood in the full model. The maximization must use the *same observations* and compatible likelihoods, including their normalizing factors. It is not the likelihood at a guessed alternative parameter. For two simple hypotheses, a different ratio is used instead: the Neyman–Pearson ratio $f_0/f_1$ of the likelihoods at the two specified parameter values. That simple-versus-simple convention is distinct from the generalised statistic above, whose denominator is the supremum over the *full* parameter space $\Theta$ — including $\Theta_0$ itself — not a maximum over alternatives. Calibration chooses a cutoff from the ratio's null law so that a chosen type I error rate is respected.{{cite:siegrist2022_lrt}} (§9.5, Basic Theory and Simple Hypotheses)

## Properties — Exact calibration and a large-sample shortcut
For a regular nested model, $G^2=2\{\ell(\widehat\theta)-\ell(\widehat\theta_0)\}$ is approximately chi-squared under $H_0$, with degrees of freedom equal to the number of independent restrictions. This is a *large-sample* reference law, not part of the definition of the ratio. Exact null probabilities can be calculated for some discrete models and may differ substantially at small $n$. Parameters on a boundary, unidentified nuisance parameters or a singular information matrix can spoil the usual chi-square limit, so the degrees-of-freedom shortcut needs its assumptions.{{cite:siegrist2022_lrt}} (§9.5, Basic Theory)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
For $n$ independent Bernoulli trials with $k$ successes, the likelihood is $L(p)\propto p^k(1-p)^{n-k}$. Under $H_0:p=p_0$ the numerator is proportional to $p_0^k(1-p_0)^{n-k}$. In the full model, differentiation gives $\widehat p=k/n$ for $0<k<n$, so
$$
G^2=2\left[k\log\frac{\widehat p}{p_0}+(n-k)\log\frac{1-\widehat p}{1-p_0}\right].
$$
The same expression extends to $k=0,n$ using $0\log0=0$. For a fair-coin null, replacing $k$ by $n-k$ leaves $G^2$ unchanged, so an exact two-sided tail includes extreme counts in both directions. The derivation establishes the statistic; its null tail must then be computed from $K\sim\operatorname{Binomial}(n,p_0)$ or approximated under justified conditions.{{cite:siegrist2022_lrt}} (§9.5, Bernoulli trials)
:::
:::

## Statistical use — How deviance fits in
For nested generalized linear models fit to the same observations with the same likelihood family and a common fixed dispersion $\phi$, the likelihood-ratio statistic is the difference in scaled deviances: $(D_{\mathrm{reduced}}-D_{\mathrm{full}})/\phi$, where $D$ denotes the unscaled deviance. When $\phi=1$, this coincides with the raw deviance difference. The reduced model's deviance is at least as large as the full model's because the full fit has at least as much freedom; equality is possible. The reference degrees of freedom are the difference in independent fitted parameters, provided regularity holds. A quasi-Poisson mean–variance specification alone is not a full likelihood, so it cannot supply an ordinary likelihood ratio simply by subtracting two quasi-deviances.{{cite:siegrist2022_lrt}} (§9.5, Basic Theory)

The ten-toss example already shows a finite-sample failure of the chi-square approximation. A null value $p=0$ lies on the edge of the Bernoulli parameter space, outside the ordinary interior-parameter argument for a chi-square limit. A mixture model with a component weight of zero leaves that component's parameters unidentified under the null, so counting them as ordinary degrees of freedom is unsafe. And if two models are fit to different rows, their likelihood maxima cannot be compared as a nested-model ratio for one common sample. In such cases use a valid exact law, simulation or a model-specific asymptotic analysis.{{cite:siegrist2022_lrt}} (§9.5, Basic Theory)

## Worked example
Under $H_0:p=0.5$, ten independent coin tosses produce eight heads. The unrestricted estimate is $\widehat p=0.8$, and
$$
G^2=2\{8\log(0.8/0.5)+2\log(0.2/0.5)\}=3.8549,
\qquad \Lambda=e^{-G^2/2}=0.1455.
$$
A chi-square reference with one degree of freedom gives an approximate upper-tail probability $0.0496$. But the exact null LRT tail consists of $K\le2$ or $K\ge8$ for $K\sim\operatorname{Binomial}(10,0.5)$, whose probability is $2(1+10+45)/1024=0.109375$. Thus a nominal $5\%$ decision can change when the asymptotic shortcut replaces the exact discrete calculation. The likelihood ratio and its calibration answer separate questions.{{cite:siegrist2022_lrt}} (§9.5, Bernoulli trials)

**Your turn.** Test $H_0:p=0.5$ after $14$ heads in $20$ independent tosses. Compute $G^2$ using $\widehat p=0.7$ and compare the one-degree chi-square tail with the exact two-sided binomial tail. Which is below $0.05$?

::: {.callout-tip collapse="true" title="Answer"}
$G^2=2\{14\log(0.7/0.5)+6\log(0.3/0.5)\}=3.2913$. The chi-square tail is about $0.06965$. The exact tail $P(K\le6\text{ or }K\ge14)=0.11532$ under $K\sim\operatorname{Binomial}(20,0.5)$. Neither is below $0.05$, so neither version rejects at that level.
:::

## Common misconceptions
The likelihood ratio is not the probability that the null hypothesis is true; it compares how well two models fit fixed data. Maximizing each likelihood is essential: an arbitrary alternative value can make the denominator misleadingly small. The degrees of freedom in the chi-square shortcut count parameter restrictions, not observations. A chi-square tail near $0.05$ is not automatically accurate for ten Bernoulli observations, as the exact calculation shows. Finally, a small ratio need not imply a useful effect size: with enough data, a tiny departure from a null model can be statistically detectable.{{cite:siegrist2022_lrt}} (§9.5, Basic Theory)

## Connections
[The ratio depends only on the between sum of squares](../questions/ex-inf-glrt-two-means.qmd) uses a normal model with a known variance. [One term of the expansion](../questions/ex-inf-pearson-one-cell.qmd) shows why Pearson and deviance statistics are close for small count deviations. [Overdispersion and quasi-Poisson inference](../questions/q-47.qmd) asks why a mean and variance model without a full probability law does not automatically give an ordinary likelihood ratio.{{cite:siegrist2022_lrt}} (§9.5, Basic Theory)

## History
Neyman and Pearson's 1928 work used likelihood ratios in hypothesis testing. Wilks's paper on the large-sample distribution of likelihood ratios appeared in 1938, supplying the historical source of the familiar chi-square approximation under suitable conditions.{{cite:dodge2008}} (pp. 309–310, “Likelihood Ratio Test,” Neyman–Pearson attribution){{cite:anastasiou_reinert2020}} (§1, p. 608; reference 25, p. 643)
