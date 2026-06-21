from fastapi import FastAPI
from pydantic import BaseModel, computed_field

app = FastAPI()

class Details(BaseModel):
    name: str
    age: int
    country: str
    
    @computed_field
    @property
    def eligible(self) -> bool:
        if self.age>=18 and self.country=="India":
            return True
        else:
            return False
    
    
@app.get("/voter",response_model=Details)
def voter_validation(name:str, age:int, country:str):
    details = Details(name=name, age=age, country=country)
    return details
