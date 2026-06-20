from utils.paths import *
import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

st.set_page_config(
    page_title="Churn Prediction",
    page_icon="⚠️",
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
    background:linear-gradient(135deg,#ef4444,#f97316);
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
    border-left:6px solid #ef4444;
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

model = joblib.load(
    MODEL_DIR / "churn_model.pkl"
)

# -----------------------------
# Predictions
# -----------------------------

X = df[["Recency", "Frequency", "Monetary"]]

df["Churn_Prediction"] = model.predict(X)

# -----------------------------
# KPI Values
# -----------------------------

total_customers = len(df)

churn_customers = int(
    df["Churn_Prediction"].sum()
)

retained_customers = (
    total_customers - churn_customers
)

churn_rate = (
    churn_customers / total_customers
) * 100

# -----------------------------
# Hero Section
# -----------------------------

st.markdown("""
<div class="hero">

<h1>⚠️ Customer Churn Prediction</h1>

<h3>
AI-Powered Retention Intelligence
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
        "⚠️ At Risk",
        f"{churn_customers:,}"
    )

with c3:
    kpi_card(
        "✅ Retained",
        f"{retained_customers:,}"
    )

with c4:
    kpi_card(
        "📉 Churn Rate",
        f"{churn_rate:.1f}%"
    )

st.write("")

# -----------------------------
# Churn Distribution
# -----------------------------

st.markdown(
    '<div class="section-title">📊 Churn Distribution</div>',
    unsafe_allow_html=True
)

churn_summary = pd.DataFrame({
    "Category": ["Retained", "At Risk"],
    "Customers": [retained_customers, churn_customers]
})

fig = px.pie(
    churn_summary,
    names="Category",
    values="Customers",
    hole=0.55,
    color="Category"
)

fig.update_layout(
    height=500
)

st.plotly_chart(
    fig,
    use_container_width=True
)



# -----------------------------
# Churn Risk by Segment
# -----------------------------

st.markdown(
    '<div class="section-title">📊 Churn Risk by Segment</div>',
    unsafe_allow_html=True
)

segment_churn = (
    df.groupby("Cluster")["Churn_Prediction"]
    .sum()
    .reset_index()
)

fig_segment = px.bar(
    segment_churn,
    x="Cluster",
    y="Churn_Prediction",
    color="Churn_Prediction",
    text_auto=True,
    title="At-Risk Customers by Segment"
)

fig_segment.update_layout(
    height=500,
    paper_bgcolor="white",
    plot_bgcolor="white"
)

st.plotly_chart(
    fig_segment,
    use_container_width=True
)



# -----------------------------
# High Risk Customers
# -----------------------------

st.markdown(
    '<div class="section-title">🚨 High Risk Customers</div>',
    unsafe_allow_html=True
)

risk_customers = df[
    df["Churn_Prediction"] == 1
][[
    "CustomerID",
    "Recency",
    "Frequency",
    "Monetary"
]]

st.dataframe(
    risk_customers.head(20),
    use_container_width=True
)

# -----------------------------
# Retention Intelligence
# -----------------------------

st.markdown("""
<div class="insight-card">

<h3>🤖 Retention Intelligence</h3>

Customers flagged as churn risk should be prioritized
for retention campaigns.

The XGBoost model evaluates customer behavior using:

• Recency

• Frequency

• Monetary Value

Customers with poor engagement patterns may require
discounts, loyalty rewards, or personalized outreach.

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
    f"Customers Analysed: {total_customers:,}"
)

st.success(
    f"Predicted Churn Customers: {churn_customers:,}"
)

st.success(
    f"Retention Rate: {(100-churn_rate):.1f}%"
)

st.success(
    "XGBoost Churn Model Operational"
)




from utils.footer import show_footer

show_footer()