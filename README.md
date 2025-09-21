# -chatbot-for-the-InfoTech-College-Website-
1.	Create a conda environment
conda create -n chatbot python=3.10 anaconda
2.	Install dependencies
pip install fastapi uvicorn langchain langchain-community langchain-ollama langchain-chroma langchain-huggingface sentence-transformers chromadb
pip install pypdf
Install Ollama -> https://ollama.com/download
ollama pull gemma3 : 1b
# InfortechGPT Chatbot - User Guide (Jupyter Notebook / Anaconda)

This guide explains how to set up and run the **InfortechGPT RAG-based PDF chatbot**
using Anaconda and Jupyter Notebook.

---

## Requirements

1. Anaconda installed with Python 3.10 or higher.
2. A folder named `docs` containing your PDF files.
3. Internet connection (to download language models if not cached).

---

## Step 1: Open Anaconda

1. Launch the **Anaconda Navigator**.
2. Open **Jupyter Notebook** from Anaconda Navigator.
3. Navigate to the folder where the chatbot files are stored.

---

## Step 2: Prepare PDF Documents

1. Create a folder named `docs` in the same directory as the notebook.
2. Place all PDF files you want the chatbot to read into the `docs` folder.

**Example folder structure:**

project_folder/
├─ InfortechGPT_notebook.ipynb
├─ docs/
├─ file1.pdf
├─ file2.pdf
