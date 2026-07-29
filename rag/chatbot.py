import os
from dotenv import load_dotenv
import google.generativeai as genai

from rag.retriever import get_retriever

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini Model
model = genai.GenerativeModel("gemini-3.6-flash")


def ask_question(question):
    retriever = get_retriever()

    docs = retriever.invoke(question)

    context = "\n\n".join([doc.page_content for doc in docs])

    prompt = f"""
You are an expert Git Assistant.

Answer only using the context below.

Context:
{context}

Question:
{question}

Answer:
"""

    response = model.generate_content(prompt)

    return response.text