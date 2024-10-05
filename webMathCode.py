"""
A small microservice that provides a web interface to the mathCode.py module.
Uses FastAPI and Uvicorn
"""

from fastapi import FastAPI  # type: ignore
from funcLog.mathCode import add, subtract, multiply, divide

app = FastAPI()


# Build out routes for each imported function
@app.get("/add/{a}/{b}")
def add_route(a: int, b: int):
    return add(a, b)


@app.get("/subtract/{a}/{b}")
def subtract_route(a: int, b: int):
    return subtract(a, b)


@app.get("/subtract/{a}/{b}")
def multiply_route(a: int, b: int):
    return multiply(a, b)


@app.get("/subtract/{a}/{b}")
def divide_route(a: int, b: int):
    return divide(a, b)


# Run the app
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
