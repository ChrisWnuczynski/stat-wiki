## Motivating example
A sheet of material may contain isolated defects scattered across its surface. A homogeneous spatial Poisson model describes a constant expected number per unit area and independent counts in disjoint regions. It therefore gives both the expected count in a rectangular inspection window and a probability that a disk contains no defect. Those are different geometric questions governed by the same intensity measure.{{cite:siegrist_poisson_general2022}} (§13.6, “The Process”)

## Definition — Specify a random counting measure
For a measurable region $A\subset\mathbb R^2$ of finite area $|A|$, a homogeneous Poisson process with intensity $\lambda>0$ has count $N(A)\sim\operatorname{Poisson}(\lambda|A|)$. Counts on pairwise disjoint regions are independent. An inhomogeneous intensity function $\lambda(x)$ replaces $\lambda|A|$ by $\Lambda(A)=\int_A\lambda(x)\,dx$. The independence condition remains part of the model; Poisson marginal counts in individual chosen windows alone do not specify it.{{cite:siegrist_poisson_general2022}} (§13.6, defining count and independence axioms)

The intensity has units of points per unit area, so the mean count $\Lambda(A)$ is dimensionless. For a Poisson variable, its mean and variance equal this parameter. Thus $E[N(A)]=\operatorname{Var}[N(A)]=\Lambda(A)$. The count law is a familiar discrete distribution; the spatial process adds consistency of those counts across regions and the independent-increment requirement.{{cite:dodge2008}} (pp. 425–426, Poisson Distribution)

## Properties — Void probabilities describe nearest-point distances
At a fixed deterministic origin, let $R$ be the distance to the nearest point of an unbounded homogeneous planar process. The event $R>r$ is the event of no point in the radius-$r$ disk. Therefore
$$P(R>r)=e^{-\lambda\pi r^2},\quad F_R(r)=1-e^{-\lambda\pi r^2},\quad r\ge0.$$
Differentiating gives density $2\lambda\pi r e^{-\lambda\pi r^2}$. The median solves $\lambda\pi r^2=\log2$, giving $r_{0.5}=\sqrt{\log2/(\lambda\pi)}$. This derivation uses the fixed origin and the disk's area, rather than a one-dimensional exponential gap formula.{{cite:siegrist_poisson_general2022}} (§13.6, nearest points and empty regions)

For overlapping windows, $N(A)=N(A\setminus B)+N(A\cap B)$ and similarly for $B$. Disjoint-region independence then gives $\operatorname{Cov}\{N(A),N(B)\}=\Lambda(A\cap B)$. Counts in overlapping windows generally correlate even though disjoint windows are independent. Geometry determines which part of the random count they share.

## Worked example — Inspect a window and a disk
Suppose defects have intensity $\lambda=2$ per square metre. A $1.5$-square-metre window has mean count $3.000$ and empty-window probability $e^{-3}=0.049787$. The probability of at least two defects is $1-e^{-3}(1+3)=0.800852$.

A radius-$0.5$-metre disk has area $\pi/4$, mean count $\pi/2=1.570796$, and empty-disk probability $e^{-\pi/2}=0.207880$. Thus the probability of a defect within half a metre of the fixed origin is $0.792120$. The nearest-point median is $0.332141$ metres. Counting and distance results agree because the distance event is precisely a count event in a geometrically specified region.{{cite:dodge2008}} (pp. 425–426, Poisson mass and count parameter)

**Your turn.** Double the intensity from two to four points per square metre. By what factor does the nearest-point median change?

::: {.callout-tip collapse="true" title="Answer"}
The median is proportional to $\lambda^{-1/2}$, so it is multiplied by $1/\sqrt2=0.707107$, becoming $0.234859$ metres.
:::

## Statistical use — Thinning preserves a Poisson model under independence
If every point is independently detected with probability $q$, the observed process has intensity $q\lambda$. Conditional on $N(A)=n$, its detected count is binomial with parameters $n,q$. Averaging its probability-generating function gives $E[(1-q+qs)^{N(A)}]=\exp\{\Lambda(A)q(s-1)\}$, a Poisson generating function. Independent marking across points and disjoint regions supplies the corresponding process property.{{cite:siegrist_poisson_general2022}} (§13.6, “Thinning and Combining”)

A low observed intensity can consequently reflect sparse events or poor detection. The count process alone does not distinguish those mechanisms. Spatial variation in detection probability gives observed intensity $q(x)\lambda(x)$, so a gradient in recorded points need not be a gradient in the underlying events. Detection assumptions belong beside the intensity model when it is used for an inspection or survey.

## Assumptions and limits — Window edges affect distance observations
The nearest-point formula assumes the process is observable over the entire disk around the fixed origin. An origin near the edge of a finite inspection window can have an unobserved closer point outside that window. Clustering, inhibition and shared physical causes can also violate Poisson independence. The model is a useful baseline, but a count mean alone does not establish its spatial independence assumptions.{{cite:siegrist_poisson_general2022}} (§13.6, model axioms on measurable regions)
