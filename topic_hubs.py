"""Curated topic hubs for the homepage library, the topic index, and the sidebar.

Fundamentals is the on-ramp. Probability distributions collects every
distribution article. Standalone fundamentals are articles whose whole text
lives in research/content; they are not copied out of a chapter.
"""

from __future__ import annotations

# Learning order. Existing articles are included; only STANDALONE slugs are new pages.
FUNDAMENTALS_ORDER: list[str] = [
    "data",
    "dataset",
    "variable",
    "levels-of-measurement",
    "population",
    "census",
    "sample",
    "simple-random-sample",
    "designed-experiment",
    "observational-study",
    "summary-statistics",
    "statistic",
    "parameter",
    "estimator",
    "sample-space",
    "event",
    "axioms-of-probability",
    "random-variable",
    "expectation",
    "variance",
    "random-sample",
    "ingredients-of-a-hypothesis-test",
    "confidence-interval",
]

FUNDAMENTALS_GROUPS: list[tuple[str, list[str]]] = [
    ("What is recorded", ["data", "dataset", "variable", "levels-of-measurement"]),
    ("Where the records come from", ["population", "census", "sample", "simple-random-sample", "designed-experiment", "observational-study"]),
    ("Description and a first inference", ["summary-statistics", "statistic", "parameter", "estimator", "ingredients-of-a-hypothesis-test", "confidence-interval"]),
    ("The probability language underneath", ["sample-space", "event", "axioms-of-probability", "random-variable", "expectation", "variance", "random-sample"]),
]

FUNDAMENTALS_INTRO = """
Statistics begins with a record and a question about a larger collection than the record itself. The pages in this topic follow that order. They start from what a measurement is, then from how a collection of measurements is chosen, then from the summaries and the models that turn those measurements into a claim, and only then from the probability that makes the claim precise.

A reader who is new to the subject can follow the groups from top to bottom. Each later page uses the words of the earlier ones. The same pages also sit in the chapters that develop them further: a definition here is the start of an argument, not the whole argument.
""".strip()

DISTRIBUTIONS_INTRO = """
A probability distribution is a rule that assigns chances to the values of a random variable. The cards below are the named families used on this site, grouped by the kind of value they describe. Discrete families put their chance on a list of points. Continuous families spread chance along an interval. Multivariate families describe several values at once. The last group collects the relationships that turn one family into another.

Each card links to the article. The articles keep their place in the chapter that derives them. Their primary listing is this topic. A laboratory draws the mass or density and the distribution function for the univariate families whose formulas are short enough to compute in the browser.
""".strip()

# Distribution articles that are not rows of distributions.json.
DISTRIBUTION_CONCEPTS: list[str] = [
    "discrete-distribution",
    "continuous-distribution",
    "conditional-distribution",
]

# Related pages listed with the families, without taking the distribution breadcrumb.
DISTRIBUTION_RELATIONS: list[str] = [
    "exponential-family",
    "natural-exponential-family",
    "poisson-limit-of-the-binomial",
    "memoryless-property",
    "the-beta-distribution-is-the-two-category-dirichlet",
    "central-limit-theorem",
]

MULTIVARIATE: set[str] = {
    "dirichlet-distribution",
    "multinomial-distribution",
    "multivariate-normal-distribution",
    "wishart-distribution",
}

# Univariate families the distribution laboratory can draw.
EXPLORER_SLUGS: list[str] = [
    "bernoulli-distribution",
    "binomial-distribution",
    "poisson-distribution",
    "geometric-distribution",
    "uniform-distribution",
    "exponential-distribution",
    "normal-distribution",
    "gamma-distribution",
    "beta-distribution",
    "chi-squared-distribution",
    "student-t-distribution",
    "cauchy-distribution",
    "lognormal-distribution",
    "pareto-distribution",
    "weibull-distribution",
    "f-distribution",
]

STANDALONE: list[dict[str, str]] = [
    {"slug": "data", "term": "Data", "field": "statistics", "article": "", "verb": "are", "description": "measurements or observations collected as a source of information"},
    {"slug": "dataset", "term": "Dataset", "field": "statistics", "article": "a", "verb": "is", "description": "a collection of observations organised so that they can be analysed together"},
    {"slug": "variable", "term": "Variable", "field": "statistics", "article": "a", "verb": "is", "description": "a characteristic that is measured or counted on each unit"},
    {"slug": "levels-of-measurement", "term": "Levels of measurement", "field": "statistics", "article": "", "verb": "are", "description": "the distinctions among names, ranks, and numerical measurements that decide which summaries are meaningful"},
    {"slug": "population", "term": "Population", "field": "statistics", "article": "a", "verb": "is", "description": "the complete collection of units about which a study wants to learn"},
    {"slug": "census", "term": "Census", "field": "statistics", "article": "a", "verb": "is", "description": "a study that observes every unit in a population"},
    {"slug": "sample", "term": "Sample", "field": "statistics", "article": "a", "verb": "is", "description": "a subset of a population, studied in order to say something about the population"},
    {"slug": "parameter", "term": "Parameter", "field": "statistics", "article": "a", "verb": "is", "description": "a numerical feature of a population, as distinct from a statistic computed from a sample"},
]


def standalone_slugs() -> set[str]:
    return {row["slug"] for row in STANDALONE}


def distribution_page_slugs(distribution_keys: list[str]) -> list[str]:
    """Every distribution article, in catalogue order, then the concept pages."""
    return list(distribution_keys) + [slug for slug in DISTRIBUTION_CONCEPTS if slug not in distribution_keys]


def is_distribution_page(slug: str, distribution_keys) -> bool:
    return slug in set(distribution_keys) or slug in DISTRIBUTION_CONCEPTS


def distribution_groups(distribution_items: list[tuple[str, dict]]) -> list[tuple[str, list[str]]]:
    discrete, continuous, multivariate = [], [], []
    for slug, facts in distribution_items:
        if slug in MULTIVARIATE:
            multivariate.append(slug)
        elif facts.get("kind") == "discrete":
            discrete.append(slug)
        else:
            continuous.append(slug)
    return [
        ("Discrete distributions", discrete),
        ("Continuous distributions", continuous),
        ("Multivariate distributions", multivariate),
        ("What a distribution is", list(DISTRIBUTION_CONCEPTS)),
        ("Families and relationships", list(DISTRIBUTION_RELATIONS)),
    ]
