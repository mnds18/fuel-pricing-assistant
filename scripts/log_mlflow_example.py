import mlflow
import random

def log_model():
    with mlflow.start_run():
        mlflow.log_param("model_type", "XGBoost")
        mlflow.log_param("features", 8)
        mlflow.log_metric("rmse", random.uniform(0.1, 0.2))
        print("MLflow run logged!")

if __name__ == "__main__":
    log_model()
