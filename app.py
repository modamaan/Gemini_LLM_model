from dotenv import load_dotenv
load_dotenv() # Loading all variables

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# function load geminiai pro model and get responses
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):  
    response = model.generate_content(question)
    return response.text

# initialize streamlit app
st.set_page_config(page_title="Q&A Demo")
# st.header("Gemini Speak LLM")
st.markdown('<h2 style="color: skyblue;">Gemini Speak LLM</h2>', unsafe_allow_html=True)
st.subheader("Ask Your Question")
input = st.text_input("Input: ",key="input")
submit = st.button("Ask the question")

# when submit is clicked
if submit:
    response = get_gemini_response(input)
    st.subheader("The Response is")
    st.write(response)
