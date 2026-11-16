# Rank 64: Metropolis–Hastings algorithm

## Sources opened

- Hastings (1970), *Biometrika* 57, pp. 97–109, Oxford Academic publisher abstract: a generalization of the 1953 Metropolis method, including Monte Carlo error assessment.
- Metropolis et al. (1953), *Journal of Chemical Physics* 21, pp. 1087–1092, AIP publisher abstract: molecular configuration Monte Carlo.
- Geyer, University of Minnesota Markov-chain notes, §5.5 and Theorem 4, full algorithm, Hastings ratio, symmetric-proposal special case, and proof of reversibility.
- Geyer, University of Minnesota Bayesian MCMC notes, §§9.1–9.2, dependent sampling and error assessment.

## Fact audit

- **Checked:** The Hastings acceptance ratio is $r(x,y)=h(y)q(y,x)/[h(x)q(x,y)]$ and $\alpha=\min(1,r)$, using unnormalized target $h$; Geyer §5.5.
- **Checked:** The accepted-flow equality is $h(x)q(x,y)\alpha(x,y)=\min\{h(x)q(x,y),h(y)q(y,x)\}$, symmetric in $x,y$; Geyer Theorem 4.
- **Checked:** Symmetric proposals cancel the proposal ratio; Geyer §5.5.
- **Checked:** Stationarity alone is not convergence from any starting point; irreducibility and recurrence conditions matter; Geyer §5.5 surrounding discussion.
- **Assumed:** Small finite-state worked examples illustrate the ratio but do not establish mixing quality.
- **Disputed:** The exact attribution of each coauthor's implementation contribution in the 1953 paper is not established by the publisher abstract; omit.

Dodge index directory was absent from `~/statwiki-sources/dodge2008`.
- **Checked numerically:** Worked two-state target $(1/4,3/4)$ with proposals $q(B\mid A)=0.8$, $q(A\mid B)=0.4$ gives ratios $3/2$ and $2/3$, accepted transitions $4/5$ and $4/15$, and equal equilibrium flows $1/5$; the $B$ stay probability is $11/15$. Practice target $(2/3,1/3)$ gives ratio $1/6$, accepted transitions $1/10$ and $1/5$, and equal flows $1/15$.
- **Checked:** Ising (1925), pp. 253–254, original public-domain scan accessible from a university lecture archive, for the two-state magnetic model referred to by the inherited paragraph.

The source chapter citations copied to the article were given locators and aligned with Geyer §5.5, Hastings' publisher abstract, and Metropolis et al.'s publisher abstract; dependent MCMC topic pages will be checked in the full rebuild.

## Result

The article grew from 958 to 2,325 body words, with zero figures before and after. Its inherited collapsed detailed-balance proof was retained and explained; a second proof box was unnecessary. It now includes a numeric two-state worked example, hidden Your turn answer, and two answered question-bank items (`c-12`, `c-14`). The full build, 67 tests, rank-specific flow check, offline verification of 451 bibliography entries, and `git diff --check` passed. Quarto HTML rendering was unavailable; the generator used the system Pandoc shim.
