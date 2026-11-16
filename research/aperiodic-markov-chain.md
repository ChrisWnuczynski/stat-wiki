# Aperiodic Markov chain — rank 158

Type: concept/topic. Baseline 430 words, zero figures. Original page has the period definition, two-state alternation, an example link, two incoming practice questions, and its navigation and infobox; all are to remain.

## Sources opened

- UC Berkeley EECS 126, *Markov Chains* (Spring 2019), full course PDF through the source reader, pp. 1–2 and 12–13, §§1 and 2.4. The PDF explicitly defines period, states its class property and the irreducible positive-recurrent aperiodic convergence theorem. It also distinguishes stationarity from convergence. The note's claim that all entries of a common power become positive is read only in the finite-state setting here; on a general infinite state space it is too broad.
- Dodge (2008), printed pp. 330–331, Markov biographical entry. This supports the historical connection of Markov's work to dependent random processes, not an attribution of the specific aperiodicity theorem.
- Existing StatWiki source chapter `sources/stat3004/chapters/sp-05-classes-and-reversibility.qmd` §§Classes and period, Limiting distributions and the linked probability chapter, checked against the Berkeley course notes. This is background, not a bibliography citation.

## Fact ledger

- **Checked:** Period is the gcd of positive-probability return times and is constant across a communicating class (Berkeley §2.4, p. 12). Independent proof supplied on the article.
- **Checked:** Finite irreducible aperiodic chains converge to their unique stationary distribution (Berkeley §2.4, pp. 12–13). A finite-state positive-power and contraction proof is supplied.
- **Checked:** Stationarity and time-averaged occupation do not require aperiodicity; deterministic two-state alternation has invariant `(1/2,1/2)` but oscillating one-time laws (Berkeley §§1, 2.3–2.4, pp. 2, 9, 12–13). Matrix powers and stationary vectors checked with SymPy.
- **Checked:** A self-loop is sufficient, not necessary. The three-state example has return lengths 3 and 5, gcd 1, no self-loops, and invariant `(1/5,2/5,2/5)`. Computed from its transition matrix.
- **Assumed:** Markov's historical role is stated only at the level described by Dodge p. 331; no historical origin is claimed for the word *aperiodic*.
- **Disputed:** The Berkeley note's general countable-state phrasing of eventual positivity of an entire matrix cannot hold without extra conditions. The article restricts that assertion to finite irreducible aperiodic chains and proves it there.

## Arithmetic

The check script asserts all printed probabilities, stationary-vector coordinates, powers, and the two-state worked/Your-turn numbers. It checks the preserved question links and no figure loss.
