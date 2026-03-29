#La refascctorización es el proceso de modificar el código fuente de un programa 
# para mejorar su estructura interna sin cambiar su comportamiento externo. 
# El objetivo principal de la refactorización es mejorar la legibilidad, 
# mantenibilidad y eficiencia del código, lo que facilita su comprensión y 
# modificación en el futuro.

#Ejemplo de refactorización: Supongamos que tenemos una función q
# ue calcula el área de un círculo, pero el código es difícil de entender y mantener.
import math
def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area                                     
#Código refactorizado: Podemos mejorar la legibilidad y mantenibilidad del 
# código al darle un nombre más descriptivo a la función y agregar comentarios. 
def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    
    Parámetros:
    radio (float): El radio del círculo.
    
    Retorna:
    float: El área del círculo.
    """
    area = math.pi * radio ** 2
    return area
#En este ejemplo, hemos agregado un docstring que explica claramente lo que hace la función,
# sus parámetros y su valor de retorno. Esto hace que el código sea más fácil de entender
# y mantener, ya que otros desarrolladores (o incluso nosotros mismos en el futuro) podrán
# comprender rápidamente la función sin tener que analizar el código en detalle.
