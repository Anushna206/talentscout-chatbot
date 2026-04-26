import os
import streamlit as st
from groq import Groq
from dotenv import load_dotenv

# Load local environment variables
load_dotenv()

# Works both locally (.env) and on Streamlit Cloud (secrets)
api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")

# Initialize Groq client
client = Groq(api_key=api_key)


def get_llm_response(prompt):
    """
    Sends prompt to Groq LLM
    and returns generated response
    """
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content
