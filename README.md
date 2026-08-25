# Yaçine Seybou Siddo

![License: AGPL v3](https://img.shields.io/badge/license-AGPL--3.0-blue.svg)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white)
![LangGraph](https://img.shields.io/badge/LangGraph-1C3C3C?style=flat&logo=langgraph&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat&logo=docker&logoColor=white)

**AI Systems Engineer · B.Sc. Artificial Intelligence · Niamey, Niger**

I build AI systems that ship, and I publish what I find — including the results that don't flatter the system. My work spans production AI engineering for clients in the Sahel, six open-source AI/ML tools, and applied research into low-resource African languages.

Email: contact@ysiddo-ai-projects.app · [LinkedIn](https://linkedin.com/in/yacineseybousiddoai) · [Portfolio](https://yacineseybousiddo.me)
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

**AI systems engineering.** Production RAG, multi-agent orchestration, document intelligence, LLMOps, and edge/IoT platforms, delivered as a freelance engineer for clients in Niger and the broader Sahel region.

**Open-source research tooling.** Six standalone AI/ML tools, dual-licensed (AGPL-3.0 / commercial), each shipped with a public evaluation protocol rather than a marketing claim.

**Applied research on low-resource languages.** Corpus aggregation and cataloging for Hausa, Zarma, and Fulfulde through an adaptive-learning platform currently in prototyping and real-user testing.

## Background

**Education**
- B.Sc., Artificial Intelligence — African Development Universalis, Niamey (2022–2025), average 15.80/20. Coursework: mathematics for AI, algorithms, ML/DL, NLP, computer vision, databases, systems and networks.
- Associate Data Scientist Program — Qwasar Silicon Valley (2023–2024), 57 project-based assignments evaluated through automated grading and peer review, fully in English.

**Certifications** — IBM Full Stack Software Developer · IBM RAG and Agentic AI · IBM AI Engineering · IBM Data Science Professional (all 2025) · Mathematics for Machine Learning and Data Science, DeepLearning.AI (2023). Full list of 19 on the [portfolio](https://yacineseybousiddo.me).

**Teaching** — Instructor, *Introduction to Artificial Intelligence*, A.D.U. (2025) · workshop lead, Git/GitHub, Tech Communities Club A.D.U. · trainer, "Master AI Tools" workshop.

## Open-Source Ecosystem — 6 tools, 2026, dual-licensed (AGPL-3.0 / commercial)

Each tool ships with a `BENCHMARK.md` and a `RESEARCH.md` in its repository — the evaluation protocol and the raw numbers, favorable and unfavorable both. Summaries below; the repos are the source of truth.

### [IntelAI](https://github.com/Yacine-ai-tech/intelai) — Persona-Aware Enterprise Analytics & RAG Copilot
![PyPI](https://img.shields.io/pypi/v/intelai?label=intelai) ![PyPI](https://img.shields.io/pypi/v/omnismart-personas?label=omnismart-personas)

Nine C-suite personas (CEO, CFO, CTO, COO, CHRO, ESG, Risk, Analyst, General), each scoped to its own data domain by architecture, not prompt instruction. 146 curated KPIs across 7 domains, 78-month history. Hybrid retrieval (BGE-large-en-v1.5 dense + BM25 + RRF fusion + cross-encoder reranking) plus a GraphRAG-lite layer for multi-hop queries.

Measured results: out-of-sample backtest on 378 forecasts, MAE 12.48% (median 9.90%); GraphRAG-lite reaches 95.0% entity coverage; a 50-case production sample scores 71.4% accuracy with a grounding score of 0.572. Published alongside those numbers: French/English answer-quality parity is currently uneven — 0.917 FR vs 0.431 EN.

### [DocIntel](https://github.com/Yacine-ai-tech/docintel) — Vision-First Document Intelligence

Extracts structured data from PDFs and images across three routes: hosted vision LLM, local Ollama vision model, and a lightweight OCR fallback. Multi-currency and multi-locale normalization, including FCFA/XOF under UEMOA VAT convention.

Measured results: 95.0% zero-shot accuracy on the SROIE benchmark; 100% on a multilingual cloud-route invoice set; the self-hosted route reaches 77.0% on CORD receipts at roughly one-fifth the per-document cost of the cloud route.

### [RAGeval](https://github.com/Yacine-ai-tech/rageval) — Self-Hosted LLMOps Observability for RAG
![PyPI](https://img.shields.io/pypi/v/omnismart-rageval?label=omnismart-rageval)

```python
from rageval import track

@track(project="my_rag_app")
async def answer(question): ...
```

Multi-judge consensus scoring with bootstrap confidence intervals, not point estimates.

Measured results: HaluEval-QA (N=200), accuracy 0.785 [0.725–0.840], ROC-AUC 0.870 [0.818–0.915]. Published as the headline finding: the multi-judge consensus did not outperform its single best judge — a negative result, kept in the title rather than buried.

### [AgentKit](https://github.com/Yacine-ai-tech/agentkit) — Governed MCP Tool Server
![PyPI](https://img.shields.io/pypi/v/agentkit-mcp?label=agentkit-mcp)

Gives Claude Desktop, Cursor, or any LangGraph agent governed access to live business data through the Model Context Protocol — tool calls, stable resource URIs, and a reusable executive-briefing prompt.

Measured results: 14/14 adversarial guardrail tests pass, deterministic and offline; on an MCP benchmark, tool selection scores 19/20 and response quality 18/20.

### [StreamPulse](https://github.com/Yacine-ai-tech/streampulse) — Real-Time Business Data Pipeline

Multi-source ingestion with n8n automation integration and a classification cascade tuned against its own score distribution rather than a fixed threshold.

Measured results: cascade accuracy improves from 0.083 to 0.917 (0.793 macro-F1) across three stages on a held-out paraphrased set. Published alongside that: the pipeline's rate ceiling is 22 requests/second, with 100% errors observed in a 1,000-request burst test.

### [VoiceFlow](https://github.com/Yacine-ai-tech/voiceflow) — Speech to Structured Business Intelligence

Routes recorded audio to per-analysis-type LLMs (meeting, sales call, support call, interview) with a multi-provider transcription and diarization fallback chain.

Measured results: 2.2% WER / 0.8% CER on LibriSpeech test-clean (Whisper large-v3, N=150). The repository explicitly declines to present this as a state-of-the-art claim — it's a controlled benchmark result, framed as exactly that.

## Results at a Glance

| Tool | Core measured result | Benchmark / protocol |
|---|---|---|
| IntelAI | MAE 12.48% (median 9.90%) | Out-of-sample backtest, 378 forecasts |
| DocIntel | 95.0% zero-shot accuracy | SROIE |
| RAGeval | 0.785 accuracy [0.725–0.840] | HaluEval-QA, N=200, bootstrap CI |
| AgentKit | 14/14 guardrail tests passed | Adversarial test suite, deterministic |
| StreamPulse | 0.917 cascade accuracy (0.793 macro-F1) | Held-out paraphrased set |
| VoiceFlow | 2.2% WER / 0.8% CER | LibriSpeech test-clean, N=150 |

## Client Work (scoped to what's publicly shareable)

**HyperTech Electronics** — AI layer for an e-commerce and retail-operations platform: bilingual semantic search, a six-persona intent-routed assistant, and a deterministic degraded-mode fallback built after a live provider-quota outage in production.

**HyperTech Connect** — zero-trust, protocol-agnostic IoT and edge-management platform for infrastructure-constrained environments (WireGuard mesh, MQTT/LoRaWAN/Modbus/CAN bus gateway, delta-compressed OTA firmware). Architecture fully designed; physical validation on ESP32 and LilyGO T-SIM7000G hardware, remainder emulated and simulated.

**HyperFlow** — digital-agriculture platform for smart irrigation across the Sahel, including migration tooling for legacy, informally-structured land-ownership records.

## Research Direction

Applied research on low-resource African languages through *Cibiyar Karatu*, an offline-first adaptive-learning platform for Hausa, Zarma, and Fulfulde speakers on entry-level hardware — currently in prototyping and testing, with real-user testing to follow. Pre-incorporation stage; architecture and product design are not detailed publicly.

I'm also working toward graduate-level engineering training, aimed at closing the hardware and robotics gap my own software work keeps surfacing — physical AI: natural-scene computer vision, robotics, and embedded systems, beyond the document- and simulation-bound versions I've shipped so far.

---

Full evaluation protocols and results for each tool are documented in their respective repositories.
