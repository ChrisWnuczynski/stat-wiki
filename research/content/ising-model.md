## Motivating example
Binary observations on a grid can form patches: nearby sites tend to agree even though no single site is fixed in advance. An Ising model gives a joint probability to the whole configuration through interactions on neighbouring pairs. It is an energy-based model whose local factors describe a global distribution.{{cite:goodfellow_bengio_courville2016}} (§§16.2.2–16.2.4, pp. 562–567)

## Definition — Count each interaction edge once
For a finite undirected graph with spins $x_i\in\{-1,+1\}$, define
$$p(x)=Z^{-1}\exp\!\left\{\sum_{\{i,j\}\in E}\beta_{ij}x_ix_j+\sum_i h_ix_i\right\}.$$
Every unordered edge appears once. Positive $\beta_{ij}$ favours equal spins on that edge and negative coupling favours opposite spins. The field $h_i$ favours one sign at that site. The partition function $Z$ is the sum of the positive weights over all configurations. It makes this finite model a probability distribution.{{cite:goodfellow_bengio_courville2016}} (§16.2.4, eq. 16.7, pp. 566–567)

## Properties — Local conditional probabilities and flips
Condition on all spins except $x_i$ and define $H_i=h_i+\sum_{j:\{i,j\}\in E}\beta_{ij}x_j$. Factors that do not involve $i$ cancel in the conditional distribution. Its odds for $x_i=+1$ rather than $-1$ are $e^{2H_i}$, giving
$$\Pr(x_i=+1\mid x_{-i})=\frac1{1+e^{-2H_i}}.$$
Changing a spin from $x_i$ to $-x_i$ gives target ratio $e^{-2x_iH_i}$. Both identities follow by subtracting the two exponents; neither requires evaluating $Z$.{{cite:goodfellow_bengio_courville2016}} (§§16.2.2, 16.2.4, local factors and energy)

A symmetric single-spin proposal accepts that flip with probability $\min(1,e^{-2x_iH_i})$. The Metropolis rule accepts a move to lower energy and randomises a move to higher energy according to its Boltzmann weight ratio.{{cite:metropolis1953}} (p. 1088)

## Worked example — Two interacting spins
With two sites, one edge, $\beta=1/2$ and zero fields, the aligned configurations have weight $e^{1/2}$ each and the two opposed configurations have weight $e^{-1/2}$ each. Thus $Z=2e^{1/2}+2e^{-1/2}=4.510504$. The probability of alignment is $0.731059$. Given the second spin is positive, the probability the first is positive is also $1/(1+e^{-1})=0.731059$. Proposing to flip one spin of an aligned pair has acceptance probability $e^{-1}=0.367879$.

**Your turn.** What is the acceptance probability for the reverse flip, from an opposed pair to an aligned pair?

::: {.callout-tip collapse="true" title="Answer"}
The target ratio is $e>1$, so the reverse proposal is accepted with probability one.
:::

## Statistical use — Local computation and global uncertainty
For a large graph, summing over all $2^m$ spin configurations can be expensive, while a local flip uses only one site's neighbours. Cancellation of a normalising constant makes sampling feasible, but does not imply that successive configurations are independent or that a short run explores every high-probability region. Mixing and statistical error still need assessment.{{cite:metropolis1953}} (§II, pp. 1088–1089)
