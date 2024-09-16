from fastapi import FastAPI
from data_model import NewStudent, UpdateStudents

app = FastAPI(
    title="CRUD Operation",
    description="API for CRUD Operations"
)

Students = {
    1: {
        "name": "amitesh",
        "age": 21
    }
}

# 
@app.get("/")
def index():
    return "Welcome to the API: CRUD Operations"

@app.get("/students")
def get_students():
    return Students

@app.get("/students/{stu_id}")
def get_student_info(stu_id: int):
    if stu_id not in Students:
        return f"No student found with student id = {stu_id}"
    return Students[stu_id]

@app.post("/add_students")
def add_student(stu: NewStudent):
    if not Students:
        new_id = 1
    else:
        new_id = max(Students.keys()) + 1
    Students[new_id] = stu.model_dump()
    return Students[new_id]


@app.put("/update-student/{stu_id}")
def update_student(stu_id:int, stu: UpdateStudents):
    if stu_id not in Students:
        return f"No student found with student id = {stu_id}"
    if stu.name is not None:
        Students[stu_id]["name"] = stu.name
    if stu.age is not None:
        Students[stu_id]["age"] = stu.age
    return Students[stu_id]

@app.delete("/delete-student/{stu_id}")
def delete_student(stu_id: int):
    if stu_id not in Students:
        return f"No student found with student id = {stu_id}"
    del Students[stu_id]
    return Students