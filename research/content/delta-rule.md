## Motivating example
An error at an output must be translated into an update for each connection leading to that output. A local error derivative, or delta, organises that translation. It is a derivative with a sign determined by the loss; the parameter change also includes the negative learning rate and the input signal on the connection.{{cite:goodfellow_bengio_courville2016}} (§6.5.4, pp. 208–209)

## Properties — Deltas are derivatives with respect to weighted inputs
For sigmoid $g(z)=1/(1+e^{-z})$, $g'(z)=g(z)(1-g(z))=e^{-z}g(z)^2$. Under summed squared error $E=\sum_{i,k}(y_{ik}-o_{ik})^2$, define $\delta_{ik}^{(o)}=\partial E/\partial z_{ik}$. The chain rule gives $2(o_{ik}-y_{ik})o_{ik}(1-o_{ik})$. A hidden delta sums all downstream contributions, then multiplies by its local derivative:
$$
\delta_{iq}^{(h)}=h_{iq}(1-h_{iq})\sum_k w_{qk}\delta_{ik}^{(o)}.
$$
Since a weighted input is linear in each connection weight, its derivative with respect to that weight is the incoming activation. Thus $\partial E/\partial w_{qk}=\sum_i\delta_{ik}^{(o)}h_{iq}$, with the analogous input–hidden formula. This derives the delta update directly from the chain rule.{{cite:zhang_d2l2023}} (§5.3, backward propagation)

Using half the summed squared error removes the factor two from every delta. Binary cross-entropy paired with a sigmoid gives output delta $o-y$, without the extra sigmoid-slope factor. Indeed, differentiating $-y\log o-(1-y)\log(1-o)$ with respect to $o$ gives $(o-y)/\{o(1-o)\}$, which cancels the sigmoid derivative on the next chain-rule step. Hidden derivatives still require their activation derivatives. A formula valid for one pairing of output link and loss should not be transferred unchanged to another.{{cite:goodfellow_bengio_courville2016}} (§6.2.2.2, pp. 178–180)

## Interpretation — Saturation changes the learning signal
For target $y=1$ and weighted input $z=-8$, the sigmoid output is $0.00033535$, yet squared-error delta is only $-0.00067025$. At $z=-1$, the output is $0.268941$ and the delta is $-0.287470$. The former prediction is further from its target but has a much smaller derivative because the sigmoid is nearly flat. Cross-entropy deltas at those points are $-0.999665$ and $-0.731059$.{{cite:goodfellow_bengio_courville2016}} (§6.2.2.2, pp. 178–180)

## Worked example — From one output delta to two gradients
Suppose a sigmoid output has $o=0.6$, target $y=1$, hidden input $h=0.5$ and outgoing weight $w=1$. Its squared-error delta is $2(0.6-1)(0.6)(0.4)=-0.192$. The outgoing weight gradient is $-0.192(0.5)=-0.096$, so learning rate $0.1$ increases that weight by $0.0096$.{{cite:zhang_d2l2023}} (§5.3)

The hidden delta is $0.5(1-0.5)(1)(-0.192)=-0.048$. If the input to this hidden connection is $2$, its weight gradient is $-0.096$ and its update is also $+0.0096$. Those equal numbers arise from the particular activations and input; the two connections use different local derivatives. All downstream weights used to compute the hidden delta are evaluated at the forward-pass parameter vector.{{cite:goodfellow_bengio_courville2016}} (§6.5.4, pp. 208–209)

**Your turn.** Use half squared error in this calculation while leaving the learning rate fixed. What happens to the two updates?

::: {.callout-tip collapse="true" title="Answer"}
All deltas and gradients halve. Each update is $+0.0048$. Doubling the learning rate would reproduce the squared-error updates.
:::
