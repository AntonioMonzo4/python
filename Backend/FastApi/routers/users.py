from fastapi import FastAPI , HTTPException
from pydantic import BaseModel #BaseModel es una clase que nos permite crear modelos de datos para validar la información que recibimos en las peticiones

app = FastAPI()

# Inicio del servidor uvicorn users:app --reload
# http://127.0.0.1:8000/users

#Entidad User
class User(BaseModel):
    id: int
    name: str
    age: int
    username: str 

users_list = [User(id =42, name="Antonio",age=26,username="antonio_dev"),
            User(id=27, name="Tesla",age=100,username="tesla_dev"),
            User(id=48,name="Einstein",age=150,username="einstein_dev")]#Para que no exista duda de como se crean los objetos 



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

@app.post("/user/",status_code=201)
async def user(user: User):
    if type(search_user(user.id) )== User:
        raise HTTPException(status_code=400, detail="User already exits")
        
    else:
        users_list.append(user)

#El put se hace para actualizar un usuario, el delete se hace para eliminar un usuario
#Patch se hace para actualizar parcialmente un usuario, es decir, solo algunos campos del usuario, 
# mientras que el put se hace para actualizar completamente un usuario, es decir, todos los campos del usuario.
@app.put("/user/")
async def user(user:User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True
            break
    if not found:
        return {"error": "User not found"}
    return {"message": "User updated"}

#Si envias datos en el body pero no se definen  en la función FastApi no lo va a tomar en cuenta, 
# por eso es importante definir los parámetros que se van a recibir en la función, 
# para que FastApi pueda validar la información y evitar errores.

@app.delete("/user/{id}")
async def user(id: int):
    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == id:
            del users_list[index]
            found = True
            break
    if not found:
        return {"error": "User not found"}
    return {"message": "User deleted"}
    