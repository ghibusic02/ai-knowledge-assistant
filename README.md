# 📚 Enterprise Knowledge Assistant (RAG Pipeline)

A modular Retrieval-Augmented Generation (RAG) web application built with **Python**, **LangChain**, **ChromaDB**, **OpenAI**, and **Streamlit**. It allows users to upload PDF documents and ask questions with answers strictly grounded in the document's content, complete with page citations.

##  Key Features
- **Modular Architecture:** Clean separation between document ingestion, vector retrieval, configuration, and UI.
- **Grounded Responses:** Reduces AI hallucinations by instructing the LLM to answer strictly from retrieved context.
- **Source Citations:** Automatically extracts and displays the exact PDF page numbers used to generate each answer.
- **Interactive Chat UI:** Built with Streamlit session state for continuous multi-turn conversations.

##  Tech Stack
- **Language:** Python 3.11+
- **LLM & Embeddings:** OpenAI (`gpt-4o-mini` & `text-embedding-3-small`)
- **Orchestration:** LangChain
- **Vector Database:** ChromaDB
- **Frontend:** Streamlit

##  Setup & Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/ghibusic02/ai-knowledge-assistant.git
   cd ai-knowledge-assistant
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the root directory and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your_openai_api_key_here
   ```
5. Run the application:
   ```bash
   python -m streamlit run .\src\app.py
   ```
