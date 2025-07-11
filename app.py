
from dash import Dash
import dash_bootstrap_components as dbc
from src.layouts import get_layout
from src.callbacks import register_callbacks
from src.data_loader import load_clean_data
import pandas as pd

df, fig_gender, revenue_bar, cards = load_clean_data()
app = Dash( external_stylesheets=[dbc.themes.SLATE])
# app.index_string = '''
# <!DOCTYPE html>
# <html>
#     <head>
#         {%metas%}
#         <title>Health Dashboard</title>
#         <link rel="icon" href="/assets/favicon_v2.png">
#         {%favicon%}
#         {%css%}
#     </head>
#     <body>
#         {%app_entry%}
#         <footer>
#             {%config%}
#             {%scripts%}
#             {%renderer%}
#         </footer>
#     </body>
# </html>
# '''
app.title = "MiDashboard"

app.layout = get_layout(df, fig_gender, revenue_bar, cards) # Load layout from layouts.py
server = app.server
hospital_options = [{"label": hosp, "value": hosp} for hosp in sorted(df['Hospital'].unique())]

# Register callbacks
register_callbacks(app,df)

if __name__ == "__main__":
    app.run(debug=True)
#, external_stylesheets=[dbc.themes.SLATE]