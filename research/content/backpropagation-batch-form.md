## Motivating example
A hidden weight affects the loss through every output that depends on it. Computing each path separately repeats intermediate derivatives. Backpropagation accumulates the downstream derivatives once, and batch training sums the resulting contributions from all observations before moving the parameters.{{cite:goodfellow_bengio_courville2016}} (§6.5.2–6.5.4, pp. 201–209)

## Properties — One gradient evaluated at one parameter vector
Let $E=\sum_i\ell_i(w)$. Differentiation is linear, so $\nabla E=\sum_i\nabla\ell_i$. All terms must be evaluated at the same $w$ for this to be the batch gradient. Updating after each observation instead gives a sequence of different evaluation points. It is a different optimisation procedure, even if the observations and learning rate coincide. Backpropagation computes derivatives; gradient descent specifies how to use them.{{cite:goodfellow_bengio_courville2016}} (§6.5, p. 200; §6.5.7, pp. 214–216)

For sigmoid hidden and output units and squared loss without a factor $1/2$,
$$
\delta_{ik}^{(o)}=2(o_{ik}-y_{ik})o_{ik}(1-o_{ik}),\quad
\delta_{iq}^{(h)}=h_{iq}(1-h_{iq})\sum_k w_{qk}\delta_{ik}^{(o)}.
$$
The output gradients sum $\delta_{ik}^{(o)}h_{iq}$ and the incoming gradients sum $\delta_{iq}^{(h)}x_{ij}$. Biases have input signal one. Matrix multiplication implements these sums, with the orientation determined by whether observations occupy rows or columns.{{cite:zhang_d2l2023}} (§5.3, backward propagation)

An average loss $\bar E=E/n$ has gradient $\nabla E/n$. A learning rate $\eta$ for the sum matches learning rate $n\eta$ for the average when every other term is scaled consistently. A penalty added to the loss also contributes its derivative; it must not accidentally be multiplied by the batch size.{{cite:zhang_d2l2023}} (§5.3, computational graph of the objective)

## Worked example — Two patterns before one update
Take two inputs, two sigmoid hidden units, one sigmoid output, and incoming rows $(0.1,0.4,-0.3)$ and $(-0.2,0.3,0.2)$, with each bias listed first. Let the output weights be $(0.2,0.5,-0.4)$. For pattern $(x,y)=((1,0),1)$, the forward pass gives $h=(0.622459,0.524979)$, $o=0.574745$ and squared error $0.180842$. The output delta is $-0.207876$ and the hidden deltas are $(-0.024426,0.020736)$.{{cite:goodfellow_bengio_courville2016}} (§6.5.4, pp. 208–209)

Now include $((0,1),0)$ without updating between patterns. In the same weight order, the summed gradient is
$$
(0.009549,-0.024426,0.033975,\ -0.006717,0.020736,-0.027453,\ 0.066650,-0.005812,0.028132).
$$
At learning rate $0.5$, the output weights become $(0.166675,0.502906,-0.414066)$. The single-pattern output-bias gradient is negative, while the two-pattern sum is positive. This is cancellation of contributions to one objective, rather than an instruction to move a weight twice. Central differences of the whole summed loss give the same vector.{{cite:zhang_d2l2023}} (§5.3, backward propagation)

**Your turn.** If the objective is the average of these two pattern losses, what learning rate reproduces the same update?

::: {.callout-tip collapse="true" title="Answer"}
The average gradient is half the sum. Use learning rate $1$ instead of $0.5$ to obtain the same parameter change.
:::

