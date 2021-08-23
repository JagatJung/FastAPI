from fastapi import FastAPI,Path
from typing import Optional
from pydantic import BaseModel

app=FastAPI()

students={
    1:{
        "name":"Jagat",
        "roll":4,
        "Address":"Hetauda"
    },
    2:{
        "name":"aman",
        "roll":6,
        "Address":"damawli"
    }
}

class newStudent(BaseModel):
    name: Optional[str] = None
    roll:Optional[int] = None
    Address: Optional[str] = None

@app.get('/')
def myapp():
    return {"name":"Jagat"}

@app.get('/stdData/{student_id}')
def retstd(student_id:int=Path(None,description=("Enter the value"),gt=0,lt=5)):
    return students[student_id]

@app.get("/get-std-name/{student_id}")
def stdname(*, student_id:int, name: Optional[str]=None, test:int):
    for student_id in students:
        if(students[student_id]['name']==name):
            return students[student_id]
    return {"Data": "course not found"}

@app.post("/makestudent/{student_id}")
def stdcreate(student_id:int, myStudent:newStudent):
    if(student_id in students):
        return {"Error":"student already exist"}
        
    students[student_id]=myStudent
    return students[student_id]

@app.put("/updateStd/{student_id}")
def updateStudent(student_id:int, myStudent:newStudent):
    if(student_id not in students):
        return{"Error":"Something wrong"}
    if myStudent.name!= None:
        students[student_id]["name"]=myStudent.name

    if myStudent.roll!= None:
        students[student_id]["roll"]=myStudent.roll

    if myStudent.Address!= None:
        students[student_id]['Address']=myStudent.Address
    
    return students[student_id]


@app.delete("/delstd/{student_id}")
def delstd(student_id:int):
    if student_id not in students:
        return {"Error":"Student is not here"}
    
    del students[student_id]
    return{"message":"Sucessful"}