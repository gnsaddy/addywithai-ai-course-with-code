# Your first AI program in Python (addywithai long video, episode 1)

A terminal chatbot that talks to Google Gemini (free tier) from Python.

## Setup (Windows, Mac or Linux)
1. Install Python 3.10 or newer from python.org (on Windows tick "Add Python to PATH").
2. Open a terminal in this folder and make a virtual environment:
   - Windows: `python -m venv .venv` then `.venv\Scripts\activate`
   - Mac / Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
3. Install the libraries: `pip install -r requirements.txt`
4. Get a free API key at https://aistudio.google.com/apikey
5. Copy `.env.example` to `.env` and paste your key. Never share `.env` or push it to GitHub.

## Run
- `python list_models.py`  (step 0: checks your key, lists models)
- `python hello_ai.py`  (step 1: one question, one answer)
- `python chatbot_no_memory.py`  (step 2: a chat loop that forgets)
- `python chatbot_memory.py`  (step 3: the same loop, now with memory)
- `python chatbot.py`  (step 4: the final chatbot with a personality, streaming and error handling)

## Common errors
- `API key not valid` / `PERMISSION_DENIED`: the key in `.env` is wrong or has a space. Copy it again.
- `ModuleNotFoundError: No module named 'google'`: activate the virtual environment, then `pip install -r requirements.txt`.
- `404 ... model not found`: model names change. Run `python list_models.py` and put a flash model name in `MODEL` (e.g. `gemini-2.5-flash`).
- `429 RESOURCE_EXHAUSTED`: you hit the free limit. Wait a minute and try again.
