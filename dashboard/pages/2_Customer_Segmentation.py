from utils.paths import *
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Customer Segmentation",
    page_icon="👥",
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
    background:linear-gradient(135deg,#7c3aed,#2563eb);
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
    border-left:6px solid #7c3aed;
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
    OUTPUT_DIR / "customer_segments.csv"
)

# -----------------------------
# KPI Calculations
# -----------------------------

total_customers = len(df)

num_clusters = df["Cluster"].nunique()

largest_cluster = df["Cluster"].value_counts().idxmax()

largest_count = df["Cluster"].value_counts().max()

# -----------------------------
# Hero Section
# -----------------------------

st.markdown("""
<div class="hero">

<h1>👥 Customer Segmentation Dashboard</h1>

<h3>
RFM Analysis & Customer Intelligence
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
        "👥 Customers",
        f"{total_customers:,}"
    )

with c2:
    kpi_card(
        "📊 Segments",
        num_clusters
    )

with c3:
    kpi_card(
        "🏆 Largest Cluster",
        f"{largest_cluster}"
    )

with c4:
    kpi_card(
        "📈 Cluster Size",
        f"{largest_count:,}"
    )

st.write("")

# -----------------------------
# Cluster Distribution
# -----------------------------

st.markdown(
    '<div class="section-title">📊 Cluster Distribution</div>',
    unsafe_allow_html=True
)

segment_counts = (
    df["Cluster"]
    .value_counts()
    .reset_index()
)

segment_counts.columns = ["Cluster", "Customers"]

# -----------------------------
# Charts
# -----------------------------

col1, col2 = st.columns(2)

with col1:

    fig_bar = px.bar(
        segment_counts,
        x="Cluster",
        y="Customers",
        text="Customers",
        color="Customers"
    )

    fig_bar.update_layout(
        height=500,
        paper_bgcolor="white",
        plot_bgcolor="white"
    )

    st.plotly_chart(
        fig_bar,
        use_container_width=True
    )

with col2:

    fig_pie = px.pie(
        segment_counts,
        names="Cluster",
        values="Customers",
        hole=0.55
    )

    fig_pie.update_layout(
        height=500
    )

    st.plotly_chart(
        fig_pie,
        use_container_width=True
    )


    # -----------------------------
# RFM Segment Analysis
# -----------------------------

st.markdown(
    '<div class="section-title">💎 RFM Segment Analysis</div>',
    unsafe_allow_html=True
)

rfm_summary = (
    df.groupby("Cluster")[["Recency", "Frequency", "Monetary"]]
    .mean()
    .reset_index()
)

fig_rfm = px.bar(
    rfm_summary,
    x="Cluster",
    y="Monetary",
    color="Frequency",
    text_auto=".0f",
    title="Average Monetary Value by Cluster"
)

fig_rfm.update_layout(
    height=550,
    paper_bgcolor="white",
    plot_bgcolor="white"
)

st.plotly_chart(
    fig_rfm,
    use_container_width=True
)



# -----------------------------
# Customer Intelligence
# -----------------------------

st.markdown("""
<div class="insight-card">

<h3>🤖 Customer Intelligence</h3>

Customer segmentation reveals distinct behavioral groups.

The largest cluster represents the majority of active customers.

Smaller clusters may contain premium, high-value,
or niche customer segments that deserve targeted campaigns.

RFM analysis can support retention strategies,
personalized marketing, and customer lifetime value optimization.

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
    f"Total Customers Analyzed: {total_customers:,}"
)

st.success(
    f"Customer Segments Identified: {num_clusters}"
)

st.success(
    f"Dominant Segment: Cluster {largest_cluster}"
)

st.success(
    "Segmentation Model Operational"
)





from utils.footer import show_footer

show_footer()