from dash import html, dcc
import dash_bootstrap_components as dbc

def build_app_layout():
    app_layout = html.Div([
        dbc.Row([
            dbc.Col(
                html.Div("This will be a fixed row with picture"),
                width="auto"
            ),
            dbc.Col(
                html.Div("This will also be a fixed row"),
                width="auto"
            )
        ], style={
            "position":"fixed",
            "top":"0",
            "left":"0"
        }),
        dbc.Row([
            dbc.Col(
                html.Div(
                    [
                        dbc.Button(
                            "Open collapse",
                            id="collapse-button",
                            className="mb-3",
                            color="primary",
                            n_clicks=0,
                        ),
                        dbc.Collapse(
                            dbc.Card(dbc.CardBody("This content is hidden in the collapse")),
                            id="collapse",
                            is_open=False,
                        ),
                    ]
                )
            ),
            dbc.Col(
                html.Div("Second row column - app")
            )
        ], style={
            "marginTop":"100px",
            "height":"2000px"
        })
    ])
    return app_layout
