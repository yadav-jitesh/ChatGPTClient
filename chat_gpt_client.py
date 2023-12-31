import os
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key=os.getenv("OPENAPI_KEY")

question = input("What is your question?")

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role":"system","content":"You are a chatbot"},
        {"role":"user","content":f"{ question } "}
    ]
)

result = ''

for choice in response.choices:
    result += choice.message.content

print(f"we asked { question } - here is their response:")
print(result)