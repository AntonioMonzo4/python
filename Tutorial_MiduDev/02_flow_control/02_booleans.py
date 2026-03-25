
#Los valores de los Bolean son un tipo de dato que representa dos valores posibles: True (verdadero) y False (falso).

#Operadores de comparación:
#== (igual a): Devuelve True si los valores son iguales.
#!= (diferente de): Devuelve True si los valores son diferentes.
#> (mayor que): Devuelve True si el valor de la izquierda es mayor que
#< (menor que): Devuelve True si el valor de la izquierda es menor que
#>= (mayor o igual que): Devuelve True si el valor de la izquierda es
#<= (menor o igual que): Devuelve True si el valor de la izquierda es menor o igual que el valor de la derecha.

#Ejemplos de operadores de comparación
print(5 == 5)  # True
print(5 != 3)  # True
print(5 > 3)   # True
print(5 < 10)  # True
print(5 >= 5)  # True
print(5 <= 4)  # False

#Comparación de cadenas
print("Hola" == "Hola")  # True
print("Hola" != "Adiós")  # True
print("Hola" > "Adiós")  # True (comparación lexicográfica)
print("Hola" < "Adiós")  # False (comparación lexicográfica)


#Tabla de verdad para operadores lógicos
#AND (y)
print(True and True)   # True
print(True and False)  # False
print(False and True)  # False
print(False and False) # False
#OR (o)
print(True or True)    # True
print(True or False)   # True
print(False or True)   # True
print(False or False)  # False
#NOT (no)
print(not True)   # False
print(not False)  # True
