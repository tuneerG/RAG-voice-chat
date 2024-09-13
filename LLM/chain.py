from dotenv import load_dotenv

from src import main
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

load_dotenv()

def create_chain(vectorstore):
    LLM=ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0.7)
    retriever=vectorstore.as_retriever()
    memory=ConversationBufferMemory(
        llm=LLM,
        output_key="answer",
        memory_key="chat_history",
        return_messages=True
    )
    
    chain=ConversationalRetrievalChain.from_llm(
        llm=LLM,
        retriever=retriever,
        memory=memory,
        verbose=True
    )
    
    return chain
    