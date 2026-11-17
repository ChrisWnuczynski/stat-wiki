## Lead context
XOR's two positive corners lie on opposite diagonals from its negative corners, obstructing separation by one affine threshold.

## Motivating example
Two binary switches should activate an output when exactly one is on. Each input matters, but its effect reverses with the other input: changing the second switch from zero to one raises the output if the first is zero and lowers it if the first is one. One affine score assigns a fixed coefficient to that input and cannot implement the required rule with one threshold.{{cite:goodfellow_bengio_courville2016}} (§6.1, pp. 167–169)

## Statement
Let $f(z)=\mathbf1\{z\ge0\}$. There are no real $b,w_1,w_2$ such that $f(b+w_1x_1+w_2x_2)$ equals $x_1\mathbin{\mathrm{XOR}}x_2$ on every point of $\{0,1\}^2$. The limitation concerns a single affine threshold applied to the two input coordinates.{{cite:goodfellow_bengio_courville2016}} (§6.1, pp. 167–170)

## Proof
Correct output at $(0,0)$ requires $b<0$. The two positive corners require $b+w_1\ge0$ and $b+w_2\ge0$. Adding those inequalities gives $2b+w_1+w_2\ge0$. Correct output at $(1,1)$ requires $b+w_1+w_2<0$. Adding this last inequality to $b<0$ gives $2b+w_1+w_2<0$, contradicting the preceding bound. This includes boundary cases under the stated convention.{{cite:goodfellow_bengio_courville2016}} (§6.1, Fig. 6.1, p. 169)

## Intuition — The diagonal midpoints coincide
An affine score at a segment midpoint is the average of its scores at the endpoints. Both positive-corner scores would be nonnegative, so their midpoint $(1/2,1/2)$ would have nonnegative score. Both negative-corner scores would be strictly negative, making the same midpoint's score negative. Equivalently, the convex hulls of the two labelled point sets intersect. A halfspace classifier cannot put those two hulls on the required opposite sides.{{cite:boyd_vandenberghe2004}} (§2.1.4, pp. 23–24; §2.2.1, pp. 27–29)

## Generalizations — Nonlinear features change the represented class
On binary inputs, $x_1+x_2-2x_1x_2$ equals XOR exactly. Thresholding this expression at one half succeeds, but its interaction feature $x_1x_2$ is nonlinear in the two initial coordinates. It therefore changes the feature map rather than contradicting the theorem.{{cite:goodfellow_bengio_courville2016}} (§6.1, pp. 168–170)

Adding layers with only affine hidden maps does not suffice. If $h=Ax+c$ and the output score is $v^\top h+b$, substitution gives $(A^\top v)^\top x+(v^\top c+b)$, again one affine score. Composition of any finite number of affine maps remains affine. Nonlinear hidden activations are what permit a feedforward network to construct features that separate the XOR labels.{{cite:goodfellow_bengio_courville2016}} (§6.1, p. 168)

## Worked example
Use two hidden thresholds,
$$
h_{\rm OR}=f(2x_1+2x_2-1),\qquad
h_{\rm NAND}=f(3-2x_1-2x_2),
$$
and output $o=f(h_{\rm OR}+h_{\rm NAND}-3/2)$. The hidden units compute OR and NAND. Their joint truth table is

| Input | OR | NAND | Output score | Output |
|:--|--:|--:|--:|--:|
| $(0,0)$ | 0 | 1 | $-1/2$ | 0 |
| $(0,1)$ | 1 | 1 | $1/2$ | 1 |
| $(1,0)$ | 1 | 1 | $1/2$ | 1 |
| $(1,1)$ | 1 | 0 | $-1/2$ | 0 |

The output is the AND of the hidden values and equals XOR at all four inputs. Every displayed score stays away from its threshold, so the construction does not depend on how zero is labelled. A two-unit hidden representation permits the separation that failed in input space.{{cite:goodfellow_bengio_courville2016}} (§6.1, pp. 168–170)

**Your turn.** Change only the final output score to $3/2-h_{\rm OR}-h_{\rm NAND}$. Which Boolean rule results?

::: {.callout-tip collapse="true" title="Answer"}
All four scores change sign and none is zero. The outputs become $(1,0,0,1)$ in the displayed row order, giving XNOR, which is one exactly when the two inputs agree.
:::
