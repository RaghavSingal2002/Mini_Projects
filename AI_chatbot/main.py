import os
from openai import OpenAI
from dotenv import load_dotenv
import time

load_dotenv()

messages = []

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def completion(message):
    global messages
    messages.append(
        {
            "role": "user",
            "content": message
        }
    )

    chat_completion = client.chat.completions.create(
        messages=messages,
        model="gpt-4o"
    )

    reply = chat_completion.choices[0].message.content
    messages.append({"role": "assistant", "content": reply})
    print(f"Jarvis: {reply}")

if __name__ == "__main__":
    print("Jarvis: Hi I am Jarvis, How may I help you?\n")
    while True:
        user_question = input("User: ")
        if user_question.lower() in ["exit", "quit"]:
            print("Jarvis: Goodbye!")
            break
        completion(user_question)
