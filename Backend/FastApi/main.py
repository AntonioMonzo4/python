#Previamente se ha instalado FastApi con el comando pip install "fastapi[all]"
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return "Hello FastAPI"

#Levantamos el servidor con el comando uvicorn main:app --reload