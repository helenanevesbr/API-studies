from datetime import datetime
from config import db, ma

'''
To show the notes for each person in the front end, add attribute include_relationships to PersonSchema and create a NotesSchema.
include_relationships by itself will make your API response only list the primary keys of each person’s notes.
That’s fair, because you haven’t yet declared how Marshmallow should deserialize the notes.
'''

class Note(db.Model):
    __tablename__ = "note"
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"))
    content = db.Column(db.String, nullable=False)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

class Person(db.Model):
    __tablename__ = "person"

    id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), unique=True)
    fname = db.Column(db.String(32))
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

    notes = db.relationship(
    "Note",
    backref="person",
    cascade="all, delete, delete-orphan",
    single_parent=True,
    order_by="desc(Note.timestamp)"
)

class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True
        sqla_session = db.session
        include_relationships = True
        '''
        By default, a Marshmallow schema doesn’t traverse into related database objects. You have to explicitly tell a schema to include relationships.
        With include_relationships in the Meta class of PersonSchema, you tell Marshmallow to add any related objects to the person schema
        '''


person_schema = PersonSchema()
people_schema = PersonSchema(many=True)