import streamlit as st

def show_footer():
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align:center;color:gray'>
        RetailPulse Analytics Platform © 2026 |
        Built with Python, Streamlit, XGBoost, Prophet & Evidently
        </div>
        """,
        unsafe_allow_html=True
    )