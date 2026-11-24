## Motivating example
Two estimators of a probability can trade bias against variability. The raw sample fraction has the right average under repeated samples, yet a slightly shrunken fraction may fluctuate less and have a smaller average squared error at some true probabilities. Mean squared error gives one scale on which to compare both effects. To use it well, the target and the sampling distribution must be stated; one observed error does not reveal an estimator's repeated-sample MSE.{{cite:gelman_bda2013}} (Ch. 4, §4.4, p. 92)

## Intuition
Squared error measures distance from a target and gives larger mistakes disproportionately more weight. Taking its expectation before the data are observed turns it into a property of an estimation procedure at a specified parameter value. The variance term in the decomposition measures random spread around the estimator's own mean; squared bias measures how far that mean is from the target. Removing bias can increase variance enough to worsen mean squared error, which is why unbiasedness alone is not a full accuracy criterion.{{cite:casella_berger2002}} (Ch. 7, §7.3.1, p. 330)

## Definition
For an estimator $T(X)$ of a fixed scalar parameter $\theta$, its frequentist risk under squared-error loss is $\operatorname{MSE}_\theta(T)=E_\theta[(T-\theta)^2]$, provided this expectation exists. The subscript matters: two estimators can exchange places as $\theta$ changes. For a vector parameter one must specify a norm or weighting matrix, such as $E_\theta\|T-\theta\|_2^2$; there is no single scalar MSE until that loss is chosen. A prediction error $E[(\widehat Y-Y_{\rm new})^2]$ has a random future observation as its target and includes irreducible outcome noise.{{cite:casella_berger2002}} (Ch. 7, §7.3.1, p. 330, Definition 7.3.1){{cite:gelman_bda2013}} (Ch. 7, §7.1, pp. 166–167)

## Interpretation
The normal-variance and uniform-maximum examples show that bias can improve MSE. Their conclusions attach to their particular models and target values; they do not establish a universal preference for biased estimators. When comparing estimators, graphing $\operatorname{MSE}_\theta$ across plausible $\theta$ values exposes where each wins. For predictions, evaluate errors on new data or a valid held-out design: averaging squared residuals on the same data used to fit a flexible model understates future risk.{{cite:gelman_bda2013}} (Ch. 7, §7.1, pp. 166–167)

## Properties
The decomposition $\operatorname{MSE}_\theta(T)=\operatorname{Var}_\theta(T)+\operatorname{Bias}_\theta(T)^2$ follows by centering at $E_\theta T$. Both terms are nonnegative, but the split is defined only when the relevant moments exist. For a future response $Y_{\rm new}=m(x)+\varepsilon$ with conditional mean-zero noise of variance $\sigma^2(x)$, a fixed prediction $a$ has conditional expected squared error $(a-m(x))^2+\sigma^2(x)$. Thus the conditional mean minimizes expected squared prediction error, while the noise variance cannot be removed by choosing a better point prediction.{{cite:casella_berger2002}} (Ch. 7, §7.3.1, p. 330, (7.3.1)){{cite:gelman_bda2013}} (Ch. 7, §7.1, pp. 166–167)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Write $T-\theta=(T-E_\theta T)+(E_\theta T-\theta)$. Squaring and taking expectations, the cross term vanishes because $E_\theta(T-E_\theta T)=0$, leaving variance plus squared bias. The same expansion with $Y_{\rm new}$ centred at $m(x)$ proves the prediction formula. For the binomial example below, $E_pX=4p$ and $\operatorname{Var}_pX=4p(1-p)$. Hence $X/4$ has MSE $p(1-p)/4$. For $(X+1)/6$, the bias is $(1-2p)/6$ and the variance is $p(1-p)/9$; their sum is $[4p(1-p)+(1-2p)^2]/36=1/36$.{{cite:casella_berger2002}} (Ch. 7, §7.3.1, p. 330, (7.3.1))
:::
:::

## Statistical use — Comparing estimators
Choose the target, loss and reference sampling model before comparing MSEs. Compute exact expectations where possible, or use simulation and disclose the parameter values used. For a fitted prediction rule, estimate out-of-sample squared error using independent test cases or a resampling procedure that refits the full rule. Report units as well: MSE has squared units of the target, whereas its square root returns the original units. A low average squared error may still conceal rare large failures or unequal costs, in which case a different loss is needed.{{cite:gelman_bda2013}} (Ch. 7, §7.1, pp. 166–167)

## Worked example
Let $X\sim\operatorname{Bin}(4,p)$. Compare the raw fraction $T_0=X/4$ with the smoothed fraction $T_1=(X+1)/6$, which is also the posterior mean under a uniform $\operatorname{Beta}(1,1)$ prior. The proof gives $\operatorname{MSE}_p(T_0)=p(1-p)/4$ and $\operatorname{MSE}_p(T_1)=1/36\approx0.02778$ for every $p$. At $p=0.5$, the raw fraction has MSE $0.0625$, so smoothing reduces it. At $p=0.1$, the raw fraction has MSE $0.0225$, so smoothing raises it. The uniform prior supplies a rule for making $T_1$; the MSE comparison here treats $p$ as fixed and averages over repeated binomial samples.{{cite:gelman_bda2013}} (Ch. 2, §§2.1 and 2.4, pp. 31–32, 35; Ch. 4, §4.4, p. 92)

**Your turn.** In the same four-trial model, compare the two MSEs when $p=0.25$. Which estimator wins at this parameter value?

::: {.callout-tip collapse="true" title="Answer"}
For $T_0$, $p(1-p)/4=(0.25)(0.75)/4=0.046875$. For $T_1$, the MSE is $1/36\approx0.02778$. The smoothed estimator wins at $p=0.25$, although the ranking reverses at sufficiently small or large $p$.
:::

## Common misconceptions
A single squared residual is a realised error, not an expected error across repeated samples. A posterior mean's minimum *posterior* squared loss conditions on observed data and averages over a parameter distribution; frequentist MSE fixes the parameter and averages over data. A smaller training MSE is not evidence of smaller error on new cases, especially after a complex model has been chosen from those same cases.{{cite:gelman_bda2013}} (Ch. 4, §4.4, p. 92; Ch. 7, §7.1, pp. 166–167)

## Assumptions and limits — When MSE is undefined or the wrong criterion
For a Cauchy observation used directly to estimate its location, $E[(X-\theta)^2]$ diverges, so finite MSE rankings do not exist for that estimator. In a flood-risk application where underprediction is costlier than overprediction, symmetric squared loss may optimize the wrong decision even if its expectation is finite. If a predictive model is evaluated only on its training sample, a more flexible fit can appear better through overfitting while predicting new cases worse. Each issue requires checking the distribution, the target or the loss rather than merely recomputing an arithmetic average.{{cite:gelman_bda2013}} (Ch. 7, §7.1, pp. 166–167)

## Connections
[Bias](bias-of-an-estimator.qmd) and [variance](variance.qmd) are the two nonnegative terms in the decomposition, and root mean squared error restores the target's units. The [Poisson-mean question](../questions/ex-inf-poisson-mle.qmd) uses unbiasedness to identify mean squared error with variance. [Posterior mean under squared loss](../questions/ex-applied-mmse.qmd) minimises a conditional Bayes risk, which fixes the data and averages over the parameter.{{cite:casella_berger2002}} (Ch. 7, §7.3.1, p. 330)

## History
Legendre's 1805 least-squares method minimized *observed* squared residuals in an astronomical fitting problem. The later MSE criterion judges an estimator by the *expected* squared distance to a target over repeated samples, including both variance and squared bias. Distinguishing observed squared residuals from expected squared error still matters when a close fit is mistaken for accurate estimation or prediction.{{cite:dodge2008}} (pp. 304–305, “Least-Squares Method”; p. 337, “Mean Squared Error”)
