from __future__ import annotations

from app.agents.base import BaseAgent
from app.memory.context_store import ContextStore
from app.memory.vector_store import VectorStore


class ResearchAgent(BaseAgent):
    name = "research"

    def run(self, instruction: str, context: ContextStore, memory: VectorStore) -> str:
        goal = context.get("goal")
        output = (
            f"Research summary for goal '{goal}': "
            "identified representative market trends, notable companies, and citation placeholders."
        )
        memory.add(output)
        return output
