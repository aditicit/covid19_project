import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
import pandas as pd
import plotly.express as px
import numpy as np
from dash.dependencies import Input, Output

from app import app
from apps import app3, app1, app2
df = pd.read_csv("C:\\Users\\LENOVO\\WebScrapping\\covidreport.csv")
df = df.dropna()
fig2 = px.sunburst(df, path=['Continents', 'Country'], values='Confirmed',
                   color='Deaths', hover_data=['Country'],
                   color_continuous_scale='RdBu',
                   color_continuous_midpoint=np.average(df['Deaths'], weights=df['Deaths']))

app.layout = html.Div([

    dcc.Location(id='url', refresh=False),
    html.Div((
        dbc.NavLink("Home||", href='/', active=True),
        dbc.NavLink('World Covid Cases||', href='/apps/app1'),
        dbc.NavLink('India Covid Cases||', href='/apps/app2'),
        dbc.NavLink('Vaccination', href='/apps/app3')
    ), className="row"),
    html.Div(id='page-content', children=[])
])



@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return [
            html.H3("Covid 19 dashboard", style={'text-align': 'center'}),
            dcc.Graph(
            id='graph2',
            figure=fig2,

        )]
    if pathname == '/apps/app1':
        return app1.layout
    if pathname == '/apps/app2':
        return app2.layout
    if pathname == '/apps/app3':
        return app3.layout
    else:
        return "404 error"


if __name__ == '__main__':
    app.run_server(debug=True)
