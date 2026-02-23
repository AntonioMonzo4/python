#Creación de listas 
#Una lista es una colección ordenada y mutable de elementos. Se pueden crear utilizando corchetes [] y separando los elementos por comas.
frutas = ["manzana", "banana", "naranja"]
numeros = [1, 2, 3, 4, 5]
mixta = ["texto", 42, 3.14, True]

#Acceso a elementos de una lista
#Puedes acceder a los elementos de una lista utilizando índices. El índice comienza en 0 para el primer elemento, 1 para el segundo, y así sucesivamente.
print(frutas[0])  # Imprime "manzana"
print(numeros[2])  # Imprime 3
print(mixta[1])    # Imprime 42

#Modificación de elementos de una lista
#Las listas son mutables, lo que significa que puedes cambiar sus elementos después de haberlas creado.
frutas[1] = "pera"
print(frutas)  # Imprime ["manzana", "pera", "naranja"]

