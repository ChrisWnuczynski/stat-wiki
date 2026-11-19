## Motivating example

A density estimate places a scaled bump around each observation. The Epanechnikov kernel gives that bump a parabolic profile and finite support: observations more than one bandwidth away make no contribution at a given evaluation point. Bandwidth determines how much detail the estimate displays; the kernel determines the shape of each contribution.{{cite:silverman1986}} (§2.4)

## Definition

The usual support-one parametrisation is
$$K(u)=\frac34(1-u^2)\mathbf1\{|u|\le1\},\qquad
 \widehat f_h(x)=\frac1{nh}\sum_{i=1}^nK\!\left(\frac{x-X_i}{h}\right),\quad h>0.$$
The indicator is essential: extending the polynomial beyond its support would give negative values. Nonnegativity and unit integral ensure that $\widehat f_h$ is itself a density.{{cite:silverman1986}} (§2.4, Eqs.2.2–2.2a)

Direct integration gives $\int K=1$, $\int uK(u)\,du=0$, second moment $\mu_2(K)=1/5$, and roughness $R(K)=\int K(u)^2\,du=3/5$. A unit-variance parametrisation uses support $[-\sqrt5,\sqrt5]$ and rescales both the horizontal and vertical axes. These are the same kernel family under a change of bandwidth.{{cite:epanechnikov1969}} (§2, pp.155–156, Eq.13)

## Properties — What the optimality statement fixes

The asymptotic bias–variance calculation involves the second kernel moment, the integrated squared kernel, bandwidth and smoothness of the target density. A kernel's roughness cannot be compared fairly without controlling its scale: simply spreading a kernel out lowers $R(K)$ while increasing its second moment. The parabolic solution is obtained with normalisation and a fixed second moment.{{cite:epanechnikov1969}} (§§1–2, pp.154–156)

There is a short exact variational argument for the support-one version. Let $L\ge0$ satisfy $\int L=1$ and $\int u^2L=1/5$, with finite $R(L)$. Put $D=L-K$. Then
$$R(L)-R(K)=\int D^2+2\int DK.$$
The two constraints imply $\int D(1-u^2)=0$. Since $K=0$ outside $[-1,1]$,
$$\int DK=\frac34\int_{|u|>1}L(u)(u^2-1)\,du\ge0.$$
Hence $R(L)\ge R(K)$. Equality requires $L=K$ almost everywhere. This optimisation supports the asymptotic efficiency result under its density-smoothness assumptions; it does not select the best bandwidth for a particular finite sample.{{cite:epanechnikov1969}} (§2, pp.155–156)

## Worked example — A bandwidth changes the neighbours

For observations $(0,1,2)$, evaluate the estimate at $x=1$. With $h=1$, the offsets are $(1,0,-1)$ and the kernel values are $(0,3/4,0)$, giving $\widehat f_1(1)=1/4$. With $h=2$, the offsets are $(1/2,0,-1/2)$ and the values are $(9/16,3/4,9/16)$, giving $\widehat f_2(1)=5/16=0.3125$. A wider window includes neighbouring observations but also divides by a larger bandwidth. The resulting height depends on both effects.{{cite:silverman1986}} (§2.4)

A compactly supported kernel can give zero estimates in gaps. It is continuous at its support boundary, but its derivative jumps there. A Gaussian kernel is positive everywhere and gives a smoother estimate. Neither choice eliminates the need to choose an appropriate bandwidth or address a boundary in the support of the target density.{{cite:silverman1986}} (§2.4)

**Your turn.** For the same three observations, what is $\widehat f_{1/2}(1)$?

::: {.callout-tip collapse="true" title="Answer"}
Only the central observation contributes. The height is $(3/4)/(3\cdot1/2)=1/2$.
:::
