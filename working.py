from fastapi import FastAPI, Path
from pydantic import BaseModel
from typing import Optional
app = FastAPI()


students = {
    1:{
        "name":"john",
        "age" : 17,
    }
}

class Student(BaseModel):
    name:str
    age:int


class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age : Optional[int] =None




@app.get("/students",tags=['students'])
async def student():
   return students
     
#pass dynamic data in route
@app.get("/get-students/{student_id}",status_code=200,tags=['students'])
def get_students(student_id:int=Path(None,description='The id of the studnet you want to view',gt=0)):
    return students[student_id]


@app.get("/get-by-name",tags=['students'])
def get_student(*,name:str=None):
    for student_id in students:
        if students[student_id]['name'] == name:
             return students[student_id]


@app.post("/create-student/{student_id}",status_code=201,tags=['students'])
def create_student(student_id: int, student: Student):
    if student_id in students:
        return{"Error":"Student exist"}

    students[student_id]=student   
    return students[student_id]


@app.put("/update-student/{student_id}",status_code=202,tags=['students'])
def update_student(student_id: int, student:UpdateStudent):
    if student_id not in  students:
        return{"Error":"Student does not  exist"}


    students[student_id]=student   
    return students[student_id]


@app.delete("/delete-student/{student_id}",status_code=204,tags=['students'])
def delete_student(student_id: int):
    if student_id not in  students:
        return{"Error":"Student does not  exist"}

    

    del students[student_id]
    return{"Message":"Student deleted successfully"}


@app.get("/blog/{id}",tags=['blogs'])
def blog(id:int):
    return {'data':id}


    


