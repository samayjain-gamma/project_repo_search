from fastmcp import FastMCP

from .tools.tool_registry import registry

mcp = FastMCP("search-tools-server")


@mcp.tool()
def list_tools():
    return registry.list_tools()


# @mcp.tool()
# def call_tool(name: str, arguments: dict):

#     tool = registry.get_tool(name)
#     result = tool(**arguments)
#     return result


@mcp.tool()
def call_tool(name: str, arguments: dict):

    print(f"Calling tool: {name}")
    print(f"Arguments: {arguments}")

    tool = registry.get_tool(name)

    result = tool(**arguments)

    print("Result returned")

    return result


if __name__ == "__main__":
    mcp.run(transport="http", host="localhost", port=8000)
