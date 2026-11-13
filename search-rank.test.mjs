import test from "node:test";
import assert from "node:assert/strict";
import {
  canonicalHref,
  documentsFromIndex,
  expandedTerms,
  rankDocuments,
  resolveExactMatch,
  scoreDocument,
  slugKey,
  tierOf,
} from "./search-rank.js";

const docs = [
  {
    href: "articles/summary-statistics.html",
    title: "Summary statistics",
    section: "",
    text: "The sample mean is the average of the observations.",
  },
  {
    href: "notes/da-02-descriptive-statistics.html#summary-statistics",
    title: "Descriptive statistics",
    section: "Summary statistics",
    text: "For the data, the sample mean is the average and the sample median is the middle value.",
  },
  {
    href: "notes/queues.html",
    title: "Queues",
    section: "Mean wait",
    text: "The mean waiting time grows with the arrival rate.",
  },
  {
    href: "files/prob-coin-averages.html",
    title: "Coin averages",
    section: "",
    text: "Each line is the mean proportion of heads.",
  },
  {
    href: "questions/q-07.html",
    title: "Normal estimation and prediction",
    section: "",
    text: "The posterior mean is not the sample mean unless the prior adds nothing.",
  },
];

function hrefs(query, meta = null) {
  return rankDocuments(docs, query, meta).map((doc) => doc.href);
}

test("figure files rank after articles and chapters", () => {
  for (const query of ["mean", "average", "sample mean"]) {
    const found = hrefs(query);
    const fileAt = found.findIndex((href) => href.startsWith("files/"));
    const articleAt = found.findIndex((href) => href.startsWith("articles/") || href.startsWith("notes/"));
    assert.ok(articleAt >= 0, query);
    if (fileAt >= 0) assert.ok(articleAt < fileAt, query + " " + found.join(" | "));
  }
});

test("mean, average, and sample mean find the same summary and surface the section anchor", () => {
  for (const query of ["mean", "average", "sample mean"]) {
    const ranked = rankDocuments(docs, query);
    const urls = ranked.map((doc) => doc.href);
    assert.ok(urls.includes("notes/da-02-descriptive-statistics.html"), query);
    assert.ok(urls.includes("articles/summary-statistics.html"), query);
    const chapterHit = ranked.find((doc) => doc.href === "notes/da-02-descriptive-statistics.html");
    assert.equal(chapterHit.section, "Summary statistics");
    assert.equal(chapterHit.sectionHref, "notes/da-02-descriptive-statistics.html#summary-statistics");
  }
  assert.deepEqual(expandedTerms("average"), ["mean", "average", "sample mean"]);
  assert.deepEqual(expandedTerms("sample mean"), ["mean", "average", "sample mean"]);
  assert.deepEqual(expandedTerms("mean"), ["mean", "average", "sample mean"]);
});

test("a lone word mean does not match meaning", () => {
  const only = [{ href: "notes/a.html", title: "Meaning", section: "", text: "The meaning of a model is not its mean." }];
  const found = rankDocuments(only, "mean").map((doc) => doc.href);
  assert.deepEqual(found, ["notes/a.html"]);
  const meaningOnly = [{ href: "notes/b.html", title: "Meaning", section: "", text: "The meaning of a model." }];
  assert.deepEqual(rankDocuments(meaningOnly, "mean"), []);
});

test("tiers put articles above notes above questions above files", () => {
  assert.equal(tierOf("articles/mean.html"), 0);
  assert.equal(tierOf("notes/da-02.html"), 1);
  assert.equal(tierOf("reference/glossary.html"), 1);
  assert.equal(tierOf("questions/q-01.html"), 2);
  assert.equal(tierOf("files/prob-coin-averages.html"), 3);
  assert.equal(tierOf("/files/prob-coin-averages.html"), 3);
  assert.equal(canonicalHref("notes/da-02.html#summary"), "notes/da-02.html");
  assert.equal(slugKey("Cramér–Rao lower bound"), "cramer-rao-lower-bound");
});

test("index payload may be a list or a docs object", () => {
  assert.equal(documentsFromIndex(docs).length, docs.length);
  assert.equal(documentsFromIndex({ docs }).length, docs.length);
  assert.equal(documentsFromIndex({ items: docs }).length, docs.length);
  assert.deepEqual(documentsFromIndex({}), []);
});

test("deduplicates Quarto section chunks so p-value returns each canonical page once", () => {
  const pValueChunks = [
    {
      href: "articles/p-value.html",
      title: "p-value",
      section: "",
      text: "The p-value of an observed statistic t is the probability under H0 that T is at least as extreme as t.",
    },
    {
      href: "articles/p-value.html#examples",
      title: "p-value",
      section: "Examples",
      text: "Worked examples computing a two-sided p-value.",
    },
    {
      href: "articles/p-value.html#example-exm-a-gene-in-lake-fish",
      title: "p-value",
      section: "A gene in lake fish",
      text: "The binomial p-value is 0.099.",
    },
    {
      href: "articles/p-value.html#used-in",
      title: "p-value",
      section: "Used in",
      text: "Taught in Hypothesis tests, where the p-value is introduced.",
    },
    {
      href: "articles/p-value.html#see-also",
      title: "p-value",
      section: "See also",
      text: "Significance level, critical region, power function, p-value.",
    },
    {
      href: "notes/inf-04-hypothesis-tests.html",
      title: "Hypothesis tests",
      section: "",
      text: "A test asks whether the data would be surprising under a stated hypothesis.",
    },
    {
      href: "notes/inf-04-hypothesis-tests.html#s-p-values",
      title: "Hypothesis tests",
      section: "P-values",
      text: "A small p-value is evidence against the null hypothesis.",
    },
    {
      href: "notes/inf-04-hypothesis-tests.html#what-links-here",
      title: "Hypothesis tests",
      section: "What links here",
      text: "Pages linking via p-value.",
    },
  ];

  for (const query of ["p-value", "p value", "pvalue"]) {
    const ranked = rankDocuments(pValueChunks, query);
    assert.equal(ranked.length, 2, query);
    assert.equal(ranked[0].href, "articles/p-value.html", query);
    assert.equal(ranked[0].section, "", "exact page hit keeps clean lead without boilerplate section");
    assert.equal(ranked[1].href, "notes/inf-04-hypothesis-tests.html", query);
    assert.equal(ranked[1].section, "P-values");
    assert.equal(ranked[1].sectionHref, "notes/inf-04-hypothesis-tests.html#s-p-values");
  }
});

test("exact canonical title ranks #1 for variance ahead of 40 compound variance articles", () => {
  const compoundTitles = [
    "Analysis of variance",
    "ANOVA sum of squares decomposition",
    "Asymptotic variance",
    "Bias–variance trade-off",
    "Chi-squared test for a variance",
    "Conditional variance",
    "Constant variance",
    "Error variance",
    "Explained variance",
    "F test for equal variances",
    "Homogeneity of variance",
    "Interval for a normal variance",
    "Interval for a ratio of variances",
    "Law of total variance",
    "Marginal variance posterior",
    "Mean and variance of an exponential family",
    "Minimum-variance unbiased estimator",
    "Moments of the sample mean and variance",
    "Normal variance with known mean",
    "Normal–inverse-Gamma variance update",
    "One-way analysis of variance",
    "Pooled variance",
    "Posterior variance",
    "Predictive variance decomposition",
    "Residual variance",
    "Sample variance and standard deviation",
    "Sandwich variance",
    "Total variance",
    "Two-factor analysis of variance",
    "Two-sample variance ratio",
    "Unbiased variance estimator",
    "Uniformly minimum-variance unbiased estimator",
    "Unit variance",
    "Variance argument for weight initialisation",
    "Variance components",
    "Variance function",
    "Variance inflation",
    "Variance stabilising transformation",
    "Variance-ratio F pivot",
    "Within-cluster variance",
  ];

  const corpus = compoundTitles.flatMap((title, idx) => {
    const slug = slugKey(title);
    return [
      {
        href: `articles/${slug}.html`,
        title,
        section: title,
        text: `This page studies ${title.toLowerCase()} and compares the variance across samples (${idx}).`,
      },
      {
        href: `articles/${slug}.html#examples`,
        title,
        section: "Variance calculation",
        text: "The variance is computed from the sum of squares.",
      },
    ];
  });

  // Insert the canonical Variance article near the end, with no section repetition.
  corpus.push({
    href: "articles/variance.html",
    title: "Variance",
    section: "",
    text: "The variance of X is E(X - EX)^2, when that expectation exists.",
  });

  const ranked = rankDocuments(corpus, "variance");
  assert.equal(ranked[0].href, "articles/variance.html");
  assert.equal(ranked.length, compoundTitles.length + 1);
  // Shorter 2-word variance titles outrank 7-word compound titles.
  const pooledAt = ranked.findIndex((d) => d.href === "articles/pooled-variance.html");
  const momentsAt = ranked.findIndex((d) => d.href === "articles/moments-of-the-sample-mean-and-variance.html");
  assert.ok(pooledAt < momentsAt, `${pooledAt} should come before ${momentsAt}`);
});

test("registered aliases rank canonical concept pages #1 above high-frequency body mentions", () => {
  const aliasCorpus = [
    {
      href: "notes/heavy-chapter.html",
      title: "Applied modelling examples",
      section: "Fitting",
      text: "We compare ANOVA, OLS, MLE, CLT, GLM, MCMC, PCA, and the normal mean across twenty datasets.",
    },
    {
      href: "notes/heavy-chapter.html#more",
      title: "Applied modelling examples",
      section: "Diagnostics",
      text: "ANOVA, OLS, MLE, CLT, GLM, MCMC, PCA, and normal residuals again.",
    },
    {
      href: "articles/tangential-pca.html",
      title: "Principal components of the colon-cancer matrix",
      section: "",
      text: "PCA reduces the gene matrix to leading scores.",
    },
    {
      href: "articles/expectation.html",
      title: "Expectation",
      section: "",
      text: "If X is discrete with mass function f, its expectation is sum x f(x).",
    },
    {
      href: "articles/summary-statistics.html",
      title: "Summary statistics",
      section: "",
      text: "The sample mean is the average of the observations.",
    },
    {
      href: "articles/one-way-analysis-of-variance.html",
      title: "One-way analysis of variance",
      section: "",
      text: "In a completely randomised one-factor design, responses follow Y_ij = mu_j + eps_ij.",
    },
    {
      href: "articles/normal-distribution.html",
      title: "Normal distribution",
      section: "",
      text: "X has density proportional to exp(-(x - mu)^2 / (2 sigma^2)).",
    },
    {
      href: "articles/ordinary-least-squares.html",
      title: "Ordinary least squares",
      section: "",
      text: "Assume rank(X) = p. Minimises the residual sum of squares.",
    },
    {
      href: "articles/maximum-likelihood.html",
      title: "Maximum likelihood",
      section: "",
      text: "Maximises the likelihood function over the parameter space.",
    },
    {
      href: "articles/central-limit-theorem.html",
      title: "Central limit theorem",
      section: "",
      text: "Standardised sums of i.i.d. finite-variance variables converge to standard normal.",
    },
    {
      href: "articles/generalised-linear-model.html",
      title: "Generalised linear model",
      section: "",
      text: "Exponential-family response, linear predictor, and link function.",
    },
    {
      href: "articles/markov-chain.html",
      title: "Markov chain",
      section: "",
      text: "Future state depends on the past only through the present state.",
    },
    {
      href: "notes/sl-03-principal-components.html",
      title: "Principal component analysis",
      section: "",
      text: "Orthogonal directions of maximal sample variance.",
    },
  ];

  const meta = {
    pages: {
      "articles/expectation.html": { title: "Expectation", aliases: ["Mean", "Expected value"] },
      "articles/summary-statistics.html": { title: "Summary statistics", aliases: ["Sample mean", "Average"] },
      "articles/one-way-analysis-of-variance.html": { title: "One-way analysis of variance", aliases: ["ANOVA"] },
      "articles/normal-distribution.html": { title: "Normal distribution", aliases: ["Normal", "Gaussian"] },
      "articles/ordinary-least-squares.html": { title: "Ordinary least squares", aliases: ["OLS"] },
      "articles/maximum-likelihood.html": { title: "Maximum likelihood", aliases: ["MLE"] },
      "articles/central-limit-theorem.html": { title: "Central limit theorem", aliases: ["CLT"] },
      "articles/generalised-linear-model.html": { title: "Generalised linear model", aliases: ["GLM"] },
      "articles/markov-chain.html": { title: "Markov chain", aliases: ["MCMC"] },
      "notes/sl-03-principal-components.html": { title: "Principal component analysis", aliases: ["PCA"] },
    },
    aliases: {
      mean: "articles/expectation.html",
      "sample-mean": "articles/summary-statistics.html",
      anova: "articles/one-way-analysis-of-variance.html",
      normal: "articles/normal-distribution.html",
      gaussian: "articles/normal-distribution.html",
      ols: "articles/ordinary-least-squares.html",
      mle: "articles/maximum-likelihood.html",
      clt: "articles/central-limit-theorem.html",
      glm: "articles/generalised-linear-model.html",
      mcmc: "articles/markov-chain.html",
      pca: "notes/sl-03-principal-components.html",
    },
  };

  const expectedTop = [
    ["mean", "articles/expectation.html"],
    ["sample mean", "articles/summary-statistics.html"],
    ["anova", "articles/one-way-analysis-of-variance.html"],
    ["normal", "articles/normal-distribution.html"],
    ["gaussian", "articles/normal-distribution.html"],
    ["ols", "articles/ordinary-least-squares.html"],
    ["mle", "articles/maximum-likelihood.html"],
    ["clt", "articles/central-limit-theorem.html"],
    ["glm", "articles/generalised-linear-model.html"],
    ["mcmc", "articles/markov-chain.html"],
    ["pca", "notes/sl-03-principal-components.html"],
  ];

  for (const [query, target] of expectedTop) {
    const ranked = rankDocuments(aliasCorpus, query, meta);
    assert.ok(ranked.length >= 1, query);
    assert.equal(ranked[0].href, target, `query "${query}" should rank ${target} #1, got ${ranked[0].href}`);

    const exact = resolveExactMatch(query, meta, aliasCorpus);
    assert.ok(exact, `resolveExactMatch("${query}") should resolve`);
    assert.equal(exact.href, target, `resolveExactMatch("${query}")`);
  }

  // Exact canonical titles also resolve directly via resolveExactMatch.
  assert.equal(resolveExactMatch("Central limit theorem", meta, aliasCorpus)?.href, "articles/central-limit-theorem.html");
  assert.equal(resolveExactMatch("the central limit theorem", meta, aliasCorpus)?.href, "articles/central-limit-theorem.html");
  assert.equal(resolveExactMatch("nonexistent gibberish query", meta, aliasCorpus), null);
  assert.ok(scoreDocument(aliasCorpus[5], "anova", meta) > scoreDocument(aliasCorpus[0], "anova", meta));
});

test("generated search-aliases.json resolves core statistical queries when built", async (t) => {
  const fs = await import("node:fs");
  const path = new URL("./search-aliases.json", import.meta.url);
  if (!fs.existsSync(path)) {
    t.skip("search-aliases.json is generated by build_wiki.py");
    return;
  }
  const meta = JSON.parse(fs.readFileSync(path, "utf8"));
  const checks = [
    ["variance", "articles/variance.html"],
    ["p-value", "articles/p-value.html"],
    ["mean", "articles/expectation.html"],
    ["sample mean", "articles/summary-statistics.html"],
    ["anova", "articles/one-way-analysis-of-variance.html"],
    ["normal", "articles/normal-distribution.html"],
    ["ols", "articles/ordinary-least-squares.html"],
    ["mle", "articles/maximum-likelihood.html"],
    ["clt", "articles/central-limit-theorem.html"],
    ["glm", "articles/generalised-linear-model.html"],
    ["mcmc", "articles/markov-chain.html"],
    ["pca", "notes/sl-03-principal-components.html"],
  ];
  for (const [q, expected] of checks) {
    const exact = resolveExactMatch(q, meta);
    assert.ok(exact, `resolveExactMatch("${q}")`);
    assert.equal(exact.href, expected, `exact match for "${q}"`);
    const ranked = rankDocuments([], q, meta);
    assert.equal(ranked[0]?.href, expected, `rankDocuments #1 for "${q}"`);
  }
});

