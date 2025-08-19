import streamlit as st
from src.utils.data_utils import get_company_statistics
from src.utils.viz_utils import create_horizontal_bar_chart

def create_company_analysis(df):
    """Analyze connections by company"""
    st.subheader("🏢 Company Analysis")
    
    # Get statistics using utility function
    company_stats = get_company_statistics(df)
    top_companies = company_stats['top_companies']
    company_sizes = company_stats['company_sizes']
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig_companies = create_horizontal_bar_chart(
            values=top_companies.values,
            labels=top_companies.index,
            title='Top 20 Companies',
            x_label='Number of Connections',
            y_label='Company'
        )
        st.plotly_chart(fig_companies, use_container_width=True)
    
    with col2:
        # Company size distribution
        fig_sizes = create_horizontal_bar_chart(
            values=company_sizes.values,
            labels=company_sizes.index,
            title='Company Size Distribution',
            x_label='Number of Connections from Company',
            y_label='Number of Companies'
        )
        st.plotly_chart(fig_sizes, use_container_width=True)
