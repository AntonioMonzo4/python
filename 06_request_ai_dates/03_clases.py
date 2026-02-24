#Clases en Python
class Coche: 
    tipo = "vehículo de cuatro ruedas"
    ruedas = 4

    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def arracar(self):
        return f"El {self.marca} {self.modelo} está arrancando."
    

#Crear una clase para llamar a la API de OpenAI, Deepseek o cualquier otra API de IA
import requests

class APIClient:
    def __init__(self, api_key, base_url, model):
        self.api_key = api_key
        self.base_url = base_url
        self.model = model
    
    def ask(self, prompt):
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }
        data = {
            "model": self.model,
            "messages": [{"role": "user", "content": prompt}]
        }
        
        response = requests.post(self.base_url, json=data, headers=headers)
        response.raise_for_status()  # Verificar si la respuesta fue exitosa
        return response.json()
        
open_ia = APIClient(OPENAI_API_KEY, "https://api.openai.com/v1/chat/completions", "gpt-4")

open_ia.ask("Describe este código en dos minutos")
