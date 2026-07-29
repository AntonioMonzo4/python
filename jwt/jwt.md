JWT (JSON Web Token) es un estándar para transmitir información de forma segura entre dos partes, principalmente para autenticación y autorización en aplicaciones web y APIs.

¿Cómo funciona?
El usuario inicia sesión con su usuario y contraseña.
El servidor verifica las credenciales.
Si son correctas, genera un JWT y se lo devuelve al cliente.
El cliente (navegador o aplicación móvil) guarda ese token.
En cada petición posterior, el cliente envía el JWT en el encabezado HTTP:
Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...
El servidor verifica la firma del token y, si es válido, permite acceder al recurso solicitado.
Estructura de un JWT

Un JWT tiene tres partes separadas por puntos (.):

xxxxx.yyyyy.zzzzz
Header (Cabecera): indica el algoritmo de firma y el tipo de token.
Payload (Carga útil): contiene la información (por ejemplo, el ID del usuario, rol y fecha de expiración).
Signature (Firma): garantiza que el token no ha sido modificado.

Ejemplo:

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
.
eyJ1c2VySWQiOjEyMywicm9sIjoiYWRtaW4ifQ
.
SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c
Ventajas
No requiere almacenar sesiones en el servidor (es stateless).
Es fácil de usar entre distintos servicios y microservicios.
Es compatible con aplicaciones web, móviles y APIs.
Desventajas
Si alguien roba un JWT válido, puede usarlo hasta que expire.
No es recomendable almacenar información sensible en el payload, ya que está codificada en Base64, no cifrada.
Revocar un JWT antes de que expire puede ser más complejo que invalidar una sesión tradicional.
Ejemplo en una API
Cliente → Login (usuario y contraseña)
        ↓
Servidor → Genera JWT
        ↓
Cliente → Guarda el JWT
        ↓
Cliente → Envía: Authorization: Bearer <JWT>
        ↓
Servidor → Verifica la firma y autoriza el acceso

En resumen, JWT es un "pase de acceso" digital firmado que permite a un usuario autenticarse una vez y acceder a recursos protegidos sin tener que enviar sus credenciales en cada solicitud. Es muy utilizado en APIs REST, aplicaciones con React, Angular, Vue, Flutter, y frameworks de backend como Node.js, Spring Boot, ASP.NET y Django.