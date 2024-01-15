import streamlit as st
from langchain_community.llms import Ollama

st.header("Write your question")
user_question = st.text_input("")
model = Ollama(model="llama2")

if user_question:
    if len(user_question) > 10:
        result = model(user_question)
        st.write(result)
