# Learn LangChain, LangGraph, Langflow and LangSmith (code)

Small, runnable Python files for the long YouTube video (2026-11-10). One running example: an "explain an AI term" helper. Python 3.10+, CPU only, no paid keys.

| File | What it shows |
|---|---|
| `settings.py` | Model settings (`BASE_URL`, `CHAT_MODEL`, `API_KEY`) and `make_model()` (ChatOpenAI pointed at any OpenAI-compatible API). `--demo` starts the stand-in server. |
| `step1_chain.py` | **LangChain**: a chain = `prompt \| model \| parser`. `invoke()` for one input, `batch()` for many. |
| `step2_agent.py` | **LangChain 1.0** agent with `create_agent()` and one `@tool` (a glossary lookup). Prints every message: human → AI tool call → tool → AI answer. |
| `step3_graph.py` | **LangGraph**: a `StateGraph` with a `write` node (LLM step), a `check` node (plain Python word count) and a conditional edge that loops back until the answer is 20 words or less (max 3 tries). |
| `step4_trace.py` | **What LangSmith records**: a tiny tracer prints the run tree (chain → prompt, model, parser, with times). LangSmith stores the same kind of runs for every request. |
| `step5_langsmith.py` | **LangSmith for real**: the 3 settings + `@traceable`. With no settings it just runs locally. |
| `stand_in_server.py` | DEMO ONLY: a tiny local server that looks like an OpenAI-compatible chat API and answers with fixed rules for the demo questions. It does not think. LangChain and LangGraph talk to it over HTTP, so the framework code runs for real. |

## Demo (no model, no key)
```
pip install -r requirements.txt
python step1_chain.py --demo
python step2_agent.py --demo
python step3_graph.py --demo
python step4_trace.py --demo
python step5_langsmith.py --demo
```

## Real run with a free local model
1. Install [Ollama](https://ollama.com) and pull a model that supports tool calling, e.g. `ollama pull llama3.2`.
2. Copy `.env.example` values into your environment (`BASE_URL`, `CHAT_MODEL`).
3. Run the files without `--demo`. A real model words things its own way and may take a different number of steps.

## LangSmith (optional)
Make a LangSmith account, create an API key, then set `LANGSMITH_TRACING=true`, `LANGSMITH_API_KEY` and `LANGSMITH_PROJECT` (for a non-US region such as the EU, also set `LANGSMITH_ENDPOINT`, see the LangSmith docs). LangChain and LangGraph runs are then traced with no code change; `@traceable` traces your own functions. Keep the key out of your code.

## Langflow (optional)
Langflow is a separate open source project (not made by LangChain). Install and start it with `uv pip install langflow` and `uv run langflow run`, then open http://localhost:7860 (tested with Langflow 1.13.1; the Desktop app or Docker also work).

## Notes
- Tested on 2026-11-10 with the versions in `requirements.txt`. These libraries change fast; if something breaks, check the current docs for your version.
- Facts in the video come from the official LangChain docs (LangChain 1.0 release notes, LangGraph overview, LangSmith docs) and the Langflow docs.
