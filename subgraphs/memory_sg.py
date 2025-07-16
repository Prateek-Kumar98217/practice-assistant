from langgraph.graph import StateGraph
from core.state import GraphState

from nodes.memory_retriever import MemoryRetrieverNode
from nodes.memory_creator import MemoryCreatorNode
from nodes.memory_updater import MemoryUpdaterNode

class MemorySubgraph:
    def __init__(self, llm):
        self.retriever = MemoryRetrieverNode()
        self.creator = MemoryCreatorNode(llm=llm)
        self.updater = MemoryUpdaterNode()

    def build(self):
        graph = StateGraph(GraphState)

        graph.add_node("memory_retriever", self.retriever)
        graph.add_node("memory_creator", self.creator)
        graph.add_node("memory_updater", self.updater)

        graph.set_entry_point("memory_retriever")
        graph.add_edge("memory_retriever", "memory_creator")
        graph.add_edge("memory_creator", "memory_updater")
        graph.set_finish_point("memory_updater")

        return graph.compile()
