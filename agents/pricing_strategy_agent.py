from langchain.agents import Tool, initialize_agent
from langchain_openai import OpenAI
from langchain.agents.agent_types import AgentType

def pricing_strategy_advice(prompt: str) -> str:
    if "elastic" in prompt:
        return "Reduce price slightly to increase volume — location shows price elasticity."
    elif "inelastic" in prompt:
        return "Do not reduce price — demand is inelastic, focus on margin."
    else:
        return "Adjust based on margin impact vs. competitor price."

tools = [
    Tool(
        name="PricingStrategyTool",
        func=pricing_strategy_advice,
        description="Reason over pricing strategy based on elasticity or margin trade-offs."
    )
]

llm = OpenAI(temperature=0)

def get_pricing_strategy_agent():
    return initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, verbose=True)

if __name__ == "__main__":
    agent = get_pricing_strategy_agent()
    print(agent.run("What should I do in an elastic market with lower competitor pricing?"))