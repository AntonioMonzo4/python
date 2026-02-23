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

#Docuentación de funciones con docstrings
def multiplicar(a, b):
    """Esta función multiplica dos números y devuelve el resultado."""
    return a * b
#Llamar a la función multiplicar
resultado = multiplicar(4, 6)
print("El resultado de la multiplicación es:", resultado)  # Imprime "El resultado de la multiplicación es: 24"
#help y __doc__ para acceder a la documentación de la función
print(multiplicar.__doc__)  # Imprime "Esta función multiplica dos números y devuelve el resultado."
help(multiplicar)  # Muestra la documentación de la función multiplicar     

#Funciones con valores predeterminados
def saludar(nombre="mundo"):
    print(f"Hola, {nombre}!")