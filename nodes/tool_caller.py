from tools import get_tool
from utils.logger import timed_node

class ToolCaller:
    def __init__(self):
        pass

    @timed_node("tool_caller")
    def __call__(self, state):
        action = getattr(state, "planner_output", None)

        if not isinstance(action, dict):
            return {
                **state.dict(),
                "tool_output": "Invalid planner output: expected dict, got None or invalid type."
            }

        tool_name = action.get("tool_name")
        tool_input = action.get("input", "")

        tool_func = get_tool(tool_name)
        if not tool_func:
            return {
                **state.dict(),
                "tool_output": f"Tool '{tool_name}' not found."
            }
        
        print(f"[Tool Caller]]: {result}")
        
        result = tool_func(tool_input)
        return {
            **state.dict(),
            "tool_output": result
        }
