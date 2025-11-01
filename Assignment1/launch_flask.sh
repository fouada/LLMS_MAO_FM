#!/bin/bash
# Launch Flask Chatbot
# Run with: bash launch_flask.sh

echo "🚀 Starting Ollama Chatbot with Flask..."
echo ""

# Check if Ollama is running
echo "1️⃣ Checking Ollama..."
if curl -s http://localhost:11434/api/tags > /dev/null; then
    echo "✅ Ollama is running"
else
    echo "❌ Ollama is NOT running!"
    echo "   Please start it with: ollama serve"
    exit 1
fi

# Activate virtual environment
echo ""
echo "2️⃣ Activating virtual environment..."
source .venv/bin/activate

# Check packages
echo ""
echo "3️⃣ Verifying packages..."
python -c "import flask, ollama" 2>/dev/null && echo "✅ Packages installed" || { echo "❌ Packages missing! Run: uv pip install -r requirements.txt --python .venv/bin/python"; exit 1; }

# Launch Flask
echo ""
echo "4️⃣ Launching Flask chatbot..."
echo ""
echo "📝 Open your browser to: http://localhost:5000"
echo "🛑 Press Ctrl+C to stop"
echo ""

python chatbot_flask.py

