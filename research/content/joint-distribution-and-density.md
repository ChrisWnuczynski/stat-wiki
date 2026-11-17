## Motivating example
Two measurements may each look continuously distributed while their pair is constrained to a curve. If $X$ is uniform on $(0,1)$ and $Y=X$, both marginal distributions have ordinary densities, but the pair always lies on the diagonal of the unit square. That diagonal has area zero. A joint density with respect to area cannot assign it probability one. The joint law describes dependence as well as the separate coordinate distributions.{{cite:durrett2019}} (§3.10, multivariate distributions and degenerate normal laws)

## Definition — A CDF exists for every real random vector
For a pair $(X,Y)$, the joint distribution function is $F(x,y)=\Pr(X\le x,Y\le y)$. For a vector, the inequalities hold coordinate by coordinate. This definition applies to discrete, continuous and mixed laws. A joint density is an additional representation: there must be a nonnegative measurable $f$ such that $\Pr((X,Y)\in A)=\int_A f(x,y)\,dx\,dy$ for every Borel set $A$. In particular $\int_{\mathbb R^2}f=1$. Merely writing two continuous marginal densities does not supply such a representation.{{cite:dodge2008}} (pp. 274–275, Joint Density Function and Joint Distribution Function)

A rectangular probability requires inclusion–exclusion:
$$\Pr(a<X\le b,c<Y\le d)=F(b,d)-F(a,d)-F(b,c)+F(a,c).$$
This follows by subtracting the two unwanted strips and adding their overlap back. Every such increment must be nonnegative. Coordinatewise monotonicity alone is weaker than this requirement, so a proposed bivariate CDF needs more than separately increasing curves. The same construction in dimension $p$ has $2^p$ corner terms.{{cite:durrett2019}} (§3.10, multivariate distribution functions)

## Properties — Marginalise before conditioning
If a joint density exists, $f_X(x)=\int f(x,y)\,dy$ and $f_Y(y)=\int f(x,y)\,dx$. Tonelli's theorem justifies these nonnegative integrals and shows they integrate to one. Whenever $f_X(x)>0$, a version of the conditional density is $f_{Y\mid X}(y\mid x)=f(x,y)/f_X(x)$. A density at a point is not the probability of that point: probabilities come from integrating over sets. Conditioning on $X=x$ is therefore handled through a conditional-density construction even though $\Pr(X=x)=0$ in a continuous model.{{cite:grinstead_snell1997}} (§4.2, continuous conditional probability)

Independence of the coordinates is equivalent to $F(x,y)=F_X(x)F_Y(y)$ for every pair of thresholds. When a joint density exists, it is equivalent to $f(x,y)=f_X(x)f_Y(y)$ almost everywhere. The reverse implication follows by integrating over rectangles, which generate the Borel sets; the forward implication follows from uniqueness of densities. A zero covariance is only one moment identity and cannot replace this factorisation criterion.{{cite:durrett2019}} (§2.1, independence and product distributions)

## Worked example — A density that changes with both coordinates
Let $F(x,y)=xy(x+y)/2$ on the unit square, extended to a CDF by setting the lower tails to zero and capping each coordinate at one. Its mixed derivative is $f(x,y)=x+y$ for $0<x,y<1$. This is nonnegative and integrates to one. Each marginal density is $x+1/2$ on the unit interval, and each marginal CDF is $(x^2+x)/2$. The rectangle $(1/4,3/4]\times(0,1/2]$ has probability $3/16$, obtained either by integrating $x+y$ or by the four CDF corners.

The joint mean product is $\mathbb E(XY)=1/3$, while $\mathbb EX=\mathbb EY=7/12$. Hence $\operatorname{Cov}(X,Y)=1/3-49/144=-1/144$. The dependence is weak in covariance magnitude but it is exact: $x+y$ is not $(x+1/2)(y+1/2)$. Small covariance need not mean independence.

**Your turn.** Find the conditional density of $Y$ when $X=1/2$ and its conditional mean.

::: {.callout-tip collapse="true" title="Answer"}
Here $f_X(1/2)=1$, so $f_{Y\mid X}(y\mid1/2)=y+1/2$ on $(0,1)$. Its mean is $\int_0^1 y(y+1/2)\,dy=7/12$.
:::

## Assumptions and limits — Differentiation loses singular mass
For an absolutely continuous joint CDF, differentiating in every coordinate recovers a density almost everywhere. Conversely, integrating an arbitrary mixed derivative of a CDF need not recover the whole law, because atoms or lower-dimensional singular mass can be lost. The pair $(X,X)$ illustrates this directly: $F(x,y)=\min(x,y)$ within the unit square, and its smooth regions have zero mixed derivative, while the diagonal still carries all the probability. A representation that combines singular and absolutely continuous components must account for both.{{cite:durrett2019}} (§3.10, densities and degenerate distributions; Appendix A.4, Theorem A.4.7)

## Connections — Transformations must respect dimension
For an invertible matrix $A$ and $Y=AX+b$, a density transforms as $f_Y(y)=f_X(A^{-1}(y-b))/|\det A|$. Indeed, substitute $y=Ax+b$ in the integral over a Borel set to obtain its probability under $Y$. The determinant accounts for the volume change and its absolute value makes the density nonnegative even when orientation reverses. The measurable-map formulation more generally defines a transformed law by inverse images of events.{{cite:tao2011_measure}} (§1.3, ex. 1.3.16; §1.4, exs. 1.4.38–1.4.39)

A lower-dimensional affine variable mapped into a higher-dimensional vector can instead have a singular law. Its possible values lie in a translated column space whose dimension is smaller than the output dimension, a set of zero volume. The pair $(X,X)$ is an example. The question to ask first is whether the transformed vector has a full-dimensional density, because a determinant density formula for an invertible square map cannot apply to a dimension-increasing map.
