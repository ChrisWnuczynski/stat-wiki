> **Handover note (20 Nov 2026):** Editor's polish plan, batch 004. QUEUED: start only after #89 AND #91 have merged. Read both ADDENDUM sections at the end first; they override the body. Copied from the previous automation's private workspace; paths were rewritten to repo paths.

# Batch 004 — Random variables and expectation

> **PRECEDENCE (overrides anything below):**
> 1. Follow `docs/automation/plans/STYLE-GUIDE.md` for all rewritten prose.
> 2. Maths uses `$...$` / `$$...$$` only. These research files already use `$` (main includes PR #72). Do not introduce `\(...\)` / `\[...\]`.
> 3. Keep every History section. Tighten wording only; never cut. Any line below that would empty or delete History is void. Do not invent a History section on a page that does not have one (`poisson-limit-of-the-binomial`).
> 4. Each concept page must keep >=5 citations from >=2 independent sources and 2–3 Check yourself questions. Do not invent locators or add unread works. Do not cite `sas2012_glm` Ch. 3 or Dodge biography / encyclopedia entries for technical claims. These eight pages already meet the citation quota without Dodge or `sas2012_glm`; do not introduce those keys.
> 5. When moving or retitling sections, replace relative references (“above”, “below”, “on this page”, “the next section”, “the examples below”, “the proof above”, “the formula above”, “Here $X$ is…”) with a named referent. Do not give away a worked answer when doing so.
> 6. Edit `research/content/*.md` only, never `research/*.md`. Do not edit `sources/`, `build_wiki.py`, generated `articles/*.qmd`, `proofs-todo.json`, or `research/self-checks.json` (the last is in open PR #65). Touch `article_leads.json` only for the keys listed below, and only as specified. Do not talk about sources or editorial process in the visible prose.
> 7. Do not duplicate a worked example or Your turn in Check yourself. Do not leave answers to generated Check yourself questions in the research file.
> 8. Chris approved `sources/` edits as a standing rule (19 Nov 2026, direct, and confirmed again the same day). This batch does not need any `sources/` change.

> **Style:** Follow `docs/automation/plans/STYLE-GUIDE.md` (Chris's editorial guide). Formal academic voice; no slang or filler.

Eight concept articles from the same chapter, [*Random variables*](https://www.statwiki.io/notes/prob-02-random-variables.html) (`sources/stat2003/chapters/prob-02-random-variables.qmd`). They cover the definition of a random variable, discrete and continuous laws, the CDF, expectation, variance, the gamma distribution, and the Poisson limit of the binomial. Most still use bare template headings. Several Lead contexts start with a dangling “It”, and two pages currently give away the answers to their generated Check yourself questions.

This batch is prose and heading work in `research/content/`, with at most light lead-sentence checks in `article_leads.json`. Do **not** change the chapter `.qmd`. Do **not** edit `build_wiki.py` or `research/self-checks.json`, and do **not** open a PR from this plan alone — a separate cloud agent implements it.

Named distribution pages that also sit on this chapter (Bernoulli, binomial, Poisson, exponential, geometric, uniform, and the normal distribution) were left out: several lean on Dodge for technical claims, and `normal-distribution.md` is already in open PR #80.

Proposed branch, cut from current `main` (which already includes #74 and #81): `claude/content/random-variables`.

## Scope summary (for Repo Helper)

- **Branch:** `claude/content/random-variables`
- **Purpose:** Polish the eight random-variable / expectation concept pages from `prob-02-random-variables` (headings, leads, relative references, History tightening, and two Check-yourself answer giveaways). No `sources/`, `build_wiki.py`, or `research/self-checks.json` edits.
- **Files:**
  - `research/content/random-variable.md`
  - `research/content/discrete-distribution.md`
  - `research/content/continuous-distribution.md`
  - `research/content/cumulative-distribution-function.md`
  - `research/content/expectation.md`
  - `research/content/variance.md`
  - `research/content/gamma-distribution.md`
  - `research/content/poisson-limit-of-the-binomial.md`
  - `article_leads.json` (only the keys named in the page plans, and only if a preview actually shows the glitch described there)

### Collision check (open PRs fetched 19 Nov 2026, 6:09pm Australia/Brisbane)

- **#74** and **#81** are already merged into `main`. Not a collision.
- **#78** (`cursor/content/gap-batch-1`): overlaps `article_leads.json` only, with new-article keys (`wilcoxon-signed-rank-test`, `shapiro-wilk-test`, `friedman-test`, `levene-s-test`). No content-file overlap with this batch. If this batch touches `article_leads.json` at all, edit only the keys named below and expect a possible JSON rebase.
- **#80** (`cursor/article-guidance-citations-5840`): touches `research/content/normal-distribution.md`, `build_wiki.py`, `citations.py`, several `checks/*.py` and labs, not these eight research files. This batch does not edit `normal-distribution.md` or the build.
- **#65** (`research/quality-followup-68-517`, draft): 376 files, including `research/self-checks.json` and 267 `research/content/` pages, but **not** these eight research files. It also touches `sources/stat2003/chapters/prob-05-transforms-and-limits.qmd` and `prob-07-reliability.qmd`, not `prob-02-random-variables.qmd`. Do not stack on #65, and do not edit `self-checks.json`.
- **#79** / **#82** (navbar / reading order / phone layout) and **#83** (Ask index checkout): no overlap, provided this batch does not touch `build_wiki.py`, `_theme-body.html`, or `styles.css`.
- **Gap batch 2** (new pages `latin-square-design`, `crossover-design`, `split-plot-design`, `two-level-factorial-design`, plus registry files) and **batch 003** (GLM count models) do not overlap these files.
- Live `main` was fetched for this plan and already includes #74 and #81.

## General guidance (read first)

- Keep mathematical formulae, proofs, worked numerical examples, `{{cite:…}}` markers, and cross-links to other wiki pages. Do not change statistical substance except where a page plan flags a **clear error**. No arithmetic errors were found in these eight pages.
- Research headings must keep their canonical key and should gain a topic-specific display title with an em dash, as `build_wiki.py` already supports:

  `## Motivating example — Two tosses, one number of heads`

  The live H2 becomes the text after ` — `. Do not invent new canonical keys, and do not invent a new site-wide heading vocabulary. Existing non-template keys already on a page (`Related distributions`, `Statistical inference`, `Generating random samples`, `Related concepts`, `Statement`, `Proof`) may receive a display title but must keep their key.
- Three templates are in play. Do not move a heading to a key the template will drop:
  - **Concept** (`concept_article_template`): `random-variable`, `discrete-distribution`, `continuous-distribution`, `cumulative-distribution-function`, `expectation`, `variance`. Allowed keys include Lead context, Motivating example, Intuition, Definition, Interpretation, Properties, Statistical use, Worked example, Common misconceptions, Assumptions and limits, Connections, Check yourself, History.
  - **Distribution** (`distribution_article_template`): `gamma-distribution` (has a card in `distributions.json`). Allowed keys include Lead context, Motivating example, Intuition, Definition, Properties, Related distributions, Statistical inference, Generating random samples, Worked example, Examples, Common misconceptions, Assumptions and limits, Connections, History. Do not rename Statistical inference to Statistical use.
  - **Theorem** (`theorem_article_template`): `poisson-limit-of-the-binomial`. Allowed keys include Lead context, Motivating example, Statement, Intuition, Key results, Proof, Generalizations, Related concepts, Statistical use, Common misconceptions, History, Worked example. On this template the research `## Worked example` body is merged into the generated **Examples** section, and `## Proof` is rendered as a callout, not as a display-titled H2. Live section order is Statement, then Motivating example, then Intuition, then Proof.
- On concept and distribution pages, the research `## Definition` is appended after a formula already injected from the chapter lead or from `distributions.json`. Do **not** paste a second copy of that displayed formula. Rewrite openers such as “Here $X$ is…” so they name the displayed formula instead of pointing at it with “Here” or “above.”
- The generated opening sentence comes from `article_leads.json` and is then followed by `## Lead context`. Rewrite Lead context so it does not repeat that sentence, and so it does not start with a dangling “It” or “Its”. If the generated sentence already carries the idea, drop a thin Lead context rather than padding it.
- Generated chrome is off limits: hatnote, infobox, **See also**, **References**, **Cite this page**, and the **Check yourself** block injected from `research/self-checks.json`. Exception: if a research file itself contains a `## Check yourself` section, or inline Check yourself questions, follow that page’s plan. Do not add a new in-file Check yourself section on a page that already has 2–3 generated questions. Do not edit `research/self-checks.json`.
- Keep the `**Your turn.**` exercises and their folded answers. Do not replace that label with a new stock closer.
- **Connections**: do not write a link farm that restates See also. Keep at most a short paragraph that explains a relationship the link list cannot. Relocate any unique link into remaining prose before deleting padding.
- Chapter figures may appear on the live article (for example `{#fig-prob-distribution-function}` and `{#fig-prob-discrete-pmfs}`). Name a figure by its caption or label; do not write “the die plot on this page” or “the figures below.”
- Build order can move Statistical use relative to Worked example. That is why relative references must be replaced even when they currently look correct.

## Source notes (no Researcher hold)

These eight pages already meet the citation quota from at least two independent sources, and every existing History section already has a citation. This batch is ready to implement without waiting for Researcher. Optional later improvements, not to be invented here:

- **continuous-distribution** History attributes the 1933 axioms to Kolmogorov via `knill2009_probability`. Sister pages already cite `kolmogorov1933_slln` (Ch. III, §2) for the random-variable and CDF conventions; do not add that key to this History unless the locator actually supports the axiomatic claim being made (the axioms are not in Ch. III, §2).
- **poisson-limit-of-the-binomial** has no History section. A sourced origin for the Poisson approximation would be useful later. Do not invent one, and do not lean on `dodge2008`.

---

## Pages

### 1. Random variable

- **File:** `research/content/random-variable.md`
- **URL:** https://www.statwiki.io/articles/random-variable.html
- **Chapter source (do not edit):** `sources/stat2003/chapters/prob-02-random-variables.qmd`
- **Template:** concept

**Opening.** Generated lead is: “In probability theory, a **random variable** is a rule that assigns a numerical value to each outcome of a random experiment.” Lead context then restates the rule-on-outcomes idea before adding the useful distinction between the function, its law, and a realised value. Keep that distinction; drop the opening restatement so the paragraph does not begin by repeating the generated sentence. Do not start with “A random variable connects….”

**Headings to rename (canonical key → display title):**

- Motivating example → Two tosses, one number of heads
- Intuition → The rule is fixed; the outcome is random
- Definition → A measurable map from outcomes to numbers
- Properties → Transformations, expectation, and the CDF
- Statistical use → A sample, a statistic, and an indicator
- Worked example → The sum of two dice, and an indicator of a large sum
- Common misconceptions → A variable, a law, and a realised value are not the same
- Assumptions and limits → The sample space, integrability, and the dice model
- Connections → Events, laws, statistics, and joint distributions
- History → Kolmogorov's 1933 threshold definition

**Relative references.** In Assumptions and limits, “the expectation formula with signed $g$ requires absolute integrability as stated above” should name the condition already in Properties ($\mathbb{E}|g(X)|<\infty$), not “above.”

**Check yourself.** None in the research file. `self-checks.json` already has 2 items: `ex-prob-three-point-expectation` (values $0,2,5$ with probabilities $1/2,1/3,1/6$) and `ex-prob-second-moment` (recover $\mathbb{E}X^2$ from mean $2$ and variance $1$). The second ID is also used on `variance` and `moments-of-the-sample-mean-and-variance`. Flag the shared ID for Peer Review; do not edit the JSON and do not add an in-file section. Neither question copies the two-dice Worked example or the Your turn ($\mathbb{P}(X\ge 11)=3/36=1/12$).

**History.** Keep and tighten. It already cites Kolmogorov, *Grundbegriffe* (1933), Ch. III, §2, for the $X<a$ convention, and Billingsley §§13–14 for the equivalent Borel-preimage condition and the $X\le x$ convention. Keep both points; they are the distinctive content. Do not retell the whole measure-theoretic setup.

**Must not change:** the measurability condition $\{X\le x\}\in\mathcal{F}$; the two-dice arithmetic ($\mathbb{P}(X=7)=6/36=1/6$, $F_X(4)=6/36=1/6$, $\mathbb{E}X=7$, $\mathbb{P}(Y=1)=6/36=1/6$); the Your turn outcomes $(5,6)$, $(6,5)$, $(6,6)$ and $3/36=1/12$; existing citation markers; the History section; the proof of the transformation law and the quantile construction.

**No statistical errors found.**

**Before-counts:** 27 citations, 4 distinct sources (`billingsley1995`, `durrett2019`, `kolmogorov1933_slln`, `nist_glossary2002`); 0 in-file Check yourself questions; 2 generated (`ex-prob-three-point-expectation`, shared `ex-prob-second-moment`); History present and sourced.

---

### 2. Discrete distribution

- **File:** `research/content/discrete-distribution.md`
- **URL:** https://www.statwiki.io/articles/discrete-distribution.html
- **Chapter source (do not edit):** `sources/stat2003/chapters/prob-02-random-variables.qmd`
- **Template:** concept

**Opening.** Generated lead is: “In probability theory, the **discrete distribution** is a probability distribution concentrated on a finite or countable set of values.” Lead context is only:

> It lets probabilities for a count or a category be calculated by adding the masses of the values of interest.

Rewrite so it does not start with “It lets” and does not repeat the generated definition. One new point is enough: a probability for a set of values is the sum of the masses on that set, including when the support is countably infinite.

**Headings to rename (canonical key → display title):**

- Motivating example → Adding the chances of two or more missed appointments
- Intuition → Masses as weights, and jumps in the CDF
- Definition → Probability one on a countable set
- Properties → Jumps, endpoint conventions, and transformed masses
- Worked example → Three inspections with defect probability $1/4$
- Common misconceptions → Discrete does not mean equally likely
- Connections → Masses, expectation, and named count laws
- History → From finite games of chance to countable supports

Keep the existing titles on Statistical use (“When a count model is appropriate”) and Assumptions and limits (“Limits of a probability mass function”).

**Relative references (must change).**

- Motivating example, “the dice-sum example below”: the $6/36$ and $1/36$ figures are already in this same paragraph, and the Worked example is the three-inspection binomial, not a dice sum. Drop “below” and keep the arithmetic in this paragraph; do not promise a later dice-sum worked example.
- Intuition, “the die plot on this page”: name the chapter figure of a fair die's mass function and right-continuous staircase (`{#fig-prob-distribution-function}`), or describe that staircase without “on this page.”
- Properties, “the sum and minimum of two dice in the examples below”: those calculations are not in this page's Worked example. Replace with a one-line preimage-sum illustration here, or a named link to a specific question (for example [the sum of two dice](../questions/ex-prob-dice-sum-pmf.qmd)), not “the examples below.”
- Statistical use, “The figure of binomial, geometric and Poisson masses”: name `{#fig-prob-discrete-pmfs}` (successes in 10 trials, trial of first success, Poisson mean 10), or describe those three laws without “the figure of.”

**Check yourself.** None in the research file. `self-checks.json` already has 2 items: `ex-prob-wait-pmf` (waiting-time mass function until two dice sum to 12) and `ex-prob-joint-table` (a joint mass table, including independence and $\mathbb{E}(X^2 Y)$). The second is really a joint-distribution question; flag that, but do not edit the JSON and do not add an in-file section. Neither question copies the Worked example or the Your turn ($p=1/3$, two trials: masses $4/9,4/9,1/9$, $\mathbb{P}(Y\ge 1)=5/9$, $\mathbb{E}Y=2/3$).

**History.** Keep and tighten. It already cites the Grinstead–Snell preface for the Pascal–Fermat tradition and Durrett Ch. 1, §1.2 for the modern countable-support definition. Keep both; do not expand into an unsourced history of the mass function.

**Must not change:** the definition $\mathbb{P}(X\in S)=1$ on a countable $S$, $p_X(x)=\mathbb{P}(X=x)$, and $\mathbb{P}(a<X\le b)=F_X(b)-F_X(a)$; the geometric masses $p(1-p)^{x-1}$; the three-inspection masses $27/64$, $27/64$, $9/64$, $1/64$, $\mathbb{P}(X\ge 2)=5/32$, $F_X(1)=27/32$, $\mathbb{E}X=3/4$; the Your turn masses and $5/9$, $2/3$; the motivating dice sums $6/36$ and $1/36$; existing citation markers; the History section; the proof of the jump and preimage-sum rules.

**No statistical errors found.**

**Before-counts:** 22 citations, 2 distinct sources (`durrett2019`, `grinstead_snell1997`); 0 in-file Check yourself questions; 2 generated; History present and sourced.

---

### 3. Continuous distribution

- **File:** `research/content/continuous-distribution.md`
- **URL:** https://www.statwiki.io/articles/continuous-distribution.html
- **Chapter source (do not edit):** `sources/stat2003/chapters/prob-02-random-variables.qmd`
- **Template:** concept

**Opening.** There is no Lead context. Generated lead is: “In probability theory, a **continuous distribution** is an atom-free probability law used to calculate chances for ranges of real-valued outcomes.” That gloss uses the broader, atom-free sense, which the Definition then distinguishes from absolute continuity. Leave `article_leads.json` alone; do not add a thin Lead context that only repeats the gloss. If a Lead context is added, it should be the distinction (atom-free versus a density), not a restatement of “atom-free.”

**Headings to rename (canonical key → display title):**

- Motivating example → A reaction time is judged by intervals, not exact instants
- Intuition → Height is concentration; area is probability
- Worked example → A linear density on $(0,2)$, and a sensor with an atom
- Common misconceptions → A density value is not a point probability
- Assumptions and limits → Rounding, mixed laws, and the Cantor counterexample
- Connections → CDFs, atoms, and named density families
- History → Area calculations and the axiomatic distinction

Keep the existing titles on Definition (“Two uses of continuous”), Interpretation (“Areas, heights and units”), Properties (“What a density guarantees”), and Statistical use (“Likelihood and recorded measurements”).

**Relative references (must change).**

- Motivating example, “The figures contrast smooth density curves with the jumps of a discrete distribution function”: name the relevant chapter figures (`{#fig-prob-distribution-function}`, and `{#fig-prob-continuous-densities}` if that is the density panel used), rather than “the figures.”
- Interpretation, “The examples use this: a cubic CDF yields a density… while a uniform point in an interval yields probabilities by length”: those calculations are not in this Worked example. Either give a one-line illustration here or name and link the actual questions ([Distance to the centre](../questions/ex-prob-random-radius.qmd) derives a density from a geometric probability; the uniform length rule is already in this Interpretation). Do not point at “the examples.”
- Connections, “The distance-to-the-centre question… the lifetime question… and the shifted-exponential question”: replace these informal names with the same named links (`ex-prob-random-radius`, `ex-prob-component-five-years`, `ex-prob-shifted-exp-generate`). Do not give away their answers.

**Check yourself.** None in the research file. `self-checks.json` already has 3 items (`ex-prob-random-radius`, `ex-prob-component-five-years`, `ex-prob-shifted-exp-generate`). That is the allowed maximum. Do not add an in-file section and do not edit the JSON. They are distinct from the Worked example ($f(x)=c(1+x)$ on $(0,2)$) and the Your turn (atom $0.2$ plus uniform on $(0,1)$).

**History.** Keep and tighten. It already cites Knill for the axiomatic setting and the Cantor illustration, and Siegrist for the density-based elementary theory. Keep the distinction between area calculations and the later event-based formulation. Do not add an unsourced Kolmogorov locator.

**Must not change:** the two conventions (absolutely continuous versus atom-free); the Cantor / ternary-sum argument in the proof; the uniform-on-$[0,0.25]$ height $4$ and interval probability $0.20$; the Worked example $c=1/4$, $F(x)=(x+x^2/2)/4$, $\mathbb{P}(0.5<X<1.5)=0.5$, $\mathbb{E}X=7/6$, $f(1)=0.5$; the Your turn $\mathbb{P}(X=0)=0.2$, $\mathbb{P}(0.25<X<0.75)=0.4$; existing citation markers; the History section.

**No statistical errors found.**

**Before-counts:** 23 citations, 2 distinct sources (`knill2009_probability`, `siegrist2022_continuous`); 0 in-file Check yourself questions; 3 generated; History present and sourced.

---

### 4. Cumulative distribution function

- **File:** `research/content/cumulative-distribution-function.md`
- **URL:** https://www.statwiki.io/articles/cumulative-distribution-function.html
- **Chapter source (do not edit):** `sources/stat2003/chapters/prob-02-random-variables.qmd`
- **Template:** concept

**Opening.** Generated lead is: “In probability theory, the **cumulative distribution function** is the probability that a random variable does not exceed a chosen value.” Lead context then restates the threshold idea before adding mixed laws and the jump convention. Keep the jump convention ($F(x)$ includes the mass at $x$); drop the opening restatement of “probabilities below a threshold.”

**Headings to rename (canonical key → display title):**

- Motivating example → At most four on a die, and a smooth rise
- Intuition → Accumulating probability from left to right
- Definition → $F(x)=\mathbb{P}(X\le x)$
- Properties → Monotonicity, right-continuity, and the quantile inverse
- Interpretation → Staircases, smooth rises, and the inverse-transform reading
- Statistical use → The empirical CDF, tails, and quantiles
- Worked example → An atom at zero and a uniform remainder
- Common misconceptions → A CDF is a probability; a density need not be
- Assumptions and limits → One dimension, and independence for a product of CDFs
- Connections → Mass functions, densities, quantiles, and the empirical CDF
- History → Kolmogorov's strict inequality and the modern $\le$ convention

**Relative references (must change).**

- Interpretation, “The first figure compares a die's staircase CDF with an exponential law's smooth CDF”: name `{#fig-prob-distribution-function}` (or its caption), not “the first figure.”
- Interpretation, “The inverse-transform figure below”: name that figure, or describe the inverse-transform reading without “below.” (On the live page, figures may sit in Interpretation, so “below” is already unreliable.)

**Check yourself.** None in the research file. `self-checks.json` already has 2 items: `ex-prob-unit-square-max` (CDF and density of $\max(X,Y)$ on the unit square) and `ex-sp-right-continuous` (why $F(x)=0$ for $x\le 0$ and $F(x)=1$ for $x>0$ is not a distribution function). The second ID is also used on `measurable-random-variable`. Flag the shared ID; do not edit the JSON and do not add an in-file section. Neither question copies the Worked example or the Your turn ($\mathbb{P}(X=0)=1/4$, $Q(1/8)=0$).

**History.** Keep and tighten. It already contrasts Kolmogorov's $P(X<x)$ (left-continuous) convention with Billingsley's $P(X\le x)$ (right-continuous) convention and the generalized-inverse construction. Keep that contrast; it is the distinctive content.

**Must not change:** $F_X(x)=\mathbb{P}(X\le x)$; $\mathbb{P}(a<X\le b)=F_X(b)-F_X(a)$; $\mathbb{P}(X=a)=F_X(a)-F_X(a-)$; the quantile $Q(u)=\inf\{x:F_X(x)\ge u\}$; the mixed-law CDF $0$ for $x<0$, $1/4+3x/4$ for $0\le x<1$, and $1$ for $x\ge 1$; $F_X(1/2)=5/8$; $\mathbb{P}(0<X\le 1/2)=3/8$; $Q(1/2)=1/3$; the Your turn $Q(1/8)=0$; the empirical illustration $F_5(2)=3/5$; existing citation markers; the History section; the proof, including the inverse-transform identity and the maximum's product formula under independence.

**No statistical errors found.**

**Before-counts:** 26 citations, 3 distinct sources (`billingsley1995`, `durrett2019`, `kolmogorov1933_slln`); 0 in-file Check yourself questions; 2 generated (one shared); History present and sourced.

---

### 5. Expectation

- **File:** `research/content/expectation.md`
- **URL:** https://www.statwiki.io/articles/expectation.html
- **Chapter source (do not edit):** `sources/stat2003/chapters/prob-02-random-variables.qmd`
- **Template:** concept

**Opening.** Generated lead is: “In probability theory, **expectation** is the probability-weighted average of a random variable, used to judge long-run outcomes and uncertain choices.” (`article` is already `""`; do not set it to “the” or “an.” If a preview shows a double space after the comma, leave the JSON as it is unless a one-character tidy in this key is clearly enough; do not edit `build_wiki.py`.) Lead context is:

> It gives a common scale for comparing uncertain payoffs and is the starting point for variance and many estimators. An expected value need not be a value that can actually occur.

Rewrite so it does not start with “It gives” and does not repeat “probability-weighted average.” Keep the point that the expected value need not be an attainable outcome.

**Headings to rename (canonical key → display title):**

- Motivating example → A rain surcharge of 100 dollars with probability 0.3
- Intuition → A weighted centre, not necessarily an attainable value
- Definition → The displayed sum or integral, and the Stieltjes form
- Properties → Linearity, indicators, and the tower property
- Statistical use → The sample mean, and expected cost
- Worked example → A fair-die game with a 2-dollar stake
- Common misconceptions → The mean need not be observable, and linearity needs no independence
- Assumptions and limits → The St Petersburg game, and nonintegrable tails
- Connections → Variance, conditional expectation, and the sample mean
- History → Huygens's 1657 fair price for a chance

**Definition and relative references (must change).** The live Definition already prepends the chapter formula ($\mathbb{E}X=\sum x f(x)$ or $\int x f(x)\,\mathrm{d}x$, with absolute convergence). Do not paste a second copy of that formula into the research file. Rewrite “Here $X$ is a random variable…” so it names the displayed formula and then adds the mixed-law Stieltjes form $\mathbb{E}X=\int x\,\mathrm{d}F_X(x)$.

- Properties, “The [expectation-of-a-function](expectation-of-a-function.qmd) formula above”: drop “above”; the link already names the referent.
- Proof, “The discrete proof of the function rule, by grouping equal values of $g$, appears above”: that proof is not on this page. Point to the [expectation of a function](expectation-of-a-function.qmd) page, or give the one-line grouping idea here without “appears above.”

**Giveaway block (must cut).** After the Your turn, the file has a “Try [the wait for double six]… then [a spike that keeps its mean]…” paragraph and a folded **Answers** callout that states $\mathbb{E}=36$ and $\mathbb{E}X_n=1$, $\mathbb{E}X_n^2=n$. Those are the two generated Check yourself questions. Delete the “Try…” sentence and the Answers callout. Leave the questions to the generated Check yourself block. Keep the Your turn and its own answer ($4.50$ with probability $1/3$ and $-1.50$ with probability $2/3$, so $\mathbb{E}X=0.50$).

**Check yourself.** After the cut, none remain in the research file. `self-checks.json` already has 2 items: `ex-prob-double-six-wait` and `ex-sp-spike`. The second ID is also used on `monotone-convergence-fatou-and-dominated-convergence`. Flag the shared ID; do not edit the JSON and do not add a replacement in-file section. They do not copy the Worked example ($\mathbb{E}X=-2/3$).

**History.** Keep and tighten. It already cites Huygens (1657), Props. I–III, for valuing equal and unequal chances. Keep that origin; do not pad it into a history of modern integration.

**Must not change:** linearity and $\mathbb{E}\mathbf{1}_A=\mathbb{P}(A)$; the rain example $0.3\times 100=30$; the fair-die mean $3.5$; the Worked example $6\times(1/6)-2\times(5/6)=-2/3$; the Your turn $0.50$; the St Petersburg terms $2^n\cdot 2^{-n}=1$; existing citation markers; the History section; the tower-property proof.

**No statistical errors found.**

**Before-counts:** 18 citations, 3 distinct sources (`durrett2019`, `grinstead_snell1997`, `huygens1657`); 0 in-file Check yourself questions, but a giveaway Answers block (must cut); 2 generated (one shared); History present and sourced.

---

### 6. Variance

- **File:** `research/content/variance.md`
- **URL:** https://www.statwiki.io/articles/variance.html
- **Chapter source (do not edit):** `sources/stat2003/chapters/prob-02-random-variables.qmd`
- **Template:** concept

**Opening.** Generated lead is: “In probability theory, **variance** is a measure of how spread out a random variable is around its mean.” (`article` is already `""`; same double-space note as for expectation.) Lead context starts “It lets you distinguish outcomes that have the same average….” Rewrite so it does not start with “It lets you” and does not repeat “spread around its mean.” Keep the pointer to [sample variance](sample-variance-and-standard-deviation.qmd) as an estimator of this population quantity.

**Headings to rename (canonical key → display title):**

- Motivating example → Two buses with the same average delay
- Intuition → Squared deviations, so large misses count more
- Definition → The displayed second-moment formula, for a mass or a density
- Properties → Nonnegativity, scaling, and the covariance term
- Statistical use → Independent replicates and the standard error
- Worked example → A delivery that is early, on time, or late
- Common misconceptions → Variance and standard deviation use different units
- Assumptions and limits → No finite variance, and sensitivity to extremes
- Connections → Covariance, standard error, and sample variance
- History → Fisher names the square of a standard deviation

**Definition and relative references (must change).** The live Definition already prepends the chapter formula $\operatorname{Var}(X)=\mathbb{E}(X-\mathbb{E}X)^2$ and the equivalent $\mathbb{E}X^2-(\mathbb{E}X)^2$. Do not paste a second copy. Rewrite “Here $X$ is the random variable…” so it names that displayed formula, then keeps the finite-second-moment condition and the discrete-sum / density-integral calculations. The proof's phrase “proving the equivalent formula in the definition” can then point to that displayed identity by name.

- Connections, “the independent-measurement calculation above”: name Statistical use (the $\sigma^2/n$ calculation for an independent sample mean).

**Giveaway block (must cut).** After the Your turn, the file links [the normal-variance derivation](../questions/ex-prob-normal-variance.qmd) (a link without an answer is fine if kept in Connections), then a “Try [recovering the second moment]… Then try [proving the normal variance]… Reveal each answer when you are ready.” paragraph and a folded **Answers** callout stating $\mathbb{E}X^2=5$ and $\operatorname{Var}(X)=1$ for a standard normal. Those are the two generated Check yourself questions. Delete the “Try… Reveal…” paragraph and the Answers callout. Keep the Your turn (mean $3$, variance $8/3$).

**Check yourself.** After the cut, none remain in the research file. `self-checks.json` already has 2 items: `ex-prob-normal-variance` and `ex-prob-second-moment` (shared with `random-variable` and `moments-of-the-sample-mean-and-variance`). Flag the shared ID; do not edit the JSON and do not add an in-file section. They do not copy the Worked example ($\mu=1/2$, $\mathbb{E}X^2=5$, $\operatorname{Var}(X)=19/4$, $\sqrt{19}/2$).

**History.** Keep and tighten. It already cites Fisher (1918 / 1919 volume), p. 399, for naming the square of a standard deviation in the study of resemblance between relatives. Keep that sourced origin.

**Must not change:** $\operatorname{Var}(aX+b)=a^2\operatorname{Var}(X)$; $\operatorname{Var}(X+Y)=\operatorname{Var}(X)+\operatorname{Var}(Y)+2\operatorname{Cov}(X,Y)$; the bus example (variance $0$ versus $100$ squared minutes); the Worked example $\mu=1/2$, $\mathbb{E}X^2=5$, $19/4=4.75$, $\sqrt{19}/2\approx 2.179$; the Your turn mean $3$ and variance $8/3$; existing citation markers; the History section; the proof of nonnegativity, scaling, and the covariance expansion.

**No statistical errors found.**

**Before-counts:** 15 citations, 3 distinct sources (`fisher1919_variance`, `grinstead_snell1997`, `nist_handbook2002`); 0 in-file Check yourself questions, but a giveaway Answers block (must cut); 2 generated (one shared); History present and sourced.

---

### 7. Gamma distribution

- **File:** `research/content/gamma-distribution.md`
- **URL:** https://www.statwiki.io/articles/gamma-distribution.html
- **Chapter source (do not edit):** `sources/stat2003/chapters/prob-02-random-variables.qmd`
- **Template:** distribution (card in `distributions.json`)

**Opening.** There is no Lead context. Generated lead is: “In probability theory and statistics, the **gamma distribution** is a positive-valued law for waiting times that also supplies priors for event rates.” That is accurate and does not need a restatement. Leave `article_leads.json` alone; do not add a thin Lead context.

The live Definition already prepends the shape–rate density $p(x)=\lambda^{\alpha}x^{\alpha-1}e^{-\lambda x}/\Gamma(\alpha)$ from `distributions.json`, and the infobox repeats the mean, variance, mode, skewness and MGF. Do not paste a second copy of the density. Keep the research Definition as the convention warning (rate versus scale, mean $\alpha/\lambda$ not $\alpha\lambda$, and the incomplete-gamma CDF as a left-tail probability).

**Headings to rename (canonical key → display title):**

- Motivating example → Waiting for the third call
- Intuition → A power near zero and an exponential tail
- Definition → Shape–rate convention, and the incomplete-gamma CDF
- Properties → The MGF, equal-rate sums, and relative spread
- Related distributions → Exponential, Erlang, chi-squared, and inverse-Gamma
- Statistical inference → A duration model, and a conjugate update for a Poisson rate
- Generating random samples → Exponential sums, and SciPy's scale argument
- Worked example → The third call at rate 2, and a two-hour tail
- Common misconceptions → Rate versus scale, and a prior is not a waiting time
- Connections → Poisson processes, special cases, and two different modelling roles
- History → Laplace, Pearson's Type III, and the Erlang special case

Keep the existing title on Assumptions and limits (“When the waiting-time model fails”).

**Relative references (must change).**

- Intuition, “These statements come from the mode, scaling and skewness formulas in the infobox and the single proof in Properties”: there is no proof callout in Properties. Name the infobox identities (mode $(\alpha-1)/\lambda$ for $\alpha>1$, coefficient of variation $1/\sqrt{\alpha}$, skewness $2/\sqrt{\alpha}$) and the MGF already displayed in Properties. Do not promise “the single proof in Properties.”
- Properties, “The proof above derives these features from the gamma integral, cumulants and derivative of the log density”: same stale promise. Either replace it with a short, sourced derivation of the mean (and, if compact, the mode) from the gamma integral, or drop the claim and point to the infobox / MGF identities. Do not leave “the proof above.” Do not change the stated formulae.

**Check yourself.** None in the research file. `self-checks.json` already has 2 items: `c-10` (“State the kernels and support of shape–rate $\operatorname{Gamma}(a,b)$ and $\operatorname{InvGamma}(a,b)$.”) and `c-23` (“What response support and mean–variance relationships define Gamma and inverse-Gaussian GLMs?”). `c-10` is also used on `inverse-gamma-distribution` and `marginal-variance-posterior`; `c-23` is also used on `generalised-linear-model` (already polished in batch 001) and is really a GLM variance-function question, not a question about the gamma distribution itself. Flag both shared IDs, and flag that `c-23` is off-topic for this page. Do not edit the JSON in this batch and do not add an in-file section that would make a third copy. They do not copy the Worked example or the Your turn ($T_2\sim\operatorname{Gamma}(2,1)$, mean and variance $2$, $\Pr(T_2>3)=4e^{-3}\approx 0.1991$).

**History.** Keep and tighten. It already cites Laplace (1812) pp. 1–4, Pearson (1895) pp. 373–374 for the Type III curve, Forbes for the Erlang name, and Siegrist / Grimmett–Stirzaker for the waiting-time special case. Keep those sourced points. The closing sentences about renewal and queueing can be tightened so the section stays a history, not a second Connections paragraph. Do not cut the section.

**Must not change:** the shape–rate convention and mean $\alpha/\lambda$, variance $\alpha/\lambda^2$; MGF $(1-t/\lambda)^{-\alpha}$; the Poisson–Gamma update $\operatorname{Gamma}(\alpha+S,\lambda+n)$ (and $\lambda+\sum t_i$ with unequal exposures); the Worked example $T_3\sim\operatorname{Gamma}(3,2)$, mean $1.5$, variance $0.75$, $\Pr(T_3>2)=13e^{-4}\approx 0.2381$, $F(2)\approx 0.7619$; the Your turn $4e^{-3}\approx 0.1991$; the unequal-rate counterexample (means $1.5$, variances $1.25$ versus $1.125$); existing citation markers; the History section; SciPy's `scale=1/\lambda` warning.

**No statistical errors found.**

**Before-counts:** 28 citations, 9 distinct sources (`diaconis_ylvisaker1979`, `forbes2011`, `gelman_bda2013`, `grimmett_stirzaker2020`, `laplace1812`, `pearson1895`, `scipy_gamma2026`, `siegrist2022_gamma`, `siegrist2022_gamma_waiting`); 0 in-file Check yourself questions; 2 generated (`c-10` shared, `c-23` shared and off-topic); History present and sourced.

---

### 8. Poisson limit of the binomial

- **File:** `research/content/poisson-limit-of-the-binomial.md`
- **URL:** https://www.statwiki.io/articles/poisson-limit-of-the-binomial.html
- **Chapter source (do not edit):** `sources/stat2003/chapters/prob-02-random-variables.qmd`
- **Template:** theorem (`thm-poisson-limit-of-the-binomial`)

**Opening.** Generated lead is: “In probability theory, the **Poisson limit of the binomial** is a limit result that turns many rare independent trials into a Poisson count.” Lead context adds: “The rare-event limit keeps the expected count finite while increasing the number of independent trials.” That is a useful extra point, not a restatement. Leave it, or tighten it slightly, but do not start a new Lead context with “It.” Leave `article_leads.json` alone (`proper: true` is already set).

**Headings to rename (canonical key → display title):**

- Motivating example → Many independent opportunities, a small chance on each
- Statement → Binomial counts with $np_n\to\lambda$ converge to $\operatorname{Poisson}(\lambda)$

Keep the existing titles on Intuition (“One expected count survives the limit”) and Related concepts (“Unequal rare-event probabilities”). Do not put a display title on `## Proof`: the theorem template renders Proof as a callout, not as a display-titled H2. A display title on `## Worked example` will not appear as a live H2 either; the body is merged into **Examples**. Keep the `## Worked example` key and its body (including Your turn); do not invent an `## Examples` key.

Remember the live section order on this template: Statement, then Motivating example, then Intuition, then Proof, with the worked numerical example later under Examples. That is why “the probability calculation below” must be replaced.

**Relative references (must change).**

- Intuition, “The probability calculation below establishes the full fixed-count limit”: name the Proof (or “the binomial-to-Poisson calculation in the Proof”), not “below.”

**Check yourself.** None in the research file. `self-checks.json` already has 2 items: `ex-prob-radioactive` (3600 independent seconds at probability $1/100$; Poisson mean $36$) and `ex-prob-brisbane-groups` (groups of three birthdays among one million people). Both are on-topic and distinct from the Worked example ($n=100$, $p=0.02$, mean $2$). Do not add an in-file section and do not edit the JSON.

**History.** None. Do not invent a section.

**Must not change:** the statement ($X_n\sim\operatorname{Bin}(n,p_n)$, $np_n\to\lambda$, pointwise masses $e^{-\lambda}\lambda^k/k!$); the displayed factorisation and the $n\log(1-p_n)=-\lambda_n+O(np_n^2)$ step; the Worked example $0.98^{100}\approx 0.132620$ versus $e^{-2}\approx 0.135335$, and $P(X=3)\approx 0.182276$ versus $e^{-2}2^3/3!\approx 0.180447$; the Your turn $p=0.002$ and $0.998^{1000}\approx 0.135065$; the Related concepts conditions (independent indicators, maximum probability $\to 0$, sums $\to$ a finite limit); existing citation markers; the `[]{#property-unequal-independent-array}` anchor.

**No statistical errors found.** The reported approximations were rechecked.

**Before-counts:** 8 citations, 2 distinct sources (`durrett2019`, `grinstead_snell1997`); 0 in-file Check yourself questions; 2 generated; no History section.

---

## Implementation order

1. Check `article_leads.json` keys only if a preview shows the glitch named above (`expectation` and `variance` empty `article` / possible double space). In the usual case, leave the JSON untouched.
2. Edit the eight `research/content/*.md` files as specified, one article at a time, running a heading-key check (`## Key` or `## Key — title`, keys already used on that page only, no unknown keys invented in this batch, and no key the page's template will drop).
3. On `expectation.md` and `variance.md`, delete the Check-yourself giveaway blocks first, then do the heading and relative-reference work, so those answers cannot be reintroduced by accident.
4. Do not regenerate or commit `_site` or `articles/*.qmd`. Leave the source edits in a branch / PR for review.
5. After implementation, a reviewer should open the eight live-or-preview URLs and confirm: topic-specific H2s; no dangling “It/Its” and no circular lead after the generated sentence; no “above / below / on this page / the examples below / the proof above / Here $X$ is” left pointing at a movable section; the expectation and variance pages no longer reveal $\mathbb{E}=36$, $\mathbb{E}X_n=1$, $\mathbb{E}X^2=5$, or $\operatorname{Var}(X)=1$ for the standard normal; History sections still present on the seven pages that had them, and still absent on the Poisson-limit page; maths and Your turn answers unchanged; See also / References / chapter excerpts and figures still present; `research/self-checks.json`, `sources/`, and `build_wiki.py` untouched.

## What Peer Review needs to verify

- **Scope:** only the eight research files listed above, plus `article_leads.json` only if a named key was actually changed. No `sources/`, `build_wiki.py`, `research/self-checks.json`, `research/*.md` (non-content tree), `articles/*.qmd`, or `proofs-todo.json`.
- **Integrity counts:** each page still has at least 5 citation markers from at least 2 independent sources (before-counts above). No `dodge2008` or `sas2012_glm` markers added. Citation keys and locators on unchanged claims are preserved.
- **History:** present and tightened, not cut, on all seven pages that had a section; still absent on `poisson-limit-of-the-binomial`.
- **Maths:** `$...$` / `$$...$$` only; every “Must not change” value and formula still present; no substance changes except the flagged presentation fixes (relative references, missing named referents, giveaway blocks).
- **Check yourself:** 2–3 generated questions remain on every page; no new in-file section; the two giveaway Answers blocks are gone. Shared IDs, left in place: `ex-prob-second-moment` (`random-variable`, `variance`, `moments-of-the-sample-mean-and-variance`); `ex-sp-right-continuous` (`cumulative-distribution-function`, `measurable-random-variable`); `ex-sp-spike` (`expectation`, `monotone-convergence-fatou-and-dominated-convergence`); `c-10` (`gamma-distribution`, `inverse-gamma-distribution`, `marginal-variance-posterior`); `c-23` (`gamma-distribution`, `generalised-linear-model`, and off-topic for the gamma distribution page).
- **Plan conformance and CI:** display titles on the listed headings; template keys respected (especially gamma's Statistical inference, and the theorem-page Proof / Examples behaviour); green CI, ignoring the known Workers Builds failure; no scratch files in the PR.
- **Quoted Chris approval for anything out of scope:** none needed. `sources/` is allowed, but this batch does not use that permission.

## ADDENDUM (19 Nov 2026, 8:00pm)
- Retitle exercise ex-prob-second-moment ("Recovering the second moment") in its sources/stat2003 chapter to a title that says what is asked (e.g. "Finding E[X^2] from the mean and variance"); keep the file's line endings. Search data: 201 impressions, 0 clicks.
- PR #89 adds Check yourself items on variance and expectation; rebase on main after #89 merges and don't duplicate them.

## ADDENDUM (20 Nov 2026, 9:00am)
- Precedence note 6's reference to PR #65 is stale. `research/self-checks.json` and `sources/depth-questions.json` are now changed by open PR #91 (Check yourself prompts move to the question bank). Cut this branch from `main` after #89 and #91 merge, and do not edit either file. If #91 has moved a page's Check yourself prompts by then, the two giveaway Answers blocks (expectation, variance) may already be gone. Verify on main, and skip the cut if so.
