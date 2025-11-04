# Assignment 1: Ollama Chatbot — Submission (Plain English Version)

**Course**: LLMs and Multi-Agent Orchestration  
**Institution**: Reichman University  
**Submission Deadline**: November 13, 2025

---

## Team Information

**Team Code (no spaces)**: `[YourUniqueCode]` *(e.g., FouadTeam2025)*

**Member A**
- ID: `[ID Number]`
- Name (optional): `[Full Name]`

**Member B**
- ID: `[ID Number]`
- Name (optional): `[Full Name]`

**GitHub Repository**: `[https://github.com/username/repo]` ✅ PUBLIC  
**Submission Date**: November 4, 2025

---

## 1) PRD — What we’re building and why

### In one sentence
We built a simple chatbot (like ChatGPT) that runs locally using **Ollama** and has a clean web UI.

### What we must support
- Connect to the local Ollama API on `localhost:11434`
- A usable GUI (we chose a browser UI with Streamlit)
- Send user messages and show model responses
- Keep conversation history within the session
- Let the user pick a model
- Handle errors nicely (e.g., if Ollama isn’t running)

### Tech stack (short and practical)
- **LLM**: Ollama (local; no API key needed)
- **Model**: `llama3.2` (small and runs everywhere)
- **UI**: Streamlit (fast to build and learn)
- **Language**: Python
- **Client**: Ollama Python SDK

### Why this setup
- We wanted zero cloud costs and fast local iterations → Ollama
- We wanted to build a working UI in hours, not days → Streamlit
- We’re comfortable with Python and the SDK is simple

---

## 2) AI prompts we actually used (paste yours here)

Replace the examples with your real prompts from ChatGPT/Claude/Cursor. Dates help show your process.

### Prompt #1 — Getting started
**Date**: [Your Date]  
**Tool**: [ChatGPT/Claude/Cursor]

```
[PASTE YOUR ACTUAL PROMPT]
```

What we got back:
- [Summarize the answer you received]

What we learned:
- [Write what you understood/changed]

---

### Prompt #2 — Conversation memory
**Date**: [Your Date]

```
[PASTE YOUR ACTUAL PROMPT]
```

What we got back:
- [Short summary]

What we changed in the code:
- [e.g., Send the full messages array each call]

---

### Prompt #3 — [Your next issue]
**Date**: [Your Date]

```
[PASTE YOUR ACTUAL PROMPT]
```

Result & learning:
- [Short and honest]

---

### Add more prompts as needed (total 3–7)

---

## 3) What we built

### Project layout
```
Assignment1/
├── chatbot_streamlit.py      # Main app
├── requirements.txt          # Dependencies
├── launch_streamlit.sh       # One-liner launcher
├── .gitignore                # Keeps venv/secrets out of git
└── Udocs/                    # Documentation
```

### How the pieces talk
```
User → Streamlit UI → Ollama Python SDK → Ollama API (localhost:11434)
    → LLM (llama3.2) → Response back to UI
```

### Core code ideas
- Call `ollama.chat(model, messages=[...])`
- Keep messages in `st.session_state` so the chat “remembers”
- Model selection in the sidebar
- Clear chat resets the session messages

---

## 4) How we built the UI (short story)

1) We compared HTML/Flask/Streamlit/desktop. We picked **Streamlit** to move fast.  
2) We scaffolded a basic page, added a chat input and message list.  
3) We wired up Ollama calls.  
4) We stored the full message history in `st.session_state` so context is preserved.  
5) We added a sidebar for model selection and a “Clear chat” button.  
6) We tested common errors (like Ollama not running) and added helpful messages.

---

## 5) How to run it (UV-first, as recommended)

### Prerequisites
```bash
# 1) Install Ollama
brew install ollama

# 2) Pull a small model
ollama pull llama3.2

# 3) Install UV (faster package manager)
brew install uv

# 4) Clone the repo
git clone [your-repo-url]
cd Assignment1
```

### Start everything

Terminal 1 — start Ollama:
```bash
ollama serve
```

Terminal 2 — set up and run the app:
```bash
cd Assignment1

# First-time only: create a virtual environment
python3 -m venv .venv

# Activate it
source .venv/bin/activate

# Install packages (fast via UV)
uv pip install -r requirements.txt

# Run the app
streamlit run chatbot_streamlit.py
```

Open your browser at: http://localhost:8501  
Quick start next time:
```bash
bash launch_streamlit.sh
```

---

## 6) How to use the UI

- Pick a model in the sidebar (e.g., `llama3.2`)
- Type your message at the bottom input
- Press Enter; the reply appears
- Ask follow‑ups — the chat keeps context
- Use “Clear chat” to start fresh

Example:
```
You: Hello!
Bot: Hi! How can I help you today?
You: What’s 2+2?
Bot: 2+2 = 4
You: And 3+3?
Bot: 3+3 = 6
```

---

## 7) Technical details (in plain English)

### Ollama in one paragraph
Ollama runs locally as a small HTTP server on `localhost:11434`. You don’t need an API key because nothing leaves your machine. Your app sends a list of messages with roles (`user` / `assistant`), and Ollama returns the next assistant message. LLMs don’t remember anything between requests, so you must send the full conversation each time.

### Minimal call
```python
import ollama

response = ollama.chat(
    model="llama3.2",
    messages=[
        {"role": "user", "content": "Hello"}
    ]
)

assistant_text = response["message"]["content"]
```

### Error handling
```python
try:
    response = ollama.chat(model=model, messages=messages)
except Exception as e:
    st.error(f"Error: {e}")
    st.info("Make sure Ollama is running: ollama serve")
```

### Session state (why it matters)
```python
if "messages" not in st.session_state:
    st.session_state.messages = []

st.session_state.messages.append({"role": "user", "content": user_input})
```

---

## 8) What we learned

- How to call Ollama’s API from Python, end‑to‑end
- Why LLMs need the full message history on every call
- How to design a simple, usable chat UI quickly
- How to handle common errors and keep the app stable

---

## 9) Repository info

**Repo URL**: [Your GitHub/GitLab URL]  
**Public**: ✅ Yes

Includes:
- `chatbot_streamlit.py` (app)
- `requirements.txt` (deps only — no venv committed)
- `launch_streamlit.sh` (launcher)
- `Udocs/ASSIGNMENT1_SUBMISSION.md` (this doc)
- `.gitignore` (excludes `.venv`, `__pycache__`, `.env`, etc.)

---

## 10) Quick checklist

- [x] App launches without errors
- [x] Connects to Ollama on localhost
- [x] Sends/receives chat messages
- [x] Keeps chat history in session
- [x] Lets you pick a model
- [x] Handles common errors
- [x] Repo is public and clean
- [x] This document includes our prompts and process

---

## 11) Self‑assessment (grade recommendation)

**Recommended grade**: `[60–100]`

Notes from the lecturer:
- 100 → extremely strict review (“find the elephants in the reeds”)
- 60 → flexible review if the submission is reasonable

**Our short reasoning**
- Strengths: [what clearly works well]
- Improvements: [what we’d polish next]
- Why this grade: [one small paragraph]

---

## 12) Special notes (optional)

Late submission: ☐ Yes ☐ No  
If late, why: `[Your reason]`  
Other notes for the grader: `[Anything they should know]`

---

## Conclusion

We delivered a working local chatbot with a clean UI and clear docs.  
We can connect to Ollama, keep conversation history, and handle errors.  
We documented our real prompts and our process, as requested.

Important: Accuracy of model answers is not graded; using the tools correctly is.

---

## Submission details

**Team Code**: `[YourTeamCode]`  
**Team Members**: `[Member A] & [Member B]`  
**Date Submitted**: November 4, 2025  
**Course**: LLMs and Multi‑Agent Orchestration  
**Institution**: Reichman University

---

**Each team member submits this document separately to Moodle.**

---

## [Blank page for grader notes]

*(When exporting to PDF, leave an empty page here for feedback.)*

