# Hi, I'm Yacine Seybou Siddo

**AI Systems Engineer | RAG · MCP Agents · Document AI · LLMOps · FastAPI**
Based in Niamey, Niger · Bilingual EN/FR

**Hire me on Upwork:** [upwork.com/freelancers/yacineseybousiddoai](https://www.upwork.com/freelancers/yacineseybousiddoai)

---

## What I build

Production AI systems. The kind that get deployed, stay deployed, and solve
a specific problem well.

This year I shipped six tools from a single codebase. Each one is
standalone, open-source, and has a live demo.

---

## Projects

### [OmniIntelOS](https://github.com/Yacine-ai-tech/omniintelos) — AI Analytics Platform with Persona-Aware RAG

The core idea: different executives need different answers from the same
data. A CFO asking about margins should get a Finance-scoped response with
financial-domain context. A CHRO asking about turnover should get a
People-scoped response. Same system, nine different lenses.

Built with 60 FastAPI endpoints, ChromaDB RAG with source citations,
WebSocket streaming chat, ML forecasting with Monte Carlo confidence bands,
four-method anomaly detection, JWT + RBAC, and a bilingual EN/FR React
frontend.

`FastAPI` `LangChain` `ChromaDB` `PostgreSQL` `React` `Groq` `Claude` `Docker`

---

### [AgentKit](https://github.com/Yacine-ai-tech/agentkit) — MCP Server for Business Intelligence Agents

Six MCP tools that give Claude Desktop, Cursor, or any LangGraph agent
access to live business data: query KPIs, get health score, detect
anomalies, forecast metrics, list available data, get executive summary.
Also exposes MCP Resources and reusable Prompts.

Comes with a three-agent LangGraph workflow (Planner → Analyst → Reporter)
for autonomous analysis. Separate demos for Claude Agent SDK, CrewAI,
and DSPy.

`FastMCP` `LangGraph` `Claude Sonnet 4.6` `Groq` `PostgreSQL` `LiteLLM`

---

### [DocIntel](https://github.com/Yacine-ai-tech/docintel) — Vision-First Document Intelligence

Three extraction routes: Claude Sonnet 4.6 Vision for complex layouts,
Ollama + Llama 3.2 Vision for local deployments, Tesseract as fallback.
The `/classify-image` endpoint classifies what's in a photo — category +
confidence + reasoning — useful for invoice processing to auction-listing
aggregators.

85%+ field accuracy on a 50-document evaluation set. Async batch
processing. Drag-and-drop demo UI.

`FastAPI` `LiteLLM` `Claude Vision` `Ollama` `Tesseract` `pdfplumber` `Docker`

---

### [VoiceFlow](https://github.com/Yacine-ai-tech/voiceflow) — Speech to Structured Intelligence

Record audio in the browser, get structured output. Meeting mode returns
action items with owner, deadline, and priority. Sales call mode returns
deal stage, pain points, objections, buying signals, and a CRM-paste-ready
note.

Routes to Claude Sonnet 4.6 for sales calls where nuance matters, and
Groq LLaMA 3.3 for meeting notes where speed matters. Supports WhisperX,
Groq Whisper, Deepgram, and AssemblyAI for transcription.

`FastAPI` `WhisperX` `Groq` `Claude` `LiteLLM` `edge-tts` `Docker`

---

### [RAGeval](https://github.com/Yacine-ai-tech/rageval) — Self-Hosted LLMOps Observability

```python
from rageval import track

@track(project="my_rag_app")
async def answer(question): ...
# That's the entire integration.
```

Scores every query: retrieval relevance, groundedness via multi-judge
consensus (Claude Haiku + Groq + GPT), faithfulness, cost per query,
latency. Persona-aware — catches when a response pulls data outside its
expected role scope. SQLite default, Postgres optional, OpenTelemetry
export for enterprise stacks.

```
pip install rageval
```

`FastAPI` `sentence-transformers` `LiteLLM` `SQLite/Postgres` `OpenTelemetry` `React`

---

### [StreamPulse](https://github.com/Yacine-ai-tech/streampulse) — Real-Time Data Pipeline

Ingests from webhooks, Gmail, Google Sheets, CSV, REST APIs. Classifies
each record by business domain using a hybrid classifier: keyword fast
path first, BGE embedding fallback, Claude Haiku as last resort. Live
WebSocket dashboard updates in real time.

First-class n8n integration — custom node template plus three importable
workflows. Composes with DocIntel via `/webhook/.../with-vision` for
image-bearing payloads.

`FastAPI` `PostgreSQL` `pgvector` `DuckDB` `React` `n8n` `Prefect 3` `LiteLLM`

---

## Stack

Here's what I work with across these projects:

```
LLMs          Claude Sonnet 4.6 · Claude Haiku 4.5 · GPT-4o / GPT-5 · Gemini 2.5 Pro
              Groq LLaMA 3.3 · DeepSeek V3 · AWS Bedrock · Ollama (local)
Abstraction   LiteLLM — every project routes across providers via a single
              env var, so you're never locked into one vendor
Frameworks    FastAPI · LangChain · LangGraph · FastMCP
Embeddings    BGE-large-en-v1.5 · all-MiniLM-L6-v2
Vector        ChromaDB (dev) · Qdrant / pgvector (prod)
Frontend      React · Recharts · Vite
Storage       PostgreSQL · SQLite · DuckDB
Pipelines     n8n · Prefect 3 · dlt
Monitoring    Prometheus · Grafana · OpenTelemetry
Speech        faster-whisper · WhisperX · Deepgram · AssemblyAI
DevOps        Docker · Railway · Fly.io · GitHub Actions · AWS
```

---

## Published packages

- [`rageval`](https://pypi.org/project/rageval/) — LLMOps observability for RAG systems
- [`omnismart-personas`](https://pypi.org/project/omnismart-personas/) — drop-in 9-persona templates for LangChain RAG

---

## Certifications

- IBM AI Engineering Professional Certificate (V3)
- IBM RAG and Agentic AI Professional Certificate
- IBM Full Stack Software Developer Professional Certificate (V5)
- IBM Data Science Professional Certificate (V3)
- Associate Data Scientist — Qwasar Silicon Valley (57 projects)
- Mathematics for Machine Learning and Data Science — DeepLearning.AI

---

## Experience

**AI Systems Engineer — Self-Employed** · Jan 2026 – Present
Building and shipping production AI systems independently. Six open-source
tools released in 2026 — each with a live demo, GitHub repo, and real
deployment.

**Software Engineer (AI & Full Stack) — HyperTech Niger** · Jul – Dec 2025
AgriDrop: designed and built an IoT + ML smart irrigation system from
scratch — sensor data ingestion, weather API integration, ML scheduling
engine. Fully deployed.
Addax SME: supervised and mentored an intern through the full delivery of
an energy management platform, then personally owned the AI layer —
forecasting, cost optimization, and policy-compliance modules. Fully
deployed.

**Intern Software Engineer — HyperTech Niger** · Apr – Jun 2025
Delivered a full-stack web application. Retained and promoted to full
engineer at the end of the internship.

**Network & Sysadmin Intern — ADU Digital Transformation Dept** · May – Sep 2024
Built and deployed the Ilimi App — a QR-based event ticketing platform
(React + Express.js, MySQL) for TEDx ADU. Also supported AI adoption
initiatives across the department.

**Data Science Program — Qwasar Silicon Valley** · Jan 2023 – Aug 2024
Completed 57 projects across the data science and engineering stack,
working to Silicon Valley standards in a fully project-based program.
Covered: data cleaning, scraping, visualization, SQL, Python (Pandas,
NumPy, Matplotlib, Seaborn, Jupyter), regression models, ML with Keras /
TensorFlow / Scikit-learn, data structures and algorithms, NLP (N-gram,
RNN, CNN, SpaCy, NER), fraud detection, SMOTE and ADASYN.
Earned the Associate Data Scientist certificate upon completing that
milestone in the program.

---

## Languages

French (native) · English (fluent) · Zarma (native) · Hausa (native)

