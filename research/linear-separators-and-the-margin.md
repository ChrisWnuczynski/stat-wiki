# Linear separators and the margin: research notes

## Sources opened

- **Checked:** Boser, Guyon & Vapnik, “A Training Algorithm for Optimal Margin Classifiers” (1992), original COLT paper via university-hosted proceedings PDF, §2 and §2.1, printed pp. 144–146. Defines the signed decision function, perpendicular margin $y_iD(x_i)/\|w\|$, maximum-margin hard separator, support patterns, and the norm-minimising constrained problem.
- **Checked:** Cortes & Vapnik, “Support-Vector Networks” (1995), original *Machine Learning* paper via university-hosted journal PDF, abstract and §§1, 3, printed pp. 273–276, 280–281. Describes support vectors, nonlinear feature spaces, and extension from separable data to soft margins with nonnegative slack.
- **Checked:** inherited `sources/stat3006/chapters/sl-17-support-vectors.qmd`, “Linear separators and the margin,” “The hard-margin quadratic programme,” and the three-point worked example. Preserves sign coding, geometric width $2/\|w\|$, and the distinction between the restricted radius–margin capacity bound and ordinary half-space VC dimension. Its textbook citations are retained only where directly supported by the original papers read or by the inherited source.
- **Checked for orientation:** Dodge's index has no direct “support vector” or “margin” entry. No Dodge citation will be used for the method's history; the original 1992 and 1995 papers supply that history.

## Mathematical checks

- **Checked:** For four support candidates $(-1,0),(-1,2)$ labelled $-1$ and $(1,0),(1,2)$ labelled $+1$, the hard-margin separator $w=(1,0), b=0$ has boundary $x_1=0$, unit geometric distance from each training point, and full slab width $2$. Extra same-label points $(-2,1),(2,1)$ lie farther away. A vertical line $x_1=c$ has minimum distance $1-|c|$ for $|c|<1$, hence $c=0$ maximises it among vertical lines; the convex hulls' closest gap is $2$, so no tilted line can beat unit per-class margin.
- **Checked:** Positive test point $(1/2,1)$ has raw score and signed geometric distance $1/2$ under this *fixed* separator. Its hinge loss is $\max(0,1-1/2)=1/2$, even though it lies on the positive side. This does not claim the old separator remains optimal after adding that point to training.
- **Checked:** Scaling $w,b$ by two leaves signs and the geometric distance unchanged, while doubling raw scores. The hard-margin constraint is therefore coupled to a specific score normalisation.

## Scope decisions

- **Assumed:** The two-dimensional coordinates are hypothetical teaching data, not observed measurements.
- **Disputed:** “Larger training margin guarantees lower test error” overstates the theory. Generalisation depends on the data-generating setting, feature map, tuning, and validation.
- **Disputed:** The radius–margin bound in the inherited chapter is a theorem about labelings achievable with a specified margin, not a bound on the VC dimension of all affine separators. Avoid conflating them.
