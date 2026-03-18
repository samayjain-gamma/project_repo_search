from langgraph.graph import END, StateGraph

# from src.agents.nodes import llm_node, tool_node, should_continue, llm_node_tool, llm_node_no_tool
from src.agents.nodes import llm_node_no_tool, llm_node_tool, tool_node
from src.agents.state import AgentState

graph = StateGraph(AgentState)

# graph.add_node("llm", llm_node)
graph.add_node("tools", tool_node)
graph.add_node("llm_tool", llm_node_tool)
graph.add_node("llm_no_tool", llm_node_no_tool)

# graph.set_entry_point("llm")

# graph.add_conditional_edges(
#     "llm",
#     should_continue ,
#     {
#         "tools": "tools",
#         END:END
#     }
# )

# graph.add_edge("tools","llm")


graph.set_entry_point("llm_tool")
graph.add_edge("llm_tool", "tools")
graph.add_edge("tools", "llm_no_tool")
graph.add_edge("llm_no_tool", END)
agent = graph.compile()
