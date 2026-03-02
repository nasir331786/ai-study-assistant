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

![Python](https://img.shields.io/badge/Python-3.11-blue)
![LangChain](https://img.shields.io/badge/LangChain-0.2-green)
![Groq](https://img.shields.io/badge/Groq-LLaMA3.1-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-1.35-red)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

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
|---|---|
| `GROQ_API_KEY` | Your Groq API key from [console.groq.com](https://console.groq.com) |

## 📦 Tech Stack

- **LLM**: LLaMA 3.1 8B via Groq API
- **RAG**: LangChain with history-aware retriever
- **Embeddings**: sentence-transformers/all-MiniLM-L6-v2
- **Vector Store**: FAISS (local, in-memory)
- **UI**: Streamlit
- **Deployment**: Docker + Hugging Face Spaces

## 💻 Author

**Nasir Husain Tamanne**  
[![GitHub](https://img.shields.io/badge/GitHub-nasir331786-black)](https://github.com/nasir331786)  
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue)](https://www.linkedin.com/in/nasir-husain-tamanne)

## 📄 License

MIT License
