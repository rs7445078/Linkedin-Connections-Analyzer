import streamlit as st

# Import components
from src.components.ui import setup_page, display_header, display_footer
from src.components.data_loader import load_data
from src.components.overview import create_overview_metrics
from src.components.company_analysis import create_company_analysis
from src.components.connection_analysis import create_connection_analysis
from src.components.network_growth import create_network_growth
from src.components.raw_data import display_raw_data

# Setup the page
setup_page()

def main():
    # Display header
    display_header()
    
    # Add compact file upload option in the sidebar
    uploaded_file = st.sidebar.file_uploader(
        "📤 Upload LinkedIn CSV",
        type=["csv"],
        help="Export connections from LinkedIn and upload here"
    )
    st.sidebar.caption("[How to export connections?](https://www.linkedin.com/help/linkedin/answer/a566336/export-connections-from-linkedin)")
    
    # Load data (from uploaded file or default)
    df = load_data(uploaded_file)
    
    if df is None:
        st.error("Could not load the data. Please check if the file exists in the 'data' folder or upload a valid CSV file.")
        return
    
    # Sidebar for navigation
    st.sidebar.title("📊 Analysis Sections")
    analysis_option = st.sidebar.selectbox(
        "Choose Analysis:",
        ["Overview", "Company Analysis", "Connection Analysis", "Network Growth", "Raw Data"]
    )
    
    if analysis_option == "Overview":
        st.header("🎯 Overview")
        create_overview_metrics(df)
        
    elif analysis_option == "Company Analysis":
        create_company_analysis(df)
        
    elif analysis_option == "Connection Analysis":
        create_connection_analysis(df)
        
    elif analysis_option == "Network Growth":
        create_network_growth(df)
        
    elif analysis_option == "Raw Data":
        display_raw_data(df)
    
    # Footer
    display_footer()

if __name__ == "__main__":
    main()