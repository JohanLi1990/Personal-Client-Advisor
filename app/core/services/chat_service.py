from typing import Any
from langgraph.graph.graph import CompiledGraph
class ChatService:
    def __init__(self, agent: CompiledGraph):
        self.agent = agent

    async def chat(self, message: str)-> dict[str, Any] | Any:
        # Use the injected agent to process the message
        return await self.agent.ainvoke({"messages": message})