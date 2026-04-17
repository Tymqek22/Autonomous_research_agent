import asyncio
from app.agents.tools.search import web_search
from app.agents.state import AgentState
from app.agents.schemas.models import Fact, FactAnalysis
from app.agents.llm_factory import LLMFactory

async def verify_single_fact(fact: Fact,llm_factory: LLMFactory) -> FactAnalysis:
    evidence = await web_search(fact.claim)

    llm = llm_factory.get_llm(structured_output=FactAnalysis)

    prompt = f'''
        You are the judge who need to make a verdict whether the fact fetched from article is true or false based on evidence 
        gathered to it. Analyze this fact based on evidence and answer using only (True, False, Unverified, Partially True).
        Fact {fact.claim}\n\nEvidence from internet {evidence}
    '''

    analysis = await llm.ainvoke(prompt)

    return analysis

async def analysis_node(state: AgentState,llm_factory: LLMFactory):
    facts = state.get("facts",[])
    print(f"[ANALYSIS] Facts received: {len(facts)}")
    print(f"[ANALYSIS] Facts content: {facts}")

    if not facts:
        return {"analysis_results": [], "error": "No facts to be analyzed."}

    tasks = [verify_single_fact(fact,llm_factory) for fact in facts]

    try:
        analysis_results = await asyncio.gather(*tasks)

        return {"analysis_results": analysis_results}
    except Exception as ex:
        return {"error": f"Analysis failed: {str(ex)}"}