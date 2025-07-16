from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda
from nodes.planner_node import PlannerNode
from core.state import GraphState
class PlannerSubgraph:
    def __init__(self, llm):
        self.planner_node = PlannerNode(llm)

    def build(self):
        graph = StateGraph(GraphState)
        graph.add_node("planner", RunnableLambda(self.planner_node.__call__))
        graph.set_entry_point("planner")
        graph.add_edge("planner", END)
        return graph.compile()
