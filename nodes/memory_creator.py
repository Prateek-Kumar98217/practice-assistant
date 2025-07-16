import json
from configs.prompts import MEMORY_CREATOR_PROMPT
from utils.logger import timed_node

class MemoryCreatorNode:
    def __init__(self, llm):
        self.llm = llm

    @timed_node("memory_creator")
    def __call__(self, state: dict) -> dict:
        user_input = state.messages[-1]

        prompt = MEMORY_CREATOR_PROMPT.format(
            user_input=user_input,
        )

        try:
            response = self.llm.invoke(prompt)
            content = response.content
            if "```json" in content:
                content = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content:
                content = content.split("```")[1].strip()
            memory_obj = json.loads(content)
        except Exception:
            memory_obj = None
        print(f"[Memory Creator]: Raw {content}")
        print(f"[Memory Creator]: {memory_obj}")
        return {
            **state.dict(),
            "structured_memory": memory_obj
        }
