import streamlit as st
import pandas as pd

from utils.paths import DATA_DIR, OUTPUT_DIR


@st.cache_data
def load_cleaned_data():
    return pd.read_csv(
        DATA_DIR / "cleaned_data.csv"
    )


@st.cache_data
def load_daily_sales():
    return pd.read_csv(
        DATA_DIR / "daily_sales.csv"
    )


@st.cache_data
def load_segments():
    return pd.read_csv(
        OUTPUT_DIR / "customer_segments.csv"
    )