from langchain_core.messages import HumanMessage, ToolMessage
from langgraph.graph import END
from langgraph.prebuilt import ToolNode

from src.agents.state import AgentState
from src.core.exception import CustomException
from src.core.llm_provider import get_llm
from src.core.logger import logger
from src.tools.mcp_tools import search_repository, search_wikipedia_articles

llm_with_tools = get_llm(temperature=0.0).bind_tools(
    [search_wikipedia_articles, search_repository], tool_choice="required"
)


llm_no_tools = get_llm(temperature=0.1)


# async def llm_node(state: AgentState):
#     try:
#         logger.info("Going to call one of the llm")
#         print("Going to call one of the llm")
#         if not state.get("tool_used"):
#             logger.info("LLM with tools called")
#             print("LLM with tools called")
#             response = await llm_with_tools.ainvoke(state["messages"])
#         else:
#             logger.info("LLM with no tools called")
#             print("LLM with no tools called")
#             message = state['messages']
#             print(f"\nstate in which the second llm call is going ot invoke:\n{message}")
#             response = await llm_no_tools.ainvoke(state["messages"])
#         # logger.info("calling llm")
#         # print("llm is called")
#         # response = await llm.ainvoke(state["messages"])
#         # print(response.content)
#         print(f"Response from LLM : \n{response}")
#         return {"messages": [response]}

#     except Exception as e:
#         logger.error("Error occurred during llm call")
#         raise CustomException(e)


async def llm_node_tool(state: AgentState):
    """
    first llm call
    """
    prompt = state["user_prompt"]
    # messages = state["message_tool"]
    # logger.info("LLM with tools called")
    # print("LLM with tools called")
    response = await llm_with_tools.ainvoke(prompt)
    print(f"\nResponse got , from first llm call:\n{response}")
    return {"messages": [response], "message_tool": response}


async def llm_node_no_tool(state: AgentState):
    message = state["executer_result"]
    content = f"""
    Use the following
    Data:
    {message}

    Return a concise answer.
    """
    response = await llm_no_tools.ainvoke(content)
    print(f"\nFinal Answer :\n{response}")
    return {"final_answer": [response]}


tool_executor = ToolNode([search_repository, search_wikipedia_articles])

# async def tool_node(state:AgentState):
#     logger.info("Executing tool")
#     print("Executing tool")
#     result = await tool_executor.ainvoke(state)
#     ans = result["messages"]
#     ans = ans[0].content
#     # ans = dict(ans)
#     print(f"\nOtuput from tool:\n{result}")
#     print(f"\nOtuput from tool:\n{ans}\n")
#     return {
#         "messsages" : [ans],
#         "tool_used" : True
#     }


async def tool_node(state: AgentState):
    # tool_call = state["message_tool"]
    tool_call = state["messages"]
    print(state["messages"][-1])
    print(f"\nTool calling:\n{tool_call}")

    result = await tool_executor.ainvoke({"messages": state["messages"]})
    print(result)
    return {
        "tool_used": True,
        "executer_result": result,
        "messages": result["messages"],
    }


# def should_continue(state: AgentState):
#     logger.info("Entered into conditional edge")
#     print("ENtered into conditonal edge")
#     print(f"State is :\n{state}\n")
#     last_message = state["messages"][-1]
#     print(f"\nLast Message :\n{last_message}")
#     if getattr(last_message, "tool_calls", None):
#         logger.info("Going to call a tool")
#         print("Going to call a tool")
#         return "tools"

#     logger.info("Returning END")
#     print("Returning END")
#     return END


# def should_continue(state: AgentState):
#     logger.info("Entered into conditional edge")
#     print("ENtered into conditonal edge")
#     print(f"State is :\n{state}\n")
#     last_message = state["messages"][-1]
#     print(f"\nLast Message :\n{last_message}")

#     logger.info("Going to call a tool")
#     print("Going to call a tool")
#     return "tools"


# def extract_tool_data(messages):
#     print("Extract tool data called")
#     for m in reversed(messages):
#         if isinstance(m, ToolMessage):
#             return m.content
#     return None
