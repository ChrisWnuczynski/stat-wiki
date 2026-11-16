# Artificial neuron — rank 138 research

## Sources read

- **Checked:** Goodfellow, Bengio and Courville, *Deep Learning* (2016), author and publisher-hosted full Chapter 6, `https://www.deeplearningbook.org/contents/mlp.html`. Sections 6.1–6.3 explain feedforward composition, the XOR limitation, output units, sigmoid activation, ReLU and backpropagation gradients. The chapter is available through the authors' official online book.
- **Checked:** McCulloch and Pitts (1943), original “A Logical Calculus of the Ideas Immanent in Nervous Activity,” pp. 115–117, full scan opened from a university-hosted research archive `https://www.cs.cmu.edu/~cdm/resources/McCullochPitts1943.pdf`; its publisher DOI remains in the inherited bibliography. It treats all-or-none activity and thresholds as a logical model.
- **Checked:** Rosenblatt (1958), original “The Perceptron: A Probabilistic Model for Information Storage and Organization in the Brain,” pp. 386–390, full paper opened from a Carnegie Mellon course archive `https://www.cs.cmu.edu/~epxing/Class/10715/reading/Rosenblatt.perceptron.pdf`; its DOI remains the citation target. It motivates the trainable perceptron as a recognition model.
- **Checked:** The authorized Dodge index has no artificial-neuron, perceptron or neural-network entry, so its orientation role is limited for this page.
- **Assumed:** The weighted-affine-plus-activation formulation is a mathematical abstraction; the page does not claim a one-to-one biological account of individual neurons.

## Baseline and numerical checks

- **Checked:** Baseline has 794 body words and zero figures. It defines the weighted input, bias, threshold and sigmoid, includes an AND example with nets $-1.5,-0.5,-0.5,0.5$ and sigmoid outputs about $.182,.378,.378,.622$, and connects a single unit to logistic regression and hidden layers. All are retained in generated content.
- **Checked:** With $x=(2,1)$, $w=(.5,-1)$ and $b=.25$, net input is $.25$, ReLU is $.25$, sigmoid is $.562177$ and derivative $.246134$. With $x=(0,1)$, net is $-.75$, ReLU zero and sigmoid $.320821$.
- **Checked:** Your-turn $x=(3,1)$, $w=(1,-2)$, $b=.5$ gives net $1.5$, ReLU $1.5$, sigmoid $.817574$ and derivative $.149146$; $x=(0,1)$ gives net $-1.5$ and ReLU zero.
- **Checked:** Question pages `ex-sl-14-3` and `ex-sl-14-5` have substantive worked answers about a unit's decision boundary and a two-hidden-unit XOR network. They exercise different aspects of the page without repeating the new numerical worked example.

## Proof scope

The single collapsed box proves the sigmoid derivative and its maximum, shows that a composition of affine layers is affine, and derives a contradiction for a one-unit threshold representation of XOR.
