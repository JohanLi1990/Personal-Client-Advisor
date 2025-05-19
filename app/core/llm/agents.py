from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langgraph.graph.graph import CompiledGraph
from datetime import timedelta

async def get_agent() -> CompiledGraph:
    client = MultiServerMCPClient(
        {
            "parents": {
                "url": "http://localhost:8000/mcp",
                "transport": "streamable_http",
                "timeout": timedelta(seconds=60),
                "sse_read_timeout": timedelta(seconds=60),
                "terminate_on_close": True,
                "headers": None,
                "session_kwargs": None
            }
        }
    )
    tools = await client.get_tools()
    agent = create_react_agent("openai:gpt-4.1", tools)
    return agent
    
    
    
    