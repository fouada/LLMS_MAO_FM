## Assignment 1 — Local Chatbot (Ollama)

This repo contains a simple local chatbot that connects to Ollama on localhost and provides a clean web UI. It aligns with the course instructions to document your prompts and process.

### What’s here
- `chatbot_streamlit.py` — main Streamlit app (recommended UI)
- `chatbot_flask.py` — alternative Flask app
- `requirements.txt` — dependencies only (no venv committed)
- `launch_streamlit.sh`, `launch_flask.sh` — one‑liners to run
- `Udocs/ASSIGNMENT1_SUBMISSION.md` — PRD + submission doc (paste your real prompts there)
- `docs/images/` — add screenshots here (UI running, tests, etc.)

### Prerequisites
```bash
# 1) Install Ollama
brew install ollama

# 2) Pull a small model
ollama pull llama3.2

# 3) Install UV (fast Python package manager)
brew install uv
```

### Setup & Run (Streamlit)
```bash
# Clone
git clone <your-public-repo-url>
cd Assignment1

# Create venv (course requires requirements.txt; do not commit venv)
python3 -m venv .venv
source .venv/bin/activate

# Start Ollama in a separate terminal
ollama serve

# Install deps (fast via UV)
uv pip install -r requirements.txt

# Run the app
streamlit run chatbot_streamlit.py
```

Open the browser at http://localhost:8501

Quick start next time:
```bash
bash launch_streamlit.sh
```

### How to use
- Pick a model in the sidebar (e.g., `llama3.2`)
- Type your message, press Enter
- The chat keeps context for the current session
- Use “Clear chat” to reset

### Screenshots (add yours)
Place images under `docs/images/` and reference them here, for example:

![App Home](docs/images/app-home.png)
![Chat Example](docs/images/chat-example.png)

### Prompts & PRD
- Paste your actual prompts and short outcomes into `Udocs/ASSIGNMENT1_SUBMISSION.md` (section: “AI prompts we actually used”). This is the single source of truth; you may link to any additional notes if you kept them separately.

The lecturer wants to see how you phrased the prompts that built the project. Export to PDF if needed from the submission doc.

### Repository expectations (from class)
- Repo must be PUBLIC
- Use `requirements.txt` (do not commit your virtual environment)
- Keep secrets out of git (`.env` is ignored by default)
- Include screenshots in docs/README

### Troubleshooting
```bash
# Verify Ollama
curl http://localhost:11434/api/tags

# Ensure packages are installed in the venv
source .venv/bin/activate
uv pip install -r requirements.txt
```

For quick commands, see `QUICK_REFERENCE.md`.


