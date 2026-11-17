## Motivating example
A threshold detector sounds when a weighted combination of two measurements exceeds a cutoff. Adjusting its weights rotates the boundary; adjusting its bias moves it. Some label patterns can be captured this way, while XOR requires an additional feature or a richer model. Linear separability asks about the existence of a perfect affine separator for the given observations, before asking how one should estimate a useful predictor from them.{{cite:goodfellow_bengio_courville2016}} (§6.1, Learning XOR)

## Definition — Strict separation and the margin
For a finite labelled sample $(x_i,y_i)$ with $y_i\in\{-1,+1\}$, strict affine separability means that some $w,b$ satisfy
$$y_i(w^\top x_i+b)>0\quad\text{for every }i.$$
A finite strictly separable sample has a positive minimum functional margin $m=\min_i y_i(w^\top x_i+b)$. Dividing $(w,b)$ by $m$ gives the equivalent canonical constraints $y_i(w^\top x_i+b)\ge1$. If $w\ne0$, the minimum geometric margin is $m/\|w\|$. Multiplying both $w$ and $b$ by the same positive constant changes the functional margin but leaves this distance unchanged.{{cite:goodfellow_bengio_courville2016}} (§5.7.2, support vector machines)

If a point lies exactly on the boundary, its score is zero and strict separation fails for that choice of weights. A weak separation with zero margins therefore differs from a strict separation. When both labels occur, a strict separator must have nonzero $w$. The labels, coordinate transformation and treatment of the intercept are all part of the question.{{cite:zhang_d2l2023}} (§5.1, multilayer perceptrons and limitations of linear models)

## Properties — Convex combinations expose an obstruction
If a strict separator exists, the convex hulls of the two classes cannot intersect. Every convex combination of positive points has positive score, because an affine function preserves convex combinations. Every convex combination of negative points has negative score. A point in both hulls would have to have both signs, a contradiction.

For XOR on $\{0,1\}^2$, the midpoint of the two positive points $(1,0)$ and $(0,1)$ is $(1/2,1/2)$. It is also the midpoint of the negative points $(0,0)$ and $(1,1)$. The convex hulls intersect, proving that no affine separator works. By contrast, adding the feature $x_1x_2$ gives the score $x_1+x_2-2x_1x_2-1/2$, positive exactly for the two XOR successes. The difficulty lies in the representation, rather than in a failure to search enough candidate lines.{{cite:goodfellow_bengio_courville2016}} (§6.1){{cite:zhang_d2l2023}} (§5.1.1, limitations of linear models)

## Worked example — A biased threshold and its distances
On the four binary inputs, the AND labels are positive only at $(1,1)$. Choose $w=(1,1)$ and $b=-3/2$. The scores at $(0,0),(1,0),(0,1),(1,1)$ are $-3/2,-1/2,-1/2,1/2$, so all labels are correct. The minimum functional margin is $1/2$ and the minimum geometric margin is $1/(2\sqrt2)\approx0.353553$. Doubling the coefficients gives canonical margin one without moving the boundary $x_1+x_2=3/2$.

With no bias, the point $(0,0)$ always has zero score. The same strict-separation problem therefore has no homogeneous solution. Appending a constant coordinate $1$ and giving it coefficient $b$ restores the affine model, though regularizing that coefficient can change the optimization problem.{{cite:zhang_d2l2023}} (§5.1, linear models and hidden representations)

**Your turn.** Classify points $x=0$ and $x=2$ as negative and positive using $f(x)=x-1$. Find their functional margins and their distances to the boundary.

::: {.callout-tip collapse="true" title="Answer"}
The scores are $-1$ and $1$, giving functional margins one. The boundary is $x=1$ and both distances are one. Multiplying the score by three gives margins three but the same distances.
:::

## Assumptions and limits
A perfectly separated training sample need not predict future labels well. Extra dimensions can make a small finite sample separable even when the population labels overlap. Validation measures generalization; separability describes the observed geometry. Under logistic likelihood, strict separation can also make coefficient magnitudes diverge: scaling a separator upward keeps improving each observation's likelihood toward one. A finite penalty changes that behavior by charging for large coefficients.{{cite:holmes_huber2019_msmb}} (§§12.4–12.6, training error and regularization)
