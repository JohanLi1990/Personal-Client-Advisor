from typing import Any
from langgraph.graph.graph import CompiledGraph
from agno.agent import Agent
class ChatService:
    def __init__(self, agent: CompiledGraph, agno_agent: Agent):
        self.agent = agent
        self.agno_agent = agno_agent
    

    async def chat(self, message: str)-> dict[str, Any] | Any:
        # Use the injected agent to process the message
        return await self.agent.ainvoke({"messages": message})
    
    async def chat_agno(self, message:str) -> str:
        return await self.agno_agent.arun(message)