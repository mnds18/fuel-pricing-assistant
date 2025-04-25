from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain.agents import tool
from typing import TypedDict

# Define state
class StrategyState(TypedDict):
    message: str
    result: str

@tool
def strategy_tool(input: str) -> str:
    """
    Provides fuel pricing strategy suggestions based on market elasticity.
    """
    if "elastic" in input:
        return "Lower price slightly in elastic markets."
    elif "inelastic" in input:
        return "Hold price for inelastic demand."
    return "Adjust pricing based on margin impact."


# LangGraph node
def run_strategy_node(state: StrategyState) -> StrategyState:
    response = strategy_tool.invoke(state["message"])
    return {"message": state["message"], "result": response}

# Build graph
graph = StateGraph(StrategyState)
graph.add_node("strategy_node", run_strategy_node)
graph.set_entry_point("strategy_node")
graph.set_finish_point("strategy_node")
chain = graph.compile()

# Run example
if __name__ == "__main__":
    out = chain.invoke({"message": "elastic market, competitor undercut"})
    print("LangGraph Output:", out["result"])