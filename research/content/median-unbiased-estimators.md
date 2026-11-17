## Motivating example — Balance the probability of overestimation
A manufacturer estimates an upper endpoint from a small uniform sample. The largest observed value always lies below the endpoint, yet multiplying it by a suitable constant can make overestimation and underestimation equally likely. A different constant removes its mean bias. The distinction matters whenever the shape of an estimator's sampling distribution makes its mean and median disagree. Median-unbiasedness concerns repeated-sample probabilities, rather than the location of a posterior distribution.{{cite:rojo2007_unbiased}} (“Unbiased Estimator”, absolute-error loss and Condition 2)

## Definition — Allow probability at the target
For every parameter value $\theta$, an estimator $T$ is median-unbiased when $\theta$ is a median of its sampling distribution:
$$\Pr_\theta(T\le\theta)\ge\tfrac12,\qquad \Pr_\theta(T\ge\theta)\ge\tfrac12.$$
Equivalently, both strict tail probabilities are at most one half. If the distribution has no atom at $\theta$, the two strict tails must each equal one half. With an atom, they can be unequal; a discrete median need not divide the probability into two equal strict tails. This convention agrees with the criterion that the target minimises expected absolute error.{{cite:rojo2007_unbiased}} (“Unbiased Estimator”, absolute-error loss)

To see that connection, consider $R(a)=\mathbb E_\theta|T-a|$ when this expectation is finite. Its left and right derivatives at $a$ are $2\Pr_\theta(T<a)-1$ and $2\Pr_\theta(T\le a)-1$. The convex function is minimised at $a=\theta$ precisely when the left derivative is nonpositive and the right derivative is nonnegative. Those inequalities are exactly the two median conditions. Squared error instead selects the mean, because $\mathbb E(T-a)^2=\operatorname{Var}(T)+(\mathbb ET-a)^2$ when the second moment exists.

## Properties — Symmetry and transformations
A sampling distribution symmetric about $\theta$ has $\theta$ as a median. For example, a normal sample mean centred at its population mean is both mean-unbiased and median-unbiased: its normal sampling density is symmetric, and its mean and median coincide.{{cite:nist_normal_distribution}} (§1.3.6.6.1, Common Statistics: Mean and Median)

For an odd iid sample of size $2k+1$ from a continuous distribution with median $\theta$, exactly half the population probability lies on each side. The sample median exceeds $\theta$ when at least $k+1$ observations exceed it. Symmetry of a $\operatorname{Binomial}(2k+1,1/2)$ count makes that probability one half. The same holds below $\theta$. Continuity removes ties, while odd sample size gives an unambiguous central order statistic. This argument needs neither a symmetric population density nor a finite population mean.

Strictly monotone transformations preserve median-unbiasedness. For increasing $g$, the events $g(T)\le g(\theta)$ and $T\le\theta$ coincide. A decreasing $g$ exchanges the two tails. Thus $g(T)$ estimates $g(\theta)$ with the same median property. Mean-unbiasedness has no corresponding general nonlinear-transformation rule, because expectations do not generally commute with $g$. This distinction is useful when the parameter is reported on a logarithmic or reciprocal scale.{{cite:rojo2007_unbiased}} (“Unbiased Estimator”, alternative loss criteria)

## Worked example — Calibrate a uniform maximum
Let $X_1,\ldots,X_n$ be iid uniform on $(0,\theta)$, with $\theta>0$, and put $M=\max_iX_i$. Independence gives $\Pr_\theta(M\le m)=(m/\theta)^n$ for $0\le m\le\theta$. Its sampling median is $\theta 2^{-1/n}$. Consequently $T=2^{1/n}M$ has median $\theta$. The density $nm^{n-1}/\theta^n$ also gives $\mathbb EM=n\theta/(n+1)$, so $\mathbb ET=2^{1/n}n\theta/(n+1)$: median calibration does not imply mean calibration.

Take $n=2$, $\theta=10$ and an observed maximum of seven. The sampling median of $M$ is $5\sqrt2\approx7.071068$. The median-unbiased estimate is $7\sqrt2\approx9.899495$, whereas the mean-unbiased estimate is $3(7)/2=10.5$. The mean of $T$ over repeated samples is $(2\sqrt2/3)\theta\approx0.942809\theta$, below the target. The numbers come from the full sampling distribution, so an observed estimate lying below ten does not by itself establish either form of bias.

**Your turn.** Suppose $T-\theta$ equals $-1,0,1$ with probabilities $0.1,0.6,0.3$. Is $T$ median-unbiased despite its unequal strict tails?

::: {.callout-tip collapse="true" title="Answer"}
Yes. The weak probabilities are $\Pr(T\le\theta)=0.7$ and $\Pr(T\ge\theta)=0.9$. Its expected absolute distances from $\theta$, $\theta+1$ and $\theta-1$ are $0.4$, $0.8$ and $1.2$, respectively. Its mean is $\theta+0.2$, so it is not mean-unbiased.
:::

## Assumptions and limits — A centring property is not an efficiency comparison
Median-unbiasedness places no upper bound on sampling spread. Two symmetric estimators can have the same sampling median and very different variances, confidence widths or absolute-error risks. In a normal model, changing the standard deviation leaves the median fixed while changing the distribution's scale.{{cite:nist_normal_distribution}} (§1.3.6.6.1, normal location and scale parameters)

The property must also hold for every admissible parameter value, including any nuisance parameters over which the definition is asserted. Checking one simulation setting or one realised sample cannot establish that uniform statement. An estimator may lack a finite mean and still have a median, making the probability definition applicable when mean bias is unavailable.
