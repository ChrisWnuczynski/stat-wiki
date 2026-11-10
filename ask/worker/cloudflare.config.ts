import { bindings, defineConfig, exports as workerExports } from "cf/config"

const name = "statwiki-ask"

export default defineConfig({
  worker: {
    name,
    entrypoint: "./src/index.ts",
    compatibilityDate: "2026-11-10",
    compatibilityFlags: ["nodejs_compat"],
    workersDev: true,
    previewUrls: false,
    observability: {
      enabled: true,
      logs: {
        enabled: true,
        invocationLogs: false,
        persist: true,
      },
    },
    exports: {
      AskBudget: workerExports.durableObject({ storage: "sqlite" }),
    },
    env: {
      AI: bindings.ai(),
      VECTORS: bindings.vectorize({ name: "statwiki-ask" }),
      CHUNKS: bindings.kv({ id: "f340dc62af8e4db6a02474b15154b9bb" }),
      BUDGET: bindings.durableObject({ worker: name, exportName: "AskBudget" }),
      XAI_API_KEY: bindings.secret(),
      TURNSTILE_SECRET: bindings.secret(),
      SESSION_SECRET: bindings.secret(),
      DEV_ASK_TOKEN: bindings.secret(),
      ASK_KILL: bindings.secret(),
      ASK_DAILY_BUDGET: bindings.text("400"),
      COVERAGE_THRESHOLD: bindings.text("0.410"),
    },
  },
})
