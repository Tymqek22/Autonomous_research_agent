from fastapi import APIRouter, HTTPException
from app.schemas.request import ResearchRequest
from app.agents.researcher import ResearcherAgent
from app.agents.llm_factory import LLMFactory

router = APIRouter()
llm_factory = LLMFactory()
agent = ResearcherAgent(llm_factory)

@router.post("/analyze-article")
async def analyze_article(request: ResearchRequest):
    try:
        final_state = await agent.run(request.url)
        
        return {
            "status": "completed",
            "verdict": final_state.get("final_verdict")
        }

    except Exception as ex:
        raise HTTPException(status_code=500,detail=f"Error during the research: {str(ex)}")