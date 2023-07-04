from datetime import datetime
from config import db
# imports db, an instance of SQLAlchemy that you defined in
# the config.py module

class Person(db.Model):
    # Inheriting from db.Model gives Person the SQLAlchemy
    # features to connect to the database and its tables.
    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), unique=True)
    # Must be unique because you’re using lname as the identifier
    # for a person in a REST API URL
    fname = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime,
        default=datetime.utcnow, # when a record is created
        onupdate=datetime.utcnow # when the record is updated
    )