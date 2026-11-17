## Motivating example
A classifier can make one confident mistake or several uncertain ones. Counting mistakes treats those outcomes alike; an exponential penalty gives the confident mistake much more weight. This provides a smooth objective for an additive classifier and links margin improvement to AdaBoost's observation weights.{{cite:schapire2013_explaining_adaboost}} (§4, pp. 7–8)

## Definition — A penalty on signed margins
For $Y\in\{-1,+1\}$ and score $f(X)$, the signed margin is $Yf(X)$ and the loss is $e^{-Yf(X)}$. At margin zero the loss is one. Positive margins reduce it and negative margins increase it without an upper bound. A margin of $-2$ gives loss $e^2=7.389056$. The population objective averages this loss over future observations; its empirical counterpart averages it over the training sample.{{cite:schapire2013_explaining_adaboost}} (§4, p. 7)

An AdaBoost update increases the relative weights of misclassified observations. The error-dependent coefficient and multiplicative update allow a direct bound on the training error, linking that update to exponential penalties.{{cite:freund_schapire1997}} (§4, AdaBoost and its training-error analysis)

## Properties — The conditional optimum and its endpoints
At a fixed input with class probability $p\in(0,1)$, the conditional risk is $pe^{-f}+(1-p)e^f$. Differentiating gives $-pe^{-f}+(1-p)e^f$, and a second derivative equal to the strictly positive risk. Its unique minimum is $f^*=\tfrac12\log\{p/(1-p)\}$, with risk $2\sqrt{p(1-p)}$. The sign of $f^*$ chooses the more probable class. This calculation connects the margin criterion to conditional class probabilities.{{cite:schapire2013_explaining_adaboost}} (§4, p. 7)

At $p=1$ the risk is $e^{-f}$ and has infimum zero as $f\to\infty$; it has no finite minimiser. At $p=0$ the corresponding direction is $f\to-\infty$. A separable training sample can exhibit the same absence of a finite optimum. Small training loss alone does not determine predictive performance on unseen data.{{cite:schapire2013_explaining_adaboost}} (§4, pp. 8–9)

## Worked example — A class probability of four fifths
For $p=0.8$, $f^*=\log2=0.693147$. Then $0.8e^{-f^*}+0.2e^{f^*}=0.8$, below the risk one at score zero. The inverse transformation $1/(1+e^{-2f^*})$ gives $0.8$. An AdaBoost round with weighted error $0.2$ has the same coefficient $\alpha=\log2$; its normaliser is $2\sqrt{0.2(0.8)}=0.8$. Starting with five equal weights and one error produces four new weights of $0.125$ and one of $0.5$.{{cite:freund_schapire1997}} (§4, AdaBoost update)

**Your turn.** What are the optimum score and conditional minimum loss when $p=1/2$?

::: {.callout-tip collapse="true" title="Answer"}
The optimum score is zero and its loss is one. Neither label is more probable at that input.
:::

