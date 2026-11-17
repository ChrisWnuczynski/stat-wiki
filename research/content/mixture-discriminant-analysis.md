## Motivating example
A class of objects can contain two separated subtypes while a second class occupies the space between them. One normal density per class compresses that structure into a centre and covariance. A mixture instead represents subgroups within each observed class and combines their densities before classification. The class label is observed during training; the component label within a class is latent. Confusing the two labels would turn a supervised classification problem into a different clustering problem.{{cite:hastie_tibshirani1996_mda}} (§2, pp. 158–159)

## Definition — Sum subclass densities within each class
Let $G$ denote the observed class and $H$ a latent subclass. A Gaussian mixture model for class $g$ has density $f_g(x)=\sum_{h=1}^{H_g}\lambda_{gh}\phi_p(x;\mu_{gh},\Sigma)$, with nonnegative weights summing to one within each class. In the canonical mixture discriminant analysis formulation, the covariance $\Sigma$ is common to all subclasses and all classes. Each subclass has its own mean. The class prior $\pi_g=\Pr(G=g)$ is distinct from the within-class weight $\lambda_{gh}=\Pr(H=h\mid G=g)$.{{cite:hastie_tibshirani1996_mda}} (§2, eq. 1, p. 158)

Bayes' formula gives $\Pr(G=g\mid x)=\pi_g f_g(x)/\sum_j\pi_j f_j(x)$. Under equal misclassification costs, choose the largest posterior probability, equivalently the largest weighted class density. Crucially, all subclass densities are summed within a class. Choosing the single most probable subclass can give a different class decision. A mixture's marginal density is produced by summing out its latent discrete variable.{{cite:wainwright_jordan2008}} (§3.3, Gaussian mixtures, eq. 3.15, pp. 46–47)

## Properties — Fit latent subclasses without changing observed labels
For training observations $x_i$ whose class labels are $g_i$, the log-likelihood contains $\sum_i\log\sum_h\lambda_{g_i h}\phi_p(x_i;\mu_{g_i h},\Sigma)$. The E step computes responsibilities
$$r_{ih}=\frac{\lambda_{g_i h}\phi_p(x_i;\mu_{g_i h},\Sigma)}{\sum_l\lambda_{g_i l}\phi_p(x_i;\mu_{g_i l},\Sigma)}.$$
Only subclasses of the observation's known class enter this denominator. Write $N_{gh}=\sum_{i:g_i=g}r_{ih}$. The M step updates $\lambda_{gh}=N_{gh}/n_g$ and $\mu_{gh}=\sum_{i:g_i=g}r_{ih}x_i/N_{gh}$. The common covariance is the pooled responsibility-weighted residual matrix, divided by the total sample size.{{cite:hastie_tibshirani1996_mda}} (§2, eqs. 2–6, pp. 158–159)

These equations have a simple weighted-fitting interpretation: an observation contributes fractionally to several subclasses, but its contributions sum to one within its class. EM increases the conditional training likelihood when its expectation and maximisation steps are exact. This ascent guarantee does not choose a globally best fit or a suitable number of subclasses. Several initialisations and validation of predictive performance address different parts of those problems.{{cite:wainwright_jordan2008}} (§6.2, EM variational formulation, pp. 153–156)

## Worked example — A class decision with two boundaries
In one dimension let class A have density $f_A(x)=\tfrac12\phi(x;-2,1)+\tfrac12\phi(x;2,1)$ and class B have density $f_B(x)=\phi(x;0,1)$. Give the two classes equal prior probabilities. All component variances are one, so this example satisfies the common-covariance formulation.

At zero, $f_A(0)/f_B(0)=e^{-2}$, giving $\Pr(A\mid0)=1/(1+e^2)\approx0.119203$: choose B. At two, $f_A(2)\approx0.199538055$ and $f_B(2)\approx0.053990967$, giving $\Pr(A\mid2)\approx0.787042$: choose A. A common component variance therefore does not force a linear class boundary once a class has several components.

Indeed, dividing each shifted normal density by the central density gives $f_A(x)/f_B(x)=e^{-2}\cosh(2x)$. Equal-prior decision boundaries solve $\cosh(2x)=e^2$, so they are $x=\pm\tfrac12\operatorname{arcosh}(e^2)\approx\pm1.344268$. Class B occupies the interval between them; class A occupies both tails. The nonlinear boundary arises from summing the two subclass densities.

**Your turn.** Keep these densities but set the class priors to $\pi_A=3/4$ and $\pi_B=1/4$. Which class is selected at zero?

::: {.callout-tip collapse="true" title="Answer"}
The posterior odds for A are $3e^{-2}\approx0.406006$, below one, so B is still selected. The posterior probability for A is $3/(e^2+3)\approx0.288765$.
:::

## Interpretation — Separate covariance constraints from component counts
With one subclass per class, a common covariance gives LDA. Allowing a separate covariance for each class then gives QDA; that is a broader Gaussian class-mixture model rather than the canonical common-covariance restriction. Component-specific covariances permit still more flexibility and require correspondingly more stable estimation. The covariance restriction and the subclass counts are separate modelling choices.{{cite:hastie_tibshirani1996_mda}} (§2, p. 158; §2.1, p. 160)

Adding subclasses can improve training fit without improving classification on new observations. Tiny subclasses and nearly singular covariance estimates signal that the fitted model may be using more detail than the data support. Initial centres also affect the local EM solution. Select tuning choices using held-out or cross-validated prediction, and estimate a final error rate on observations unused for selecting them. The common-covariance model can share information across small subclasses, but it does not make an arbitrarily large subclass count reliable.{{cite:hastie_tibshirani1996_mda}} (§2.1, implementation and initialisation, p. 160)
