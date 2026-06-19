from utils.paths import *
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Inventory Optimization",
    page_icon="📦",
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
    background:linear-gradient(135deg,#10b981,#2563eb);
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
    border-left:6px solid #10b981;
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

df = pd.read_csv(
    DATA_DIR / "inventory_optimization_report.csv"
)

metrics = dict(zip(df["Metric"], df["Value"]))

avg_demand = metrics["Average Daily Demand"]
std_demand = metrics["Demand Std Dev"]
safety_stock = metrics["Safety Stock"]
reorder_point = metrics["Reorder Point"]

# -----------------------------
# Hero Section
# -----------------------------

st.markdown("""
<div class="hero">

<h1>📦 Inventory Optimization</h1>

<h3>
Smart Inventory Planning & Stock Intelligence
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
        "📈 Avg Demand",
        f"{avg_demand:,.0f}"
    )

with c2:
    kpi_card(
        "📊 Demand Variability",
        f"{std_demand:,.0f}"
    )

with c3:
    kpi_card(
        "🛡 Safety Stock",
        f"{safety_stock:,.0f}"
    )

with c4:
    kpi_card(
        "📦 Reorder Point",
        f"{reorder_point:,.0f}"
    )

st.write("")

# -----------------------------
# Inventory Metrics Chart
# -----------------------------

st.markdown(
    '<div class="section-title">📊 Inventory Planning Metrics</div>',
    unsafe_allow_html=True
)

fig = px.bar(
    df,
    x="Metric",
    y="Value",
    text="Value",
    color="Value"
)

fig.update_layout(
    height=550,
    paper_bgcolor="white",
    plot_bgcolor="white"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# Inventory Health Indicator
# -----------------------------

inventory_score = round(
    (safety_stock / reorder_point) * 100,
    1
)

st.metric(
    "📈 Inventory Health Score",
    f"{inventory_score}%"
)

# -----------------------------
# Supply Chain Intelligence
# -----------------------------

st.markdown("""
<div class="insight-card">

<h3>🤖 Supply Chain Intelligence</h3>

Inventory planning has been optimized using
forecasted demand patterns.

Safety stock provides protection against
unexpected demand fluctuations.

The reorder point defines when replenishment
should begin to avoid stockouts.

These metrics support efficient inventory
management while minimizing excess holding costs.

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
    f"Average Daily Demand: {avg_demand:,.0f}"
)

st.success(
    f"Recommended Safety Stock: {safety_stock:,.0f}"
)

st.success(
    f"Optimal Reorder Point: {reorder_point:,.0f}"
)

st.success(
    "Inventory Optimization Model Operational"
)

# -----------------------------
# Recommendation
# -----------------------------

st.markdown("""
<div class="insight-card">

<h3>🎯 Business Recommendation</h3>

Maintain inventory levels above the calculated
safety stock threshold.

Trigger replenishment once inventory reaches
the reorder point.

This strategy helps reduce stockout risk while
avoiding unnecessary inventory carrying costs.

</div>
""", unsafe_allow_html=True)




from utils.footer import show_footer

show_footer()