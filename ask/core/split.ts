import { DEV_SIZE, SPLIT_SEED } from "./config.ts"

function mulberry32(seed: number): () => number {
  let state = seed >>> 0
  return () => {
    state = (state + 0x6d2b79f5) >>> 0
    let t = Math.imul(state ^ (state >>> 15), 1 | state)
    t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t
    return ((t ^ (t >>> 14)) >>> 0) / 4294967296
  }
}

export function splitBank(ids: string[], seed = SPLIT_SEED, devSize = DEV_SIZE): { dev: string[]; heldout: string[] } {
  const items = [...ids].sort()
  const random = mulberry32(seed)
  for (let i = items.length - 1; i > 0; i--) {
    const j = Math.floor(random() * (i + 1))
    const swap = items[i]
    items[i] = items[j]
    items[j] = swap
  }
  return { dev: items.slice(0, devSize), heldout: items.slice(devSize) }
}
