from typing import List, Optional, Dict, Any
from pydantic import BaseModel

class GraphState(BaseModel):
    messages: List[str] = []  # Full user + assistant history, as raw strings for now
    memories: Optional[str] = None
    planner_output: Optional[Dict[str, Any]] = None
    tool_output: Optional[str] = None
    final_output: Optional[str] = None
    structured_memory: Optional[Dict[str, str]] = None

