#Las variable son espacios de memoria que se utilizan para almacenar datos. En Python, 
#no es necesario declarar el tipo de dato de una variable, 
#ya que el intérprete lo infiere automáticamente.   

#Para crear una variable, simplemente asigna un valor a un nombre utilizando el operador de asignación (=)
mi_variable = 10
print(mi_variable) # Imprime el valor 10 en la consola
#Puedes asignar cualquier tipo de dato a una variable
mi_variable = "Hola Mundo"

#También puedes asignar el resultado de una operación a una variable
a = 5  
b = 3
suma = a + b
print(suma) # Imprime el resultado de la suma, que es 8
#Las variables pueden ser utilizadas para almacenar diferentes tipos de datos, como números, cadenas de texto, listas, diccionarios, etc.
#Ejemplo de variables con diferentes tipos de datos
numero = 42
texto = "Python es genial"  
lista = [1, 2, 3, 4, 5]
diccionario = {"nombre": "Juan", "edad": 30}

#Es importante seguir las reglas de nomenclatura de variables en Python.
#Las variables deben comenzar con una letra o un guion bajo, y pueden contener letras, números y guiones bajos.
#No pueden contener espacios ni caracteres especiales, y no pueden ser palabras reservadas de Python.   
#Ejemplo de variables con nombres válidos
mi_variable = 10
_variable = "Hola"
variable2 = 3.14
#Ejemplo de variables con nombres inválidos (esto generará un error)
#2variable = 5  # No puede comenzar con un número
#mi variable = "Hola"  # No puede contener espacios
#mi-variable = "Hola"  # No puede contener guiones


#Es tipado dinámico, lo que significa que el tipo de dato de una variable puede cambiar durante la ejecución del programa.
#Ejemplo de tipado dinámico
mi_variable = 10  # mi_variable es un entero
print(mi_variable)  # Imprime 10
mi_variable = "Ahora soy una cadena"  # mi_variable ahora es una cadena de texto
print(mi_variable)  # Imprime "Ahora soy una cadena"
#En resumen, las variables son fundamentales en la programación, ya que nos permiten almacenar y manipular datos de manera eficiente.

#Es de tipado fuerte, lo que significa que el tipo de dato de una variable no puede cambiar automáticamente a otro tipo sin una conversión explícita.
#Ejemplo de tipado fuerte
mi_variable = 10  # mi_variable es un entero
print(mi_variable)  # Imprime 10
#Intentar asignar un valor de tipo diferente sin conversión explícita generará un error
#mi_variable = "Ahora soy una cadena"  # Esto generará un error porque no se puede asignar una cadena a una variable que anteriormente era un entero
#Para cambiar el tipo de dato de una variable, es necesario realizar una conversión explícita
mi_variable = str(mi_variable)  # Convertimos el entero a una cadena
print(mi_variable)  # Imprime "10" como una cadena de texto
#Podemos usar f-strings para mostrar el valor de una variable junto con texto
nombre = "Alice"
edad = 30
print(f"Mi nombre es {nombre} y tengo {edad} años.")  # Imprime "Mi nombre es Alice y tengo 30 años."

#Palabras reservadas son palabras que tienen un significado especial en Python y no pueden ser utilizadas como nombres de variables.
#Ejemplo de palabras reservadas
#def = 5  # No se puede usar 'def' como nombre de variable porque
#class = "Hola"  # No se puede usar 'class' como nombre de variable porque
#if = True  # No se puede usar 'if' como nombre de variable porque
#Es importante evitar el uso de palabras reservadas para nombrar variables, ya que esto puede causar errores en el código.

#Tambien puedes trucar el tipo de una variable(anotación de tipo) para indicar el tipo de dato que se espera que tenga una variable, aunque esto no es obligatorio en Python.
is_user_logged: bool = True
print(is_user_logged)  # Imprime True
#Pero tienes que pner el typechecker para que te avise de los errores de tipo