#Transformar de un valor de un tipo a otro se llama "casting" o "conversión de tipos"
#Pythn tiene un tipado fuerte pero dinámico, lo que significa que cada valor tiene un tipo 
#específico pero las variables pueden cambiar de tipo

print("Conversión de tipos en Python") # Imprime el mensaje "Conversión de tipos en Python" en la consola
print(type(10)) # Imprime <class 'int'> en la consola
print(type(float(10))) # Imprime <class 'float'> en la consola
print(type(str(10))) # Imprime <class 'str'> en la consola

#Puedes convertir entre tipos numéricos
print(int(3.14)) # Imprime el valor 3 en la consola (trunca el decimal)
print(float(10)) # Imprime el valor 10.0 en la consola (agrega el punto decimal)
#También puedes convertir entre tipos de texto y números
print(int("123")) # Imprime el valor 123 en la consola (convierte la cadena a entero)
print(float("3.14")) # Imprime el valor 3.14 en la consola (convierte la cadena a flotante)
print(str(123)) # Imprime el valor "123" en la consola (convierte el entero a cadena)
print(str(3.14)) # Imprime el valor "3.14" en la consola (convierte el flotante a cadena)   

#Ten cuidado al convertir tipos, ya que no todos los valores pueden convertirse a otros tipos
#Por ejemplo, intentar convertir una cadena que no representa un número a entero o flotante generará un error
# print(int("Hola")) # Esto generará un ValueError: invalid literal for int() with base 10: 'Hola'

#También puedes usar la función bool() para convertir valores a booleanos
print(bool(0)) # Imprime False en la consola (cero se considera falso)
print(bool(1)) # Imprime True en la consola (cualquier número distinto de cero se considera verdadero)
print(bool("")) # Imprime False en la consola (cadena vacía se considera falsa)
print(bool("Hola")) # Imprime True en la consola (cualquier cadena no vacía se considera verdadera)
