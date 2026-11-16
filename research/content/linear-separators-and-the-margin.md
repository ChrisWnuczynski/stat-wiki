## Motivating example
Imagine two kinds of observations plotted on a plane, with several lines that separate their training labels perfectly. Training accuracy cannot choose among those lines. A line pressed against one observation may change its prediction after a tiny measurement error, while a line running through the middle of the gap tolerates more movement. The geometric margin makes that preference precise.{{cite:boser_guyon_vapnik1992}} (§2.1, pp. 145–146)

## Intuition
A linear separator divides a feature space with a hyperplane. Its normal vector $w$ points across the divide; the intercept $b$ shifts it. The sign of $w^\top x+b$ gives a class prediction, but the raw score is not a distance. Doubling both $w$ and $b$ leaves every prediction and the boundary unchanged while doubling that score. Dividing by $\lVert w\rVert$ removes this arbitrary scale.{{cite:boser_guyon_vapnik1992}} (§2.1, p. 145)

For a correctly classified training point, the signed distance on its own side is $y_i(w^\top x_i+b)/\lVert w\rVert$. The smallest such distance is the clearance between the decision boundary and the nearest labelled point. With a separable training set, choosing the largest clearance yields the **maximum-margin separator**. The points that attain the minimum are the **support vectors**: they hold the separating slab in place.{{cite:boser_guyon_vapnik1992}} (§§2.1–2.2, pp. 145–147)

## Definition
Let $x_i\in\mathbb R^p$ have binary label $y_i\in\{-1,+1\}$ and let $w\ne0$. The classifier predicts by $\operatorname{sign}(w^\top x+b)$; its decision boundary is $H=\{x:w^\top x+b=0\}$. When every training point is correctly separated, the minimum *one-sided geometric margin* is
$$
m(w,b)=\min_i\frac{y_i(w^\top x_i+b)}{\lVert w\rVert}>0.
$$
The two parallel supporting hyperplanes have full gap $2m(w,b)$ under the usual equal-margin normalisation. Some accounts call $m$ the margin and others call the full gap $2m$ the margin; stating which distance is meant prevents a factor-of-two error.{{cite:boser_guyon_vapnik1992}} (§2.1, p. 145)

Positive rescaling of $(w,b)$ leaves $m$ unchanged. Therefore a hard-margin fit can fix the smallest *functional* margin $y_i(w^\top x_i+b)$ at one. Its optimisation becomes
$$
\min_{w,b}\frac12\lVert w\rVert^2
\quad\text{subject to}\quad y_i(w^\top x_i+b)\ge1\quad\text{for every }i.
$$
At that solution, the one-sided geometric margin is $1/\lVert w\rVert$ and the full supporting-slab width is $2/\lVert w\rVert$. Maximising the latter is equivalent to minimising the displayed norm.{{cite:boser_guyon_vapnik1992}} (§2.1, equations 12–13, p. 146)

## Properties — Geometry and the points that matter
The closest points of the two class convex hulls bound how wide any separating slab can be. Moving the boundary toward either class reduces its clearance. In a hard-margin solution, support vectors satisfy $y_i(w^\top x_i+b)=1$; points farther away satisfy a strict inequality and do not directly pin the slab. The dual optimisation makes this precise: $w$ is a weighted sum of labelled training vectors, and a positive multiplier can occur only when its point lies on a margin boundary. This is why a distant extra observation often changes neither the fitted line nor its width.{{cite:boser_guyon_vapnik1992}} (§2.2, equations 15–16, pp. 146–147)

The margin is measured in the chosen feature coordinates. Multiplying one predictor by a large constant changes Euclidean distances and may change which observations are support vectors. Feature scaling must therefore be treated as part of fitting the classifier, not as a cosmetic display choice. The same geometric statement holds in a transformed feature space even when its boundary appears curved in the original coordinates.{{cite:boser_guyon_vapnik1992}} (§2, feature-space formulation, pp. 145–146){{cite:cortes_vapnik1995}} (§1, pp. 275–276)

## Statistical use — Hard and soft margins
The hard-margin problem requires a linearly separable training set. Real data may contain overlap, label errors, or outliers, so this constraint can be infeasible or unhelpfully sensitive to one point. A soft-margin classifier introduces nonnegative slack $\xi_i$ and relaxes the constraints to $y_i(w^\top x_i+b)\ge1-\xi_i$. Penalising the slacks trades margin width against violations; the tuning constant controls that trade-off. A point can be correctly classified yet lie *inside* the margin, while a point with a negative signed score is misclassified.{{cite:cortes_vapnik1995}} (§3, pp. 279–281)

The margin is a training-set geometric quantity, not a test-error guarantee for one fitted model. Its possible relation to prediction depends on assumptions and the learning setup. The radius–margin bound in this topic concerns a restricted set of labellings attainable with a specified gap inside a bounded ball; it does not reduce the VC dimension of *all* affine half-spaces just because one observed fit has a wide gap. Hold-out assessment remains needed when prediction is the goal.{{cite:boser_guyon_vapnik1992}} (§2.1, pp. 144–146; introduction)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Take any $x_0$ on $H$ and a unit normal $u=w/\lVert w\rVert$. A point displaced by distance $r$ along that normal is $x_0+ru$, and its score is $w^\top(x_0+ru)+b=r\lVert w\rVert$. Hence a point with score $w^\top x+b$ has signed perpendicular distance $(w^\top x+b)/\lVert w\rVert$. Replacing $(w,b)$ by $(cw,cb)$ for $c>0$ multiplies numerator and denominator by $c$, so the distance and predictions do not change.

For separable data, rescale until the smallest labelled score is one. The nearest point is then at distance $1/\lVert w\rVert$, and the two supporting hyperplanes $w^\top x+b=\pm1$ lie $2/\lVert w\rVert$ apart. Since this decreases as $\lVert w\rVert$ increases, maximum width and minimum squared norm are equivalent under these constraints. Finally, complementary slackness gives $\alpha_i[y_i(w^\top x_i+b)-1]=0$ for a dual multiplier $\alpha_i\ge0$. A positive multiplier requires a point on the supporting boundary; it cannot be assigned to a point strictly outside the slab.{{cite:boser_guyon_vapnik1992}} (§§2.1–2.2, pp. 145–147)
:::
:::

## Worked example
Consider hypothetical negative observations $(-1,0)$, $(-1,2)$, $(-2,1)$ and positive observations $(1,0)$, $(1,2)$, $(2,1)$. The boundary $x_1=0$ corresponds to $w=(1,0)$ and $b=0$. The four points with first coordinate $-1$ or $1$ have labelled score one, so each is one unit from the boundary; the two outer points have labelled score two. The supporting lines are $x_1=-1$ and $x_1=1$, giving full width $2/\lVert w\rVert=2$. The four inner observations are support vectors.{{cite:boser_guyon_vapnik1992}} (§2.1, geometry of the supporting slab, pp. 145–146)

This is the widest possible slab: the negative convex hull reaches $x_1=-1$ and the positive hull begins at $x_1=1$, so their closest separation is two. A tilted or shifted separator cannot leave more than one unit on *both* sides of a two-unit gap. The example also shows why the outer points do not determine the line: moving either outer point a little while it remains outside the slab leaves the nearest class faces and the solution unchanged.

**Your turn.** Keeping this fitted separator fixed, consider a new positive point $(1/2,1)$. Find its raw score, signed geometric distance, and hinge loss $\max\{0,1-y(w^\top x+b)\}$. Is it misclassified? Then double both $w$ and $b$ and explain what changes.

::: {.callout-tip collapse="true" title="Answer"}
The raw score is $1/2=0.5$. Because $\lVert w\rVert=1$ and the label is positive, its signed distance is also $1/2$. The hinge loss is $1-1/2=1/2$: it is correctly classified but lies inside the supporting margin. Doubling $w$ and $b$ doubles the raw score to one and doubles $\lVert w\rVert$ to two, leaving the signed geometric distance $1/2$ and the predicted class unchanged. The hinge loss formula uses a fixed score normalisation, so it is not invariant to an arbitrary rescaling of a fitted parameter pair.{{cite:cortes_vapnik1995}} (§3, slack-variable interpretation, pp. 279–281)
:::

## Common misconceptions
A larger raw score is not necessarily a larger geometric margin: rescaling $w$ and $b$ changes the former without changing the line. A point inside the margin is not necessarily on the wrong side; the Your turn point is correctly classified despite positive hinge loss. A wide *training* margin does not certify performance on new data. Finally, a linear boundary in a feature space need not be a straight boundary in the original input space when the feature map is nonlinear. These errors concern scale, classification, generalisation, and representation respectively.{{cite:boser_guyon_vapnik1992}} (§§2–3, pp. 145–148){{cite:cortes_vapnik1995}} (§§1, 3, pp. 275–281)

## Assumptions and limits — When the hard gap disappears
The XOR pattern with positives $(1,1)$ and $(-1,-1)$ and negatives $(1,-1)$ and $(-1,1)$ cannot be separated by any straight line in the original plane: each class's convex hull contains the origin. The hard-margin constraints are therefore infeasible. A feature transformation or soft-margin formulation is needed, depending on the task. Even for separable labels, adding one mislabeled outlier near the opposite class can sharply narrow the hard margin. A soft margin allows a controlled violation, but its result depends on the chosen penalty, feature scaling, and validation procedure.{{cite:cortes_vapnik1995}} (§§1, 3, pp. 275–281)

## Connections
[Distance to a hyperplane](distance-to-a-hyperplane.qmd) supplies the normalisation that turns a score into a distance. The worked bank problem [Distance to a hyperplane](../questions/ex-sl-17-1.qmd) applies that formula with a different normal vector; [Which points matter?](../questions/ex-sl-17-3.qmd) tests why adding a distant observation leaves a fitted support-vector solution alone. [Hard-margin primal](hard-margin-primal.qmd), [soft-margin primal](soft-margin-primal.qmd), and [kernel](kernel.qmd) continue the progression from geometric clearance to optimisation and nonlinear features.{{cite:boser_guyon_vapnik1992}} (§§2.1–2.2, pp. 145–147)

## History
Boser, Guyon, and Vapnik's 1992 training algorithm placed maximum-margin classification in a feature-space optimisation and showed that the decision rule can depend on a subset of supporting patterns. Cortes and Vapnik's 1995 support-vector network extended the approach from perfectly separable examples to data with training errors by introducing a soft-margin construction. The geometric distinction between a separating line and its margin remains the starting point for both versions.{{cite:boser_guyon_vapnik1992}} (§2, pp. 145–147){{cite:cortes_vapnik1995}} (§§1, 3, pp. 275–276, 279–281)
