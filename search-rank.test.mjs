import test from "node:test";
import assert from "node:assert/strict";
import {
  augmentQuartoSearchItems,
  canonicalHref,
  canonicalSearchKey,
  documentsFromIndex,
  expandedTerms,
  parseQuery,
  rankDocuments,
  resolveComparison,
  resolveDisambiguation,
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
    ["p value", "articles/p-value.html"],
    ["sample mean", "articles/summary-statistics.html"],
    ["anova", "articles/one-way-analysis-of-variance.html"],
    ["normal", "articles/normal-distribution.html"],
    ["ols", "articles/ordinary-least-squares.html"],
    ["mle", "articles/maximum-likelihood.html"],
    ["clt", "articles/central-limit-theorem.html"],
    ["glm", "articles/generalised-linear-model.html"],
    ["mcmc", "articles/markov-chain.html"],
    ["pca", "notes/sl-03-principal-components.html"],
    ["sd", "articles/sample-variance-and-standard-deviation.html"],
    ["se", "articles/standard-error.html"],
    ["ci", "articles/confidence-interval.html"],
    ["pi", "articles/prediction-interval.html"],
    ["cv", "articles/cross-validation.html"],
    ["df", "articles/degrees-of-freedom.html"],
    ["rv", "articles/random-variable.html"],
    ["iid", "articles/random-sample.html"],
    ["i.i.d.", "articles/random-sample.html"],
    ["bf", "articles/marginal-likelihood-and-bayes-factor.html"],
    ["kl", "articles/kullback-leibler-divergence.html"],
    ["em", "articles/em-algorithm.html"],
    ["ar", "articles/autoregression-and-moving-averages.html"],
    ["ma", "articles/autoregression-and-moving-averages.html"],
    ["rss", "articles/ordinary-least-squares.html"],
    ["ess", "articles/anova-sum-of-squares-decomposition.html"],
    ["tss", "articles/anova-sum-of-squares-decomposition.html"],
    ["t", "articles/student-t-distribution.html"],
    ["z", "articles/normal-distribution.html"],
    ["f", "articles/f-distribution.html"],
    ["p", "articles/p-value.html"],
    ["r", "articles/sample-correlation-coefficient.html"],
    ["t test", "articles/one-sample-t-test.html"],
    ["t-test", "articles/one-sample-t-test.html"],
    ["z test", "articles/two-proportion-z-test.html"],
    ["f test", "articles/f-test-for-equal-variances.html"],
    ["chi2", "articles/chi-squared-distribution.html"],
    ["r2", "articles/coefficient-of-determination.html"],
    ["k means", "notes/sl-04-kmeans.html"],
    ["k fold", "articles/fold-cross-validation.html"],
    ["qq", "articles/normal-quantile-plot.html"],
    ["log likelihood", "articles/likelihood-function.html"],
    ["Bayes theorem", "articles/bayes-rule.html"],
    ["Bayes' theorem", "articles/bayes-rule.html"],
    ["Bayes’ theorem", "articles/bayes-rule.html"],
    ["Students t", "articles/student-t-distribution.html"],
    ["Student's t", "articles/student-t-distribution.html"],
    ["Fishers exact test", "articles/fisher-s-exact-test.html"],
    ["Jensens inequality", "articles/jensen-s-inequality.html"],
    ["Chebyshevs inequality", "articles/chebyshev-s-inequality.html"],
    ["Markovs inequality", "articles/markov-s-inequality.html"],
    ["Wilks theorem", "articles/wilks-theorem.html"],
    ["Wilks' theorem", "articles/wilks-theorem.html"],
    ["Hotellings T2", "articles/hotelling-s-t2-test.html"],
    ["Simpsons paradox", "articles/confounding-variable.html"],
    ["Slutskys", "articles/asymptotic-normality-of-maximum-likelihood.html"],
    ["Tukeys", "articles/tukey-intervals.html"],
    ["Stirlings", "articles/k-means-criterion.html"],
    ["Cramér", "articles/cramer-rao-lower-bound.html"],
    ["Cramers", "articles/cramer-rao-lower-bound.html"],
    ["Hölder", "notes/sp-11-convergence.html#s-inequalities-and-passing-a-limit-inside-the-expectation"],
    ["Holder", "notes/sp-11-convergence.html#s-inequalities-and-passing-a-limit-inside-the-expectation"],
    ["Itô", "articles/stochastic-process.html"],
    ["Ito", "articles/stochastic-process.html"],
    ["Lévy", "articles/levy-s-continuity-theorem.html"],
    ["Levy", "articles/levy-s-continuity-theorem.html"],
    ["Rényi", "articles/kullback-leibler-divergence.html"],
    ["Renyi", "articles/kullback-leibler-divergence.html"],
    ["Fréchet", "articles/power-law-tails-and-the-frechet-law.html"],
    ["Frechet", "articles/power-law-tails-and-the-frechet-law.html"],
  ];
  for (const [q, expected] of checks) {
    const exact = resolveExactMatch(q, meta);
    assert.ok(exact, `resolveExactMatch("${q}")`);
    assert.equal(exact.href, expected, `exact match for "${q}"`);
    const ranked = rankDocuments([], q, meta);
    assert.equal(ranked[0]?.href, expected.split("#")[0], `rankDocuments #1 for "${q}"`);
  }

  // Disambiguated queries surface all intended targets at the top.
  const meanDis = resolveDisambiguation("mean", meta);
  assert.ok(meanDis, "mean should have disambiguation options");
  const meanHrefs = meanDis.options.map((o) => o.href);
  assert.ok(meanHrefs.includes("articles/summary-statistics.html"));
  assert.ok(meanHrefs.includes("articles/expectation.html"));
  assert.ok(meanHrefs.includes("articles/posterior-mean.html"));

  const kernelDis = resolveDisambiguation("kernel", meta);
  assert.ok(kernelDis, "kernel should have disambiguation options");
  const kernelHrefs = kernelDis.options.map((o) => o.href);
  assert.ok(kernelHrefs.includes("articles/kernel-density-estimator.html"));
  assert.ok(kernelHrefs.includes("articles/kernel.html"));
  assert.ok(kernelHrefs.includes("articles/kernel-of-a-density.html"));
  assert.ok(kernelHrefs.includes("articles/markov-chain.html"));

  const tTestDis = resolveDisambiguation("t test", meta);
  assert.ok(tTestDis, "t test should have disambiguation options");
  const tTestHrefs = tTestDis.options.map((o) => o.href);
  assert.ok(tTestHrefs.includes("articles/one-sample-t-test.html"));
  assert.ok(tTestHrefs.includes("articles/two-sample-t-test.html"));
  assert.ok(tTestHrefs.includes("articles/welch-interval.html"));
  assert.ok(tTestHrefs.includes("articles/paired-samples.html"));

  // Conversational & comparison queries against full generated metadata.
  assert.equal(rankDocuments([], "what is a p value?", meta)[0]?.href, "articles/p-value.html");
  assert.equal(rankDocuments([], "how to compute sample variance", meta)[0]?.href, "articles/sample-variance-and-standard-deviation.html");
  const compTop = rankDocuments([], "mean vs median", meta).slice(0, 2).map((d) => d.href);
  assert.deepEqual(compTop, ["articles/expectation.html", "articles/median.html"]);
});

test("canonicalSearchKey folds diacritics, strips possessives, and normalises punctuation", () => {
  assert.equal(canonicalSearchKey("Cramér–Rao lower bound"), "cramer-rao-lower-bound");
  assert.equal(canonicalSearchKey("Hölder's inequality"), "holder-inequality");
  assert.equal(canonicalSearchKey("Itô"), "ito");
  assert.equal(canonicalSearchKey("Lévy's continuity theorem"), "levy-continuity-theorem");
  assert.equal(canonicalSearchKey("Rényi"), "renyi");
  assert.equal(canonicalSearchKey("Fréchet"), "frechet");
  assert.equal(canonicalSearchKey("Bayes' theorem"), "bayes-theorem");
  assert.equal(canonicalSearchKey("Bayes’ theorem"), "bayes-theorem");
  assert.equal(canonicalSearchKey("Student's t-test"), "student-t-test");
  assert.equal(canonicalSearchKey("Students t test"), "student-t-test");
  assert.equal(canonicalSearchKey("Wilks' theorem"), "wilk-theorem");
  assert.equal(canonicalSearchKey("Wilks theorem"), "wilk-theorem");
  assert.equal(canonicalSearchKey("i.i.d."), "iid");
  assert.equal(canonicalSearchKey("s.d."), "sd");
});

test("conversational questions, comparisons, and live Quarto augmentation synthesize canonical hits", () => {
  const miniMeta = {
    pages: {
      "articles/p-value.html": {
        title: "p-value",
        kind: "article",
        summary: "Probability under H0 of a test statistic at least as extreme as observed.",
        aliases: ["p value", "pvalue"],
      },
      "articles/sample-variance-and-standard-deviation.html": {
        title: "Sample variance and standard deviation",
        kind: "article",
        summary: "Sample dispersion s^2 and sample standard deviation s.",
        aliases: ["sd", "Standard deviation", "sample variance"],
      },
      "articles/variance.html": {
        title: "Variance",
        kind: "article",
        summary: "Population variance E[(X - EX)^2].",
        aliases: ["var"],
      },
      "articles/expectation.html": {
        title: "Expectation",
        kind: "article",
        summary: "Population mean E[X].",
        aliases: ["Mean", "Expected value"],
      },
      "articles/median.html": {
        title: "Median",
        kind: "article",
        summary: "Middle quantile of a sample or distribution.",
        aliases: ["sample median"],
      },
    },
    aliases: {
      "p-value": "articles/p-value.html",
      sd: "articles/sample-variance-and-standard-deviation.html",
      mean: "articles/expectation.html",
    },
    disambiguations: {
      variance: {
        term: "Variance",
        aliases: ["var"],
        options: [
          { href: "articles/variance.html", label: "Variance (random variable)", description: "Population variance" },
          { href: "articles/sample-variance-and-standard-deviation.html", label: "Sample variance", description: "Data variance s^2" },
        ],
      },
    },
  };

  assert.equal(parseQuery("what is a p value?").core, "p value");
  assert.equal(parseQuery("how do I compute the sample variance?").core, "sample variance");
  assert.deepEqual(parseQuery("difference between mean and median").comparison, ["mean", "median"]);
  assert.deepEqual(parseQuery("mean vs median").comparison, ["mean", "median"]);

  // Even when Fuse returns 0 items ([]), augmentQuartoSearchItems synthesizes canonical hits!
  const sdItems = augmentQuartoSearchItems([], "sd", miniMeta, []);
  assert.ok(sdItems.length >= 1);
  assert.equal(sdItems[0].href, "articles/sample-variance-and-standard-deviation.html");

  const pvalItems = augmentQuartoSearchItems([], "what is a p value?", miniMeta, []);
  assert.ok(pvalItems.length >= 1);
  assert.equal(pvalItems[0].href, "articles/p-value.html");

  const comp = resolveComparison("mean vs median", miniMeta, []);
  assert.ok(comp);
  assert.equal(comp.targets.length, 2);
  const compItems = augmentQuartoSearchItems([], "mean vs median", miniMeta, []);
  assert.deepEqual(
    compItems.slice(0, 2).map((i) => i.href),
    ["articles/expectation.html", "articles/median.html"]
  );

  const varItems = augmentQuartoSearchItems([], "how to compute variance", miniMeta, []);
  assert.deepEqual(
    varItems.slice(0, 2).map((i) => i.href),
    ["articles/variance.html", "articles/sample-variance-and-standard-deviation.html"]
  );
});

