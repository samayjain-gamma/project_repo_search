import json

from langchain_core.tools import tool

from src.client import McpClient


@tool
async def search_repository(query: str, top_k: int = 5):
    """Search GitHub repositories."""
    result = await McpClient.call_tool(
        "search_repository", {"query": query, "top_k": top_k}
    )
    raw = result.content[0].text
    return json.loads(raw)
    # try:
    #     return result.content[0].text
    # except:
    #     print("failed to return in try block , entered in to except block")
    #     return str(result)


@tool
async def search_wikipedia_articles(topics: list[str]):
    """Retrieve summaries for Wikipedia topics."""
    return await McpClient.call_tool("search_wikipedia_articles", {"topics": topics})
