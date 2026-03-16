from typing import Callable, Dict, List

# from src.core.exception import CustomException
from src.core.logger import logger

from .github_tools import search_repository


class ToolRegistry:

    def __init__(self):
        self._tools: Dict[str, Callable] = {}

    def register_tool(self, name: str, tool: Callable):
        self._tools[name] = tool

    def get_tool(self, name: str) -> Callable:
        if name not in self._tools:
            logger.info("Tool not in tools")
            return
        return self._tools[name]

    def list_tools(self) -> List:
        return list(self._tools)


registry = ToolRegistry()

registry.register_tool("search_repository", search_repository)

if __name__ == "__main__":
    github_tool = registry.get_tool("search_repository")
    tools = registry.list_tools()
    print(tools)
    repos = github_tool("RAG")
    print(repos)
