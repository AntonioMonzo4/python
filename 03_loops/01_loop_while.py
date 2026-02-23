#Bucle while con una condición
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1  # Incrementa el contador en 1

#Bucle while con una condición de parada
while True:
    respuesta = input("¿Quieres salir del bucle? (s/n): ")
    if respuesta.lower() == 's':
        print("Saliendo del bucle...")
        break  # Sale del bucle si la respuesta es 's'
    else:
        print("Continuando el bucle...")

#Bucle while con una condición de parada basada en una variable
numero = 0
while numero < 10:
    print("Número:", numero)
    numero += 1  # Incrementa el número en 1

#Bucle while con una condición de parada basada en una lista
frutas = ["manzana", "banana", "naranja"]
while frutas:
    fruta = frutas.pop(0)  # Elimina la primera fruta de la lista
    print("Procesando:", fruta)

#Bucle while con una condición de parada basada en una función
def es_par(numero):
    return numero % 2 == 0  
contador = 0
while contador < 10:
    if es_par(contador):
        print("Número par:", contador)
    contador += 1  # Incrementa el contador en 1    

#Palabra clave continue
contador = 0
while contador < 10:
    contador += 1  # Incrementa el contador en 1
    if contador % 2 == 0:
        continue  # Salta el resto del código en esta iteración si el número es par
    print("Número impar:", contador)

    