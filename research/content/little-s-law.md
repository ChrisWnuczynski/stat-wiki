## Lead context
Little's law says that the average number of customers present is the arrival rate multiplied by the average time each customer stays.

## Intuition — Headcount is a rate times a duration
Picture a steady cafe. If \(20\) customers arrive each hour and each stays a quarter of an hour, then over that hour the arrivals contribute \(20\times 1/4=5\) customer-hours, which is an average headcount of \(5\). The same product runs in either direction: a known headcount and a known stay give the throughput. The three numbers have to describe one population. Mixing the queue-only wait with the time spent in service, or counting customers who never enter, breaks the identity even though each separate average may be correct.

## Definition — One population, three averages
For a stable system, \(L=\lambda_{\mathrm{eff}} W\). Here \(L\) is the time-average number present, \(W\) is the mean sojourn of the customers who are counted in \(L\), and \(\lambda_{\mathrm{eff}}\) is their mean arrival rate. The queue-only companion is \(L_q=\lambda_{\mathrm{eff}} W_q\), with the wait before service in place of the full sojourn. In a system that turns arrivals away, \(\lambda_{\mathrm{eff}}\) is the rate of accepted arrivals.

## Worked example — Twenty arrivals an hour, each staying fifteen minutes
Take \(\lambda_{\mathrm{eff}}=20\) customers per hour and \(W=1/4\) hour. Then
\[
L=20\times\frac14=5.
\]
Five customers present, each staying a quarter of an hour, are the same statement run backwards: \(W=L/\lambda_{\mathrm{eff}}=5/20=1/4\). If the mean wait before service is \(1/10\) hour and the mean service is the remaining \(3/20\) hour, the queue length is \(L_q=20\times 1/10=2\), and the mean number in service is \(5-2=3\). Adding the service time back recovers the system sojourn: \(1/10+3/20=1/4\).

**Your turn.** A clinic holds \(L=8\) patients on average, and each accepted patient stays \(W=2/5\) hour. What arrival rate does Little's law require, and how many patient-hours is that per hour?

::: {.callout-tip collapse="true" title="Answer"}
\(\lambda_{\mathrm{eff}}=L/W=8/(2/5)=20\) patients per hour. The patient-hours per hour are the headcount, \(8\), which is also \(20\times 2/5\).
:::

## Connections — Queues, blocking, and the population you named
An [M/M/1 queue](m-m-1-queue.qmd) with arrival rate below the service rate is stable, so the identity applies to the whole system and, separately, to the waiting line. A [blocking probability](blocking-probability.qmd) means some arrivals never join \(L\); the rate in the formula is then the throughput. The identity is an accounting relation for those averages. It does not require exponential service or a single server.

## Check yourself — Matching the three numbers
A server completes \(12\) jobs an hour, and the mean number of jobs in the system is \(3\). What is the mean sojourn, in minutes?

::: {.callout-tip collapse="true" title="Answer"}
\(W=3/12=1/4\) hour, which is \(15\) minutes. The completion rate in a stable system is the accepted arrival rate.
:::

The mean wait in the queue is \(10\) minutes and the mean service is \(5\) minutes, with \(12\) jobs an hour accepted. What are \(L_q\) and \(L\)?

::: {.callout-tip collapse="true" title="Answer"}
Ten minutes is \(1/6\) hour and five minutes is \(1/12\) hour, so \(W=1/6+1/12=1/4\) hour. Then \(L_q=12\times 1/6=2\) and \(L=12\times 1/4=3\).
:::
