# AI Job Outreach Automation (RAG + LLM)

## Overview

This project automates **job opportunity discovery and personalized outreach** using **LLMs, vector databases, and portfolio matching**.

The system extracts job postings from company career pages, structures them into JSON using an LLM, stores relevant embeddings in a vector database, and finally generates **personalized cold emails** based on the job description and your portfolio.

This is a practical **RAG (Retrieval-Augmented Generation)** style workflow using modern AI tooling.

---

## Architecture Diagram

![Architecture](architecture.png)

---

## Workflow Explanation

### 1. Career Page Scraping

* The system reads **company career pages**.
* Job descriptions are collected as raw text.
* These pages may include multiple job listings.

---

### 2. LLM Extraction

An **LLM processes the career page content** and extracts structured job information.

Output format:

```json
{
  "job_title": "Frontend Developer",
  "skills": ["React", "JavaScript", "CSS"],
  "experience": "2+ years",
  "job_description": "We are looking for..."
}
```

This step converts **unstructured HTML/text into structured data**.

---

### 3. Job JSON Storage

All extracted jobs are stored in a structured format with fields:

* `job_title`
* `skills`
* `experience`
* `job_description`

This allows easier querying and downstream processing.

---

### 4. Vector Database

Job descriptions and skill requirements are converted into **embeddings** and stored in a **Vector Store**.

 vector database used **chromadb**

Purpose:

* Semantic similarity search
* Matching jobs with relevant portfolio projects

---

### 5. Portfolio Link Retrieval

Your **portfolio projects** are also embedded and stored in the vector database.

When a job appears:

* The system searches for **portfolio projects with similar skills**
* Returns relevant **portfolio links**

Example result:

```
Job requires: React + API integration

Retrieved portfolio:
- React Dashboard Project
- REST API Integration Project
```

---

### 6. LLM Cold Email Generation

A second **LLM call** generates a personalized outreach email using:

* Job information
* Required skills
* Relevant portfolio links

Example output:

```
Subject: Application for Frontend Developer Role

Hi Team,

I came across your opening for a Frontend Developer and it aligns closely with my experience in React and API integrations.

Here are a few relevant projects from my portfolio:
- React Analytics Dashboard
- REST API Integration Tool

I would love the opportunity to contribute to your team.

Best regards,
Akash Rathour
```

---

## Key Technologies

### Backend
* Python

### AI / LLM

* LangChain
* Groq / OpenAI / Llama models

### Vector Database

* chromadb

### Data Processing

* BeautifulSoup (for scraping)
* JSON parsing

---

## Example Tech Stack

```
Python
LangChain
Groq LLM
Chroma Vector DB
BeautifulSoup
```

---

## Project Structure

```
project/
│
├── main.py
├── chains.py
├── my_portfolio.csv
├── vector_store.py
├── utils.py
├── notebook.ipynb
├──requirements.txt
├── architecture.png
└── README.md
```

---

## Use Cases

* Automated job applications
* AI-powered outreach
* Recruiter prospecting

---

## Future Improvements
* Resume customization per job
* Dashboard for tracking applications

---

## Author

**Akash Rathour**
React Developer | AI Enthusiast | FastAPI Projects

---
