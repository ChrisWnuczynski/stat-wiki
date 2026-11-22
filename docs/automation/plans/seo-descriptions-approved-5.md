> **Handover note (20 Nov 2026):** Editor-approved meta-description overrides. Implement after #90 merges (search_meta.py). Copied from the previous automation's private workspace; paths were rewritten to repo paths.

# Editor-approved descriptions (19 Nov 2026, 8:05pm)

Mechanism: change a lead only where the lead itself is wrong (item 1, item 5 summary). Otherwise add a small per-page description override (Grok Bot builds it in search_meta.py). Generator-wide: strip citation markers ([1], {{cite}}) and cut at a sentence boundary, never mid-clause.

1. articles/conditional-probability
   Lead first sentence -> "In probability theory, the conditional probability is the probability of an event, computed within the outcomes of a second event that has positive probability." Keep the remaining lead sentences.
   Description (143): Conditional probability measures an event inside a second event of positive probability, keeping relative weights; it implies no order in time.
2. articles/expected-duration-of-a-random-walk (override; no lead change)
   Description (137): For a random walk absorbed at either end of a finite interval, the mean number of steps to absorption follows from a first-step equation.
3. articles/wishart-distribution (override; no lead change)
   Description (149): The Wishart distribution is the law of a scatter matrix built from independent zero-mean normal vectors: a matrix analogue of a chi-squared variable.
4. questions/ex-prob-hazard-survival (override; exercise wording unchanged; no difficulty label, and the answer is not given away)
   Description (144): Given a lifetime's density, survival function and hazard, this question shows how the survival function is recovered from the hazard rate alone.
5. notes/sl-01-multivariate-normal (chapter_guides.py GUIDES summary)
   Description (152): Covariance algebra for a random vector is developed, together with the multivariate normal, whose law is fixed by a mean vector and a covariance matrix.
   Summary/lead: "Covariance describes how several measurements on the same unit vary together. The multivariate normal is the family whose members are determined entirely by a mean vector and a covariance matrix."
