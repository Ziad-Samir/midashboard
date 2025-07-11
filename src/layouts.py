# src/layouts.py
from dash import html, dcc
import dash_bootstrap_components as dbc
# # Layout
def get_layout(df, fig_gender, revenue_bar, cards):
    layout = dbc.Container([
        html.Div(style={"height": "120px"}), 

        html.H1(
        "Top 20 Hospitals Dashboard",
        className="text-center my-1",
        style={"color": "#97ffff"}
    ),
    html.Div(style={"height": "120px"}), 
    dbc.Row(cards, className="mb-5"),

        dbc.Row([
            dbc.Col(dcc.Graph(figure=fig_gender, config={
        'displaylogo': False  # This removes the Plotly logo
    }),  className="zoom-in",md=4),
            dbc.Col(dcc.Graph(figure=revenue_bar),className="zoom-in", md=7),
        ]),
   
           dbc.Row([
            dbc.Col([
                dcc.Dropdown(
                    id='hospital-filter',
                    options=[{'label': hospital, 'value': hospital} for hospital in df['Hospital'].unique()],
                    placeholder="Select a hospital",
                    multi=True,
                    
                )
            ],className="zoom-in", width=4),
        ], className="mb-4"),
           dbc.Row([
            dbc.Col(dcc.Graph(id='Total-Revenue-Graph'),className="zoom-in", width=12)  # This is the output graph to update
        ]),

    
    ], fluid=True)

    return layout
