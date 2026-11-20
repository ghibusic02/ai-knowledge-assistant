import os
import streamlit as st
from src.config import DATA_DIR
from src.ingestion import ingest_pdf
from src.retriever import query_knowledge_base


# Page configuration
st.set_page_config(page_title="Enterprise knowledge Assistant", page_icon="📚", layout="centered")
st.title("📚 Enterprise knowledge Assistant")
st.markdown("Upload an internal PDF file and ask questions strictly regarding its content.")

# Initialize chat history in session_state
if "messages" not in st.session_state:
    st.session_state["messages"] = []

# Ensure that data directory exists
os.makedirs(DATA_DIR, exist_ok=True)

# Sidebar for PDF upload
with st.sidebar:
    st.header("Document upload ")
    uploaded_file = st.file_uploader("Choose a PDF file", type=["PDF"])
    
    if uploaded_file is not None:
        file_path = os.path.join(DATA_DIR,uploaded_file.name)
        
        # Save and process the file only if it has not been processed in this session
        if "processed_file" not in st.session_state or st.session_state["processed_file"]!=uploaded_file.name:
            with open(file_path,"wb") as f:
                f.write(uploaded_file.getbuffer())
                
            with st.spinner("Processing document and building vector index.."):
                st.session_state["vector_store"]= ingest_pdf(file_path)
                st.session_state["processed_file"]=uploaded_file.name
                st.session_state["messages"] = [] # reset chat when a new file was uploaded
                
            st.success(f"Indexed {uploaded_file.name} successfully!")
            
    if st.button("Clear Chat History"):
        st.session_state["messages"] = []
        st.rerun()
        
    # Display chat messages from history
    for message in st.session_state["messages"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            if "sources" in message and message["sources"]:
                st.caption(f" Sources: Page(s) {','.join(map(str,message['sources']))}")
            
    # Main chat interface
    if "vector_store" in st.session_state:
        if prompt:= st.chat_input("Ask a question about the document: "):
            #display user message
            st.session_state["messages"].append({"role":"user",
                                                 "content":prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
                
            # Generate and display assistant respond
            with st.chat_message("assistant"):
                with st.spinner("Searching document..."):
                    answer, pages = query_knowledge_base(st.session_state["vector_store"],prompt)
                st.markdown(answer)
                if pages:
                    st.caption(f" Sources: ** Page(s) {','.join(map(str,pages))}")
                
                st.session_state["messages"].append({
                    "role":"assistent",
                    "content":answer,
                    "sources":pages
                })

        
    else:
        st.info("Please upload a PDF file in the sidebar to get started")
        
            
        
    
    