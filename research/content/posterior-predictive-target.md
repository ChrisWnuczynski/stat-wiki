## Motivating example
A posterior for a machine's defect probability describes uncertainty about a parameter. A prediction for the number of defective items in tomorrow's batch must also include the batch's sampling variation. Drawing a parameter and reporting that draw as a future observation omits this second source of variation. A posterior predictive target specifies the random observable to which the prediction refers.{{cite:downey2020_thinkbayes2}} (Ch. 8, “Predicting the Rematch”)

## Definition — Integrate the sampling law over the posterior
Given data $D$ and parameters $\theta$, a future observable $\widetilde Y$ has predictive law
$$p(\widetilde y\mid D)=\int p(\widetilde y\mid\theta,D)p(\theta\mid D)\,d\theta.$$
When the future observation is conditionally independent of the observed data given the parameters and supplied predictors, the first factor reduces to the sampling model for that future observation. Dependence from a shared latent effect or a time-series state must remain in that factor; conditional independence should be stated rather than presumed.{{cite:goodfellow_bengio_courville2016}} (§§3.4, 3.7, 3.11, marginalisation, conditional independence and Bayes' rule){{cite:downey2020_thinkbayes2}} (Ch. 8, posterior predictive mixture)

The prediction target also includes exposure, sample size and the identity of any grouping unit. A new outcome for an observed subject and a new outcome for a new subject can require different latent-effect integrations. Likewise, predicting the mean of a future batch differs from predicting a single item even if both use the same posterior parameter draws. Specifying that target precedes choosing a numerical algorithm.

## Properties — Two components of predictive variance
If the necessary second moments exist, conditioning on the parameter gives
$$\operatorname{Var}(\widetilde Y\mid D)=E\{\operatorname{Var}(\widetilde Y\mid\theta,D)\mid D\}+\operatorname{Var}\{E(\widetilde Y\mid\theta,D)\mid D\}.$$
To verify the identity, write $E(\widetilde Y^2\mid\theta,D)=\operatorname{Var}(\widetilde Y\mid\theta,D)+[E(\widetilde Y\mid\theta,D)]^2$, average over the posterior and subtract the squared predictive mean. The first term describes variation of future observations at fixed parameters; the second describes uncertainty about their conditional mean.{{cite:goodfellow_bengio_courville2016}} (§3.8, expectation and variance)

This decomposition also explains why substituting the posterior mean parameter into the sampling distribution can misrepresent a prediction. A nonlinear mean function need not commute with posterior averaging, and even where it does, its plug-in predictive variance can omit parameter uncertainty. Exact integration, quadrature and nested simulation all target the same mixture when they implement the same model.{{cite:downey2020_thinkbayes2}} (Ch. 8, mixture construction)

## Worked example — Predict a batch, rather than its probability
Suppose $\theta\mid D\sim\operatorname{Beta}(3,9)$ and $K\mid\theta,D\sim\operatorname{Binomial}(4,\theta)$ for a new four-item batch. The posterior mean is $E\theta=0.250$ and variance is $\operatorname{Var}\theta=3/208=0.014423$. Integrating the binomial mass gives
$$P(K=k\mid D)=\binom4k\frac{B(3+k,9+4-k)}{B(3,9)},\quad k=0,\ldots,4.$$
The predictive mean is $1.000$ and variance is $0.923077$. In contrast, a binomial distribution at the plug-in probability $0.25$ has variance $0.750$. The beta posterior and its conjugate update supply the ingredients, and the displayed predictive mass follows by integrating the beta density.{{cite:downey2020_thinkbayes2}} (Ch. 18, “Binomial Likelihood”)

The probability that every item is nondefective is $P(K=0\mid D)=0.362637$. Plugging $0.25$ into $(1-\theta)^4$ gives $0.316406$. The difference is a consequence of averaging a nonlinear quantity over parameter uncertainty. It should not be interpreted as a universal direction of predictive error for every possible event or model.

**Your turn.** Predict just one future binary item under the same posterior. Give its success probability and variance.

::: {.callout-tip collapse="true" title="Answer"}
The predictive distribution is Bernoulli with success probability $E(\theta\mid D)=0.250$. Its variance is $0.25(1-0.25)=0.187500$. For one binary item, integrating the probability still yields a Bernoulli law.
:::

## Statistical use — Simulate both levels of uncertainty
One posterior predictive draw can be obtained by drawing $\theta^{(s)}$ from the posterior and then drawing $\widetilde Y^{(s)}$ from its conditional sampling distribution. Repeating only the first step estimates parameter uncertainty; repeating only the second step at a single estimate gives a plug-in prediction. For dependent posterior draws, predictive Monte Carlo summaries also require an assessment of dependence and numerical precision.{{cite:downey2020_thinkbayes2}} (Ch. 8, predictive distributions)

A predictive interval describes uncertainty under the full assumed model. It can be narrow and still misleading if tomorrow's batch differs systematically from the observed data, if the exposure is misrecorded or if important dependence has been omitted. A conditional prediction explicitly states the predictors and exposure at which it is calculated, including whether it extrapolates outside the observations used to estimate the model.
