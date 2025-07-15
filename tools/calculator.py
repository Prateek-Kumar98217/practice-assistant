def run_tool(tool_input: str):
    try:
        result=str(eval(tool_input))
        return result
    except Exception as e:
        return f"Error evaluating expression: {str(e)}"