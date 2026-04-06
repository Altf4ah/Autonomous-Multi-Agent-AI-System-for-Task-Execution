from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ContextStore:
    """Simple in-memory run context for agent handoffs."""

    values: dict[str, str] = field(default_factory=dict)

    def set(self, key: str, value: str) -> None:
        self.values[key] = value

    def get(self, key: str, default: str = "") -> str:
        return self.values.get(key, default)

    def dump(self) -> dict[str, str]:
        return dict(self.values)
