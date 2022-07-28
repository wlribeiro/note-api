from sqlalchemy.orm import Session

from src import models, schemas
from src.db import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        return db
    finally:
        db.close()


async def get_note(id:int):
    db: Session = get_db()
    return db.query(models.Notes).get(id)

async def delete_note(id: int):
    db: Session = get_db()
    response = db.query(models.Notes).filter(models.Notes.id == id).delete()
    db.commit()
    return response

async def get_all_notes():
    db: Session = get_db()
    return db.query(models.Notes).all()


async def create_note(note: schemas.NotesCreate):
    db: Session = get_db()
    db_note =  models.Notes(**note)
    db.add(db_note)
    db.commit()
    db.refresh(db_note)
    return db_note
