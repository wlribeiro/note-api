from fastapi import FastAPI, Response, status
from fastapi.middleware.cors import CORSMiddleware

from src import schemas, repository


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"https?:\/\/.*$",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", status_code=status.HTTP_200_OK)
async def hello_world():
    return {"message": "hello world"}


@app.get("/notes", status_code=status.HTTP_200_OK)
async def list_notes():
    notes = await repository.get_all_notes()
    return notes


@app.post("/notes", status_code=status.HTTP_201_CREATED)
async def create_note(note: schemas.NotesCreate):
    note_dict = note.dict()
    result = await repository.create_note(note_dict)
    return result


@app.get("/notes/{note_id}", status_code=status.HTTP_200_OK)
async def update_note(note_id: int):
    note = await repository.get_note(note_id)
    return note

# TO-DO - add methods to update and add fields created_at and updated_at at columns
@app.put("/notes/{note_id}", status_code=status.HTTP_200_OK)
async def update_note(note_id: int):
    return "updated"


@app.delete("/notes/{note_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_note(note_id: int):
    result = await repository.delete_note(note_id)
    if not result:
        return Response(status_code=status.HTTP_404_NOT_FOUND)
    
    return Response(status_code=status.HTTP_204_NO_CONTENT)
