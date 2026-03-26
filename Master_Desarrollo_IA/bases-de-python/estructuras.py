lenguajes = ["Python" , "Java" , "PHP" , "JavaScript" , "C#"]
print(type(lenguajes))
print(lenguajes)
print(lenguajes[0])
print(lenguajes[4])

lenguajes.append("C++")
print(lenguajes)    

lenguajes.insert(1,"Ruby")
print(lenguajes)

for lenguaje in lenguajes:
    print(lenguaje) 

lenguajes.remove("PHP")
print(lenguajes)

#tuplas 
tupla = ("Python" , "Java" , "PHP" , "JavaScript" , "C#")
print(type(tupla))  
print(tupla)
print(tupla[0])
print(tupla[4])

#Las tuplas son inmutables, no se pueden modificar, agregar o eliminar elementos después de su creación.

#set 
conjunto = {"Python" , "Java" , "PHP" , "JavaScript" , "C#"}
print(type(conjunto))
print(conjunto)
conjunto.add("C++")
print(conjunto)
conjunto.remove("PHP")
print(conjunto)
conjunto.discard("PHP") # Si intentamos eliminar un elemento que no existe, no se generará un error.
print(conjunto)
conjunto.pop() # Elimina un elemento aleatorio del conjunto.
print(conjunto)
# conjunto.remove("Ruby") # Si intentamos eliminar un elemento que no existe, se generará un error.
print(conjunto)
# conjunto.discard("Ruby") # Si intentamos eliminar un elemento que no existe, no se generará un error.
print(conjunto)
conjunto.clear() # Elimina todos los elementos del conjunto.
print(conjunto)
conjunto2= {"Python" , "Java" , "PHP" , "JavaScript" , "C#"}
conjunto3 = conjunto.union(conjunto2) # Devuelve un nuevo conjunto que contiene todos los elementos de ambos conjuntos.
print(conjunto3)
conjunto3 = conjunto.intersection(conjunto2) # Devuelve un nuevo conjunto que contiene solo los elementos comunes a ambos conjuntos.
print(conjunto3)
conjunto3 = conjunto.difference(conjunto2) # Devuelve un nuevo conjunto que contiene los elementos que están en el primer conjunto pero no en el segundo.
print(conjunto3)
conjunto3 = conjunto.symmetric_difference(conjunto2) # Devuelve un nuevo conjunto que contiene los elementos que están en uno de los conjuntos pero no en ambos.
print(conjunto3)

#diccionario = {"Python" : "Lenguaje de programación" , "Java" : "Lenguaje de programación" , "PHP" : "Lenguaje de programación" , "JavaScript" : "Lenguaje de programación" , "C#" : "Lenguaje de programación"}
diccionario = {"Python" : "Lenguaje de programación" , "Java" : "Lenguaje de programación" , "PHP" : "Lenguaje de programación" , "JavaScript" : "Lenguaje de programación" , "C#" : "Lenguaje de programación"}
print(type(diccionario))
print(diccionario)
print(diccionario["Python"])
diccionario["C++"] = "Lenguaje de programación"
print(diccionario)
del diccionario["PHP"]
print(diccionario)

estudiante = {"nombre" : "Juan" , "edad" : 20 , "carrera" : "Ingeniería en Sistemas"}
print(estudiante)# Imprime el diccionario completo
print(estudiante["nombre"]) # Imprime el valor asociado a la clave "nombre"
# Agregar un nuevo par clave-valor al diccionario
estudiante["universidad"] = "Universidad Nacional"
print(estudiante)
# Eliminar un par clave-valor del diccionario
del estudiante["edad"]  
print(estudiante)

print("Detalles del estudiante:")
for clave, valor in estudiante.items():
    print(f"{clave}: {valor}")

print("Claves del diccionario:")
for clave in estudiante.keys():
    print(clave)    
