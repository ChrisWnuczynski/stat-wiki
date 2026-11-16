# Early stopping

Rank 313. Lighter tier. Concept page.

## Sources read

- Bishop, *Pattern Recognition and Machine Learning*, §5.5.2, printed pp. 259–261. Validation error often falls then rises; stop at its minimum. For a quadratic error, a gradient path started at the origin makes an early stop similar to weight decay, via the Hessian picture. The factor $\tau\eta$ is mentioned as an exercise and is not used on the page.
- ESL, Ch. 11, §11.5.2, p. 398. Stop well before the training minimum; a validation set times the stop; early weights sit near a linear fit.

## Checked

- The five-epoch curves select epoch 3, validation $0.27$, against a still-falling training error $0.09$.
- The second curve selects epoch 3 at $0.28$.
- A still-falling validation list selects the last epoch.
- Epoch 3 beats epoch 4 on validation ($0.27<0.29$) despite a higher training error.

## Not claimed

- Early stopping is not stated to equal a pre-chosen $L^2$ penalty. Bishop's similarity is restricted to the quadratic gradient path he describes.
