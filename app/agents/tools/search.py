from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool

@tool('web_search')
async def web_search(query: str):
    search = DuckDuckGoSearchRun()

    return search.run(query)