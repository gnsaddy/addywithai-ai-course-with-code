# stand_in_server.py: DEMO ONLY. A tiny local server that looks like an
# OpenAI-compatible chat API, so LangChain and LangGraph run with no model.
# It does not think. It follows fixed rules for the demo questions.
# A real model (run without --demo) writes its own answers.
import json, re, threading
from http.server import BaseHTTPRequestHandler, HTTPServer

LINES = {
    "RAG": "RAG means the AI first looks up your documents, then answers.",
    "embeddings": "Embeddings turn text into numbers that capture meaning.",
    "tokens": "Tokens are the small pieces of text a model reads.",
}
LONG = ("RAG, or retrieval augmented generation, is a method where the "
        "system first searches a store of documents for parts that match "
        "the question and then gives them to the model so it can answer.")
SHORT = "RAG lets the AI read your notes first, then answer."

def fake_model(messages):
    said = lambda m: m.get("content") or ""
    system, last = said(messages[0]), said(messages[-1])
    if "glossary" in system:                    # the agent (step 2)
        if messages[-1]["role"] != "tool":
            term = re.findall(r"\b[A-Z]{2,}\b", last)[0]
            return {"role": "assistant", "content": "", "tool_calls": [{
                "id": "call_1", "type": "function", "function": {
                    "name": "glossary",
                    "arguments": json.dumps({"term": term})}}]}
        return {"role": "assistant", "content": "From your notes: " + last}
    if "10 year old" in system:                 # the graph (step 3)
        return {"role": "assistant",
                "content": SHORT if "Too long" in last else LONG}
    term = last.split(": ")[-1]                 # the chain (step 1)
    return {"role": "assistant", "content": LINES.get(term, "I'm not sure.")}

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        body = json.loads(self.rfile.read(int(self.headers["Content-Length"])))
        msg = fake_model(body["messages"])
        out = json.dumps({
            "id": "demo", "object": "chat.completion", "created": 0,
            "model": body.get("model", "stand-in"),
            "choices": [{"index": 0, "message": msg, "finish_reason":
                         "tool_calls" if msg.get("tool_calls") else "stop"}],
            "usage": {"prompt_tokens": 0, "completion_tokens": 0,
                      "total_tokens": 0}}).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(out)))
        self.end_headers()
        self.wfile.write(out)
    def log_message(self, *args):
        pass

def start():
    server = HTTPServer(("127.0.0.1", 0), Handler)
    threading.Thread(target=server.serve_forever, daemon=True).start()
    return f"http://127.0.0.1:{server.server_port}/v1"
