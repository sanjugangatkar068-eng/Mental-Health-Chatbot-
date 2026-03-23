import streamlit as st
st.set_page_config(page_title="Mental Health Chatbot", page_icon="🧠")
st.title("🧠 Mental Health Support Chatbot")
if "messages" not in st.session_state:
    st.session_state.messages = []


