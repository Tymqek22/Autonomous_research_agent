from uuid import uuid4
from celery.result import AsyncResult
from app.core.celery_app import celery
from fastapi import APIRouter
from app.schemas.request import ResearchRequest
from app.tasks.agent_tasks import process_agent_request

router = APIRouter()

@router.post("/analyze-article")
async def analyze_article(request: ResearchRequest):
    task = process_agent_request.delay(request.url)
    
    return {
        "taskId": task.id,
        "status": "processing"
    }
    
@router.get("/tasks/{task_id}")
async def get_task_status(task_id: str):
    task_result = AsyncResult(task_id, app=celery)

    result = {
        "taskId": task_id,
        "status": task_result.status,
        "result": task_result.result if task_result.ready() else None
    }
    return result