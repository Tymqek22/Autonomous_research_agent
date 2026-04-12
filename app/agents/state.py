from typing import TypedDict, List
from app.agents.schemas.models import Fact, FactAnalysis,FinalVerdict

class AgentState(TypedDict):
    url: str
    article_text: str
    facts: List[Fact]
    analysis_results: List[FactAnalysis]
    final_verdict: FinalVerdict
    error: str