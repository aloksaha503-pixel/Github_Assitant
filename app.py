import random
import streamlit as st
from rag.chatbot import ask_question

st.set_page_config(
    page_title="Git Repo Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 :green[Git Repo] Assistant")

st.caption(
    "Your AI-powered assistant for learning Git and GitHub."
)
st.divider()

spinner_messages = [
    "📡 Contacting NASA...",
    "👽 Calling aliens for advice...",
    "🙏🏼 Asking God...",
    "🧙 Asking your toper friend...",
    "💻 Calling Stephen Hawking..",
]

question = st.text_area(
    "Ask your question",
    placeholder="Example: Explain the difference between git merge and git rebase.",
    height=70
)


ask = st.button("🚀 Ask", use_container_width=True)


if ask:

    if not question.strip():
        st.warning("⚠️ Please enter a question.")
    else:

        with st.spinner(random.choice(spinner_messages)):
            answer = ask_question(question)

        st.success("✅ Answer")
        st.write(answer)

st.divider()

st.caption("Created by JEET • SANIYA • SNIGDHA • ABHIJIT • ALOK")