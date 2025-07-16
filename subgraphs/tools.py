from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from nodes.tool_caller import ToolCaller
from core.state import GraphState

class ToolSubgraph:
    def __init__(self):
        self.tool_node = ToolCaller()

    def build(self):
        graph = StateGraph(GraphState)
        graph.add_node("tool_caller", RunnableLambda(self.tool_node.__call__))
        graph.set_entry_point("tool_caller")
        graph.add_edge("tool_caller", END)
        return graph.compile()
