import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

df = pd.read_csv("data/raw/fuel_sales_data.csv", parse_dates=["date"])
df["daily_margin"] = (df["fuel_price"] - df["cost_price"]) * df["volume_sold"]
margin_over_time = df.groupby("date")["daily_margin"].sum().reset_index()

plt.figure(figsize=(10, 5))
plt.plot(margin_over_time["date"], margin_over_time["daily_margin"], marker="o")
plt.title("Total Daily Margin Over Time")
plt.xlabel("Date")
plt.ylabel("Margin ($)")
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()

Path("docs").mkdir(exist_ok=True)
plt.savefig("docs/margin_over_time.png")
print("✅ Saved to docs/margin_over_time.png")