#Diccionarios 
#Los diccionarios son una estructura de datos que almacena pares de clave-valor.
#Se definen utilizando llaves {} y cada par de clave-valor se separa por dos puntos :.
#Creación de un diccionario
persona = {
    "nombre": "Alice",
    "edad": 30,
    "ciudad": "Madrid"
}
print(persona)  # Imprime el diccionario completo

#Acceso a los valores del diccionario
print(persona["nombre"])  # Imprime "Alice"
print(persona["edad"])  # Imprime 30

#Modificación de los valores del diccionario
persona["edad"] = 31
print(persona["edad"])  # Imprime 31

#Agregar nuevos pares de clave-valor al diccionario
persona["profesión"] = "Ingeniera"
print(persona)  # Imprime el diccionario actualizado con la nueva clave "profesión"

#Eliminar un par de clave-valor del diccionario
del persona["ciudad"]
print(persona)  # Imprime el diccionario actualizado sin la clave "ciudad"

#Obtener todas las claves, valores o pares de clave-valor del diccionario
print(persona.keys())  # Imprime dict_keys(['nombre', 'edad', 'profesión'])
print(persona.values())  # Imprime dict_values(['Alice', 31, 'Ingeniera'])
print(persona.items())  # Imprime dict_items([('nombre', 'Alice'), ('edad', 31), ('profesión', 'Ingeniera')])

#Verificar si una clave existe en el diccionario
print("nombre" in persona)  # Imprime True
print("ciudad" in persona)  # Imprime False

#Recorrer un diccionario con un bucle for
for clave, valor in persona.items():
    print(f"Clave: {clave}, Valor: {valor}")    
#Diccionarios anidados
#Un diccionario puede contener otro diccionario como valor, lo que se conoce como diccionario anidado.
estudiante = {
    "nombre": "Bob",
    "edad": 22,
    "notas": {
        "matemáticas": 85,
        "historia": 90,
        "ciencias": 78
    }
}
print(estudiante)  # Imprime el diccionario completo con el diccionario anidado
print(estudiante["notas"]["matemáticas"])  # Imprime 85, accediendo al valor de la clave "matemáticas" dentro del diccionario "notas"

#Sobreescritura de un diccionario
#Si asignas un nuevo valor a una clave que ya existe en el diccionario, el valor anterior se sobrescribirá con el nuevo valor.
persona["nombre"] = "Charlie"   
print(persona)  # Imprime el diccionario actualizado con el nuevo valor para la clave "nombre"

#sobreescritura de un diccionario con otro diccionario
persona = {
    "nombre": "David",
    "edad": 25,
    "ciudad": "Barcelona"
}
print(persona)  # Imprime el diccionario original
persona = {
    "nombre": "Eva",
    "edad": 28,
    "ciudad": "Valencia"
}
print(persona)  # Imprime el diccionario actualizado con los nuevos valores
#MÉTODO UPDATE PARA ACTUALIZAR UN DICCIONARIO
persona.update({"nombre": "Frank", "edad": 35})
print(persona)  # Imprime el diccionario actualizado con los nuevos valores para las claves "nombre" y "edad"
