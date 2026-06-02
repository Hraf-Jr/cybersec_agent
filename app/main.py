import streamlit as st
from orchestrator import generate_response


st.set_page_config(
    page_title="CyberSec Agent",
    page_icon="🛡️",
    layout="centered"
)

st.title("🛡️ CyberSec Agent")
st.write(
    "Chatbot de sensibilisation à la cybersécurité. "
    "Posez une question sur les mots de passe, le phishing, le Wi-Fi, les VPN ou les bonnes pratiques."
)

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("Réinitialiser la conversation"):
    st.session_state.messages = []
    st.rerun()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

user_question = st.chat_input("Posez votre question ici...")

if user_question:
    st.session_state.messages.append({
        "role": "user",
        "content": user_question
    })

    with st.chat_message("user"):
        st.write(user_question)

    response = generate_response(user_question, st.session_state.messages)

    st.session_state.messages.append({
        "role": "assistant",
        "content": response
    })

    with st.chat_message("assistant"):
        st.write(response)