from uuid import uuid4
from celery.result import AsyncResult
from app.core.celery_app import celery
from fastapi import APIRouter
from app.schemas.models import ResearchRequest, TaskAccepted, ResearchResponse
from app.tasks.agent_tasks import process_agent_request

router = APIRouter()

@router.post("/analyze-article")
async def analyze_article(request: ResearchRequest):
    task = process_agent_request.delay(request.url)
    
    return TaskAccepted(task_id=task.id, status="Processing")
    
@router.get("/tasks/{task_id}")
async def get_task_status(task_id: str):
    task_result = AsyncResult(task_id, app=celery)

    return ResearchResponse(
        task_id=task_id,
        status=task_result.status,
        verdict=task_result.result['verdict'] if task_result.ready() else None,
        explanation=task_result.result['explanation'] if task_result.ready() else None
    )