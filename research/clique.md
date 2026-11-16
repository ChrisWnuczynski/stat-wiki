# Clique

Type: Concept. Rank 272. Tier: lighter.

## Material checked

- **Checked:** Baseline 310 words, 0 figures. Evans, *Graphical Models*, §4.3: a complete set has every pair adjacent, a clique is a maximal complete set, and a density factorises according to the graph when it is a product of clique potentials (equation 4.1). The six-vertex edge list and the four-vertex examples were enumerated directly.
- **Checked by code:** The three triples on the six-vertex edge list are complete; {1,2,4} is not. Adding edge 14 to the pendant graph moves the clique from {3,4} to {1,3,4}. `checks/clique.py`.
- **Assumed:** None beyond the edge lists stated in the article.
- **Not opened:** Lauritzen 1996 and the Hammersley–Clifford paper. The full equivalence of the Markov property and clique factorisation is not reproved.

## Sources opened

1. Robin J. Evans, *Graphical Models*, 2025, §4.3, equation 4.1, https://www.stats.ox.ac.uk/~evans/gms/_book/ug.html. Key `evans2025_graphical`.
