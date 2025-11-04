## Submission Checklist (aligned to lecture notes)

### Core Requirements (Yoram's instructions)

- [ ] **Repository is PUBLIC** (private repos will NOT be reviewed)
- [ ] **Document folder exists** with PRD and prompts in Markdown or PDF format
  - Location: `Udocs/ASSIGNMENT1_SUBMISSION.md` (single source for PRD + prompts)
- [ ] **Prompts are included** — show how you phrased prompts to build the project
  - What you asked (exact prompts from ChatGPT/Claude/Cursor)
  - How you iterated to reach the final app
  - Location: `Udocs/ASSIGNMENT1_SUBMISSION.md` → section "AI prompts we actually used"
- [ ] **Works with Ollama locally** — connects to the LLM API at `localhost:11434`
  - No cloud API key needed
  - Demonstrates you can integrate and use the API correctly
  - Quality of LLM answers is NOT graded; correct usage IS

### Technical Requirements

- [ ] **Python projects use `requirements.txt`** (mandatory)
  - Do NOT commit virtual environment folders (`.venv/`, `venv/`, `env/`)
  - Use `.gitignore` to exclude them
- [ ] **UV package manager recommended** for fast, parallel installs (optional but preferred)
  - Alternative: use standard `venv` + `pip`
- [ ] **No secrets committed** (passwords, API keys, tokens)
  - Use `.gitignore` for `.env` and credential files
  - Reviewer checks for this

### Documentation

- [ ] **README with setup/run instructions**
  - How to install dependencies
  - How to run the app
  - Screenshots or links to `docs/images/`
- [ ] **Screenshots included** showing:
  - UI running
  - Example chat interaction
  - Any tests or verification steps
- [ ] **Quick verification commands** (e.g., `curl http://localhost:11434/api/tags`)

### Functionality

- [ ] **Chat UI works** (Streamlit, Flask, or any framework)
  - Sends user messages to Ollama
  - Receives and displays responses
  - Keeps conversation history in session
- [ ] **Model selection** (user can pick from available Ollama models)
- [ ] **Error handling** (graceful messages if Ollama isn't running)

### Language/Framework Choice

- [ ] Any language is allowed (Python, JavaScript, Java, HTML, etc.)
  - This is NOT a programming course; focus is on LLM integration
  - Choose what you're comfortable with

---

## Notes from Yoram

- **What matters**: That you know how to activate and use an LLM API (Ollama) with an API key (or localhost in this case), connect to it, and integrate it.
- **What doesn't matter**: The quality or accuracy of the LLM's answers. If it says "Paris is the capital of Israel," that's not the point. The point is you connected correctly.
- **Prompts**: Yoram wants to see how you phrased things, what you created, how you arrived at the UI you built. Be honest and direct.
- **Repository hygiene**: Public, clean, no passwords, proper `.gitignore`, `requirements.txt` for Python.

---

## Optional (but recommended)

- [ ] Export `Udocs/ASSIGNMENT1_SUBMISSION.md` to PDF for submission if requested
- [ ] Add a `docs/images/` folder with 2–3 key screenshots
- [ ] Include a one-liner launcher script (e.g., `launch_streamlit.sh`)

---

**Reminder**: Each team member submits the document separately to Moodle.


