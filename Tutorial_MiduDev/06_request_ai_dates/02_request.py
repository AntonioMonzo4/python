#Como hacer peticiones a una API con Python 

#sin dependencia externa
import urllib.request
import json
url = "https://jsonplaceholder.typicode.com/posts/"

try:
    response = urllib.request.urlopen(url)  # Abrir la URL y obtener la respuesta
    data = json.loads(response.read())  # Leer la respuesta y convertirla de JSON a un diccionario de Python
    print(data)  # Imprimir los datos obtenidos de la API
except urllib.error.URLError as e:
    print("Error al hacer la petición:", e.reason)  # Imprimir el error si la petición falla
finally:
    if 'response' in locals():
        response.close()  # Cerrar la conexión si se abrió

response = urllib.request.urlopen(url)#Abrir la URL y obtener la respuesta
data = json.loads(response.read())#Leer la respuesta y convertirla de JSON a un diccionario de Python
print(data) #Imprimir los datos obtenidos de la API
response.close()#Cerrar la conexión

#con la librería requests (recomendada)
import requests
url = "https://jsonplaceholder.typicode.com/posts/"
try:
    response = requests.get(url)  # Hacer una petición GET a la URL
    response.raise_for_status()  # Verificar que la respuesta fue exitosa (código 200)
    data = response.json()  # Convertir la respuesta de JSON a un diccionario de Python
    print(data[0])  # Imprimir el primer elemento de los datos obtenidos de la API
except requests.exceptions.RequestException as e:   
    print(data)  # Imprimir los datos obtenidos de la API
except requests.exceptions.RequestException as e:
    print("Error al hacer la petición:", e)  # Imprimir el error si la petición falla
    
#Hacer una petición POST a la API
url = "https://jsonplaceholder.typicode.com/posts/"
payload = {
    "title": "foo",
    "body": "bar",
    "userId": 1
}
try:
    response = requests.post(url, json=payload)  # Hacer una petición POST a la URL con el payload como JSON
    response.raise_for_status()  # Verificar que la respuesta fue exitosa (código 201)
    data = response.json()  # Convertir la respuesta de JSON a un diccionario de Python
    print(data)  # Imprimir los datos obtenidos de la API después de la petición POST
except requests.exceptions.RequestException as e:
    print("Error al hacer la petición:", e)  # Imprimir el error si la petición falla

#Hacer una petición GET a la API con parámetros de consulta
url = "https://jsonplaceholder.typicode.com/posts/"
params = {
    "userId": 1
}   
try:
    response = requests.get(url, params=params)  # Hacer una petición GET a la URL con los parámetros de consulta
    response.raise_for_status()  # Verificar que la respuesta fue exitosa (código 200)
    data = response.json()  # Convertir la respuesta de JSON a un diccionario de Python
    print(data)  # Imprimir los datos obtenidos de la API después de la petición GET con parámetros
except requests.exceptions.RequestException as e:
    print("Error al hacer la petición:", e)  # Imprimir el error si la petición falla

#Hacer un PUT a la API para actualizar un recurso
url = "https://jsonplaceholder.typicode.com/posts/1"
payload = {
    "id": 1,
    "title": "foo",
    "body": "bar",
    "userId": 1
}
try:
    response = requests.put(url, json=payload)  # Hacer una petición PUT a la URL con el payload como JSON
    response.raise_for_status()  # Verificar que la respuesta fue exitosa (código 200)
    data = response.json()  # Convertir la respuesta de JSON a un diccionario de Python
    print(data)  # Imprimir los datos obtenidos de la API después de la petición PUT
except requests.exceptions.RequestException as e:
    print("Error al hacer la petición:", e)  # Imprimir el error si la petición falla
    
#Hacer un DELETE a la API para eliminar un recurso
url = "https://jsonplaceholder.typicode.com/posts/1"
try:
    response = requests.delete(url)  # Hacer una petición DELETE a la URL
    response.raise_for_status()  # Verificar que la respuesta fue exitosa (código 200)
    print("Recurso eliminado exitosamente")  # Imprimir un mensaje de éxito si la eliminación fue exitosa
except requests.exceptions.RequestException as e:
    print("Error al hacer la petición:", e)  # Imprimir el error si la petición falla

#Hacer un PATCH a la API para actualizar parcialmente un recurso
url = "https://jsonplaceholder.typicode.com/posts/1"
payload = {
    "title": "foo"
}
try:
    response = requests.patch(url, json=payload)  # Hacer una petición PATCH a la URL con el payload como JSON
    response.raise_for_status()  # Verificar que la respuesta fue exitosa (código 200)
    data = response.json()  # Convertir la respuesta de JSON a un diccionario de Python
    print(data)  # Imprimir los datos obtenidos de la API después de la petición PATCH
except requests.exceptions.RequestException as e:
    print("Error al hacer la petición:", e)  # Imprimir el error si la petición falla


#USAR LA API DE OPENAI PARA OBTENER FECHAS Y HORAs 
import openai
openai.api_key = "TU_API_KEY_AQUI"
try:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt="¿Cuál es la fecha y hora actual en formato YYYY-MM-DD HH:MM:SS?",
        max_tokens=50
    )
    print("Respuesta de la API de OpenAI:", response.choices[0].text.strip())  # Imprimir la respuesta de la API de OpenAI      
except Exception as e:
    print("Error al hacer la petición a la API de OpenAI:", e)  # Imprimir el error si la petición a la API de OpenAI falla

#Usar la Api de OpenAI para usar gpt-4 
import openai
openai.api_key = "TU_API_KEY_AQUI"
try:
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {openai.api_key}"
    }
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "Eres un asistente útil que proporciona la fecha y hora actual."},
            {"role": "user", "content": "¿Cuál es la fecha y hora actual en formato YYYY-MM-DD HH:MM:SS?"}
        ],
        max_tokens=50
    )
    print("Respuesta de la API de OpenAI (GPT-4):", response.choices[0].message['content'].strip())  # Imprimir la respuesta de la API de OpenAI (GPT-4)
except Exception as e:
    print("Error al hacer la petición a la API de OpenAI (GPT-4):", e)  # Imprimir el error si la petición a la API de OpenAI (GPT-4) falla 


#Hacer una petición a la API de OpenAI para HACER UNA PREGUNTA usando gpt-4
import openai
api_key = "TU_API_KEY_AQUI"
url = "https://api.openai.com/v1/chat/completions"
openai.api_key = api_key
prompt = "¿Cuál es la fecha y hora actual en formato YYYY-MM-DD HH:MM:SS?"
try:
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json", 
        "Authorization": f"Bearer {openai.api_key}"
    }
    data = {
        "model": "gpt-4",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }
    response = requests.post(url, json=data, headers=headers )  # Hacer una petición POST a la API de OpenAI con el prompt como JSON
    print("Respuesta de la API de OpenAI (GPT-4):", response.json()['choices'][0]['message']['content'].strip())  # Imprimir la respuesta de la API de OpenAI (GPT-4)
except requests.exceptions.RequestException as e:
    print("Error al hacer la petición a la API de OpenAI (GPT-4):", e)  # Imprimir el error si la petición a la API de OpenAI (GPT-4) falla 

#LLAMA A LA API DE DEEPSEEK  

API_KEY = "TU_API_KEY_AQUI" 

try:
    url = "https://api.deepseek.com/v1/ask"
    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_KEY}"
    }
    data = {
        "model": "deepseek-chatbot",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(url, json=data, headers=headers )  
    print("Respuesta de la API de DeepSeek:", response.json())  
except requests.exceptions.RequestException as e:
    print("Error al hacer la petición a la API de DeepSeek:", e)    
    