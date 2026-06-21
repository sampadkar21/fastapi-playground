from pydantic import BaseModel, Field, StrictInt
from typing import Optional

class Employee(BaseModel):
    fname: str = Field(...,min_length=3,max_length=30,description="First Name",pattern=r'[A-Za-z]')
    sname: Optional[str] = Field(min_length=3,max_length=30,default=None,description="Last Name",pattern=r'[A-Za-z]')
    age: StrictInt = Field(...,ge=18,le=60,description="Age")
    dept: str = Field(...,examples=["AI","DevOps"])
    salary: StrictInt = Field(...,gt=999,description="Salary")

employees = {
    1: Employee(fname="Sam", sname="Roy", age=22, dept="Data Science", salary=65000),
    2: Employee(fname="Priya", sname="Sharma", age=28, dept="HR", salary=55000),
    3: Employee(fname="Rahul", sname="Verma", age=31, dept="Backend", salary=85000),
    4: Employee(fname="Ananya", sname="Sen", age=26, dept="Frontend", salary=72000),
    5: Employee(fname="Arjun", sname="Das", age=35, dept="DevOps", salary=95000),
}
