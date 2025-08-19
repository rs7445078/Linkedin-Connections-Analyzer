"""
Visualization utility functions
"""
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd

def create_horizontal_bar_chart(values, labels, title, x_label, y_label):
    """
    Create a horizontal bar chart
    
    Args:
        values: Values for the bars
        labels: Labels for the bars
        title: Chart title
        x_label: X-axis label
        y_label: Y-axis label
    
    Returns:
        Plotly figure
    """
    fig = px.bar(
        x=values, 
        y=labels,
        orientation='h',
        title=title,
        labels={'x': x_label, 'y': y_label}
    )
    fig.update_layout(yaxis={'categoryorder':'total ascending'})
    
    return fig

def create_company_comparison_chart(filtered_df, full_df, company_name):
    """
    Create a comparison chart showing growth of connections at a specific company versus all companies
    
    Args:
        filtered_df: DataFrame filtered to a specific company
        full_df: Complete connections DataFrame
        company_name: Name of the company being analyzed
    
    Returns:
        Plotly figure with dual y-axes
    """
    # Create timeline for company vs. all
    company_timeline = filtered_df.groupby('Year').size().reset_index()
    company_timeline.columns = ['Year', 'Company Connections']
    
    all_timeline = full_df.groupby('Year').size().reset_index()
    all_timeline.columns = ['Year', 'All Connections']
    
    # Merge the two timelines
    merged_timeline = pd.merge(company_timeline, all_timeline, on='Year')
    
    # Create a plotly figure with two y-axes
    fig = make_subplots(specs=[[{"secondary_y": True}]])
    
    # Add traces
    fig.add_trace(
        go.Bar(x=merged_timeline['Year'], y=merged_timeline['Company Connections'], name=company_name),
        secondary_y=False,
    )
    
    fig.add_trace(
        go.Scatter(x=merged_timeline['Year'], y=merged_timeline['All Connections'], name="All Companies", line=dict(color='red')),
        secondary_y=True,
    )
    
    # Set titles
    fig.update_layout(
        title_text=f"Connection Growth: {company_name} vs All Companies"
    )
    fig.update_xaxes(title_text="Year")
    fig.update_yaxes(title_text=f"{company_name} Connections", secondary_y=False)
    fig.update_yaxes(title_text="All Connections", secondary_y=True)
    
    return fig

def create_growth_chart(df):
    """
    Create cumulative growth chart
    
    Args:
        df: DataFrame with connection data
    
    Returns:
        Plotly line chart
    """
    df_sorted = df.sort_values('Connected On')
    df_sorted['Cumulative'] = range(1, len(df_sorted) + 1)
    
    fig = px.line(
        df_sorted,
        x='Connected On',
        y='Cumulative',
        title='Cumulative Network Growth',
        labels={'Connected On': 'Date', 'Cumulative': 'Total Connections'}
    )
    
    return fig
