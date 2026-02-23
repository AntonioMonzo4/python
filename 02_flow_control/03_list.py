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

#Acceder al último elemento de una lista
#Puedes usar índices negativos para acceder a los elementos desde el final de la lista. El índice -1 se refiere al último elemento, -2 al penúltimo, y así sucesivamente.
print(frutas[-1])  # Imprime "naranja"

#Añadir elementos a una lista
frutas.append("uva")
print(frutas)  # Imprime ["manzana", "pera", "naranja", "uva"]
numeros.append(6)
print(numeros)  # Imprime [1, 2, 3, 4, 5, 6]

#Lista de listas
#Puedes crear listas que contengan otras listas como elementos. Esto se conoce como listas anidadas.
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matriz[0])  # Imprime [1, 2, 3]
print(matriz[1][2])  # Imprime 6 (elemento en la segunda fila, tercera columna) 

#Slicing de listas
#Puedes obtener una sublista utilizando el slicing. La sintaxis es lista[inicio:fin :paso], donde inicio es el índice de inicio (inclusive), fin es el índice de fin (exclusive) y paso es el número de elementos a saltar.
print(frutas[0:2])  # Imprime ["manzana", "pera"]
print(numeros[1:5:2])  # Imprime [2, 4]

