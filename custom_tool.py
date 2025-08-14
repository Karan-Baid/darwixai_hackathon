# src/research_crew/custom_tool.py
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
import requests
from bs4 import BeautifulSoup

class GetArticleTextInput(BaseModel):
    """Input schema for GetArticleTextTool."""
    url: str = Field(..., description="The URL of the news article to fetch.")

class GetArticleTextTool(BaseTool):
    name: str = "Get Article Text Tool"
    description: str = "Fetches and cleans the main text content from a news article URL."
    args_schema: Type[BaseModel] = GetArticleTextInput

    def _run(self, url: str) -> str:
        headers = {"User-Agent": "Mozilla/5.0"}
        try:
            r = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(r.text, "html.parser")

            # Extract title
            title_tag = soup.find("title")
            title = title_tag.get_text() if title_tag else "Untitled"

            # Extract paragraphs
            paragraphs = soup.find_all("p")
            text = "\n".join([p.get_text() for p in paragraphs if p.get_text().strip()])

            return f"Title: {title}\n\n{text}"
        except Exception as e:
            return f"Error fetching article: {str(e)}"
