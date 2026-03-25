#Errores y try catch 
edad_string = input("Ingrese su edad: ")

try:
    edad = int(edad_string)
    print(f"Su edad es: {edad}")    
except ValueError:
    print("Error: Debe ingresar un número válido para la edad.")

        