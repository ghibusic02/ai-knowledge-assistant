from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from src.config import (EMBEDDING_MODEL,
                        CHUNK_SIZE,
                        CHUNK_OVERLAP,
                        CHROMA_DB_DIR)

def ingest_pdf(pdf_path: str)->Chroma:
    """Load a pdf, split it into chuncks and store embeddings into ChromaDB"""
    
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size = CHUNK_SIZE,
        chunk_overlap = CHUNK_OVERLAP
    )
    chunks = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=CHROMA_DB_DIR
    )
    
    return vector_store

def load_existing_vector_store()->Chroma:
    """Load an already created instance of ChromaDB from disk"""
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL)
    return Chroma(
        embedding_function=embeddings,
        persist_directory=CHROMA_DB_DIR
    )