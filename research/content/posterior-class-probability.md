## Motivating example
An image classifier may assign probability 0.55 to one class and 0.45 to another. A second image can receive the same predicted label with probabilities 0.99 and 0.01. A label alone suppresses that difference in uncertainty. Posterior class probabilities describe uncertainty about a case's class after observing its features, and make it possible to choose decisions for a particular loss rather than reporting only the most probable category.{{cite:zhang_d2l2023}} (Chapter “Linear Neural Networks for Classification”, “Softmax Regression”, probability and likelihood subsections)

## Definition — Reverse the conditioning with Bayes' rule
Let $G$ take values in classes $1,\ldots,K$, with prior probabilities $\pi_g$. If the feature vector $X$ has class-conditional density or mass function $f_g$, then at a point with a positive marginal density,
$$\tau_g(x)=\Pr(G=g\mid X=x)=\frac{\pi_g f_g(x)}{\sum_{h=1}^K\pi_h f_h(x)}.$$
The product $\pi_g f_g(x)$ is a joint density contribution. Its sum over classes supplies the normalising constant. Posterior class probabilities are nonnegative and sum to one; class-conditional likelihoods alone generally do not.{{cite:dodge2008}} (Bayes’ Theorem, pp. 30–31)

For two classes with positive terms, posterior odds factor as prior odds times a likelihood ratio:
$$\frac{\tau_1(x)}{\tau_2(x)}=\frac{\pi_1}{\pi_2}\frac{f_1(x)}{f_2(x)}.$$
A common multiplier applied to all likelihood contributions cancels, but a class-specific multiplier need not cancel. This is why it is legitimate to work with a shared normalising constant and illegitimate to normalise each class contribution separately before applying Bayes' rule.{{cite:dodge2008}} (Bayes’ Theorem, pp. 30–31)

## Properties — Probabilities and decisions answer different questions
Under zero–one loss, choosing a class $a$ incurs conditional expected loss $1-\tau_a(x)$. Minimising it gives the class with largest posterior probability. If losses are unequal, the appropriate decision instead minimises $\sum_g L(a,g)\tau_g(x)$. Thus a change in classification threshold can reflect a change in costs without changing the probability model. A probabilistic classifier also permits a refusal or referral decision when the expected cost of an immediate prediction is too large.{{cite:goodfellow_bengio_courville2016}} (§5.1.2, classification and probabilities; §6.2.2.3, softmax outputs)

The term posterior here need not imply a Bayesian posterior over model coefficients. A frequentist fitted logistic model estimates $\Pr(G=g\mid X=x)$ too. A Bayesian treatment can integrate those probabilities over a coefficient posterior, introducing another layer of uncertainty. The two conditioning operations should be identified explicitly: uncertainty about an individual label and uncertainty about the coefficients of the probability model are different random quantities.{{cite:zhang_d2l2023}} (“Softmax Regression”, probabilistic model and cross-entropy loss)

## Worked example — A likelihood advantage is not enough by itself
Suppose $\pi_1=0.2$, $\pi_2=0.8$, and the two likelihood values at an observed feature vector are $f_1(x)=0.6$ and $f_2(x)=0.1$. The joint contributions are $0.12$ and $0.08$, summing to $0.20$. Therefore the class probabilities are $\tau_1(x)=0.6$ and $\tau_2(x)=0.4$. The prior odds $1/4$ have been multiplied by the likelihood ratio $6$, giving posterior odds $3/2$.

With false-positive cost 4 for assigning class 1 to a class-2 case and false-negative cost 1, choose class 1 only when $4\tau_2(x)<\tau_1(x)$, or $\tau_1(x)>0.8$. The zero–one rule chooses class 1 for this example, but the stated cost-sensitive rule chooses class 2. Both decisions use the same posterior probabilities.

**Your turn.** Change only the prior probabilities to $\pi_1=\pi_2=0.5$. What is the posterior probability of class 1?

::: {.callout-tip collapse="true" title="Answer"}
It becomes $0.3/(0.3+0.05)=6/7=0.857143$. The feature likelihoods stay the same, while the prior odds change from 1/4 to 1.
:::

## Statistical use — Check the probabilities on representative data
A classifier can rank cases well while producing poor probabilities. Calibration concerns whether predictions near a probability value correspond to an appropriate observed frequency over repeated comparable cases. Computing an accuracy alone cannot establish calibration: many different probability vectors yield the same largest-probability class. Cross-entropy uses the probability assigned to the realised category and therefore distinguishes such predictions.{{cite:zhang_d2l2023}} (“Softmax Regression”, cross-entropy loss)

Changing class prevalence can also change posterior probabilities. If the class-conditional feature distributions transfer to a new population but the class priors do not, Bayes' rule permits an odds adjustment. If the class-conditional distributions change too, a simple prior adjustment is insufficient. These are assumptions about the population represented by the data, and should be checked before treating a fitted probability as a property of the feature vector alone.{{cite:dodge2008}} (Bayes’ Theorem, pp. 30–31)
