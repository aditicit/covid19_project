import pandas as pd
import plotly.express as px  # (version 4.7.0)
#import plotly.graph_objects as go


import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': '#119DFF',
    'color': 'white',
    'padding': '6px'
}

df = pd.read_csv("C:\\Users\\LENOVO\\WebScrapping\\covidreport.csv")
df = df.dropna()
df_continent = df['Continents'].value_counts().keys()

df1 = pd.read_csv("https://s3.amazonaws.com/rawstore.datahub.io/f6f2ac7be65b7d271b8a3b74df3ad724.csv")
df_Ind = df1[df1['Country'] == 'India']
print(df_Ind[:5])
df2_rest = pd.read_csv("https://s3.amazonaws.com/rawstore.datahub.io/9dc095afacc22888e66192aa23e71314.csv")


# App layout
layout = html.Div([

    html.Div([

        html.H3("Continent-wise Covid cases", style={'text-align': 'center'}),

        dcc.Dropdown(
            id="option_slctd",
            options=[{"label": x1, "value": x1}
                     for x1 in df_continent],
            value=df_continent[1],
            clearable=False,
            style={'width': "40%"}
        ),

        #html.Div(id='output_container', children=[]),
        html.Br(),

        dcc.Graph(id='covid_map',style={'width': "100%"})

    ])

])


# ------------------------------------------------------------------------------
# Connect the Plotly graphs with Dash Components
@app.callback(

     Output(component_id="covid_map", component_property="figure"),

    [Input(component_id='option_slctd', component_property='value')]

)
def update_graph(option_slctd):

    #container = "The Continent chosen by user was: {}".format(option_slctd)

    dff = df.copy()
    dff = dff[dff["Continents"] == option_slctd]

    # Plotly Express
    fig = px.choropleth(
        data_frame=dff,
        locationmode='country names',
        locations='Country',
        scope="world",
        color='Deaths',
        hover_data=['Country', 'Deaths', 'Confirmed'],
        color_continuous_scale=px.colors.sequential.YlOrRd,
        labels={'Deaths': 'No. of Deaths'},
        width=900, height=700,
        template='plotly_dark'
    )

    return fig

