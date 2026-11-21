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
  const mass = page.locator("#distribution svg").first();
  const stems = mass.locator("g[clip-path] line");
  const n = spin("n as a number");
  const nSlider = page.locator("#distribution").getByRole("slider", { name: "n", exact: true });
  const nFeedbackId = await n.getAttribute("aria-describedby");
  assert.ok(nFeedbackId, "the number field has linked feedback");
  const nFeedback = page.locator(`[id="${nFeedbackId}"]`);
  const accessibility = await page.context().newCDPSession(page);
  await accessibility.send("Accessibility.enable");
  const statusNodes = new Map();
  async function assertFeedbackStatus(input, feedback, text) {
    const id = await feedback.getAttribute("id");
    assert.equal(await input.getAttribute("aria-describedby"), id);
    const status = feedback.locator("..");
    assert.equal(await status.getAttribute("role"), "status");
    assert.equal(await status.getAttribute("aria-live"), "polite");
    assert.equal(await status.getAttribute("aria-atomic"), "true");
    assert.equal(await feedback.getAttribute("aria-live"), null, "only the wrapper is a live region");
    assert.equal(await status.locator("[aria-live], [role='status'], [role='alert'], input").count(), 0);
    assert.equal(await status.textContent(), text);
    assert.notEqual(await status.evaluate((node) => getComputedStyle(node).display), "none");
    assert.equal(await status.evaluate((node) => getComputedStyle(node).visibility), "visible");
    const { root } = await accessibility.send("DOM.getDocument");
    const { nodeId } = await accessibility.send("DOM.querySelector", {
      nodeId: root.nodeId, selector: `[role="status"]:has(> [id="${id}"])`,
    });
    assert.ok(nodeId, "the linked note has a persistent status wrapper");
    const { nodes } = await accessibility.send("Accessibility.getPartialAXTree", { nodeId });
    const exposed = nodes.find((node) => node.role?.value === "status" && !node.ignored);
    assert.ok(exposed, "the status is exposed in Chromium's accessibility tree, even when empty");
    assert.ok(Number.isInteger(exposed.backendDOMNodeId));
    if (!statusNodes.has(id)) statusNodes.set(id, exposed.backendDOMNodeId);
    assert.equal(exposed.backendDOMNodeId, statusNodes.get(id), "the same status survives invalid and valid edits");
    assert.equal(exposed.properties.find((property) => property.name === "live")?.value.value, "polite");
    assert.equal(exposed.properties.find((property) => property.name === "atomic")?.value.value, true);
    const { nodeId: inputId } = await accessibility.send("DOM.querySelector", {
      nodeId: root.nodeId, selector: `input[aria-describedby="${id}"]`,
    });
    const { nodes: inputNodes } = await accessibility.send("Accessibility.getPartialAXTree", { nodeId: inputId });
    const spinbutton = inputNodes.find((node) => node.role?.value === "spinbutton" && !node.ignored);
    assert.ok(spinbutton);
    assert.equal(spinbutton.description?.value ?? "", text, "the field exposes its own feedback");
  }
  await assertFeedbackStatus(n, nFeedback, "");
  assert.equal(await nFeedback.isVisible(), false);
  const emptyRow = await n.evaluate((input) => {
    const field = input.closest(".control-field").getBoundingClientRect();
    const controls = input.closest(".control-slider").getBoundingClientRect();
    return field.bottom - controls.bottom;
  });
  assert.ok(Math.abs(emptyRow) < 1, `empty status adds no visual row: ${emptyRow}px`);
  assert.equal(await stems.count(), 11);
  await n.fill("25");
  await page.waitForFunction(() => document.querySelector("#distribution svg").querySelectorAll("g[clip-path] line").length === 26);
  assert.equal(await stems.count(), 26);
  assert.equal(await mass.locator("circle").count(), 26);
  assertSpread(await distributionCharts());

  step("invalid binomial edits keep the accepted value and both plots");
  const acceptedCharts = await distributionCharts();
  const acceptedReadout = await page.locator("#distribution .readout-line").textContent();
  assert.match(acceptedReadout, /n 25, p 0\.3/);
  async function assertInvalidN(raw) {
    assert.equal(await n.inputValue(), raw);
    assert.equal(await nSlider.inputValue(), "25");
    assert.equal(await n.evaluate((input) => input === document.activeElement), true);
    assert.equal(await n.getAttribute("aria-invalid"), "true");
    assert.equal(await nFeedback.isVisible(), true);
    assert.match(await nFeedback.textContent(), /from 1 to 40 in steps of 1.*Showing 25/);
    await assertFeedbackStatus(n, nFeedback, "n must be a number from 1 to 40 in steps of 1. Showing 25.");
    assert.equal(await page.locator("#distribution .readout-line").textContent(), acceptedReadout);
    assert.equal(await stems.count(), 26);
    assert.equal(await mass.locator("circle").count(), 26);
    assert.deepEqual(await distributionCharts(), acceptedCharts);
  }
  for (const raw of ["10.5", "10.0000000001", "0", "41"]) {
    await n.fill(raw);
    await assertInvalidN(raw);
  }
  await n.press("ControlOrMeta+A");
  await n.press("Delete");
  await assertInvalidN("");
  await n.press("-");
  assert.equal(await n.evaluate((input) => input.validity.badInput), true);
  await assertInvalidN("");
  await n.press("ControlOrMeta+A");
  await n.press("Delete");
  await assertInvalidN("");

  step("keyboard digits accept n = 12, clear feedback and draw the CDF endpoints");
  await n.press("1");
  assert.equal(await n.inputValue(), "1");
  assert.equal(await nSlider.inputValue(), "1");
  assert.equal(await n.getAttribute("aria-invalid"), null);
  assert.equal(await nFeedback.textContent(), "");
  await n.press("2");
  assert.equal(await n.inputValue(), "12");
  assert.equal(await nSlider.inputValue(), "12");
  assert.equal(await n.evaluate((input) => input === document.activeElement), true);
  assert.equal(await nFeedback.isVisible(), false);
  await assertFeedbackStatus(n, nFeedback, "");
  assert.equal(await stems.count(), 13);
  assert.equal(await mass.locator("circle").count(), 13);
  assert.match(await page.locator("#distribution .readout-line").textContent(), /n 12, p 0\.3/);
  const twelveCharts = await distributionCharts();
  assertSpread(twelveCharts);
  const cdf = twelveCharts[1];
  const yZero = cdf.yLabels.find((tick) => parseTick(tick.text) === 0).y;
  const yOne = cdf.yLabels.find((tick) => parseTick(tick.text) === 1).y;
  const probabilityAt = (point) => (yZero - point[1]) / (yZero - yOne);
  assert.equal(cdf.points.length, 26);
  assert.equal(cdf.points[0][0], cdf.points[1][0]);
  assert.ok(Math.abs(probabilityAt(cdf.points[1]) - 0.7 ** 12) < 0.01 / (yZero - yOne), "F(0) = 0.7^12, within SVG rounding");
  assert.equal(probabilityAt(cdf.points.at(-1)), 1, "F(12) = 1");
  assert.equal(cdf.points.at(-1)[0], cdf.xLabels.find((tick) => parseTick(tick.text) === 12).x);

  step("keyboard range input recovers from invalid text and keeps focus");
  await n.fill("12.5");
  assert.equal(await n.getAttribute("aria-invalid"), "true");
  assert.equal(await n.evaluate((input) => input === document.activeElement), true);
  assert.equal(await nSlider.inputValue(), "12");
  assert.deepEqual(await distributionCharts(), twelveCharts);
  await assertFeedbackStatus(n, nFeedback, "n must be a number from 1 to 40 in steps of 1. Showing 12.");
  await nSlider.focus();
  await nSlider.press("ArrowRight");
  assert.equal(await nSlider.inputValue(), "13");
  assert.equal(await n.inputValue(), "13");
  assert.equal(await nSlider.evaluate((input) => input === document.activeElement), true);
  assert.equal(await n.getAttribute("aria-invalid"), null);
  assert.equal(await nFeedback.textContent(), "");
  await assertFeedbackStatus(n, nFeedback, "");
  assert.equal(await stems.count(), 14);
  assertSpread(await distributionCharts());

  step("a decimal sigma stays editable and obeys its configured step");
  await familySelect.selectOption("normal");
  const sigma = spin("σ as a number");
  const sigmaSlider = page.locator("#distribution").getByRole("slider", { name: "σ", exact: true });
  const sigmaFeedbackId = await sigma.getAttribute("aria-describedby");
  assert.ok(sigmaFeedbackId);
  const sigmaFeedback = page.locator(`[id="${sigmaFeedbackId}"]`);
  assert.notEqual(sigmaFeedbackId, nFeedbackId);
  await assertFeedbackStatus(sigma, sigmaFeedback, "");
  await sigma.focus();
  await sigma.press("ControlOrMeta+A");
  await sigma.press("Delete");
  for (const key of ["1", ".", "2", "5"]) await sigma.press(key);
  assert.equal(await sigma.inputValue(), "1.25");
  assert.equal(await sigmaSlider.inputValue(), "1.25");
  assert.equal(await sigma.evaluate((input) => input === document.activeElement), true);
  assert.equal(await sigma.getAttribute("aria-invalid"), null);
  assert.equal(await sigmaFeedback.textContent(), "");
  assert.match(await page.locator("#distribution .readout-line").textContent(), /σ 1\.25/);
  const decimalCharts = await distributionCharts();
  assertSpread(decimalCharts);
  for (const raw of ["1.23", "1.2500000001"]) {
    await sigma.fill(raw);
    assert.equal(await sigma.inputValue(), raw);
    assert.equal(await sigmaSlider.inputValue(), "1.25");
    assert.equal(await sigma.getAttribute("aria-invalid"), "true");
    assert.match(await sigmaFeedback.textContent(), /from 0\.3 to 3 in steps of 0\.05.*Showing 1\.25/);
    await assertFeedbackStatus(sigma, sigmaFeedback, "σ must be a number from 0.3 to 3 in steps of 0.05. Showing 1.25.");
    assert.deepEqual(await distributionCharts(), decimalCharts);
  }
  await sigmaSlider.focus();
  await sigmaSlider.press("ArrowRight");
  assert.equal(await sigmaSlider.inputValue(), "1.3");
  assert.equal(await sigma.inputValue(), "1.3");
  assert.equal(await sigmaSlider.evaluate((input) => input === document.activeElement), true);
  assert.equal(await sigma.getAttribute("aria-invalid"), null);
  assert.equal(await sigmaFeedback.textContent(), "");
  assert.match(await page.locator("#distribution .readout-line").textContent(), /σ 1\.3/);
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
