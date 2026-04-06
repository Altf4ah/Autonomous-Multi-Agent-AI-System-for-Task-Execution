from pydantic import BaseModel, Field


class TaskRequest(BaseModel):
    goal: str = Field(..., min_length=5, description="High-level user goal")


class Task(BaseModel):
    id: str
    agent: str
    instruction: str


class TaskResult(BaseModel):
    task_id: str
    agent: str
    output: str
