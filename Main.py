from fastapi import FastAPI 
from pydantic import BaseModel

app=FastAPI()

class ScoringItem(BaseModel):
    Yearsatcompany:float
    EmployeeSatisfaction:float
    position:str 
    salary:int

@app.post('\')
async def scoring_endpoint(item:ScoringItem):
    return item
