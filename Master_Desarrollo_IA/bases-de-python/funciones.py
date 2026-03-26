def saludar(nombre):
    return f"Hola, {nombre}!"

saludo = saludar("Pepe")
print(saludo)
saludo = saludar("Juan")
print(saludo)

#Funcionea con parametros opcionales 
def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}!"