
edad = 18 

if edad >= 18:
    print("Eres mayor de edad.")

if edad < 18:
    print("Eres menor de edad.")
else:
    print("Eres mayor de edad.")

nota = 85
if nota >= 90:
    print("Excelente")
elif nota >= 80:
    print("Muy bien")
elif nota >= 70:
    print("Bien")
elif nota >= 60:
    print("Suficiente")
else:
    print("Insuficiente")
    

#OPCIONES DE OPERADORES LÓGICOS
#AND (y): Devuelve True si ambas condiciones son verdaderas.
#OR (o): Devuelve True si al menos una de las condiciones es verdadera.
#NOT (no): Devuelve True si la condición es falsa, y False si la condición es verdadera.
edad = 25
if edad >= 18 and edad < 65:
    print("Eres un adulto.")
if edad < 18 or edad >= 65:
    print("No eres un adulto.")
if not (edad < 18):
    print("Eres mayor de edad.")

#OPERADOR TERNARIO
#El operador ternario es una forma concisa de escribir una expresión condicional en una sola línea. La sintaxis general es:
#valor_si_verdadero if condición else valor_si_falso
edad = 20
mensaje = "Eres mayor de edad." if edad >= 18 else "Eres menor de edad."
print(mensaje)