> **Handover note (20 Nov 2026):** Editor's backlog as of 19 Nov 2026 evening. Items marked done in docs/automation/HANDOVER.md are done; the SEO audit/duplicate reports it cites were private working files and are not in the repo. Copied from the previous automation's private workspace; paths were rewritten to repo paths.

# Editor backlog
- score-function History is vague; fisher-scoring History centres on R glm.fit. Ask Researcher for sourced history (keep sections).
- GLM line ~25 "canonical form above" should mean the exponential-family form.
- Self-check IDs shared across pages: q-45 (GLM, random-component), q-33 (score-function, fisher-information), ex-sl-10-7 (linear-predictor, logit-link).
- Web sources have section locators but no page numbers.
- Audit pages citing sas2012_glm Ch.3 or Dodge biography entries for technical claims (may not support them).
- 47 "no worked answer" questions; 9 "A tempting wrong turn" titles; 20 duplicate titles.
- Findability aliases: z-score, Mann-Whitney, Bayes' theorem.
- Maths delimiter conversion (PR #72 covers it).
- Missing datasets (cholest.csv, studentsurvey.csv, heart.csv, alon.rda) and helpers (stratified_folds, scale_train).
- sign-test, wilcoxon-rank-sum-test, f-test-for-equal-variances, normal-quantile-plot: add prose links to new pages (wilcoxon-signed-rank, shapiro-wilk, friedman, levene) after #78 merges.
- wilcoxon1945 bibliography entry: pages 80-83.
- Build may place Statistical use before Worked example, making "above" a forward reference: plans must avoid relative references.
- Levene 1960 / Brown-Forsythe 1974 not read; #78 uses Gastwirth, Gel & Miao (2009). Find full texts later and add direct locators.

## batch-003 (GLM count models) — held, ready to send when PRs in flight < 3
- Ask Researcher for sourced locators before dispatch: count-responses (needs 5 citations / 2 sources, plus History); underdispersion (only Dodge p. 341); quasi-Poisson (cite wedderburn1974); count-models-beyond-the-Poisson (only Dodge pp. 425–426); Conway–Maxwell–Poisson (conway_maxwell1962 / shmueli2005 / huang2017_cmp, plus History); negative binomial History (greenwood_yule1920 directly); Poisson regression History unsourced; overdispersion History should cite nelder_wedderburn1972.
- Branch: claude/content/glm-count-models. #65 overlaps three files (Repo Helper said don't wait).
- Self-check IDs shared across pages (Peer Review, 19 Nov): q-45 (GLM / random-component), q-33 (score-function / fisher-information), ex-sl-10-7 (linear-predictor / logit). Needs dedup in a later batch.
- #80 locator fix may move to the content side. Worst pages: diversity-index, hawthorne-effect, computational-biology.
- Stepped (aligned) equations for long chains if UX picks option B: 182 concept pages, starting with sampling-distribution-of-the-regression-estimators, jacobian, cramer-rao-lower-bound, fisher-scoring.
- Conway–Maxwell–Poisson page: needs printed-page locators for conway_maxwell1962 / shmueli2005 / huang2017_cmp (library access). Dodge Poisson markers to remove. Verified numbers: Z(1,2)≈2.2796, P(0)≈0.4387, mean 0.6978, var 0.5131.
- Self-check c-23 on gamma-distribution is shared with generalised-linear-model and is off-topic (Gamma vs inverse-Gaussian GLM variances). Fix after #65 settles self-checks.json. Other shared IDs: ex-prob-second-moment, ex-sp-right-continuous, ex-sp-spike, c-10.
- continuous-distribution History cites Kolmogorov only via Knill (optional).

## 19 Nov 2026, 7:40pm
- Citation rendering after #80: adjacent cites separated by ";" in research files render as "group.;[1] ;[2]" (Peer Review). Fix in build (collapse separators between adjacent cites) or strip in polish batches.
- SEO audit (SEO audit 19 Nov, not in repo): 16 questions share their article's title; fix the visible question titles in sources/ chapters during polish batches. Chapter/article overlap pairs: add "main article" links; SEO may run a full duplicate scan.
- SEO duplicates scan (SEO duplicates scan 19 Nov, not in repo): 3 sibling question pairs need distinct titles and openings (sources/ edits); hubs notes/applications and notes/final-applied need short intros; review article_extras summaries for article pairs at 55% or more when Grok Bot's PR lands.

## 20 Nov 2026, 9:00am
- #78 merged (new-001). The sign-test / wilcoxon-rank-sum-test / f-test-for-equal-variances / normal-quantile-plot prose links to the four new pages can now go into a polish batch.
- #91 (Check yourself prompts into depth-questions.json; ~340 files) overlaps #87 on count-models-beyond-the-poisson, count-responses, poisson-regression, and #89 on arima-model, hazard-rate. Editor call: merge #87 first; #91 rebases and keeps #87's prose. Batch-004 launches on main after #89 and #91 and must not touch self-checks.json / depth-questions.json (stale #65 reference in its precedence note 6).
