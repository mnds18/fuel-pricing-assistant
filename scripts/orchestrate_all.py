import subprocess

print("🚀 Step 1: Train model...")
subprocess.run(["python", "scripts/train_model_xgb.py"], check=True)

print("📊 Step 2: Generate price-margin tradeoff chart...")
subprocess.run(["python", "scripts/margin_tradeoff_chart.py"], check=True)

print("📈 Step 3: Generate margin-over-time chart...")
subprocess.run(["python", "scripts/margin_over_time_chart.py"], check=True)

print("💾 Step 4: Save example scenario...")
subprocess.run(["python", "scripts/save_scenario_example.py"], check=True)

print("🧠 Step 5: Run all agents...")
subprocess.run(["python", "scripts/run_all_agents.py"], check=True)

# Optional: Launch Streamlit
import sys
if "--launch-ui" in sys.argv:
    print("🎛️ Launching Streamlit App...")
    subprocess.run(["streamlit", "run", "app/human_loop_app.py"])

print("✅ Full pipeline executed.")