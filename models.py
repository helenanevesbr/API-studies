from datetime import datetime
from marshmallow_sqlalchemy import fields
from config import db, ma


class Note(db.Model):
    __tablename__ = "note"
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"))
    content = db.Column(db.String, nullable=False)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

class NoteSchema(ma.SQLAlchemyAutoSchema):
    # you must place NoteSchema underneath your Note class definition to prevent errors...
    class Meta:
        model = Note # because you’re referencing Note from within NoteSchema
        load_instance = True
        sqla_session = db.session
        include_fk = True # your Note model contains a foreign key

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
    notes = fields.Nested(NoteSchema, many=True) # referencing the Note object by its NoteSchema
    '''
    After importing fields from marshmallow_sqlalchemy, you have to explicitly create the notes field in PersonSchema.
    Otherwise Marshmallow doesn’t receive all the information it needs.
    For example, it won’t know that you’re expecting a list of objects using the many argument.
    '''

person_schema = PersonSchema()
people_schema = PersonSchema(many=True)