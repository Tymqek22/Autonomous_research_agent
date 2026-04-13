from fastapi import APIRouter, Depends, HTTPException
from app.schemas.request import ResearchRequest
from app.schemas.response import ResearchResponse
from app.agents.researcher import ResearcherAgent
from app.api.dependencies import get_researcher_agent

router = APIRouter()

@router.post("/analyze-article")
async def analyze_article(
    request: ResearchRequest,
    agent: ResearcherAgent = Depends(get_researcher_agent)
):
    try:
        final_state = await agent.run(request.url)

        return ResearchResponse(
            status="completed",
            verdict=final_state['final_verdict'].verdict,
            explanation=final_state['final_verdict'].explanation)

    except Exception as ex:
        raise HTTPException(status_code=500,detail=f"Error during the research: {str(ex)}")