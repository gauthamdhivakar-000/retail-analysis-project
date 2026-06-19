

from utils.paths import *

import streamlit as st
import pandas as pd
import plotly.express as px


with st.sidebar:

    st.image(
    ASSET_DIR / "logo.png",
    width=180
 )
    st.markdown("# RetailPulse")
    st.caption("AI-Powered Retail Intelligence")
    st.markdown("---")

# ==================================================
# PAGE CONFIG
# ==================================================

st.set_page_config(
    page_title="Demand Forecasting",
    page_icon="📈",
    layout="wide"
)

# ==================================================
# MODERN LIGHT THEME CSS
# ==================================================

st.markdown("""
<style>

.stApp{
    background-color:#f8fafc;
}

/* Sidebar */
[data-testid="stSidebar"]{
    background:#ffffff;
}

/* Hero Section */
.hero{
    padding:40px;
    border-radius:25px;
    background:linear-gradient(135deg,#2563eb,#7c3aed);
    color:white;
    text-align:center;
    margin-bottom:25px;
    box-shadow:0px 10px 25px rgba(0,0,0,0.15);
}

/* KPI Cards */
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

/* Section Titles */
.section-title{
    color:#0f172a;
    font-size:30px;
    font-weight:700;
    margin-top:20px;
    margin-bottom:20px;
}

/* Insight Card */
.insight-card{
    background:white;
    padding:25px;
    border-radius:20px;
    border-left:6px solid #3b82f6;
    box-shadow:0px 4px 15px rgba(0,0,0,0.08);
}

</style>
""", unsafe_allow_html=True)

# ==================================================
# SIDEBAR
# ==================================================

with st.sidebar:
    st.markdown("# 📊 RetailPulse")
    st.caption("AI-Powered Retail Analytics")
    st.markdown("---")

# ==================================================
# LOAD DATA
# ==================================================

sales = pd.read_csv(
    DATA_DIR / "daily_sales.csv"
)

sales["ds"] = pd.to_datetime(sales["ds"])

# ==================================================
# KPI CALCULATIONS
# ==================================================

total_sales = sales["y"].sum()
avg_sales = sales["y"].mean()
peak_sales = sales["y"].max()
total_days = len(sales)

peak_row = sales.loc[sales["y"].idxmax()]
peak_date = peak_row["ds"].strftime("%Y-%m-%d")

# ==================================================
# HERO SECTION
# ==================================================

st.markdown("""
<div class="hero">

<h1>📈 Demand Forecasting Dashboard</h1>

<h3>
AI-Driven Sales Forecasting & Trend Intelligence
</h3>

</div>
""", unsafe_allow_html=True)

# ==================================================
# KPI CARD FUNCTION
# ==================================================

def kpi_card(title, value):
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">{title}</div>
        <div class="kpi-value">{value}</div>
    </div>
    """, unsafe_allow_html=True)

# ==================================================
# KPI SECTION
# ==================================================

c1, c2, c3, c4 = st.columns(4)

with c1:
    kpi_card("💰 Total Sales", f"₹{total_sales:,.0f}")

with c2:
    kpi_card("📈 Avg Daily Sales", f"₹{avg_sales:,.0f}")

with c3:
    kpi_card("🔥 Peak Sales", f"₹{peak_sales:,.0f}")

with c4:
    kpi_card("📅 Records", f"{total_days}")

st.write("")
st.write("")

# ==================================================
# SALES TREND CHART
# ==================================================

st.markdown(
    '<div class="section-title">📊 Daily Sales Trend</div>',
    unsafe_allow_html=True
)

fig = px.line(
    sales,
    x="ds",
    y="y",
    markers=True
)

fig.update_traces(
    line=dict(width=4)
)

fig.update_layout(
    paper_bgcolor="white",
    plot_bgcolor="white",
    font=dict(
        color="#0f172a",
        size=14
    ),
    xaxis_title="Date",
    yaxis_title="Sales",
    title="Historical Daily Sales",
    title_font_size=24,
    height=600
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# ==================================================
# AI INSIGHT
# ==================================================

st.markdown("""
<div class="insight-card">

<h3>🤖 AI Forecast Insight</h3>

Demand forecasting indicates stable sales trends.

Inventory planning should maintain adequate safety stock
to prevent stockouts during peak demand periods.

Forecast outputs can directly support inventory
optimization and procurement decisions.

</div>
""", unsafe_allow_html=True)

st.write("")

# ==================================================
# STATUS SECTION
# ==================================================

col1, col2 = st.columns(2)

with col1:
    st.success(f"🔥 Peak Sales Day: {peak_date}")

with col2:
    st.success("✅ Forecasting Pipeline Active")

# ==================================================
# EXECUTIVE SUMMARY
# ==================================================

st.markdown(
    '<div class="section-title">📌 Executive Summary</div>',
    unsafe_allow_html=True
)

st.info(f"""
• Total Sales Processed: ₹{total_sales:,.0f}

• Average Daily Sales: ₹{avg_sales:,.0f}

• Peak Daily Sales: ₹{peak_sales:,.0f}

• Total Records Analyzed: {total_days}

• Historical demand data is ready for forecasting,
inventory optimization and business planning.
""")


from utils.footer import show_footer

show_footer()