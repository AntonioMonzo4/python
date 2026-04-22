from fastapi import Depends, HTTPException, status, APIRouter
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta, timezone

# =========================================================
# CONFIGURACIÓN GENERAL DE SEGURIDAD
# =========================================================

# Algoritmo usado para firmar el token JWT
ALGORITHM = "HS256"

# Duración del token de acceso en minutos
ACCESS_TOKEN_DURATION = 1

# Clave secreta usada para firmar y validar los tokens JWT
# En producción debe almacenarse en variables de entorno
SECRET = "v4gh32fv4345v345hg34f5hjgf345jgc34j5gfv34fj5fv34j5fv3j4fc5h353b"

# Router para agrupar las rutas de autenticación
router = APIRouter()

# Esquema OAuth2 de tipo Bearer.
# tokenUrl indica la ruta donde se obtiene el token.
oauth2 = OAuth2PasswordBearer(tokenUrl="login")

# Contexto criptográfico para trabajar con hashes de contraseñas usando bcrypt
crypt = CryptContext(schemes=["bcrypt"])


# =========================================================
# MODELOS DE DATOS
# =========================================================

class User(BaseModel):
    """
    Modelo base de usuario.
    Representa la información pública o funcional del usuario.
    """
    username: str
    full_name: str
    email: str
    disabled: bool


class UserDB(User):
    """
    Modelo de usuario en base de datos.
    Hereda de User y añade la contraseña hasheada.
    """
    password: str


# =========================================================
# BASE DE DATOS SIMULADA
# =========================================================

users_db = {
    "antoniodev": {
        "username": "antoniodev",
        "full_name": "Antonio Developer",
        "email": "antonio.dev@example.com",
        "disabled": False,
        "password": "$2a$12$WuZqGEBOVfh03j8KWbudO.TJRLTttIYB8XRG4FIa6edd8JiRNFpEu"
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
    """
    Busca un usuario en la base de datos simulada a partir de su username.

    Parámetros:
        username (str): nombre de usuario a buscar.

    Retorna:
        UserDB | None: devuelve un objeto UserDB si el usuario existe;
        en caso contrario, devuelve None.
    """
    if username in users_db:
        return UserDB(**users_db[username])


# =========================================================
# RUTA DE LOGIN
# =========================================================

@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    """
    Autentica al usuario a partir de username y password.

    Flujo:
    1. Comprueba si el usuario existe.
    2. Verifica la contraseña contra el hash almacenado.
    3. Genera un token JWT con expiración.
    4. Devuelve el token al cliente.
    """

    # Buscar usuario en la base de datos simulada
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username not found"
        )

    # Convertir el diccionario del usuario a objeto UserDB
    user = search_user_db(form.username)

    # Verificar la contraseña en texto plano contra el hash almacenado
    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect Password"
        )

    # Definir la expiración del token
    access_token_expiration = timedelta(minutes=ACCESS_TOKEN_DURATION)
    expire = datetime.now(timezone.utc) + access_token_expiration

    # Payload del JWT
    access_token = {
        "sub": user.username,   # subject: identificador del usuario
        "exp": expire           # fecha y hora de expiración
    }

    # Generar el token y devolverlo al cliente
    return {
        "access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM),
        "token_type": "bearer"
    }


# =========================================================
# DEPENDENCIA: VALIDACIÓN DEL TOKEN Y RECUPERACIÓN DEL USUARIO
# =========================================================

async def auth_user(token: str = Depends(oauth2)):
    """
    Valida el token JWT recibido en la cabecera Authorization
    y recupera el usuario asociado.

    Parámetros:
        token (str): token Bearer extraído automáticamente por OAuth2PasswordBearer.

    Retorna:
        UserDB: usuario autenticado.

    Lanza:
        HTTPException 401 si el token es inválido, ha expirado
        o no contiene información válida del usuario.
    """

    exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid authentication credentials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        # Decodificar el token y extraer el username desde el claim "sub"
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")

        # Si el token no contiene un subject válido, se considera inválido
        if username is None:
            raise exception

        # Buscar el usuario asociado al token
        user = search_user_db(username)

        # Si el usuario ya no existe, lanzar excepción
        if user is None:
            raise exception

    except JWTError:
        # Cualquier error relacionado con JWT termina en 401 Unauthorized
        raise exception

    return user


# =========================================================
# DEPENDENCIA: COMPROBAR QUE EL USUARIO ESTÁ ACTIVO
# =========================================================

async def current_user(user: User = Depends(auth_user)):
    """
    Comprueba si el usuario autenticado está activo.

    Parámetros:
        user (User): usuario devuelto por la dependencia auth_user.

    Retorna:
        User: usuario autenticado y activo.

    Lanza:
        HTTPException si el usuario está deshabilitado.
    """

    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Inactive user"
        )

    return user


# =========================================================
# RUTA PROTEGIDA
# =========================================================

@router.get("/users/me", response_model=User)
async def me(user: User = Depends(current_user)):
    """
    Devuelve la información del usuario autenticado actualmente.

    Esta ruta solo puede ejecutarse si:
    1. El token es válido.
    2. El usuario existe.
    3. El usuario está activo.
    """
    return user