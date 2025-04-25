import pandas as pd
import numpy as np
import xgboost as xgb
import joblib
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from pathlib import Path
from math import sqrt


# Load data
df = pd.read_csv("data/raw/fuel_sales_data.csv")
df["date"] = pd.to_datetime(df["date"])
df["dayofweek"] = df["date"].dt.dayofweek
df["month"] = df["date"].dt.month
df["price_gap"] = df["fuel_price"] - df["competitor_price"]

# Feature set
features = ["fuel_price", "competitor_price", "cost_price", "price_gap", "dayofweek", "month"]
X = df[features]
y = df["volume_sold"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = xgb.XGBRegressor(n_estimators=100, max_depth=3, learning_rate=0.1)
model.fit(X_train, y_train)

# Evaluate
preds = model.predict(X_test)
rmse = sqrt(mean_squared_error(y_test, preds))
y_test_safe = y_test.replace(0, np.finfo(float).eps)
mape = np.mean(np.abs((y_test_safe - preds) / y_test_safe)) * 100
print(f"✅ Model trained.")
print(f"📉 RMSE: {rmse:.2f}")
print(f"📊 MAPE: {mape:.2f}%")

# Save model
Path("models").mkdir(exist_ok=True)
joblib.dump(model, "models/xgb_demand_forecaster.pkl")