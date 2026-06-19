import streamlit as st

st.set_page_config(
    page_title="About RetailPulse",
    page_icon="ℹ️",
    layout="wide"
)

with st.sidebar:
    st.markdown("# 📊 RetailPulse")
    st.caption("AI-Powered Retail Analytics")
    st.markdown("---")

st.title("ℹ️ About RetailPulse")

st.markdown("""
## 🚀 RetailPulse Analytics Platform

RetailPulse is an end-to-end retail analytics platform built using:

- Python
- Pandas
- Streamlit
- Plotly
- XGBoost
- Prophet
- Evidently AI

### Features

📈 Demand Forecasting

👥 Customer Segmentation

⚠️ Churn Prediction

📦 Inventory Optimization

📊 Model Monitoring

### Project Objective

Help retailers make data-driven decisions using analytics and machine learning.
""")

st.success("✅ RetailPulse Analytics Platform")