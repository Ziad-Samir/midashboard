# # src/callbacks.py
# def register_callbacks(app):
#     pass  # You’ll add interactive logic here later
# from dash import Input, Output
# import plotly.express as px

# def register_callbacks(app, df):
#     @app.callback(
#         Output('Total-Reveneue-Insurance', 'figure'),
#         Input('hospital-filter', 'value')
#     )
#     def update_chart(selected_hospital):
#         if selected_hospital:
#             filtered_df = df[df['Hospital'] == selected_hospital]
#         else:
#             filtered_df = df

#         fig = px.bar(
#             data_frame=filtered_df,
#             x='Insurance Provider',
#             y='Hospital',
#             title='Total Revenue ',
#             color='Insurance Provider'
#         )
#         fig.update_layout(title_font_size=20)
#         return fig
# src/callbacks.py
from dash import Input, Output
import plotly.express as px

def register_callbacks(app, df):
    @app.callback(
        Output('Total-Revenue-Graph', 'figure'),  # Target the graph with id 'Total-Revenue-Graph'
        Input('hospital-filter', 'value')  # Get the selected hospitals from the dropdown
    )
    def update_chart(selected_hospital):
        if selected_hospital:
            filtered_df = df[df['Hospital'].isin(selected_hospital)]  # Use isin() for multiple selections
        else:
            filtered_df = df  # If no filter is selected, use the whole data
    
        revenue_df = filtered_df.groupby('Insurance Provider')['Revenue'].sum().reset_index()


        # Creating a bar chart for the selected hospital's insurance revenue
        fig = px.bar(
            data_frame=revenue_df,
            x='Insurance Provider',  # X-axis: Insurance Provider
            y='Revenue',  # Y-axis: Total Revenue
            title='Total Revenue by Insurance Provider',
            color='Insurance Provider' , # Color bars by Insurance Provider
            orientation='v',
        )
        
        fig.update_layout(
            title_font_size=20,
            title_font_family='Arial',
            paper_bgcolor='rgba(0,0,0,0)',  
            plot_bgcolor='rgba(0,0,0,0)',
            title=dict(font=dict(color='white',size=22,family='Arial')),
            xaxis=dict(
            title=dict(text='Insurance Provider', font=dict(color="#FFFFFF", size=18, family='Arial')),
            tickfont=dict(color="#FFFFFF", size=14)
            ),
            yaxis=dict(
            title=dict(text='Total Revenue', font=dict(color="#FFFFFF", size=18, family='Arial')),
            tickfont=dict(color="#FFFFFF", size=14)
            ),
            legend=
            dict(font=dict(family='Arial', color="#FFFFFF", size=24))
            )
        fig.update_traces(
            texttemplate='%{y:.0f}',
            textfont=dict(color="#ffffff", family="Arial", weight="bold"),
            textposition='inside',
            marker_line_width=0,
        )
        
        
        
        return fig
