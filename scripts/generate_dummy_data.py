import pandas as pd
import numpy as np
from pathlib import Path

np.random.seed(42)

locations = ["Station_A", "Station_B", "Station_C"]
num_days = 60

rows = []
for loc in locations:
    for day in pd.date_range(end=pd.Timestamp.today(), periods=num_days):
        price = np.random.uniform(1.60, 2.00)
        comp_price = price + np.random.uniform(-0.05, 0.05)
        vol = max(1000, np.random.normal(5000, 800))
        cost = price - np.random.uniform(0.10, 0.20)
        margin = (price - cost) * vol
        rows.append([day.date(), loc, price, comp_price, vol, cost, margin])

df = pd.DataFrame(rows, columns=[
    "date", "location", "fuel_price", "competitor_price", "volume_sold", "cost_price", "daily_margin"
])

output_path = Path("data/raw/fuel_sales_data.csv")
output_path.parent.mkdir(parents=True, exist_ok=True)
df.to_csv(output_path, index=False)
print(f"Dummy data saved to {output_path}")
