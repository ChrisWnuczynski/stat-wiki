## Motivating example
The TG5 marker study asks whether evidence about a genotype contrast can be combined across cattle populations and marbling measurements. A simple average treats every estimate as equally precise and equally comparable. A multilevel analysis instead distinguishes sampling uncertainty, variation between studies, and variation between breed groups. It can share information while allowing those effects to differ.{{cite:wood_mengersen2006_tg5}} (§2.2, pp. 482–483)

## Interpretation — Collected evidence and modelled evidence
The evidence collection and the fitted data set have different sizes. Fourteen studies were considered and nineteen estimates were available; three studies reported results in a form that was discussed separately. The hierarchical analysis used sixteen standardised effect estimates from eleven studies. Some studies contributed several traits, so an estimate is not interchangeable with an independent study. Four breed groups and four trait definitions supplied additional structure.{{cite:wood_mengersen2006_tg5}} (§§2.1–2.2, pp. 480–483; §4, p. 488)

Standardising an effect by its study's residual standard deviation makes contrasts dimensionless. It does not prove that different measurements identify the same biological quantity. The fitted model groups observations within study and breed, and sensitivity analyses assess changes in gene-action assumptions, precision priors and selected observations. Such checks address particular assumptions; they cannot recover studies that were never located or unreported outcome definitions.{{cite:wood_mengersen2006_tg5}} (§§2.1, 2.4, pp. 481–485)

## Properties — The normal update behind partial pooling
Consider one observed standardised estimate $y$ with sampling variance $v$, and a study effect $\delta$ with conditional prior $N(m,\tau^2)$. Hold $m,\tau^2,v$ fixed and positive. Multiplying the two normal kernels gives posterior precision $1/v+1/\tau^2$ and mean
$$m_* =\frac{y/v+m/\tau^2}{1/v+1/\tau^2}.$$
This follows by expanding $(y-\delta)^2/v+(\delta-m)^2/\tau^2$ and completing the square in $\delta$. The coefficient on $y$ is $\tau^2/(v+\tau^2)$, so a noisy estimate receives less weight. The TG5 hierarchy uses related conditional normal layers from observed contrast to study, breed and overall effect.{{cite:wood_mengersen2006_tg5}} (§2.2, pp. 482–483)

Conditional normal calculations do not require marginal posteriors to be normal. Uncertainty in the higher-level means and precisions must also be integrated. In particular, making a prior broad on one variance scale need not make it weak on another. The choice can matter when the number of independent groups is small.{{cite:gelman2006}} (§§1.1–2.3, pp. 516–517)

## Worked example — A schematic study-level update
Suppose a standardised estimate is $y=0.30$ with standard error $0.20$, and a fixed breed-level prior is $N(0.10,0.10^2)$. These are illustrative inputs, rather than a refit of the cattle data. Sampling precision is $25$ and prior precision is $100$. The conditional posterior mean is $(25\times0.30+100\times0.10)/125=0.14$, and its variance is $1/125=0.008$. Its standard deviation is approximately $0.089443$. The data weight is $25/125=0.2$.

A second estimate with the same value but standard error $0.10$ has sampling precision $100$. Its posterior mean is $0.20$ and its variance is $0.005$. The estimate with greater sampling precision moves the posterior further from the prior centre. This calculation explains the mechanics of partial pooling, but a full multilevel fit must also update the centre and dispersion.

**Your turn.** Keep the first estimate and sampling variance, but set the prior mean to $0$. What is its conditional posterior mean?

::: {.callout-tip collapse="true" title="Answer"}
It is $(25\times0.30+100\times0)/125=0.06$. The conditional posterior variance stays $0.008$.
:::

## Assumptions and limits — Several estimates can share animals
When subsets of animals overlap, two effect estimates can have nonzero sampling covariance. For the TG5 analysis, overlap information was insufficient to incorporate those covariances, and diagonal precision structures were used. Treating several estimates from one study as independent therefore adds an assumption beyond standardising their units. The consequences concern uncertainty as well as the point estimate. A study with several correlated outcomes should not automatically count as several independent replications.{{cite:wood_mengersen2006_tg5}} (§§2.1–2.2, pp. 482–483; §5, pp. 490–491)

## Connections — Sensitivity belongs to the scientific analysis
A positive posterior shift describes an association under the selected model and evidence set. It does not identify the effect of changing a genotype in a different breed or management environment. Comparing assumptions about dominance, excluding sparse genotype cells and checking posterior predictive summaries are concrete ways to assess dependence on the model. They complement, rather than replace, scrutiny of how studies and measurements entered the analysis.{{cite:wood_mengersen2006_tg5}} (§2.4, pp. 484–485)

## Statistical use — Precision, not the raw estimate, sets the conditional weight
For $y=0.30$ with sampling variance $0.20^2=0.04$, the sampling precision is $25$. A normal prior centred at $0.10$ with variance $0.01$ has precision $100$. The conditional posterior precision is $125$, the mean is $(25\times0.30+100\times0.10)/125=0.14$, and the variance is $0.008$. The data weight is $0.2$. Replacing the prior mean by $0$ changes the mean to $(25\times0.30+100\times0)/125=0.06$ and leaves the variance at $0.008$. The prior still supplies four times the precision of the estimate. A second estimate with the same value $0.30$ and standard error $0.10$ has sampling precision $100$, posterior mean $(100\times0.30+100\times0.10)/200=0.20$ and variance $0.005$. Equal precision splits the difference between $0.30$ and $0.10$.{{cite:wood_mengersen2006_tg5}} (§2.2, pp. 482–483)

The published evidence set is larger than one estimate and smaller than a pile of independent studies. Fourteen studies were considered and nineteen estimates were available. The hierarchical analysis used sixteen standardised estimates from eleven studies. Four estimates from one study remain four rows inside one study. They can share animals, and the analysis did not have the overlap information needed to fill the off-diagonal sampling covariances. Counting those four rows as four independent studies would overstate the number of independent breed-level contributions.{{cite:wood_mengersen2006_tg5}} (§§2.1–2.2, pp. 480–483; §5, pp. 490–491)

### Interpretation — Standardising the contrast does not identify the trait
Dividing a genotype contrast by the study's residual standard deviation removes the original measurement unit. Two standardised estimates can then be entered in one normal model. The division does not show that marbling recorded in one way is the same biological target as marbling recorded in another. The fitted hierarchy groups rows by study and by breed and then states a distribution for those standardised numbers. A sensitivity check that changes the precision prior, or that drops a sparse genotype cell, answers a specific stability question about that fitted distribution. It does not restore an estimate that was never reported, and it does not turn a posterior shift into an effect of altering a genotype under a new management regime.{{cite:wood_mengersen2006_tg5}} (§§2.1, 2.4, pp. 481–485)

### Assumptions and limits — The normal update is conditional on the higher-level parameters
The square-completion formula treats $m$, $\tau^2$ and $v$ as fixed. In the hierarchy those quantities have their own uncertainty, and the marginal posterior of a study effect mixes the conditional normals. A plug-in that inserts one estimated prior variance can look more precise than the mixture. The schematic calculation with variance $0.008$ is the conditional variance at the stated prior. It is not a marginal posterior variance for the cattle analysis, and the inputs $0.30$ and $0.20$ were chosen to show the arithmetic rather than to reproduce a published conditional draw.{{cite:gelman2006}} (§§1.1–2.3, pp. 516–517){{cite:wood_mengersen2006_tg5}} (§2.2, pp. 482–483)
