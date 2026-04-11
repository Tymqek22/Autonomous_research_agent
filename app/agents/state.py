from typing import TypedDict, List
from app.agents.schemas.models import Fact

class AgentState(TypedDict):
    article_text: str
    facts: List[Fact]
    error: str