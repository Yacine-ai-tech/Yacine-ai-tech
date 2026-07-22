<div align="center">
  Yacine Seybou Siddo
 
**AI Systems Engineer**
 
`RAG` `MCP Agents` `Document AI` `LLMOps` `FastAPI`
 
🇳🇪 🌍 Niamey, Niger &nbsp;·&nbsp; FR &nbsp;·&nbsp; EN &nbsp;·&nbsp; [![Upwork](https://img.shields.io/badge/Hire%20me%20on-Upwork-6FDA44?style=flat&logo=upwork&logoColor=white)](https://www.upwork.com/freelancers/yacineseybousiddoai)
 
</div>

I build production AI systems — the kind that get deployed, stay deployed, and solve a specific problem well.

Six standalone tools shipped in 2026. All open-source (AGPL-3.0). All live. Four on PyPI.
 
 
## 🚀 Projects
 
### [IntelAI](https://github.com/Yacine-ai-tech/IntelAI) — Persona-Aware AI Analytics & RAG Copilot

The core idea: different executives need different answers from the same data. A CFO asking about margins gets a Finance-scoped response. A CHRO asking about turnover gets a People-scoped one. The scope boundaries are enforced by architecture, not prompt engineering.

- **9 C-suite AI personas** — CEO, CFO, CTO, COO, CHRO, ESG, Risk, Analyst, General — each with its own data scope, system prompt, and tool whitelist
- **169 curated KPIs** across 7 domains (Finance, HR, IT, Ops, Logistics, ESG, Risk) — 36-month history, 7 benchmarking scenarios
- **Hybrid retrieval** — BGE-large-en-v1.5 dense + BM25 + RRF fusion + BGE Reranker v2-m3 cross-encoder; Cohere rerank as hosted backstop (resilience when inference Studio is unreachable)
- **GraphRAG-lite** — entity graph over KPI records for multi-hop queries (`USE_GRAPH_RAG=true`)
- **WebSocket streaming** with source citations; Qdrant in prod, Chroma in dev, pgvector available via env
- **ML forecasting** with Monte Carlo confidence bands; four-method anomaly detection; board-ready PDF export
- **LiteLLM multi-provider router** — Groq LLaMA 3.3 70B (default/speed), Claude Sonnet 4.6 (reasoning), Claude Haiku 4.5 (judge), Ollama (local)
- **Tavily web search** with cited sources (real-time data for the copilot)
- **JWT + RBAC**, bilingual EN/FR React frontend (Recharts), 7 benchmarking scenarios
- **74 endpoints**, **157 tests**, AGPL-3.0

```bash
pip install intelai  # v0.1.2
```
also: `pip install omnismart-personas` — v0.1.3 — standalone persona templates for LangChain RAG projects

`FastAPI` `LangChain` `ChromaDB` `Qdrant` `pgvector` `PostgreSQL` `React` `Groq` `Claude` `LiteLLM` `Docker`

---
 
### [AgentKit](https://github.com/Yacine-ai-tech/AgentKit) — MCP Server for Business Intelligence Agents

Six MCP tools that give Claude Desktop, Cursor, or any LangGraph agent direct access to live business data.

- **6 MCP Tools:** `query_kpis`, `get_company_health`, `detect_kpi_anomalies`, `forecast_metric`, `list_available_metrics`, `get_executive_summary`
- **6 MCP Resources** (stable data URIs: `kpi://Finance/latest`, Growth, Operations, People, ESG, IT_Ops)
- **1 reusable Prompt** — `monthly_executive_briefing`
- **3-agent LangGraph workflow** — Planner (Claude Sonnet 4.6) → Analyst (Groq LLaMA 3.3) → Reporter (Claude Sonnet 4.6)
- Separate working demos for **Claude Agent SDK**, **CrewAI**, and **DSPy**
- **34 tests**, AGPL-3.0

```bash
pip install agentkit-mcp  # v0.1.4
agentkit-mcp              # CLI entrypoint → starts the MCP server
```

`FastMCP` `LangGraph` `Claude Sonnet 4.6` `Groq` `PostgreSQL` `LiteLLM`

---
 
### [DocIntel](https://github.com/Yacine-ai-tech/DocIntel) — Vision-First Document Intelligence

Extracts structured data from PDFs and images using vision models — not just OCR.

- **Route A:** Claude Sonnet 4.6 Vision — complex layouts, handwriting, mixed languages
- **Route B:** Ollama local vision (`.env` default: `llama3.2-vision`; production-validated: `qwen2.5-VL:7b` on NVIDIA T4) — fully local, zero cost per page
- **Route C:** Tesseract + Claude Haiku LLM cleanup — lightweight fallback for clean scans
- **Multi-currency & multi-locale** — 45+ currencies (USD, EUR, GBP, JPY, INR, CNY, XOF/FCFA) normalized to ISO 4217 + float; dates to ISO 8601
- **Multi-page map-reduce** — handles 100+ page PDFs via concurrent chunk extraction and merge (MAX_PDF_PAGES default: 200)
- **`/classify-image`** — vision-first object classification (category + confidence + reasoning)
- **550-document benchmark** (500 with field-level ground truth):

| Route | Model | Test set | Accuracy |
|-------|-------|----------|----------|
| A — vision_premium | Claude Sonnet 4.6 Vision | multilingual invoices | **100%** |
| A — vision_premium | Claude Sonnet 4.6 Vision | CORD phone-photo receipts (40) | **92.5%** |
| A — vision_premium | Claude Sonnet 4.6 Vision | SROIE world-standard | **95%** |
| B — vision_local | Ollama qwen2.5-VL 7B (T4) | CORD phone-photo receipts (100) | **77%** |
| B — vision_local | Ollama qwen2.5-VL 7B (T4) | French + FCFA (XOF) sample | **100%** |
| C — ocr_fallback | Tesseract + Claude Haiku | clean invoices | **100%** |
| C — ocr_fallback | Tesseract + Claude Haiku | CORD receipts | **28.5%** |

- **15 endpoints**, **62 tests**, AGPL-3.0

`FastAPI` `LiteLLM` `Claude Vision` `Ollama` `Tesseract` `pdfplumber` `Docker`

---
 
### [VoiceFlow](https://github.com/Yacine-ai-tech/VoiceFlow) — Speech to Structured Intelligence

Record audio in the browser, get structured output — not just a transcript.

- **5 analysis types** with per-type LLM routing:
  - `meeting` → Groq LLaMA 3.3 · `sales_call` → Claude Sonnet 4.6 · `support_call` → Claude Haiku 4.5 · `interview` → Claude Sonnet 4.6 · `general` → Groq LLaMA 3.3
- **4 transcription providers:** WhisperX (local default) · Groq Whisper · Deepgram · AssemblyAI
- **Diarization fallback chain:** pyannote 3.x → NeMo → no-diarization
- **Real-time voice agent** via OpenAI Realtime API; when only `GEMINI_API_KEY` is set, routes to **Gemini Multimodal Live** automatically (translation layer in api.py:338)
- **13 endpoints**, **38 tests**, AGPL-3.0

`FastAPI` `WhisperX` `Groq` `Claude` `LiteLLM` `edge-tts` `Docker`

---
 

### [RAGeval](https://github.com/Yacine-ai-tech/RAGeval) — Self-Hosted LLMOps Observability

```python
from rageval import track

@track(project="my_rag_app")
async def answer(question): ...
# That is the entire integration.
```

```bash
pip install omnismart-rageval          # core
pip install "omnismart-rageval[eval]"  # + multi-judge scoring and embeddings
pip install "omnismart-rageval[all]"   # everything
rageval init && rageval serve --port 8003
```

- **5 scoring dimensions:** retrieval relevance · groundedness · faithfulness · cost · latency
- **Multi-judge consensus** — Claude Haiku 4.5 + Groq LLaMA 3.3 + GPT-5-mini; disagreement triggers human-review flag
- **Persona-aware:** catches when a CFO response pulls data outside its Finance scope
- **SQLite by default** — zero infrastructure. Postgres + pgvector optional. OpenTelemetry export.
- **12 endpoints**, **38 tests**, AGPL-3.0

`FastAPI` `sentence-transformers` `LiteLLM` `SQLite/Postgres` `OpenTelemetry` `React`

---
 
### [StreamPulse](https://github.com/Yacine-ai-tech/StreamPulse) — Real-Time Data Pipeline

Multi-source ingestion with domain auto-classification and a live classified dashboard.

- **6 source types:** JSON, CSV, Gmail email, webhooks (HMAC-verified), Google Sheets, custom n8n nodes
- **Hybrid classifier:** keyword fast-path (zero cost) → BGE embedding fallback → Claude Haiku zero-shot
- **`/webhook/{source}/with-vision`** — composes with DocIntel `/classify-image` for auction/inventory aggregation
- **First-class n8n integration:** custom node template + 3 importable workflows (`auction_aggregator`, `invoice_intake`, `crm_sync`)
- **Prefect 3 orchestration** for retried, scheduled runs · **dlt declarative sources** for Gmail/Sheets/webhook
- Live dashboard via WebSocket + SSE · SQLite or Postgres store
- **12 endpoints**, **35 tests**, AGPL-3.0

`FastAPI` `PostgreSQL` `pgvector` `DuckDB` `React` `n8n` `Prefect 3` `LiteLLM`

---
 
## PyPI Packages

| Package | Install | Version | What it is |
|---------|---------|---------|------------|
| [omnismart-rageval](https://pypi.org/project/omnismart-rageval/) | `pip install omnismart-rageval` | **v0.1.10** | Drop-in LLMOps observability for RAG systems |
| [omnismart-personas](https://pypi.org/project/omnismart-personas/) | `pip install omnismart-personas` | **v0.1.3** | Persona templates for LangChain RAG projects |
| [agentkit-mcp](https://pypi.org/project/agentkit-mcp/) | `pip install agentkit-mcp` | **v0.1.4** | MCP server for business intelligence agents |
| [intelai](https://pypi.org/project/intelai/) | `pip install intelai` | **v0.1.2** | Persona-aware AI analytics backend |

---

## Stack

```
LiteLLM             Multi-provider LLM router (no vendor lock-in)
Claude Sonnet 4.6   Reasoning tier (executive personas, deep analysis, sales call)
Claude Haiku 4.5    Judge tier (classification, scoring, support)
Groq LLaMA 3.3 70B  Speed tier (high-volume RAG, meeting notes, general)
Ollama              Local tier (Llama 3.3, Qwen2.5-VL 7B, Llama 3.2 Vision)
OpenAI              Voice agent (VoiceFlow /realtime) + RAGeval 3rd judge (gpt-5-mini)
Gemini              VoiceFlow /realtime fallback when only GEMINI_API_KEY is set
BGE-large-en-v1.5   Dense embeddings
BGE Reranker v2-m3  Cross-encoder reranking
BM25 + RRF          Sparse retrieval + fusion
FastAPI + Uvicorn   API layer across all 6 projects
PostgreSQL + pgvector  Production data store
Qdrant              Vector store in prod (Chroma in dev)
LangGraph           Multi-agent workflows (AgentKit)
FastMCP             MCP server framework (AgentKit)
React + Recharts    Frontends (all 6 have a live dashboard at /)
Docker              Containerized deployment
WhisperX            Local speech transcription (VoiceFlow)
Tesseract           OCR fallback (DocIntel)
Prefect 3           Pipeline orchestration (StreamPulse)
dlt                 Declarative sources (StreamPulse)
PyTorch             Sentence-transformers backend
OpenTelemetry       Observability export (RAGeval)
Tavily              Real-time web search with citations (IntelAI)
```
 
 ## Background

- **Software Engineer** — HyperTech Niger (2025): Designed and deployed full-stack AI and IoT systems, including an ML-driven smart irrigation engine and an energy management platform.
- **B.Sc. Artificial Intelligence** — African Development University (2022–2025)
- **Associate Data Scientist** — Qwasar Silicon Valley (2023–2024), trained to SV standards across 57 projects
- IBM certifications: Full Stack Developer · AI Engineering · RAG & Agentic AI · Data Science
- Languages: **French** (native) · **English** (fluent) · 🇳🇪 Zarma / 🇳🇪 Hausa (native)

## Contact

- **Upwork:** [Hire me](https://www.upwork.com/freelancers/yacineseybousiddoai)
- **LinkedIn:** [Yacine Seybou Siddo](https://www.linkedin.com/in/yacineseybousiddoai/)
- **Email:** [contact@ysiddo-ai-projects.app](mailto:contact@ysiddo-ai-projects.app)

## 🎓 Certifications
 
| Certificate | Provider | Verify |
|-------------|----------|--------|
| IBM AI Engineering Professional Certificate (V3) | IBM | [↗](https://www.coursera.org/account/accomplishments/specialization/9285T5IRZNGO) |
| IBM RAG and Agentic AI Professional Certificate | IBM | [↗](https://www.coursera.org/account/accomplishments/specialization/OV82XYPSA6Y3) |
| IBM Full Stack Software Developer Professional Certificate (V5) | IBM | [↗](https://www.coursera.org/account/accomplishments/specialization/KFQC99T229SZ) |
| IBM Data Science Professional Certificate (V3) | IBM | [↗](https://www.coursera.org/account/accomplishments/specialization/9RKBFDZQEH2F) |
| IBM Data Science Professional Certificate | IBM | [↗](https://www.coursera.org/account/accomplishments/specialization/A3QFEHLGTSJK) |
| Associate Data Scientist (57 projects) | Qwasar Silicon Valley | [↗](https://upskill.us.qwasar.io/certificates/MTM1Mi1zZXlib3Utc195LWp1bC0yMDIxLTMwLTVlYWU=) |
| Mathematics for Machine Learning and Data Science | DeepLearning.AI | [↗](https://coursera.org/share/74c82eeef8eee1add248694b39dea49d) |
 
---
 
<div align="center">
Open to freelance projects · Available for short-term and ongoing engagements
 
[![Upwork](https://img.shields.io/badge/Hire%20me%20on-Upwork-6FDA44?style=for-the-badge&logo=upwork&logoColor=white)](https://www.upwork.com/freelancers/yacineseybousiddoai)
 
</div>
