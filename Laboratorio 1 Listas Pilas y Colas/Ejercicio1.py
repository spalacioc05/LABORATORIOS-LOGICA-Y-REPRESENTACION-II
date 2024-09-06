"""
Ejercicio 1
Utiliza una lista simplemente enlazada para crear una estructura de 25 nodos,
cada uno conteniendo un número aleatorio entre 1 y 30. Una vez generada la lista enlazada,
construye una pila en la que los números pares se coloquen en la parte inferior y los impares en la parte superior. 
"""

import random

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class LSL:
    def __init__(self):
        self.cabecera = None

    def insertar_valor(self, valor):
        nuevo_nodo = Nodo(valor)
        if self.cabecera is None:
            self.cabecera = nuevo_nodo
        else:
            nodo_actual = self.cabecera
            while nodo_actual.siguiente is not None:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
    
    def imprimir_lista(self):
        nodo_actual = self.cabecera
        while nodo_actual is not None:
            print(nodo_actual.valor, end=" -> ")
            nodo_actual = nodo_actual.siguiente
        print("None")


class Pila:
    def __init__(self, tam):
        self.V = LSL()
        self.tope = -1
        self.tam = tam
        
    def pila_vacia(self):
        return self.tope < 0

    def pila_llena(self):
        return self.tope == self.tam - 1

    def apilar(self, valor):
        if self.pila_llena():
            print("La pila esta llena, solo podemos apilar 25 objetos a la vez.")
            raise ValueError("Error")
        else:
            self.tope = self.tope + 1
            self.V.insertar_valor(valor)

    def imprimir_pila(self):
        # Reverse the linked list
        prev = None
        current = self.V.cabecera
        while current is not None:
            nuevo_nodo = current.siguiente
            current.siguiente = prev
            prev = current
            current = nuevo_nodo
        
        # Print the reversed linked list
        nodo_actual = prev
        while nodo_actual is not None:
            print(f"| {nodo_actual.valor} |")
            print(" --- ")
            nodo_actual = nodo_actual.siguiente


lista = LSL()
for i in range(8): 
    lista.insertar_valor(random.randint(1, 30))

print("LSL")
lista.imprimir_lista()
print("------------------------------------------------------------------------------------------------------------------------------------------------")

pila = Pila(25)
nodo_actual = lista.cabecera

try:
    while nodo_actual is not None:
        if nodo_actual.valor % 2 == 0:
            pila.apilar(nodo_actual.valor)
        nodo_actual = nodo_actual.siguiente

    nodo_actual = lista.cabecera

    while nodo_actual is not None:
        if nodo_actual.valor % 2 != 0:
            pila.apilar(nodo_actual.valor)
        nodo_actual = nodo_actual.siguiente

    print("Pila (numeros pares abajo, impares arriba):")
    pila.imprimir_pila()

except:
    print("Pila (numeros pares abajo, impares arriba):")
    pila.imprimir_pila()