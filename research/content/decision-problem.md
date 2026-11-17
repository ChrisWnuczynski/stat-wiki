## Lead context

An inference that stops at a posterior probability still leaves someone to act. A decision problem is that next question written in full: which actions are available, which outcomes they can lead to, and how those outcomes are scored. The probability model supplies the distribution of outcomes given an action. The decision problem supplies the list of actions and the reason one of them is chosen.{{cite:gelman_bda2013}} (Ch. 9, §9.1, pp. 237–238)

## Motivating example

A 95-year-old patient with a lung tumour can choose radiotherapy, surgery, or no treatment. There is a $90\%$ chance the tumour is malignant. Life expectancy is $16.7$ months with radiotherapy if it is cancer and $34.8$ months if it is not. Surgery carries a $35\%$ chance of immediate death and otherwise a longer expectancy. No treatment leaves $5.6$ months if the tumour is malignant. Treatment also costs about a month of comfort. Scoring each action by expected quality-adjusted lifetime makes radiotherapy the best of the three, at about $17.5$ months against $13.5$ and $8.5$. Adding a bronchoscopy, which might change the probability of cancer before the treatment is chosen, is a second decision point in the same problem. The calculation shows that the test would not change the treatment, so the test is not worth its risk.{{cite:gelman_bda2013}} (Ch. 9, §9.3, pp. 245–246)

## Intuition

A probability answers “what might be true?” A decision problem answers “what will be done, and what happens if it is?” The two come apart because the best action is not always the action that maximises the probability of the most likely state. Surgery might be the right gamble for a younger patient and the wrong one here, with the same probability of cancer, because the outcomes are scored differently. Writing the actions, the outcomes, and the score down is what makes that difference visible.{{cite:gelman_bda2013}} (Ch. 9, §9.1, p. 238; §9.3, p. 245)

Multistage problems alternate decisions and uncertain results. A test is chosen, nature reveals a result, and a treatment is chosen with the result in hand. The value of the test is not the value of the result in isolation. It is the improvement, if any, in the action that will be taken after the result is seen.{{cite:gelman_bda2013}} (Ch. 9, §9.3, pp. 245–246)

## Definition

A decision problem, in the Bayesian account used for applied decision analysis, has four parts.

1. A set of decisions $d$ and a set of outcomes $x$. Outcomes may be money, years of life, or a vector of several attributes. The outcome can include quantities that will eventually be observed and parameters that will not.
2. A probability distribution of the outcome given each decision, written $p(x\mid d)$. The decision itself is not assigned a probability. Every probability in the problem is conditional on the action under consideration.
3. A utility $U(x)$ that scores outcomes on one numerical scale. With several attributes the utility has to weigh them against each other, as quality-adjusted life years do when a month of treatment discomfort is subtracted.
4. The expected utility $E\bigl(U(x)\mid d\bigr)$, computed for each $d$, with the preferred decision the one whose expected utility is highest. In a tree of several decisions the expectation at each node uses only the information available at that node.

A full analysis does all four steps. Many applications stop after the first two and leave the weighing of outcomes to the person who must act.{{cite:gelman_bda2013}} (Ch. 9, §9.1, pp. 237–239)

Point estimation is a decision problem of a narrower kind. The action is the number reported for a parameter, and a loss scores the use of that number in place of the unknown value. When the loss is quadratic, the point estimate is the mean of the distribution calculated for the parameter.{{cite:dodge2008}} (p. 34)

A household radon problem has the same four parts. It asks whether to remediate at once, do nothing, or measure and then remediate only if the measurement is high. The actions, the uncertain exposure, and the dollar cost of a reduction in risk are the decision problem. The statistical model that estimates exposure is an input to it.{{cite:gelman_bda2013}} (Ch. 9, §9.4, pp. 246–248)

## Properties

Expected utility, or expected loss if the score is written as a cost, ranks actions. It does not rank states. In the lung-tumour numbers the probability of cancer is $0.90$ under every treatment that does not include a fatal test. The actions differ because the life expectancy attached to cancer, and the chance of dying from the action itself, differ. Radiotherapy’s quality-adjusted expectancy is $0.9\times 16.7+0.1\times 34.8-1=17.51$ months. Surgery’s is $0.65\times(0.9\times 20.3+0.1\times 34.8-1)=13.49$ months. No treatment’s is $0.9\times 5.6+0.1\times 34.8=8.52$ months. The ranking uses one probability and three different outcome maps.{{cite:gelman_bda2013}} (Ch. 9, §9.3, p. 245)

Information has value inside the problem only when it can change a later action. After bronchoscopy the posterior probability of cancer is about $0.997$ if the test is positive and about $0.73$ if it is negative, and radiotherapy remains the best treatment in both cases. The test’s quality-adjusted expectancy, including a $5\%$ chance the test is fatal, is about $16.6$ months, below the $17.5$ months of radiotherapy without the test. A datum that does not switch the action does not pay for itself in this score.{{cite:gelman_bda2013}} (Ch. 9, §9.3, pp. 245–246)

Choosing how to summarise a posterior can itself be posed as a decision problem, with a scoring rule for the summary. That is a decision about a report, not a decision about a treatment, and the loss is whatever the scoring rule charges for a bad report.{{cite:gelman_bda2013}} (Ch. 9, §9.1, p. 239)

## Statistical use

Write the actions before computing a posterior that is meant to guide one of them. Name the outcome and the utility, including any tradeoff such as a month of discomfort per treatment. Then compute the expected score under each action, using the posterior distribution of whatever is still unknown. If a test is optional, compute the expected score of the policy “test, then act,” and compare it with the score of acting now. Report the base probabilities that entered the expectation, because a different probability of cancer can reorder the actions even when the test characteristics stay fixed.{{cite:gelman_bda2013}} (Ch. 9, §9.1, pp. 237–238; §9.3, pp. 245–246)

A [confidence interval](confidence-interval.qmd) or a posterior interval is not yet a decision. It becomes an input once an action and a loss are named. [Loss and risk](loss-and-risk.qmd) are the sampling-theory version of the same score, with the average taken over repeated samples at a fixed parameter.

## Worked example

Using the life expectancies above and a cancer probability of $0.90$, radiotherapy scores $17.51$ quality-adjusted months, surgery $13.49$, and no treatment $8.52$. Radiotherapy is preferred. Now change only the cancer probability, to $0.50$, and recompute radiotherapy and no treatment. Radiotherapy scores $0.5\times 16.7+0.5\times 34.8-1=24.75$ months. No treatment scores $0.5\times 5.6+0.5\times 34.8=20.2$ months. Radiotherapy is still ahead. The gap changed because the base rate changed, which is a change in the decision problem’s probabilities, not a change in the actions.{{cite:gelman_bda2013}} (Ch. 9, §9.3, p. 245)

**Your turn.** Keep the cancer probability at $0.50$ and the same life expectancies. Surgery still kills immediately with probability $0.35$, and otherwise follows the cancer-specific expectancies, minus one month, and that whole quantity is then multiplied by $0.65$. Compute surgery’s quality-adjusted expectancy and say whether it beats radiotherapy’s $24.75$.

::: {.callout-tip collapse="true" title="Answer"}
The quantity inside is $0.5\times 20.3+0.5\times 34.8-1=26.55$. Multiply by $0.65$ to get $17.2575$ months. Radiotherapy’s $24.75$ is larger, so surgery is not preferred at this cancer probability either.
:::

## Common misconceptions

The action with the highest probability of the best state is not automatically the solution. The solution maximises expected utility, which can favour an action that sometimes fails badly if it does well often enough under the score in use. A test with impressive sensitivity is not automatically worth doing. If every result leads to the same next action, the test has no decision value. A decision problem is not the same object as a hypothesis test. A test rejects or retains a claim about a parameter. A decision problem chooses an action whose consequences are scored.{{cite:gelman_bda2013}} (Ch. 9, §9.1, pp. 237–239; §9.3, pp. 245–246)

## Assumptions and limits

The ranking is only as good as the probabilities and the utility. The lung-tumour expectancies are described as extrapolations from the literature, and a different discomfort penalty would move the scores. Expected utility treats the score as something one may average. A person who refuses a small chance of immediate death at any average gain is using a different score, and the problem should say so. The analysis also assumes the list of actions is complete. An action that was never written down cannot win.{{cite:gelman_bda2013}} (Ch. 9, §9.3, p. 245; §9.1, p. 238)

## Connections

[Expected loss](expected-loss.qmd) is the score when outcomes are written as costs and the preferred action minimises the expectation. The [base rate](base-rate.qmd) is the probability of the condition that enters $p(x\mid d)$ before a test is seen. [Loss and risk](loss-and-risk.qmd) study the average loss of a statistical procedure. [Inference](inference.qmd) produces the probabilities a decision problem then uses.

## History

Statistical decision theory took shape as a way to place inference inside a choice among actions with gains and losses. Applied Bayesian writing uses that pattern as four explicit steps: list decisions and outcomes, assign $p(x\mid d)$, choose a utility, and maximise expected utility, with a tree when later actions depend on data the first action made available. Medical examples made the steps concrete. A single treatment choice among radiotherapy, surgery, and no treatment is a one-node problem. Offering a diagnostic test first makes it multistage, and the arithmetic can show that the test does not change the treatment. Household risk problems, such as whether to measure radon before spending on remediation, use the same tree with dollars and cancer risk in place of months of life.{{cite:gelman_bda2013}} (Ch. 9, §9.1, pp. 237–239; §9.3, pp. 245–246; §9.4, pp. 246–248)
