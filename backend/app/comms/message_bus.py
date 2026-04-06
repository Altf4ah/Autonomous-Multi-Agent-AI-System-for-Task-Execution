from __future__ import annotations

from collections import deque

from app.schemas.message import AgentMessage


class MessageBus:
    def __init__(self) -> None:
        self._queue: deque[AgentMessage] = deque()

    def publish(self, message: AgentMessage) -> None:
        self._queue.append(message)

    def drain(self) -> list[AgentMessage]:
        messages = list(self._queue)
        self._queue.clear()
        return messages
