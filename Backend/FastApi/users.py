from fastapi import FastAPI 
from pydatic import BaseModel #BaseModel es una clase que nos permite crear modelos de datos para validar la información que recibimos en las peticiones

app = FastAPI()

# Inicio del servidor uvicorn users:app --reload
# http://127.0.0.1:8000/users

#Entidad User
class User(BaseModel):
    name: str
    age: int
    username: str 

users_list = [User(name="Antonio",age=26,username="antonio_dev"),
            User(name="Tesla",age=100,username="tesla_dev"),
            User(name="Einstein",age=150,username="einstein_dev")
         ]#Para que no exista duda de como se crean los objetos 



@app.get("/usersjson")
async def users_json():
    return [{"name":"Antonio","age":26,"username":"antonio_dev"},
            {"name":"Tesla","age":100,"username":"tesla_dev"},
            {"name":"Einstein","age":150,"username":"einstein_dev"}
            ]

@app.get("/users")
async def users():
    return users_list