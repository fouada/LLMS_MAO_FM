#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment 1 - Ollama Chatbot with Flask
Course: LLMs and Multi-Agent Orchestration
Reichman University

Flask-based Chatbot Interface using Ollama
"""

from flask import Flask, render_template, request, jsonify, session
import ollama
import json
import time
from datetime import datetime
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Configuration
app.config['JSON_AS_ASCII'] = False  # Support Unicode characters


@app.route('/')
def index():
    """Main page"""
    return render_template('index.html')


@app.route('/api/models', methods=['GET'])
def get_models():
    """Get available Ollama models"""
    try:
        models = ollama.list()
        model_names = [model['name'] for model in models['models']]
        return jsonify({'success': True, 'models': model_names})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500


@app.route('/api/chat', methods=['POST'])
def chat():
    """Handle chat messages"""
    try:
        data = request.json
        user_message = data.get('message', '')
        model = data.get('model', 'llama3.2')
        temperature = data.get('temperature', 0.7)
        max_tokens = data.get('max_tokens', 2000)
        
        # Get chat history from session
        if 'messages' not in session:
            session['messages'] = []
        
        # Add user message to history
        session['messages'].append({
            'role': 'user',
            'content': user_message
        })
        
        # Call Ollama
        start_time = time.time()
        
        response = ollama.chat(
            model=model,
            messages=session['messages'],
            options={
                'temperature': temperature,
                'num_predict': max_tokens,
            }
        )
        
        end_time = time.time()
        response_time = end_time - start_time
        
        # Extract assistant response
        assistant_message = response['message']['content']
        
        # Add to history
        session['messages'].append({
            'role': 'assistant',
            'content': assistant_message
        })
        
        # Mark session as modified
        session.modified = True
        
        return jsonify({
            'success': True,
            'response': assistant_message,
            'response_time': f"{response_time:.2f}",
            'timestamp': datetime.now().strftime("%H:%M:%S")
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/clear', methods=['POST'])
def clear_history():
    """Clear chat history"""
    session['messages'] = []
    return jsonify({'success': True})


@app.route('/api/history', methods=['GET'])
def get_history():
    """Get chat history"""
    messages = session.get('messages', [])
    return jsonify({'success': True, 'messages': messages})


@app.route('/api/save', methods=['GET'])
def save_history():
    """Save chat history to file"""
    try:
        messages = session.get('messages', [])
        filename = f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(messages, f, ensure_ascii=False, indent=2)
        
        return jsonify({
            'success': True,
            'filename': filename,
            'message': f'Chat history saved to {filename}'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500


@app.route('/api/health', methods=['GET'])
def health_check():
    """Check if Ollama is available"""
    try:
        ollama.list()
        return jsonify({
            'success': True,
            'status': 'Ollama is running',
            'timestamp': datetime.now().isoformat()
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'status': 'Ollama is not available',
            'error': str(e)
        }), 503


if __name__ == '__main__':
    # Check Ollama availability on startup
    try:
        ollama.list()
        print("✅ Ollama is available")
        print("🚀 Starting Flask server...")
        print("📱 Open http://localhost:5000 in your browser")
        
        app.run(debug=True, host='0.0.0.0', port=5000)
        
    except Exception as e:
        print("❌ Error: Ollama is not available!")
        print(f"   {str(e)}")
        print("\n📋 Please ensure:")
        print("   1. Ollama is installed")
        print("   2. Ollama server is running (run 'ollama serve')")
        print("   3. At least one model is downloaded (run 'ollama pull llama3.2')")
