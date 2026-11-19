## Lead context
The approximation estimates an integral from the height and curvature of an interior peak, rather than from the peak height alone.

## Motivating example
Two fitted models can attain similar maximum likelihoods while spreading substantial likelihood over very different parameter volumes. A marginal likelihood integrates likelihood against a prior, so a narrow peak and a broad peak need not contribute equally. Laplace's method replaces a sufficiently concentrated smooth peak by a Gaussian integral.{{cite:schwarz1978}} (§§2–3, pp. 462–464)

## Definition — Peak height times local volume
For $I=\int_\Theta e^{\ell(\theta)}\,d\theta$, let $\widetilde\theta$ be an interior local maximum and $H=-\nabla^2\ell(\widetilde\theta)$ be positive definite. The quadratic Taylor approximation gives
$$
I\approx e^{\ell(\widetilde\theta)}(2\pi)^{d/2}|H|^{-1/2}.
$$
For a marginal likelihood, $\ell$ includes the log prior as well as the log likelihood. Thus $\widetilde\theta$ is the mode of the joint integrand, and its curvature need not equal the observed likelihood information at the maximum likelihood estimate.{{cite:tierney_kadane1986}} (§2, p. 83)

## Properties — Integrating the quadratic peak
Write $u=\theta-\widetilde\theta$. Vanishing gradient removes the linear Taylor term, leaving $\ell(\theta)\approx\ell(\widetilde\theta)-u^\top Hu/2$. An orthogonal diagonalisation $H=Q\operatorname{diag}(\lambda_j)Q^\top$ and the substitution $z_j=\sqrt{\lambda_j}(Q^\top u)_j$ give Jacobian $|H|^{-1/2}$. The integral of the quadratic surrogate is therefore
$$
e^{\ell(\widetilde\theta)}|H|^{-1/2}\prod_{j=1}^d\int_{\mathbb R}e^{-z_j^2/2}\,dz_j
=e^{\ell(\widetilde\theta)}(2\pi)^{d/2}|H|^{-1/2}.
$$
This evaluation is exact for a Gaussian-shaped integrand on the full Euclidean space. Its use for another integrand requires control beyond the quadratic expansion.{{cite:tierney_kadane1986}} (§2, p. 83, eq. 2.2)

## Assumptions and limits — Concentration and dimension penalties
[]{#property-laplace-asymptotics}
For integrals $\int e^{nf(\theta)}a(\theta)d\theta$, the leading expression takes the form
$$
e^{nf(\theta_0)}a(\theta_0)(2\pi/n)^{d/2}|-\nabla^2f(\theta_0)|^{-1/2}.
$$
A unique dominant interior maximum, nondegenerate curvature, local smoothness and sufficiently small tail contributions are essential to the usual asymptotic argument. Local derivatives alone do not control a second peak elsewhere.{{cite:tierney_kadane1986}} (§2, p. 83; Appendix, p. 86)

Taking logarithms exposes $-(d/2)\log n$ when dimension is fixed and curvature grows proportionally to $n$. This is the source of the regular-model BIC penalty after multiplying log marginal likelihood by minus two. Boundary estimates, nonidentifiable mixture components, or a Hessian with a zero eigenvalue require a different analysis; counting parameters alone does not repair those failures.{{cite:schwarz1978}} (§3, pp. 463–464)

## Statistical use — Curvature belongs to coordinates
A change of variable also changes the integration measure. Its Jacobian must enter the transformed log integrand before locating its mode and curvature. Omitting that factor changes the integral. Positive definite $H$ permits a stable log-determinant calculation from a Cholesky factor rather than explicitly forming $H^{-1}$. A sum of well-separated local contributions can describe multiple peaks, provided their neglected regions are controlled.{{cite:tierney_kadane1986}} (§2, p. 83)

## Worked example
For a positive integer $n$, consider
$$
I_n=\int_0^\infty e^{n(\log x-x)}dx=\frac{\Gamma(n+1)}{n^{n+1}}.
$$
The equality follows by setting $t=nx$. The mode is $x=1$ and the negative second derivative there is $n$, so the approximation is $L_n=e^{-n}\sqrt{2\pi/n}$. For $n=10$,
$$
I_{10}=3.6288\times10^{-5},\qquad L_{10}\approx3.598696\times10^{-5},\qquad L_{10}/I_{10}\approx0.991704.
$$
For $n=100$ the ratio is about $0.999167$. The finite boundary at zero is increasingly distant in local standard-deviation units as the peak concentrates near one. This example allows direct comparison with an exact integral rather than assuming the approximation is exact at a finite sample size.{{cite:tierney_kadane1986}} (§2, p. 83)

**Your turn.** Evaluate the approximation to $\int_{\mathbb R}e^{-2(x-2)^2}dx$. Is it exact?

::: {.callout-tip collapse="true" title="Answer"}
The mode is $2$, peak height is one, and $H=4$. The value is $\sqrt{2\pi}/2=\sqrt{\pi/2}\approx1.253314$. It is exact because the log integrand is a quadratic on the full real line.
:::
