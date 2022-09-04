#!python3

import asyncio
from enum import Enum
from fastapi import FastAPI
import httpx

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World!" }

@app.get("/google")
async def google():
    async with httpx.AsyncClient() as client:
        r = await client.get('https://www.google.com', timeout=10)
    return r.text

@app.get("/call")
async def call():
    async with httpx.AsyncClient() as client:
        r = await client.get('http://localhost:8181/google', timeout=10)
    await asyncio.sleep(5)
    return r.text

@app.get("/req")
async def req():
    async with httpx.AsyncClient() as client:
        r = await client.get('http://localhost:8181/call', timeout=10)
    return r.text

@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id }

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("microservice:app", host="0.0.0.0", port=8181, workers=1)