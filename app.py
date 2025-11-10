from fastapi import FastAPI

app = FastAPI()
@app.get("/")
def home():
    return {"message": "Hello from FastAPI!"}

@app.get("/info")
def info():
    return {"version": "1.0", "status": "running"}

@app.get("/hello")
def hello(name: str = "friend"):
    return {"greeting": f"Hello, {name}!"}

@app.get("/hello/age")
def hello_age(age: int):
    return {"message": f"Your age is {age}"}
