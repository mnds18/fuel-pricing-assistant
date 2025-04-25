import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
from agents.pricing_agent import get_code_agent


st.set_page_config(page_title="Fuel Pricing Assistant", layout="wide")
st.title("⛽ Fuel Pricing Optimization Assistant")

st.sidebar.header("Choose Agent Type")
agent_type = st.sidebar.radio("Select Agent", ["Code-based Agent", "LLM-based Agent"])

agent = get_code_agent()

query = st.text_input("Enter your pricing query", value="margin for price 1.85 cost 1.65 volume 5000")

result = agent.run(query)

if st.button("💾 Save Scenario"):
    df.to_csv("saved_scenarios/scenario_2025_04_25.csv", index=False)
    st.success("Scenario saved!")
