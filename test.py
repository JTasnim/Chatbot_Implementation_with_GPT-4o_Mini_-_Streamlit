import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import tiktoken
enc = tiktoken.encoding_for_model("gpt-4o-mini")

load_dotenv()

client = OpenAI()


# system = st.text_input("System:", "You are a helpful assistant.")
# prompt = st.text_input("Your Prompt:")


stream = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        # {"role": "user", "content": system},
        {"role": "user", "content": "How to make a pizza?"}
    ],
    stream=True
)
for chunk in stream:
    token = chunk.choices[0].delta.content
    if token is not None:
        print(token, end="")
