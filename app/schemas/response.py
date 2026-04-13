from pydantic import BaseModel

class ResearchResponse(BaseModel):
    status: str
    verdict: str
    explanation: str