## Submission Checklist (aligned to lecture notes)

- [ ] **Repo is PUBLIC** (will not be reviewed if private)
- [ ] **PRD document exists** (Markdown or PDF)
  - Location: `Udocs/ASSIGNMENT1_SUBMISSION.md` (or `docs/PRD.md`)
  - Explains what you built and why
- [ ] **Prompts log included**
  - Paste the real prompts used to build the project
  - Location: `Udocs/ASSIGNMENT1_SUBMISSION.md` → “AI prompts we actually used” (single source of truth). You may link to extra notes if needed, but do not duplicate.
- [ ] **README contains install/run instructions**
  - Uses `requirements.txt` (no committed venv)
  - Shows how to install UV and run with venv
  - Screenshots section with images under `docs/images/`
- [ ] **.gitignore protects secrets/venv** (`.env`, `.venv/`, etc.)
- [ ] **Works with Ollama locally** (`localhost:11434`)
  - Can pull and select a small model (e.g., `llama3.2`)
  - Chat UI runs (Streamlit or Flask)
  - Conversation memory within the session
  - Graceful error handling if Ollama isn’t running
- [ ] **Quick verification commands** included (e.g., `curl` to `11434`)
- [ ] **Screenshots added** (UI up, example chat, any tests)
- [ ] **No secrets committed** (API keys, etc.)

Notes
- Accuracy of LLM responses is not graded; demonstrating correct usage and integration is.
- You may use any language/framework; this repo uses Python + Streamlit.


