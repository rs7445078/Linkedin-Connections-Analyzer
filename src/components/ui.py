import streamlit as st

def setup_page():
    """Set the page configuration and styling"""
    st.set_page_config(
        page_title="LinkedIn Analysis",
        page_icon=":bar_chart:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Custom CSS for better styling
    st.markdown("""
    <style>
        .main-header {
            font-size: 3rem;
            color: #0077B5;
            text-align: center;
            margin-bottom: 2rem;
        }
        .metric-card {
            background-color: #f0f2f6;
            padding: 1rem;
            border-radius: 10px;
            border-left: 5px solid #0077B5;
        }
    </style>
    """, unsafe_allow_html=True)

def display_header():
    """Display the main header"""
    st.markdown('<h1 class="main-header">LinkedIn Network Analysis Dashboard</h1>', 
                unsafe_allow_html=True)

def display_footer():
    """Display the footer"""
    st.markdown("---")
    st.markdown("*Built with Streamlit for LinkedIn Network Analysis*")
