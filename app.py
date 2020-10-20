import dash
app = dash.Dash()
server = app.server
app.config.supress_callback_exceptions = True
server.secret_key = os.environ.get('secret_key', 'secret')
