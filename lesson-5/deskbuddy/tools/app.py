from fastapi import FastAPI
from pydantic import BaseModel
import datatime

app = FastAPI(title="Deskbuddy Tools")

class Calc(BaseModel):
    expression: str

@app.post("/calculator")
def calculator(c: Calc):
    try:
        return {"result": eval(c.expression, {"__builtins__": {}})}
    except Exception as e:
        return {"error" : str(e)}


@app.get("/datatime")
def now():
    return {"now": datatime.datatime.now().isoformat()}
