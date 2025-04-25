import os

folders = [
    "app", "agents", "data/raw", "data/processed", "docs", "mlflow_logs",
    "models", "notebooks", "scripts", "tests", "utils"
]

base_dir = "fuel-pricing-assistant"
for folder in folders:
    os.makedirs(os.path.join(base_dir, folder), exist_ok=True)
