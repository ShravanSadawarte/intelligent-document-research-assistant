# 🧠 Intelligent Document Research Assistant

A **Retrieval-Augmented Generation (RAG)** based document research assistant that allows users to ask questions about their documents and receive answers grounded in the retrieved document content.

The current version implements a complete **Basic RAG pipeline** using PDF ingestion, fixed-size chunking, local embeddings, ChromaDB vector search, and Gemini for answer generation.

---

## 🚀 Project Overview

Traditional LLMs answer questions using their pretrained knowledge. They may not know the contents of a user's private documents.

This project solves that problem using **Retrieval-Augmented Generation (RAG)**.

Instead of directly sending a question to an LLM, the system:

1. Loads a document.
2. Extracts its text.
3. Splits the text into chunks.
4. Converts chunks into vector embeddings.
5. Stores the vectors in ChromaDB.
6. Converts the user's question into a vector.
7. Retrieves the most semantically relevant chunks.
8. Builds a context-aware prompt.
9. Sends the context and question to Gemini.
10. Generates an answer based on the retrieved document information.

---

# 🔄 RAG Pipeline

```text
                    DOCUMENT INGESTION
                           │
                           ▼
                      📄 PDF File
                           │
                           ▼
                    Text Extraction
                           │
                           ▼
                    Fixed-Size Chunks
                           │
                           ▼
                      Embeddings
                           │
                           ▼
                       ChromaDB
                           │
                           │
                           │
                    USER QUERY FLOW
                           │
                           ▼
                    👤 User Question
                           │
                           ▼
                    Query Embedding
                           │
                           ▼
                    Similarity Search
                           │
                           ▼
                  Top-K Relevant Chunks
                           │
                           ▼
                   Context Construction
                           │
                           ▼
                      RAG Prompt
                           │
                           ▼
                       Gemini LLM
                           │
                           ▼
                    🤖 Final Answer
```

---

# 🛠️ Tech Stack

### AI / RAG

* Python
* Sentence Transformers
* `all-MiniLM-L6-v2`
* ChromaDB
* Google Gemini API

### Backend / AI Service

* Python
* Modular RAG architecture

### Document Processing

* PyPDF

### Environment

* Python Virtual Environment
* PowerShell

---

# 📁 Project Structure

```text
intelligent-document-research-assistant/
│
├── ai-service/
│   │
│   ├── app.py
│   ├── requirements.txt
│   │
│   ├── embeddings/
│   │   ├── embedding_model.py
│   │   └── __init__.py
│   │
│   ├── generation/
│   │   ├── llm.py
│   │   ├── prompt.py
│   │   └── __init__.py
│   │
│   ├── ingestion/
│   │   ├── loader.py
│   │   ├── chunker.py
│   │   └── __init__.py
│   │
│   ├── pipeline/
│   │   ├── rag_pipeline.py
│   │   └── __init__.py
│   │
│   ├── retrieval/
│   │   ├── retriever.py
│   │   └── __init__.py
│   │
│   ├── vectorstore/
│   │   ├── chroma.py
│   │   └── __init__.py
│   │
│   ├── data/
│   │   └── sample.pdf
│   │
│   └── chroma_db/
│
└── README.md
```

---

# 🧩 Core Components

## 1. PDF Loader

File:

```text
ingestion/loader.py
```

Uses `pypdf` to extract text from PDF files page-by-page.

Each extracted page retains its page number.

Example:

```python
{
    "page_number": 1,
    "text": "Document content..."
}
```

Keeping page metadata allows the system to identify where retrieved information came from.

---

## 2. Chunker

File:

```text
ingestion/chunker.py
```

The extracted document is divided into smaller pieces.

Current configuration:

```text
Chunk size:     500 characters
Overlap:         50 characters
```

Current implementation uses **fixed-size character-based chunking**.

This is intentionally simple because this version focuses on understanding and implementing **Basic RAG**.

Advanced chunking techniques will be introduced later.

---

## 3. Embedding Model

File:

```text
embeddings/embedding_model.py
```

The project currently uses:

```text
all-MiniLM-L6-v2
```

The model converts text into numerical vectors.

Current vector dimension:

```text
384
```

For example:

```text
"React and Node.js developer"
            ↓
     Embedding Model
            ↓
[0.12, -0.31, 0.47, ..., 0.09]
```

The same embedding model is used for both:

* Document chunks
* User queries

This allows semantic similarity search.

---

# 🗄️ 4. ChromaDB

File:

```text
vectorstore/chroma.py
```

ChromaDB is used as the project's local vector store.

It stores:

```text
Chunk ID
   +
Chunk Text
   +
Embedding
   +
Page Metadata
```

Example:

```text
Chunk:
"Developed an AI-powered fashion platform..."

Embedding:
[0.12, -0.42, ...]

Metadata:
page_number = 1
```

The database is persisted locally in:

```text
chroma_db/
```

This directory is excluded from Git.

---

# 🔎 5. Retriever

File:

```text
retrieval/retriever.py
```

The Retriever is responsible for finding relevant information.

When the user asks:

```text
"What projects are mentioned?"
```

the system:

```text
Question
   ↓
Embedding Model
   ↓
Query Vector
   ↓
ChromaDB
   ↓
Similarity Search
   ↓
Top-K Chunks
```

The current default is:

```python
top_k = 5
```

The Retriever **does not generate the answer**.

Its responsibility is:

> Find the most relevant document chunks.

---

# 📝 6. Prompt Construction

File:

```text
generation/prompt.py
```

Retrieved chunks are combined into a context.

The prompt instructs the LLM to:

* Use the provided context.
* Answer the user's question.
* Avoid making up information.
* State when the answer cannot be found in the document.

Conceptually:

```text
System Instructions
        +
Retrieved Context
        +
User Question
        ↓
     RAG Prompt
```

---

# 🤖 7. LLM Generation

File:

```text
generation/llm.py
```

Gemini is used as the generation model.

The LLM receives:

```text
Retrieved Context
       +
User Question
       ↓
     Gemini
       ↓
Generated Answer
```

The LLM is therefore not responsible for searching the document.

The Retriever finds the information first.

---

# 🔗 8. RAG Pipeline

File:

```text
pipeline/rag_pipeline.py
```

This is the orchestration layer.

It connects:

```text
Retriever
    ↓
Context
    ↓
Prompt
    ↓
LLM
    ↓
Answer
```

The main interface is:

```python
rag.ask(question)
```

This hides the internal complexity and provides a simple way to execute the complete RAG process.

---

# 💻 Running the Project

## 1. Clone the repository

```bash
git clone <your-repository-url>
cd intelligent-document-research-assistant
```

---

## 2. Enter the AI service

PowerShell:

```powershell
cd .\ai-service
```

---

## 3. Create virtual environment

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

You should see:

```text
(.venv)
```

in your terminal.

---

## 4. Install dependencies

```powershell
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create:

```text
ai-service/.env
```

Add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

Never commit `.env` to Git.

The project `.gitignore` already excludes environment files.

---

# ▶️ Run the Application

From:

```text
D:\intelligent-document-research-assistant\ai-service
```

run:

```powershell
python app.py
```

The application can then operate as a terminal-based document research assistant.

Example:

```text
====================================
   Intelligent Document Assistant
====================================
Ask questions about your document.
Type 'exit' to quit.

You: What projects are mentioned?

Assistant:
The document mentions several projects including ...
```

You can continue asking questions:

```text
You: What is the educational qualification?

Assistant:
...

You: What technologies are mentioned?

Assistant:
...

You: exit

Goodbye!
```

---

# 🧪 Current RAG Capabilities

### Supported

* PDF ingestion
* Page-level text extraction
* Fixed-size chunking
* Chunk overlap
* Local text embeddings
* 384-dimensional embeddings
* Persistent ChromaDB storage
* Semantic similarity search
* Top-K retrieval
* Context construction
* Gemini generation
* Grounded prompt instructions
* Terminal-based question answering

---

# ⚠️ Current Limitations

This is intentionally a **Basic RAG implementation**.

The current system uses:

```text
Fixed-size chunking
+
Basic vector similarity search
+
Top-K retrieval
```

Therefore, retrieval quality can sometimes be poor.

For example, a question asking for the document's overall purpose may retrieve chunks about projects or education instead of the ideal summary section.

This is an expected limitation of Basic RAG.

---

# 🚀 Advanced RAG — Future Improvements

The next stage of the project will improve retrieval quality.

Planned features:

### Better Chunking

* Structure-aware chunking
* Section-aware chunking
* Sentence/paragraph chunking
* Semantic chunking

### Better Retrieval

* Metadata filtering
* Hybrid search
* Keyword + semantic search
* Reranking
* Query rewriting
* Multi-query retrieval

### Context Improvements

* Context compression
* Relevant-context selection
* Conversation-aware retrieval
* Multi-document retrieval

### Reliability

* Source/page citations
* Retrieval evaluation
* Answer evaluation
* Hallucination detection
* Grounding checks

---

# 🗺️ Development Roadmap

```text
PHASE 1 — BASIC RAG
│
├── PDF ingestion                 ✅
├── Text extraction               ✅
├── Chunking                      ✅
├── Embeddings                    ✅
├── ChromaDB                      ✅
├── Retrieval                     ✅
├── Prompt construction           ✅
├── Gemini integration            ✅
├── End-to-end pipeline           ✅
└── Testing                       🔄
        │
        ▼
PHASE 2 — ADVANCED RAG
│
├── Better chunking
├── Metadata filtering
├── Hybrid retrieval
├── Reranking
├── Query rewriting
├── Multi-document retrieval
├── Context compression
├── Conversation-aware RAG
└── Evaluation
        │
        ▼
PHASE 3 — FULL-STACK APPLICATION
│
├── Node.js
├── Express.js
├── MongoDB
├── JWT Authentication
├── React frontend
├── Document upload
├── Chat interface
└── User document management
```

---

# 🎯 Learning Objectives

This project is being built not just as a working application, but as a way to understand the internal mechanics of RAG.

By completing this project, you will understand:

* What embeddings actually represent
* Why vector databases are used
* How semantic similarity search works
* How retrieval differs from generation
* How retrieved context is passed to an LLM
* Why retrieval quality affects answer quality
* How a RAG pipeline is orchestrated
* Why Basic RAG has limitations
* How Advanced RAG techniques solve those limitations

---

# 🧠 Key Concept

The fundamental distinction in this project is:

```text
Retriever = FIND 🔎
LLM       = UNDERSTAND + GENERATE 🧠
```

Together:

```text
User Question
      ↓
Retriever 🔎
      ↓
Relevant Evidence
      ↓
LLM 🧠
      ↓
Grounded Answer
```

That is the core idea behind **Retrieval-Augmented Generation**.

---

# 📌 Project Status

**Current Version:** Basic RAG v1

**Status:** 🟢 Core end-to-end pipeline implemented

**Next milestone:** Basic RAG testing and source/page citations

**Future:** Advanced RAG → Full-stack RAG application

---

## 👨‍💻 Author

**Shravan Sadawarte**

B.Tech — Artificial Intelligence & Data Science

---

⭐ This project is part of a structured AI learning journey focused on building practical, portfolio-level AI systems from first principles.
