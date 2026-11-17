## Motivating example — A separator that must leave room
A binary training set may be separable by a hyperplane while some points lie extremely close to it. Requiring a positive empty slab between the two classes restricts which labelings can be realised. The radius–margin idea compares that slab with the size of a ball containing the candidate points. The comparison is scale-free: changing all coordinates to another common unit changes both lengths by the same factor.{{cite:burges1998}} (§7.1, Theorem 6)

## Statement
Use $D$ for the ball's diameter and $\rho$ for the *full* distance between its parallel margin planes. For the restricted shattering count described above,
$$h\le\min\{\lceil D^2/\rho^2\rceil,p\}+1.$$
Both the diameter and full slab width are part of this convention. If $R=D/2$ is a radius and $\gamma=\rho/2$ is a one-sided margin, then $D^2/\rho^2=R^2/\gamma^2$. Mixing a radius with a full width would introduce a factor of four. The count concerns the ability to realise every labeling while respecting the gap condition.{{cite:burges1998}} (§7.1, gap-tolerant classifiers and Theorem 6)

## Intuition — One successful labeling is weaker than shattering
A large observed margin is a property of a fitted separator for one labeling. Shattering requires a suitable separator for every labeling of the same points. Thus an observed margin does not by itself calculate the ordinary VC dimension of all hyperplanes. Capacity restrictions matter in generalisation arguments alongside sample size and empirical error. A capacity bound is one ingredient in such an argument, rather than a test-error estimate by itself.{{cite:schapire2013_explaining_adaboost}} (§2, “Direct Application of VC Theory”)

The ambient dimension still limits the count through $p+1$. When the ball-to-margin ratio is large, that dimension limit can be the tighter bound. When the margin is substantial relative to the ball, the geometric term can bind. A translation moves the enclosing ball's centre without changing the relevant distances; common rescaling preserves the ratio. Unequal rescaling of individual coordinates changes the geometry and can change the bound.{{cite:burges1998}} (§7.1, Theorem 6)

## Key results — What the bound can and cannot certify
The theorem controls a family with a margin condition, and its detailed geometric proof invokes a simplex configuration argument. The elementary affine-hyperplane bound supplies the dimension term. The radius–margin term adds a quantitative restriction based on the permitted gap. These statements need the shattering and geometric conventions specified in the theorem; arbitrary hard-margin solutions selected after inspecting data do not automatically create a fixed family with that capacity.{{cite:burges1998}} (§7.1, Theorem 6 and the stated geometric lemma)

## Worked example — Compare both restrictions
For $D=6$, $\rho=2$ and $p=20$, the ratio is nine and the bound is $h\le10$. In radius notation $R=3$ and $\gamma=1$, producing the same ratio. Doubling the full margin to four gives ratio $36/16=2.25$, ceiling three and bound four. At the first geometry but dimension $p=4$, the bound is instead five: the dimension restriction binds.

Multiplying every coordinate by five changes $(D,\rho)$ from $(6,2)$ to $(30,10)$ and preserves the ratio nine. This invariance applies to common changes of scale. It does not say that arbitrary feature standardisation leaves a learned separator or its margin unchanged.

**Your turn.** With $D=4$, $\rho=3$ and $p=10$, evaluate the bound.

::: {.callout-tip collapse="true" title="Answer"}
The ratio is $16/9$, whose ceiling is two. The bound is $h\le\min(2,10)+1=3$.
:::

## Statistical use — Capacity and error require different inputs
A generalisation bound must also specify a sampling model, a confidence level and a way of combining capacity with empirical performance. The geometry alone lacks those inputs. Comparing margins within a scientifically chosen feature representation can be informative, but tuning that representation by the same data affects the analysis of the selected procedure. The broader VC framework makes the role of these additional assumptions explicit.{{cite:schapire2013_explaining_adaboost}} (§2)
