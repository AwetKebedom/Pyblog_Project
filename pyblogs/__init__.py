import flask
import flask_sqlalchemy
import os
import flask_migrate

app = flask.Flask(__name__)
app.config['SECRET_KEY'] = 'my-secret-key'

# create a database object

app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///'+os.path.join(os.path.dirname(__file__),'pyblogs.db')

db = flask_sqlalchemy.SQLAlchemy(app)



from pyblogs import routes
