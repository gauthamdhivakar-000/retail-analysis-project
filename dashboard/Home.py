
import streamlit as st
import pandas as pd
from pathlib import Path
from utils.metrics import calculate_kpis

st.set_page_config(
    page_title="RetailPulse Analytics",
    page_icon="📊",
    layout="wide"
)

# ==================================================
# PATH CONFIGURATION
# ==================================================

ROOT_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = ROOT_DIR / "data" / "processed"
ASSET_DIR = ROOT_DIR / "dashboard" / "assets"

# ==================================================
# LOAD DATA
# ==================================================

df = pd.read_csv(
    DATA_DIR / "cleaned_data.csv"
)

kpis = calculate_kpis(df)

# ==================================================
# PREMIUM CSS
# ==================================================

st.markdown("""
<style>

.stApp{
    background:#0f172a;
}

#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.hero{
    padding:40px;
    border-radius:25px;
    background:linear-gradient(
        135deg,
        #2563eb,
        #7c3aed
    );
    text-align:center;
    color:white;
    margin-bottom:25px;
    box-shadow:0px 10px 30px rgba(0,0,0,0.25);
}

.kpi-card{
    background:rgba(255,255,255,0.06);
    border:1px solid rgba(255,255,255,0.1);
    backdrop-filter:blur(15px);
    padding:25px;
    border-radius:20px;
    text-align:center;
    transition:0.3s;
}

.kpi-card:hover{
    transform:translateY(-5px);
}

.kpi-title{
    color:#94a3b8;
    font-size:18px;
}

.kpi-value{
    color:white;
    font-size:34px;
    font-weight:700;
}

.section-title{
    color:white;
    font-size:30px;
    font-weight:700;
    margin-top:20px;
    margin-bottom:20px;
}

.info-card{
    background:#1e293b;
    padding:25px;
    border-radius:20px;
    color:white;
    border-left:5px solid #3b82f6;
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:

    st.image(
        ASSET_DIR / "logo.png",
        width=180
    )

    st.markdown("# 📊 RetailPulse AI")

    st.caption(
        "Advanced Retail Intelligence Platform"
    )

    st.markdown("---")

    st.success("🟢 System Status: Online")

# ==================================================
# HERO SECTION
# ==================================================

st.markdown("""
<div class="hero">

<h1>📊 RetailPulse Analytics Platform</h1>

<h3>
AI-Powered Forecasting, Customer Intelligence,
Inventory Optimization & Model Monitoring
</h3>

</div>
""", unsafe_allow_html=True)

# ==================================================
# KPI SECTION
# ==================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">💰 Revenue</div>
        <div class="kpi-value">₹{kpis['Revenue']:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">🛒 Orders</div>
        <div class="kpi-value">{kpis['Orders']:,}</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">👥 Customers</div>
        <div class="kpi-value">{kpis['Customers']:,}</div>
    </div>
    """, unsafe_allow_html=True)

with c4:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">📦 Avg Order Value</div>
        <div class="kpi-value">₹{kpis['AOV']:,.0f}</div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

# ==================================================
# EXECUTIVE SUMMARY
# ==================================================

st.markdown(
    '<div class="section-title">📌 Executive Summary</div>',
    unsafe_allow_html=True
)

st.markdown("""
<div class="info-card">

RetailPulse combines:

✅ Demand Forecasting

✅ Customer Segmentation

✅ Churn Prediction

✅ Inventory Optimization

✅ Drift Detection

✅ Automated Retraining

into a unified AI-powered retail intelligence platform.

</div>
""", unsafe_allow_html=True)

# ==================================================
# AVAILABLE MODULES
# ==================================================

st.markdown(
    '<div class="section-title">⚡ Available Modules</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.info("📈 Demand Forecasting")

with col2:
    st.info("👥 Customer Segmentation")

with col3:
    st.info("⚠️ Churn Prediction")

col4, col5, col6 = st.columns(3)

with col4:
    st.info("📦 Inventory Optimization")

with col5:
    st.info("📊 Model Monitoring")

with col6:
    st.info("🔄 Automated Retraining")

# ==================================================
# PLATFORM STATUS
# ==================================================

st.markdown(
    '<div class="section-title">🚀 Platform Status</div>',
    unsafe_allow_html=True
)

st.success("All Analytics Services Operational")

st.progress(100)

# ==================================================
# FOOTER
# ==================================================

st.markdown("---")

st.caption(
    "RetailPulse AI • Enterprise Analytics Platform • Version 3.0"
)
