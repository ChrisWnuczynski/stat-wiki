## Motivating example
After fitting a classifier, a user may want to know how often that particular rule will make a mistake on future observations. This is a conditional question: the rule is held fixed while a new feature–label pair is drawn. Repeating the training algorithm across new datasets asks a different question, because each training sample can produce a different rule. Keeping the target explicit prevents a training score from being mistaken for future performance.{{cite:goodfellow_bengio_courville2016}} (§5.2, generalization and test error)

## Definition — Average loss over a fresh observation
For a measurable classifier $h$ held fixed and a future pair $(X,Y)\sim F$, define $R_F(h)=\Pr_F\{h(X)\ne Y\}$. Under zero–one loss this equals $E_F\mathbf1\{h(X)\ne Y\}$. If $\pi_g=\Pr(Y=g)>0$ and $r_g=\Pr\{h(X)\ne g\mid Y=g\}$, the law of total probability gives $R_F(h)=\sum_g\pi_gr_g$. The class proportions used in this weighted average belong to the intended future population, which need not match a deliberately balanced test sample.{{cite:grinstead_snell1997}} (§4.1, total probability; §6.1, indicator expectations)

## Properties — Independent testing has a simple sampling law
If $m$ independent test observations come from $F$ and are independent of training, their mistake indicators are independent Bernoulli variables conditional on $h$. Thus the test error fraction is unbiased for $R_F(h)$, with conditional variance $R_F(h)\{1-R_F(h)\}/m$. The result follows by adding the expectations and variances of indicators. Test-set uncertainty can therefore be large for a small test sample even if training is complete.{{cite:grinstead_snell1997}} (§§5.1, 6.1–6.2, Bernoulli trials and their sums)

Using the same test observations to choose repeatedly between rules changes that assessment procedure. The selected rule is then a function of the test results, so the conditional independent-test calculation no longer applies to its reported score in that simple form. A separate final evaluation sample is one way to preserve the meaning of a future-error assessment.{{cite:goodfellow_bengio_courville2016}} (§5.3, hyperparameters and validation sets)

## Worked example — Reweight class-specific errors
Suppose a classifier's class-specific errors are $r_1=1/10$ and $r_2=2/5$. In a population with prevalences $(4/5,1/5)$, its overall error is $(4/5)(1/10)+(1/5)(2/5)=4/25=0.16$. On an equally balanced class mixture, the same conditional error rates instead give error $1/4$. This difference can arise solely from population composition, without changing either conditional error rate.{{cite:grinstead_snell1997}} (§4.1, law of total probability)

For $m=400$ independent observations from the first population, the conditional standard deviation of the error fraction is $\sqrt{0.16(0.84)/400}\approx0.018330$. The balanced class mixture and the future mixture answer different aggregate questions, so both the per-class errors and the weighting scheme should be reported. Estimates of rare-class errors additionally need enough observations in that class.{{cite:goodfellow_bengio_courville2016}} (§5.2, expected test error)

**Your turn.** If class two becomes half the future population while its conditional error remains $2/5$ and class one's remains $1/10$, what is overall error?

::: {.callout-tip collapse="true" title="Answer"}
It is $(1/2)(1/10)+(1/2)(2/5)=1/4$.
:::

## Assumptions and limits — Deployment can change the target
An independent test set estimates the error for the distribution it represents. If the future joint distribution changes, an accurate historical estimate can become irrelevant. Reweighting by new class proportions is valid only under an appropriate stability assumption for the class-conditional behaviour. Different mistake costs also change the relevant loss function, even if the unweighted error rates are unchanged. Performance assessment should therefore identify the fixed rule, sampling population, loss and uncertainty.{{cite:goodfellow_bengio_courville2016}} (§§5.2–5.3)
