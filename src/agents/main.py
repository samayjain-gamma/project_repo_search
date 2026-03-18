import asyncio

from langchain_core.messages import HumanMessage

from src.agents.first_agent import agent
from src.client import McpClient


async def main():
    await McpClient.init()

    print("CLIENT:", McpClient.client)
    print("Entered into main funciton ")
    result = await agent.ainvoke(
        {"user_prompt": "Find 2 github repos on FastAPI project"}
    )

    output = result["messages"][-1].content
    print(output)


asyncio.run(main())
