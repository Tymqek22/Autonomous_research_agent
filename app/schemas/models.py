from pydantic import BaseModel
from typing import Optional

class ResearchRequest(BaseModel):
    url: Optional[str] = None

class TaskAccepted(BaseModel):
    task_id: str
    status: str

class ResearchResponse(BaseModel):
    task_id: str
    status: str
    verdict: str | None
    explanation: str | None