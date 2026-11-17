## Motivating example
A linear classifier reports scores of $5$ and $50$ for the same observation after its coefficients are multiplied by ten. The decision boundary has not moved. Dividing the score by the length of its normal vector turns this arbitrary algebraic scale into a geometric distance.{{cite:burges1998}} (§3.1, Linear Support Vector Machines)

## Key results — Projection and orientation
For $H=\{z:w^\top z+b=0\}$ with $w\ne0$, define
$$
d_H(x)=\frac{w^\top x+b}{\|w\|},\qquad
P_H(x)=x-\frac{w^\top x+b}{\|w\|^2}w.
$$
The sign depends on the chosen normal orientation; the ordinary distance is $|d_H(x)|$. The projection is the closest point on the boundary. In a support-vector classifier, the parallel score levels $+1$ and $-1$ are separated by $2/\|w\|$.{{cite:scholkopf_smola2003_intro}} (§3, pp. 46–48)

To see minimality, $P_H(x)$ lies in $H$, and $x-P_H(x)$ is parallel to $w$. For any $z\in H$, the vector $P_H(x)-z$ is orthogonal to $w$. Pythagoras gives
$$
\|x-z\|^2=d_H(x)^2+\|P_H(x)-z\|^2.
$$
Its minimum occurs uniquely at $z=P_H(x)$. This proves both the distance and projection formulas for every nonzero normal.

## Generalizations — Rescaling a classifier
Multiplying $(w,b)$ by $c>0$ preserves the signed distance, projection, and class labels. Multiplying by $c<0$ preserves the boundary and projection while reversing the signed distance and labels. Thus orientation is extra information attached to the same geometric hyperplane. The functional margin $y(w^\top x+b)$ changes under positive scaling, while the geometric margin $yd_H(x)$ does not. Fixing support levels at $\pm1$ gives the scale used by the maximum-margin optimisation.{{cite:burges1998}} (§3.1, canonical hyperplanes){{cite:scholkopf_smola2003_intro}} (§3, eqs. 23–25, pp. 47–48)

Distances also depend on feature units. Replacing centimetres by metres changes Euclidean geometry unless the coordinate transformation is accounted for. A geometric margin is meaningful relative to the chosen feature space and its inner product. Kernel classifiers apply the same normal-vector argument in that feature space.{{cite:scholkopf_smola2003_intro}} (§4, pp. 49–50)

## Worked example
Let $w=(3,4)^\top$, $b=-5$ and $x=(2,1)^\top$. The score is $5$, the normal has length $5$, and the signed distance is $1$. The projection is $(1.4,0.2)^\top$, whose score is zero. The origin has signed distance $-1$. The score planes $+1$ and $-1$ have total width $0.4$; this is different from the distance of this particular observation to the decision boundary.

For $w=(3,0)^\top$, $b=-6$ and $x=(5,4)^\top$, the boundary is the vertical line $x_1=2$. The signed distance is $3$, and the canonical margin width is $2/3$. These values follow from the same formula despite the unused second coordinate.{{cite:burges1998}} (§3.1, margin geometry)

**Your turn.** Multiply $(3,4,-5)$ by $-2$. What happens to the signed distance and projection of $(2,1)$?

::: {.callout-tip collapse="true" title="Answer"}
The signed distance becomes $-1$. The projection remains $(1.4,0.2)$, because multiplying the numerator and normal by $-2$ and the squared norm by four leaves the displacement unchanged.
:::
