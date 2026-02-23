#FECHAS Y HORAS EN PYTHON 

from datetime import datetime, date, time, timedelta
#Crear un objeto de fecha   
fecha_actual = date.today()
print("Fecha actual:", fecha_actual)  # Imprime la fecha actual en formato YYYY-MM-DD
#Crear un objeto de hora
hora_actual = datetime.now().time()
print("Hora actual:", hora_actual)  # Imprime la hora actual en formato HH:MM:SS.microsegundos
#Crear un objeto de fecha y hora
fecha_hora_actual = datetime.now()
print("Fecha y hora actual:", fecha_hora_actual)  # Imprime la fecha y hora actual en formato YYYY-MM-DD HH:MM:SS.microsegundos
#Crear un objeto de fecha y hora a partir de una cadena
fecha_hora_str = "2024-08-15 14:30:00"
fecha_hora_obj = datetime.strptime(fecha_hora_str, "%Y-%m-%d %H:%M:%S")
print("Fecha y hora a partir de cadena:", fecha_hora_obj)  # Imprime "Fecha y hora a partir de cadena: 2024-08-15 14:30:00"
#Formatear un objeto de fecha y hora como una cadena
fecha_hora_formateada = fecha_hora_actual.strftime("%d/%m/%Y %H:%M:%S")
print("Fecha y hora formateada:", fecha_hora_formateada)  # Imprime la fecha y hora actual en formato DD/MM/YYYY HH:MM:SS
#Realizar operaciones con fechas y horas
fecha_futura = fecha_actual + timedelta(days=30)
print("Fecha dentro de 30 días:", fecha_futura)  # Imprime la fecha que será dentro de 30 días
fecha_pasada = fecha_actual - timedelta(days=30)
print("Fecha hace 30 días:", fecha_pasada)  # Imprime la fecha que fue hace 30 días

import re
#Ejemplo de uso de expresiones regulares para extraer fechas
texto = "La reunión es el 15/08/2024 y la fecha límite para entregar el informe es el 30/09/2024."
#Patrón para fechas en formato dd/mm/yyyy
patron_fecha = r"\b\d{2}/\d{2}/\d{4}\b"
fechas_encontradas = re.findall(patron_fecha, texto)
print("Fechas encontradas:", fechas_encontradas)  # Imprime "Fechas encontradas: ['15/08/2024', '30/09/2024']"

