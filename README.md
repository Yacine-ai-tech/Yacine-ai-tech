# Yaçine Seybou Siddo

![License: AGPL v3](https://img.shields.io/badge/license-AGPL--3.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat&logo=langgraph&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)

**AI Systems Engineer · B.Sc. Artificial Intelligence · Niamey, Niger**

I build AI systems that ship, and I publish what I find — including the results that don't flatter the system. My work spans production AI engineering for clients in Niger, six open-source AI/ML tools, and Cibiyar Karatu, an adaptive learning platform for Niger and the Sahel.

Email: contact@yacineseybousiddo.me · [LinkedIn](https://linkedin.com/in/yacineseybousiddoai) · [Portfolio](https://yacineseybousiddo.me)
Location: Niamey, Niger · Languages: French, English, Hausa, Zarma

---

## Contents

- [What I Do](#what-i-do)
- [Background](#background)
- [Open-Source Ecosystem](#open-source-ecosystem--6-tools-2026-dual-licensed-agpl-30--commercial)
- [Results at a Glance](#results-at-a-glance)
- [Client Work](#client-work-scoped-to-whats-publicly-shareable)
- [Research Direction](#research-direction)

---

## What I Do

I work across three registers, and I try not to blur them.

**AI systems engineering.** Production RAG, multi-agent orchestration, document intelligence, LLMOps, and edge/IoT platforms, delivered as a freelance engineer for clients in Niger — engineered against Sahel-wide infrastructure constraints (intermittent connectivity, shared NAT, low-end hardware), not yet delivered outside Niger.

**Open-source research tooling.** Six standalone AI/ML tools, dual-licensed (AGPL-3.0 / commercial), each shipped with a public evaluation protocol rather than a marketing claim.

**Adaptive learning platform.** *Cibiyar Karatu*, subject-agnostic and offline-first, for Niger and the Sahel — French alongside Hausa, Zarma, and Fulfulde — plus a parallel research contribution in corpus and benchmark work for those three languages, at very different starting points of existing NLP coverage.

## Background

**Education**
- B.Sc., Artificial Intelligence — African Development Universalis, Niamey (2022–2025), average 15.80/20. Coursework: mathematics for AI, algorithms, ML/DL, NLP, computer vision, databases, systems and networks.
- Associate Data Scientist Program — Qwasar Silicon Valley (2023–2024), 57 project-based assignments evaluated through automated grading and peer review, fully in English.

**Certifications** — IBM Full Stack Software Developer · IBM RAG and Agentic AI · IBM AI Engineering · IBM Data Science Professional (all 2025) · Mathematics for Machine Learning and Data Science, DeepLearning.AI (2023). Full list of 19 on the [portfolio](https://yacineseybousiddo.me).

**Teaching** — Instructor, *Introduction to Artificial Intelligence*, A.D.U. (2025) · workshop lead, Git/GitHub, Tech Communities Club A.D.U. · trainer, "Master AI Tools" workshop.

## Open-Source Ecosystem — 6 tools, 2026, dual-licensed (AGPL-3.0 / commercial)

Each tool ships with a `BENCHMARK.md` and a `RESEARCH.md` in its repository — the evaluation protocol and the raw numbers, favorable and unfavorable both. Summaries below; the repos are the source of truth.

### [IntelAI](https://github.com/Yacine-ai-tech/intelai) — Persona-Aware Enterprise Analytics & RAG Copilot
[![PyPI](https://img.shields.io/pypi/v/intelai?label=intelai&color=blue)](https://pypi.org/project/intelai/) [![PyPI](https://img.shields.io/pypi/v/omnismart-personas?label=omnismart-personas&color=blue)](https://pypi.org/project/omnismart-personas/)
[![Live App](https://img.shields.io/badge/Live_App-intelai-0070f3?style=flat)](https://intelai.ysiddo-ai-projects.app) [![Research](https://img.shields.io/badge/Research-Empirical_Methods-8a2be2?style=flat)](https://intelai.ysiddo-ai-projects.app/research) [![Benchmarks](https://img.shields.io/badge/Benchmarks-Backtest_4.64%25-green?style=flat)](https://intelai.ysiddo-ai-projects.app/benchmark) [![Guide](https://img.shields.io/badge/Docs-User_Guide-blue?style=flat)](https://intelai.ysiddo-ai-projects.app/guide)

Nine C-suite personas (CEO, CFO, CTO, COO, CHRO, ESG, Risk, Analyst, General), each scoped to its own data domain by architecture, not prompt instruction. 146 curated KPIs across 9 domains, 78-month history (2020-01 to 2026-06). Hybrid retrieval (BGE-M3 dense 1024-dim + BM25 sparse + RRF fusion + BAAI/bge-reranker-v2-m3 cross-encoder reranking) with 100% live Qdrant precision, plus GraphRAG-lite multi-hop entity traversal and prompt caching with dynamic recency cutoff (June 2026).

Measured results: out-of-sample backtest on 444 forecasts across 6 core metrics, Mean APE 4.64% (median 2.77%, down from 12.48% baseline without auto-selection); GraphRAG-lite reaches 100.0% entity extraction coverage (7,878/7,878 rows across all 7 operational domains) with 8/8 multi-hop queries verified; live production RAG scores 71.4% ground-truth accuracy across 50 verified cases; prompt-cached responses cite verified sources with inline bracketed numbers [1]. Published alongside those numbers: bilingual grounding parity is monitored across French and English with strict adherence to the verified reporting horizon.

### [DocIntel](https://github.com/Yacine-ai-tech/docintel) — Vision-First Document Intelligence
[![Live App](https://img.shields.io/badge/Live_App-docintel-0070f3?style=flat)](https://docintel.ysiddo-ai-projects.app) [![Research](https://img.shields.io/badge/Research-Tri--Route_Topology-8a2be2?style=flat)](https://docintel.ysiddo-ai-projects.app/research) [![Benchmarks](https://img.shields.io/badge/Benchmarks-95.0%25_SROIE-green?style=flat)](https://docintel.ysiddo-ai-projects.app/benchmarks) [![Guide](https://img.shields.io/badge/Docs-User_Guide-blue?style=flat)](https://docintel.ysiddo-ai-projects.app/guide)

Extracts structured data from PDFs, images, and scanned files across three production routes: Route A (Frontier Multimodal Vision: Claude Sonnet 4.6 / Gemini 3.8 Flash Native Vision), Route B (Self-Hosted Vision Model via Ollama: Qwen 2.5-VL 7B with zero cloud API cost), and Route C (Layout-Aware Surya OCR on GPU with Tesseract CPU fallback + LLM structured cleanup). Deterministic currency normalization across 45+ currencies (including FCFA/XOF under UEMOA VAT convention) and ISO dates, with SHA-256 document deduplication and sub-second cached retrieval.

Measured results: 95.0% zero-shot accuracy on the public SROIE benchmark (57/60 receipts) and 100% on multilingual cloud-route invoices (Route A); 97.8% overall and 100% on French/FCFA sample (325/325 fields) on self-hosted Route B ($0 API cost); 96.3% field accuracy on Route C with Surya OCR + LLM cleanup; 650-document multi-format corpus processed at 100% throughput reliability (~1.1 docs/second).

### [RAGeval](https://github.com/Yacine-ai-tech/rageval) — Self-Hosted LLMOps Observability for RAG
[![PyPI](https://img.shields.io/pypi/v/omnismart-rageval?label=omnismart-rageval&color=blue)](https://pypi.org/project/omnismart-rageval/)
[![Live App](https://img.shields.io/badge/Live_App-rageval-0070f3?style=flat)](https://rageval.ysiddo-ai-projects.app) [![Research](https://img.shields.io/badge/Research-Heterogeneous_Panel-8a2be2?style=flat)](https://rageval.ysiddo-ai-projects.app/research) [![Benchmarks](https://img.shields.io/badge/Benchmarks-ROC--AUC_0.9191-green?style=flat)](https://rageval.ysiddo-ai-projects.app/benchmarks) [![Guide](https://img.shields.io/badge/Docs-User_Guide-blue?style=flat)](https://rageval.ysiddo-ai-projects.app/guide)

```python
from rageval import track

@track(project="my_rag_app")
async def answer(question): ...
```

Zero-credit symbolic evaluation combined with a heterogeneous 4-judge consensus panel (Groq Maverick 17B, Gemini 3.5 Flash, Claude Haiku, GPT-5-mini), rate-limiting, and persistent SQLite/PostgreSQL disk caching.

Measured results: folding the zero-credit symbolic judge (numeric consistency + lexical overlap) into the panel raises consensus ROC-AUC from 0.8709 to 0.9191 on HaluEval-QA (N=240); the 4-Judge Heterogeneous Consensus achieves 0.860 accuracy, 0.867 F1, and 0.902 ROC-AUC on HaluEval-QA (N=200). Panel disagreement standard deviation (0.217 on incorrect predictions vs 0.082 on correct ones) serves as an automated anomaly signal for human review.

### [AgentKit](https://github.com/Yacine-ai-tech/agentkit) — Governed MCP Tool Server
[![PyPI](https://img.shields.io/pypi/v/agentkit-mcp?label=agentkit-mcp&color=blue)](https://pypi.org/project/agentkit-mcp/)
[![Live App](https://img.shields.io/badge/Live_App-agentkit-0070f3?style=flat)](https://agentkit.ysiddo-ai-projects.app) [![Research](https://img.shields.io/badge/Research-Capability_Policy-8a2be2?style=flat)](https://agentkit.ysiddo-ai-projects.app/research) [![Benchmarks](https://img.shields.io/badge/Benchmarks-14%2F14_Guardrails-green?style=flat)](https://agentkit.ysiddo-ai-projects.app/benchmark) [![Guide](https://img.shields.io/badge/Docs-User_Guide-blue?style=flat)](https://agentkit.ysiddo-ai-projects.app/guide)

Gives Claude Desktop, Cursor, or any LangGraph agent governed access to live business data through the Model Context Protocol — typed tool effects (read/write/destructive), capability policies, and deterministic audit logging.

Measured results: DSPy BootstrapFewShot metric score compiled from 0.6800 → 0.7067 (30/30 held-out examples); live MCP tool-selection and execution achieves 12/12 (100%) accuracy across standardized business intelligence scenarios on a running FastMCP server; 14/14 adversarial guardrail tests pass deterministically offline; LangGraph autonomous multi-agent workflows execute at 43/43 (100%) success across all 10 domains.

### [StreamPulse](https://github.com/Yacine-ai-tech/streampulse) — Real-Time Business Data Pipeline
[![Live App](https://img.shields.io/badge/Live_App-streampulse-0070f3?style=flat)](https://streampulse.ysiddo-ai-projects.app) [![Research](https://img.shields.io/badge/Research-Cascade_Architecture-8a2be2?style=flat)](https://streampulse.ysiddo-ai-projects.app/research) [![Benchmarks](https://img.shields.io/badge/Benchmarks-Macro--F1_0.990-green?style=flat)](https://streampulse.ysiddo-ai-projects.app/benchmark) [![Guide](https://img.shields.io/badge/Docs-User_Guide-blue?style=flat)](https://streampulse.ysiddo-ai-projects.app/guide)

Multi-source ingestion (JSON, CSV, email, HMAC-verified webhooks, Google Sheets) with first-class n8n automation integration (custom node + 5 workflows) and a 3-tier hybrid classification cascade (regex/heuristics → semantic embeddings → LLM reasoning escalation).

Measured results: cascade accuracy reaches 99.0% (0.990 macro-F1, N=504 held-out SaaS telemetry events) across three stages; sustained multi-worker ingestion achieves 46.8 requests/second with a 0.00% error rate under burst load (89.1 req/s on 2-instance scaling); 100.0% HMAC-SHA256 signature verification (90/90 valid accepted, 10/10 invalid rejected at >100 req/s).

### [VoiceFlow](https://github.com/Yacine-ai-tech/voiceflow) — Speech to Structured Business Intelligence
[![Live App](https://img.shields.io/badge/Live_App-voiceflow-0070f3?style=flat)](https://voiceflow.ysiddo-ai-projects.app) [![Research](https://img.shields.io/badge/Research-Gemini_Live_Pipeline-8a2be2?style=flat)](https://voiceflow.ysiddo-ai-projects.app/research) [![Benchmarks](https://img.shields.io/badge/Benchmarks-WER_2.2%25-green?style=flat)](https://voiceflow.ysiddo-ai-projects.app/benchmark) [![Guide](https://img.shields.io/badge/Docs-User_Guide-blue?style=flat)](https://voiceflow.ysiddo-ai-projects.app/guide)

Routes recorded audio to per-analysis-type LLMs with a multi-provider transcription fallback chain (Groq Whisper, Deepgram, AssemblyAI, local WhisperX) and bidirectional real-time audio streaming via Gemini Live (gemini-2.5-flash-native-audio-preview-09-2025 with google-genai v1beta SDK, 24kHz → 16kHz downsampling, gated frame pipeline).

Measured results: 2.2% WER / 0.8% CER on LibriSpeech test-clean (Whisper large-v3 on T4 GPU, N=150; 6.4% on CPU); WebSocket connection latency averages 1.157s (all 25/25 under 1.8s) with 0.940s time-to-first-chunk; meeting intelligence achieves 92.4% action-item precision, 94.8% assignee identification, and 89.6% sentiment concordance; live 9-tool discovery and execution bridge to AgentKit.

## Results at a Glance

| Tool | Core measured result | Benchmark / protocol |
|---|---|---|
| [IntelAI](https://intelai.ysiddo-ai-projects.app) | Mean APE 4.64% (median 2.77%), 100.0% entity coverage, 71.4% RAG accuracy | Out-of-sample backtest (444 forecasts) & 50 production cases |
| [DocIntel](https://docintel.ysiddo-ai-projects.app) | 95.0% zero-shot (Route A), 97.8% self-hosted (Route B) | SROIE benchmark (57/60) & 106-doc Ollama evaluation |
| [RAGeval](https://rageval.ysiddo-ai-projects.app) | ROC-AUC 0.9191 (panel + symbolic), 0.860 4-judge accuracy | HaluEval-QA (N=240 / N=200), heterogeneous consensus |
| [AgentKit](https://agentkit.ysiddo-ai-projects.app) | 14/14 guardrails, 12/12 (100%) MCP routing, DSPy 0.7067 | Deterministic test suite & live FastMCP benchmark |
| [StreamPulse](https://streampulse.ysiddo-ai-projects.app) | 0.990 macro-F1 (99.0% accuracy), 46.8 req/s (0.00% errors) | N=504 SaaS telemetry suite & sustained burst test |
| [VoiceFlow](https://voiceflow.ysiddo-ai-projects.app) | 2.2% WER / 0.8% CER, 1.157s latency, 92.4% action item prec. | LibriSpeech test-clean (N=150) & Gemini Live turns |

## Client Work (scoped to what's publicly shareable)

**HyperTech Electronics** — AI layer for an e-commerce and retail-operations platform: bilingual semantic search, a  six-persona intent-routed assistant powered by Rag, two recommendation engines and a deterministic degraded-mode fallback built after a live provider-quota outage in production.

**HyperTech Connect** — Designed a zero-trust, protocol-agnostic IoT and edge-management platform for low-connectivity environments, with secure edge networking, multi-protocol device integration, and resilient OTA update capabilities. Validated the platform at 1,000+ devices under test and conducted physical validation on embedded hardware.

**HyperFlow** — built the software layer of the smart irrigation system, including data ingestion, analysis, recommendations, exporting, scheduling and control interfaces, and AI-based recommendations.

**Dermato Care** -
 **Offline-First Clinical Management:** Developed a cross-platform dermatology workstation that unifies patient records, consultations, appointments, inventory, and analytics for a specialist working across multiple institutions in Niger.

- **Privacy, Security & Resilience:** Engineered a privacy-by-design architecture with encrypted clinical records, secure phone-to-desktop transfers, verified portable backups, and database recovery—designed to operate without cloud dependency.

- **Responsible AI & Document Intelligence:** Implemented offline French document OCR with mandatory clinical review and an opt-in local AI framework featuring audit trails and fairness-gated training pipelines for dark-skin subgroups.

## Research Direction

*Cibiyar Karatu* ("Centre of Learning" in Hausa) is a subject-agnostic, offline-first adaptive learning platform for Niger and the Sahel, spanning formal, non-formal, and informal learning — French instruction alongside Hausa, Zarma, and Fulfulde, on entry-level Android hardware, with or without a network connection. Alongside the platform, it produces a parallel research contribution: corpus and benchmark work for Hausa, Zarma, and Fulfulde — three languages with wide disparity in existing NLP coverage despite their combined speaker count. Zarma and Fulfulde remain acutely under-resourced; Hausa, though still classified as low-resource, already has meaningful benchmark and corpus infrastructure this work builds on rather than starts from scratch. Currently in prototyping and testing, pre-incorporation; architecture and product design are not detailed publicly.

I'm also working toward graduate-level engineering training, aimed at closing the hardware and robotics gap my own software work keeps surfacing — physical AI: natural-scene computer vision, robotics, and embedded systems, beyond the document- and simulation-bound versions I've shipped so far.

---

Full evaluation protocols and results for each tool are documented in their respective repositories.
