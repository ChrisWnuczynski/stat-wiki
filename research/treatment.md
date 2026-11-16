# Treatment — rank 94

Type: concept. Baseline 420 words, no figures. Preserve the definition, 12-plot fertiliser illustration, citations, infobox and all question links. The new numeric worked example uses a separate twelve-plot outcome dataset; the collapsed proof establishes unbiasedness of a difference in means under complete random assignment.

## Sources opened

- **Checked:** Hernán and Robins, *Causal Inference: What If* (author-hosted full PDF, version 19 August 2026, author site gives 2020 citation), Chapters 1–3: individual and average potential-outcome effects, randomization/exchangeability, consistency, well-defined interventions and observational identification. The authors' full book directly supports the proof's assignment mechanism and the history of Neyman 1923/Rubin 1974.
- **Checked:** authorized Dodge (2008), printed p. 541 “Treatment”: a treatment can be a combination of factor levels, and fertiliser doses exemplify distinct levels.
- **Checked:** answered bank items `ex-da-devil-tumours` and `ex-da-blood-pressure-covariates`, each exercises treatment assignment/response identification; the latter's answer is stronger than the book's nuanced account of finite-sample imbalance, addressed in the prose.
- **Assumed:** the numeric plot yields are fixed potential outcomes under a precisely defined fertiliser/control assignment, with no interference across plots. The observed treated/control values alone do not reveal all potential outcomes.
- **Disputed:** the inherited definition says a designed experiment can support a causal conclusion “that an observational study cannot.” Hernán and Robins Ch. 3 gives conditions under which observational data can identify causal effects. The shared `topics.py` phrase should be narrowed; the page adds the correct nuance now.

## Mathematical checks

Treated six-plot yields sum to 75 and average 12.5; controls sum to 54 and average 9; observed difference 3.5. Your-turn treated sum 34, mean 8.5; controls sum 26, mean 6.5; observed difference 2. Assignment expectation uses E[A_i]=n1/N. The source interpretation uses 12 plots split 6/6; the new worked numbers respect that design.
