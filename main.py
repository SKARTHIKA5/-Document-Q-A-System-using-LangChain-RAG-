# import dependencies
import os
import tempfile
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import ollama
from IPython.display import display, clear_output
import ipywidgets as widgets
import streamlit as st
import gradio as gr

db = None

# 1. Upload + Process PDF
def load_pdf(file):
    global db

    if file is None:
        return "❗ Please upload a PDF file."
      
    # Load PDF
    loader = PyPDFLoader(file.name)
    docs = loader.load()
  
    # Split text
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_documents(docs)
  
    # Embeddings
    embeddings = OllamaEmbeddings(model="gemma:2b")

    #vectorstore
    db = FAISS.from_documents(chunks, embeddings)

    return "✔ PDF successfully uploaded and indexed!"


# 2. Chat Function (No Streaming, Fixed)
def chat(query, history):
    global db
    if not query:
        return "❗ Please enter a question."

    if db is None:
        return "❗ Please upload a PDF first."

    retriever = db.as_retriever()
    docs = retriever.invoke(query)
    context = "\n\n".join([d.page_content for d in docs])
    llm = Ollama(model="gemma:2b")
    prompt = f"""
  You are an expert assistant. Use ONLY the context below to answer.

  CONTEXT:
  {context}

  QUESTION:
  {query}

  ANSWER:
  """
    # ✅ Correct method
    return llm.invoke(prompt)


# 3. Build Gradio Web UI
with gr.Blocks() as ui:
    gr.Markdown("## 📘 RAG Chatbot with Llama3 (Local, No Streaming)")
    pdf_file = gr.File(label="Upload PDF")
    upload_btn = gr.Button("Process PDF")
    upload_status = gr.Textbox(label="Status")
    upload_btn.click(load_pdf, inputs=pdf_file, outputs=upload_status)
    chatbot = gr.ChatInterface(fn=chat, title="Ask Questions About Your PDF")

ui.launch()



