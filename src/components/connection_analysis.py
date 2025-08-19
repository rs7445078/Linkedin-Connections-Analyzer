import streamlit as st
import plotly.express as px
from src.utils.data_utils import filter_by_company
from src.utils.viz_utils import create_company_comparison_chart

def create_connection_analysis(df):
    """Analyze and filter connections based on company"""
    st.subheader("🔍 Connection Analysis")
    
    # Company filter section
    st.write("### Filter Connections by Company")
    
    # Get all companies and sort them alphabetically
    all_companies = sorted(df['Company'].unique().tolist())
    
    # Create a list with "All Companies" first, then all other companies in alphabetical order
    company_options = ["All Companies"] + all_companies
    
    # Company filter dropdown
    selected_company = st.selectbox("Select a company to analyze:", company_options)
    
    # Use utility function to filter data
    filtered_df = filter_by_company(df, selected_company)
    
    if selected_company == "All Companies":
        st.write(f"Showing all {len(filtered_df)} connections")
    else:
        st.write(f"Showing {len(filtered_df)} connections from **{selected_company}**")
    
    # Display company stats
    if selected_company != "All Companies":
        # Calculate company growth over time
        company_growth = filtered_df.groupby('Year').size()
        
        # Show company growth chart
        fig = px.bar(x=company_growth.index, 
                    y=company_growth.values,
                    title=f'Connections from {selected_company} by Year',
                    labels={'x': 'Year', 'y': 'Number of Connections'})
        st.plotly_chart(fig, use_container_width=True)
        
        # Show positions at this company
        positions = filtered_df['Position'].value_counts().reset_index()
        positions.columns = ['Position', 'Count']
        
        if len(positions) > 0:
            st.write("### Positions at this company")
            st.dataframe(positions, use_container_width=True)
    
    # Display filtered connections
    st.write("### Filtered Connections")
    st.dataframe(filtered_df[['Full Name', 'Position', 'Company', 'Connected On']], use_container_width=True)
    
    # Company comparison
    if selected_company != "All Companies":
        st.write("### Connection Growth Comparison")
        st.write("Compare how your network has grown with this company vs. overall")
        
        # Use utility function to create comparison chart
        fig = create_company_comparison_chart(filtered_df, df, selected_company)
        st.plotly_chart(fig, use_container_width=True)
