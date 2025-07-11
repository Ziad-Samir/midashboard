from dash import html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('data/Top20hospitals.csv')
df.rename(columns={'Unnamed: 0':'ID','Billing Amount' :'Revenue'},inplace=True)
df.drop('lenght Of Stay',axis=1,inplace=True)
df['Date of Admission']=pd.to_datetime(df['Date of Admission'],errors='coerce')
df['Discharge Date']=pd.to_datetime(df['Discharge Date'],errors='coerce')
df['Lenght Of Stay']=df['Discharge Date']-df['Date of Admission']
df['Revenue'].round(1)


# Pre-calculate KPI values
total_patients = df['Name'].nunique()
avg_age = round(df['Age'].mean(), 1)
avg_stay = df["Lenght Of Stay"].mean().days

# Pie chart: Gender
fig_gender = px.pie(df, names='Gender',
                     title='Gender Distribution',
                     color='Gender', 
                     color_discrete_map={
                    'Male': '#1f77b4',      # Blue
                    'Female': "#df38ad"     # Pinkish
    },
    hole=0.5,
    )
fig_gender.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',  
    plot_bgcolor='rgba(0,0,0,0)',
    title=dict(font=dict(color='white',size=22,family='Arial')),
    margin=dict(l=100, r=40, t=60, b=40),
    legend= dict(font=dict(family='Arial', color="#FFFFFF", size=14)),
   
        

)

# Bar chart: Revenue by hospital
# import plotly.express as px

# Group and sort data
revenue_df = (
    df.groupby('Hospital')['Revenue']
    .sum()
    .sort_values(ascending=False)
    .reset_index()
    .round()

)

# Bar chart
revenue_bar = px.bar(
    revenue_df,
    x='Revenue',
    y='Hospital',  # horizontal bar chart
    orientation='h',
    title='Total Revenue by Hospital',
    text='Revenue',  # display values on bars
    #color='Revenue',  # color by revenue values
    color_continuous_scale='blues'  # or 'Viridis', 'Teal', etc.
)
revenue_bar.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',  
    plot_bgcolor='rgba(0,0,0,0)',
    # title_font_size=22,
    # title_font_family='Arial',
    title=dict(font=dict(color='white',size=22,family='Arial')),
    margin=dict(l=100, r=40, t=60, b=40),
    
    xaxis=dict(
        title=dict(text='Total Revenue', font=dict(color="#FFFFFF", size=18, family='Arial')),
        tickfont=dict(color="#FFFFFF", size=14)
    ),
    
    yaxis=dict(
        title=dict(text='Hospital', font=dict(color="#FFFFFF", size=18, family='Arial')),
        tickfont=dict(color="#FFFFFF", size=14)
    ),
    legend=dict(font=dict(family='Arial', color="#FFFFFF", size=14))
)


# Text appearance
revenue_bar.update_traces(
    texttemplate='%{text:.2s}',  # rounded text on bars
    textfont=dict(color="#ffffff"),
    textposition='outside',
    marker_line_width=0,
   
)

# Cards
cards = dbc.Row([
    dbc.Col(dbc.Card(dbc.CardBody([html.H5("Total Patients"), html.H2(f"{total_patients}")]), color="primary", inverse=True), md=4),
    dbc.Col(dbc.Card(dbc.CardBody([html.H5("Average Age"), html.H2(f"{avg_age}")]), color="#335c8b8f", inverse=True), md=4),
    dbc.Col(dbc.Card(dbc.CardBody([html.H5("Average Stay (days)"), html.H2(f"{avg_stay}")]), color="#335c8b", inverse=True), md=4),

])
