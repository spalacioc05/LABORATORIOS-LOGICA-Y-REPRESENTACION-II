"""
Laboratorio 1 Listas, Pilas y Colas

Ejercicio 1
Utiliza una lista simplemente enlazada para crear una estructura de 25 nodos,
cada uno conteniendo un número aleatorio entre 1 y 30. Una vez generada la lista enlazada,
construye una pila en la que los números pares se coloquen en la parte inferior y los impares en la parte superior.

1015066047 - Sarai Restrepo Rodriguez
1045076775 - Santiago Palacio Cardenas
"""

import random


class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None


class LSL:
    def __init__(self):
        self.cabecera = None

    def insertar_valor(self, valor):  # Método para insertar nodos a la lista
        nuevo_nodo = Nodo(valor)
        if self.cabecera is None:
            self.cabecera = nuevo_nodo
        else:
            nodo_actual = self.cabecera
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def imprimir_lista(self):  # Método para imprimir los elementos de la lista
        nodo_actual = self.cabecera
        while nodo_actual is not None:
            print(nodo_actual.valor, end=" -> ")
            nodo_actual = nodo_actual.siguiente
        print("None")


class Pila:
    def __init__(self, tam):
        self.V = []
        self.cima = -1
        self.tam = tam

    def pila_llena(self):  # Verificamos si la pila esta llena o vacia
        return self.cima == self.tam - 1

    def apilar(self, valor):  # Método para apilar
        if self.pila_llena():  # Verificamos que la pila o este llena
            print("La pila esta llena, solo podemos apilar 25 objetos a la vez.\n")
            # Si la pila esta llena, elevamos un error para que el programa pueda empezar a imprimir los valores apilados
            raise ValueError("Error")
        else:
            # Aumentamos el valor de cima para poder usar el metodo de pila llena
            self.cima = self.cima + 1
            self.V.append(valor)

    def imprimir_pila(self):
        # Usamos el reversed como un metodo similar al .peek de las pilas, para ver los elementos sin necesidad de desapilar
        for V in reversed(self.V):
            print(f"| {V} |")
            print(" --- ")


lsl = LSL()
for i in range(25):
    lsl.insertar_valor(random.randint(1, 30))

print("LSL\n")
lsl.imprimir_lista()
print(
    "\n---------------------------------------------------------------------------------------------------------------------------------------------------\n")

pila = Pila(25)
nodo_actual = lsl.cabecera

try:
    # Vamos a apilar los elementos de la lista que sean números pares
    while nodo_actual is not None:
        if nodo_actual.valor % 2 == 0:
            pila.apilar(nodo_actual.valor)
        nodo_actual = nodo_actual.siguiente

    nodo_actual = lsl.cabecera

    # Vamos a apilar los elementos de la lista que sean números impares
    while nodo_actual is not None:
        if nodo_actual.valor % 2 != 0:
            pila.apilar(nodo_actual.valor)
        nodo_actual = nodo_actual.siguiente

    print("Pila (numeros pares abajo, impares arriba):\n")
    pila.imprimir_pila()

except:  # Aquí "atrapamos" el error en caso de que la pila este llena
    print("Pila (numeros pares abajo, impares arriba):\n")
    pila.imprimir_pila()
