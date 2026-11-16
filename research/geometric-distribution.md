# Geometric distribution

Type: Distribution. Rank 237. Tier: full.

## Material checked

- **Checked:** Frozen baseline 2,173 body words and three figures. The page keeps the trial-count mass $p(1-p)^{x-1}$, the mean $1/p$, the survival example $(3/4)^3=27/64\approx 0.4219$, and the three plots.
- **Checked:** Dodge, printed pp. 226–227. The entry defines the number of failures before the first success, with mass $p q^k$, mean $q/p$, and variance $q/p^2$, and identifies it as the negative binomial law with one required success. The series $1+2q+3q^2+\cdots=1/(1-q)^2$ is the step in the mean calculation.
- **Checked by code:** For $p=0.2$, the masses $0.2$, $0.16$, $0.128$ sum to $0.488$, the tail $0.512$ matches, the variance is $20$, $\sqrt{20}$ rounds to $4.472$, and $0.8^{10}$ rounds to $0.1074$. For $p=1/4$, $27/64$ rounds to $0.4219$ and the failure-count mean is $3$.
- **Assumed:** Trials are independent with a constant success probability. The memoryless identity is for that model.
- **Disputed:** None. The two conventions differ by one. The page states both and computes with the trial count.

The catalogue tail-sum proof of the mean is replaced by the proof in Properties, which includes that tail sum and Dodge's variance shift.

## Sources opened and used

1. Yadolah Dodge, *The Concise Encyclopedia of Statistics* (2008), pp. 226–227. Key `dodge2008`.
