from datetime import datetime
from config import db, ma

'''
REST API works with JSON data. Because SQLAlchemy returns data as Python class instances, Connexion can’t serialize these class instances to JSON-formatted data.
In this context, serializing means converting Python objects into simpler data structures that can be parsed into JSON data types.
As an example, your Person class contains a timestamp, which is a Python DateTime class. There’s no DateTime definition in JSON, so the timestamp has to be converted to a string in order to exist in a JSON structure.
'''

class Person(db.Model):
    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), unique=True)
    fname = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True # to deserialize JSON data and load Person model instances from it
        sqla_session = db.session
'''
For PersonSchema, the SQLAlchemy model is Person, and the SQLALchemy session is db.session.
This is how Marshmallow finds attributes in the Person class and learns the types of those attributes so it knows how to serialize and deserialize them.
'''

person_schema = PersonSchema()
people_schema = PersonSchema(many=True)

'''
JSON data types are listed below:
- string
- number
- object: A JSON object, which is equivalent to a Python dictionary
- array: Roughly equivalent to a Python List
- boolean: Represented in JSON as true or false, but in Python as True or False
- null: Essentially None in Python
'''