from __future__ import annotations

from abc import ABC, abstractmethod

from app.memory.context_store import ContextStore
from app.memory.vector_store import VectorStore


class BaseAgent(ABC):
    name: str

    @abstractmethod
    def run(self, instruction: str, context: ContextStore, memory: VectorStore) -> str:
        raise NotImplementedError
