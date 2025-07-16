def run_tool(tool_input: str):
    """USe to evaluate mathematical expression"""
    try:
        result=str(eval(tool_input))
        return result
    except Exception as e:
        return f"Error evaluating expression: {str(e)}"