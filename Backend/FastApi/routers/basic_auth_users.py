from fastapi import FastAPI, Depends, HTTPException, status 
from pydantic import BaseModel
from fastapi.security  import OAuth2PasswordBearer, OAuth2PasswordRequestForm #OAuth2PasswordBearer es una 
#clase que nos permite implementar la autenticación mediante tokens en nuestra API. OAuth2PasswordRequestForm es una c
# lase que nos permite manejar las solicitudes de autenticación mediante formularios, es decir, 
# cuando un usuario envía sus credenciales (nombre de usuario y contraseña) para obtener un token de acceso.

app= FastAPI()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

class User(BaseModel):
    username: str
    full_name: str
    email: str 
    disabled: bool

class UserDB(User):
    password: str

users_db = {
    "antoniodev": {
        "username": "antoniodev",
        "full_name": "Antonio Developer",
        "email": "antonio.dev@example.com",
        "disabled": False,
        "password": "123456"
    },
    "tesla_dev": {
        "username": "tesla_dev",
        "full_name": "Tesla Developer",
        "email": "tesla.dev@example.com",
        "disabled": True,
        "password": "654321"
    }

}

def search_user(username:str):
    if username in users_db:
        return UserDB(**users_db[username])
    
async def current_user(token: str = Depends(oauth2)):
    user = search_user(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, 
                            detail="Invalid authentication credentials", 
                            headers={"WWW-Authenticate": "Bearer"})
    
@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username not found")
    
    user = search_user(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect Password")
    return {"access_token": user.username , "token_type": "bearer"}

@app.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user