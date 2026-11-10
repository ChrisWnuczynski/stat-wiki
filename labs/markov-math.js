// Finite Markov chains for the laboratory. No DOM.
//
// A row is a distribution over the next state. Communicating classes come from
// reachability. The period of a class is the gcd of level[u] + 1 - level[v]
// over the edges inside the class; 0 means the class has no edge to itself.
// There is one stationary distribution for each closed class, found by
// Gaussian elimination on that class. It is the unique stationary distribution
// when there is exactly one closed class.
//
// The generator is not R's. A seed reproduces this page, not an R session.

import { mulberry32 } from "./stat-math.js";

export const MIN_STATES = 2;
export const MAX_STATES = 6;
export const MAX_STEPS = 5000;
const ROW_TOL = 1e-9;

const THIRD = 1 / 3;
const HALF = 1 / 2;

function stickyMatrix() {
  const stay = 0.96;
  const move = (1 - stay) / 2;
  return [0, 1, 2].map((i) => [0, 1, 2].map((j) => (i === j ? stay : move)));
}

export const PRESETS = [
  {
    id: "stepping",
    label: "Six stepping stones",
    detail: "From each stone the frog jumps to a neighbour, except from stone 4, which always goes to stone 6. Start on stone 1.",
    start: 0,
    states: ["1", "2", "3", "4", "5", "6"],
    matrix: [
      [0, THIRD, 0, THIRD, THIRD, 0],
      [HALF, 0, HALF, 0, 0, 0],
      [HALF, 0, 0, HALF, 0, 0],
      [0, 0, 0, 0, 0, 1],
      [0, 0, 0, HALF, 0, HALF],
      [0, 0, HALF, 0, HALF, 0],
    ],
  },
  {
    id: "weather",
    label: "Weather",
    detail: "A dry day stays dry with probability 0.8. A wet day stays wet with probability 0.6.",
    start: 0,
    states: ["Dry", "Wet"],
    matrix: [
      [0.8, 0.2],
      [0.4, 0.6],
    ],
  },
  {
    id: "cycle",
    label: "Two-cycle",
    detail: "Every step switches state. The distribution oscillates. The fraction of time in each state still settles.",
    start: 0,
    states: ["1", "2"],
    matrix: [
      [0, 1],
      [1, 0],
    ],
  },
  {
    id: "sticky",
    label: "Sticky",
    detail: "The chain stays put with probability 0.96, so the starting state is forgotten slowly.",
    start: 0,
    states: ["1", "2", "3"],
    matrix: stickyMatrix(),
  },
  {
    id: "reducible",
    label: "Two closed classes",
    detail: "The start moves into one of two closed classes. One path's time average follows the class it hits.",
    start: 0,
    states: ["Start", "A", "B", "C"],
    matrix: [
      [0, 0.5, 0, 0.5],
      [0, 0.8, 0.2, 0],
      [0, 0.4, 0.6, 0],
      [0, 0, 0, 1],
    ],
  },
];

export const DEFAULTS = Object.freeze({ preset: "stepping", steps: 60, seed: 2026 });

function finiteSquare(matrix) {
  if (!Array.isArray(matrix) || matrix.length < MIN_STATES || matrix.length > MAX_STATES) {
    return `A transition matrix needs ${MIN_STATES} to ${MAX_STATES} states.`;
  }
  const n = matrix.length;
  for (let i = 0; i < n; i++) {
    if (!Array.isArray(matrix[i]) || matrix[i].length !== n) return `Row ${i + 1} needs ${n} entries.`;
  }
  return null;
}

export function validateMatrix(matrix) {
  const shape = finiteSquare(matrix);
  if (shape) return shape;
  for (let i = 0; i < matrix.length; i++) {
    let sum = 0;
    for (let j = 0; j < matrix.length; j++) {
      const value = matrix[i][j];
      if (!Number.isFinite(value)) return `Row ${i + 1} has an entry that is not a finite number.`;
      if (value < 0) return `Row ${i + 1} has a negative entry.`;
      sum += value;
    }
    if (Math.abs(sum - 1) > ROW_TOL) return `Row ${i + 1} sums to ${sum.toPrecision(4)}, not 1.`;
  }
  return null;
}

export function normaliseRows(matrix) {
  const shape = finiteSquare(matrix);
  if (shape) return { error: shape };
  const out = [];
  for (let i = 0; i < matrix.length; i++) {
    let sum = 0;
    for (let j = 0; j < matrix.length; j++) {
      const value = matrix[i][j];
      if (!Number.isFinite(value)) return { error: `Row ${i + 1} has an entry that is not a finite number.` };
      if (value < 0) return { error: `Row ${i + 1} has a negative entry.` };
      sum += value;
    }
    if (!(sum > 0)) return { error: `Row ${i + 1} sums to 0, so it cannot be rescaled.` };
    out.push(matrix[i].map((value) => value / sum));
  }
  return { matrix: out };
}

function gcd(a, b) {
  let x = Math.abs(a);
  let y = Math.abs(b);
  while (y) {
    const next = x % y;
    x = y;
    y = next;
  }
  return x;
}

function periodOf(matrix, states) {
  const inside = new Set(states);
  const start = states[0];
  const level = new Map([[start, 0]]);
  const queue = [start];
  let period = 0;
  while (queue.length) {
    const u = queue.shift();
    for (let v = 0; v < matrix.length; v++) {
      if (!(matrix[u][v] > 0) || !inside.has(v)) continue;
      if (!level.has(v)) {
        level.set(v, level.get(u) + 1);
        queue.push(v);
      }
      period = gcd(period, level.get(u) + 1 - level.get(v));
    }
  }
  return period;
}

export function communicatingClasses(matrix) {
  const n = matrix.length;
  const reach = Array.from({ length: n }, () => Array(n).fill(false));
  for (let i = 0; i < n; i++) {
    reach[i][i] = true;
    for (let j = 0; j < n; j++) if (matrix[i][j] > 0) reach[i][j] = true;
  }
  for (let k = 0; k < n; k++) {
    for (let i = 0; i < n; i++) {
      if (!reach[i][k]) continue;
      for (let j = 0; j < n; j++) if (reach[k][j]) reach[i][j] = true;
    }
  }
  const seen = Array(n).fill(false);
  const classes = [];
  for (let i = 0; i < n; i++) {
    if (seen[i]) continue;
    const states = [];
    for (let j = 0; j < n; j++) {
      if (reach[i][j] && reach[j][i]) {
        states.push(j);
        seen[j] = true;
      }
    }
    const closed = states.every((state) => {
      for (let j = 0; j < n; j++) if (matrix[state][j] > 0 && !states.includes(j)) return false;
      return true;
    });
    classes.push({ states, closed, period: periodOf(matrix, states) });
  }
  return classes;
}

// Solve M x = the last column. M is an array of rows of length n + 1.
function solveAugmented(rows) {
  const n = rows.length;
  const m = rows.map((row) => row.slice());
  for (let col = 0; col < n; col++) {
    let pivot = col;
    for (let r = col + 1; r < n; r++) if (Math.abs(m[r][col]) > Math.abs(m[pivot][col])) pivot = r;
    if (!(Math.abs(m[pivot][col]) > 1e-14)) return null;
    if (pivot !== col) [m[col], m[pivot]] = [m[pivot], m[col]];
    const scale = m[col][col];
    for (let c = col; c <= n; c++) m[col][c] /= scale;
    for (let r = 0; r < n; r++) {
      if (r === col) continue;
      const factor = m[r][col];
      if (factor === 0) continue;
      for (let c = col; c <= n; c++) m[r][c] -= factor * m[col][c];
    }
  }
  return m.map((row) => row[n]);
}

function asProbability(vector) {
  if (!vector) return null;
  const clipped = vector.map((value) => (value < 0 && value > -1e-10 ? 0 : value));
  if (clipped.some((value) => value < 0 || !Number.isFinite(value))) return null;
  const sum = clipped.reduce((total, value) => total + value, 0);
  if (!(sum > 0)) return null;
  return clipped.map((value) => value / sum);
}

function stationaryOn(matrix, states) {
  const n = states.length;
  const rows = states.map((j) => {
    const row = states.map((i) => matrix[i][j] - (i === j ? 1 : 0));
    row.push(0);
    return row;
  });
  for (let c = 0; c < n; c++) rows[n - 1][c] = 1;
  rows[n - 1][n] = 1;
  return asProbability(solveAugmented(rows));
}

export function analyse(matrix) {
  const problem = validateMatrix(matrix);
  if (problem) return { error: problem };
  const classes = communicatingClasses(matrix);
  const distributions = [];
  for (const item of classes) {
    if (!item.closed) continue;
    const pi = stationaryOn(matrix, item.states);
    if (!pi) return { error: "The stationary equations could not be solved." };
    const full = Array(matrix.length).fill(0);
    item.states.forEach((state, index) => {
      full[state] = pi[index];
    });
    distributions.push({ states: item.states.slice(), pi: full });
  }
  const closed = classes.filter((item) => item.closed);
  return {
    classes,
    unique: closed.length === 1,
    settles: closed.length > 0 && closed.every((item) => item.period === 1),
    distributions,
  };
}

export function limitingFrom(matrix, start, chain) {
  if (chain.error) return null;
  const home = chain.distributions.find((item) => item.states.includes(start));
  if (home) return home.pi.slice();
  const closedStates = new Set(chain.distributions.flatMap((item) => item.states));
  const transient = [];
  for (let i = 0; i < matrix.length; i++) if (!closedStates.has(i)) transient.push(i);
  if (!transient.length || !transient.includes(start)) return null;
  const mix = Array(matrix.length).fill(0);
  for (const dist of chain.distributions) {
    const rows = transient.map((i) => {
      const row = transient.map((j) => (i === j ? 1 : 0) - matrix[i][j]);
      row.push(dist.states.reduce((sum, j) => sum + matrix[i][j], 0));
      return row;
    });
    const weights = solveAugmented(rows);
    if (!weights) return null;
    const weight = weights[transient.indexOf(start)];
    dist.pi.forEach((probability, state) => {
      mix[state] += weight * probability;
    });
  }
  return asProbability(mix);
}

function checkPath(matrix, start, steps) {
  const problem = validateMatrix(matrix);
  if (problem) return { error: problem };
  if (!Number.isInteger(start) || start < 0 || start >= matrix.length) return { error: "The starting state is not one of the states." };
  if (!Number.isInteger(steps) || steps < 0 || steps > MAX_STEPS) {
    return { error: `The number of steps must be a whole number from 0 to ${MAX_STEPS}.` };
  }
  return null;
}

export function distributionPath(start, matrix, steps) {
  const problem = checkPath(matrix, start, steps);
  if (problem) return problem;
  const n = matrix.length;
  let dist = Array(n).fill(0);
  dist[start] = 1;
  const distributions = [dist];
  for (let t = 0; t < steps; t++) {
    const next = Array(n).fill(0);
    for (let i = 0; i < n; i++) {
      const mass = dist[i];
      if (mass === 0) continue;
      for (let j = 0; j < n; j++) next[j] += mass * matrix[i][j];
    }
    dist = next;
    distributions.push(dist);
  }
  return { distributions };
}

export function simulate(seed, start, matrix, steps) {
  const problem = checkPath(matrix, start, steps);
  if (problem) return problem;
  if (!Number.isFinite(seed)) return { error: "The seed must be a finite number." };
  const next = mulberry32(seed >>> 0);
  const path = [start];
  let state = start;
  for (let t = 0; t < steps; t++) {
    const draw = next();
    const row = matrix[state];
    let cum = 0;
    let chosen = row.length - 1;
    for (let j = 0; j < row.length; j++) {
      cum += row[j];
      if (draw < cum) {
        chosen = j;
        break;
      }
    }
    state = chosen;
    path.push(state);
  }
  return { path };
}

export function occupation(path, states) {
  const counts = Array(states).fill(0);
  return path.map((state, t) => {
    counts[state] += 1;
    const denom = t + 1;
    return counts.map((count) => count / denom);
  });
}

export function tv(left, right) {
  if (!left || !right || left.length !== right.length) return NaN;
  let sum = 0;
  for (let i = 0; i < left.length; i++) sum += Math.abs(left[i] - right[i]);
  return 0.5 * sum;
}
