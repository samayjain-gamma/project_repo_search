from src.client import McpClient


class GithubService:

    @staticmethod
    async def serch_repository_query(query, top_k):
        result = await McpClient.call_tool(
            "search_repository", {"query": query, "top_k": top_k}
        )

        return result
