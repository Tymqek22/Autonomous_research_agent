from app.agents.schemas.models import FactExtraction
from app.agents.state import AgentState
from app.agents.llm_factory import LLMFactory

def extraction_node(state: AgentState,llm_factory: LLMFactory):
    text = state.get("article_text","")

    if not text:
        return {"error": "No text to analize."}
    
    try:
        llm = llm_factory.get_llm(structured_output=FactExtraction)

        prompt = f'''
            Extract maximum 5 facts from the article text. Fetch facts related with dates, statistics, people and events.
            Every fact should have a context based on this article. You can't extract raw date, number or person.\n\n
            Text: {text}
        '''

        response = llm.invoke(prompt)

        return {"facts": response.facts}
    except Exception as ex:
        return {"error": f"Extraction failed: {str(ex)}"}