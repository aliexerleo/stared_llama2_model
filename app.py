import streamlit as st
from langchain_community.llms import Ollama

# title
st.header("Write your question")
# user input
user_question = st.text_input("")

# setup llama model and connect to the server
model = Ollama(model="llama2", base_url='http://YOUR-EC2-PUBLIC_IP:11434')

if user_question:
    # get the answer
    answer = model(user_question)
    # display the answer
    st.write(answer)
