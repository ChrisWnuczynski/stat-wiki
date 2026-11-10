# Ask

Phase 1 builds a passage index and a retrieval harness for StatWiki. It does not deploy a worker and it does not add a chat widget.

`ask/core` chunks entries, builds the prompt, maps citation numbers to entry URLs, and calls Workers AI, Vectorize, and KV. `ask/harness` embeds `wiki.json`, then scores open-book and closed-book retrieval.

Set `CLOUDFLARE_ACCOUNT_ID` and `CLOUDFLARE_API_TOKEN` in the environment. `XAI_API_KEY` is optional. If it is unset, retrieval still runs and answers are marked not called.

```
npm test
node --experimental-strip-types harness/index-wiki.ts
node --experimental-strip-types harness/run.ts --all
```

`index-wiki.ts --plan` prints chunk counts and does not call the embedding service. The default run scores the dev split. `--all` scores dev, calibrates the coverage threshold, then scores the held-out split once. `--limit N` caps each set.
