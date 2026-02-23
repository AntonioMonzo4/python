#MetaCaractes en expresiones regulares
import re   

#Ejemplo de uso de metacaracteres en expresiones regulares
texto = "El número de teléfono es 123-456-7890."
#Búsqueda de un patrón específico utilizando metacaracteres
patron = r"\d{3}-\d{3}-\d{4}"
resultado = re.search(patron, texto)
if resultado:
    print("Número de teléfono encontrado:", resultado.group())  # Imprime "Número de teléfono encontrado: 123-456-7890"
else:
    print("Número de teléfono no encontrado.")
#Uso de metacaracteres para buscar patrones más complejos
texto_con_email = "Mi correo electrónico es juan.perez@ejemplo.com y mi otro correo es maria.gomez@otrodominio.org."
#Buscar correos electrónicos
patron_email = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"
resultados_emails = re.findall(patron_email, texto_con_email)
print("Correos electrónicos encontrados:", resultados_emails)  # Imprime "Correos electrónicos encontrados: ['juan.perez@ejemplo.com', 'maria.gomez@otrodominio.org']"