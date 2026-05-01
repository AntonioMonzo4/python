from openai import OpenAI
client = OpenAI()

response = client.responses.create(
    model="gpt-5.5",
    input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)

#setx OPENAI_API_KEY "your_api_key_here"
#pip install openai


#Para usarla: 

# Primero creamos una APIkey en .env o env.local
# Segundo, importamos la key con . env.local
# Tercero, importamos la libreria y creamos el cliente

