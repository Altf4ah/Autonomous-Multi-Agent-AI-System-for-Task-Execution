from __future__ import annotations

from app.agents.analysis_agent import AnalysisAgent
from app.agents.base import BaseAgent
from app.agents.research_agent import ResearchAgent
from app.agents.writer_agent import WriterAgent


class Dispatcher:
    def __init__(self) -> None:
        self._registry: dict[str, BaseAgent] = {
            "research": ResearchAgent(),
            "analysis": AnalysisAgent(),
            "writer": WriterAgent(),
        }

    def get_agent(self, name: str) -> BaseAgent:
        if name not in self._registry:
            raise KeyError(f"Unknown agent: {name}")
        return self._registry[name]
