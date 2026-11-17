# Step 4: memory, personality, streaming, errors
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()
MODEL = "gemini-flash-latest"
PERSONA = "You are Addy, a friendly AI tutor. Use simple English."
config = types.GenerateContentConfig(
    system_instruction=PERSONA,
    temperature=0.7,
)
chat = client.chats.create(model=MODEL, config=config)

while True:
    question = input("You: ")
    if question.lower() == "bye":
        break
    try:
        print("Addy: ", end="")
        for chunk in chat.send_message_stream(question):
            print(chunk.text or "", end="", flush=True)
        print()
    except Exception as error:
        print("Error:", error)
