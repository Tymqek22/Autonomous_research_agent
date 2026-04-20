# 🧠 Autonomous Research Agent

Autonomous Research Agent is an AI-driven system designed to evaluate the credibility of online articles by decomposing the problem into structured reasoning steps. The agent analyzes content, verifies extracted claims using external sources, and produces a final credibility assessment with justification.



## 🚀 Overview

This project implements a multi-stage autonomous agent built using **LangChain** and **LangGraph**, orchestrated as a pipeline of specialized nodes. The system processes an article URL and determines its reliability by extracting facts, validating them against external data, and synthesizing a final verdict.

The application is exposed as an API built with **FastAPI**, while computationally intensive agent workflows are handled asynchronously using **Celery** and **Redis**.


## 🧩 Architecture

The agent operates as a graph of four main nodes:

### 1. Scraper
- Fetches and parses the HTML content of the target webpage
- Filters out irrelevant elements (e.g., scripts, ads, navigation)
- Produces clean, structured text for downstream processing

### 2. Extractor
- Processes the cleaned HTML content
- Identifies and extracts factual claims from the article
- Outputs a structured list of facts

### 3. Analyzer
- For each extracted fact:
  - Performs external research (e.g., web search)
  - Gathers supporting or contradicting evidence
  - Evaluates credibility based on collected data
- Outputs a verdict for each fact (e.g., *true*, *false*, *unverified*, *partially true*) along with reasoning

### 4. Synthesizer
- Aggregates all individual fact verdicts
- Produces a final credibility score or classification for the article
- Generates a human-readable explanation of the decision



## 🔄 Workflow

Each stage is executed as part of a **LangGraph workflow**, enabling modularity and extensibility.



## ⚙️ Tech Stack

- **Backend API:** FastAPI  
- **Task Queue:** Celery  
- **Message Broker / Backend:** Redis  
- **Agent Framework:** LangChain + LangGraph  
- **Language:** Python  



## 🧵 Asynchronous Processing

To ensure scalability and responsiveness:

- API requests trigger background tasks via Celery
- Agent execution runs in a separate worker process
- Redis is used as both broker and result backend
- Results can be retrieved asynchronously

