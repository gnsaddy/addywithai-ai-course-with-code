# Step 0: test your key, list the models you can use.
from dotenv import load_dotenv
from google import genai

load_dotenv()            # reads your key from .env
client = genai.Client()  # finds the key by itself

for model in client.models.list():
    if "flash" in model.name:
        print(model.name)
