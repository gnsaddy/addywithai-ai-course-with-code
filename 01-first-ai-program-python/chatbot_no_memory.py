# Step 2: a chat loop (it forgets!)
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()

while True:
    question = input("You: ")
    if question.lower() == "bye":
        break
    response = client.models.generate_content(
        model="gemini-flash-latest",
        contents=question,
    )
    print("AI:", response.text)
