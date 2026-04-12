from langgraph.graph import StateGraph, END
from app.agents.nodes.analyzer import analysis_node
from app.agents.nodes.extractor import extraction_node
from app.agents.nodes.scraper import scraping_node
from app.agents.nodes.synthesizer import evaluation_node
from app.agents.state import AgentState

workflow = StateGraph(AgentState)

workflow.add_node("scraping_node",scraping_node)
workflow.add_node("extraction_node",extraction_node)
workflow.add_node("analysis_node",analysis_node)
workflow.add_node("evaluation_node",evaluation_node)

workflow.set_entry_point("scraping_node")
workflow.add_edge("scraping_node","extraction_node")
workflow.add_edge("extraction_node","analysis_node")
workflow.add_edge("analysis_node","evaluation_node")
workflow.add_edge("evaluation_node",END)

app_graph = workflow.compile()