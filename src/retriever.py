from langchain_openai import ChatOpenAI
from langchain_chroma import Chroma
from src.config import LLM_MODEL, TEMPERATURE


def query_knowledge_base(vector_store: Chroma, question: str)->tuple[str,list[int]]:
    """Retrieve the relevant chuncks and generate the response with the source pages"""
    retrieve = vector_store.as_retriever(search_kwargs={"k": 3})
    relevant_docs = retrieve.invoke(question)
    
    context = "\n\n".join([doc.page_content for doc in relevant_docs])
    sources = sorted(list(set([doc.metadata.get("page",0)+1 for doc in relevant_docs])))
    
    llm = ChatOpenAI(model=LLM_MODEL,temperature=TEMPERATURE)
    prompt =  f"""You are a helpfull enterprise assistent.Answer to the user question only using the context provided.
    If the answer isnot in the context ,please answer "I cannot find the answer in the provided document!"
    Context: {context} 
    Question: {question}"""
    response = llm.invoke(prompt)
    
    return response.content, sources

