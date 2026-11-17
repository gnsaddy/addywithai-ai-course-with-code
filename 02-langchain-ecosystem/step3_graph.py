# step3_graph.py: LangGraph. Write -> check -> (too long? write again).
from typing import TypedDict
from langgraph.graph import END, START, StateGraph
from settings import make_model

class State(TypedDict):
    term: str
    draft: str
    feedback: str
    tries: int

model = make_model()

def write(state: State):                       # an LLM step
    ask = f"Explain {state['term']}. {state['feedback']}"
    msgs = [("system", "Explain like I am a 10 year old."), ("user", ask)]
    return {"draft": model.invoke(msgs).content, "tries": state["tries"] + 1}

def check(state: State):                       # a plain Python step
    words = len(state["draft"].split())
    print(f"try {state['tries']}: {words} words")
    if words > 20:
        return {"feedback": f"Too long: {words} words. Use at most 20."}
    return {"feedback": ""}

def route(state: State):                       # pick the next node
    if state["feedback"] and state["tries"] < 3:
        return "write"
    return END

graph = StateGraph(State)
graph.add_node("write", write)
graph.add_node("check", check)
graph.add_edge(START, "write")
graph.add_edge("write", "check")
graph.add_conditional_edges("check", route, ["write", END])
app = graph.compile()

if __name__ == "__main__":
    out = app.invoke({"term": "RAG", "draft": "", "feedback": "", "tries": 0})
    print("final:", out["draft"])
