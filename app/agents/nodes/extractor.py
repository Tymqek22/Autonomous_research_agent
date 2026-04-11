import instructor
from openai import OpenAI
from app.agents.schemas.models import FactExtraction
from app.agents.state import AgentState

client = instructor.from_openai(
    OpenAI(
        base_url="http://localhost:11434",
        api_key="ollama"),
        mode=instructor.Mode.JSON
)

async def extraction_node(state: AgentState):
    text = state.get("article_text","")

    if not text:
        return {"error": "No text to analize."}
    
    try:
        response = client.chat.completions.create(
            model="llama3.1",
            response_model=FactExtraction,
            messages= [
                {"role": "system", "content": "Exctacts facts from the text. Fetch only facts related with dates, statistics, people and events."},
                {"role": "user", "content": text}
            ]
        )

        return {"facts": response.facts}
    except Exception as ex:
        return {"error": f"Extraction failed: {str(ex)}"}