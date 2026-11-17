## Motivating example
An observation lying between two estimated cluster centers can receive partial membership in both Gaussian components. As a common component variance shrinks, even a modest distance advantage becomes overwhelming evidence for the nearer center. This connects probabilistic mixture fitting with the hard assignments of $K$-means. Gaussian mixture EM uses posterior membership weights when updating means.{{cite:holmes_huber2019_msmb}} (§4.2.2, eq. 4.5 and E/M steps)

## Definition
Fix $K$ component means in $\mathbb R^d$, common covariance $\varepsilon I_d$, and equal positive weights. For squared distances $d_{ih}=\|x_i-\mu_h\|^2$, Bayes' rule gives $\tau_{ih}=e^{-d_{ih}/(2\varepsilon)}/\sum_me^{-d_{im}/(2\varepsilon)}$. Gaussian normalizing factors and common weights cancel. The usual mixture likelihood permits soft membership; $K$-means supplies a one-hot representation assigning an observation to one cluster.{{cite:goodfellow_bengio_courville2016}} (§5.8.2, $k$-means clustering)

## Properties — The limit and the tie case
If observation $i$ has unique nearest center $h_*$, divide numerator and denominator by $e^{-d_{ih_*}/(2\varepsilon)}$. Every other term becomes $e^{-(d_{ih}-d_{ih_*})/(2\varepsilon)}\to0$, proving $\tau_{ih_*}\to1$ and all other memberships tend to zero. If exactly $r$ centers tie for minimum distance, each instead receives limit $1/r$ under equal weights. A deterministic tie-breaking rule is an additional convention, not the soft limit itself. Probabilistic and hard assignments differ at finite variance.{{cite:holmes_huber2019_msmb}} (§5.4.1, question 5.4, soft versus hard membership)

The weighted update $\mu_h'=\sum_i\tau_{ih}x_i/\sum_i\tau_{ih}$ tends to the mean of the assigned observations whenever the limiting cluster is nonempty. For a fixed hard assignment, expanding $\sum_{i\in C}\|x_i-\mu\|^2$ around the cluster mean gives
$$\sum_{i\in C}\|x_i-\mu\|^2=\sum_{i\in C}\|x_i-\bar x_C\|^2+|C|\|\mu-\bar x_C\|^2.$$
Thus the mean minimizes squared distance, and nearest-center assignment minimizes each observation's contribution for fixed centers. Alternating these two minimizations cannot increase the $K$-means objective.{{cite:holmes_huber2019_msmb}} (§5.4.1, iterative relocation and arithmetic means)

## Worked example — A soft assignment sharpens
Take centers 0 and 4 and an observation at 1. Its squared distances are 1 and 9, so membership in the first component is $1/(1+e^{-4/\varepsilon})$. It is $0.88080$ at $\varepsilon=2$, $0.98201$ at $\varepsilon=1$, and $0.99966$ at $\varepsilon=0.5$. At observation 2, both distances are four and each membership remains exactly one half for every positive variance. These values display the limit without conflating near ties with exact ties.{{cite:holmes_huber2019_msmb}} (§4.2.2, posterior membership formula)

**Your turn.** Hard-assign observations $(0,1,5,6)$ to centers $(0,6)$. Compute the next means and the objective before and after the mean update.

::: {.callout-tip collapse="true" title="Answer"}
The groups are $(0,1)$ and $(5,6)$; their new means are $0.5$ and $5.5$. The objective is $0^2+1^2+1^2+0^2=2$ before updating and four contributions of $0.5^2$, totaling 1, afterward.
:::

## Interpretation — A likelihood objective also approaches distortion
For fixed equal weights, dropping terms independent of the means and multiplying negative log-likelihood by $2\varepsilon$ gives a sum of expressions $-2\varepsilon\log\sum_he^{-d_{ih}/(2\varepsilon)}$. If $d_i^*=\min_hd_{ih}$, the sum inside lies between $e^{-d_i^*/(2\varepsilon)}$ and $Ke^{-d_i^*/(2\varepsilon)}$. Hence each expression lies between $d_i^*-2\varepsilon\log K$ and $d_i^*$ and converges to the nearest-center squared distance. This derives the limiting objective directly. The hard representation is the cluster index encoded as a one-hot vector.{{cite:goodfellow_bengio_courville2016}} (§5.8.2)

### Fixed unequal weights and vanishing weights
Equal weights give the displayed expression, but the unique-nearest-center limit also holds for any fixed positive weights $\pi_h$. The ratio of a nonnearest posterior weight to the nearest one becomes $(\pi_h/\pi_{h_*})e^{-(d_{ih}-d_{ih_*})/(2\varepsilon)}$, which still tends to zero. At an exact distance tie, the limiting memberships are proportional to the tied components' weights. This distinction is useful when comparing constrained EM with a mixture fit that also estimates mixing proportions. If weights themselves depend on $\varepsilon$ and vanish exponentially fast, the probability factor can compete with the distance factor and the preceding fixed-weight conclusion need not apply. The membership formula contains both prior mixture weights and component densities.{{cite:holmes_huber2019_msmb}} (§4.2.2, eq. 4.5)

### Monotonicity at a fixed positive variance
The likelihood check for finite-variance EM has a different objective from the limiting distortion. Let $q(u)=p(u\mid x,\theta_t)$ and let $L(\theta)=\log p(x\mid\theta)$ for the full observed sample. Jensen's inequality gives
$$L(\theta)-L(\theta_t)=\log E_q\left[\frac{p(x,u\mid\theta)}{p(x,u\mid\theta_t)}\right]\ge E_q\log\frac{p(x,u\mid\theta)}{p(x,u\mid\theta_t)}=Q(\theta,\theta_t)-Q(\theta_t,\theta_t).$$
Consequently an M step that increases the expected complete-data log-likelihood cannot reduce the observed likelihood, provided the relevant supports and expectations are well-defined. This proves the monotonicity criterion for an exact E step without suggesting that the algorithm finds a global maximum. The expected complete-data objective fixes the current posterior weights during the M step.{{cite:holmes_huber2019_msmb}} (§4.2.2, eq. 4.8–4.9)

## Assumptions and limits
The derivation is pointwise for fixed centers; it does not justify interchanging a variance limit with arbitrarily many EM iterations or guarantee a global optimum. Empty limiting clusters need an explicit algorithmic treatment. Unequal covariances change the distance geometry, and non-spherical groups can be poorly represented by Euclidean clusters. Multiple starts can reveal dependence on initialization but do not prove global optimality.{{cite:holmes_huber2019_msmb}} (§5.4.1, initialization and cluster shape)
