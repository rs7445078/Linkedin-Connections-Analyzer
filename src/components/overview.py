import streamlit as st

def create_overview_metrics(df):
    """Create overview metrics"""
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric("Total Connections", len(df))
    
    with col2:
        unique_companies = df['Company'].nunique()
        st.metric("Unique Companies", unique_companies)
    
    # Top 10 Companies
    st.subheader("Top 10 Companies")
    top_companies = df['Company'].value_counts().head(10).reset_index()
    top_companies.columns = ['Company', 'Number of Connections']
    st.dataframe(top_companies, use_container_width=True)
