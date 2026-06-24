from utils.paths import *

import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Model Monitoring",
    page_icon="📊",
    layout="wide"
)

with st.sidebar:

    st.image(
    ASSET_DIR / "logo.png",
    width=180
)

    st.markdown("# RetailPulse")
    st.caption("AI-Powered Retail Intelligence")
    st.markdown("---")

# -----------------------------
# CSS
# -----------------------------

st.markdown("""
<style>

.stApp{
    background-color:#f8fafc;
}

.kpi-card{
    background:white;
    padding:25px;
    border-radius:20px;
    text-align:center;
    box-shadow:0px 4px 15px rgba(0,0,0,0.08);
    border:1px solid #e2e8f0;
}

.kpi-title{
    color:#64748b;
    font-size:16px;
    font-weight:600;
}

.kpi-value{
    color:#0f172a;
    font-size:32px;
    font-weight:800;
}

.hero{
    padding:40px;
    border-radius:25px;
    background:linear-gradient(135deg,#0ea5e9,#2563eb);
    color:white;
    text-align:center;
    margin-bottom:25px;
}

.section-title{
    color:#0f172a;
    font-size:28px;
    font-weight:700;
}

.insight-card{
    background:white;
    padding:25px;
    border-radius:20px;
    border-left:6px solid #2563eb;
    box-shadow:0px 4px 15px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Sidebar
# -----------------------------

with st.sidebar:
    st.markdown("# 📊 RetailPulse")
    st.caption("AI-Powered Retail Analytics")
    st.markdown("---")

# -----------------------------
# Load Data
# -----------------------------



drift = pd.read_csv(
    REPORT_DIR / "drift_summary.csv"
)

history = pd.read_csv(
    REPORT_DIR / "retraining_history.csv"
)

log = pd.read_csv(
    REPORT_DIR / "retraining_log.csv"
)

# -----------------------------
# Metrics
# -----------------------------

metrics = dict(zip(
    drift["Metric"],
    drift["Value"]
))

columns_monitored = metrics["Columns Monitored"]
columns_drift = metrics["Columns with Drift"]
drift_percentage = metrics["Drift Percentage"]

status = (
    "Healthy"
    if str(drift_percentage) == "0%"
    else "Drift Detected"
)

# -----------------------------
# Hero Section
# -----------------------------

st.markdown("""
<div class="hero">

<h1>📊 Model Monitoring Dashboard</h1>

<h3>
Drift Detection, Model Health & Retraining Intelligence
</h3>

</div>
""", unsafe_allow_html=True)

# -----------------------------
# KPI Function
# -----------------------------

def kpi_card(title, value):
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">{title}</div>
        <div class="kpi-value">{value}</div>
    </div>
    """, unsafe_allow_html=True)

# -----------------------------
# KPI Cards
# -----------------------------

c1,c2,c3,c4 = st.columns(4)

with c1:
    kpi_card(
        "📈 Features Monitored",
        columns_monitored
    )

with c2:
    kpi_card(
        "⚠️ Drift Features",
        columns_drift
    )

with c3:
    kpi_card(
        "📊 Drift %",
        drift_percentage
    )

with c4:
    kpi_card(
        "🔄 Retraining Events",
        len(history)
    )

st.write("")

# -----------------------------
# Model Health
# -----------------------------

st.markdown(
    '<div class="section-title">🩺 Model Health Status</div>',
    unsafe_allow_html=True
)

if str(drift_percentage) == "0%":
    st.success(
        "✅ Model Status: Healthy"
    )
else:
    st.warning(
        "⚠️ Model Status: Drift Detected"
    )



    # -----------------------------
# Alert Center
# -----------------------------

st.markdown(
    '<div class="section-title">🚨 Alert Center</div>',
    unsafe_allow_html=True
)

if str(drift_percentage) == "0%":
    st.success(
        "✅ No active alerts. Model is operating normally."
    )
else:
    st.error(
        "🚨 Drift detected. Model retraining recommended."
    )



    # -----------------------------
# Real-Time Monitoring Metrics
# -----------------------------

st.markdown(
    '<div class="section-title">📡 Monitoring Metrics</div>',
    unsafe_allow_html=True
)

m1, m2, m3 = st.columns(3)

with m1:
    st.metric(
        "Model Status",
        status
    )

with m2:
    st.metric(
        "Drift Features",
        columns_drift
    )

with m3:
    st.metric(
        "Monitoring Coverage",
        f"{columns_monitored} Features"
    )


    

# -----------------------------
# Drift Summary Chart
# -----------------------------

st.markdown(
    '<div class="section-title">📊 Drift Monitoring Summary</div>',
    unsafe_allow_html=True
)

fig = px.bar(
    drift,
    x="Metric",
    y="Value",
    text="Value",
    color="Metric"
)

fig.update_layout(
    height=550,
    paper_bgcolor="white",
    plot_bgcolor="white",
    showlegend=False
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# Retraining History
# -----------------------------

st.markdown(
    '<div class="section-title">🔄 Retraining History</div>',
    unsafe_allow_html=True
)

st.dataframe(
    history,
    use_container_width=True
)

# -----------------------------
# Retraining Logs
# -----------------------------

st.markdown(
    '<div class="section-title">📋 Retraining Logs</div>',
    unsafe_allow_html=True
)

st.dataframe(
    log,
    use_container_width=True
)

# -----------------------------
# Monitoring Intelligence
# -----------------------------

st.markdown("""
<div class="insight-card">

<h3>🤖 Monitoring Intelligence</h3>

The monitoring pipeline continuously evaluates
data quality and model stability.

Drift detection helps identify shifts in
incoming business data that may impact
forecasting performance.

Automated retraining workflows ensure that
models remain accurate and production-ready.

</div>
""", unsafe_allow_html=True)

st.write("")

# -----------------------------
# Executive Summary
# -----------------------------

st.markdown(
    '<div class="section-title">📌 Executive Summary</div>',
    unsafe_allow_html=True
)

st.success(
    f"Features Monitored: {columns_monitored}"
)

st.success(
    f"Features Showing Drift: {columns_drift}"
)

st.success(
    f"Current Drift Level: {drift_percentage}"
)

st.success(
    "Monitoring & Retraining Pipeline Operational"
)




from utils.footer import show_footer

show_footer()
