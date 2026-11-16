# Communicating classes

Type: Concept. Rank 222. Tier: full.

## Material checked

- **Checked:** Baseline 194 words and no figures. The source chapter's accessibility definition is the same relation as Siegrist's leads-to relation, including the zero-step case.
- **Checked:** Kyle Siegrist, *Transience and Recurrence*, §4, `https://www.randomservices.org/random/markov/Recurrence.html`. Closed sets, irreducible sets, the to-and-from equivalence, the two-state matrix with classes $\{0\}$ and $\{1\}$, and the fact that recurrence is constant on a class. The finite-set argument uses finiteness explicitly.
- **Checked:** Kyle Siegrist, *Periodicity*, §5, `https://www.randomservices.org/random/markov/Periodicity.html`. Period as a gcd, the class property and its proof, the self-loop criterion, and the three-state chain with returns at times 2 and 3 and no self-loop.
- **Checked by code:** the alternation satisfies $P^2=I$ and $(1/2,1/2)P=(1/2,1/2)$; the paths $a\to c\to a$ and $a\to b\to c\to a$ have probabilities $2/3$ and $1/3$; $\gcd(2,3)=1$.
- **Assumed:** The chain is time-homogeneous, as in both Siegrist sections. Accessibility uses a strictly positive probability, with no numerical cutoff.
- **Disputed:** Nothing. A class need not be closed, and a closed set need not be one class; both failures are Siegrist's two-state example.

## Sources opened and used

1. Kyle Siegrist, §4 *Transience and Recurrence*, `https://www.randomservices.org/random/markov/Recurrence.html`. New pending key `siegrist2022_markov_recurrence`.
2. Kyle Siegrist, §5 *Periodicity*, `https://www.randomservices.org/random/markov/Periodicity.html`. New pending key `siegrist2022_markov_period`.

## Skipped

The integer-line random walk was not used. An earlier draft called it transient, which is the wrong classification, and the sentence now stops at the finiteness step Siegrist actually gives.
