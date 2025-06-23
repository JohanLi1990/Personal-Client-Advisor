from arrow import get
from dotenv import load_dotenv
from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langgraph.graph.graph import CompiledGraph
from datetime import timedelta
from agno.agent import Agent
from agno.models.openai import OpenAIChat
from agno.tools.yfinance import YFinanceTools

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
    

def get_agnos_agent():
    return Agent(
        model=OpenAIChat(id="o1"),
        tools=[YFinanceTools(stock_price=True)],
        instructions="Use tables to display data, Don't include any other text.",
        markdown=True
    )


# load_dotenv()
# import os
# print(os.environ.get("OPENAI_API_KEY"))
# get_agnos_agent().print_response("what is the price of Apple?", stream=True)
    
    
    