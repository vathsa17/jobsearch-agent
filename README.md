# AI Job Agent 🚀

An AI-powered job search assistant that automatically searches the German **Jobsuche (Bundesagentur für Arbeit)** portal, evaluates job postings against your CV using LLMs, and helps you find the best opportunities.

> **Status:** 🚧 Work in Progress

---

## Features

### Current

- Search Jobsuche (Bundesagentur für Arbeit)
- Search multiple keywords
- Parse job results
- Remove duplicate jobs
- Clean Python architecture

### Planned

- Download complete job descriptions
- AI-powered job matching (OpenRouter)
- Match score (0-100)
- Missing skills analysis
- Tailored CV generation
- Cover letter generation
- HTML email reports
- Daily GitHub Actions automation
- Streamlit dashboard
- SQLite database
- Interview question generation

---

## Tech Stack

- Python 3.12+
- Jobsuche API
- OpenRouter
- SQLite
- Requests
- HTTPX
- Jinja2
- GitHub Actions

---

## Project Structure

```text
job-agent/

├── app.py
├── config.py
├── requirements.txt
├── README.md
├── .env.example
│
├── jobs/
│   ├── jobsuche.py
│   ├── models.py
│   └── details.py
│
├── llm/
│   ├── matcher.py
│   └── openrouter.py
│
├── database/
│   └── db.py
│
├── email/
│   └── sender.py
│
├── templates/
│
├── cv/
│   └── cv.txt
│
├── reports/
│
└── data/
```

---

## Setup

Clone the repository.

```bash
git clone https://github.com/<your-username>/ai-job-agent.git

cd ai-job-agent
```

Create a virtual environment.

```bash
python -m venv .venv
```

Activate it.

Linux / macOS

```bash
source .venv/bin/activate
```

Windows

```powershell
.venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Configuration

Copy

```text
.env.example
```

to

```text
.env
```

Add your OpenRouter API key.

```text
OPENROUTER_API_KEY=sk-or-v1-xxxxxxxxxxxxxxxx
```

---

## Run

```bash
python app.py
```

---

## Example Output

```
Searching: Salesforce
Searching: Salesforce Developer

Found 18 unique jobs

----------------------------------------------------
Salesforce Developer
Brunel GmbH
Stuttgart

Remote : Yes

Salary : 60000 - 95000 €
----------------------------------------------------
```

---

# Roadmap

## Phase 1

- [x] Jobsuche API
- [x] Job models
- [x] Multi-keyword search
- [ ] SQLite database

## Phase 2

- [ ] Full job description retrieval
- [ ] OpenRouter integration
- [ ] AI scoring

## Phase 3

- [ ] HTML reports
- [ ] Email notifications
- [ ] GitHub Actions automation

## Phase 4

- [ ] Tailored CV generation
- [ ] Cover letter generation
- [ ] Interview question generation

## Phase 5

- [ ] Streamlit dashboard
- [ ] Telegram Bot
- [ ] LinkedIn support
- [ ] Greenhouse support
- [ ] Lever support

---

## Motivation

Searching for jobs manually every day is repetitive and time-consuming.

This project automates the process by:

- finding relevant jobs,
- ranking them against your CV,
- identifying missing skills,
- generating tailored application documents,
- and notifying you only about the best opportunities.

---

## License

MIT License

---

## Disclaimer

This project is an independent tool and is **not affiliated with the Bundesagentur für Arbeit** or any other job platform.