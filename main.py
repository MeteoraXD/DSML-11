from fastapi import FastAPI
from DailyDSML.Day21.calculator import Calculator

app = FastAPI()


@app.get("/")
def read_root():
    return {"My": "Calculator"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: str | None = None):
#     return {"item_id": item_id, "q": q}


@app.get("/calculator")
def Calc(num1: float, num2: float, optr: str ):
    calculator = Calculator(num1,num2,optr)
    result = calculator.calc()
    return{'result': result}

