from fastapi import FastAPI
from pydinamic import BaseModel


app = FastAPI()

@app.get("/api/users")
async def userss():
    return {"users": "hola fast users"}
