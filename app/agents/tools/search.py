from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool

@tool('web_search')
def search(query: str) -> str:
    search = DuckDuckGoSearchRun()

    return search.invoke(query)