from __future__ import annotations

from fastapi import APIRouter

from app.orchestrator.service import OrchestrationService
from app.schemas.task import TaskRequest

router = APIRouter(prefix="/api", tags=["orchestration"])
service = OrchestrationService()


@router.post("/execute")
def execute_task(request: TaskRequest) -> dict[str, object]:
    return service.execute_goal(request.goal)
