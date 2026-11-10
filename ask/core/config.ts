// Live retrieval settings. Chosen before any scored run.

export const EMBEDDING_MODEL = "@cf/qwen/qwen3-embedding-0.6b"
export const EMBEDDING_DIMENSIONS = 1024
export const EMBEDDING_METRIC = "cosine"
export const QUERY_INSTRUCTION = "Given a web search query, retrieve relevant passages that answer the query"

export const VECTORIZE_INDEX = "statwiki-ask"
export const KV_TITLE = "statwiki-ask-chunks"

export const CHUNK_CHARS = 3000
export const CHUNKER_VERSION = 1

export const CANDIDATE_K = 20
export const FETCH_K = 50
export const TOKEN_BUDGET = 6000

export const PAGE_BOOST = 0.08
export const SECTION_BOOST = 0.05
export const TITLE_BOOST = 0.1
export const DEFINES_BOOST = 0.06

export const SPLIT_SEED = 1729
export const DEV_SIZE = 100

export const WIKI_URL = "https://www.statwiki.io/wiki.json"

export const XAI_BASE_URL = "https://api.x.ai/v1"
export const ANSWER_MODEL = "grok-4.7"
export const COMPARE_MODEL = "grok-4.6"
export const JUDGE_MODEL = "grok-4.7"
export const ANSWER_MAX_TOKENS = 1500
export const WORKER_MAX_TOKENS = 1200
export const WORKER_K = 8
export const COVERAGE_THRESHOLD = 0.41
export const QUESTION_CHAR_LIMIT = 2000
export const MAX_TURNS = 6
export const SESSION_DAILY_LIMIT = 30
export const IP_DAILY_LIMIT = 60
export const DEFAULT_DAILY_BUDGET = 400
export const SESSION_TTL_SECONDS = 12 * 60 * 60
export const RESTING_MESSAGE = "Ask StatWiki is resting until tomorrow"

export const OVERLAP_PARAGRAPH_CHARS = 180
export const OVERLAP_WORDS = 40
