import asyncio
import instructor
from openai import AsyncOpenAI
from app.agents.tools.search import web_search
from app.agents.state import AgentState
from app.agents.schemas.models import Fact, FactAnalysis

client = instructor.from_openai(AsyncOpenAI(base_url="http://localhost:11434/v1",api_key="ollama"))

async def verify_single_fact(fact: Fact) -> FactAnalysis:
    evidence = await web_search(fact.claim)

    analysis = client.chat.completions.create(
        model="llama3.1",
        response_model=FactAnalysis,
        messages=[
            {"role": "system", "content": "You are the judge who need to make a verdict whether the fact fetched from internet is true or false based on evidences gathered to it."},
            {"role": "user", "content": f"Fact {fact.claim}\n\nEvidence from internet {evidence}\n\nJudge the truth of this fact."}
        ]
    )

    return analysis

async def analysis_node(state: AgentState):
    facts = state.get("facts",[])

    if not facts:
        return {"analysis_results": [], "error": "No facts to be analyzed."}
    
    tasks = []
    for fact in facts:
        tasks.append(verify_single_fact(fact))

    analysis_results = await asyncio.gather(*tasks)

    return {"analysis_results": analysis_results}