import json
from langchain_ollama import ChatOllama
from app.agents.schemas.models import FinalVerdict
from app.agents.state import AgentState

async def evaluation_node(state: AgentState):
    analysis_results = state.get("analysis_results","")

    if not analysis_results:
        return {"error": "No results to evaluate."}
    
    analysis_results_formatted = json.dumps(
        [claim.model_dump() for claim in analysis_results],
        indent=2
    )

    llm = ChatOllama(
        model="llama3.1",
        temperature=0
    )
    structured_llm = llm.with_structured_output(FinalVerdict)

    prompt = f'''
        You are a final judge who needs to make a verdict about the article reliability based on already analyzed facts.
        Focus on concise explanation.
        The formatted analysis results are here:
        {analysis_results_formatted}

        Return the final verdict and appropriate explanation in JSON format.
    '''

    result = await structured_llm.ainvoke(prompt)

    return {"final_verdict": result}