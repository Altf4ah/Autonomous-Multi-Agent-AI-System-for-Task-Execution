from __future__ import annotations

from app.agents.base import BaseAgent
from app.memory.context_store import ContextStore
from app.memory.vector_store import VectorStore


class AnalysisAgent(BaseAgent):
    name = "analysis"

    def run(self, instruction: str, context: ContextStore, memory: VectorStore) -> str:
        research_output = context.get("research")
        output = (
            "Analysis summary: prioritized insights by opportunity, risk, and supporting signals. "
            f"Input digest: {research_output}"
        )
        memory.add(output)
        return output
