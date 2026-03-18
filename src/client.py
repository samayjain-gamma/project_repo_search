import asyncio

from fastmcp import Client

from src.core.exception import CustomException
from src.core.logger import logger


class McpClient:

    SERVER_URL = "http://localhost:8000/mcp"
    client: Client | None = None

    @classmethod
    async def init(cls):
        cls.client = Client(cls.SERVER_URL)
        await cls.client.__aenter__()

    @classmethod
    async def list_tools(cls):
        return await cls.client.call_tool("list_tools")

    @classmethod
    async def call_tool(cls, name: str, arguments: dict):
        logger.info(
            f"Calling tool from MCP client \nName : {name} \nArguments : {arguments}"
        )
        return await cls.client.call_tool(
            "call_tool", {"name": name, "arguments": arguments}
        )


# async def main():

#     await McpClient.init()

#     tools = await McpClient.list_tools()

#     print("\nAvailable tools:")
#     print(tools)

#     result = await McpClient.call_tool(
#         "search_repository", {"query": "langgraph", "top_k": 1}
#     )

#     print("\nTool Result:")
#     print(result)

#     wiki_articles = await McpClient.call_tool(
#         "search_wikipedia_articles",
#         {"topics": ("Artificial Intelligence", "Alan Turing")},
#     )
#     print(f"\n\n Articles :  {wiki_articles}")
#     print(f"\n type  of articles return ed   : {type(wiki_articles)}")
#     # for i in wiki_articles:
#     #     print(f"{i} \n\n")


# if __name__ == "__main__":
#     asyncio.run(main())
