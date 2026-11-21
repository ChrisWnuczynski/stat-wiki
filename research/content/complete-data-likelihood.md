## Motivating example
Two mixture cases have component probabilities $0.4$ and $0.6$. With the labels known, the first case contributes $0.4\times 0.5=0.2$ and the second contributes $0.6\times 0.8=0.48$. The complete likelihood of the labelled pair is $0.096$.

## Intuition — The likelihood if the labels were seen
A mixture observation is produced by one component, but the component label is not in the data. The observed likelihood sums over those labels, and the logarithm of that sum is awkward to maximise. The complete-data likelihood is the joint probability of the measurement and the label. With the label written as a one-hot indicator, the joint contribution is a product, not a sum inside a logarithm. Replacing the unseen indicator by its conditional probability is the step that turns this likelihood into the function EM actually maximises.{{cite:bishop2006}} (eqs. 9.35–9.36, p. 443)

## Definition — A product over the active component
Give case $i$ a latent vector $z_i$ with a single $1$, in coordinate $h$ when component $h$ produced the case. For component densities $f_h$ and weights $\pi_h$,
$$
L_C=\prod_{i=1}^n\prod_{h=1}^H\bigl(\pi_h f_h(x_i)\bigr)^{z_{ih}},
\qquad
\ell_C=\sum_{i=1}^n\sum_{h=1}^H z_{ih}\bigl[\ln\pi_h+\ln f_h(x_i)\bigr].
$$
Bishop writes the same product for normal component densities. Every factor with exponent $0$ equals $1$, so each case keeps only the component that generated it. The observed likelihood of one case is the sum of those component contributions, not any single one of them.{{cite:bishop2006}} (eqs. 9.35–9.36, p. 443)

::: {.callout-note collapse="true" title="Proof"}
::: {.proof}
Fix one case and two components, and suppose $z_1=1$, $z_2=0$. The inner product is $(\pi_1 f_1)^{1}(\pi_2 f_2)^{0}=\pi_1 f_1$. If instead $z_2=1$, the product is $\pi_2 f_2$. The observed density of the case is the sum of those two mutually exclusive contributions, $\pi_1 f_1+\pi_2 f_2$. Taking logarithms turns the complete-data product across cases into the sum $\ell_C$. Linearity in $z_{ih}$ is immediate from that sum.{{cite:bishop2006}} (eq. 9.36, p. 443)
:::
:::

## Worked example — Two cases, two components
Take $\pi_1=0.4$, $\pi_2=0.6$. For the first case let $f_1=0.5$ and $f_2=0.1$, and suppose the label is component $1$. Its complete contribution is $0.4\times 0.5=0.2$. For the second case let $f_1=0.2$ and $f_2=0.8$, with label component $2$. Its contribution is $0.6\times 0.8=0.48$. The complete likelihood of the two labelled cases is $0.2\times 0.48=0.096$, and $\ell_C=\ln 0.096=-2.343$ to three decimal places.

The observed likelihood does not use the labels. The first case contributes $0.4\times 0.5+0.6\times 0.1=0.26$. The second contributes $0.4\times 0.2+0.6\times 0.8=0.56$. The product is $0.26\times 0.56=0.1456$, with logarithm $-1.927$ to three decimal places. The complete value $0.096$ is smaller because it includes one latent label rather than summing both.{{cite:bishop2006}} (eqs. 9.35–9.36, p. 443)

**Your turn.** Keep the same densities and weights, and switch the first label to component $2$. Find that case's complete contribution, and the complete likelihood of the two cases if the second label stays on component $2$.

::: {.callout-tip collapse="true" title="Answer"}
The first case now contributes $0.6\times 0.1=0.06$. With the second contribution still $0.48$, the complete likelihood is $0.06\times 0.48=0.0288$.
:::

## Connections — What the E step is averaging
The [EM algorithm](em-algorithm.qmd) replaces each $z_{ih}$ in $\ell_C$ by its conditional expectation given the case, then maximises. Those conditional probabilities are the responsibilities in a [finite mixture model](finite-mixture-model.qmd). The [likelihood function](likelihood-function.qmd) of the observed sample is the product of the sums, which is what $\ell_C$ avoids. The algebra is the same for a normal component and for any other component density that the indicator simply switches on.{{cite:bishop2006}} (eqs. 9.30 and 9.36, pp. 440–443)
