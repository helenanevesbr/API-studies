import pathlib
import connexion
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

basedir = pathlib.Path(__file__).parent.resolve()
#points to the directory that the program is running in
connex_app = connexion.App(__name__, specification_dir=basedir)
#creates the Connexion app instance and give it the path
# to that directory
app = connex_app.app
# this is the Flask instance initialized by Connexion

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{basedir / 'people.db'}"
# tell SQLAlchemy to use SQLite as the database and a file named
# people.db in the current directory as the database file

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# Since I'm not creating an event-driven program,
# I can turn this feature off.

db = SQLAlchemy(app)
# initializes SQLAlchemy by passing the app configuration
# information to SQLAlchemy
ma = Marshmallow(app)
# initializes Marshmallow and allows it to work with the
# SQLAlchemy components attached to the app