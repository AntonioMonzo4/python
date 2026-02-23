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