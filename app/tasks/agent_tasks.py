import asyncio
from celery import shared_task
from app.agents.agent_factory import get_researcher_agent

@shared_task(name="process_agent_request",bind=True)
def process_agent_request(self,url: str):      
    agent = get_researcher_agent()

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    try:
        final_state = loop.run_until_complete(agent.run(url))
    finally:
        loop.close()
    
    verdict = final_state.get('final_verdict')
    
    return {
        "verdict": verdict.verdict,
        "explanation": verdict.explanation
    }