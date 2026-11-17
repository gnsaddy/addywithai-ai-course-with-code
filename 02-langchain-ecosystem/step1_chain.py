# step1_chain.py: LangChain. A chain = prompt | model | parser.
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from settings import make_model

prompt = ChatPromptTemplate.from_messages([
    ("system", "You explain AI terms in one simple sentence."),
    ("user", "Explain: {term}"),
])
model = make_model()
parser = StrOutputParser()          # message -> plain text

chain = prompt | model | parser     # the pipe joins the steps

if __name__ == "__main__":
    print(chain.invoke({"term": "RAG"}))
    for line in chain.batch([{"term": "embeddings"}, {"term": "tokens"}]):
        print(line)
