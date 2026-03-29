import streamlit as st
st.set_page_config(page_title="Mental Health Chatbot", page_icon="🧠")
st.title("🧠 Mental Health Support Chatbot")
if "messages" not in st.session_state:
    st.session_state.messages = []
user_input = st.text_input("How are you feeling today?")
def get_response(text):
    text = text.lower()
if any(word in text for word in ["sad", "depressed", "low"]):
          return "I'm really sorry you're feeling this way 💙 Try talking to someone you trust or doing something you enjoy."



