import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()


def get_llm(temperature: float = 0.2):

    api_key = os.getenv("GROQ_API_KEY")

    return ChatGroq(
        model="llama-3.1-8b-instant", temperature=temperature, api_key=api_key
    )
