# step2_agent.py: a LangChain agent. The model decides when to use a tool.
from langchain.agents import create_agent
from langchain_core.tools import tool
from settings import make_model

NOTES = {"RAG": "Retrieval Augmented Generation: search, then answer.",
         "LLM": "Large Language Model: predicts the next token."}

@tool
def glossary(term: str) -> str:
    """Look up an AI term in my study notes."""
    return NOTES.get(term.upper(), "Not in my notes.")

agent = create_agent(
    model=make_model(),
    tools=[glossary],
    system_prompt="Use the glossary tool for AI terms. Keep it short.",
)

if __name__ == "__main__":
    result = agent.invoke({"messages": [("user", "What is RAG?")]})
    for msg in result["messages"]:
        print(f"{msg.type:>5}: {msg.content or msg.tool_calls[0]['name']}")
