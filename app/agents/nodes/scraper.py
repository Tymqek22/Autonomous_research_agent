import httpx
from bs4 import BeautifulSoup
from app.agents.state import AgentState

async def scraping_node(state: AgentState):
    breakpoint()
    url = state.get("url","")

    if not url:
        return {"error": "Url was not specified."}

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    soup = BeautifulSoup(response.text,"html.parser")

    ignored_tags = ['header','footer','nav','aside','script','style','noscript','form']

    for tag in soup(ignored_tags):
        tag.decompose()
    
    article_text = soup.get_text(separator=" ",strip=True)

    return {"article_text": article_text}