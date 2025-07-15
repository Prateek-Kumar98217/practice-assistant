from configs.prompts import FINAL_RESPONSE_PROMPT
from utils.logger import timed_node

class OutputSynthesizerNode:
    def __init__(self, llm):
        self.llm = llm

    @timed_node("synthesizer")
    def __call__(self, state: dict) -> dict:
        planner_action = state.get("planner_output", {})
        tool_output = state.get("tool_output", "")
        context = state.get("memories", "")

        prompt = FINAL_RESPONSE_PROMPT.format(
            tool_output=tool_output,
            context=context,
            input=planner_action.get("input", "")
        )

        try:
            final = self.llm.invoke(prompt)
        except Exception as e:
            final = f"(LLM Error): {str(e)}"

        state["final_output"] = final
        return state
