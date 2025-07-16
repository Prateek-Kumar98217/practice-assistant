from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from nodes.output_synthesizer import OutputSynthesizerNode
from core.state import GraphState

class SynthesizerSubgraph:
    def __init__(self, llm):
        self.synth_node = OutputSynthesizerNode(llm)

    def build(self):
        graph = StateGraph(GraphState)
        graph.add_node("synthesizer", RunnableLambda(self.synth_node.__call__))
        graph.set_entry_point("synthesizer")
        graph.add_edge("synthesizer", END)
        return graph.compile()
