from pydantic import BaseModel


class AgentMessage(BaseModel):
    sender: str
    receiver: str
    payload: str
