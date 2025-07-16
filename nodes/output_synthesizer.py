from configs.prompts import FINAL_RESPONSE_PROMPT
from utils.logger import timed_node

class OutputSynthesizerNode:
    def __init__(self, llm):
        self.llm = llm

    @timed_node("synthesizer")
    def __call__(self, state: dict) -> dict:
        planner_output = getattr(state, "planner_output", "")
        tool_output = getattr(state, "tool_output", "")
        context = getattr(state, "memories", "")
        user_input=state.messages[-1]

        prompt = FINAL_RESPONSE_PROMPT.format(
            planner_output=planner_output,
            tool_output=tool_output,
            context=context,
            input= user_input
        )

        try:
            final = self.llm.invoke(prompt)
        except Exception as e:
            final = f"(LLM Error): {str(e)}"

        return{ 
            **state.dict(),
            "final_output": final}
