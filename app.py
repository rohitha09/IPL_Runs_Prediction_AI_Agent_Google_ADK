import streamlit as st
import json
import os
import pandas as pd
import plotly.express as px


st.set_page_config(
    page_title="IPL Prediction Results",
    layout="wide",
    page_icon="🏏"
)

st.markdown("""
<style>
.big-title {
    font-size: 40px !important;
    font-weight: 700;
    text-align: center;
    color: #1a73e8;
     margin-bottom: -10px;
}
.sub-text {
    text-align: center;
    font-size: 18px;
    color: #666;
}
.metric-card {
    background: linear-gradient(135deg, #e3f2fd, #bbdefb);
    padding: 25px;
    border-radius: 20px;
    text-align: center;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}
.best-model-card {
    background: linear-gradient(135deg, #fff3e0, #ffe0b2);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0 4px 15px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)
# Title

st.markdown('<div class="big-title">🏏 IPL 2026 — Prediction Results Dashboard</div>',
            unsafe_allow_html=True)
st.markdown('<div class="sub-text">AI Model Performance Summary</div>',
            unsafe_allow_html=True)
st.write("")



# Load JSON

RESULT_PATH = "step4_predictions.json"

def load_results():
    if os.path.exists(RESULT_PATH):
        with open(RESULT_PATH, "r") as f:
            return json.load(f)
    return None

results = load_results()

if results is None:
    st.error("❌ Prediction results file not found! Run your pipeline first.")
    st.stop()
st.success("Prediction results loaded successfully!")


# BEST MODEL SECTION

st.subheader("🏆 Best Model Overview")

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="best-model-card">', unsafe_allow_html=True)
    st.markdown("### ⭐ Best Model")
    st.markdown(f"<h2>{results['best_model'].upper()}</h2>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.markdown("### 🎯 Best Accuracy")
    acc = round(results["best_accuracy"] * 100, 2)
    st.markdown(f"<h2>{acc}%</h2>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)



# MODEL PERFORMANCE CHART

st.subheader("📊 Model Accuracy Comparison")

model_data = pd.DataFrame({
    "Model": list(results["all_models"].keys()),
    "Accuracy": [results["all_models"][m]["accuracy"] * 100 for m in results["all_models"]]
})

fig = px.bar(
    model_data,
    x="Model",
    y="Accuracy",
    color="Model",
    text=[f"{a:.2f}%" for a in model_data["Accuracy"]],
    title="Model Accuracy (%)",
     height=450
)
fig.update_traces(textposition="outside")
fig.update_layout(showlegend=False)

st.plotly_chart(fig, use_container_width=True)