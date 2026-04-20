from fastapi import FastAPI 
from pydatic import BaseModel #BaseModel es una clase que nos permite crear modelos de datos para validar la información que recibimos en las peticiones

app = FastAPI()

# Inicio del servidor uvicorn users:app --reload
# http://127.0.0.1:8000/users

#Entidad User
class User(BaseModel):
    id: int
    name: str
    age: int
    username: str 

users_list = [User(id :42, name="Antonio",age=26,username="antonio_dev"),
            User(id:27, name="Tesla",age=100,username="tesla_dev"),
            User(id:48,name="Einstein",age=150,username="einstein_dev")]#Para que no exista duda de como se crean los objetos 



@app.get("/usersjson")
async def users_json():
    return [{"name":"Antonio","age":26,"username":"antonio_dev"},
            {"name":"Tesla","age":100,"username":"tesla_dev"},
            {"name":"Einstein","age":150,"username":"einstein_dev"}
            ]
#Este se hace mediante el path 
@app.get("/user/{id}")
async def users(id: int ):
    users = filter(lambda user: user.id == id, users_list)
    try: 
        return list(users)[0]
    except: 
        return {"error": "User not found"}

#Este se hace mediante la query
@app.get("/userquery/")
async def users(id: int ):
   return search_user(id)

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try: 
        return list(users)[0]
    except: 
        return {"error": "User not found"}

@app.get("/users/")
async def user():
    return users_list