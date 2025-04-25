from langchain.agents import Tool, initialize_agent
from langchain_openai import OpenAI
from langchain.agents.agent_types import AgentType

def summarize_news(news: str) -> str:
    return "Summary: " + news[:200] + "..."  # Simulate summarization

tools = [
    Tool(
        name="ComplianceChecker",
        func=summarize_news,
        description="Summarizes regulatory news or updates for fuel pricing."
    )
]

llm = OpenAI(temperature=0)

def get_compliance_agent():
    return initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

if __name__ == "__main__":
    agent = get_compliance_agent()
    sample_news = "The ACCC announced new guidelines on fuel price disclosure to protect consumers and ensure fair competition among retailers."
    print(agent.run(f"Summarize this for compliance relevance: {sample_news}"))