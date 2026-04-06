from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class VectorStore:
    """Placeholder semantic memory.

    This keeps text chunks and does naive substring scoring for demo purposes.
    Swap this class with FAISS/Pinecone for production.
    """

    entries: list[str] = field(default_factory=list)

    def add(self, text: str) -> None:
        self.entries.append(text)

    def query(self, query_text: str, top_k: int = 3) -> list[str]:
        lowered = query_text.lower()
        ranked = sorted(
            self.entries,
            key=lambda e: e.lower().count(lowered),
            reverse=True,
        )
        return ranked[:top_k]
