#Esto es para los inputs en python 

print("¿Cuál es tu nombre?")  # Imprime un mensaje solicitando el nombre del usuario
nombre = input()  # Lee la entrada del usuario y la almacena en la variable 'nombre'
print(f"Hola, {nombre}!")  # Imprime un saludo personalizado utilizando el nombre ingresado por el usuario
#También puedes proporcionar un mensaje directamente dentro de la función input()
edad = input("¿Cuántos años tienes? ")  # Solicita la edad del usuario y la almacena en la variable 'edad'
print(f"Tienes {edad} años.")  # Imprime la edad ingresada por el usuario
#Ten en cuenta que la función input() siempre devuelve una cadena de texto, incluso si el usuario ingresa un número. Si deseas trabajar con números, es necesario convertir la entrada a un tipo de dato numérico utilizando funciones como int() o float().
#Ejemplo de conversión de entrada a un número entero
edad = input("¿Cuántos años tienes? ")  # Solicita la edad del usuario
edad = int(edad)  # Convierte la entrada de texto a un número entero
print(f"En 5 años, tendrás {edad + 5} años.")  # Imprime la edad del usuario en 5 años

#En el mismoo input puedes pedir distintas cosas, por ejemplo el nombre y la edad al mismo tiempo, y luego separar esa información utilizando el método split()
datos = input("Ingresa tu nombre y edad separados por un espacio: ")  # Solicita al usuario que ingrese su nombre y edad separados por un espacio
nombre, edad = datos.split()  # Separa la entrada en dos partes: nombre y edad
edad = int(edad)  # Convierte la edad de texto a un número entero
print(f"Hola, {nombre}. Tienes {edad} años.")  # Imprime un saludo personalizado con el nombre y la edad del usuario
