#Programacion Funcional
#La programación funcional es un paradigma de programación que se basa en el uso de funciones puras,
# es decir, funciones que no tienen efectos secundarios y siempre devuelven el mismo resultado para los mismos argumentos. 
# En la programación funcional, las funciones son tratadas como ciudadanos de primera clase, 
# lo que significa que pueden ser asignadas a variables, pasadas como argumentos a otras funciones y devueltas como resultados.
#Algunas características clave de la programación funcional incluyen:
#1. Funciones puras: Las funciones puras no tienen efectos secundarios y siempre devuelven el mismo resultado para los mismos argumentos. 
# Esto facilita la depuración y el razonamiento sobre el código.
#2. Inmutabilidad: En la programación funcional, los datos son inmutables, lo que significa que no pueden ser modificados después de su creación. 
# En lugar de modificar los datos, se crean nuevos datos a partir de los existentes. 
#3. Funciones de orden superior: Las funciones de orden superior son funciones que pueden tomar otras funciones 
# como argumentos o devolver funciones como resultados.
#4. Recursión: La recursión es una técnica en la que una función se llama a sí misma para resolver un problema.
#5. Composición de funciones: La composición de funciones es el proceso de combinar dos o más funciones para crear una nueva función.
#6. Evaluación perezosa: La evaluación perezosa es una técnica en la que las expresiones no se evalúan hasta que se necesitan, 
# lo que puede mejorar el rendimiento y reducir el uso de memoria. 

#Ejemplo de función pura
def suma(a, b):
    return a + b
#Ejemplo de función de orden superior
def aplicar_funcion(func, a, b):
    return func(a, b)
resultado = aplicar_funcion(suma, 3, 5)
print(resultado)  # Salida: 8
#Ejemplo de composición de funciones
def multiplicar(a, b):
    return a * b 
def componer(func1, func2):
    def funcion_compuesta(a, b):
        return func1(func2(a, b), func2(a, b))
    return funcion_compuesta
funcion_compuesta = componer(suma, multiplicar)
resultado = funcion_compuesta(2, 3)
print(resultado)  # Salida: 36 (suma(multiplicar(2, 3), multiplicar(2, 3)) = suma(6, 6) = 12)

#Funciones lambda: Las funciones lambda son funciones anónimas que se pueden definir en una sola línea.
# Se utilizan comúnmente para funciones de orden superior o para crear funciones pequeñas y simples.
#Ejemplo de función lambda
suma_lambda = lambda a, b: a + b
resultado = suma_lambda(4, 6)
print(resultado)  # Salida: 10

#Map, filter, list comprehensions y reduce son funciones y técnicas comunes en la programación funcional
#para trabajar con colecciones de datos.
# Map se utiliza para aplicar una función a cada elemento de una colección,
# Filter se utiliza para filtrar elementos de una colección según una condición,
# List comprehensions se utilizan para crear nuevas listas a partir de otras listas de manera concisa,
# y Reduce se utiliza para reducir una colección de datos a un solo valor utilizando una función de acumulación.
from functools import reduce
#Ejemplo de map
numeros = [1, 2, 3, 4, 5]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)  # Salida: [1, 4, 9, 16, 25]
#Ejemplo de filter
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Salida: [2, 4]
#Ejemplo de list comprehensions
cubos = [x**3 for x in numeros]
print(cubos)  # Salida: [1, 8, 27, 64, 125]
#Ejemplo de reduce
suma_total = reduce(lambda a, b: a + b, numeros)
print(suma_total)  # Salida: 15
