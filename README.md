## 📚 Multi-Document RAG Chatbot (PDF, DOCX, TXT)
A locally running Retrieval-Augmented Generation (RAG) chatbot powered by Ollama and LangChain.
This AI assistant lets you upload documents in multiple formats and ask questions multiple times through a simple Web UI.

#🚀 Features
✔️ Runs fully local — no cloud/API required
✔️ Supports multiple document formats:
 • PDF
 • DOCX / Word
 • TXT files
✔️ RAG pipeline using LangChain
✔️ Supports multi-turn conversation
✔️ Simple Web UI built using Gradio
✔️ Uses local LLMs via Ollama (llama3, mistral, phi3, gemma, etc.)

# 🚀 Setup
Install dependencies
pip install -r requirements.txt
Install Ollama:
ollama pull gemma:2b

You can also use:
llama3
mistral
phi3
lamma2
etc.

# ▶️ To Run the Application
python app.py

# 🔧 Project Structure
.
├── main.ipynb             
├── venv
└── requirements.txt

#💡 How to Use
Start the app
Upload one or more documents
Ask any question
Ask more questions — the chat stays active
The model answers based only on your documents

# 🧪 Example Use Cases
Research assistants
Technical documentation Q&A
HR policy chatbot
Study material assistant
Legal document analysis
Financial reports summarizer


