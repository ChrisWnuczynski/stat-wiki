# Research log: delta-rule

Rank 501; batch AC.

Goodfellow full §6.2.2.2 pp178–180 read for sigmoid/Bernoulli output and saturation; §§6.5.4 pp208–209 read for chain-rule deltas. D2L full backprop text read. Delta factors derived explicitly for squared-error convention and alternative cross-entropy. Checks verify toy updates, finite differences, legacy nine-weight example, saturation and missing exponential factor.

## Sources actually read

- `goodfellow_bengio_courville2016`: §6.5.4, pp. 208–209; §6.2.2.2, pp. 178–180. https://www.deeplearningbook.org/contents/mlp.html ; https://www.deeplearningbook.org/contents/ml.html ; https://www.deeplearningbook.org/contents/optimization.html
- `zhang_d2l2023`: §5.3, backward propagation; §5.3. https://raw.githubusercontent.com/d2l-ai/d2l-en/master/chapter_multilayer-perceptrons/backprop.md ; https://raw.githubusercontent.com/d2l-ai/d2l-en/master/chapter_optimization/gd.md

## Verification

- All numerical sections executed successfully independently before final generated-content validation. `checks/delta-rule.py` recomputes the examples and inspects generated citations, structure, hidden answers and real question links.
- 6 located citations across 2 proper works in the new prose. The generated page has 12 located inline citations across 2 proper works actually read.
- No tests, generator, bibliography or shared source input edited by this agent. Exact shared substitutions and any self-check map request are in ignored `research/pending/delta-rule.json`.
- The successful Done517 build generated 718 articles and 626 questions. All15 AC checks, the generated-page citation/answer/structure audit, offline665-work bibliography verification and diff check passed. The full72-test run passed all517 calculation scripts and71 test methods; its single failure was a shared worked-example heading. After root repaired both affected headings, the exact previously failing method passed (1 test, 1.172s). The integration coordinator will run a fresh full build and full suite after merging all batches.
