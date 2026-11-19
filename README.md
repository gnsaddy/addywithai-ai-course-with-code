# AI Course with Code: code for every episode

Python code for the **AI Course with Code** series by **@addywithai**. Each folder matches one episode and has its own `README.md`.

## How to run any lecture

```bash
cd <folder>
python -m venv .venv
# Windows: .venv\Scripts\activate    macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt   # if the folder has one
cp .env.example .env              # only if the folder has one, then paste your own key
```

Then follow the run steps in that folder's `README.md`. Never commit your `.env` file; it is already in `.gitignore`.

Python 3.10 or newer.

## Episodes

| # | Episode | Code |
|---|---|---|
| 1 | Your First AI Program in Python | [01-first-ai-program-python](01-first-ai-program-python) |
| 2 | The LangChain Ecosystem | [02-langchain-ecosystem](02-langchain-ecosystem) |
| 3 | Learn the NGINX HTTP/2 RCE Bugs (check_nginx.py, read-only version checker): checks if your NGINX version and HTTP/2 setting are exposed, no traffic sent (2026-11-19) | [03-nginx-http2-rce-vulnerabilities](03-nginx-http2-rce-vulnerabilities) |
