import streamlit as st
st.title("🧠 Mental Health Support Chatbot")
user_input = st.text_input("How are you feeling today?")
if user_input:
    text = user_input.lower()
