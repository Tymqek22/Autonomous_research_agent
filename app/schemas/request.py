from pydantic import BaseModel
from typing import Optional

class ResearchRequest(BaseModel):
    url: Optional[str] = None