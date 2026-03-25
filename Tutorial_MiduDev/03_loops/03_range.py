#range() IMPORTANTE no es una función, 
#es un tipo de dato que representa una secuencia de números enteros. 
#Es comúnmente utilizado en bucles for para iterar sobre un rango de números.

#Bucle for con range
for numero in range(5):
    print("Número:", numero)

#Bucle for con range y un paso
for numero in range(0, 10, 2):
    print("Número par:", numero)

#Bucle for con range y un paso negativo
for numero in range(10, 0, -1):
    print("Número:", numero)

#Bucle for con range y un paso negativo para contar hacia atrás
for numero in range(10, 0, -1):
    print("Número:", numero)

#Para crear una lista a partir de un rango de números, puedes convertir el objeto range en una lista utilizando la función list().
numeros = list(range(5))

#Hacer algo con los números del rango con _
for _ in range(5):
    print("Hola, mundo!")
    
