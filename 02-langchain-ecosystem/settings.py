# settings.py: one place for the model settings.
# Any OpenAI-compatible API works: Ollama on your laptop, or a hosted one.
import os, sys

BASE_URL = os.getenv("BASE_URL", "http://localhost:11434/v1")
MODEL = os.getenv("CHAT_MODEL", "llama3.2")
API_KEY = os.getenv("API_KEY", "none")

if "--demo" in sys.argv:            # no model needed: start the stand-in
    from stand_in_server import start
    BASE_URL = start()

def make_model():
    from langchain_openai import ChatOpenAI
    return ChatOpenAI(model=MODEL, base_url=BASE_URL, api_key=API_KEY,
                      temperature=0)
