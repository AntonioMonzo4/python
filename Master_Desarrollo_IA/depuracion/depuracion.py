#Depuración con print 
import logging #Importar el módulo de logging para una depuración más estructurada


def calcular_precio_con_descuento(precio_base,descuento):

    #El descuento debe ser un factor entre 0 y 1
    factor_descuentor = descuento / 100
    #Depuración: Verificar el valor del factor de descuento
    logging.debug(f"Factor de descuento calculado: {factor_descuentor}")

    #Depuración: Imprimir el factor de descuento para verificar su valor
    print(f"Factor de descuento calculado: {factor_descuentor}")
    #Fallo se esta sumando no restando el descuento
    logging.debug(f"Precio base: {precio_base}, Descuento: {descuento}, Factor de descuento: {factor_descuentor}")
    precio_final = precio_base * (1 + factor_descuentor)
    return precio_final

precio_producto = 100
descuento_producto = 20
precio_con_descuento = calcular_precio_con_descuento(precio_producto, descuento_producto)
print(f"Precio final con descuento: {precio_con_descuento}")
#Salida incorrecta: Precio final con descuento: 120.0


#Depuración interactiva 
#Concepto de depuración interactiva: Permite al desarrollador ejecutar el código 
# paso a paso y examinar el estado de las variables en tiempo real. 
# Esto se puede hacer utilizando herramientas de depuración integradas en 
# los entornos de desarrollo (IDEs) 
# o mediante la inserción de puntos de interrupción (breakpoints) en el código.