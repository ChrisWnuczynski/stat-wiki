## Motivating example
A sensor measures a concentration that can arise from either of two manufacturing processes. Each process may produce several clusters because it runs at different temperatures. Fitting one bell curve per process can smooth away those clusters. A density classifier instead asks which process assigns the larger local density to the observed concentration, after allowing for how common the processes are. Kernel estimates supply flexible class densities without declaring how many clusters a process has.{{cite:zhang_d2l2023}} (§11.2, Attention Pooling by Similarity)

## Intuition — Local evidence and class frequency
A kernel places a smooth bump around each training observation. The sum of the bumps estimates where a class tends to put its measurements. Dividing by the number of observations in the class turns that sum into a density; multiplying by the class prior then combines local evidence with prevalence. With empirical priors $\widehat\pi_g=n_g/n$ and a common kernel bandwidth, these two factors cancel the class sample size:
$$\widehat\pi_g\widehat f_g(x)=\frac1n\sum_{i:y_i=g}K_H(x-x_i).$$
Thus a common-bandwidth classifier can also be interpreted as a weighted vote, with nearby observations receiving larger weights. Normalising all class scores gives posterior probability estimates. This is the same normalization principle used for kernel classification with one-hot class labels.{{cite:zhang_d2l2023}} (§11.2, Regression and Classification)

The density-estimation kernel and a positive semidefinite kernel used in a support vector machine serve different mathematical roles. Here the kernel must integrate to one after its bandwidth scaling, because each class score comes from a probability density. A Gaussian function can serve in either construction, but that shared shape does not make the procedures interchangeable.{{cite:downey2014_thinkstats2}} (§6.2, Kernel density estimation)

## Properties — Probabilities, costs and bandwidths
For positive total score, Bayes' formula gives
$$\widehat P(Y=g\mid x)=\frac{\pi_g\widehat f_g(x)}{\sum_k\pi_k\widehat f_k(x)}.$$
Choosing the largest posterior minimizes conditional zero–one loss. Indeed, predicting $g$ has conditional error probability $1-\widehat P(Y=g\mid x)$, so maximizing the posterior minimizes that error. With loss $L(a,g)$ for choosing action $a$ when the true class is $g$, choose the action minimizing $\sum_g L(a,g)\widehat P(Y=g\mid x)$ instead. A rare but costly error can therefore change the decision even when the density estimates stay fixed.{{cite:holmes_huber2019_msmb}} (§12.5, Objective functions)

The estimates integrate to one: substitute $v=H_g^{-1/2}(x-x_i)$ in each bump, so the Jacobian $|H_g|^{1/2}$ cancels its scale factor, then average the resulting unit integrals. This justifies comparing densities whose bandwidths differ. Omitting the scale factor would reward a wider bump merely for covering a larger region. Bandwidth controls smoothing; a small value emphasizes nearby measurements, while a large value blends modes together.{{cite:downey2014_thinkstats2}} (§6.2)

For a fixed query and a common Gaussian bandwidth $h\to\infty$, $h\widehat f_g(x)\to\varphi(0)$, hence the estimated posterior tends to the prior. This is a pointwise limit. Equal priors need not produce an exact tie at any finite bandwidth. At $h\to0$, a query different from all observations has densities tending to zero, so numerical underflow is a practical issue; logarithms and stable score normalization help. Neither limit selects a statistically useful bandwidth by itself.{{cite:zhang_d2l2023}} (§11.2, Adapting Attention Pooling)

## Worked example — Reading the density ratio
For the two samples $\{0,1\}$ and $\{4,5\}$ with unit Gaussian bandwidth, the densities at $x=3$ are $0.0292114$ and $0.1479808$. Their ratio is about $5.0659$ in favour of class 2. Equal priors give posterior probability $0.83514$ for class 2. If process 1 accounts for $90\%$ of production, its score is $0.9(0.0292114)=0.0262903$, exceeding $0.1(0.1479808)=0.0147981$; the prediction changes to class 1. Local proximity and overall prevalence answer different parts of the question.{{cite:holmes_huber2019_msmb}} (§12.3, Linear discrimination, prior probabilities)

**Your turn.** At the symmetry point $x=2.5$, use priors $\pi_1=0.3$ and $\pi_2=0.7$. Find the posterior probabilities and the zero–one-loss decision.

::: {.callout-tip collapse="true" title="Answer"}
The class densities are equal, so they cancel from the posterior ratio. The posterior probabilities are $0.3$ and $0.7$, and the decision is class 2.
:::

## Assumptions and limits
Training and test observations must be comparable on the measured coordinates. Rescaling one coordinate changes distances unless its bandwidth changes too. A full bandwidth matrix can describe directional smoothing, but estimating many directions requires data. Dimension makes local neighborhoods sparse; this is a statistical limitation rather than a universal bound of six predictors. Bandwidth and feature choices must be made within training folds if cross-validation is to estimate predictive performance fairly.{{cite:holmes_huber2019_msmb}} (§§12.4, 12.6, overfitting and dimensionality)
