from langchain.agents import initialize_agent, Tool
from langchain_openai import ChatOpenAI
from langchain.agents.agent_types import AgentType
from tools.search_tool import get_search_tool
from tools.scraper_tool import scrape_url

def build_research_agent():
    llm = ChatOpenAI(temperature=0, model="gpt-4")

    tools = [
        Tool(
            name="WebSearch",
            func=get_search_tool().run,
            description="Searches for current events or general knowledge."
        ),
        Tool(
            name="WebScraper",
            func=scrape_url,
            description="Scrapes and extracts text from a URL."
        )
    ]

    agent = initialize_agent(
        tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )
    return agent
