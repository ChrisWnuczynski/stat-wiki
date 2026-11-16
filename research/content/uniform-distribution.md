## Motivating example
A measurement reported to the nearest centimetre may have a rounding error somewhere between minus half and plus half a centimetre. If the unrounded position within that interval has no preferred location, a uniform law models the error: equal-length subintervals receive equal probability. The model is useful precisely because it states that assumption openly, not because every measurement error is flat. The density and cumulative plots above show its constant height and linear accumulation.{{cite:dodge2008}} (pp. 553–554, “Uniform Distribution”){{cite:siegrist2022_uniform_interval}} (§5.21, Uniform Distribution on a General Interval)

## Intuition — Why interval length governs probability
For $X\sim U[a,b]$, the support has length $b-a$ and the constant density must be $1/(b-a)$ so its total area is one. An interval of length $d$ entirely inside $[a,b]$ therefore has probability $d/(b-a)$. This is the continuous counterpart of counting equally likely outcomes, but each exact point has probability zero. The interval midpoint is both mean and median; moving the support without changing its width moves the centre but leaves the variance unchanged.{{cite:siegrist2022_uniform_interval}} (§5.21, Definition; Distribution Functions; Moments)

## Definition
The notation $U[a,b]$ here denotes a *continuous* uniform law on a real interval with $a<b$. Whether endpoints are included makes no difference to probabilities because single points have probability zero. A discrete uniform law on integers $a,a+1,\ldots,b$ is a different distribution with positive probability at each integer. The distinction matters whenever a recorded measurement has been rounded.{{cite:siegrist2022_uniform_interval}} (§5.21, Definition; Distribution Functions)

## Properties
The CDF is zero below $a$, rises as $(x-a)/(b-a)$ inside the interval, and equals one above $b$. Solving $u=(x-a)/(b-a)$ gives the quantile $Q(u)=a+(b-a)u$. This linear map sends a standard uniform draw to $U[a,b]$, while the inverse-CDF result above extends the simulation idea to any target distribution. The mean–variance proof in this section shows that the spread is $(b-a)^2/12$, not $(b-a)/12$.{{cite:siegrist2022_uniform_interval}} (§5.21, Distribution Functions; Moments; Related Distributions)

## Related distributions
The standard uniform $U[0,1]$ is the $\operatorname{Beta}(1,1)$ law. It is also the input for inverse-transform generation: if $F$ is a target CDF and $F^{-1}$ its generalized quantile, $F^{-1}(U)$ has CDF $F$. Conversely, for a continuous $X$ with CDF $F$, $F(X)$ is standard uniform. These transformations connect a simple flat law to non-flat sampling models without claiming that the target variables themselves are uniform.{{cite:siegrist2022_uniform_interval}} (§5.21, Related Distributions)

## Statistical inference
Uniform bounds can be a physical constraint, such as a known range of a rounding error, or a modeling choice for an unknown quantity. A flat density on an interval does not mean an analysis is free of prior assumptions: changing the variable by a nonlinear transformation changes what “flat” means. [Draws from a uniform interval](../questions/ex-prob-generate-uniform.qmd) applies the linear quantile map; [Minimum and average of uniform draws](../questions/ex-prob-min-and-mean.qmd) shows how summaries of uniform samples acquire different laws; [State the probability functions](../questions/ex-prob-name-the-laws.qmd) contrasts the continuous density with discrete masses.{{cite:siegrist2022_uniform_interval}} (§5.21, Definition; Related Distributions)

## Generating random samples
For a standard uniform $U$, compute $a+(b-a)U$. If $a=10$, $b=15$, and $U=0.2$, the transformed value is $11$. A reproducible computer generator produces a deterministic sequence from a seed that is designed to behave like independent uniform draws for simulation; the mathematical uniform model describes the intended distribution, not the literal mechanism of every generated bit.{{cite:siegrist2022_uniform_interval}} (§5.21, Related Distributions){{cite:von_neumann1951_random_digits}} (pp. 36–38, random digits and uniform reals)

## Examples
### Worked example — An interval probability and quantile
Let $X\sim U[2,8]$. The support length is $6$, so its density is $1/6$ inside the interval. The probability that $3<X<6$ is $(6-3)/6=0.5$. Its mean is $(2+8)/2=5$ and variance is $6^2/12=3$. To find the 90th percentile, solve $Q(0.9)=2+6(0.9)=7.4$. Probability, centre, spread and percentile each summarize a different part of this one flat law.{{cite:siegrist2022_uniform_interval}} (§5.21, Distribution Functions; Moments)

**Your turn.** For $Y\sim U[-2,4]$, calculate $\Pr(0<Y<3)$, the mean and variance, and the 75th percentile.

::: {.callout-tip collapse="true" title="Answer"}
The support length is $6$. The interval $(0,3)$ has length $3$, so its probability is $3/6=0.5$. The mean is $(-2+4)/2=1$ and the variance is $6^2/12=3$. The quantile is $Q(0.75)=-2+6(0.75)=2.5$. The upper quartile is inside the support, as it must be.{{cite:siegrist2022_uniform_interval}} (§5.21, Distribution Functions; Moments)
:::

## Common misconceptions
Uniform density means equal probability for equal *lengths*, not equal positive probability for each real number. A density height can exceed one when $b-a<1$; it is an area under the density that must be at most one. A continuous $U[1,6]$ does not model a fair die, whose six integer outcomes form a discrete uniform law. Nor does a flat prior remain flat after a nonlinear reparameterization; the implied density changes by a Jacobian factor.{{cite:siegrist2022_uniform_interval}} (§5.21, Definition; Distribution Functions)

## Assumptions and limits
If customers tend to arrive just before opening, their arrival times in a fixed interval will cluster near one endpoint and a uniform timing model will be misleading. Rounding error may also cluster if measurements are digit-preferred rather than smoothly spread. The bounded support gives zero probability to any value outside $[a,b]$, so a surprise outside the proposed bounds contradicts the model. For a computer simulation, a poorly designed pseudorandom generator can create correlations even when each output looks marginally uniform.{{cite:dodge2008}} (pp. 553–554, “Uniform Distribution”){{cite:von_neumann1951_random_digits}} (pp. 36–38, random-digit generation)

## Connections
The [beta distribution](beta-distribution.qmd) includes $U[0,1]$ as a special shape. The [cumulative distribution function](cumulative-distribution-function.qmd) turns interval length into cumulative probability, and the [inverse-transform method](inverse-transform-method.qmd) turns uniform draws into many other laws. The [sum of uniforms](convolution.qmd) has a triangular rather than flat density, as the example below shows. A uniform starting law is thus useful even when the quantity ultimately studied has a very different shape.{{cite:siegrist2022_uniform_interval}} (§5.21, Related Distributions)

## History
The continuous uniform law has also been called the *rectangular distribution* because its density graph is a rectangle. As computation grew, uniform random digits became the raw material for simulating other laws: von Neumann's 1951 discussion explicitly asked how to generate uniform reals and then numbers following a specified non-uniform law. The modern inverse-CDF construction formalizes one answer to that simulation problem.{{cite:dodge2008}} (p. 553, “Uniform Distribution”){{cite:von_neumann1951_random_digits}} (pp. 36–38, questions on random digits and assigned laws){{cite:siegrist2022_uniform_interval}} (§5.21, Related Distributions)
