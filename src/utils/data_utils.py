"""
Data processing utility functions
"""
import pandas as pd

def preprocess_linkedin_data(df):
    """
    Clean and preprocess LinkedIn connections data
    
    Args:
        df: DataFrame containing LinkedIn connections data
        
    Returns:
        Processed DataFrame
    """
    # Process dates
    df['Connected On'] = pd.to_datetime(df['Connected On'], format='%d %b %Y')
    df['Year'] = df['Connected On'].dt.year
    df['Month'] = df['Connected On'].dt.month
    df['Month_Year'] = df['Connected On'].dt.to_period('M')
    
    # Clean company and position data
    df['Company'] = df['Company'].fillna('Unknown')
    df['Position'] = df['Position'].fillna('Unknown')
    
    # Create full name
    df['Full Name'] = df['First Name'] + ' ' + df['Last Name']
    
    return df

def get_company_statistics(df):
    """
    Generate company statistics from connections data
    
    Args:
        df: DataFrame containing processed LinkedIn connections data
        
    Returns:
        Dictionary containing company statistics
    """
    top_companies = df['Company'].value_counts().head(20)
    unique_companies = df['Company'].nunique()
    company_sizes = df['Company'].value_counts().value_counts().sort_index()
    
    return {
        'top_companies': top_companies,
        'unique_companies': unique_companies,
        'company_sizes': company_sizes
    }

def filter_by_company(df, company_name):
    """
    Filter connections by company name
    
    Args:
        df: DataFrame containing LinkedIn connections data
        company_name: String name of company to filter by
        
    Returns:
        Filtered DataFrame
    """
    if company_name == "All Companies":
        return df
    else:
        return df[df['Company'] == company_name]
