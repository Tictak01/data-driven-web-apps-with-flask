import flask

app = flask.Flask('omega')

@app.route('/')
def index():
    return "Hello World"

app.run()