# XOR problem — research notes

- **Checked:** Goodfellow, Bengio and Courville, *Deep Learning*, author-hosted full Ch. 6 HTML, §6.1 (pp. 166–171): four binary corners, failure of an affine score, nonlinear hidden features and an explicit two-hidden-unit solution. §6.6 (pp. 220–221) recounts the historical perceptron limitation and later multilayer training.
- **Checked:** Rumelhart, Hinton and Williams (1986), full four-page *Nature* original from Hinton's University of Toronto author-hosted PDF, pp. 533–536: backpropagation learns internal representations in multilayer units. It is cited only for that historical role, not for an alleged unique invention or a universal convergence guarantee.
- **Checked:** StatWiki source's existing single-threshold proof and its OR/AND constructions against algebra and direct code evaluation; distinct question-bank answers are `ex-sl-14-5` (NAND/OR construction) and `ex-sl-17-10` (nonlinear product feature), both worked in the bank.
- **Checked by code:** all four XOR corners, one-line contradiction, two-hidden-unit threshold network, quadratic feature score, and numeric Your turn answer are in `checks/xor-problem.py`.
- **Assumed:** four exact binary inputs and deterministic labels. Continuous noisy coordinates and statistical generalisation require a separately specified sampling model.
- **Disputed/limited:** XOR does not show neural networks cannot learn nonlinear patterns; it shows a specific one-layer affine-threshold architecture cannot fit these labels. Backpropagation's practical 1986 role should not be called the sole invention of reverse differentiation.
- **Dodge:** no relevant XOR or perceptron article located in the Dodge index; no history attributed to it.
