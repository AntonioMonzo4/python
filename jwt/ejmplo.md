1. El usuario inicia sesión

El cliente envía:

POST /login

{
    "username": "antonio",
    "password": "123456"
}

El servidor comprueba las credenciales.

usuario = buscar_usuario("antonio")

if usuario.password == "123456":
    # Login correcto


2. El servidor genera el JWT

Con la librería PyJWT:

pip install pyjwt
import jwt
import datetime

SECRET_KEY = "mi_clave_super_secreta"

payload = {
    "user_id": 15,
    "username": "antonio",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
}

token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")

print(token)

Salida (parecida):

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ...

Ese token se envía al cliente.

{
    "access_token": "eyJhbGc..."
}


3. El cliente guarda el token

Por ejemplo, una aplicación React podría guardarlo en memoria o en una cookie HttpOnly.

A partir de ahora, todas las peticiones incluirán:

Authorization: Bearer eyJhbGc...
4. El servidor recibe una petición

Supongamos que el usuario quiere ver sus notas.

GET /notes

El cliente envía:

GET /notes

Authorization: Bearer eyJhbGc...
5. El servidor verifica el JWT
import jwt

SECRET_KEY = "mi_clave_super_secreta"

token = "eyJhbGc..."

try:
    payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

    print(payload)

except jwt.ExpiredSignatureError:
    print("El token ha expirado")

except jwt.InvalidTokenError:
    print("Token inválido")

Resultado:

{
    "user_id": 15,
    "username": "antonio",
    "exp": 1785330000
}

El servidor ya sabe quién eres sin volver a pedir usuario y contraseña.

¿Por qué funciona?

La clave está en la firma.

Cuando haces:

jwt.encode(payload, SECRET_KEY, algorithm="HS256")

se genera una firma usando tu SECRET_KEY.

Cuando llega otra petición:

jwt.decode(token, SECRET_KEY, algorithms=["HS256"])

Python vuelve a calcular esa firma.

Si coincide → el token es auténtico.
Si no coincide → alguien lo ha modificado.

Por ejemplo, si un atacante cambia el contenido del token de:

{
    "user_id": 15,
    "role": "user"
}

a

{
    "user_id": 15,
    "role": "admin"
}

la firma dejará de ser válida y jwt.decode() lanzará una excepción.

Así es el flujo completo
              LOGIN
+---------+                     +------------+
| Cliente | -- usuario/pass --> | Servidor   |
+---------+                     +------------+
                                      │
                                      │ Comprueba la contraseña
                                      ▼
                              Genera JWT firmado
                                      │
                                      ▼
                      eyJhbGciOiJIUzI1NiIs...
                                      │
                                      ▼
+---------+                     +------------+
| Cliente | <-- Guarda JWT -----| Servidor   |
+---------+                     +------------+

      Más tarde...

+---------+
| Cliente |
+---------+
      │
      │ Authorization: Bearer eyJhbGc...
      ▼
+------------+
| Servidor   |
+------------+
      │
      │ Verifica la firma
      ▼
 Token válido
      │
      ▼
 Devuelve los datos
En FastAPI (como se hace en proyectos reales)

La mayoría de proyectos con FastAPI usan este flujo:

El usuario hace POST /login.
FastAPI verifica las credenciales.
Se genera un Access Token (JWT).
El frontend lo envía en cada petición con Authorization: Bearer <token>.
Un middleware o dependencia de FastAPI valida el token antes de ejecutar el endpoint.
El endpoint ya conoce al usuario autenticado y puede acceder a user.id, user.email, user.role, etc.

Este es exactamente el patrón que encontrarás en la mayoría de APIs profesionales construidas con FastAPI, Django REST Framework, Flask, Express o Spring Boot.