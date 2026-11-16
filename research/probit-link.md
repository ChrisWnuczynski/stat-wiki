# Probit link

Rank 201. Type: Concept/link. Frozen baseline: 470 body words and zero figures. The original link definition, coefficient-scale comparison, logistic slope-matching derivation, heavier-tail comparison, infobox and three linked questions remain represented.

## Checked

- **Checked in full repository source chapters:** `sources/book/chapters/01-introduction-to-glms.qmd`, §“Three links”, and `sources/stat3006/chapters/sl-10-logistic-regression.qmd`, §“Logistic and probit”. Both give the normal-CDF inverse link and central slope comparison. `questions/q-38.qmd` and `questions/c-20.qmd` give answered cross-checks.
- **Checked by proof:** One collapsed box derives the latent-normal threshold representation, normal symmetry, probability derivative, half-probability point and central logit/probit slope-matching constant.
- **Checked by code:** `checks/probit-link.py` evaluates each printed normal probability, derivative, constant and practice answer.
- **Assumed:** Bernoulli response conditional on stated covariates; standard-normal variance fixed to one in the latent-threshold interpretation; the worked doses are illustrative.
- **Disputed:** A fixed 1.6–1.8 coefficient factor is only heuristic across comparable fitted models. The source chapter's claim that fitted links almost always agree is too broad. The shared topic and GLM chapter now qualify the central slope comparison and note that fitted tail behavior and calibration can matter.

## Sources used

- Both complete repository sections and their worked reasoning were read. Unlocated inherited Bliss, Berkson and McCullagh–Nelder citations in the relevant source paragraph were removed during the citation audit. The slope factor is checked algebraically; no citation to an unopened original was added.
- The authorized Dodge full text and index were searched for “probit”, “Bliss”, “Finney” and “bioassay”; no relevant entry was found, so there is no Dodge citation or added history claim.

## Changes

Added a concrete dose-response motivation, latent-normal interpretation, differential effect, proof, checked example and hidden practice answer, three answered self-checks pending, distinct misconceptions, failure cases and connections. No figures changed.
