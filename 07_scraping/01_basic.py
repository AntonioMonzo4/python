
import requests


url = "https://www.apple.com/es/shop/buy-iphone/iphone-15-pro"

response = requests.get(url)

if response.status_code == 200:
    print("La petición fue exitosa.")
    print("Contenido de la página:")
    print(response.text)  # Imprime el contenido HTML de la página

#NO PUEDES SALTARTE NI LOS PAYWALL NI LOS CAPTCHA, NI LOS BLOQUEOS DE IP, NI NADA DE ESO. 
#SI LA PÁGINA TIENE ALGUNA DE ESAS PROTECCIONES, NO PODRÁS HACER SCRAPING DE ELLA. S
# I QUIERES HACER SCRAPING DE UNA PÁGINA QUE TIENE ALGUNA DE ESAS PROTECCIONES, 
# TENDRÁS QUE USAR HERRAMIENTAS MÁS AVANZADAS COMO SELENIUM O PUPPETEER, PERO ESO YA ES OTRO NIVEL 
# Y REQUIERE MÁS CONOCIMIENTOS Y HABILIDADES.