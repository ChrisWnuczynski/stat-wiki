// Browser test of the R runner against test/page.html, with real webR.
//
// The page is served without cross-origin isolation, as GitHub Pages serves
// the site, so webR uses its postMessage channel. R comes from the webR CDN
// and dplyr from the webR package repository: this needs the network, and
// the first start takes a while. Not part of npm test.
//
//   cd webr && node test/e2e.mjs
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
  const file = path === "notes/page.html" ? join(root, "webr", "test", "page.html") : join(root, path);
  if (!file.startsWith(join(root, "webr"))) {
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
const page = await browser.newPage({ viewport: { width: 1000, height: 900 } });
const problems = [];
page.on("pageerror", (error) => problems.push(String(error)));
page.on("console", (message) => {
  if (message.type() === "error") problems.push(message.text());
});

const bar = (n) => page.locator(".r-run").nth(n - 1);
const output = (n) => page.locator(`.r-output[aria-label="Output of R block ${n}"]`);
const status = (n) => bar(n).locator(".r-run-status");
const step = (name) => console.log("-", name);

try {
  await page.goto(base + "notes/page.html");
  step("six blocks get Run and Edit, and the page says what Run does");
  await page.locator(".r-run").first().waitFor();
  assert.equal(await page.locator(".r-run").count(), 6);
  assert.match(await page.locator(".r-run-intro").textContent(), /run in your browser/);
  assert.equal(await page.evaluate(() => window.crossOriginIsolated), false);

  step("Run on block 3 starts R, runs blocks 1 and 2 first, and draws the plot");
  const started = Date.now();
  await bar(3).getByRole("button", { name: "Run" }).click();
  await output(3).locator("canvas").waitFor({ timeout: 240_000 });
  console.log(`  R started and three blocks ran in ${((Date.now() - started) / 1000).toFixed(1)} s`);
  assert.match(await output(1).textContent(), /Ran first/);
  const two = await output(2).textContent();
  assert.match(two, /\[1\] 5/);
  assert.match(two, /a note/);
  assert.match(two, /Warning: careful/);
  assert.match(await status(3).textContent(), /^Ran in/);
  const inked = await output(3).locator("canvas").evaluate((canvas) => {
    const data = canvas.getContext("2d").getImageData(0, 0, canvas.width, canvas.height).data;
    let dark = 0;
    for (let i = 0; i < data.length; i += 4) if (data[i] < 128 && data[i + 3] > 0) dark++;
    return { dark, width: canvas.width, height: canvas.height };
  });
  assert.ok(inked.dark > 500, `the plot has ${inked.dark} dark pixels`);
  assert.ok(inked.width >= 640, `the plot is ${inked.width} px wide`);

  step("an edited block runs with Control+Enter, and later blocks see the change");
  await bar(1).getByRole("button", { name: "Edit" }).click();
  const editor = page.locator(".r-run-editor").first();
  await editor.fill("x <- c(1, 2)");
  assert.equal(await bar(1).getByRole("button", { name: "Reset" }).isVisible(), true);
  await editor.press("Control+Enter");
  await page.waitForFunction(() => /Ran in/.test(document.querySelectorAll(".r-run-status")[0].textContent));
  await bar(2).getByRole("button", { name: "Run" }).click();
  await page.waitForFunction(() => /\[1\] 1\.5/.test(document.querySelector('[aria-label="Output of R block 2"]').textContent));

  step("Reset puts the page's code back");
  await bar(1).getByRole("button", { name: "Reset" }).click();
  assert.equal(await page.locator(".r-run-editor").count(), 0);
  assert.equal(await page.locator("#cb1").isVisible(), true);

  step("an R error shows under its block and does not stop R");
  await bar(4).getByRole("button", { name: "Run" }).click();
  await page.waitForFunction(() => /boom/.test(document.querySelector('[aria-label="Output of R block 4"]')?.textContent ?? ""));
  assert.match(await output(4).locator(".r-out-error").textContent(), /Error: boom/);
  assert.match(await status(4).textContent(), /^Error in/);

  step("a block that names dplyr:: installs it first");
  await bar(5).getByRole("button", { name: "Run" }).click();
  await page.waitForFunction(() => /doubled/.test(document.querySelector('[aria-label="Output of R block 5"]')?.textContent ?? ""), null, { timeout: 240_000 });
  assert.match(await output(5).textContent(), /tibble/);

  step("Stop R ends a block that would run for a minute, and the next Run starts R again");
  await bar(6).getByRole("button", { name: "Run" }).click();
  await bar(6).getByRole("button", { name: "Stop R" }).waitFor();
  assert.equal(await bar(2).getByRole("button", { name: "Run" }).isDisabled(), true);
  await bar(6).getByRole("button", { name: "Stop R" }).click();
  assert.match(await status(6).textContent(), /R stopped/);
  assert.equal(await bar(2).getByRole("button", { name: "Run" }).isDisabled(), false);
  await bar(2).getByRole("button", { name: "Run" }).click();
  await page.waitForFunction(() => /\[1\] 5/.test(document.querySelector('[aria-label="Output of R block 2"]').textContent), null, { timeout: 240_000 });

  assert.deepEqual(problems.filter((text) => !/favicon/.test(text)), []);
  console.log("All browser checks passed.");
} finally {
  await browser.close();
  server.close();
}
