# step5_langsmith.py: send real traces to LangSmith (account + API key).
# 1) Set these in your terminal or .env file:
#      LANGSMITH_TRACING=true
#      LANGSMITH_API_KEY=<your key>
#      LANGSMITH_PROJECT=langchain-ecosystem
# 2) LangChain and LangGraph runs are traced with no code change.
# 3) Your own Python functions: add @traceable.
from langsmith import traceable
from step1_chain import chain

@traceable(name="explain_term")
def explain(term: str) -> str:
    return chain.invoke({"term": term})

if __name__ == "__main__":
    print(explain("RAG"))
