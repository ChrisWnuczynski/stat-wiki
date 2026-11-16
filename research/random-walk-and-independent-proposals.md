# Random-walk and independent proposals: research notes

## Sources opened

- **Checked:** Metropolis, Rosenbluth, Rosenbluth, Teller & Teller (1953), original *Journal of Chemical Physics* paper, §II, printed p. 1088, via university-hosted journal PDF and DOI/publisher record. The paper uses local symmetric displacements, accepts favourable energy moves, accepts less favourable moves with an exponential probability, and includes rejected states in averages.
- **Checked:** W. K. Hastings (1970), original *Biometrika* paper, §§2.1–2.3, printed pp. 99–101, via an author-associated probability.ca PDF and publisher DOI record. Presents the proposal/target ratio, detailed balance, symmetric Metropolis choice, and examples where proposal scale affects coverage.
- **Checked:** inherited `sources/book/chapters/bayes-04-mcmc.qmd`, section “Random-walk and independent proposals” and adjoining proposal-design discussion. Preserves the existing Normal-target trace figure and the Gibbs/Metropolis comparison. The figure's qualitative message is supported by Hastings's proposal-scale discussion.
- **Checked for history only:** Dodge, *The Concise Encyclopedia of Statistics*, “Monte Carlo Method,” pp. 359–360, which gives the broad historical context and cites Metropolis & Ulam 1949. It does not give the Hastings correction, so it is not cited for the acceptance rule.

## Mathematical checks

- **Checked:** Hypothetical target on states $0,1,2$ has masses $(1/2,1/3,1/6)$. A symmetric nearest-neighbour-with-hold proposal has $q(1\mid0)=q(0\mid1)=1/2$ and $q(2\mid1)=q(1\mid2)=1/2$. For $0\to1$, random-walk acceptance is $2/3$ and stationary flow each way is $1/6$.
- **Checked:** Independent proposal masses $g=(1/6,1/2,1/3)$ give acceptance $2/9$ for $0\to1$ and one for $1\to0$. The two stationary flows equal $1/18$. Dropping the $g$ ratio incorrectly gives $2/3$ for $0\to1$.
- **Checked:** For $1\to2$, random-walk acceptance is $1/2$ and independent-proposal acceptance is $3/4$.
- **Checked:** For nonnegative $a,b$, $a\min(1,b/a)=\min(a,b)$ when $a>0$; this gives the detailed-balance proof, with zero-flow cases handled separately.

## Scope decisions

- **Assumed:** The three-state target and proposals are pedagogical, not a real posterior.
- **Disputed:** Independence of the proposal from the *current state* does not make successive accepted states independent; rejection repeats states.
- **Disputed:** A high acceptance rate alone measures efficiency. Local steps can be almost always accepted while exploring slowly; a badly matched independence proposal can miss important regions.
