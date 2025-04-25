from langchain.agents import Tool, initialize_agent
from langchain_openai import OpenAI
from langchain.agents.agent_types import AgentType

# 🔧 Pure Python tool: margin calculator
def calculate_fuel_margin(query: str) -> str:
    try:
        tokens = query.lower().split()
        price = float(tokens[tokens.index("price") + 1].replace("'", "").replace('"', ''))
        cost = float(tokens[tokens.index("cost") + 1].replace("'", "").replace('"', ''))
        volume = float(tokens[tokens.index("volume") + 1].replace("'", "").replace('"', ''))

        margin_per_litre = price - cost
        total_margin = margin_per_litre * volume

        return f"✅ Margin per litre: ${margin_per_litre:.2f}, Total daily margin: ${total_margin:,.2f}"
    except Exception as e:
        return f"❌ Error parsing input: {str(e)}. Use format: 'margin for price 1.85 cost 1.65 volume 5000'"

# Tool definition
code_tools = [
    Tool(
        name="FuelMarginCalculator",
        func=calculate_fuel_margin,
        description="Calculates fuel margin. Format: 'margin for price 1.85 cost 1.65 volume 5000'"
    )
]

# LLM + Tool agent
llm = OpenAI(temperature=0)

def get_code_agent():
    return initialize_agent(
        code_tools,
        llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        verbose=True
    )

# Optional CLI run
if __name__ == "__main__":
    query = input("Enter query: ")
    agent = get_code_agent()
    print(agent.run(query))
