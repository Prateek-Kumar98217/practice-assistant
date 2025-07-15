import json
from configs.prompts import PLANNER_PROMPT
from utils.logger import timed_node

class PlannerNode:
    def __init__(self, llm):
        self.llm = llm

    @timed_node("planner_node")
    def __call__(self, state: dict) -> dict:
        user_input = state["messages"][-1].content
        context = state.get("memories", "")

        prompt = PLANNER_PROMPT.format(
            user_input=user_input,
            context=context
        )

        try:
            response = self.llm.invoke(prompt)
            action = json.loads(response)
        except Exception:
            action = {"action": "respond_directly", "tool_name": None, "input": user_input}

        state["planner_output"] = action
        return state
