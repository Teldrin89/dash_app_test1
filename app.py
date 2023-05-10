# utf8

'''
Information about module?
'''

import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import layout
from dash import Dash, Input, State, Output
import subprocess as sbp
import sys

app = Dash(__name__, external_stylesheets=[dbc.themes.SIMPLEX])


df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = layout.build_app_layout()

@app.callback(
    Output("collapse", "is_open"),
    [Input("collapse-button", "n_clicks")],
    [State("collapse", "is_open")],
    prevent_initial_call=True
)
def toggle_collapse(n, is_open):
    p = sbp.Popen([sys.executable, "script_test.py", "1", "2", "3", "4"])
    p.communicate()

    if n:
        return not is_open
    return is_open

if __name__ == '__main__':
    app.run_server(debug=True)