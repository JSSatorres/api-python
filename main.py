from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def root():
    return {"name": "hola fast api"}

@app.get("/url")
async def root():
    return {"url": "http/miDick"}

@app.get("/")
async def root():
    return {"url": "http/miDick"}