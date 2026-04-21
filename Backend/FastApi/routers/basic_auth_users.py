from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

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
        return UserDB(users_db[username])