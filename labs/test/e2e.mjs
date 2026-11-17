// Browser test for the three laboratories. No Quarto and no network.
// Serves labs/ the way a static host would, then drives the controls.
//
//   cd labs && npm install && node test/e2e.mjs
// Behind a proxy, HTTPS_PROXY is passed to Chromium.

import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import { createServer } from "node:http";
import { createRequire } from "node:module";
import { dirname, extname, join, normalize } from "node:path";
import { fileURLToPath } from "node:url";

const require = createRequire(import.meta.url);
const { chromium } = require("playwright");
const root = join(dirname(fileURLToPath(import.meta.url)), "..", "..");
const TYPES = { ".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8" };

const server = createServer(async (request, response) => {
  const path = normalize(decodeURIComponent(new URL(request.url, "http://x").pathname)).replace(/^([/\\])+/, "");
  const file = join(root, path);
  if (!file.startsWith(join(root, "labs"))) {
    response.writeHead(404);
    response.end();
    return;
  }
  try {
    const body = await readFile(file);
    response.writeHead(200, { "content-type": TYPES[extname(file)] ?? "application/octet-stream" });
    response.end(body);
  } catch {
    response.writeHead(404);
    response.end();
  }
});
await new Promise((resolve) => server.listen(0, "127.0.0.1", resolve));
const base = `http://127.0.0.1:${server.address().port}/`;
const proxy = process.env.HTTPS_PROXY || process.env.https_proxy;
const browser = await chromium.launch(proxy ? { proxy: { server: proxy, bypass: "127.0.0.1,localhost" } } : {});
const page = await browser.newPage({ viewport: { width: 1100, height: 900 } });
const problems = [];
page.on("pageerror", (error) => problems.push(String(error)));
page.on("console", (message) => {
  if (message.type() === "error") problems.push(message.text());
});
const step = (name) => console.log("-", name);

function parseTick(text) {
  return Number(String(text).replaceAll("−", "-"));
}

function assertSpread(charts) {
  assert.equal(charts.length, 2);
  for (const chart of charts) {
    assert.ok(chart.width > 200 && chart.height > 200, chart.label);
    const ySpan = Math.max(...chart.yLabels.map((item) => item.y)) - Math.min(...chart.yLabels.map((item) => item.y));
    const xSpan = Math.max(...chart.xLabels.map((item) => item.x)) - Math.min(...chart.xLabels.map((item) => item.x));
    assert.ok(ySpan > chart.height * 0.45, `${chart.label} y labels span ${ySpan}`);
    assert.ok(xSpan > chart.width * 0.45, `${chart.label} x labels span ${xSpan}`);
    const xSorted = [...chart.xLabels].sort((a, b) => parseTick(a.text) - parseTick(b.text));
    for (let i = 1; i < xSorted.length; i += 1) {
      assert.ok(xSorted[i].x > xSorted[i - 1].x + 8, `${chart.label} x order ${xSorted.map((item) => item.text).join(" ")}`);
    }
    const ySorted = [...chart.yLabels].sort((a, b) => parseTick(a.text) - parseTick(b.text));
    for (let i = 1; i < ySorted.length; i += 1) {
      assert.ok(ySorted[i].y < ySorted[i - 1].y - 8, `${chart.label} y order ${ySorted.map((item) => item.text).join(" ")}`);
    }
    const xGaps = xSorted.slice(1).map((item, index) => item.x - xSorted[index].x);
    assert.ok(Math.max(...xGaps) - Math.min(...xGaps) < 1.5, `${chart.label} x gaps`);
    if (chart.points.length) {
      assert.ok(chart.points.every((point) => point.every(Number.isFinite)), chart.label);
      const px = chart.points.map((point) => point[0]);
      const py = chart.points.map((point) => point[1]);
      assert.ok(Math.max(...px) - Math.min(...px) > chart.width * 0.45, `${chart.label} path x`);
      assert.ok(Math.max(...py) - Math.min(...py) > chart.height * 0.15, `${chart.label} path y`);
    } else {
      assert.ok(chart.circles.length >= 2, chart.label);
      assert.ok(chart.circles.every((point) => Number.isFinite(point.x) && Number.isFinite(point.y)), chart.label);
      const cx = chart.circles.map((point) => point.x);
      assert.ok(Math.max(...cx) - Math.min(...cx) > chart.width * 0.25, chart.label);
    }
  }
}

function distributionCharts() {
  return page.evaluate(() => [...document.querySelectorAll("#distribution svg")].map((svg) => {
    const parts = (svg.getAttribute("viewBox") || "").split(/[\s,]+/).map(Number);
    const texts = [...svg.querySelectorAll("text")].map((node) => ({
      text: node.textContent,
      x: Number(node.getAttribute("x")),
      y: Number(node.getAttribute("y")),
      anchor: node.getAttribute("text-anchor"),
    }));
    const poly = svg.querySelector("polyline");
    return {
      label: svg.getAttribute("aria-label"),
      width: parts[2],
      height: parts[3],
      yLabels: texts.filter((item) => item.anchor === "end"),
      xLabels: texts.filter((item) => item.anchor === "middle"),
      points: poly ? poly.getAttribute("points").trim().split(/\s+/).map((pair) => pair.split(",").map(Number)) : [],
      circles: [...svg.querySelectorAll("circle")].map((node) => ({
        x: Number(node.getAttribute("cx")),
        y: Number(node.getAttribute("cy")),
      })),
    };
  }));
}

// Chart titles repeat the status text inside <title>. Match the paragraph a reader sees.
function shown(text, options) {
  return page.locator("p.control-note, p.graph-note, .readout-line").getByText(text, options);
}

function spin(name) {
  return page.getByRole("spinbutton", { name, exact: true });
}

try {
  await page.goto(base + "labs/test/page.html");
  await page.getByRole("button", { name: "Beta(5, 5)" }).waitFor();
  step("default Beta(5, 5) with 3 heads in 10 tosses is Beta(8, 12) with mean 0.4");
  await shown("Beta(8, 12)", { exact: true }).waitFor();
  assert.match(await page.locator("#beta .readout-line").textContent(), /0\.4/);
  assert.equal(problems.length, 0, problems.join("\n"));

  step("uniform prior");
  await page.getByRole("button", { name: "Beta(1, 1)" }).click();
  await shown("Beta(4, 8)", { exact: true }).waitFor();
  assert.match(await page.locator("#beta .readout-line").textContent(), /0\.3333/);

  step("no tosses leaves the posterior equal to the prior");
  await page.locator("#beta").getByRole("button", { name: "Reset" }).click();
  await spin("Tosses n as a number").fill("0");
  await shown("No tosses yet").waitFor();
  assert.match(await page.locator("#beta .readout-line").textContent(), /Beta\(5, 5\)/);
  assert.equal(await page.locator("#beta svg polyline").count() > 0, true);

  step("a shape that is not a number draws nothing");
  await page.locator("#beta").getByRole("button", { name: "Reset" }).click();
  await spin("Prior heads α as a number").fill("");
  await shown("α must be a number").waitFor();
  assert.match(await page.locator("#beta svg").first().textContent(), /Not drawn/);

  step("an unbounded prior is clipped rather than scaled to infinity");
  await page.locator("#beta").getByRole("button", { name: "Reset" }).click();
  await page.getByRole("button", { name: "Beta(0.6, 0.6)" }).click();
  await shown("clipped").waitFor();

  step("stepping stones report one stationary distribution");
  assert.match(await page.locator("#markov .readout-line").textContent(), /period 1/);
  assert.match(await page.locator("#markov .readout-line").textContent(), /0\.1008/);

  step("the two-cycle has period 2 and does not settle");
  await page.getByRole("button", { name: "Two-cycle" }).click();
  const cycle = await page.locator("#markov .readout-line").textContent();
  assert.match(cycle, /period 2/);
  assert.match(await page.locator("#markov").textContent(), /does not settle|alternates/);

  step("zero steps keeps the chain at the start");
  await page.getByLabel("Steps", { exact: true }).fill("0");
  await shown("No steps yet").waitFor();

  step("a negative entry and a blank cell are refused");
  await page.getByLabel("Steps", { exact: true }).fill("20");
  const cell = page.getByLabel("Probability from 1 to 1");
  await cell.fill("-1");
  await shown("negative entry").waitFor();
  assert.match(await page.locator("#markov svg").first().textContent(), /Not drawn/);
  await cell.fill("");
  await shown("not a finite number").waitFor();

  step("two closed classes are not a unique stationary distribution");
  await page.getByRole("button", { name: "Two closed classes" }).click();
  assert.match(await page.locator("#markov .readout-line").textContent(), /not unique/);

  step("forty intervals, then 100 more, keep the first interval");
  await page.waitForFunction(() => document.querySelectorAll("#coverage [data-sample]").length === 40);
  const first = await page.locator("#coverage [data-sample='0']").getAttribute("data-lower");
  await page.getByRole("button", { name: "100 more" }).click();
  await page.waitForFunction(() => document.querySelectorAll("#coverage [data-sample]").length === 140);
  assert.equal(await page.locator("#coverage [data-sample='0']").getAttribute("data-lower"), first);
  assert.match(await page.locator("#coverage .readout-line").textContent(), /Exact/);

  step("no intervals is an empty figure, not a fake fraction");
  await page.getByLabel("Number of intervals", { exact: true }).fill("0");
  await page.locator("#coverage .graph-note", { hasText: "No intervals drawn." }).waitFor();
  assert.match(await page.locator("#coverage .readout-line").textContent(), /none yet/);
  assert.equal(await page.locator("#coverage [data-sample]").count(), 0);

  step("a mean interval refuses a sample of size 1");
  await page.getByLabel("Number of intervals", { exact: true }).fill("10");
  await spin("Sample size as a number").fill("1");
  await shown(/divisor/).waitFor();
  assert.match(await page.locator("#coverage svg").first().textContent(), /Not drawn/);

  step("a proportion shows the Wald sawtooth, including p = 0");
  await page.locator("#coverage").getByRole("button", { name: "Reset" }).click();
  await page.getByLabel("Population", { exact: true }).selectOption("bernoulli");
  await shown("sawtooth").waitFor();
  assert.equal(await page.getByLabel("Probability p as a number").isVisible(), true);
  await spin("Probability p as a number").fill("0");
  await page.waitForFunction(() => document.querySelector("#coverage [data-sample='0']"));
  const atZero = await page.locator("#coverage .readout-line").textContent();
  assert.match(atZero, /Hits/);
  assert.equal(problems.length, 0, problems.join("\n"));

  step("exponential coverage is labelled Monte Carlo");
  await page.getByLabel("Population", { exact: true }).selectOption("exponential");
  await shown(/Monte Carlo, 20000 repetitions/).waitFor({ timeout: 30_000 });

  step("the normal density crosses the frame and the ticks are ordered");
  assert.equal(problems.length, 0, problems.join("\n"));
  assertSpread(await distributionCharts());

  step("every family draws a mass or a density and a distribution function");
  const families = ["bernoulli", "binomial", "poisson", "geometric", "uniform", "exponential", "normal", "gamma", "beta", "chi2", "t", "cauchy", "lognormal", "pareto", "weibull", "f"];
  const familySelect = page.locator("#distribution").getByLabel("Distribution family");
  for (const id of families) {
    await familySelect.selectOption(id);
    await page.waitForFunction((familyId) => {
      const select = document.querySelector("#distribution select");
      const drawn = document.querySelector("#distribution svg polyline, #distribution svg circle");
      return select && select.value === familyId && drawn;
    }, id);
    assertSpread(await distributionCharts());
  }

  step("a binomial sample size moves the stems");
  await familySelect.selectOption("binomial");
  const stemsAtTen = await page.locator("#distribution svg").first().locator("circle").count();
  await spin("n as a number").fill("25");
  await page.waitForFunction((start) => document.querySelector("#distribution svg").querySelectorAll("circle").length > start, stemsAtTen);
  assert.ok(await page.locator("#distribution svg").first().locator("circle").count() > stemsAtTen);
  assertSpread(await distributionCharts());

  step("a closed chart keeps a real width, then follows the container");
  await familySelect.selectOption("normal");
  await page.locator("#distribution .readout-line").getByText("Normal").waitFor();
  await page.locator("#distribution .graph-plot").first().evaluate((node) => {
    node.style.width = "0px";
  });
  await page.waitForFunction(() => Number(document.querySelector("#distribution svg").getAttribute("viewBox").split(" ")[2]) === 640);
  await page.locator("#distribution .graph-plot").first().evaluate((node) => {
    node.style.width = "";
  });
  await page.waitForFunction(() => {
    const svg = document.querySelector("#distribution svg");
    const width = Number(svg.getAttribute("viewBox").split(" ")[2]);
    const host = svg.parentElement.clientWidth;
    return host > 400 && width === Math.max(280, Math.round(host));
  });
  assertSpread(await distributionCharts());

  step("dark theme redraws the posterior");
  const light = await page.locator("#beta svg polyline").evaluateAll((nodes) => nodes.map((node) => node.getAttribute("stroke")));
  assert.ok(light.includes("#1d4e9e"), light.join(","));
  const lightDensity = await page.locator("#distribution svg polyline").first().getAttribute("stroke");
  assert.equal(lightDensity, "#1d4e9e");
  await page.evaluate(() => document.body.classList.add("quarto-dark"));
  await page.waitForFunction(() => [...document.querySelectorAll("#beta svg polyline")].some((node) => node.getAttribute("stroke") === "#9eb6f0"));
  await page.waitForFunction(() => document.querySelector("#distribution svg polyline").getAttribute("stroke") === "#9eb6f0");

  step("a narrow viewport keeps the charts inside the window");
  await page.setViewportSize({ width: 390, height: 800 });
  await page.waitForFunction(() => {
    const svg = document.querySelector("#beta svg");
    const width = Number((svg.getAttribute("viewBox") || "").split(" ")[2]);
    return width > 200 && width < 420;
  });
  await page.waitForFunction(() => [...document.querySelectorAll("#distribution svg")].every((svg) => {
    const width = Number((svg.getAttribute("viewBox") || "").split(" ")[2]);
    return width > 200 && width < 420;
  }));
  assertSpread(await distributionCharts());
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
  assert.ok(overflow < 8, `horizontal overflow ${overflow}px`);
  assert.equal(problems.length, 0, problems.join("\n"));
  console.log("passed");
} finally {
  await browser.close();
  await new Promise((resolve) => server.close(resolve));
}
