import requests

url ="https://jsonplaceholder.typicode.com/users/1"
response =requests.get(url)

if response.status_code == 200:
    print("Solicitud aceptada")
    usuario = response.json()
    print(f"Nombre: {usuario["name"]}")
else: 
    print("Error en la solicitud")
    print(f"Código de estado: {response.status_code}")

