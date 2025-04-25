import pandas as pd
from datetime import datetime
from pathlib import Path

# Example input
scenario = {
    "fuel_price": 1.85,
    "cost_price": 1.65,
    "competitor_price": 1.80,
    "volume_predicted": 5150,
    "date": str(datetime.today().date())
}

df = pd.DataFrame([scenario])
Path("saved_scenarios").mkdir(exist_ok=True)
df.to_csv(f"saved_scenarios/scenario_{scenario['date']}.csv", index=False)
print("✅ Scenario saved!")