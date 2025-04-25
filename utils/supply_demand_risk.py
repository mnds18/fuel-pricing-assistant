def supply_demand_risk(price_gap, volume):
    if price_gap < -0.05 and volume > 6000:
        return "⚠️ High risk of demand surge or supply shortage."
    return "✅ Stable supply/demand balance."