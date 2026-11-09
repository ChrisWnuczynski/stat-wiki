// Write the exact draws the laboratory generator produces.
// Python and R never reimplement this generator. They only see these numbers.
import { mkdir, writeFile } from "node:fs/promises";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import {
  DEFAULTS,
  POPULATIONS,
  population,
  realise,
  samplePrefix,
  sequence,
  uniformStream,
} from "./kde-math.js";

const root = dirname(fileURLToPath(import.meta.url));
const extra = [
  { weight: 0.3, mean: -2, sd: 0.8 },
  { weight: 0.7, mean: 1, sd: 0.3 },
];

const seq = sequence(DEFAULTS.seed);
const seq7 = sequence(7);
if (seq.error || seq7.error) throw new Error(seq.error || seq7.error);

const cases = [
  { name: "mixture-n120", seed: DEFAULTS.seed, n: 120, population: "mixture" },
  { name: "mixture-n40", seed: DEFAULTS.seed, n: 40, population: "mixture" },
  { name: "normal-n80", seed: DEFAULTS.seed, n: 80, population: "normal" },
  { name: "normal-n15", seed: 7, n: 15, population: "normal" },
  { name: "extra-mixture-n25", seed: 7, n: 25, population: "extra" },
];

const samples = cases.map((item) => {
  const source = item.seed === 7 ? seq7 : seq;
  const components = item.population === "extra" ? extra : population(item.population).components;
  const drawn = item.population === "extra"
    ? realise(source, components, item.n)
    : samplePrefix(source, item.population, item.n);
  if (drawn.error) throw new Error(drawn.error);
  return {
    name: item.name,
    seed: item.seed,
    n: item.n,
    population: item.population,
    components,
    values: drawn.values,
  };
});

const payload = {
  generator: "labs/kde-math.js mulberry32 then Box-Muller. Not R's RNG.",
  uniforms3500: uniformStream(3500, 6),
  samples,
  populations: POPULATIONS,
};

const dest = join(root, "fixtures", "samples.json");
await mkdir(dirname(dest), { recursive: true });
await writeFile(dest, JSON.stringify(payload));
console.log(dest);
