// Node test for the package reader. No webR, no browser.

import assert from "node:assert/strict";
import test from "node:test";
import { browserExplanation, packagesForBlocks, packagesIn, scan } from "./packages.js";

test("pkg:: and pkg::: name a package, base packages do not", () => {
  const code = `aq <- datasets::airquality |>
  dplyr::mutate(x = stats::median(Ozone, na.rm = TRUE))
ggplot2::ggplot(aq, ggplot2::aes(Wind)) + scales:::percent_format()`;
  assert.deepEqual(packagesIn(code), ["dplyr", "ggplot2", "scales"]);
});

test("library, require and the namespace loaders, bare or quoted", () => {
  const code = `library(mgcv)
require("lme4")
requireNamespace('broom', quietly = TRUE)
loadNamespace(package = "coda")
library(MASS, warn.conflicts = FALSE)`;
  assert.deepEqual(packagesIn(code), ["mgcv", "lme4", "broom", "coda", "MASS"]);
});

test("comments and strings do not name packages", () => {
  const code = `# dplyr::filter is not used here
x <- "ggplot2::ggplot is in a string"
y <- 'library(tidyr)'
z <- 1 # purrr::map`;
  assert.deepEqual(packagesIn(code), []);
});

test("a package held in a variable is not guessed", () => {
  assert.deepEqual(packagesIn(`pkg <- "dplyr"\nlibrary(pkg, character.only = TRUE)`), []);
});

test("names with dots and digits, and no match inside a longer name", () => {
  assert.deepEqual(packagesIn("data.table::fread(x); EMMIXmfa::mfa(y); x.dplyr::f"), ["data.table", "EMMIXmfa", "x.dplyr"]);
  assert.deepEqual(packagesIn("a$dplyr::b"), ["dplyr"]);
});

test("escaped quotes stay inside their string", () => {
  assert.deepEqual(packagesIn(`x <- "a \\" dplyr::b"; tidyr::pivot_longer(d)`), ["tidyr"]);
});

test("scan keeps positions and reports each string", () => {
  const code = `f("ab") # c\ng('x')`;
  const out = scan(code);
  assert.equal(out.code.length, code.length);
  assert.equal(out.code, `f("  ")    \ng(' ')`);
  assert.deepEqual(out.strings.map((s) => s.body), ["ab", "x"]);
});

test("blocks are read in order with no repeats", () => {
  assert.deepEqual(packagesForBlocks(["dplyr::n()", "ggplot2::aes(); dplyr::n()", "library(mgcv)"]), ["dplyr", "ggplot2", "mgcv"]);
  assert.deepEqual(packagesIn(""), []);
  assert.deepEqual(packagesIn(undefined), []);
});

test("package = \"x\" names a package, in data() and elsewhere", () => {
  assert.deepEqual(packagesIn('data("Orthodont", package = "nlme")'), ["nlme"]);
  assert.deepEqual(packagesIn('system.file("extdata", package="readr"); f(mypackage = "x")'), ["readr"]);
  assert.deepEqual(packagesIn('data("housing", package = "MASS"); x <- "package = \'no\'"'), ["MASS"]);
});

test("browser explanations", () => {
  assert.match(browserExplanation("there is no package called 'mclust'", { unavailable: ["mclust"] }), /mclust package is not available for R in the browser/);
  // A package that webR has but this session did not install is not called unavailable.
  const notInstalled = browserExplanation("there is no package called ‘nlme’");
  assert.match(notInstalled, /not installed in this browser session/);
  assert.match(notInstalled, /install\.packages\("nlme"\)/);
  assert.match(browserExplanation("'data/measurements.csv' does not exist in current working directory ('/home/web_user')."), /file from your own computer/);
  assert.match(browserExplanation("cannot open file 'x.csv': No such file or directory"), /file from your own computer/);
  assert.match(browserExplanation("Error: object 'mix_equal' not found", { earlierFailed: 2 }), /Block 2 above did not run/);
  assert.equal(browserExplanation("Error: object 'aq' not found"), null);
  assert.match(browserExplanation("null function or function signature mismatch", { fatal: true }), /fresh R/);
  assert.equal(browserExplanation("non-numeric argument to binary operator"), null);
});
