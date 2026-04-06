from __future__ import annotations

from app.agents.base import BaseAgent
from app.memory.context_store import ContextStore
from app.memory.vector_store import VectorStore


class WriterAgent(BaseAgent):
    name = "writer"

    def run(self, instruction: str, context: ContextStore, memory: VectorStore) -> str:
        goal = context.get("goal")
        analysis_output = context.get("analysis")
        recalled = memory.query(goal)
        output = (
            f"# Final Report\n\nGoal: {goal}\n\n"
            f"## Key Findings\n{analysis_output}\n\n"
            f"## Memory Recall\n- " + "\n- ".join(recalled)
        )
        return output
