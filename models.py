from datetime import datetime
from config import db, ma


class Note(db.Model):
    __tablename__ = "note"
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"))
    '''
    person_id is known as a foreign key. The foreign key gives each entry in the note table the primary key of the person record that it’s associated with.
    This and the Person.notes attribute are how SQLAlchemy knows what to do when interacting with Person and Note objects
    '''
    content = db.Column(
        db.String, # contains the actual text of the note
        nullable=False # new notes must contain content
    )
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
    "Note", # The "Note" SQLAlchemy class isn’t defined yet
    backref="person", # Each instance of Note will contain an attribute called .person. The .person attribute references the parent object that a particular Note instance is associated with.
    cascade="all, delete, delete-orphan", # how to treat Note instances when changes are made to the parent Person instance.
    # For example, when a Person object is deleted, SQLAlchemy will create the SQL necessary to delete the Person object from the database.
    # This parameter tells SQLAlchemy to also delete all the Note instances associated with it.
    single_parent=True, # tells SQLAlchemy not to allow an orphaned Note instance —that is, a Note without a parent Person object— to exist
    order_by="desc(Note.timestamp)"
)

class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True
        sqla_session = db.session


person_schema = PersonSchema()
people_schema = PersonSchema(many=True)