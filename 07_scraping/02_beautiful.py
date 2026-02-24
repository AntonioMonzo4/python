#Web scrapping con BeautifulSoup
from bs4 import BeautifulSoup
import requests 

url = "https://www.apple.com/es/shop/buy-iphone/iphone-15-pro"   
response = requests.get(url)

if response.status_code == 200:
    print("La petición fue exitosa.")
    soup = BeautifulSoup(response.text, 'html.parser')  # Analizar el contenido HTML de la página
    print(soup.prettify())  # Imprime el contenido HTML de la página de forma legible

    title_tag = soup.find('title')  # Encontrar la etiqueta <title> en el HTML
    if title_tag:
        print("Título de la página:", title_tag.text)  # Imprime el texto dentro de la etiqueta <title>
    else:
        print("No se encontró la etiqueta <title> en la página.")
else:
    print("La petición falló con el código de estado:", response.status_code)


    
  # find price using bs
  # price_span = soup.find('span', class_='rc-prices-fullprice')
  # if price_span:
  #   print(f"El precio del producto es: {price_span.text}")

  # find all the prices
  # prices_span = soup.find_all(class_='rc-prices-fullprice')
  # for price in prices_span:
  #   print(f"El precio del producto es: {price.text}")

  # find each product and get the name and the price
  #products = soup.find_all(class_='rc-productselection-item')
  # for product in products:
  # name = product.find(class_="list-title").text
  # price = product.find(class_="rc-prices-fullprice").attrs
  # print(f"El producto con las características:\n {name}\nPrecio de {price}\n\n")