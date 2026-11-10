# Ask

`ask/core` chunks entries, builds the prompt, maps citation numbers to entry URLs, and calls Workers AI, Vectorize, and KV. `ask/harness` embeds `wiki.json`, scores retrieval, and checks the answers and the misuse handling. `ask/worker` is the streaming `POST /ask` endpoint at `https://ask.statwiki.io`. `ask/widget` is the chat on the site's pages.

## The Worker

- A browser opens a session with Turnstile (`POST /session`), then asks with that session (`POST /ask`). There is no other way in.
- If nothing in StatWiki scores above the coverage threshold, the Worker sends a fixed reply and does not call the model.
- Each answer stream starts with a `status` event (`{"covered": true|false}`), then `delta` events, then `citations`.
- CORS allows `https://www.statwiki.io` and localhost only.
- Limits: 30 questions per session and 60 per address each day, and a global daily budget of 400 questions. `ASK_KILL` set to anything but `0`, `false`, `no` or `off` stops all model calls.
- Secrets: `XAI_API_KEY`, `SESSION_SECRET`, `TURNSTILE_SECRET`, `ASK_KILL`. The `workers.dev` address is switched off.

From `ask/worker`, `cf deploy` publishes it. The token needs permission to edit Workers, and Workers Routes on `statwiki.io` for the custom domain.

## Checks

Set `CLOUDFLARE_ACCOUNT_ID`, `CLOUDFLARE_API_TOKEN` and `XAI_API_KEY`. Behind a proxy, also set `NODE_USE_ENV_PROXY=1`.

```
npm test
node --experimental-strip-types harness/index-wiki.ts
node --experimental-strip-types harness/run.ts --all
node --experimental-strip-types harness/answers.ts --models grok-4.7,grok-4.7@low --student
node --experimental-strip-types harness/misuse-check.ts
```

- `index-wiki.ts` embeds `wiki.json`. `--plan` prints chunk counts without calling the embedding service.
- `run.ts` scores retrieval only. `--all` scores dev, calibrates the coverage threshold, then scores the held-out split once.
- `answers.ts` answers the dev questions with the Worker's retrieval, prompt and limits, then a judge grades each answer against the worked answer. `--modes closed,open` picks the modes; closed removes the question's own worked answer from retrieval. A model can carry a thinking level, as in `grok-4.7@low`. Every answer is saved, and the report flags worked answers the judge doubted.
- `misuse-check.ts` sends every misuse prompt through the Worker's own handler with the real index and model, saves each reply, and has the judge decide whether model-written replies were acceptable. `misuse-new.jsonl` holds prompts the threshold was not tuned on.

## The widget

`ask/widget` builds two files into `ask/widget/dist`, which the site ships as a resource. `loader.js` (under 4 KB) is on every page and adds the Ask StatWiki button; it shows only on `statwiki.io`. `app.js` (React, Markdown, the reading panel) loads when the chat is opened. Maths uses the site's own KaTeX from `/katex/`.

- The browser check (Turnstile) runs when someone first asks, not on page load. The session lasts 12 hours and is kept in the browser.
- Model text is rendered with raw HTML off and sanitised: no links, images or scripts from the model. Citation numbers become buttons only for numbers the Worker returned.
- A citation opens the cited block in a panel beside the chat. The conversation, the panel and whether the chat is open are kept in the browser, so they follow the reader to the next page. An answer cut off by a page change offers Try again.

```
cd widget
npm ci
npm run build
npm test
npm run e2e
```

`npm run e2e` runs the browser tests against `test/server.mjs`, which serves fixture pages, the built widget and a stand-in Worker.
