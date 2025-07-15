from tools.calculator import run_tool as calculator_tool
from tools.weather import run_tool as weather_tool

TOOL_REGISTRY={
    "calculator": calculator_tool,
    "weather": weather_tool,
}

def get_tool(tool_name:str):
    return TOOL_REGISTRY.get(tool_name)