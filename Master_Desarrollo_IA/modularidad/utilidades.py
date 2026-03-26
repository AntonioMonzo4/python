def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

def es_palindromo(palabra):
    palabra = palabra.replace(" ", "").lower()
    return palabra == palabra[::-1]

def calcular_factorial(n):
    if n < 0:
        raise ValueError("El número debe ser no negativo")
    elif n == 0 or n == 1:
        return 1
    else:
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial
