#Un entorno virtual es una copia aislada del entorno de Python que permite instalar paquetes y dependencias sin afectar al sistema global.
#Esto es especialmente útil para evitar conflictos entre diferentes proyectos que pueden requerir diferentes versiones de paquetes
#Para crear un entorno virtual, puedes usar el módulo venv que viene incluido con Python.
#Para crear un entorno virtual, abre una terminal y navega al directorio de tu proyecto, luego ejecuta el siguiente comando:
#python -m venv nombre_del_entorno
#Esto creará un nuevo directorio llamado "nombre_del_entorno" que contiene una copia aislada de Python y sus paquetes.
#Para activar el entorno virtual, ejecuta el siguiente comando:
#En Windows:
#nombre_del_entorno\Scripts\activate
#En macOS/Linux:
#source nombre_del_entorno/bin/activate
#Una vez que el entorno virtual esté activado, puedes instalar paquetes usando pip sin afectar al sistema global. Por ejemplo:
#pip install nombre_del_paquete
#Para desactivar el entorno virtual, simplemente ejecuta el comando:
#deactivate


#Comandos útiles para gestionar dependencias en Python:

#python3 -m venv nombre_del_entorno --> normalmente .venv o env 
#para activar en windows: .\nombre_del_entorno\Scripts\activate
#para activar en macOS/Linux: source nombre_del_entorno/bin/activate


#GESTOR DE PAQUETES Y REQUISITOS 
#un paquete es una colección de módulos de Python que se pueden instalar y usar en tus proyectos.
#pip es el gestor de paquetes oficial de Python que se utiliza para instalar y gestionar paquetes de Python.
#Para instalar un paquete usando pip, puedes usar el siguiente comando:
#pip install nombre_del_paquete
#Para instalar una versión específica de un paquete, puedes usar el siguiente comando:
#pip install nombre_del_paquete==version
#Para actualizar un paquete a la última versión, puedes usar el siguiente comando:
#pip install --upgrade nombre_del_paquete
#Para desinstalar un paquete, puedes usar el siguiente comando:
#pip uninstall nombre_del_paquete
#Para guardar las dependencias de tu proyecto en un archivo de requisitos, puedes usar el siguiente comando:
#pip freeze > requirements.txt
#Esto creará un archivo llamado requirements.txt que contiene una lista de todas las dependencias de tu proyecto y sus versiones.
#Para instalar las dependencias de tu proyecto desde un archivo de requisitos, puedes usar el siguiente comando:
#pip install -r requirements.txt
#pip list --> muestra una lista de todos los paquetes instalados en el entorno virtual junto con sus versiones.


