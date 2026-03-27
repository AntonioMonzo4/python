#Programación Orientada a Objetos (POO) es un paradigma de programación que se basa en el concepto de "objetos", 
# que son instancias de clases.
# Las clases son plantillas o moldes que definen las propiedades
# (atributos) y comportamientos (métodos) de los objetos que se crean a partir de ellas.
#lOS CUATRO PILARES DE LA POO SON:
#1. Encapsulamiento: ocultar los detalles internos de una clase y exponer solo lo necesario a través de métodos públicos.
#2. Abstracción: representar conceptos complejos de manera simplificada, enfocándose en los aspectos esenciales
#3. Herencia: permite crear una nueva clase (clase hija) que hereda atributos y métodos de una clase existente (clase padre).
#4. Polimorfismo: permite que diferentes clases puedan ser tratadas como instancias de una clase común, 
# lo que facilita la reutilización de código y la flexibilidad en el diseño de programas.


class Libro:
    #La palabra self se refiere a la instancia actual de la clase y se utiliza para acceder a los atributos y 
    # métodos de esa instancia.
    def __init__(self,titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.prestado = False

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            print(f"Has prestado '{self.titulo}' de {self.autor}.")
        else:
            print(f"Lo siento, '{self.titulo}' ya está prestado.")
    def devolver(self):
        if not self.prestado:
            print(f"'{self.titulo}' no está prestado.")
        else:
            self.prestado = False
            print(f"Has devuelto '{self.titulo}' de {self.autor}.")

#Encapsulamiento: ocultar los detalles internos de una clase y exponer solo lo necesario a través de métodos públicos.
#Abstracción: representar conceptos complejos de manera simplificada, enfocándose en los aspectos esenciales 
# y ocultando los detalles innecesarios.

#Ejemplos 
class CuentaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.__saldo = saldo_inicial  # Atributo privado

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Has depositado {cantidad}. Saldo actual: {self.__saldo}")
        else:
            print("La cantidad a depositar debe ser positiva.")

    def retirar(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            print(f"Has retirado {cantidad}. Saldo actual: {self.__saldo}")
        else:
            print("No tienes suficiente saldo o la cantidad es inválida.")

    def consultar_saldo(self):
        print(f"El saldo actual de la cuenta de {self.titular} es: {self.__saldo}")


#Herencia: permite crear una nueva clase (clase hija) que hereda atributos y
# métodos de una clase existente (clase padre).


class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def mostrar_info(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}")

class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)  # Llama al constructor de la clase padre
        self.puertas = puertas

    def mostrar_info(self):
        super().mostrar_info()  # Llama al método de la clase padre 
        print(f"Puertas: {self.puertas}")

#Polimorfismo: permite que diferentes clases puedan ser tratadas como instancias de una clase común, 
#lo que facilita la reutilización de código y la flexibilidad en el diseño de programas.
#Ejemplo de polimorfismo con una clase base y clases derivadas que implementan un método común:
# En este ejemplo, la clase base "Animal" tiene un método "hacer_sonido", 
# y las clases derivadas "Perro" y "Gato" implementan este método de manera diferente.
# Esto permite que podamos tratar a los objetos de ambas clases como instancias de la clase base "Animal" 
# y llamar al método "hacer_sonido" sin preocuparnos por la implementación específica de cada clase derivada.
#Overriding: es una característica de la programación orientada a objetos 
# que permite a una clase hija proporcionar una implementación específica de 
# un método que ya está definido en su clase padre.

class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    #Ejemplo de overriding: la clase Perro proporciona su propia implementación del método hacer_sonido,
    # que anula la implementación vacía de la clase base Animal.
    def hacer_sonido(self):
        print("Guau!")

class Gato(Animal):
    #Ejemplo de overriding: la clase Gato proporciona su propia implementación del método hacer_sonido,
    # que anula la implementación vacía de la clase base Animal.
    def hacer_sonido(self):
        print("Miau!")



libro_1 = Libro("1984", "George Orwell")
print(libro_1.titulo)
print(libro_1.autor)
print(libro_1.prestado)