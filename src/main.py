from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

async def say_hello(name:str=None):
    if name is not None:
        return {"message": f"Hello {name}"}
    return {"message": "Hello World!"}

@app.get("/")
async def root():
    return await say_hello()

@app.get("/{name}")
async def hello(name:str=None):
    return await say_hello(name=name)

@app.get("/healtcheck")
async def healtcheck():
    return {"message": datetime.now()}