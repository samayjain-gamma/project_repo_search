from typing import Any, List, TypedDict

from langchain_core.messages import BaseMessage

# class AgentState(TypedDict, total = False):
#     messages: List[BaseMessage]
#     tool_used : bool


class AgentState(TypedDict, total=False):
    messages: List[BaseMessage]
    tool_used: bool
    message_no_tool: Any
    message_tool: Any
    user_prompt: str
    executer_result: Any
    final_answer: Any
