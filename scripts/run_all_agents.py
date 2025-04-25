import subprocess

print("🧠 Running Pricing Strategy Agent (LangGraph)...")
try:
    subprocess.run(["python", "agents/pricing_strategy_langgraph.py"], check=True)
except subprocess.CalledProcessError:
    print("⚠️ Pricing strategy agent failed. Skipping.")

print("📋 Running Compliance Agent...")
try:
    subprocess.run(["python", "agents/compliance_agent.py"], check=True)
except subprocess.CalledProcessError:
    print("⚠️ Compliance agent failed. Skipping.")

print("✅ All agents executed.")