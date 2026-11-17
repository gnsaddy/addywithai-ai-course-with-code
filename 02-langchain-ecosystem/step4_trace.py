# step4_trace.py: what LangSmith records. Every step becomes a "run".
# Real LangSmith: set LANGSMITH_TRACING=true and LANGSMITH_API_KEY,
# and the same runs go to your LangSmith project. Here we print them.
from langchain_core.tracers.base import BaseTracer
from step1_chain import chain

class PrintTracer(BaseTracer):
    def _persist_run(self, run):               # called with the root run
        self.show(run, 0)

    def show(self, run, depth):
        ms = (run.end_time - run.start_time).total_seconds() * 1000
        print(f"{'  ' * depth}{run.run_type:<7} {run.name:<20} {ms:6.1f} ms")
        for child in run.child_runs:
            self.show(child, depth + 1)

if __name__ == "__main__":
    answer = chain.invoke({"term": "RAG"},
                          config={"callbacks": [PrintTracer()]})
    print("answer:", answer)
