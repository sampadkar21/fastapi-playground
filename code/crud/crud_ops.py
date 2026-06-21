from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from data_model import Employee, employees as emp
from pydantic import ValidationError

app = FastAPI()


@app.get('/find_employee', response_model=Employee)
def get_emp(id: int):
    e = emp.get(id)
    if e is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return e

@app.get("/all_employees")
def get_all_emps():
    return [
        {
            "id": emp_id,
            "fname": e.fname,
            "sname": e.sname,
            "age": e.age,
            "dept": e.dept,
            "salary": e.salary,
        }
        for emp_id, e in emp.items()
    ]

@app.post('/add_employee')
def add_emp(id:int, fname:str, sname:str, age:int, dept:str, salary:int):
    if emp.get(id):
        raise HTTPException(status_code=409, detail="ID can't be overwritten")
    emp[id] = Employee(fname=fname,sname=sname,age=age,dept=dept,salary=salary)
    return JSONResponse(
        status_code=201,
        content={"Message":f"New Employee Added With ID {id}"}
    )
    
@app.put("/update_employee")
def update_emp(id: int, attr: str, new_value):
    e = emp.get(id)
    if e is None:
        raise HTTPException(status_code=404, detail="Employee not found")

    cols = Employee.model_fields.keys()
    if attr not in cols:
        raise HTTPException(status_code=400, detail="Attribute not found")

    try:
        old_data = e.model_dump()
        old_data[attr] = new_value
        emp[id] = Employee(**old_data)
        return JSONResponse(
            status_code=200,
            content={"message": f"Employee {id} updated"}
        )

    except ValidationError as ex:
        raise HTTPException(
            status_code=422,
            detail=ex.errors()
        )
        
@app.delete("/delete_employee")
def delete_emp(id:int):
    e = emp.get(id)
    if e is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    
    emp.pop(id)
    return JSONResponse(
            status_code=200,
            content={"message": f"Employee {id} deleted"}
        )