import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import joblib

# Load trained model
model = joblib.load("models/xgb_demand_forecaster.pkl")

# Generate prices and predict volumes
prices = np.linspace(1.60, 2.00, 20)
cost = 1.60
comp_price = 1.75
volume_preds = []

for price in prices:
    df = pd.DataFrame([{
        "fuel_price": price,
        "competitor_price": comp_price,
        "cost_price": cost,
        "price_gap": price - comp_price,
        "dayofweek": 2,
        "month": 4
    }])
    volume = model.predict(df)[0]
    margin = (price - cost) * volume
    volume_preds.append(margin)

# Plot
plt.figure(figsize=(10, 5))
plt.plot(prices, volume_preds, marker='o')
plt.title("Expected Margin vs Price")
plt.xlabel("Fuel Price ($)")
plt.ylabel("Expected Daily Margin ($)")
plt.grid(True)
plt.tight_layout()
plt.savefig("docs/price_margin_tradeoff.png")
print("Saved chart to docs/price_margin_tradeoff.png")