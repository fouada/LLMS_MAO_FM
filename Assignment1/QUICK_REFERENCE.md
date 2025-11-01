# ⚡ Quick Reference Card

## 🚀 Launch Commands

```bash
# Streamlit (Recommended)
bash launch_streamlit.sh

# Flask (Alternative)
bash launch_flask.sh

# Manual Streamlit
source .venv/bin/activate && streamlit run chatbot_streamlit.py

# Manual Flask
source .venv/bin/activate && python chatbot_flask.py
```

## 🌐 URLs

- **Streamlit:** http://localhost:8501
- **Flask:** http://localhost:5000
- **Ollama API:** http://localhost:11434

## 🛠️ Common Commands

```bash
# Check Ollama
curl http://localhost:11434/api/tags

# List Ollama models
ollama list

# Pull a model
ollama pull llama3.2

# Start Ollama
ollama serve

# Activate venv
source .venv/bin/activate

# Install packages
uv pip install -r requirements.txt --python .venv/bin/python

# Check Python
which python
```

## 🐛 Quick Fixes

**Ollama not responding:**
```bash
ollama serve
```

**Missing packages:**
```bash
source $HOME/.local/bin/env
source .venv/bin/activate
uv pip install -r requirements.txt --python .venv/bin/python
```

**Port in use:**
```bash
# Kill process on port 8501
lsof -i :8501 | grep LISTEN | awk '{print $2}' | xargs kill -9

# Kill process on port 5000
lsof -i :5000 | grep LISTEN | awk '{print $2}' | xargs kill -9
```

## 📁 File Structure

```
Assignment1/
├── chatbot_streamlit.py   # Main Streamlit app
├── chatbot_flask.py        # Main Flask app
├── requirements.txt        # Dependencies
├── .venv/                  # Virtual environment
├── launch_streamlit.sh     # Quick launch (Streamlit)
├── launch_flask.sh         # Quick launch (Flask)
└── LAUNCH_GUIDE.md         # Detailed guide
```

## 🎯 Test Questions

Try these in your chatbot:

```
1. Hello! What can you help me with?
2. Write a Python function to reverse a string
3. Explain what a REST API is
4. Remember that my favorite color is blue. What's my favorite color?
```

## ⌨️ Keyboard Shortcuts

**In Terminal:**
- `Ctrl + C` - Stop server
- `Ctrl + Z` - Suspend (then `fg` to resume)

**In Streamlit:**
- Auto-reloads on file save
- No restart needed!

**In Flask:**
- Must restart after code changes
- Use debug mode for auto-reload

## 📊 System Check

```bash
# One-liner status check
curl -s http://localhost:11434/api/tags > /dev/null && echo "✅ Ollama" || echo "❌ Ollama"; \
python -c "import streamlit, flask, ollama" 2>/dev/null && echo "✅ Packages" || echo "❌ Packages"
```

## 🎓 Development Tips

1. **Edit → Save → Auto-reload** (Streamlit only)
2. **Check terminal** for errors
3. **Use browser DevTools** for debugging
4. **Test with simple prompts** first
5. **Add features incrementally**

## 🆘 Help Commands

```bash
# UV help
uv --help

# Ollama help
ollama --help

# Streamlit help
streamlit --help

# Python packages
pip list
```

---
**Quick Start:** `cd Assignment1 && bash launch_streamlit.sh`

