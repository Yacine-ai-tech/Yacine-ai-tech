# GitHub Profile — Yacine-ai-tech/README.md

> Source of truth for the public GitHub profile. Code must strictly back every claim here. Saved 2026-07-02.

# Yacine Seybou Siddo
**AI Systems Engineer** — RAG · MCP Agents · Document AI · LLMOps · FastAPI
🌍 Niamey, Niger · 🇫🇷 FR · 🇺🇸 EN · Upwork

I build production AI systems — the kind that get deployed, stay deployed, and solve a specific problem well.
This year I shipped six standalone tools from a single codebase. Each one is open-source and has a live demo.

## 🚀 Projects

### IntelAI — Persona-Aware AI Analytics & RAG Copilot
The core idea: different executives need different answers from the same data. A CFO asking about margins gets a Finance-scoped response. A CHRO asking about turnover gets a People-scoped one. Same system, nine different lenses — the scope boundaries are enforced by architecture, not just prompt engineering. A self-contained, cloud-deployable product. No dependency on the full platform — single app (**Railway API + Vercel frontend**), managed Postgres (**Neon**).
- 9 C-suite AI personas — each with its own system prompt, data scope, and tool whitelist
- 7 KPI domains — Finance, HR, IT, Ops, Logistics, ESG, Risk — dashboard, analytics, forecasting, and anomaly detection per domain
- GraphRAG-lite + hybrid retrieval + BGE reranker — the differentiator; better cross-entity answer quality than flat vector search
- WebSocket streaming with source citations; **Qdrant vector store in prod, Chroma in dev** (swap via `VECTOR_STORE`); Postgres on **Neon** for relational data; pgvector available via env
- ML forecasting with Monte Carlo confidence bands, four-method anomaly detection, board-ready PDF export
- LiteLLM multi-provider router — swap models via a single env var, no vendor lock-in
- JWT + RBAC, bilingual EN/FR React frontend with Recharts visualizations
- omnismart-personas extracted as a standalone PyPI package — reusable in any LangChain RAG project
- Knowledge graph search, compare-personas mode, governance audit trail, and organization views
Stack: FastAPI · LangChain · ChromaDB · pgvector · PostgreSQL · React · Groq · Claude · LiteLLM · Docker

### AgentKit — MCP Server for Business Intelligence Agents
Six MCP tools that give Claude Desktop, Cursor, or any LangGraph agent direct access to live business data.
- Tools: query KPIs, company health score, anomaly detection, metric forecasting, data inventory, executive summary
- MCP Resources (stable data URIs) + Prompts (reusable templates)
- 3-agent LangGraph workflow — Planner (Claude Sonnet 4.6) → Analyst (Groq) → Reporter (Claude Sonnet 4.6) — with live execution and Markdown report export
- ASGI-level request observability
- Separate demos for Claude Agent SDK, CrewAI, and DSPy
Stack: FastMCP · LangGraph · Claude Sonnet 4.6 · Groq · PostgreSQL · LiteLLM

### DocIntel — Vision-First Document Intelligence
Extracts structured data from PDFs and images using vision models — not just OCR.
- Route A: Claude Sonnet 4.6 Vision — complex layouts, handwriting, mixed languages
- Route B: Ollama local vision (Qwen2.5-VL, validated on GPU; model swappable via env) — fully local, $0/page
- Route C: Tesseract — lightweight fallback for clean scans
- /classify-image — tells you what's in a photo (category + confidence + reasoning), built for auction-listing aggregators and inventory systems
- Released 550-document benchmark — Route A: 100% on multilingual multi-page invoices, 92.5% on phone-photo receipts; SROIE (world-standard) 95% zero-shot · async batch · side-by-side route comparison · session document library · drag-and-drop UI
Stack: FastAPI · LiteLLM · Claude Vision · Ollama · Tesseract · pdfplumber · Docker

### VoiceFlow — Speech to Structured Intelligence
Record audio in the browser, get structured output — not just a transcript.
- Meeting mode → action items with owner, deadline, and priority
- Sales call mode → deal stage, pain points, objections, buying signals, CRM-paste-ready note
- Routes to Claude Sonnet 4.6 for sales calls (nuance matters) and Groq LLaMA 3.3 for meeting notes (speed matters)
- Transcription providers: WhisperX · Groq Whisper · Deepgram · AssemblyAI
- Custom schema extraction, webhook integrations relay, and analytics dashboard
- Real-time voice agent demo via OpenAI Realtime API (with full Gemini Multimodal Live API fallback)
Stack: FastAPI · WhisperX · Groq · Claude · LiteLLM · edge-tts · Docker

### RAGeval — Self-Hosted LLMOps Observability
```python
from rageval import track

@track(project="my_rag_app")
async def answer(question): ...
# That's the entire integration.
```
`pip install omnismart-rageval`  (distribution name; import is `from rageval import track`)
- 5 scoring dimensions: retrieval relevance · groundedness · faithfulness · cost · latency
- Multi-judge consensus across Claude Haiku + Groq + GPT + Gemini 2.5 Flash — disagreement triggers a human-review flag
- Persona-aware: catches when a CFO response pulls data outside its Finance scope
- Live telemetry event stream and model configuration API
- SQLite by default — zero infrastructure. Postgres + pgvector optional. OpenTelemetry export included.
- Browser dashboard (/demo/) · PyPI published
Stack: FastAPI · sentence-transformers · LiteLLM · SQLite/Postgres · OpenTelemetry · React

### StreamPulse — Real-Time Data Pipeline
Multi-source ingestion with a live WebSocket dashboard that updates as records arrive.
- Sources: webhooks · Gmail · Google Sheets · CSV · REST APIs
- Hybrid classifier: keyword fast path → BGE embedding fallback → Claude Haiku last resort
- First-class n8n integration — custom node template + 3 importable workflows (auction aggregation, invoice intake, CRM sync)
- Event replay, pipeline status aggregates, and source/destination management
- /webhook/.../with-vision composes with DocIntel for image-bearing payloads
Stack: FastAPI · PostgreSQL · pgvector · DuckDB · React · n8n · Prefect 3 · LiteLLM

## 🛠 Stack
- LLMs: Claude Sonnet 4.6 · Claude Haiku 4.5 · GPT-4o / GPT-5 · Gemini 2.5 Pro · Groq LLaMA 3.3 · DeepSeek V3 · AWS Bedrock · Ollama (local)
- Abstraction: LiteLLM — every project routes across providers via a single env var
- Frameworks: FastAPI · LangChain · LangGraph · FastMCP
- Embeddings: BGE-large-en-v1.5 · all-MiniLM-L6-v2
- Vector: ChromaDB (dev) · Qdrant / pgvector (prod)
- Frontend: React · Recharts · Vite
- Storage: PostgreSQL · SQLite · DuckDB
- Pipelines: n8n · Prefect 3 · dlt
- Monitoring: Prometheus · Grafana · OpenTelemetry
- Speech: faster-whisper · WhisperX · Deepgram · AssemblyAI
- DevOps: Docker · Railway · Render · GitHub Actions · AWS

## 📦 Published Packages
| Package | Description |
|---|---|
| omnismart-rageval | Self-hosted LLMOps observability for RAG systems (import: `rageval`) |
| omnismart-personas | Drop-in 9-persona templates for LangChain RAG |
