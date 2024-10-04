from langchain.prompts import PromptTemplate

import streamlit as st
from groq import Groq
from constants import groq_key
from langchain_groq import ChatGroq

client=Groq(
    api_key=groq_key
)


st.title("ChefBot")

input_text=st.text_input("Name the Dish")
prompt=PromptTemplate(
    input_variables=["name"],
    template="Tell me how to make the dish named {name}"
)

llm=ChatGroq(
    api_key=groq_key,
    model="llama3-70b-8192",)
chain=prompt | llm

st.write(chain.invoke(input_text).content)