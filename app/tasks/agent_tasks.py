import asyncio
from celery import shared_task
from app.agents.agent_factory import get_researcher_agent

@shared_task(name="process_agent_request",bind=True)
def process_agent_request(self,url: str):      
    agent = get_researcher_agent()
    final_state = asyncio.run(agent.run(url))
    
    verdict = final_state.get('final_verdict')
    
    return {
        "verdict": verdict.verdict,
        "explanation": verdict.explanation
    }