
import flask

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'my-secret-key'
from pyblogs import routes
