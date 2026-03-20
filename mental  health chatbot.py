import streamlit as st
st.title("🧠 Mental Health Support Chatbot")
user_input = st.text_input("How are you feeling today?")
if user_input:
    text = user_input.lower()
if "sad" in text:
        st.write("I'm sorry you're feeling sad. Try listening to your favorite music or talking to a friend ❤️")

