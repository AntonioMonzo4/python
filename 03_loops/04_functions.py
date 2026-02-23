#Funciones en Python

#Estructura de una función
def nombre_de_la_funcion(parametros):
    # Código de la función
    return resultado  # Opcional, solo si la función devuelve un valor  
#Ejemplo de una función que suma dos números
def sumar(a, b):
    return a + b
#Llamar a la función sumar
resultado = sumar(3, 5)
print("El resultado de la suma es:", resultado)  # Imprime "El resultado de la suma es: 8"

#Definir una función
def saludar(nombre):
    print(f"Hola, {nombre}!")

#Llamar a una función
saludar("Alice")  # Imprime "Hola, Alice!"