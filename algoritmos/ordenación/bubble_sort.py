#ALGORITMO DE ORDENACIÓN: BURBUJA - BUBBLE SORT

"""
El algoritmo de ordenación burbuja, también conocido como bubble sort,
es un algoritmo de ordenación sencillo que funciona comparando elementos 
adyacentes y permutándolos si están en el orden incorrecto. 
El proceso el proceso vuelve a repetirse hasta que la lista esta ordenada.
El algoritmo de ordenación burbuja es conocido por su simplicidad, 
pero no es eficiente para listas grandes, 
ya que su complejidad temporal es O(n^2) en el peor de los casos.
"""

def bubble_sort(arr):
    """
    Ejemplo de uso: 
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr)
    print(arr)-> [11, 12, 22, 25, 34, 64, 90]
    """

    """
    Explicación del código: 
    length: es una variable cuyo valor es el tamaño del array
    Pasos: 
    1-Bucle for con i tantos elementos igual al valor de length
    2-Bucle for j de 0 a length - i -1 
    3- Si arr[j] es mayor que arr[j+1] se cambian posiciones 
    """
    length = len (arr)
    for i in range(length):
        for j in range(0, length-i-1):#Bucle for para recorrer la lista 
            #desde el primer elemento hasta el elemento no ordenado
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]# Intercambia los elementos 
                # si el elemento encontrado es mayor que el siguiente
                # Esto se hace para ordenar la lista en orden ascendente
                #Se igualan los elementos para que el elemento mayor se mueva 
                # hacia el final de la lista


