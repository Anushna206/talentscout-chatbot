import os
from groq import Groq
from dotenv import load_dotenv

# Loads API credentials securely from environment file
# force load latest .env file
load_dotenv(dotenv_path=".env", override=True)

api_key = os.getenv("GROQ_API_KEY")

print("Current API key being used:", api_key[:10])   # only prints first few chars
# Initializes Groq LLM client
client = Groq(api_key=api_key)

# Sends prompt to LLM and returns generated response
def get_llm_response(prompt):
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