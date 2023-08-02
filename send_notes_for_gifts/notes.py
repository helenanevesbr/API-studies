from flask import abort, make_response

from config import db
from models import Note, Person, note_schema

def read_one(note_id):
    note = Note.query.get(note_id)

    if note is not None:
        return note_schema.dump(note)
    else:
        abort(
            404, f"Note with ID {note_id} not found"
        )

def update(note_id, note):
    existing_note = Note.query.get(note_id)

    if existing_note:
        update_note = note_schema.load(note, session=db.session)
        existing_note.content = update_note.content
        db.session.merge(existing_note)
        db.session.commit()
        return note_schema.dump(existing_note), 201
    else:
        abort(404, f"Note with ID {note_id} not found")

def delete(note_id):
    existing_note = Note.query.get(note_id)

    if existing_note:
        db.session.delete(existing_note)
        db.session.commit()
        return make_response(f"{note_id} successfully deleted", 204)
    else:
        abort(404, f"Note with ID {note_id} not found")

def create(note):
    person_id = note.get("person_id")
    person = Person.query.get(person_id)
    '''
    A note always needs a person to belong to.
    That’s why you need to work with the Person model when you create a new note.
    '''

    if person:
        new_note = note_schema.load(note, session=db.session)
        person.notes.append(new_note)
        # Although you’re working with the person database table in this case, SQLAlchemy will take care that the note is added to the note table.
        db.session.commit()
        return note_schema.dump(new_note), 201
    else:
        abort(
            404,
            f"Person not found for ID: {person_id}"
        )