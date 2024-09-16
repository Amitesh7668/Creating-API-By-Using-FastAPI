# data_model.py
from pydantic import BaseModel

class NewStudent(BaseModel):
    name: str
    age: int

class UpdateStudents(BaseModel):
    name: str = None
    age: int = None