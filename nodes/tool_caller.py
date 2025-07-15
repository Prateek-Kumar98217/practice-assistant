from tools import get_tool
from utils.logger import timed_node

class ToolCaller:
    def __init__(self):
        pass
    
    @timed_node("tool_caller")
    def __call__(self, state):
        action=state.get("planner_output", {})
        tool_name=action.get("tool_name")
        tool_input=action.get("input", "")

        tool_func=get_tool(tool_name)
        if not tool_func:
            state["tool_output"]=f"Tool {tool_name} not found"
            return state
        result=tool_func(tool_input)
        state["tool_output"]=result
        return result