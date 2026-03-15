import flask

app = flask.Flask(__name__)

app.static_folder = 'css'

@app.route('/css.css')
def index():
    return flask.send_from_directory('', 'css.css')

@app.route('/settings.css')
def settings():
    return flask.send_from_directory('', 'settings.css')

@app.route('/parts/<path:path>')
def static_proxy(path):
    return flask.send_from_directory('parts', path)

if __name__ == '__main__':
    app.run(debug=True)