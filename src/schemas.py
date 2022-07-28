from typing import Optional
from pydantic import BaseModel


class Notes(BaseModel):
    text: str
    color: Optional[str] = None
    title: Optional[str] = None


class NotesCreate(Notes):
    pass
