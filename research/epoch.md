# Epoch

Rank 314. Lighter tier. Concept page.

## Sources read

- ESL, Ch. 11, §11.4, p. 397. A training epoch is one sweep through the training set. Online learning replaces the batch sum by one case and cycles through the cases many times.

## Checked

- $n=20$, $m=4$: $5$ updates per epoch; $12$ updates are $2.4$ epochs.
- Three batch epochs read $60$ case-gradients and make $3$ updates. Twelve online updates read $12$ case-gradients.
- Mini-batches of $5$: $4$ updates per epoch; $8$ updates are $2$ epochs.
- $n=5000$: $5000$ online updates, or $1$ batch update, per epoch.
- Seven updates with $m=4$ are $1.4$ epochs.

## Not used

- The source exercise that compares $10{,}000$ epochs of batch learning with $10{,}000$ online iterations was left as that chapter's exercise. The page uses a smaller count.
