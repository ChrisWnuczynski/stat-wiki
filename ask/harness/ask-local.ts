// Ask questions through the Worker's own handler from a terminal and print
// the replies with their citations.
//
//   node --experimental-strip-types harness/ask-local.ts --page /notes/x.html "Can I have a link to this chapter?"
//   node --experimental-strip-types harness/ask-local.ts --model grok-4.7@low "Why take logs?" "What is a p-value?"
//
// Needs CLOUDFLARE_ACCOUNT_ID, CLOUDFLARE_API_TOKEN and XAI_API_KEY.

import { Cloudflare } from "../core/cloudflare.ts"
import { ANSWER_MODEL, ANSWER_REASONING_EFFORT, WIKI_URL } from "../core/config.ts"
import { buildGraph } from "../core/graph.ts"
import { loadWiki } from "../core/wiki-file.ts"
import { localAsk } from "./local.ts"

const argv = process.argv.slice(2)
const flag = (name: string) => {
  const i = argv.indexOf(`--${name}`)
  if (i < 0) return ""
  const [value] = argv.splice(i, 2).slice(1)
  return value ?? ""
}
const page = flag("page")
const anchor = flag("anchor")
const spec = flag("model") || (ANSWER_REASONING_EFFORT ? `${ANSWER_MODEL}@${ANSWER_REASONING_EFFORT}` : ANSWER_MODEL)
const wiki = flag("wiki") || WIKI_URL
const questions = argv
if (questions.length === 0) throw new Error("give at least one question")

const graph = buildGraph(await loadWiki(wiki))
const client = await Cloudflare.connect()
const { ask } = await localAsk(client, graph, spec, process.env.XAI_API_KEY?.trim() ?? "")
for (const question of questions) {
  const result = await ask(question, { page, anchor })
  console.log(`\n=== ${question}${page ? `  (on ${page})` : ""}  [${spec}, ${result.covered ? "covered" : "not covered"}]`)
  console.log(result.reply)
  for (const c of result.citations) console.log(`  [${c.number}] ${c.title} (${c.kind}) ${c.url}`)
}
