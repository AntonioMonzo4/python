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