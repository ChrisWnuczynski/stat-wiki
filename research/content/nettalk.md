## Motivating example
The pronunciation of a letter depends on its surrounding text. A neural network can use a short character window to predict a pronunciation code for its centre, learning the mapping from labelled examples. NETtalk demonstrated this approach with a feedforward network trained by error backpropagation.{{cite:sejnowski_rosenberg1987}} (§§1–2, pp. 146–150)

## Definition — Context as an input representation
A seven-character window provides three characters on each side of the central character. Encoding each position with 29 binary input units gives $7\times29=203$ inputs. The architecture with 80 hidden units and 26 outputs maps that context to a distributed pronunciation code. The outputs encode speech features rather than a single integer label for a character.{{cite:sejnowski_rosenberg1987}} (§2, pp. 147–151)

At each hidden unit, weighted inputs and a bias determine an activation; output units combine hidden activations in the same way. Backpropagation differentiates the training error through those transformations. Adjusting the weights changes the mapping, while choosing the window and output coding determines what information and targets the learner receives.{{cite:sejnowski_rosenberg1987}} (§2, pp. 148–150)

## Worked example — Connections, biases and thresholds
A fully connected network with $d$ inputs, $h$ hidden units and $c$ outputs has $dh+hc$ connections. One bias per hidden and output unit adds $h+c$, giving $(d+1)h+(h+1)c$. For $(d,h,c)=(203,80,26)$ this is
$$
203(80)+80(26)+80+26=18426.
$$
The connection count alone is $18320$. Counting thresholds on all 309 units, including the 203 input units, gives $18320+309=18629$, the total reported with the architecture. Parameter counts require specifying which thresholds are included.{{cite:sejnowski_rosenberg1987}} (§2, p. 148; Fig. 1, p. 147)

Reducing the hidden layer to 50 units gives $(203+1)50+(50+1)26=11526$ hidden/output-bias parameters. A toy architecture with 15 inputs, 2 hidden units and 3 outputs gives $(15+1)2+(2+1)3=41$. These products explain why a modest change in layer width changes the parameter count substantially.

**Your turn.** A network has 10 inputs, 5 hidden units and 3 outputs. Count its connections and hidden/output biases.

::: {.callout-tip collapse="true" title="Answer"}
There are $10(5)+5(3)=65$ connections and $5+3=8$ biases, giving $73$ parameters.
:::

## Statistical use — Weight decay and held-out performance
With objective $E_0(w)+(\lambda/2)\sum_jw_j^2$, the penalty contributes $\lambda w_j$ to the gradient. A gradient step therefore contains a shrinkage term $-\epsilon\lambda w_j$ as well as the data-gradient term. A NETtalk weight-decay experiment used a different layer configuration from the 80-hidden-unit architecture, so its tuning result depends on its own model and sample.{{cite:krogh_hertz1992}} (§1, p. 951; §6, pp. 955–956)

A large count of scalar output targets does not establish a correspondingly large number of independent observations: targets for the same window share inputs, and neighbouring windows overlap. Training loss and performance on held-out words consequently answer different questions. A penalty setting needs evaluation in the intended prediction setting rather than being inferred from a parameter-to-target ratio.{{cite:sejnowski_rosenberg1987}} (§§2–3, pp. 150–155){{cite:krogh_hertz1992}} (§6, pp. 955–956)
