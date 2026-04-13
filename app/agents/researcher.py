from functools import partial
from langgraph.graph import StateGraph, END
from app.agents.nodes.analyzer import analysis_node
from app.agents.nodes.extractor import extraction_node
from app.agents.nodes.scraper import scraping_node
from app.agents.nodes.synthesizer import evaluation_node
from app.agents.state import AgentState
from app.agents.llm_factory import LLMFactory

class ResearcherAgent:
    def __init__(self,llm_factory: LLMFactory):
        self.llm_factory = llm_factory
        self._graph = self._build_graph()

    def _build_graph(self):
        workflow = StateGraph(AgentState)
        workflow.add_node("scraping_node",scraping_node)
        workflow.add_node("extraction_node",partial(extraction_node,llm_factory=self.llm_factory))
        workflow.add_node("analysis_node",partial(analysis_node,llm_factory=self.llm_factory))
        workflow.add_node("evaluation_node",partial(evaluation_node,llm_factory=self.llm_factory))

        workflow.set_entry_point("scraping_node")
        workflow.add_edge("scraping_node","extraction_node")
        workflow.add_edge("extraction_node","analysis_node")
        workflow.add_edge("analysis_node","evaluation_node")
        workflow.add_edge("evaluation_node",END)
        
        return workflow.compile()
    
    async def run(self,url: str):
        agent_input = {"url": url}
        return await self._graph.ainvoke(agent_input)