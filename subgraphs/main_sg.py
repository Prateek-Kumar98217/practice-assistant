from langgraph.graph import StateGraph, END
from subgraphs.planner import PlannerSubgraph
from subgraphs.tools import ToolSubgraph
from subgraphs.synthesizer import SynthesizerSubgraph
from core.state import GraphState
from subgraphs.memory_sg import MemorySubgraph

class MainSubgraphBuilder:
    def __init__(self, planner_llm, synthesizer_llm, memory_llm):
        self.memory = MemorySubgraph(memory_llm).build()
        self.planner = PlannerSubgraph(planner_llm).build()
        self.tool = ToolSubgraph().build()
        self.synth = SynthesizerSubgraph(synthesizer_llm).build()

    def build(self):
        graph = StateGraph(GraphState)

        graph.add_node("memory_subgraph", self.memory)
        graph.add_node("planner_subgraph", self.planner)
        graph.add_node("tool_subgraph", self.tool)
        graph.add_node("synthesizer_subgraph", self.synth)

        graph.set_entry_point("memory_subgraph")
        graph.add_edge("memory_subgraph", "planner_subgraph")
        graph.add_edge("planner_subgraph", "tool_subgraph")
        graph.add_edge("tool_subgraph", "synthesizer_subgraph")
        graph.add_edge("synthesizer_subgraph", END)

        return graph.compile()

