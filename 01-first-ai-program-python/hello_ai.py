# Step 1: ask AI one question, print the answer.
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client()

response = client.models.generate_content(
    model="gemini-flash-latest",
    contents="Explain what an API is in one simple sentence.",
)
print(response.text)
