from fastapi import FastAPI, Depends, HTTPException, status , APIRouter
from pydantic import BaseModel
from fastapi.security  import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone 

#Importaciones: 
# FastAPI: Framework para crear APIs
# Depends: Para manejar dependencias en FastAPI
# HTTPException: Para manejar excepciones HTTP
# status: Para manejar códigos de estado HTTP
# BaseModel: Para crear modelos de datos con Pydantic
# OAuth2PasswordBearer: Para implementar autenticación mediante tokens
# OAuth2PasswordRequestForm: Para manejar solicitudes de autenticación mediante formularios
# jwt: Para manejar JSON Web Tokens 
# CryptContext: Para manejar el hashing de contraseñas
# datetime, timedelta: Para manejar fechas y tiempos, especialmente para la expiración de tokens


#Dependencias que necesitamos implementar + comandos 
# pip install "fastapi[all]" 
# Levantar el servidor uvicorn basic_auth_users:app --reload
# pip install "python-jose[cryptography]"
# pip install passlib[bcrypt]
#Para obtener un secret key para la generación de tokens se puede usar el siguiente comando en la terminal: openssl rand -hex 32

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "v4gh32fv4345v345hg34f5hjgf345jgc34j5gfv34fj5fv34j5fv3j4fc5h353b"

router= APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login") #Instancia de OAuth2PasswordBearer, se le pasa la URL de login para obtener el token

crypt = CryptContext(schemes=["bcrypt"])

class User(BaseModel):# Modelo de datos para el usuario 
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
        "password": "$2a$12$WuZqGEBOVfh03j8KWbudO.TJRLTttIYB8XRG4FIa6edd8JiRNFpEu" #Contraseña encriptada con bcrypt, la contraseña original es "123456"
    },
    "tesla_dev": {
        "username": "tesla_dev",
        "full_name": "Tesla Developer",
        "email": "tesla.dev@example.com",
        "disabled": True,
        "password": "$2a$12$WuZqGEBOVfh03j8KWbudO.TJRLTttIYB8XRG4FIa6edd8JiRNFpEu"
    }

}



def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


""""
Función antesde editar 

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username not found")
    
    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect Password")
    return {"access_token": user.username , "token_type": "bearer"}
"""


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Username not found")
    user = search_user_db(form.username)


    if not crypt.verify(form.password, user.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect Password")
    
    access_token_expiration = timedelta(minutes=ACCESS_TOKEN_DURATION)
    expire = datetime.now(timezone.utc) + access_token_expiration
    access_token = {"sub":user.username,"exp":expire}
    

    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM) , "token_type": "bearer"}

async def auth_user(token: str = Depends(oauth2)):

    exception=HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )

    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None: 
            raise exception
        
        user = search_user_db(username)

    except JWTError:
         raise exception
    
    return user
    



async def current_user(user: User = Depends(auth_user)):
    
    
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Inactive user"
        )

    return user



@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
