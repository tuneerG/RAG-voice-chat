import os

import streamlit as st
from LLM.chain import *
from src.main import *

work_dir=os.path.dirname(os.path.abspath(__file__))




st.set_page_config(
    page_title="Regional Chat-Bot",
    page_icon="🌾",
    layout="centered"
)

st.title("Agriculture Voice-Bot - Llama 3.1")

#initialise chat history in streamlit
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
    
uploaded_file=st.file_uploader(label="Upload PDF", type=["PDF"])

if uploaded_file:
    file_path = f"{work_dir}/{uploaded_file.name}"
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())


    if "vectorstore" not in st.session_state:
        st.session_state.vectorstore = set_vector_store(load_document(file_path))

    if "conversation_chain" not in st.session_state:
        st.session_state.conversation_chain = create_chain(st.session_state.vectorstore)
    

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

#TODO: Convert to voice input
user_input= st.chat_input("Ask Anything..")

if user_input:
    st.session_state.chat_history.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)


    with st.chat_message("assistant"):
        response = st.session_state.conversation_chain({"question": user_input})
        #TODO:COnvert Assitant response to voice
        assistant_response = response["answer"]
        st.markdown(assistant_response)
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_response})
