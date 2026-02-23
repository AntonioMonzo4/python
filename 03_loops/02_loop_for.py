#Bucle for 
#Bucle for con una lista
frutas = ["manzana", "banana", "naranja"]
for fruta in frutas:
    print("Fruta:", fruta)

#Bucle for con un rango de números
for numero in range(5):
    print("Número:", numero)

#Bucle for con un rango de números y un paso
for numero in range(0, 10, 2):
    print("Número par:", numero)    

#Bucle for con una cadena
palabra = "Python"
for letra in palabra:
    print("Letra:", letra)

#Bucle for con una lista de listas
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for fila in matriz:
    for elemento in fila:
        print("Elemento:", elemento)

#Bucle for con una función
def es_par(numero):
    return numero % 2 == 0
for numero in range(10):
    if es_par(numero):
        print("Número par:", numero)

#Palabra clave continue
for numero in range(10):
    if numero % 2 == 0:
        continue  # Salta el resto del código en esta iteración si el número es par
    print("Número impar:", numero)

#Bucle for con else
for numero in range(5):
    print("Número:", numero)
else:
    print("El bucle ha terminado normalmente")

#Bucle for con else y break
for numero in range(5):
    print("Número:", numero)
    if numero == 3:
        print("Se ha alcanzado el número 3, saliendo del bucle...")
        break  # Sale del bucle si el número es igual a 3
else:
    print("El bucle ha terminado normalmente")


#Bucle for con enumerate
frutas = ["manzana", "banana", "naranja"]
for indice, fruta in enumerate(frutas):
    print(f"Índice: {indice}, Fruta: {fruta}")

#Bucle for con zip
nombres = ["Alice", "Bob", "Charlie"]
edades = [25, 30, 35]
for nombre, edad in zip(nombres, edades):
    print(f"Nombre: {nombre}, Edad: {edad}")    


#Compresión de listas con bucle for
#Puedes crear una nueva lista a partir de una existente utilizando una comprensión de listas.
#La sintaxis es [expresión for elemento in iterable if condición], donde expresión es el valor que se agregará a la nueva lista,
#elemento es la variable que representa cada elemento del iterable, y condición es una expresión opcional que filtra los elementos.
numeros = [1, 2, 3, 4, 5]
cuadrados = [numero ** 2 for numero in numeros]
print(cuadrados)  # Imprime [1, 4, 9, 16, 25]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)  # Imprime [2, 4]

#Con cadenas puedes usar la comprensión de listas para crear una nueva lista de caracteres a partir de una cadena.
palabra = "Python"
letras = [letra for letra in palabra]
print(letras)  # Imprime ['P', 'y', 't', 'h', 'o', 'n']
