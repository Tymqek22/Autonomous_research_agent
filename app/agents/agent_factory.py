from app.agents.llm_factory import LLMFactory
from app.agents.researcher import ResearcherAgent

def get_researcher_agent() -> ResearcherAgent:
    llm_factory = LLMFactory()
    return ResearcherAgent(llm_factory=llm_factory)