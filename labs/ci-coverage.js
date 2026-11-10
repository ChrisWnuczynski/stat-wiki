// Confidence-interval laboratory. The samples and the coverage sums are in
// coverage-math.js. This file only draws them.

import { controlRow, graphFrame, installLabChrome, markerLegend, readoutLine } from "./lab-chrome.js";
import {
  DEFAULTS,
  LIMITS,
  METHODS,
  POPULATIONS,
  draw,
  exactMeanCoverage,
  exactProportionCoverage,
  exponentialMonteCarlo,
  fractionBand,
  populationById,
  runningFraction,
  truthOf,
  validate,
} from "./coverage-math.js";
import { formatNumber } from "./stat-math.js";
import { band, chartColors, createPlot, drawAxes, message, niceTicks, plotBox, rule, scaleLinear, stroke, svgEl } from "./svg-chart.js";

function button(label) {
  const node = document.createElement("button");
  node.type = "button";
  node.textContent = label;
  return node;
}

function readNumber(input) {
  if (input.value.trim() === "") return Number.NaN;
  return Number(input.value);
}

export function mount(root) {
  installLabChrome();
  root.replaceChildren();
  const form = controlRow("Confidence interval controls");
  const population = document.createElement("select");
  population.setAttribute("aria-label", "Population");
  for (const item of POPULATIONS) {
    const option = document.createElement("option");
    option.value = item.id;
    option.textContent = item.label;
    option.title = item.detail;
    population.appendChild(option);
  }
  population.value = DEFAULTS.population;
  const populationLabel = document.createElement("label");
  populationLabel.className = "control-field";
  populationLabel.append(Object.assign(document.createElement("span"), { textContent: "Population" }), population);

  const method = document.createElement("select");
  method.setAttribute("aria-label", "Interval");
  const methodLabel = document.createElement("label");
  methodLabel.className = "control-field";
  methodLabel.append(Object.assign(document.createElement("span"), { textContent: "Interval" }), method);

  const nLabel = document.createElement("label");
  nLabel.className = "control-field";
  const nWrap = document.createElement("span");
  nWrap.className = "control-slider";
  const nSlider = document.createElement("input");
  nSlider.type = "range";
  nSlider.min = "1";
  nSlider.max = String(LIMITS.nMax);
  nSlider.step = "1";
  nSlider.value = String(DEFAULTS.n);
  nSlider.setAttribute("aria-label", "Sample size");
  const nNumber = document.createElement("input");
  nNumber.type = "number";
  nNumber.min = "1";
  nNumber.max = String(LIMITS.nMax);
  nNumber.step = "1";
  nNumber.value = String(DEFAULTS.n);
  nNumber.setAttribute("aria-label", "Sample size as a number");
  nWrap.append(nSlider, nNumber);
  nLabel.append(Object.assign(document.createElement("span"), { textContent: "Sample size n" }), nWrap);

  const level = document.createElement("select");
  level.setAttribute("aria-label", "Confidence level");
  for (const value of [0.9, 0.95, 0.99]) {
    const option = document.createElement("option");
    option.value = String(value);
    option.textContent = `${Math.round(value * 100)}%`;
    level.appendChild(option);
  }
  level.value = String(DEFAULTS.level);
  const levelLabel = document.createElement("label");
  levelLabel.className = "control-field control-field-fixed";
  levelLabel.append(Object.assign(document.createElement("span"), { textContent: "Level" }), level);

  const countLabel = document.createElement("label");
  countLabel.className = "control-field";
  const countWrap = document.createElement("span");
  countWrap.className = "control-slider";
  const countSlider = document.createElement("input");
  countSlider.type = "range";
  countSlider.min = "0";
  countSlider.max = String(LIMITS.countMax);
  countSlider.step = "1";
  countSlider.value = String(DEFAULTS.count);
  countSlider.setAttribute("aria-label", "Number of intervals");
  const countOut = document.createElement("output");
  countOut.textContent = String(DEFAULTS.count);
  countWrap.append(countSlider, countOut);
  countLabel.append(Object.assign(document.createElement("span"), { textContent: "Intervals" }), countWrap);

  const pLabel = document.createElement("label");
  pLabel.className = "control-field control-field-wide";
  const pWrap = document.createElement("span");
  pWrap.className = "control-slider";
  const pSlider = document.createElement("input");
  pSlider.type = "range";
  pSlider.min = "0";
  pSlider.max = "1";
  pSlider.step = "0.01";
  pSlider.value = String(DEFAULTS.p);
  pSlider.setAttribute("aria-label", "Probability p");
  const pNumber = document.createElement("input");
  pNumber.type = "number";
  pNumber.min = "0";
  pNumber.max = "1";
  pNumber.step = "0.01";
  pNumber.value = String(DEFAULTS.p);
  pNumber.setAttribute("aria-label", "Probability p as a number");
  pWrap.append(pSlider, pNumber);
  pLabel.append(Object.assign(document.createElement("span"), { textContent: "Probability p" }), pWrap);

  const seedLabel = document.createElement("label");
  seedLabel.className = "control-field control-field-fixed";
  const seed = document.createElement("input");
  seed.type = "number";
  seed.step = "1";
  seed.value = String(DEFAULTS.seed);
  seed.setAttribute("aria-label", "Seed");
  seedLabel.append(Object.assign(document.createElement("span"), { textContent: "Seed" }), seed);

  const actions = document.createElement("div");
  actions.className = "control-actions";
  const more = button("100 more");
  const restore = button("Reset");
  actions.append(more, restore);
  const hint = document.createElement("p");
  hint.className = "control-hint";
  hint.textContent = "Adding intervals keeps the ones already drawn. The seed reproduces this page, not an R session.";
  const note = document.createElement("p");
  note.className = "control-note";
  note.setAttribute("role", "status");
  form.append(populationLabel, methodLabel, nLabel, levelLabel, countLabel, pLabel, seedLabel, actions, hint, note);

  const readout = document.createElement("div");
  const stack = graphFrame("Repeated intervals");
  const stackNote = document.createElement("p");
  stackNote.className = "graph-note";
  const running = graphFrame("Coverage");
  const runningNote = document.createElement("p");
  runningNote.className = "graph-note";
  root.append(form, readout, stack.section, running.section);
  stack.section.append(stackNote);
  running.section.append(runningNote);
  const plotA = createPlot(stack.plot, { height: 360, label: "Repeated confidence intervals" });
  const plotB = createPlot(running.plot, { height: 300, label: "Coverage" });
  let mcCache = null;
  let curveCache = null;

  function cachedMonteCarlo(cfg) {
    const key = `${cfg.n}|${cfg.level}|${cfg.method}`;
    if (!mcCache || mcCache.key !== key) mcCache = { key, value: exponentialMonteCarlo({ n: cfg.n, level: cfg.level, method: cfg.method }) };
    return mcCache.value;
  }

  function cachedCurves(n, level) {
    const key = `${n}|${level}`;
    if (curveCache && curveCache.key === key) return curveCache;
    const grid = 80;
    const wald = [];
    const wilson = [];
    for (let i = 0; i <= grid; i++) {
      const p = i / grid;
      wald.push(exactProportionCoverage(n, p, level, "wald"));
      wilson.push(exactProportionCoverage(n, p, level, "wilson"));
    }
    curveCache = { key, grid, wald, wilson };
    return curveCache;
  }

  function fillMethods(keep) {
    const kind = populationById(population.value).kind;
    const options = METHODS[kind];
    method.replaceChildren();
    for (const item of options) {
      const option = document.createElement("option");
      option.value = item.id;
      option.textContent = item.label;
      method.appendChild(option);
    }
    method.value = options.some((item) => item.id === keep) ? keep : options[0].id;
    pLabel.classList.toggle("control-hidden", kind !== "proportion");
    nSlider.min = kind === "mean" ? String(LIMITS.nMinMean) : "1";
  }

  function config() {
    return {
      population: population.value,
      method: method.value,
      n: readNumber(nNumber),
      level: Number(level.value),
      seed: readNumber(seed),
      p: readNumber(pNumber),
    };
  }

  function render() {
    const count = Number(countSlider.value);
    countOut.textContent = String(count);
    more.disabled = count >= LIMITS.countMax;
    const cfg = config();
    const problem = validate(cfg) || (!Number.isInteger(count) || count < 0 ? "The number of intervals must be a whole number." : null);
    const pop = populationById(cfg.population);
    if (problem) {
      note.textContent = problem;
      readout.replaceChildren();
      stackNote.textContent = "";
      runningNote.textContent = "";
      plotA.draw((ctx) => message(ctx.svg, ctx.width, ctx.height, ctx.colors, "Not drawn."));
      plotB.draw((ctx) => message(ctx.svg, ctx.width, ctx.height, ctx.colors, "Not drawn."));
      plotA.setLabel(problem);
      plotB.setLabel(problem);
      root.querySelectorAll(".legend-row").forEach((node) => node.remove());
      return;
    }
    note.textContent = count >= LIMITS.countMax ? `${LIMITS.countMax} is the most intervals this page draws.` : "";
    const drawn = draw(cfg.seed, cfg, count);
    const truth = truthOf(cfg);
    const proportion = pop.kind === "proportion";
    let reference = null;
    let referenceLabel = "";
    if (proportion) {
      reference = exactProportionCoverage(cfg.n, cfg.p, cfg.level, cfg.method);
      referenceLabel = "Exact";
    } else if (pop.id === "exponential") {
      const mc = cachedMonteCarlo(cfg);
      reference = mc.coverage;
      referenceLabel = "Monte Carlo";
      runningNote.textContent = `Monte Carlo, ${mc.reps} repetitions, standard error ${formatNumber(mc.se)}. The normal-theory interval is not exact for an exponential sample. The shaded band is a normal approximation to the realised fraction.`;
    } else {
      reference = exactMeanCoverage(cfg.n, cfg.level, cfg.method);
      referenceLabel = cfg.method === "t" ? "Exact" : "Exact under normality";
      const claim = cfg.method === "z-with-s"
        ? "z with s uses the normal quantile. Under normality the coverage is the t probability of that quantile, which is below the stated level."
        : "Under normality the t interval covers with probability exactly equal to the stated level.";
      const extra = count === 0 ? " No intervals yet, so there is no running fraction." : " The shaded band is a normal approximation to the realised fraction, not a second confidence interval.";
      runningNote.textContent = claim + extra;
    }
    const fraction = drawn.fraction;
    readout.replaceChildren(readoutLine([
      { label: "Truth", value: formatNumber(truth) },
      { label: "Drawn", value: String(count) },
      { label: "Hits", value: String(drawn.hits) },
      { label: "Fraction", value: fraction === null ? "none yet" : formatNumber(fraction) },
      { label: referenceLabel, value: formatNumber(reference) },
    ]));
    const colors = chartColors();
    if (count === 0) {
      stackNote.textContent = "No intervals drawn.";
      plotA.setLabel("No intervals drawn");
      plotA.draw((ctx) => message(ctx.svg, ctx.width, ctx.height, ctx.colors, "No intervals drawn."));
    } else {
      const lows = drawn.intervals.map((row) => row.lower);
      const highs = drawn.intervals.map((row) => row.upper);
      const sortedLow = [...lows].sort((a, b) => a - b);
      const sortedHigh = [...highs].sort((a, b) => a - b);
      const q = (list, p) => list[Math.min(list.length - 1, Math.max(0, Math.round((list.length - 1) * p)))];
      let lo = Math.min(truth, q(sortedLow, 0.05));
      let hi = Math.max(truth, q(sortedHigh, 0.95));
      if (!(hi > lo)) {
        lo -= 1;
        hi += 1;
      }
      const pad = (hi - lo) * 0.08;
      lo -= pad;
      hi += pad;
      const outside = drawn.intervals.some((row) => row.lower < lo || row.upper > hi);
      stackNote.textContent = outside ? "Some intervals extend past the axis." : "A miss is drawn in the contrasting colour. An endpoint counts as a hit.";
      plotA.setLabel(`${drawn.hits} of ${count} intervals cover ${formatNumber(truth)}`);
      plotA.draw(({ svg, width, height, colors: ink }) => {
        const box = plotBox(width, height, { left: 36, right: 12 });
        const xScale = scaleLinear([lo, hi], [box.left, box.left + box.innerWidth]);
        const yOf = (index) => box.top + ((index + 0.5) / count) * box.innerHeight;
        drawAxes(svg, box, {
          xScale,
          yScale: (value) => value,
          xTicks: niceTicks(lo, hi, 5),
          yTicks: [],
          colors: ink,
          xFormat: (value) => formatNumber(value),
          yFormat: () => "",
        });
        rule(svg, xScale(truth), box.top, xScale(truth), box.top + box.innerHeight, { stroke: ink.truth, width: 1.6 });
        drawn.intervals.forEach((row, index) => {
          const y = yOf(index);
          const x1 = xScale(Math.max(lo, Math.min(hi, row.lower)));
          const x2 = xScale(Math.max(lo, Math.min(hi, row.upper)));
          const color = row.covers ? ink.hit : ink.miss;
          const line = Math.abs(x2 - x1) < 1.5
            ? svgEl(svg, "circle", { cx: (x1 + x2) / 2, cy: y, r: 2.4, fill: color })
            : rule(svg, x1, y, x2, y, { stroke: color, width: count > 120 ? 1 : 2 });
          line.dataset.sample = String(index);
          line.dataset.lower = String(row.lower);
          line.dataset.upper = String(row.upper);
          line.dataset.covers = row.covers ? "yes" : "no";
        });
      });
    }
    const legend = markerLegend([
      { text: "Covers", color: colors.hit, kind: "line" },
      { text: "Misses", color: colors.miss, kind: "line" },
      { text: "Truth", color: colors.truth, kind: "line" },
    ]);
    const oldLegend = stack.section.querySelector(".legend-row");
    if (oldLegend) oldLegend.remove();
    stack.section.appendChild(legend);

    if (proportion) {
      runningNote.textContent = "Exact coverage, summed over the binomial counts. The stated level is the horizontal line. Wald's curve is the sawtooth.";
      const curves = cachedCurves(cfg.n, cfg.level);
      const { grid, wald, wilson } = curves;
      plotB.setLabel(`Exact ${cfg.method} coverage at p = ${formatNumber(cfg.p)} is ${formatNumber(reference)}`);
      plotB.draw(({ svg, width, height, colors: ink }) => {
        const box = plotBox(width, height);
        const xScale = scaleLinear([0, 1], [box.left, box.left + box.innerWidth]);
        const yScale = scaleLinear([0, 1], [box.top + box.innerHeight, box.top]);
        drawAxes(svg, box, {
          xScale, yScale,
          xTicks: [0, 0.25, 0.5, 0.75, 1],
          yTicks: [0, 0.5, cfg.level, 1].filter((value, index, list) => list.indexOf(value) === index).sort((a, b) => a - b),
          colors: ink,
          xFormat: (value) => formatNumber(value),
          yFormat: (value) => formatNumber(value),
        });
        rule(svg, box.left, yScale(cfg.level), box.left + box.innerWidth, yScale(cfg.level), { stroke: ink.muted, width: 1, dash: "4 3" });
        const place = (series) => series.map((value, index) => [xScale(index / grid), yScale(value)]);
        stroke(svg, place(wald), { stroke: ink.miss, width: cfg.method === "wald" ? 2.2 : 1.3 });
        stroke(svg, place(wilson), { stroke: ink.hit, width: cfg.method === "wilson" ? 2.2 : 1.3 });
        svgEl(svg, "circle", { cx: xScale(cfg.p), cy: yScale(reference), r: 4, fill: cfg.method === "wald" ? ink.miss : ink.hit, stroke: ink.bg, "stroke-width": 1 });
      });
      const curveLegend = markerLegend([
        { text: "Wald", color: colors.miss, kind: "line" },
        { text: "Wilson", color: colors.hit, kind: "line" },
        { text: "Stated level", color: colors.muted, kind: "line", dash: "dashed" },
      ]);
      const old = running.section.querySelector(".legend-row");
      if (old) old.remove();
      running.section.appendChild(curveLegend);
      return;
    }

    const series = runningFraction(drawn.intervals);
    const shade = count > 0 ? fractionBand(count, reference, 0.95) : null;
    plotB.setLabel(count === 0 ? "No running fraction yet" : `Running coverage ${formatNumber(fraction)}`);
    plotB.draw(({ svg, width, height, colors: ink }) => {
      const box = plotBox(width, height);
      const xMax = Math.max(1, count);
      const xScale = scaleLinear([1, xMax], [box.left, box.left + box.innerWidth]);
      const yScale = scaleLinear([0, 1], [box.top + box.innerHeight, box.top]);
      drawAxes(svg, box, {
        xScale, yScale,
        xTicks: niceTicks(1, xMax, 5),
        yTicks: [0, 0.5, reference, 1].filter((value) => value >= 0 && value <= 1),
        colors: ink,
        xFormat: (value) => String(Math.round(value)),
        yFormat: (value) => formatNumber(value),
      });
      if (shade && Number.isFinite(shade.lower)) {
        const top = yScale(Math.min(1, shade.upper));
        const bottom = yScale(Math.max(0, shade.lower));
        band(svg, box.left, top, box.innerWidth, Math.max(0, bottom - top), ink.posterior, 0.15);
      }
      rule(svg, box.left, yScale(reference), box.left + box.innerWidth, yScale(reference), { stroke: ink.truth, width: 1.5, dash: "6 4" });
      if (series.length) stroke(svg, series.map((row) => [xScale(row.m), yScale(row.fraction)]), { stroke: ink.posterior, width: 2 });
    });
    const runLegend = markerLegend([
      { text: "Running fraction", color: colors.posterior, kind: "line" },
      { text: referenceLabel, color: colors.truth, kind: "line", dash: "dashed" },
      { text: "Normal approximation", color: colors.posterior, kind: "tick" },
    ]);
    const oldRun = running.section.querySelector(".legend-row");
    if (oldRun) oldRun.remove();
    running.section.appendChild(runLegend);
  }

  function syncN(fromSlider) {
    if (fromSlider) nNumber.value = nSlider.value;
    else if (nNumber.value.trim() !== "" && Number.isFinite(Number(nNumber.value))) nSlider.value = nNumber.value;
    render();
  }
  population.addEventListener("change", () => {
    fillMethods(method.value);
    render();
  });
  method.addEventListener("change", render);
  level.addEventListener("change", render);
  nSlider.addEventListener("input", () => syncN(true));
  nNumber.addEventListener("input", () => syncN(false));
  countSlider.addEventListener("input", render);
  pSlider.addEventListener("input", () => {
    pNumber.value = pSlider.value;
    render();
  });
  pNumber.addEventListener("input", () => {
    if (pNumber.value.trim() !== "" && Number.isFinite(Number(pNumber.value))) pSlider.value = pNumber.value;
    render();
  });
  seed.addEventListener("input", render);
  more.addEventListener("click", () => {
    const next = Math.min(LIMITS.countMax, Number(countSlider.value) + 100);
    countSlider.value = String(next);
    render();
  });
  restore.addEventListener("click", () => {
    population.value = DEFAULTS.population;
    fillMethods(DEFAULTS.method);
    nSlider.value = String(DEFAULTS.n);
    nNumber.value = String(DEFAULTS.n);
    level.value = String(DEFAULTS.level);
    countSlider.value = String(DEFAULTS.count);
    pSlider.value = String(DEFAULTS.p);
    pNumber.value = String(DEFAULTS.p);
    seed.value = String(DEFAULTS.seed);
    render();
  });
  fillMethods(DEFAULTS.method);
  render();
  return () => {
    plotA.destroy();
    plotB.destroy();
  };
}
