import test from "node:test";
import assert from "node:assert/strict";
import { documentsFromIndex, expandedTerms, rankDocuments, tierOf } from "./search-rank.js";

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

function hrefs(query) {
  return rankDocuments(docs, query).map((doc) => doc.href);
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

test("mean, average, and sample mean find the same summary", () => {
  const summary = "notes/da-02-descriptive-statistics.html#summary-statistics";
  for (const query of ["mean", "average", "sample mean"]) {
    assert.ok(hrefs(query).includes(summary), query);
    assert.ok(hrefs(query).includes("articles/summary-statistics.html"), query);
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
});

test("index payload may be a list or a docs object", () => {
  assert.equal(documentsFromIndex(docs).length, docs.length);
  assert.equal(documentsFromIndex({ docs }).length, docs.length);
  assert.deepEqual(documentsFromIndex({}), []);
});
