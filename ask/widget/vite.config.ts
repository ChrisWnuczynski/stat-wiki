import react from "@vitejs/plugin-react"
import { defineConfig } from "vite"

// Two entries. loader.js is the only file every page loads; app.js (React,
// Markdown, the reading panel) is fetched when someone opens the chat.
export default defineConfig({
  plugins: [react()],
  base: "./",
  build: {
    outDir: "dist",
    emptyOutDir: true,
    target: "es2022",
    rollupOptions: {
      input: { loader: "src/loader.ts", app: "src/app.tsx" },
      preserveEntrySignatures: "exports-only",
      output: {
        entryFileNames: "[name].js",
        chunkFileNames: "chunks/[name]-[hash].js",
        assetFileNames: "[name][extname]",
      },
    },
  },
})
