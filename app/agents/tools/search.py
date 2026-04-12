from langchain_community.tools import DuckDuckGoSearchRun

async def web_search(query: str):
    search = DuckDuckGoSearchRun()

    return search.run(query)