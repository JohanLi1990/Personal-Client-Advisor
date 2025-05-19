from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Family")

@mcp.tool()
async def get_father(child: str) -> str:
    """Get Father of a child """
    return "Johan Li"

@mcp.tool()
async def get_mother(child: str) -> str:
    """Get Mother of a child"""
    return "Rona Li"

if __name__=="__main__":
    mcp.run(transport="streamable-http")