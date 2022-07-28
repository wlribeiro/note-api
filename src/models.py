from sqlalchemy import Column, Integer, String, Text

from src.db import Base


class Notes(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    text = Column(Text)
    color = Column(String(10))
