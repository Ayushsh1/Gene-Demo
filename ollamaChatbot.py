
import os
import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


prompt = ChatPromptTemplate.from_messages(
    [
        # System message defines AI behavior
        ("system", "You are a helpful assistant. Please respond clearly to the question asked."),
        
        # User message contains placeholder {question}
        ("user", "Question: {question}")
    ]
)

st.title("LangChain Demo with Gemma Model (Ollama)")
input_text = st.text_input("What question do you have in mind?")

llm = Ollama(model="gemma2:2b")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)
