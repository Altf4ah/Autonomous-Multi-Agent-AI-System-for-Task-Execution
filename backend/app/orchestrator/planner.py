from __future__ import annotations

from app.schemas.task import Task


class Planner:
    def create_plan(self, goal: str) -> list[Task]:
        return [
            Task(id="t1", agent="research", instruction=f"Research context for: {goal}"),
            Task(id="t2", agent="analysis", instruction="Analyze the research output"),
            Task(id="t3", agent="writer", instruction="Write a final structured report"),
        ]
