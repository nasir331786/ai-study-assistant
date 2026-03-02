---
title: AI Study Assistant
emoji: 📚
colorFrom: blue
colorTo: indigo
sdk: docker
app_file: app.py
pinned: false
---

# 📚 AI Study Assistant

> Chat with any PDF using RAG + LLaMA 3.1 — 100% free to run.

[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-0.2-green)](https://langchain.com)
[![Groq](https://img.shields.io/badge/Groq-LLaMA3.1-orange)](https://groq.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.35-red)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)
[![Live Demo](https://img.shields.io/badge/🤗%20Live%20Demo-Hugging%20Face-yellow)](https://huggingface.co/spaces/huntnasir/ai-study-assistant)

## 🚀 Live Demo

**Try it now → [https://huggingface.co/spaces/huntnasir/ai-study-assistant](https://huggingface.co/spaces/huntnasir/ai-study-assistant)**

> Upload any PDF and start chatting with it instantly — no setup required!

---

## 🌊 What It Does

Upload any PDF — textbook, research paper, notes — and ask questions in plain English. The app uses Retrieval-Augmented Generation (RAG) to find the most relevant sections and answer accurately with source references.

## 🏗️ Architecture

```
PDF → PyPDF Loader → Text Splitter → HuggingFace Embeddings
                                              ↓
User Question → History-Aware Retriever → FAISS Vector Store
                                              ↓
                    LLaMA 3.1 8B (via Groq) → Answer + Sources
```

## 🚀 Quick Start

### 1. Clone the repo

```bash
git clone https://github.com/nasir331786/ai-study-assistant
cd ai-study-assistant
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Set up environment variables

```bash
cp .env.example .env
# Edit .env and add your GROQ_API_KEY
```

### 4. Run the app

```bash
streamlit run app.py
```

## 🔑 Environment Variables

| Variable | Description |
|----------|-------------|
| `GROQ_API_KEY` | Your Groq API key from [console.groq.com](https://console.groq.com/) |

## 📦 Tech Stack

| Tool | Purpose |
|------|---------|
| LangChain | RAG pipeline & chains |
| Groq API | Fast LLM inference (free tier) |
| LLaMA 3.1 8B | Language model |
| HuggingFace Embeddings | Text embeddings (free, local) |
| FAISS | Vector similarity search |
| Streamlit | Web UI |
| Docker | Containerization |

## ⚙️ Configuration

All settings are in `config.py` — no need to touch core logic:

| Setting | Default | Description |
|---------|---------|-------------|
| `llm_model` | `llama-3.1-8b-instant` | Groq model to use |
| `llm_temperature` | `0.3` | Response creativity |
| `chunk_size` | `1000` | PDF chunk size |
| `retriever_k` | `4` | Chunks retrieved per query |
| `max_file_size_mb` | `10` | Max PDF upload size |

## 💻 Author

**Nasir Husain Tamanne**  
[GitHub](https://github.com/nasir331786) · [LinkedIn](https://www.linkedin.com/in/nasir-husain-tamanne)

## 📄 License

MIT License — free to use, modify and distribute.
