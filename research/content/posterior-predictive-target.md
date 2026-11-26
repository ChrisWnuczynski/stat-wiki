## Motivating example
A posterior for a machine's defect probability describes uncertainty about a parameter. A prediction for the number of defective items in tomorrow's batch must also include the batch's sampling variation. Drawing a parameter and reporting that draw as a future observation omits this second source of variation. A posterior predictive target specifies the random observable to which the prediction refers.{{cite:downey2020_thinkbayes2}} (Ch. 8, “Predicting the Rematch”)

## Definition — Integrate the sampling law over the posterior
Given data $D$ and parameters $\theta$, a future observable $\widetilde Y$ has predictive law
$$p(\widetilde y\mid D)=\int p(\widetilde y\mid\theta,D)p(\theta\mid D)\,d\theta.$$
When the future observation is conditionally independent of the observed data given the parameters and supplied predictors, the first factor reduces to the sampling model for that future observation. Dependence from a shared latent effect or a time-series state must remain in that factor; conditional independence should be stated rather than presumed.{{cite:goodfellow_bengio_courville2016}} (§§3.4, 3.7, 3.11, marginalisation, conditional independence and Bayes' rule){{cite:downey2020_thinkbayes2}} (Ch. 8, posterior predictive mixture)

The prediction target also includes exposure, sample size and the identity of any grouping unit. A new outcome for an observed subject and a new outcome for a new subject can require different latent-effect integrations. Likewise, predicting the mean of a future batch differs from predicting a single item even if both use the same posterior parameter draws. Specifying that target precedes choosing a numerical algorithm.

## Properties — Two components of predictive variance
If the necessary second moments exist, conditioning on the parameter gives
$$\operatorname{Var}(\widetilde Y\mid D)=\E\{\operatorname{Var}(\widetilde Y\mid\theta,D)\mid D\}+\operatorname{Var}\{\E(\widetilde Y\mid\theta,D)\mid D\}.$$
To verify the identity, write $\E(\widetilde Y^2\mid\theta,D)=\operatorname{Var}(\widetilde Y\mid\theta,D)+[\E(\widetilde Y\mid\theta,D)]^2$, average over the posterior and subtract the squared predictive mean. The first term describes variation of future observations at fixed parameters; the second describes uncertainty about their conditional mean.{{cite:goodfellow_bengio_courville2016}} (§3.8, expectation and variance)

This decomposition also explains why substituting the posterior mean parameter into the sampling distribution can misrepresent a prediction. A nonlinear mean function need not commute with posterior averaging, and even where it does, its plug-in predictive variance can omit parameter uncertainty. Exact integration, quadrature and nested simulation all target the same mixture when they implement the same model.{{cite:downey2020_thinkbayes2}} (Ch. 8, mixture construction)

## Worked example — Predict a batch, rather than its probability
Suppose $\theta\mid D\sim\operatorname{Beta}(3,9)$ and $K\mid\theta,D\sim\operatorname{Binomial}(4,\theta)$ for a new four-item batch. The posterior mean is $\E\theta=0.250$ and variance is $\operatorname{Var}\theta=3/208=0.014423$. Integrating the binomial mass gives
$$P(K=k\mid D)=\binom4k\frac{B(3+k,9+4-k)}{B(3,9)},\quad k=0,\ldots,4.$$
The predictive mean is $1.000$ and variance is $0.923077$. In contrast, a binomial distribution at the plug-in probability $0.25$ has variance $0.750$. The beta posterior and its conjugate update supply the ingredients, and the displayed predictive mass follows by integrating the beta density.{{cite:downey2020_thinkbayes2}} (Ch. 18, “Binomial Likelihood”)

The probability that every item is nondefective is $P(K=0\mid D)=0.362637$. Plugging $0.25$ into $(1-\theta)^4$ gives $0.316406$. The difference is a consequence of averaging a nonlinear quantity over parameter uncertainty. It should not be interpreted as a universal direction of predictive error for every possible event or model.

**Your turn.** Predict just one future binary item under the same posterior. Give its success probability and variance.

::: {.callout-tip collapse="true" title="Answer"}
The predictive distribution is Bernoulli with success probability $\E(\theta\mid D)=0.250$. Its variance is $0.25(1-0.25)=0.187500$. For one binary item, integrating the probability still yields a Bernoulli law.
:::

## Statistical use — Simulate both levels of uncertainty
One posterior predictive draw can be obtained by drawing $\theta^{(s)}$ from the posterior and then drawing $\widetilde Y^{(s)}$ from its conditional sampling distribution. Repeating only the first step estimates parameter uncertainty; repeating only the second step at a single estimate gives a plug-in prediction. For dependent posterior draws, predictive Monte Carlo summaries also require an assessment of dependence and numerical precision.{{cite:downey2020_thinkbayes2}} (Ch. 8, predictive distributions)

A predictive interval describes uncertainty under the full assumed model. A narrow interval can still miss tomorrow's batch when the batch differs systematically from the observed data, when the exposure is misrecorded, or when dependence has been left out of the sampling factor. A conditional prediction states the predictors and the exposure at which it is calculated, including any extrapolation beyond the observations used to estimate the model.

## Interpretation — The beta-binomial probabilities are an average of binomial probabilities
With $\theta\mid D\sim\operatorname{Beta}(3,9)$ and $K\mid\theta\sim\operatorname{Binomial}(4,\theta)$, the predictive masses are
$$
\begin{align*}
P(K=0\mid D)&=0.362637,\\
P(K=1\mid D)&=0.362637,\\
P(K=2\mid D)&=0.197802,\\
P(K=3\mid D)&=0.065934,\\
P(K=4\mid D)&=0.010989.
\end{align*}
$$
They sum to one. The mean $\sum k\,P(K=k\mid D)=1.000$ equals $4\E(\theta\mid D)=4\times0.250$, because the conditional binomial mean is linear in $\theta$ and the average passes inside. A plug-in binomial at $\theta=0.25$ has masses $0.316406$, $0.421875$, $0.210938$, $0.046875$, $0.003906$ for $k=0,\ldots,4$. The mixture puts more probability on $k=0$ and on $k=4$ than the plug-in does, which is the visible trace of uncertainty in $\theta$.{{cite:downey2020_thinkbayes2}} (Ch. 18, “Binomial Likelihood”)

The variance decomposition accounts for the same spread. The conditional variance is $4\theta(1-\theta)$, and its posterior expectation is $0.692308$. The conditional mean is $4\theta$, and the posterior variance of that mean is $16\operatorname{Var}(\theta)=16\times0.014423=0.230769$. Adding these pieces gives $0.923077$, the predictive variance. The plug-in binomial variance $4\times0.25\times0.75=0.750$ sits near the first piece and leaves out the second. For a single future binary item the conditional variance is $\theta(1-\theta)$ and the conditional mean is $\theta$; after averaging, the predictive law is Bernoulli with success probability $0.250$ and variance $0.187500$. Two future items that share one draw of $\theta$ are dependent under the predictive law, because the covariance $\operatorname{Var}(\theta)$ is positive, while they are independent given $\theta$.{{cite:goodfellow_bengio_courville2016}} (§3.8, expectation and variance)

## Intuition — Name the observable, then average its sampling distribution
A posterior draw of $\theta$ is a draw of a defect probability. A posterior predictive draw of the batch count is a draw of $\theta$ followed by a draw of $K$ from $\operatorname{Binomial}(4,\theta)$. Stopping after the first step answers a question about the machine. Taking both steps answers a question about tomorrow's four items. The same posterior can feed either question, and the numerical summaries differ: the posterior variance of $\theta$ is $0.014423$, while the predictive variance of $K$ is $0.923077$.

The integral $p(\widetilde y\mid D)=\int p(\widetilde y\mid\theta)\,p(\theta\mid D)\,d\theta$ is the definition once $\widetilde Y$ is conditionally independent of the data given $\theta$. A shared random effect or a time-series state stays inside $p(\widetilde y\mid\theta,D)$. For a new subject the random effect is drawn from its population distribution; for another measurement on a subject already observed, the random effect is drawn from its conditional distribution given that subject's data. Those two predictive targets use different sampling factors and the same posterior for the shared parameters.

## Common misconceptions
The posterior mean $0.250$ is a summary of $\theta$. Substituting it into $(1-\theta)^4$ produces $0.316406$, whereas $P(K=0\mid D)=0.362637$. The gap is the difference between a nonlinear function of the mean and the mean of the nonlinear function. Jensen's inequality for the convex map $\theta\mapsto(1-\theta)^4$ on $(0,1)$ places the plug-in probability below the predictive probability in this particular case. A different event can bend the other way. The reliable operation is to average the conditional probability, which is what the beta function ratio does.

Simulation that redraws only $\theta$, or only $K$ at a frozen $\theta$, estimates one layer of the hierarchy. The full predictive sample redraws both. Monte Carlo error in a finite simulation is an additional uncertainty about the numerical estimate, on top of the predictive uncertainty the sample is trying to represent.{{cite:downey2020_thinkbayes2}} (Ch. 8, predictive distributions)
