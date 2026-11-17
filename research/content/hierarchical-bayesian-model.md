## Motivating example

A course has many tutorial classes, some with a hundred students and others with only two. A separate mean for every class respects possible differences, but a mean based on two marks is noisy. One common mean for all classes ignores real variation. A hierarchical Bayesian model gives each class its own mean and learns a population distribution for those means, so small classes can use information from the whole course without being forced to match it exactly.

## Intuition — Why partial pooling follows from shared parameters

The levels describe distinct sources of variation. Marks vary between students within a class; class means vary across classes; the overall location and spread of class means are uncertain too. Data from one class change the inferred population distribution, which in turn changes what is plausible for other classes. This is partial pooling.{{cite:gelman_bda2013}} (Ch. 5, §§5.1–5.3, pp. 101–110) It is most visible for a class with little data because its own mean has low precision.

Sharing depends on the model, not merely on putting parameters in layers. The classes must be comparable after relevant differences have been represented. If one class uses a different examination, its marks may not be exchangeable with the rest on a common scale. A hierarchical model can include curriculum or instructor effects, but a misspecified population distribution can pull an unusual class in the wrong direction.

## Definition

In a simple normal hierarchy, $Y_{ij}\mid\theta_j,\sigma^2\sim N(\theta_j,\sigma^2)$ for student $i$ in class $j$, while $\theta_j\mid\mu,\tau^2\sim N(\mu,\tau^2)$. The within-class variance $\sigma^2$ describes scatter of individual marks; the between-class variance $\tau^2$ describes genuine variation in class means. Priors on $\mu$, $\tau^2$ and any unknown $\sigma^2$ complete a full Bayesian model. Conditional independence at one level does not make the class outcomes marginally independent after common uncertain quantities are integrated out.{{cite:gelman_bda2013}} (Ch. 5, §§5.1–5.3, pp. 101–110)

This normal example is one member of a broader family. In the rat-tumour example, each study has a binomial count with its own risk $\theta_j$, and the risks share a Beta population distribution with uncertain shape parameters. The scientific meaning of a level and the adequacy of its distribution matter more than whether conjugacy makes the algebra short.

## Properties

For known $\mu$, $\tau^2$ and $\sigma^2$, the class mean has sampling variance $\sigma^2/n_j$. The posterior precision for $\theta_j$ is the sum $n_j/\sigma^2+1/\tau^2$. Hence its posterior mean is $w_j\overline y_j+(1-w_j)\mu$ with $w_j=n_j\tau^2/(\sigma^2+n_j\tau^2)$. More students increase $w_j$ toward one; a smaller between-class variance pulls it toward zero. These limits describe the balance between within-class information and the common population level.

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Multiplying the normal likelihood for $\overline y_j$ by the $N(\mu,\tau^2)$ population density gives an exponent proportional to $-\tfrac12\{n_j(\theta_j-\overline y_j)^2/\sigma^2+(\theta_j-\mu)^2/\tau^2\}$. Completing the square yields posterior precision $A_j=n_j/\sigma^2+1/\tau^2$, mean $(n_j\overline y_j/\sigma^2+\mu/\tau^2)/A_j$, and variance $1/A_j$. Algebra gives the displayed weighted mean. For the binomial–Beta hierarchy, multiplication of $\theta_j^{y_j}(1-\theta_j)^{n_j-y_j}$ by $\theta_j^{\alpha-1}(1-\theta_j)^{\beta-1}/B(\alpha,\beta)$ gives the Beta$(y_j+\alpha,n_j-y_j+\beta)$ conditional. Integrating this product over $\theta_j$ yields $\binom{n_j}{y_j}B(y_j+\alpha,n_j-y_j+\beta)/B(\alpha,\beta)$; multiplying over studies and by the hyperprior gives the displayed hyperposterior kernel after factors constant in $\alpha,\beta$ are dropped. The law of total variance, obtained by expanding $\theta_j-\mathbb E(\theta_j\mid y)$ around $\mathbb E(\theta_j\mid\alpha,\beta,y)$, separates average conditional variance from uncertainty in the conditional mean due to the hyperparameters.
:::
:::

## Interpretation

The two figures address different parts of inference. The hyperposterior contours show where plausible shared Beta shape parameters lie and whether the numerical grid clips appreciable mass. The shrinkage plot compares each raw study rate with its posterior median, making the larger movements of noisy small studies visible. Neither figure proves exchangeability. A plot of between-group residuals or a sensitivity analysis can reveal whether scientifically distinct groups need predictors or separate population distributions.

In a full Bayesian analysis, uncertainty about the population distribution propagates into each group-specific posterior. A plug-in calculation that fixes hyperparameters omits the second component of the law of total variance. It does not follow that every full-Bayes credible interval is numerically wider than every plug-in interval: their centres and conditional spread can change as well. The comparison must be made for the actual model and data.

## Statistical use

Start by defining which groups plausibly share a population distribution and which measured features distinguish them. Fit the hierarchy with priors that allow credible between-group variation, then inspect the posterior of that variation rather than reporting only the group means. In the rat-tumour analysis, the transformed two-dimensional hyperparameter grid is practical, but its boundary must enclose the important posterior mass. A grid clipped through a contour gives misleading numerical summaries even when its plotted centre looks reasonable. With many uncertain higher-level parameters, simulation methods replace a dense grid.

If one class takes a harder examination, its lower mean may reflect a different scale rather than a random draw from the same population of class means. A single narrow normal population distribution can over-shrink a genuinely exceptional class. In the cattle meta-analysis, missing small or null studies can bias the set of observed effects before any hierarchy is fitted. In the rat-tumour grid, a boundary cutting through the hyperposterior can distort posterior medians and intervals. These failures concern comparability, population shape, selection and computation separately.
## Worked example

Suppose the population class mean is $\mu=70$, the within-class standard deviation is $\sigma=10$, and the between-class standard deviation is $\tau=5$. Class A has $n_A=100$ students with sample mean $75$, giving $w_A=100(25)/(100+100(25))=25/26\approx0.9615$ and posterior mean $(25/26)75+(1/26)70\approx74.81$. Class B has only $n_B=2$ students with sample mean $95$, giving $w_B=2(25)/(100+2(25))=1/3$ and posterior mean $(1/3)95+(2/3)70\approx78.33$. B's raw mean exceeds A's by $20$, but their posterior means differ by only about $3.53$. B remains higher; it simply moves much further toward the population centre. These calculations condition on the population parameters being known.

**Your turn.** With $\mu=50$, $\sigma=10$ and $\tau=5$, a class has mean $60$. Find its posterior mean and variance first when $n=4$, then when $n=16$, treating all population parameters as fixed. Explain the direction of the change.

::: {.callout-tip collapse="true" title="Answer"}
For $n=4$, $w=4(25)/(100+4(25))=1/2$, so the posterior mean is $55$ and variance $100(25)/(100+4(25))=12.5$. For $n=16$, $w=16(25)/(100+16(25))=4/5$, so the mean is $58$ and variance $100(25)/(100+16(25))=5$. More observations make the class's own mean more influential and reduce its posterior uncertainty, conditional on the fixed population parameters.
:::

## Common misconceptions

Partial pooling does not replace every group estimate by the overall average; the amount of movement depends on its sample size and estimated between-group variation. Conditional independence given shared hyperparameters does not imply independence after those hyperparameters are integrated out. A hyperprior is not a decoration in full Bayes: its uncertainty affects the group posteriors. Nor does a visually convincing shrinkage plot establish that the groups are scientifically exchangeable.

## Connections

[Exchangeability](exchangeability.qmd) is the modelling claim behind a shared population distribution. [Normal hierarchical shrinkage](normal-hierarchical-shrinkage.qmd) gives the conditional normal calculation, and [complete pooling, no pooling, and partial pooling](complete-pooling-no-pooling-and-partial-pooling.qmd) compare the limiting strategies. A [random-intercept model](random-intercept-model.qmd) has a similar structure in a regression setting, while [posterior summaries from draws](posterior-summaries-from-draws.qmd) turn a fitted hierarchy into reported group estimates.

## History

Bayes's 1763 essay, published after his death through Richard Price, is part of the history of updating uncertain quantities from observations.{{cite:dodge2008}} (p. 32, “Bayes, Thomas”) Hierarchical models extend that updating to related group parameters and their uncertain population distribution.
