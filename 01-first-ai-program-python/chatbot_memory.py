# Step 3: the same loop, now with memory
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()
chat = client.chats.create(model="gemini-flash-latest")

while True:
    question = input("You: ")
    if question.lower() == "bye":
        break
    response = chat.send_message(question)
    print("AI:", response.text)
