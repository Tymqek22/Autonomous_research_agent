from fastapi import APIRouter, HTTPException
from app.schemas.request import ResearchRequest
from app.agents.researcher import app_graph

router = APIRouter()

@router.post("/analyze-article")
async def analyze_article(request: ResearchRequest):
    agent_input = {"url": str(request.url)}

    try:
        final_state = await app_graph.ainvoke(agent_input)

        return {
            "status": "completed",
            "verdict": final_state.get("final_verdict")
        }

    except Exception as ex:
        raise HTTPException(status_code=500,detail=f"Error during the research: {str(ex)}")