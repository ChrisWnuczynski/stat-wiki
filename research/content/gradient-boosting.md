## Motivating example

A small regression tree may leave a systematic pattern in its prediction errors. Rather than replacing the tree with one large fit, gradient boosting adds a learner that addresses the current loss. The target for that learner depends on the chosen loss function; ordinary residual fitting is the squared-error instance.{{cite:natekin_knoll2013}} (§§2.3–2.4)

## Definition — Fit the negative loss gradient

Let $F_{m-1}$ denote the current score and let $L(y,F)$ be differentiable in its second argument. Compute pseudo-responses
$$r_{im}=-\left.\frac{\partial L(y_i,F)}{\partial F}\right|_{F=F_{m-1}(x_i)}.$$
Fit a base learner $h_m$ to these values, often by least squares, select a step $\gamma_m$ by minimising $\sum_iL(y_i,F_{m-1}(x_i)+\gamma h_m(x_i))$, and update
$$F_m(x)=F_{m-1}(x)+\nu\gamma_m h_m(x),\qquad0<\nu\le1.$$
The fitted learner approximates a direction available in function space. It need not reproduce the negative gradient exactly at every observation.{{cite:natekin_knoll2013}} (§2.4, Algorithm1; §4.2)

## Properties — The loss determines the pseudo-response

For $L=(y-F)^2/2$, the pseudo-response is $y-F$. For Bernoulli log loss with $y\in\{0,1\}$ and $p=(1+e^{-F})^{-1}$, differentiating $\log(1+e^F)-yF$ gives pseudo-response $y-p$. For exponential loss with labels $y\in\{-1,1\}$ it is $ye^{-yF}$. These choices share a stagewise structure but optimize different losses and weight difficult observations differently.{{cite:natekin_knoll2013}} (§§3.1.1–3.1.2)

For squared error, once $h$ is fixed and not identically zero on the sample, exact line search gives $\gamma=\sum_i r_i h(x_i)/\sum_i h(x_i)^2$. A proposed direction with no alignment with the residual can give zero improvement. Increasing ensemble size alone therefore does not prove that any arbitrary sequence of learners reduces the objective.{{cite:natekin_knoll2013}} (§2.4)

## Worked example — Two residual-fitting rounds

Take responses $(0,0,2,2)$ and initialise at their mean $F_0=1$. Suppose a stump separates the first two from the last two observations, fitting residuals $(-1,-1,1,1)$ exactly. With line-search step one and learning rate $\nu=1/2$, the first predictions are $(0.5,0.5,1.5,1.5)$. Average half-squared error decreases from $0.5$ to $0.125$. Fitting the new residuals and taking the same learning rate gives $(0.25,0.25,1.75,1.75)$ and loss $0.03125$. Each round halves the residual and quarters this loss.{{cite:natekin_knoll2013}} (§3.1.1; §4.2)

**Your turn.** For the squared-error example, replace the learning rate $1/2$ by one for the first round. What happens to the training loss?

::: {.callout-tip collapse="true" title="Answer"}
The learner fits every residual exactly, so adding it with step one reproduces $(0,0,2,2)$. The training loss becomes zero. This finite-sample interpolation says nothing by itself about error on fresh observations.
:::

## Connections — AdaBoost as a stagewise exponential-loss calculation

For a fixed binary learner and normalised current weights, its exponential-loss contribution is $(1-\epsilon)e^{-a}+\epsilon e^a$. Differentiation gives $a=\tfrac12\log[(1-\epsilon)/\epsilon]$ for $0<\epsilon<1$. The corresponding reweighting increases the relative influence of misclassified cases. This discrete weighted-error construction is one specific boosting algorithm; the general gradient method can instead fit pseudo-responses for other differentiable losses.{{cite:freund_schapire1997}} (§4.1, pp.125–126, Fig.2)

## Statistical use — Complexity accumulates across rounds

Learning rate, the number of rounds, and base-learner complexity jointly control the fitted function. A smaller learning rate generally requires more rounds to attain a comparable training loss. Holding out data for stopping or tuning assesses predictive behaviour; continuing to reduce training loss alone does not establish improved prediction. The unrestricted population minimiser need not belong to the chosen finite ensemble class.{{cite:natekin_knoll2013}} (§§2.1–2.3; §4.2)


## Check yourself

### [One round of AdaBoost](../questions/ex-sl-13-4.qmd) {#self-check-ex-sl-13-4}

::: {.callout-tip collapse="true" title="Answer"}
One error among five equally weighted observations gives $\epsilon=0.2$ and $a=\log2$. Correct observations receive unnormalised weight $0.1$ each and the error receives $0.4$, with normaliser $0.8$. The resulting weights are $0.125$ for each correct case and $0.5$ for the incorrect case; the same stump then has weighted error $0.5$.
:::

### [How ensemble members differ](../questions/depth-ensemble-mechanism.qmd) {#self-check-depth-ensemble-mechanism}

::: {.callout-tip collapse="true" title="Answer"}
Bagging changes training samples through bootstrap resampling. Random forests also randomise the candidate variables at tree splits. AdaBoost changes observation weights sequentially and combines weighted learners, directing later fits toward cases that the current ensemble handles poorly.
:::
