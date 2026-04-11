import httpx
from bs4 import BeautifulSoup
from langchain.tools import tool

@tool('web_scraper')
async def scrape_article(url: str):
    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    soup = BeautifulSoup(response.text,'http.parser')

    ignored_tags = ['header','footer','nav','aside','script','style','noscript','form']

    for tag in soup(ignored_tags):
        tag.decompose()
    
    return soup.get_text(separator=" ",strip=True)