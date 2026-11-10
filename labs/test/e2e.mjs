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

function spin(name) {
  return page.getByRole("spinbutton", { name, exact: true });
}

try {
  await page.goto(base + "labs/test/page.html");
  await page.getByRole("button", { name: "Beta(5, 5)" }).waitFor();
  step("default Beta(5, 5) with 3 heads in 10 tosses is Beta(8, 12) with mean 0.4");
  await page.getByText("Beta(8, 12)").waitFor();
  assert.match(await page.locator("#beta .readout-line").textContent(), /0\.4/);
  assert.equal(problems.length, 0, problems.join("\n"));

  step("uniform prior");
  await page.getByRole("button", { name: "Beta(1, 1)" }).click();
  await page.getByText("Beta(4, 8)").waitFor();
  assert.match(await page.locator("#beta .readout-line").textContent(), /0\.3333/);

  step("no tosses leaves the posterior equal to the prior");
  await page.locator("#beta").getByRole("button", { name: "Reset" }).click();
  await spin("Tosses n as a number").fill("0");
  await page.getByText("No tosses yet").waitFor();
  assert.match(await page.locator("#beta .readout-line").textContent(), /Beta\(5, 5\)/);
  assert.equal(await page.locator("#beta svg polyline").count() > 0, true);

  step("a shape that is not a number draws nothing");
  await page.locator("#beta").getByRole("button", { name: "Reset" }).click();
  await spin("Prior heads α as a number").fill("");
  await page.getByText("α must be a number").waitFor();
  assert.match(await page.locator("#beta svg").first().textContent(), /Not drawn/);

  step("an unbounded prior is clipped rather than scaled to infinity");
  await page.locator("#beta").getByRole("button", { name: "Reset" }).click();
  await page.getByRole("button", { name: "Beta(0.6, 0.6)" }).click();
  await page.getByText("clipped").waitFor();

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
  await page.getByText("No steps yet").waitFor();

  step("a negative entry and a blank cell are refused");
  await page.getByLabel("Steps", { exact: true }).fill("20");
  const cell = page.getByLabel("Probability from 1 to 1");
  await cell.fill("-1");
  await page.getByText("negative entry").waitFor();
  assert.match(await page.locator("#markov svg").first().textContent(), /Not drawn/);
  await cell.fill("");
  await page.getByText("not a finite number").waitFor();

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
  await page.getByText(/divisor/).waitFor();
  assert.match(await page.locator("#coverage svg").first().textContent(), /Not drawn/);

  step("a proportion shows the Wald sawtooth, including p = 0");
  await page.locator("#coverage").getByRole("button", { name: "Reset" }).click();
  await page.getByLabel("Population", { exact: true }).selectOption("bernoulli");
  await page.getByText("sawtooth").waitFor();
  assert.equal(await page.getByLabel("Probability p as a number").isVisible(), true);
  await spin("Probability p as a number").fill("0");
  await page.waitForFunction(() => document.querySelector("#coverage [data-sample='0']"));
  const atZero = await page.locator("#coverage .readout-line").textContent();
  assert.match(atZero, /Hits/);
  assert.equal(problems.length, 0, problems.join("\n"));

  step("exponential coverage is labelled Monte Carlo");
  await page.getByLabel("Population", { exact: true }).selectOption("exponential");
  await page.getByText(/Monte Carlo, 20000 repetitions/).waitFor({ timeout: 30_000 });

  step("dark theme redraws the posterior");
  const light = await page.locator("#beta svg polyline").evaluateAll((nodes) => nodes.map((node) => node.getAttribute("stroke")));
  assert.ok(light.includes("#1d4e9e"), light.join(","));
  await page.evaluate(() => document.body.classList.add("quarto-dark"));
  await page.waitForFunction(() => [...document.querySelectorAll("#beta svg polyline")].some((node) => node.getAttribute("stroke") === "#9eb6f0"));

  step("a narrow viewport keeps the charts inside the window");
  await page.setViewportSize({ width: 390, height: 800 });
  await page.waitForFunction(() => {
    const svg = document.querySelector("#beta svg");
    const width = Number((svg.getAttribute("viewBox") || "").split(" ")[2]);
    return width > 200 && width < 420;
  });
  const overflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
  assert.ok(overflow < 8, `horizontal overflow ${overflow}px`);
  assert.equal(problems.length, 0, problems.join("\n"));
  console.log("passed");
} finally {
  await browser.close();
  await new Promise((resolve) => server.close(resolve));
}
