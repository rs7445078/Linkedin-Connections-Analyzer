import streamlit as st

def display_raw_data(df):
    """Display and search raw data"""
    st.subheader("📄 Raw Data")
    st.write(f"Total records: {len(df)}")
    
    # Search functionality
    search_term = st.text_input("Search connections:")
    if search_term:
        mask = (df['Full Name'].str.contains(search_term, case=False, na=False) |
               df['Company'].str.contains(search_term, case=False, na=False) |
               df['Position'].str.contains(search_term, case=False, na=False))
        filtered_df = df[mask]
        st.write(f"Found {len(filtered_df)} matches:")
        st.dataframe(filtered_df, use_container_width=True)
    else:
        st.dataframe(df, use_container_width=True)
