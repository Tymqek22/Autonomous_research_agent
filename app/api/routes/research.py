from fastapi import APIRouter
from app.schemas.request import ResearchRequest
from app.schemas.response import ResearchResponse

router = APIRouter()

@router.get("/research",response_model=ResearchResponse)
def process_research():
    return ResearchResponse(summary="Basic flow implemented")