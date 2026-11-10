# Ask

`ask/core` chunks entries, builds the prompt, maps citation numbers to entry URLs, and calls Workers AI, Vectorize, and KV. `ask/harness` embeds `wiki.json`, then scores open-book and closed-book retrieval. `ask/worker` is the streaming `POST /ask` endpoint. It does not add a chat widget and it does not change the site.

Set `CLOUDFLARE_ACCOUNT_ID` and `CLOUDFLARE_API_TOKEN` in the environment. `XAI_API_KEY` is optional for the harness. If it is unset, retrieval still runs and answers are marked not called. The worker reads `XAI_API_KEY`, `SESSION_SECRET`, `TURNSTILE_SECRET`, `DEV_ASK_TOKEN`, and `ASK_KILL` from its own secrets. From `ask/worker`, `cf deploy` publishes it. The token needs permission to edit Workers.

```
npm test
node --experimental-strip-types harness/index-wiki.ts
node --experimental-strip-types harness/run.ts --all
node --experimental-strip-types harness/worker-check.ts --worker https://example.workers.dev --limit 5
```

`index-wiki.ts --plan` prints chunk counts and does not call the embedding service. The default run scores the dev split. `--all` scores dev, calibrates the coverage threshold, then scores the held-out split once. `--limit N` caps each set. `worker-check.ts` reads `DEV_ASK_TOKEN` and compares closed-book dev retrieval with the deployed worker.
