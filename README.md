<div align="center">
 # Yacine Seybou Siddo
 
**AI Systems Engineer**
 
`RAG` `MCP Agents` `Document AI` `LLMOps` `FastAPI`
 
🌍 Niamey, Niger &nbsp;·&nbsp; 🇫🇷 FR &nbsp;·&nbsp; 🇺🇸 EN &nbsp;·&nbsp; [![Upwork](https://img.shields.io/badge/Hire%20me%20on-Upwork-6FDA44?style=flat&logo=upwork&logoColor=white)](https://www.upwork.com/freelancers/yacineseybousiddoai)
 
</div>
 
I build production AI systems — the kind that get deployed, stay deployed, and solve a specific problem well.
 
This year I shipped six standalone tools from a single codebase. Each one is open-source and has a live demo.
 
 
## 🚀 Projects
 
### [IntelAI](https://github.com/Yacine-ai-tech/IntelAI) — Persona-Aware AI Analytics & RAG Copilot
 
The core idea: different executives need different answers from the same data. A CFO asking about margins gets a Finance-scoped response. A CHRO asking about turnover gets a People-scoped one. Same system, nine different lenses — the scope boundaries are enforced by architecture, not just prompt engineering.
 
A self-contained, cloud-deployable product. No dependency on the full platform — single app (Railway API + Vercel frontend), managed Postgres (Neon).
 
- **9 C-suite AI personas** — each with its own system prompt, data scope, and tool whitelist
- **7 KPI domains** — Finance, HR, IT, Ops, Logistics, ESG, Risk — dashboard, analytics, forecasting, and anomaly detection per domain
- **GraphRAG-lite + hybrid retrieval + BGE reranker** — the differentiator; better cross-entity answer quality than flat vector search
- **WebSocket streaming** with source citations; **Qdrant** vector store in prod, **Chroma** in dev (swap via VECTOR_STORE); **Postgres** on Neon for relational data; **pgvector** available via env
- **ML forecasting** with Monte Carlo confidence bands, four-method anomaly detection, board-ready PDF export
- **LiteLLM multi-provider router** — swap models via a single env var, no vendor lock-in
- **JWT + RBAC**, bilingual EN/FR React frontend with Recharts visualizations
- `omnismart-personas` extracted as a standalone PyPI package — reusable in any LangChain RAG project
`FastAPI` `LangChain` `ChromaDB` `pgvector` `PostgreSQL` `React` `Groq` `Claude` `LiteLLM` `Docker`
 
---
 
### [AgentKit](https://github.com/Yacine-ai-tech/agentkit) — MCP Server for Business Intelligence Agents
 
Six MCP tools that give Claude Desktop, Cursor, or any LangGraph agent direct access to live business data.
 
- **Tools:** query KPIs, company health score, anomaly detection, metric forecasting, data inventory, executive summary
- **MCP Resources** (stable data URIs) + **Prompts** (reusable templates)
- **3-agent LangGraph workflow** — Planner (Claude Sonnet 4.6) → Analyst (Groq) → Reporter (Claude Sonnet 4.6)
- Separate demos for **Claude Agent SDK**, **CrewAI**, and **DSPy**
`FastMCP` `LangGraph` `Claude Sonnet 4.6` `Groq` `PostgreSQL` `LiteLLM`
 
---
 
### [DocIntel](https://github.com/Yacine-ai-tech/docintel) — Vision-First Document Intelligence
 
Extracts structured data from PDFs and images using vision models — not just OCR.
 
- **Route A:** Claude Sonnet 4.6 Vision — complex layouts, handwriting, mixed languages
- **Route B:** Ollama local vision (Qwen2.5-VL, validated on GPU; model swappable via env) — fully local, $0/page
- **Route C:** Tesseract — lightweight fallback for clean scans
- **`/classify-image`** — tells you what's in a photo (category + confidence + reasoning), built for auction-listing aggregators and inventory systems
- **Released 550-document benchmark** — Route A: 100% on multilingual multi-page invoices, 92.5% on phone-photo receipts; SROIE (world-standard) 95% zero-shot · async batch · drag-and-drop UI
`FastAPI` `LiteLLM` `Claude Vision` `Ollama` `Tesseract` `pdfplumber` `Docker`
 
---
 
### [VoiceFlow](https://github.com/Yacine-ai-tech/voiceflow) — Speech to Structured Intelligence
 
Record audio in the browser, get structured output — not just a transcript.
 
- **Meeting mode** → action items with owner, deadline, and priority
- **Sales call mode** → deal stage, pain points, objections, buying signals, CRM-paste-ready note
- Routes to **Claude Sonnet 4.6** for sales calls (nuance matters) and **Groq LLaMA 3.3** for meeting notes (speed matters)
- Transcription providers: WhisperX · Groq Whisper · Deepgram · AssemblyAI
- **Real-time voice agent** demo via OpenAI Realtime API
`FastAPI` `WhisperX` `Groq` `Claude` `LiteLLM` `edge-tts` `Docker`
 
---
 
### [RAGeval](https://github.com/Yacine-ai-tech/rageval) — Self-Hosted LLMOps Observability
 
```python
from rageval import track
 
@track(project="my_rag_app")
async def answer(question): ...
# That's the entire integration.
```
 
```bash
pip install omnismart-rageval     # distribution name; import is `from rageval import track`
```
 
- **5 scoring dimensions:** retrieval relevance · groundedness · faithfulness · cost · latency
- **Multi-judge consensus** across Claude Haiku + Groq + GPT — disagreement triggers a human-review flag
- **Persona-aware:** catches when a CFO response pulls data outside its Finance scope
- **SQLite by default** — zero infrastructure. Postgres + pgvector optional. OpenTelemetry export included.
- Browser dashboard (`/demo/`) · PyPI published
`FastAPI` `sentence-transformers` `LiteLLM` `SQLite/Postgres` `OpenTelemetry` `React`
 
---
 
### [StreamPulse](https://github.com/Yacine-ai-tech/streampulse) — Real-Time Data Pipeline
 
Multi-source ingestion with a live WebSocket dashboard that updates as records arrive.
 
- **Sources:** webhooks · Gmail · Google Sheets · CSV · REST APIs
- **Hybrid classifier:** keyword fast path → BGE embedding fallback → Claude Haiku last resort
- **First-class n8n integration** — custom node template + 3 importable workflows (auction aggregation, invoice intake, CRM sync)
- **`/webhook/.../with-vision`** composes with DocIntel for image-bearing payloads
`FastAPI` `PostgreSQL` `pgvector` `DuckDB` `React` `n8n` `Prefect 3` `LiteLLM`
 
---
 
## 🏗 Platform
 
### [OmniIntelOS](https://github.com/Yacine-ai-tech/OmniIntelOS) — Full-Stack AI Company Intelligence Platform *(private repo)*
 
The complete, self-hostable version — all six tools under one roof, plus the infrastructure layer organizations need to run everything on their own servers. Think of it as IntelAI with the ceiling removed.
 
- **Everything in IntelAI** — all 9 personas, GraphRAG-lite, hybrid retrieval, BGE reranker, ML forecasting, anomaly detection, RBAC, bilingual frontend
- **Monitoring stack** — Prometheus, Grafana, pre-configured alert rules, nginx reverse proxy, Cloudflare tunnels, MonitoringPage
- **OCR microservice** (`omnitel-ocr`) — DocIntel extracted as a standalone service with its own API and ScannerPage
- **Voice microservice** (`omnitel-voice`) — VoiceFlow extracted as a standalone service with VoicePage
- **n8n workflow automation** — IntegrationsPage, N8NWorkflowPage, custom node template, 3 importable workflows
- **Multi-service Docker Compose** — full on-prem deployment with all services orchestrated
- **BulkData / DataHub ingestion** — heavy-volume enterprise data pipeline layer
Available as a [Project Catalog engagement on Upwork](https://www.upwork.com/freelancers/yacineseybousiddoai) — scoped, priced, and ready to deploy.
 
`FastAPI` `LangChain` `ChromaDB` `pgvector` `React` `Prometheus` `Grafana` `n8n` `Prefect 3` `Docker Compose` `Nginx` `LiteLLM`
 
---
 
## 🛠 Stack
 
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
 
## 📦 Published Packages
 
| Package | Description |
|---------|-------------|
| [`omnismart-rageval`](https://pypi.org/project/omnismart-rageval/) | Self-hosted LLMOps observability for RAG systems (import: `rageval`) |
| [`omnismart-personas`](https://pypi.org/project/omnismart-personas/) | Drop-in 9-persona templates for LangChain RAG |
 
---
 
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
 
## 💼 Experience
 
**AI Systems Engineer — Self-Employed** · Jan 2026 – Present
> Building and shipping production AI systems independently. Six open-source tools released in 2026 — IntelAI, AgentKit, DocIntel, VoiceFlow, RAGeval, StreamPulse — each with a live demo, GitHub repo, and real deployment. OmniIntelOS (the full platform) developed in parallel as a private enterprise engagement. Client work includes HyperTech Electronics — a live omni-channel commerce platform with a full AI layer (RAG chatbot, semantic search, recommendations) built on Groq + local embeddings, alongside 73 DB tables, ~390 API endpoints, and B2B + POS integration.
 
**Software Engineer (AI & Full Stack) — HyperTech Niger** · Jul – Dec 2025
> AgriDrop: designed and built an IoT + ML smart irrigation system from scratch — sensor data ingestion, weather API integration, ML scheduling engine. Fully deployed.
>
> Addax SME: supervised and mentored an intern through the full delivery of an energy management platform, then personally owned the AI layer — forecasting, cost optimization, and policy-compliance modules. Fully deployed.
 
**Intern Software Engineer — HyperTech Niger** · Apr – Jun 2025
> Delivered a full-stack web application. Retained and promoted to full engineer at the end of the internship.
 
**Network & Sysadmin Intern — ADU Digital Transformation Dept** · May – Sep 2024
> Built and deployed the Ilimi App — a QR-based event ticketing platform (React + Express.js, MySQL) for TEDx ADU. Also supported AI adoption initiatives across the department.
 
**Data Science Program — Qwasar Silicon Valley** · Jan 2023 – Aug 2024
> Fully project-based program at Silicon Valley standards — 57 projects with peer review and auto-grading. Covered: data cleaning, scraping, visualization, SQL, Python (Pandas, NumPy, Matplotlib, Seaborn, Jupyter), regression models, ML with Keras / TensorFlow / Scikit-learn, data structures and algorithms, NLP (N-gram, RNN, CNN, SpaCy, NER), fraud detection, SMOTE and ADASYN. Earned the Associate Data Scientist certificate upon completing that milestone in the program.
 
---
 
## 🌐 Languages
 
🇫🇷 French (native) &nbsp;·&nbsp; 🇺🇸 English (fluent) &nbsp;·&nbsp; Zarma (native) &nbsp;·&nbsp; Hausa (native)
 
---
 
<div align="center">
Open to freelance projects · Available for short-term and ongoing engagements
 
[![Upwork](https://img.shields.io/badge/Hire%20me%20on-Upwork-6FDA44?style=for-the-badge&logo=upwork&logoColor=white)](https://www.upwork.com/freelancers/yacineseybousiddoai)
 
</div>
