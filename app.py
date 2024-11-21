# This file contains the app

# Utilities
from utils.third_party import Dash, dash, dbc, html, Output, Input, State
from utils.local_imports import layout


# Define application
app = Dash(
   __name__,
   external_stylesheets=[dbc.themes.DARKLY],
   use_pages=False,
   suppress_callback_exceptions=True,
)

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

search_bar = dbc.Row(
   [
      dbc.Col(dbc.Input(type="search", placeholder="Search")),
      dbc.Col(
         dbc.Button(
            "Search",
            color="primary",
            className="ms-2",
            n_clicks=0,
         ),
         width="auto",
      ),
   ],
   className="g-0 ms-auto flex-nowrap mt-3 mt-md-0",
   align="center",
)

navbar = dbc.Navbar(
   dbc.Container([
      dbc.Row([
         dbc.Col(
            html.A(
               html.Img(
                  src=PLOTLY_LOGO,
                  height="30px",
               ),
               href="https://dash.plotly.com/",
               target='_blank',
               style={"textDecoration": "none"},
            ),
         ),

         dbc.NavbarToggler(
            id="navbar-toggler",
            n_clicks=0,
            style={'border-width':'0px', 'width':'50px'},
         ),
      ], justify='center', align='center'),
   ]),
   color="dark",
   dark=True
)

app.layout = html.Div([
   navbar,  # Add navigation bar as app header
   layout.layout()
])

# Callback for toggling the collapse on small screens or when zooming in.
@app.callback(
   [Output("navbar-collapse", "is_open")],
   [Input("navbar-toggler", "n_clicks")],
   [State("navbar-collapse", "is_open")],
   prevent_initial_call=True,
)
def toggle_navbar_collapse(n, is_open):
   if n:
      return [not is_open]
   return [is_open]
   

# Run the app
if __name__ == '__main__':
   app.run(use_reloader=True, debug=True)

   