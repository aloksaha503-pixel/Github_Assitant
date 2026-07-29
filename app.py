import streamlit as st
from rag.chatbot import ask_question

st.set_page_config(
    page_title="Git Repo Assistant",
    page_icon="🤖",
)

st.title("🤖 Git Repo Assistant")
st.write("Ask any Git or GitHub-related question.")

question = st.text_input("Enter your question:")

if st.button("Ask") and question:
    with st.spinner("Thinking..."):
        answer = ask_question(question)

    st.success("Answer")
    st.write(answer)