# Assignment 1: Ollama Chatbot - Submission Document

**Course**: LLMs and Multi-Agent Orchestration  
**Institution**: Reichman University  
**Student**: [Your Name Here]  
**Partner**: [Partner Name Here]  
**Date**: November 4, 2025

---

## 1. Product Requirements Document (PRD)

### Project Goal
Create a chatbot interface similar to ChatGPT/Gemini/Claude, but using **Ollama** (local LLM) instead of cloud APIs.

### Requirements
- ✅ Connect to Ollama API (localhost:11434)
- ✅ Build a GUI interface (web-based or desktop)
- ✅ Send user messages to Ollama
- ✅ Display AI responses
- ✅ Maintain conversation history
- ✅ Allow model selection
- ✅ Handle errors gracefully

### Technology Choices
- **LLM**: Ollama (local, no API key needed)
- **Model**: llama3.2 (or any small model)
- **Frontend**: Streamlit (web interface)
- **Language**: Python
- **API Client**: Ollama Python SDK

### Why These Choices?
- **Ollama**: Free, runs locally, no API costs
- **Streamlit**: Fast to build, good for prototyping
- **Python**: Industry standard for AI/ML

---

## 2. AI Prompts Used to Create This Project

### Prompt #1: [Initial Setup]
**Date**: [Your Date]  
**AI Tool**: [ChatGPT/Claude/Cursor]

```
[PASTE YOUR ACTUAL PROMPT HERE]

Example:
"I need to create a chatbot for my assignment that connects to Ollama 
running locally. It should have a web interface where users can type 
messages and see responses. Can you help me set this up with Python?"
```

**What I Received**:
- [Describe what code/suggestions the AI gave you]

**What I Learned**:
- [What technical concept you understood from this]

---

### Prompt #2: [Feature/Problem]
**Date**: [Your Date]

```
[YOUR SECOND PROMPT]

Example:
"The chatbot forgets previous messages. How do I maintain conversation 
history when calling Ollama API?"
```

**What I Received**:
- [AI's response]

**What I Learned**:
- [Your learning]

---

### Prompt #3: [Another Feature/Issue]
**Date**: [Your Date]

```
[YOUR THIRD PROMPT]
```

**What I Received**:  
**What I Learned**:

---

### [Add more prompts as needed - include 3-7 significant prompts]

---

## 3. What We Created

### Project Structure
```
Assignment1/
├── chatbot_streamlit.py      # Main application
├── requirements.txt          # Python dependencies
├── launch_streamlit.sh       # Launch script
├── .gitignore               # Git ignore file
└── Udocs/                    # This documentation
```

### Architecture Diagram
```
User types message
    ↓
Streamlit Interface (Frontend)
    ↓
Ollama Python SDK
    ↓
Ollama API (localhost:11434)
    ↓
LLM Model (llama3.2)
    ↓
Response back to user
```

### Key Components

#### 1. Ollama Connection Code
```python
import ollama

# Connect to Ollama and send message
response = ollama.chat(
    model='llama3.2',
    messages=[
        {"role": "user", "content": "Hello!"}
    ]
)

# Get response
assistant_reply = response['message']['content']
```

#### 2. Conversation History Management
```python
# Store messages in Streamlit session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Add user message
st.session_state.messages.append({
    "role": "user", 
    "content": user_input
})

# Send entire history to Ollama
response = ollama.chat(
    model=selected_model,
    messages=st.session_state.messages  # Full history
)
```

#### 3. User Interface
```python
import streamlit as st

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Type your message..."):
    # Process and respond
```

---

## 4. How We Got to the GUI

### Design Process

**Step 1: Technology Selection**
- Considered: HTML/JavaScript, Flask, Streamlit, Desktop app
- **Chose Streamlit** because:
  - Fast to build
  - Built-in chat components
  - No HTML/CSS needed
  - Auto-refresh on code changes

**Step 2: Interface Layout**
```
┌─────────────────────────────────────────┐
│  Ollama Chatbot          [Sidebar →]   │
├─────────────────────────────────────────┤
│                                         │
│  👤 User: Hello!                        │
│  🤖 Bot: Hi! How can I help?            │
│                                         │
│  👤 User: What is Python?               │
│  🤖 Bot: Python is a programming...     │
│                                         │
├─────────────────────────────────────────┤
│  💬 Type your message... [Send]         │
└─────────────────────────────────────────┘

Sidebar:
┌─────────────┐
│ Model:      │
│ ▼ llama3.2  │
│   mistral   │
│             │
│ [Clear]     │
└─────────────┘
```

**Step 3: Implementation**
1. Created basic Streamlit app skeleton
2. Added Ollama connection
3. Implemented message display
4. Added conversation history
5. Added model selection
6. Added error handling

**Step 4: Testing**
- Tested with various prompts
- Verified conversation memory works
- Tested model switching
- Tested error cases (Ollama not running)

---

## 5. How to Launch the Application

### Prerequisites
```bash
# 1. Install Ollama (one-time setup)
brew install ollama

# 2. Pull a model (one-time setup)
ollama pull llama3.2

# 3. Install UV for package management (recommended by lecturer)
brew install uv

# 4. Clone repository
git clone [your-repo-url]
cd Assignment1
```

### Launch Steps

**Terminal 1: Start Ollama**
```bash
ollama serve
```

**Terminal 2: Run Application**
```bash
cd Assignment1

# Create virtual environment (first time only)
python3 -m venv .venv

# Activate
source .venv/bin/activate

# Install dependencies (first time only)
uv pip install -r requirements.txt

# Launch app
streamlit run chatbot_streamlit.py
```

**Access the Application**
- Open browser: http://localhost:8501

### Quick Launch (Using Script)
```bash
bash launch_streamlit.sh
```

---

## 6. How to Use the GUI

### Using the Chatbot

**Step 1: Select Model**
- Look at the sidebar on the left
- Click the dropdown menu
- Choose a model (e.g., llama3.2)

**Step 2: Type a Message**
- Find the text input box at the bottom
- Type your question or prompt
- Press Enter or click Send

**Step 3: View Response**
- The bot's response appears in the chat area
- Your message shows with 👤 icon
- Bot's response shows with 🤖 icon

**Step 4: Continue Conversation**
- Type follow-up questions
- The bot remembers previous messages
- Conversation history is maintained

**Step 5: Clear Chat (Optional)**
- Click "Clear Chat" button in sidebar
- Starts fresh conversation

### Example Conversation
```
You: Hello!
Bot: Hi! How can I help you today?

You: What's 2+2?
Bot: 2+2 equals 4.

You: And what's 3+3?
Bot: 3+3 equals 6.
```

### Features
- ✅ Real-time responses
- ✅ Conversation memory
- ✅ Multiple model support
- ✅ Clear error messages
- ✅ Simple, clean interface

---

## 7. Technical Implementation Details

### 7.1 How Ollama API Works

**Connection**:
- Ollama runs as a local service on port 11434
- No API key needed (local service)
- Access via `http://localhost:11434`

**API Call Structure**:
```python
import ollama

response = ollama.chat(
    model='llama3.2',           # Which model to use
    messages=[                   # Conversation history
        {"role": "user", "content": "Hello"},
        {"role": "assistant", "content": "Hi!"},
        {"role": "user", "content": "How are you?"}
    ]
)

# Response structure
{
    "message": {
        "role": "assistant",
        "content": "I'm doing well, thank you!"
    },
    "model": "llama3.2",
    "created_at": "...",
    "done": true
}
```

**Why Send Full History?**
- LLMs are stateless (no memory)
- Must send complete conversation each time
- This is how the bot "remembers" context

### 7.2 Error Handling

```python
try:
    response = ollama.chat(model=model, messages=messages)
except Exception as e:
    st.error(f"Error: {e}")
    st.info("Make sure Ollama is running: ollama serve")
```

### 7.3 Session Management

```python
# Streamlit session state persists across reruns
if "messages" not in st.session_state:
    st.session_state.messages = []

# Add messages
st.session_state.messages.append(new_message)

# Access anywhere in the app
all_messages = st.session_state.messages
```

---

## 8. What We Learned

### Technical Skills
1. **API Integration**: Learned how to connect to Ollama API using Python SDK
2. **LLM Concepts**: Understood that LLMs are stateless and need full context
3. **Message Format**: Learned the role/content structure for conversations
4. **Web Development**: Built a web interface with Streamlit
5. **Error Handling**: Implemented proper error checking and user feedback

### Key Insights
- **Local LLMs**: Ollama allows running models locally without API costs
- **Conversation History**: Must send entire message history for context
- **Model Selection**: Different models have different capabilities and speeds
- **User Experience**: Simple interfaces can be powerful

### Challenges Solved
1. **Challenge**: Chatbot forgot previous messages
   - **Solution**: Send full message history in each API call
   
2. **Challenge**: Application crashed when Ollama wasn't running
   - **Solution**: Added try-catch error handling with helpful messages

3. **Challenge**: UI needed to update after each message
   - **Solution**: Used Streamlit's session state and rerun()

---

## 9. Repository Information

**Repository URL**: [Your GitHub/GitLab URL]

**Repository is PUBLIC**: ✅ Yes

**Files Included**:
- ✅ Source code (chatbot_streamlit.py)
- ✅ Dependencies (requirements.txt)
- ✅ Launch script (launch_streamlit.sh)
- ✅ Documentation (this file)
- ✅ .gitignore (excludes .venv, __pycache__, etc.)

---

## 10. Verification Checklist

- [x] Application launches without errors
- [x] Connects to Ollama API successfully
- [x] Sends user messages to LLM
- [x] Displays responses correctly
- [x] Maintains conversation history
- [x] Allows model selection
- [x] Handles errors gracefully
- [x] GUI is functional and user-friendly
- [x] Documentation is complete
- [x] Repository is public and accessible

---

## Conclusion

This project demonstrates understanding of:
- ✅ Connecting to Ollama API (localhost:11434)
- ✅ Sending messages and receiving responses
- ✅ Building a functional GUI interface
- ✅ Managing conversation state
- ✅ Error handling and user experience

**Note**: As per course requirements, accuracy of chatbot answers is not evaluated. The focus is on demonstrating technical ability to integrate with Ollama API and build a working interface.

---

**Submitted by**: [Your Name]  
**Date**: November 4, 2025  
**Course**: LLMs and Multi-Agent Orchestration  
**Reichman University**

