#Expresiones Regulares
# Las expresiones regulares son una herramienta poderosa para buscar y manipular texto. En Python, el módulo `re` proporciona funciones para trabajar con expresiones regulares.

import re

#Búsqueda de patrones
texto = "El número de teléfono es 123-456-7890."
#Buscar un patrón específico (número de teléfono)
patron = r"\d{3}-\d{3}-\d{4}"
resultado = re.search(patron, texto)
if resultado:
    print("Número de teléfono encontrado:", resultado.group())  # Imprime "Número de teléfono encontrado: 123-456-7890"
else:
    print("Número de teléfono no encontrado.")
#Reemplazo de texto
nuevo_texto = re.sub(patron, "XXX-XXX-XXXX", texto)
print("Texto después del reemplazo:", nuevo_texto)  # Imprime "Texto después del reemplazo: El número de teléfono es XXX-XXX-XXXX." 
#División de texto
partes = re.split(r"\s+", texto)
print("Partes del texto:", partes)  # Imprime "Partes del texto: ['El', 'número', 'de', 'teléfono', 'es', '123-456-7890.']"
#Búsqueda de todos los patrones
numeros = re.findall(r"\d+", texto)
print("Números encontrados:", numeros)  # Imprime "Números encontrados: ['123', '456', '7890']"
#Uso de grupos en expresiones regulares
patron_con_grupos = r"(\d{3})-(\d{3})-(\d{4})"
resultado_con_grupos = re.search(patron_con_grupos, texto)  
if resultado_con_grupos:
    print("Número de teléfono encontrado:", resultado_con_grupos.group())  # Imprime "Número de teléfono encontrado: 123-456-7890"
    print("Código de área:", resultado_con_grupos.group(1))  # Imprime "Código de área: 123"
    print("Primer bloque:", resultado_con_grupos.group(2))  # Imprime "Primer bloque: 456"
    print("Segundo bloque:", resultado_con_grupos.group(3))  # Imprime "Segundo bloque: 7890"   
else:
    print("Número de teléfono no encontrado.")
#Expresiones regulares con banderas
texto_mayusculas = "ESTE ES UN TEXTO EN MAYÚSCULAS  Y minúsculas."
#Buscar un patrón sin importar mayúsculas o minúsculas
patron_sin_mayusculas = r"texto"
resultado_sin_mayusculas = re.search(patron_sin_mayusculas, texto_mayusculas, re.IGNORECASE)
if resultado_sin_mayusculas:
    print("Patrón encontrado:", resultado_sin_mayusculas.group())  # Imprime "Patrón encontrado: TEXTO" 
else:
    print("Patrón no encontrado.")
#Método match para buscar al inicio del texto
resultado_match = re.match(r"ESTE", texto_mayusculas)   
if resultado_match:
    print("El texto comienza con 'ESTE'.")  # Imprime "El texto comienza con 'ESTE'."   
else:
    print("El texto no comienza con 'ESTE'.")
#Método fullmatch para buscar una coincidencia completa
resultado_fullmatch = re.fullmatch(r"ESTE ES UN TEXTO EN MAYÚSCULAS  Y minúsculas.", texto_mayusculas)
if resultado_fullmatch:
    print("El texto coincide completamente con el patrón.")  # Imprime "El texto coincide completamente con el patrón."
else:
    print("El texto no coincide completamente con el patrón.")
#Método finditer para encontrar todas las coincidencias con información de posición
for coincidencia in re.finditer(r"\d+", texto):
    print(f"Número encontrado: {coincidencia.group()} en la posición {coincidencia.start()}-{coincidencia.end()}")  
    # Imprime "Número encontrado: 123 en la posición 27-30", "Número encontrado: 456 en la posición 31-34", "Número encontrado: 7890 en la posición 35-39"  
#Método split para dividir el texto en partes utilizando un patrón como delimitador
partes_con_split = re.split(r"\s+", texto)
print("Partes del texto con split:", partes_con_split)  # Imprime "Partes del texto con split: ['El', 'número', 'de', 'teléfono', 'es', '123-456-7890.']"
#Método findall para encontrar todas las coincidencias de un patrón
numeros_con_findall = re.findall(r"\d+", texto)
print("Números encontrados con findall:", numeros_con_findall)  # Imprime "Números encontrados con findall: ['123', '456', '7890']"
