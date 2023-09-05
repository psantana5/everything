from flask import Flask, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import dash
from dash import Dash, dcc, html, Input, Output, State, no_update
from dash.exceptions import PreventUpdate
from dash import ALL
import dash_bootstrap_components as dbc
import yfinance as yf
import plotly.graph_objects as go
from dash import no_update


# Initialize Flask and Dash apps with Bootstrap
server = Flask(__name__)
app = Dash(__name__, server=server, external_stylesheets=[dbc.themes.DARKLY], url_base_pathname='/dashboard/')
app.server.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.server.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.server.config['SECRET_KEY'] = 'SJOHWNLRIHK4NWEUIKJSNFUIELJKB EI'

db = SQLAlchemy(server)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

# Initialize the database and create tables
with server.app_context():
    db.create_all()

login_manager = LoginManager()
login_manager.init_app(server)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@server.route('/dashboard/')
@login_required
def render_dashboard():
    return redirect('/dashboard/')

available_stocks = ['AAPL', 'GOOGL', 'TSLA', 'AMZN', 'MSFT', 'BTC-USD']

profile_modal = dbc.Modal(
    [
        dbc.ModalHeader("Profile"),
        dbc.ModalBody(
            [
                html.Div("Login Form"),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Username"),
                        dbc.Input(id="login-username", type="text")
                    ],
                    className="mb-3"
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Password"),
                        dbc.Input(id="login-password", type="password")
                    ],
                    className="mb-3"
                ),
                dbc.Button("Login", id="login-button"),
                html.Div(id="login-output", className="mb-3"),
                html.Hr(),
                html.Div("Register Form"),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Username"),
                        dbc.Input(id="register-username", type="text")
                    ],
                    className="mb-3"
                ),
                dbc.InputGroup(
                    [
                        dbc.InputGroupText("Password"),
                        dbc.Input(id="register-password", type="password")
                    ],
                    className="mb-3"
                ),
                dbc.Button("Register", id="register-button"),
                html.Div(id="register-output")
            ]
        )
    ],
    id="profile-modal"
)

app.layout = dbc.Container([
    dbc.Row([
        dcc.Location(id='url', refresh=False),
        dbc.Col(html.H1("Real-time Stock Price Dashboard"), width=8),
        dbc.Col(dbc.Button(html.Img(src="/assets/profile_icon.png", height="30px"), id="open-modal", className="ml-auto"))
    ], className="mb-4"),
    profile_modal,

    html.Div(id='featured-stocks', className='mb-4'),
    html.Div(id='stock-alert', className='mb-4'),

    dcc.Interval(
        id='interval-update',
        interval=60 * 1000,
        n_intervals=0
    ),

    dbc.Row([
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardBody(
                        dcc.Dropdown(
                            id='stock-dropdown',
                            options=[{'label': stock, 'value': stock} for stock in available_stocks],
                            value='AAPL'
                        ),
                    ),
                ],
                style={"borderRadius": "20px", "backgroundColor": "#333", "color": "#fff"},
            ),
            width={"size": 4, "offset": 4},
        ),
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(dcc.Graph(id='live-graph'), width=12)
    ]),

], fluid=True)

@app.callback(
    Output("profile-modal", "is_open"),
    [Input("open-modal", "n_clicks"), Input("profile-modal", "is_open")],
    [State("profile-modal", "is_open")],
)
def toggle_modal(n1, n2, is_open):
    if n1 or n2:
        return not is_open
    return is_open

@app.callback(
    [Output('register-output', 'children'),
     Output('login-output', 'children'),
     Output('url', 'pathname')],
    [Input('register-button', 'n_clicks'),
     Input('login-button', 'n_clicks')],
    [State('register-username', 'value'),
     State('register-password', 'value'),
     State('login-username', 'value'),
     State('login-password', 'value')],
)
def manage_users(register_clicks, login_clicks, reg_username, reg_password, login_username, login_password):
    ctx = dash.callback_context
    if not ctx.triggered:
        raise PreventUpdate

    trigger_id = ctx.triggered[0]['prop_id'].split('.')[0]

    if trigger_id == 'register-button':
        if register_clicks is None:
            return no_update, no_update, no_update
        hashed_password = generate_password_hash(reg_password, method='sha256')
        new_user = User(username=reg_username, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        return 'User registered', no_update, '/dashboard/'

    elif trigger_id == 'login-button':
        if login_clicks is None:
            return no_update, no_update, no_update
        user = User.query.filter_by(username=login_username).first()
        if user and check_password_hash(user.password, login_password):
            login_user(user)
            return no_update, 'Logged in', '/dashboard/'
        
        return no_update, 'Invalid credentials', no_update
    
@app.callback(
    [Output('live-graph', 'figure'),
     Output('stock-alert', 'children')],
    [Input('interval-update', 'n_intervals'),
     Input('stock-dropdown', 'value')]
)
def update_graph_and_alert(n, selected_stock):
    data = yf.download(selected_stock, period='1d', interval='1m')
    fig = go.Figure()
    fig.add_trace(
        go.Scatter(x=data.index, y=data['Close'], mode='lines', name='Close Price')
    )
    return fig, None  

if __name__ == '__main__':
    app.run_server(debug=True)