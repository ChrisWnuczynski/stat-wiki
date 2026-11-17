## Lead context

Buyers compare products, and producers compare themselves with the buyer who switched. Quality control is the statistical side of that comparison: deciding whether a stream of output is stable, whether a lot should be accepted, and whether the process is even capable of meeting a specification. Inspection of every piece is sometimes possible and often wasteful. The modern subject replaces that habit with sampling, charts, and designed experiments, and it treats a stable process as a different problem from a process that is stable and still not good enough.

## Definition — Scope

Quality control is the use of statistical methods to maintain and improve the quality of a product or a process. It is older than the statistical theory attached to it. Guilds trained apprentices and examined master-work; modern regulators inspect factories. Statistical quality control is the twentieth-century layer: sampling theory applied to manufacturing. Process monitoring divides the work into acceptance sampling of lots, control charts for ongoing production, and process capability, which asks whether an in-control process meets the specification. Those are different decisions. A lot that fails an acceptance plan is a bad batch. A point outside control limits is a signal that the process has changed. A capable process is one whose ordinary variation sits inside the tolerances.{{cite:nist_pmc2002}} (Ch. 6){{cite:nist_pmc11_2002}} (§6.1.1)

Engineering statistics includes this work alongside design and efficiency tests. It is not the same subject as a clinical trial or a national account, even though each uses samples and intervals. The quality-control question is about a production process and a specification.{{cite:dodge2008}} (p. 519)

## Statistical use

Acceptance sampling chooses a plan, inspects a sample from a lot, and accepts or rejects the lot. Control charts, the main tool of [statistical process control](statistical-process-control.qmd), plot a statistic against time with a centre line and control limits, conventionally near three standard deviations for a normally varying characteristic. A point outside the limits, or a systematic pattern inside them, is treated as evidence of an assignable cause rather than of the chance variation the limits were built to contain. Process capability then compares that chance variation with the specification. If the process is stable and still produces too many pieces outside the tolerances, the remedy is a change of the process, not a hunt for a special cause that is not there.{{cite:nist_pmc31_2002}} (§6.3.1){{cite:nist_pmc13_2002}} (§6.1.3)

Designed experiments belong in the same toolbox when the question is which factor moves the output. A control chart will not say which knob to turn. It says that the output is no longer the output the limits describe.{{cite:nist_pmc11_2002}} (§6.1.1)

## History

Statistical theory began to be applied effectively to industrial quality in the 1920s, once sampling theory was in hand. Walter Shewhart, at Bell Telephone Laboratories, circulated a memorandum on 16 May 1924 that sketched a control chart, and in 1931 published *Economic Control of Quality of Manufactured Product*. Harold Dodge and Harry Romig, also at Bell Labs, developed sampling inspection. Those three lines of work became the core of statistical quality control. W. Edwards Deming, after leaving the U.S. Census Bureau in 1946, worked as a consultant, and from 1950 Japanese industry took up his management teaching; the sampling ideas he had used in census work were part of the same career, not a separate subject from industrial quality.{{cite:nist_pmc11_2002}} (§6.1.1){{cite:dodge2008}} (p. 155)

## Connections

Quality control contains [statistical process control](statistical-process-control.qmd) and sits next to reliability, where the question is how long a unit survives rather than whether today's lot meets a limit. The [survival function](survival-function.qmd) is the reliability function in that setting. A specification limit is not a control limit. The first is a statement of what the customer will accept. The second is a statement of what the process has been doing. Confusing them produces either a search for a special cause when the process is only incapable, or a shrug at a real shift because the pieces are still inside a wide tolerance.{{cite:nist_pmc2002}} (Ch. 6){{cite:nist_reliability2002}} (§8.1.2.2)
