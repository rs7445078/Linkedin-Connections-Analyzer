import streamlit as st
import pandas as pd
from src.utils.data_utils import preprocess_linkedin_data

@st.cache_data
def load_data(uploaded_file=None):
    """Load and preprocess the LinkedIn connections data
    
    Args:
        uploaded_file: The uploaded file from Streamlit's file_uploader
    """
    try:
        # Handle file from different sources
        if uploaded_file is not None:
            # If file was uploaded via Streamlit UI
            df = pd.read_csv(uploaded_file)
            st.sidebar.caption(f"✅ Using: {uploaded_file.name}")
        else:
            # Use default file
            df = pd.read_csv('data/Connections.csv')
            st.sidebar.caption("⚙️ Using default file")
            
        # Preprocess data using utility function
        df = preprocess_linkedin_data(df)
        
        return df
    except Exception as e:
        st.error(f"Error loading data: {e}")
        return None
