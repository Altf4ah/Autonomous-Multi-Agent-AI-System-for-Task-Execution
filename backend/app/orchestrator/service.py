from __future__ import annotations

from app.comms.message_bus import MessageBus
from app.memory.context_store import ContextStore
from app.memory.vector_store import VectorStore
from app.orchestrator.dispatcher import Dispatcher
from app.orchestrator.evaluator import Evaluator
from app.orchestrator.planner import Planner
from app.schemas.message import AgentMessage
from app.schemas.task import TaskResult


class OrchestrationService:
    def __init__(self) -> None:
        self.planner = Planner()
        self.dispatcher = Dispatcher()
        self.evaluator = Evaluator()

    def execute_goal(self, goal: str) -> dict[str, object]:
        context = ContextStore()
        context.set("goal", goal)
        memory = VectorStore()
        bus = MessageBus()

        results: list[TaskResult] = []
        for task in self.planner.create_plan(goal):
            agent = self.dispatcher.get_agent(task.agent)
            output = agent.run(task.instruction, context, memory)
            context.set(task.agent, output)
            bus.publish(
                AgentMessage(
                    sender=task.agent,
                    receiver="orchestrator",
                    payload=output,
                )
            )
            results.append(TaskResult(task_id=task.id, agent=task.agent, output=output))

        report = context.get("writer")
        if self.evaluator.needs_refinement(report):
            report = self.evaluator.refine(report)

        return {
            "goal": goal,
            "plan": [task.model_dump() for task in self.planner.create_plan(goal)],
            "results": [r.model_dump() for r in results],
            "messages": [m.model_dump() for m in bus.drain()],
            "final_report": report,
            "context": context.dump(),
        }
