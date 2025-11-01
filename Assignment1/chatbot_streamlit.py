#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment 1 - Ollama Chatbot with Streamlit
Course: LLMs and Multi-Agent Orchestration
Reichman University

Fancy Chatbot Interface using Ollama for local LLM inference
"""

import streamlit as st
import ollama
import time
from datetime import datetime
import json

# Configure page
st.set_page_config(
    page_title="🤖 Ollama ChatBot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        flex-direction: column;
    }
    .user-message {
        background-color: #e3f2fd;
        border-left: 4px solid #2196f3;
    }
    .assistant-message {
        background-color: #f5f5f5;
        border-left: 4px solid #4caf50;
    }
    .message-header {
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .message-timestamp {
        font-size: 0.8rem;
        color: #666;
        margin-top: 0.5rem;
    }
    .stButton>button {
        width: 100%;
    }
    h1 {
        text-align: center;
        color: #1976d2;
    }
</style>
""", unsafe_allow_html=True)


def init_session_state():
    """Initialize session state variables"""
    if "messages" not in st.session_state:
        st.session_state.messages = []
    if "model" not in st.session_state:
        st.session_state.model = "llama3.2"
    if "temperature" not in st.session_state:
        st.session_state.temperature = 0.7
    if "max_tokens" not in st.session_state:
        st.session_state.max_tokens = 2000


def get_available_models():
    """Get list of available Ollama models"""
    try:
        models = ollama.list()
        return [model['name'] for model in models['models']]
    except Exception as e:
        st.error(f"Error loading models list: {str(e)}")
        return ["llama3.2", "phi3", "mistral"]  # Fallback


def save_chat_history():
    """Save chat history to JSON file"""
    filename = f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(st.session_state.messages, f, ensure_ascii=False, indent=2)
    return filename


def load_chat_history(uploaded_file):
    """Load chat history from JSON file"""
    try:
        content = uploaded_file.read().decode('utf-8')
        messages = json.loads(content)
        st.session_state.messages = messages
        return True
    except Exception as e:
        st.error(f"Error loading history: {str(e)}")
        return False


def format_message(role, content, timestamp):
    """Format a message for display"""
    role_emoji = "👤" if role == "user" else "🤖"
    role_name = "You" if role == "user" else "ChatBot"
    message_class = "user-message" if role == "user" else "assistant-message"
    
    return f"""
    <div class="chat-message {message_class}">
        <div class="message-header">{role_emoji} {role_name}</div>
        <div>{content}</div>
        <div class="message-timestamp">🕒 {timestamp}</div>
    </div>
    """


def main():
    """Main application"""
    init_session_state()
    
    # Title
    st.title("🤖 Ollama ChatBot - Local AI Assistant")
    st.markdown("---")
    
    # Sidebar configuration
    with st.sidebar:
        st.header("⚙️ Settings")
        
        # Model selection
        available_models = get_available_models()
        st.session_state.model = st.selectbox(
            "Select Model:",
            available_models,
            index=0 if not available_models else available_models.index(st.session_state.model) if st.session_state.model in available_models else 0
        )
        
        # Temperature slider
        st.session_state.temperature = st.slider(
            "Temperature (Creativity):",
            min_value=0.0,
            max_value=2.0,
            value=st.session_state.temperature,
            step=0.1,
            help="Low value = more precise answers, High value = more creative answers"
        )
        
        # Max tokens slider
        st.session_state.max_tokens = st.slider(
            "Maximum Tokens:",
            min_value=100,
            max_value=4000,
            value=st.session_state.max_tokens,
            step=100
        )
        
        st.markdown("---")
        
        # Chat history management
        st.subheader("📝 Chat Management")
        
        col1, col2 = st.columns(2)
        
        with col1:
            if st.button("🗑️ Clear Chat"):
                st.session_state.messages = []
                st.rerun()
        
        with col2:
            if st.button("💾 Save Chat"):
                if st.session_state.messages:
                    filename = save_chat_history()
                    st.success(f"Saved to: {filename}")
                else:
                    st.warning("No chat to save")
        
        # Load chat history
        uploaded_file = st.file_uploader("📂 Load Saved Chat", type=['json'])
        if uploaded_file is not None:
            if load_chat_history(uploaded_file):
                st.success("Chat loaded successfully!")
                st.rerun()
        
        st.markdown("---")
        
        # Statistics
        st.subheader("📊 Statistics")
        st.metric("Total Messages", len(st.session_state.messages))
        
        user_messages = len([m for m in st.session_state.messages if m['role'] == 'user'])
        assistant_messages = len([m for m in st.session_state.messages if m['role'] == 'assistant'])
        
        col1, col2 = st.columns(2)
        col1.metric("Your Messages", user_messages)
        col2.metric("Bot Responses", assistant_messages)
        
        st.markdown("---")
        
        # Info
        st.info("""
        💡 **Usage Tips:**
        - Write clear questions
        - Try different temperatures
        - Save interesting conversations
        - Switch models as needed
        """)
    
    # Main chat area
    chat_container = st.container()
    
    with chat_container:
        # Display chat history
        for message in st.session_state.messages:
            st.markdown(
                format_message(
                    message['role'],
                    message['content'],
                    message.get('timestamp', 'N/A')
                ),
                unsafe_allow_html=True
            )
    
    # Chat input
    st.markdown("---")
    
    # Create two columns for input and button
    col1, col2 = st.columns([5, 1])
    
    with col1:
        user_input = st.text_input(
            "Type your message:",
            key="user_input",
            placeholder="Ask me anything... 💬",
            label_visibility="collapsed"
        )
    
    with col2:
        send_button = st.button("📤 Send", use_container_width=True)
    
    # Process user input
    if send_button and user_input:
        # Add user message
        timestamp = datetime.now().strftime("%H:%M:%S")
        st.session_state.messages.append({
            'role': 'user',
            'content': user_input,
            'timestamp': timestamp
        })
        
        # Display user message immediately
        st.markdown(
            format_message('user', user_input, timestamp),
            unsafe_allow_html=True
        )
        
        # Generate response
        with st.spinner('🤔 ChatBot is thinking...'):
            try:
                start_time = time.time()
                
                # Call Ollama API
                response = ollama.chat(
                    model=st.session_state.model,
                    messages=[
                        {'role': m['role'], 'content': m['content']}
                        for m in st.session_state.messages
                    ],
                    options={
                        'temperature': st.session_state.temperature,
                        'num_predict': st.session_state.max_tokens,
                    }
                )
                
                end_time = time.time()
                response_time = end_time - start_time
                
                # Extract response
                assistant_message = response['message']['content']
                
                # Add assistant message
                response_timestamp = datetime.now().strftime("%H:%M:%S")
                st.session_state.messages.append({
                    'role': 'assistant',
                    'content': assistant_message,
                    'timestamp': response_timestamp,
                    'response_time': f"{response_time:.2f}s"
                })
                
                # Show success message
                st.success(f"✅ Response received in {response_time:.2f} seconds")
                
                # Rerun to show the new message
                st.rerun()
                
            except Exception as e:
                st.error(f"❌ Error: {str(e)}")
                st.info("""
                **Please check:**
                1. Is Ollama running? (`ollama serve`)
                2. Is the model downloaded? (`ollama pull llama3.2`)
                3. Is there a connection to the server?
                """)


if __name__ == "__main__":
    # Check if Ollama is available
    try:
        ollama.list()
        main()
    except Exception as e:
        st.error("❌ Cannot connect to Ollama!")
        st.warning("""
        **Please ensure:**
        1. Ollama is installed on your computer
        2. The server is running (run `ollama serve` in terminal)
        3. At least one model is downloaded (`ollama pull llama3.2`)
        
        **Installation:**
        - macOS: `brew install ollama`
        - Or: `curl -fsSL https://ollama.com/install.sh | sh`
        
        **Start Server:**
        ```
        ollama serve
        ```
        
        **Download Model:**
        ```
        ollama pull llama3.2
        ```
        """)
        st.stop()
