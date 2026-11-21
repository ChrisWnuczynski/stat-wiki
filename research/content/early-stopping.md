## Motivating example
Over five epochs the training errors are $0.50$, $0.32$, $0.21$, $0.14$ and $0.09$, while the validation errors are $0.48$, $0.30$, $0.27$, $0.29$ and $0.36$. Training is still falling at epoch $5$. Validation is smallest at epoch $3$.

## Intuition — Stop when new cases stop improving
Training error for many network optimisers keeps falling as the iteration continues. Error on cases that were held out of the fit often falls and then rises. Early stopping takes the weights at the low point of that held-out curve, before the training criterion has reached its minimum. The weights usually start near a simple fit, so an early point on the path is a less specialised network than the eventual training minimum.{{cite:hastie_esl2009}} (Ch. 11, §11.5.2, p. 398){{cite:bishop2006}} (§5.5.2, pp. 259–260)

## Definition — The validation minimum
Split the fitting data into a training set, used to form the gradients, and a validation set, used only to watch the error. Record the validation error after each epoch, or after each block of updates. Stop at the recorded point whose validation error is smallest. If the optimiser is conjugate gradients, or another method whose training error is nonincreasing, the training curve itself does not provide that stopping signal.{{cite:bishop2006}} (§5.5.2, pp. 259–260)

For a quadratic error, with the weights started at the origin and a path that follows the local negative gradient, Bishop shows that an early point on that path is similar to a weight-decay fit. The picture uses the eigenvectors of the Hessian. It describes that path. It does not say that every stopped network equals a penalised fit with a penalty chosen in advance.{{cite:bishop2006}} (§5.5.2, pp. 259–261)

## Worked example — Five epochs
Suppose the training mean squared error over five epochs is $0.50$, $0.32$, $0.21$, $0.14$, $0.09$, and the validation error is $0.48$, $0.30$, $0.27$, $0.29$, $0.36$. The training numbers are still falling at epoch $5$. The validation minimum is $0.27$, at epoch $3$. The stopped network is the one saved at epoch $3$, not the one with training error $0.09$.

**Your turn.** A second run has validation errors $0.42$, $0.35$, $0.28$, $0.33$, $0.34$. Which epoch is selected, and what would go wrong if the same minimum were read off the test set instead?

::: {.callout-tip collapse="true" title="Answer"}
The smallest validation error is $0.28$, at epoch $3$. Using the test set to choose the epoch spends that set as a tuning device, so the chosen test score is no longer an untouched estimate of future error.
:::

## Connections — A path, not a penalty
The clock of the rule is the [epoch](epoch.qmd). The steps being stopped are often [stochastic gradient descent](stochastic-gradient-descent.qmd), and the place they start is the [weight initialisation](weight-initialisation.qmd). [Regularisation](regularisation.qmd) changes the criterion by a penalty; early stopping leaves the criterion alone and shortens the path. The [validation set](validation-set.qmd) is what chooses the stopping time, so a later [held-out test set](a-held-out-test-set.qmd) has to stay out of that choice.{{cite:hastie_esl2009}} (Ch. 11, §11.5.2, p. 398){{cite:bishop2006}} (§5.5.2, pp. 259–260)
