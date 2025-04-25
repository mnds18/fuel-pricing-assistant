import streamlit as st
import joblib
import pandas as pd
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from datetime import datetime
from agents.pricing_agent import get_code_agent
from agents.pricing_strategy_agent import get_pricing_strategy_agent
from agents.compliance_agent import get_compliance_agent
from utils.supply_demand_risk import supply_demand_risk
from utils.margin_threshold import check_margin_threshold

st.set_page_config(page_title="Fuel Pricing Assistant", layout="wide")
st.title("🔍 Human-in-the-Loop Fuel Pricing Assistant, by Mrig")

# Inputs
price = st.number_input("Fuel Price", value=1.85)
cost = st.number_input("Cost Price", value=1.65)
comp_price = st.number_input("Competitor Price", value=1.82)
dayofweek = st.selectbox("Day of Week", list(range(7)))
month = st.selectbox("Month", list(range(1, 13)))

predict_button = st.button("Predict & Recommend")

if predict_button:
    model = joblib.load("models/xgb_demand_forecaster.pkl")
    features = ['fuel_price', 'competitor_price', 'cost_price', 'price_gap', 'dayofweek', 'month']
    data = {
        "fuel_price": price,
        "competitor_price": comp_price,
        "cost_price": cost,
        "price_gap": price - comp_price,
        "dayofweek": dayofweek,
        "month": month
    }
    df = pd.DataFrame([[data[feature] for feature in features]], columns=features)
    prediction = model.predict(df)[0]
    st.success(f"📈 Predicted Volume: {prediction:.0f} litres")

    # Agents
    pricing_agent = get_pricing_strategy_agent()
    compliance_agent = get_compliance_agent()
    pricing_strategy = pricing_agent.run("elastic market with competitor undercut")
    compliance_summary = compliance_agent.run("ACCC fuel price monitoring update 2025")

    # Utils
    margin_check = check_margin_threshold(price, cost, prediction)
    supply_demand = supply_demand_risk(price - comp_price, prediction)

    # Output
    st.info(f"💡 Strategy Advice: {pricing_strategy}")
    st.warning(f"📋 Compliance Summary: {compliance_summary}")
    st.success(f"📏 Margin Check: {margin_check}")
    st.info(f"🔎 Supply/Demand Risk: {supply_demand}")

    if st.button("💾 Save Scenario"):
        scenario = {
            "date": str(datetime.today().date()),
            "fuel_price": price,
            "cost_price": cost,
            "competitor_price": comp_price,
            "volume_predicted": prediction,
            "margin_check": margin_check,
            "strategy": pricing_strategy
        }
        pd.DataFrame([scenario]).to_csv(f"saved_scenarios/scenario_{scenario['date']}.csv", index=False)
        st.success("Scenario saved!")