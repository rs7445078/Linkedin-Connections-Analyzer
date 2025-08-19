import streamlit as st
from src.utils.viz_utils import create_growth_chart

def create_network_growth(df):
    """Analyze network growth patterns"""
    st.subheader("📊 Network Growth Analysis")
    
    # Use utility function to create growth chart
    fig_growth = create_growth_chart(df)
    st.plotly_chart(fig_growth, use_container_width=True)
    
    # Growth rate analysis
    monthly_growth = df.groupby('Month_Year').size()
    
    col1, col2 = st.columns(2)
    
    with col1:
        avg_monthly = monthly_growth.mean()
        st.metric("Average Monthly Connections", f"{avg_monthly:.1f}")
    
    with col2:
        peak_month = monthly_growth.idxmax()
        peak_count = monthly_growth.max()
        st.metric("Peak Month", f"{peak_month} ({peak_count} connections)")
