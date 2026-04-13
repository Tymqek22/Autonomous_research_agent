import json
from app.agents.schemas.models import FinalVerdict
from app.agents.state import AgentState
from app.agents.llm_factory import llm_factory

async def evaluation_node(state: AgentState):
    analysis_results = state.get("analysis_results","")

    if not analysis_results:
        return {"error": "No results to evaluate."}
    
    analysis_results_formatted = json.dumps(
        [claim.model_dump() for claim in analysis_results],
        indent=2
    )

    try:
        llm = llm_factory.get_llm(structured_output=FinalVerdict)

        prompt = f'''
                You are a final judge who needs to make a verdict about the article reliability based on already analyzed facts.
                Focus on concise explanation.
                The formatted analysis results are here:\n
                {analysis_results_formatted}\n\n
                Return the final verdict and appropriate explanation in JSON format.
            '''

        result = await llm.ainvoke(prompt)

        return {"final_verdict": result}
    except Exception as ex:
        return {"error": f"Final evaluation failed: {str(ex)}"}