## Motivating example
Suppose an alarm sounds when exactly one of two switches is on, and stays quiet when both are off or both are on. Each switch has only two positions, so the entire rule has four inputs. It is easy to state and easy to check, but a classifier that cuts the two-input plane with one straight line cannot reproduce it. This tiny task isolates the difference between a linear decision boundary and a model that can combine features nonlinearly.{{cite:goodfellow_deep_learning2016_ch6}} (Ch. 6, §6.1, pp. 166–168)

## Intuition
Write the positive inputs at $(0,1)$ and $(1,0)$ and the negative inputs at $(0,0)$ and $(1,1)$. The two positive points lie on one diagonal of the unit square; the two negative points lie on the other. Both diagonal segments pass through $(1/2,1/2)$. A straight-line separator cannot put the common midpoint simultaneously on opposite sides. This is a geometric way to read the four incompatible threshold inequalities in the definition below.{{cite:goodfellow_deep_learning2016_ch6}} (Ch. 6, §6.1, pp. 167–169)

The obstruction concerns the original two coordinates and one affine score $b+w_1x_1+w_2x_2$. It does not prohibit every classifier with a linear final layer. A nonlinear map can move the four points into a new feature space where a linear final score works. A hidden layer computes such features from the inputs; a hand-chosen interaction $x_1x_2$ provides another route.{{cite:goodfellow_deep_learning2016_ch6}} (Ch. 6, §6.1, pp. 168–171)

## Definition
The exclusive-or rule is $y=1$ exactly when $x_1\ne x_2$ for binary $x_1,x_2$, and $y=0$ otherwise. Its truth table in the order $(0,0),(0,1),(1,0),(1,1)$ is $(0,1,1,0)$. Under the threshold convention $f(u)=1$ for $u\geq0$ and $0$ for $u<0$, the one-unit model $f(b+w_1x_1+w_2x_2)$ asks a single line to separate alternating corners. The four threshold inequalities show why no choice of its three weights succeeds.{{cite:goodfellow_deep_learning2016_ch6}} (Ch. 6, §6.1, pp. 166–169)

## Interpretation
The word “problem” names an expressiveness test for a chosen architecture. A flexible classifier can memorise the four labels, while one affine threshold cannot represent the rule. Representation and training are separate: a nonlinear network may contain an exact XOR solution but a particular optimisation run may still fail to find it.{{cite:goodfellow_deep_learning2016_ch6}} (Ch. 6, §6.1, pp. 167–171){{cite:rumelhart_hinton_williams1986}} (pp. 533–536, hidden-unit representations and weight learning)

## Properties
A product feature resolves the four-point contradiction. On binary inputs, $y=x_1+x_2-2x_1x_2$: at the two mixed corners the score is one, while at the equal corners it is zero. With feature map $\phi(x)=(x_1,x_2,x_1x_2)$, that formula is affine in $\phi$, although it is nonlinear in the original $x$. The threshold score $x_1+x_2-2x_1x_2-1/2$ has signs $(-,+,+,-)$ at the four corners. A polynomial kernel can supply such interactions to a linear classifier in feature space without writing down every mapped coordinate.{{cite:goodfellow_deep_learning2016_ch6}} (Ch. 6, §6.1, learned representation)

Two nonlinear threshold features also suffice. Let $h_{\rm OR}=f(x_1+x_2-1/2)$ and $h_{\rm AND}=f(x_1+x_2-3/2)$. The output $h_{\rm OR}-h_{\rm AND}$ is one if either switch is on but not both. An output threshold $f(h_{\rm OR}-h_{\rm AND}-1/2)$ gives the same binary rule. This construction uses an OR detector and an AND detector; the answered network question uses a distinct NAND-and-OR construction, while the feature-space question explores a product coordinate.{{cite:goodfellow_deep_learning2016_ch6}} (Ch. 6, §6.1, two hidden units)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Suppose one threshold unit produces XOR. The negative inputs require $b<0$ and $b+w_1+w_2<0$, while the positive inputs require $b+w_1\geq0$ and $b+w_2\geq0$. Adding the positive inequalities gives $2b+w_1+w_2\geq0$; adding the negative inequalities gives $2b+w_1+w_2<0$, a contradiction. For the proposed nonlinear construction, the pairs $(h_{\rm OR},h_{\rm AND})$ at $(0,0),(0,1),(1,0),(1,1)$ are respectively $(0,0),(1,0),(1,0),(1,1)$. Their differences are $(0,1,1,0)$, exactly XOR.{{cite:goodfellow_deep_learning2016_ch6}} (Ch. 6, §6.1, pp. 167–171)
:::
:::

## Statistical use
XOR is a compact diagnostic for what a model class can express. A linear or logistic classifier using only $x_1$ and $x_2$ has a linear decision boundary and cannot give all four corners their labels, regardless of how long it is trained. Adding the interaction $x_1x_2$, a nonlinear hidden layer, or a suitable kernel changes the model class. Choosing among those routes then depends on the data and the question: a hand-written interaction is transparent when the scientific mechanism suggests it; learned features can be useful when interactions are numerous or unknown.{{cite:goodfellow_deep_learning2016_ch6}} (Ch. 6, §6.1, original and learned feature spaces)

If a dataset contains repeated measurements or noise, fitting the four exact corners is only a training-set check. Generalisation to points between corners depends on how the features extend beyond binary inputs. For instance, the polynomial expression gives $0.32$ at $(0.8,0.8)$, whereas the threshold OR-minus-AND rule there gives zero. Both match the binary truth table, but they make different predictions away from it.{{cite:goodfellow_deep_learning2016_ch6}} (Ch. 6, §6.1, distinction between four-point fit and generalisation)

## Worked example
Take the single threshold score $s=x_1+x_2-1/2$. At $(0,0),(0,1),(1,0),(1,1)$ it is $-1/2,1/2,1/2,3/2$, giving outputs $(0,1,1,1)$. This is OR: it gets the two mixed corners right but incorrectly sounds the alarm when both switches are on. Add the AND detector with score $x_1+x_2-3/2$; its outputs are $(0,0,0,1)$. Subtracting the detector outputs gives $(0,1,1,0)$, the desired XOR pattern. One additional nonlinear feature corrects the specific corner that the first threshold could not exclude.{{cite:goodfellow_deep_learning2016_ch6}} (Ch. 6, §6.1, two-hidden-unit idea)

**Your turn.** For the same four binary inputs, define XNOR to be one when the switches agree. Use the two detector outputs above to write an XNOR expression, and list its four outputs in the same order.

::: {.callout-tip collapse="true" title="Answer"}
Since XOR is $h_{\rm OR}-h_{\rm AND}$, XNOR is $1-h_{\rm OR}+h_{\rm AND}$. Its outputs are $(1,0,0,1)$. The complement changes which corners are positive, but the two diagonals still intersect, so one affine threshold in the original coordinates cannot separate XNOR either.{{cite:goodfellow_deep_learning2016_ch6}} (Ch. 6, §6.1, XOR geometry)
:::

## Common misconceptions
The failure is not that a perceptron learning rule needs more iterations; no one-line separator exists for these labels. Adding linear hidden layers alone does not solve XOR, because a composition of affine maps is still affine. A sigmoid applied only after one affine score changes probabilities but not the linear boundary between labels. Finally, an exact four-corner fit does not identify a unique function between the corners, as the continuous-input example shows.{{cite:goodfellow_deep_learning2016_ch6}} (Ch. 6, §6.1, pp. 167–171)

## Assumptions and limits
The impossibility proof assumes one affine threshold applied directly to the two original binary inputs. If the label at $(1,1)$ changes from zero to one, the rule becomes OR, and $x_1+x_2-1/2$ separates it. If a recorded input such as $(0,1)$ appears twice with contradictory labels, even a deterministic nonlinear function of that input cannot fit both observations; a probability or noise model is needed. With continuous-valued inputs, the four-corner truth table leaves interpolation unresolved, so test predictions on the actual input range rather than relying on the toy fit alone.{{cite:goodfellow_deep_learning2016_ch6}} (Ch. 6, §6.1, four-point setup and generalisation caveat)

## Connections
[Linear separability](linear-separability.qmd) describes the boundary condition that XOR violates in its original coordinates. The [perceptron](perceptron.qmd) and its [learning rule](perceptron-learning-rule.qmd) operate within that linear class. A nonlinear [activation function](activation-function.qmd) lets [hidden layers](hidden-layer.qmd) learn new coordinates, while a [polynomial kernel](polynomial-kernel.qmd) introduces interactions for a separator in feature space. These approaches alter representation; training and regularisation then determine which represented rule is learned.{{cite:goodfellow_deep_learning2016_ch6}} (Ch. 6, §6.1 and §6.5)

## History
The inability of early single-layer perceptrons to represent XOR became a standard example of the limits of linear threshold models. Goodfellow and coauthors recount how criticism of that limitation influenced neural-network research. Multilayer models with nonlinear hidden units removed the representational obstacle; Rumelhart, Hinton and Williams's 1986 paper developed back-propagation for learning useful internal representations. The distinction between a model's capacity and an algorithm's ability to train it remains the lasting lesson of the example.{{cite:goodfellow_deep_learning2016_ch6}} (Ch. 6, §6.6, pp. 220–221){{cite:rumelhart_hinton_williams1986}} (pp. 533–536)
