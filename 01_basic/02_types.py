#Python tiene distintos tipos de datos 

#Tipo de dato entero (int)
numero_entero = 10
print(numero_entero) # Imprime el valor 10 en la consola

#Tipo de dato flotante (float)
numero_flotante = 3.14
print(numero_flotante) # Imprime el valor 3.14 en la consola
#Los números flotantes pueden usar notación científica
numero_grande = 1.5e6
print(numero_grande) # Imprime el valor 1500000.0 en la consola

#Tipo de dato número complejo (complex)
numero_complejo = 2 + 3j
print(numero_complejo) # Imprime el número complejo (2+3j) en la consola

#Tipo de dato cadena (str)
mensaje = "Hola Mundo"
print(mensaje) # Imprime el mensaje "Hola Mundo" en la consola

#Tipo de dato booleano (bool)
es_verdadero = True
print(es_verdadero) # Imprime el valor True en la consola
es_falso = False
print(es_falso) # Imprime el valor False en la consola

#Tiop de dato None (NoneType)
valor_nulo = None
print(valor_nulo) # Imprime el valor None en la consola

#Python también tiene tipos de datos compuestos como listas, tuplas y diccionarios
#Tipo de dato lista (list)
mi_lista = [1, 2, 3, "Hola", True]
print(mi_lista) # Imprime la lista [1, 2, 3, "Hola", True] en la consola

#Tipo de dato tupla (tuple)
mi_tupla = (1, 2, 3, "Mundo", False)
print(mi_tupla) # Imprime la tupla (1, 2, 3, "Mundo", False) en la consola

#Tipo de dato diccionario (dict)
mi_diccionario = {"nombre": "Antonio", "edad": 25, "ciudad": "Madrid"}
print(mi_diccionario) # Imprime el diccionario {"nombre": "Antonio", "edad": 25, "ciudad": "Madrid"} en la consola

#con la funcion type() podemos verificar el tipo de dato de una variable
print(type(numero_entero)) # Imprime <class 'int'> en la consola
print(type(numero_flotante)) # Imprime <class 'float'> en la consola
print(type(mensaje)) # Imprime <class 'str'> en la consola
print(type(es_verdadero)) # Imprime <class 'bool'> en la consola
print(type(mi_lista)) # Imprime <class 'list'> en la consola
print(type(mi_tupla)) # Imprime <class 'tuple'> en la consola
print(type(mi_diccionario)) # Imprime <class 'dict'> en la consola
