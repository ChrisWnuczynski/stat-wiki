// Markov-chain laboratory. The matrix is edited here; the calculations are
// in markov-math.js.

import { controlRow, graphFrame, installLabChrome, markerLegend, readoutLine } from "./lab-chrome.js";
import { analyse, DEFAULTS, distributionPath, limitingFrom, MAX_STATES, MIN_STATES, normaliseRows, occupation, PRESETS, simulate, tv, validateMatrix } from "./markov-math.js";
import { formatNumber } from "./stat-math.js";
import { chartColors, createPlot, drawAxes, message, niceTicks, plotBox, plotClip, rule, scaleLinear, stroke, svgEl } from "./svg-chart.js";

const PATH_LIMIT = 120;

function button(label) {
  const node = document.createElement("button");
  node.type = "button";
  node.textContent = label;
  return node;
}

function cellText(value) {
  if (!Number.isFinite(value)) return "";
  if (value === 0) return "0";
  return String(Number(value.toPrecision(6)));
}

function readCell(input) {
  if (input.value.trim() === "") return Number.NaN;
  return Number(input.value);
}

export function mount(root) {
  installLabChrome();
  root.replaceChildren();
  const opening = PRESETS.find((item) => item.id === DEFAULTS.preset);
  let matrix = opening.matrix.map((row) => row.slice());
  let labels = opening.states.slice();
  let active = opening.id;

  const form = controlRow("Markov chain controls");
  const presets = document.createElement("div");
  presets.className = "control-actions";
  presets.setAttribute("role", "group");
  presets.setAttribute("aria-label", "Chain presets");
  const presetButtons = PRESETS.map((preset) => {
    const node = button(preset.label);
    node.title = preset.detail;
    node.setAttribute("aria-pressed", preset.id === active ? "true" : "false");
    presets.appendChild(node);
    return node;
  });
  const sizeLabel = document.createElement("label");
  sizeLabel.className = "control-field control-field-fixed";
  sizeLabel.append(document.createTextNode("States"));
  const size = document.createElement("select");
  size.setAttribute("aria-label", "Number of states");
  for (let n = MIN_STATES; n <= MAX_STATES; n++) {
    const option = document.createElement("option");
    option.value = String(n);
    option.textContent = String(n);
    size.appendChild(option);
  }
  size.value = String(matrix.length);
  sizeLabel.appendChild(size);
  const grid = document.createElement("div");
  grid.className = "matrix-grid";
  grid.setAttribute("role", "group");
  grid.setAttribute("aria-label", "Transition matrix");
  const startLabel = document.createElement("label");
  startLabel.className = "control-field";
  startLabel.append(document.createTextNode("Start"));
  const start = document.createElement("select");
  start.setAttribute("aria-label", "Starting state");
  startLabel.appendChild(start);
  const stepsLabel = document.createElement("label");
  stepsLabel.className = "control-field control-field-wide";
  const stepsName = document.createElement("span");
  stepsName.textContent = "Steps";
  const stepsWrap = document.createElement("span");
  stepsWrap.className = "control-slider";
  const steps = document.createElement("input");
  steps.type = "range";
  steps.min = "0";
  steps.max = "400";
  steps.step = "1";
  steps.value = String(DEFAULTS.steps);
  steps.setAttribute("aria-label", "Steps");
  const stepsOut = document.createElement("output");
  stepsOut.textContent = String(DEFAULTS.steps);
  stepsWrap.append(steps, stepsOut);
  stepsLabel.append(stepsName, stepsWrap);
  const seedLabel = document.createElement("label");
  seedLabel.className = "control-field control-field-fixed";
  seedLabel.append(document.createTextNode("Seed"));
  const seed = document.createElement("input");
  seed.type = "number";
  seed.step = "1";
  seed.value = String(DEFAULTS.seed);
  seed.setAttribute("aria-label", "Seed");
  seedLabel.appendChild(seed);
  const actions = document.createElement("div");
  actions.className = "control-actions";
  const normalise = button("Normalise rows");
  const newer = button("New path");
  const restore = button("Reset");
  actions.append(normalise, newer, restore);
  const hint = document.createElement("p");
  hint.className = "control-hint";
  hint.textContent = "Each row is the distribution of the next state. A blank cell is not zero. The path uses this seed and is not R's generator.";
  const note = document.createElement("p");
  note.className = "control-note";
  note.setAttribute("role", "status");
  form.append(presets, sizeLabel, grid, startLabel, stepsLabel, seedLabel, actions, hint, note);

  const readout = document.createElement("div");
  const pathFrame = graphFrame("One path");
  const pathNote = document.createElement("p");
  pathNote.className = "graph-note";
  const distFrame = graphFrame("Distribution and occupation");
  const distNote = document.createElement("p");
  distNote.className = "graph-note";
  root.append(form, readout, pathFrame.section, distFrame.section);
  pathFrame.section.append(pathNote);
  distFrame.section.append(distNote);
  const plotA = createPlot(pathFrame.plot, { height: 280, label: "Simulated path" });
  const plotB = createPlot(distFrame.plot, { height: 320, label: "Distribution after each step" });

  function paintPresets() {
    presetButtons.forEach((node, index) => node.setAttribute("aria-pressed", PRESETS[index].id === active ? "true" : "false"));
  }

  function fillStart(preferred) {
    const previous = preferred ?? Number(start.value);
    start.replaceChildren();
    labels.forEach((label, index) => {
      const option = document.createElement("option");
      option.value = String(index);
      option.textContent = label;
      start.appendChild(option);
    });
    start.value = String(previous >= 0 && previous < labels.length ? previous : 0);
  }

  function buildGrid() {
    grid.replaceChildren();
    grid.style.gridTemplateColumns = `repeat(${matrix.length}, minmax(0, 1fr)) auto`;
    matrix.forEach((row, i) => {
      row.forEach((value, j) => {
        const input = document.createElement("input");
        input.type = "number";
        input.min = "0";
        input.step = "any";
        input.value = cellText(value);
        input.setAttribute("aria-label", `Probability from ${labels[i]} to ${labels[j]}`);
        input.addEventListener("input", () => {
          matrix[i][j] = readCell(input);
          active = null;
          paintPresets();
          render();
        });
        grid.appendChild(input);
      });
      const sum = document.createElement("span");
      sum.className = "matrix-sum";
      sum.dataset.row = String(i);
      grid.appendChild(sum);
    });
  }

  function showSums() {
    grid.querySelectorAll(".matrix-sum").forEach((sum) => {
      const row = matrix[Number(sum.dataset.row)];
      if (row.some((value) => !Number.isFinite(value))) {
        sum.textContent = "—";
        return;
      }
      const total = row.reduce((acc, value) => acc + value, 0);
      sum.textContent = Math.abs(total - 1) <= 1e-9 ? "1" : formatNumber(total);
    });
  }

  function applyMatrix(next, nextLabels, presetId, startAt) {
    matrix = next.map((row) => row.slice());
    labels = nextLabels.slice();
    active = presetId;
    size.value = String(matrix.length);
    buildGrid();
    fillStart(startAt);
    paintPresets();
  }

  function render() {
    showSums();
    paintPresets();
    const stepsValue = Number(steps.value);
    stepsOut.textContent = String(stepsValue);
    const seedValue = readNumber(seed);
    const startValue = Number(start.value);
    const problem = validateMatrix(matrix)
      || (!Number.isInteger(seedValue) ? "The seed must be a whole number." : null)
      || (!Number.isInteger(stepsValue) || stepsValue < 0 ? "The number of steps must be a whole number." : null);
    if (problem) {
      note.textContent = problem;
      readout.replaceChildren();
      pathNote.textContent = "";
      distNote.textContent = "";
      plotA.draw((ctx) => message(ctx.svg, ctx.width, ctx.height, ctx.colors, "Not drawn."));
      plotB.draw((ctx) => message(ctx.svg, ctx.width, ctx.height, ctx.colors, "Not drawn."));
      plotA.setLabel(problem);
      plotB.setLabel(problem);
      const old = root.querySelectorAll(".legend-row");
      old.forEach((node) => node.remove());
      return;
    }
    note.textContent = "";
    const chain = analyse(matrix);
    if (chain.error) {
      note.textContent = chain.error;
      return;
    }
    const target = limitingFrom(matrix, startValue, chain);
    const exact = distributionPath(startValue, matrix, stepsValue);
    const simulated = simulate(seedValue, startValue, matrix, stepsValue);
    const fractions = occupation(simulated.path, matrix.length);
    const current = exact.distributions[stepsValue];
    const occ = fractions[stepsValue];
    const classText = chain.classes.map((item) => {
      const name = `{${item.states.map((state) => labels[state]).join(", ")}}`;
      const period = item.period === 0 ? "does not return" : `period ${item.period}`;
      return `${name}${item.closed ? ", closed" : ""}, ${period}`;
    }).join("; ");
    const piText = chain.unique
      ? `(${chain.distributions[0].pi.map((value) => formatNumber(value)).join(", ")})`
      : "not unique";
    const entries = [
      { label: "Classes", value: classText },
      { label: "Stationary", value: piText },
      { label: "Distribution TV", value: formatNumber(tv(current, target)) },
      { label: "Occupation TV", value: formatNumber(tv(occ, target)) },
    ];
    readout.replaceChildren(readoutLine(entries));
    if (!chain.unique) {
      const detail = document.createElement("p");
      detail.className = "graph-note";
      detail.textContent = chain.distributions.map((item) => `{${item.states.map((state) => labels[state]).join(", ")}}: (${item.pi.map((value) => formatNumber(value)).join(", ")})`).join("  ");
      readout.appendChild(detail);
    }
    const shownSteps = Math.min(stepsValue, PATH_LIMIT);
    pathNote.textContent = stepsValue > PATH_LIMIT
      ? `The path shows the first ${PATH_LIMIT} of ${stepsValue} steps.`
      : stepsValue === 0 ? "No steps yet: the chain is still at the start." : "";
    distNote.textContent = chain.settles
      ? "Solid lines are the exact distribution. Dashed lines are the long-run probability from this start. Dotted lines are this path's occupation."
      : "The closed class is periodic, so the distribution alternates and its total variation does not go to 0. The occupation fraction still settles on the dashed line.";
    const colors = chartColors();
    plotA.setLabel(`Path of ${shownSteps} steps from ${labels[startValue]}`);
    plotA.draw(({ svg, width, height, colors: ink }) => {
      const box = plotBox(width, height, { left: 58 });
      const xScale = scaleLinear([0, Math.max(1, shownSteps)], [box.left, box.left + box.innerWidth]);
      const yScale = scaleLinear([-0.5, matrix.length - 0.5], [box.top + box.innerHeight, box.top]);
      drawAxes(svg, box, {
        xScale, yScale,
        xTicks: niceTicks(0, shownSteps, 6).filter((value) => Number.isInteger(value) || shownSteps <= 1),
        yTicks: labels.map((_, index) => index),
        colors: ink,
        xFormat: (value) => String(Math.round(value)),
        yFormat: (value) => labels[value] ?? "",
      });
      const points = simulated.path.slice(0, shownSteps + 1).map((state, t) => [xScale(t), yScale(state)]);
      stroke(svg, points, { stroke: ink.states[0], width: 1.8 });
      points.forEach((point) => svgEl(svg, "circle", { cx: point[0].toFixed(2), cy: point[1].toFixed(2), r: shownSteps > 80 ? 1.4 : 2.4, fill: ink.states[0] }));
    });
    plotB.setLabel(`Distribution through ${stepsValue} steps`);
    plotB.draw(({ svg, width, height, colors: ink }) => {
      const box = plotBox(width, height, { left: 48 });
      const xScale = scaleLinear([0, Math.max(1, stepsValue)], [box.left, box.left + box.innerWidth]);
      const yScale = scaleLinear([0, 1], [box.top + box.innerHeight, box.top]);
      drawAxes(svg, box, {
        xScale, yScale,
        xTicks: niceTicks(0, Math.max(1, stepsValue), 6),
        yTicks: [0, 0.25, 0.5, 0.75, 1],
        colors: ink,
        xFormat: (value) => formatNumber(value),
        yFormat: (value) => formatNumber(value),
      });
      const clip = plotClip(svg, box);
      const layer = svgEl(svg, "g", { "clip-path": `url(#${clip})` });
      labels.forEach((_, state) => {
        const color = ink.states[state % ink.states.length];
        if (target) rule(layer, box.left, yScale(target[state]), box.left + box.innerWidth, yScale(target[state]), { stroke: color, width: 1.2, dash: "6 4" });
        stroke(layer, exact.distributions.map((dist, t) => [xScale(t), yScale(dist[state])]), { stroke: color, width: 1.8 });
        stroke(layer, fractions.map((dist, t) => [xScale(t), yScale(dist[state])]), { stroke: color, width: 1.5, dash: "2 3" });
      });
    });
    const legendItems = labels.map((label, state) => ({ text: label, color: colors.states[state % colors.states.length], kind: "line" }));
    legendItems.push(
      { text: "Long-run from this start", color: colors.text, kind: "line", dash: "dashed" },
      { text: "This path's occupation", color: colors.text, kind: "line", dash: "dotted" },
    );
    const legend = markerLegend(legendItems);
    const old = distFrame.section.querySelector(".legend-row");
    if (old) old.remove();
    distFrame.section.appendChild(legend);
  }

  function readNumber(input) {
    if (input.value.trim() === "") return Number.NaN;
    return Number(input.value);
  }

  presetButtons.forEach((node, index) => {
    node.addEventListener("click", () => {
      const preset = PRESETS[index];
      applyMatrix(preset.matrix, preset.states, preset.id, preset.start);
      render();
    });
  });
  size.addEventListener("change", () => {
    const n = Number(size.value);
    const next = Array.from({ length: n }, (_, i) => Array.from({ length: n }, (_, j) => (i < matrix.length && j < matrix[i].length ? matrix[i][j] : 0)));
    next.forEach((row, i) => {
      const total = row.reduce((sum, value) => sum + (Number.isFinite(value) ? value : 0), 0);
      if (!(total > 0)) {
        row.fill(0);
        row[i] = 0.5;
        row[(i + 1) % n] = 0.5;
      }
    });
    const scaled = normaliseRows(next);
    labels = Array.from({ length: n }, (_, i) => labels[i] || String(i + 1));
    applyMatrix(scaled.error ? next : scaled.matrix, labels, null, 0);
    render();
  });
  start.addEventListener("change", render);
  steps.addEventListener("input", render);
  seed.addEventListener("input", render);
  normalise.addEventListener("click", () => {
    const scaled = normaliseRows(matrix.map((row) => row.map((value) => (Number.isFinite(value) ? value : 0))));
    if (scaled.error) {
      note.textContent = scaled.error;
      return;
    }
    applyMatrix(scaled.matrix, labels, null, Number(start.value));
    render();
  });
  newer.addEventListener("click", () => {
    const current = readNumber(seed);
    seed.value = String(Number.isInteger(current) ? current + 1 : DEFAULTS.seed);
    render();
  });
  restore.addEventListener("click", () => {
    const preset = PRESETS.find((item) => item.id === DEFAULTS.preset);
    steps.value = String(DEFAULTS.steps);
    seed.value = String(DEFAULTS.seed);
    applyMatrix(preset.matrix, preset.states, preset.id, preset.start);
    render();
  });
  applyMatrix(matrix, labels, active, opening.start);
  render();
  return () => {
    plotA.destroy();
    plotB.destroy();
  };
}
