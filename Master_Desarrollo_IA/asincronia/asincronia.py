#Asincronia
import asyncio
import time

async def pedir_cafe():
    print("Pidiendo café...")
    
    await asyncio.sleep(5)  # Simula el tiempo que tarda en preparar el café
    # time.sleep(2)  # Simula el tiempo que tarda en preparar el café
    print("Café listo!")
    return "Café"

async def main():

    inicio = time.time() # Marca el inicio del tiempo
    await asyncio.gather(# gather permite ejecutar varias tareas de manera concurrente
                        pedir_cafe(),
                        pedir_cafe(),
                        pedir_cafe()
                         )  # Espera a que se prepare el café

    fin = time.time() # Calcula el tiempo transcurrido
    print(f"Tiempo transcurrido: {fin - inicio:.2f} segundos")


asyncio.run(main())

#Cuando usar asincronía:
#1. Operaciones de E/S: La asincronía es especialmente útil para operaciones de entrada/salida (E/S), 
# como leer o escribir archivos, hacer solicitudes a una API, o interactuar con bases de datos.
#2. Tareas concurrentes: Si tienes varias tareas que pueden ejecutarse de manera concurrente,
# como descargar múltiples archivos o procesar varias solicitudes al mismo tiempo, la asincronía puede mejorar el rendimiento.
#3. Interfaz de usuario: En aplicaciones con interfaces de usuario, la asincronía puede ayudar a mantener la 
# interfaz receptiva mientras se realizan tareas en segundo plano.
#4. Procesamiento de datos: Si estás procesando grandes cantidades de datos o realizando 
# cálculos intensivos, la asincronía puede permitir que otras tareas se ejecuten mientras se espera a que se completen los cálculos.
#5. Aplicaciones web: En el desarrollo de aplicaciones web, la asincronía es fundamental para 
# manejar múltiples solicitudes de clientes de manera eficiente y mejorar la experiencia del usuario.
#En general, la asincronía es útil cuando tienes tareas que pueden beneficiarse de la ejecución concurrente
#  o cuando quieres mejorar la eficiencia y la capacidad de respuesta de tu aplicación.