import asyncio

from fastmcp import Client


async def main():

    client = Client("http://localhost:8000/mcp")

    async with client:

        tools = await client.call_tool("list_tools")
        print("TOOLS:", tools)

        result = await client.call_tool(
            "call_tool",
            {
                "name": "search_repository",
                "arguments": {"query": "langgraph", "top_k": 3},
            },
        )

        print(result)


if __name__ == "__main__":
    asyncio.run(main())
