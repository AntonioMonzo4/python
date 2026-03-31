#Algoritmo búsqueda lineal - Linear Search
"""
Recorre una lista de elementos hasta encontra el valor buscado
"""
def linear_search(list, numero):
    for i in range(len(list)):
        if list[i]==numero:
            return i
        return "No se encuentra el valor: {numero} en esta lista."